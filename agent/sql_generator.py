"""Groq SQL generation over the curated, safe cleaned-schema views."""

from __future__ import annotations

import re
import os
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Protocol

from sqlalchemy import text

from ._config import DATABASE_URL
from .sql_safety import ALLOWED_VIEWS, SafeSQLExecutor, SqlResult

VIEW_DESCRIPTIONS = {
    "cleaned.v_performance_latest": "One latest snapshot per individual client; group rollups are excluded.",
    "cleaned.v_performance_latest_group": "One latest performance snapshot per client group; client_id is NULL on source group rows.",
    "cleaned.v_performance_history": "All client and group performance snapshots over time; grain is one source row.",
    "cleaned.dim_client": "One aggregate row per client across investment, performance, and meeting sources.",
    "cleaned.dim_group": "One aggregate row per client_group_id across investments, group performance, and meetings.",
    "cleaned.dim_deal": "One aggregate row per deal across its investment rows.",
    "cleaned.dim_rm": "One aggregate row per relationship manager across investment rows.",
    "cleaned.fact_investment": "Investment/capital-call source grain; aggregate before joining to multi-snapshot performance or meetings.",
    "cleaned.v_meetings": "One row per meeting with structured metadata, summary, attendees, and action items.",
}

COLUMN_DESCRIPTIONS = {
    "client_id": "Canonical client identifier. Joins client facts across tables.",
    "client_group_id": "Client's group identifier; group rollups live in v_performance_latest_group.",
    "group_id": "Canonical client group identifier.",
    "as_of_date": "Performance snapshot date. Report it with every performance metric.",
    "ci_current_irr": "Current corporate-investments IRR stored as a decimal.",
    "ci_total_irr": "Corporate-investments total IRR stored as a decimal.",
    "cop_total_irr": "Credit-opportunities total IRR stored as a decimal.",
    "total_aum_amount": "Total assets under management in USD.",
    "investment_amount_usd": "USD-normalized investment amount; use for aggregation.",
    "investment_amount_natural_currency": "Original-currency amount; do not sum across currencies.",
    "nam_lob": "Line-of-business name. The redundant LOB code was dropped during cleaning.",
    "account_rm": "Relationship manager name.",
    "meeting_date": "Date the meeting took place.",
    "summary": "Narrative meeting notes.",
    "action_items": "Meeting action items as a text array.",
}


class TextGenerator(Protocol):
    def generate(self, prompt: str) -> str: ...


@dataclass
class MultiSqlResult:
    """Result of executing multiple SQL queries."""
    results: Dict[str, SqlResult]  # key -> SqlResult


def _schema_card(engine) -> str:
    views = sorted(ALLOWED_VIEWS)
    query = text("""
        SELECT table_schema, table_name, column_name, data_type
        FROM information_schema.columns
        WHERE table_schema = 'cleaned' AND table_name = ANY(:view_names)
        ORDER BY table_name, ordinal_position
    """)
    view_names = [view.split(".", 1)[1] for view in views]
    with engine.connect() as connection:
        rows = connection.execute(query, {"view_names": view_names}).mappings().all()
    grouped: Dict[str, list[str]] = {view: [] for view in views}
    for row in rows:
        view = f"{row['table_schema']}.{row['table_name']}"
        description = COLUMN_DESCRIPTIONS.get(row["column_name"], "")
        suffix = f" — {description}" if description else ""
        grouped[view].append(f"  - {row['column_name']} ({row['data_type']}){suffix}")
    return "\n".join(
        f"{view}: {VIEW_DESCRIPTIONS[view]}\n" + "\n".join(grouped[view])
        for view in views if grouped[view]
    )


def _strip_sql_fence(value: str) -> str:
    match = re.fullmatch(r"\s*```(?:sql)?\s*(.*?)\s*```\s*", value, flags=re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else value.strip()


class SQLGenerator:
    """Generate, validate, and execute SQL queries."""

    def __init__(
        self,
        llm: TextGenerator,
        db_url: str = DATABASE_URL,
        executor: Optional[SafeSQLExecutor] = None,
        max_repair_attempts: int = 2,
    ):
        if max_repair_attempts < 0:
            raise ValueError("max_repair_attempts cannot be negative")
        self.llm = llm
        self.executor = executor or SafeSQLExecutor(os.getenv("AGENT_RO_URL", db_url))
        self.schema_card = _schema_card(self.executor.engine)
        self.max_repair_attempts = max_repair_attempts

    def run(
        self,
        question: str,
        params: Optional[Dict[str, Any]] = None,
        resolved_entities: Optional[Dict[str, str]] = None,
    ) -> SqlResult:
        """Run a single SQL query (backward compatible)."""
        return self._run_single(question, params, resolved_entities)

    def run_structured(
        self,
        question: str,
        params: Optional[Dict[str, Any]] = None,
        resolved_entities: Optional[Dict[str, str]] = None,
    ) -> SqlResult:
        """Run SQL for structured data (performance, investments)."""
        return self._run_single(question, params, resolved_entities, query_type="structured")

    def run_meetings(
        self,
        question: str,
        params: Optional[Dict[str, Any]] = None,
        resolved_entities: Optional[Dict[str, str]] = None,
    ) -> SqlResult:
        """Run SQL for meeting data."""
        return self._run_single(question, params, resolved_entities, query_type="meetings")

    def _run_single(
        self,
        question: str,
        params: Optional[Dict[str, Any]] = None,
        resolved_entities: Optional[Dict[str, str]] = None,
        query_type: str = "auto",
    ) -> SqlResult:
        parameters = dict(params or {})
        entities = dict(resolved_entities or {})
        
        type_guidance = {
            "structured": "Use performance/investment views (v_performance_latest, v_performance_latest_group, v_performance_history, dim_client, dim_group, dim_deal, dim_rm, fact_investment). Do NOT use v_meetings.",
            "meetings": "Use only cleaned.v_meetings view. Do NOT join with performance or investment views.",
            "auto": "Use appropriate views based on the question."
        }
        
        few_shot_examples = """
=== FEW-SHOT EXAMPLES ===

-- 1. Simple performance query (client)
Question: What is the current CI total IRR for client A12345?
Parameters: {"client_id": "A12345"}
SQL:
SELECT client_id, client_name, as_of_date, ci_total_irr, ci_total_moic, total_aum_amount
FROM cleaned.v_performance_latest
WHERE client_id = :client_id;

-- 2. Simple performance query (group)
Question: What is the current IRR for group 346?
Parameters: {"group_id": 346}
SQL:
SELECT client_group_id, ci_total_irr, ci_total_moic, total_aum_amount, as_of_date
FROM cleaned.v_performance_latest_group
WHERE client_group_id = :group_id;

-- 3. Performance history / trend
Question: Show IRR trend for client A12345 over last 4 snapshots
Parameters: {"client_id": "A12345"}
SQL:
SELECT as_of_date, ci_current_irr, ci_total_irr, total_aum_amount
FROM cleaned.v_performance_history
WHERE client_id = :client_id
ORDER BY as_of_date DESC
LIMIT 4;

-- 4. Investment total for group
Question: Show total invested for group 346
Parameters: {"group_id": 346}
SQL:
SELECT :group_id AS group_id, SUM(investment_amount_usd) AS total_invested_usd
FROM cleaned.fact_investment
WHERE client_group_id = :group_id;

-- 5. Investment total for deal
Question: What is the total invested for deal DL100000?
Parameters: {"deal_id": "DL100000"}
SQL:
SELECT deal_id, deal_name, SUM(investment_amount_usd) AS total_invested_usd
FROM cleaned.fact_investment
WHERE deal_id = :deal_id
GROUP BY deal_id, deal_name;

-- 6. Deals for a client with LOB and invested amount
Question: Show all deals for client A12345 with deal names, LOB, and total invested per deal
Parameters: {"client_id": "A12345"}
SQL:
SELECT fi.deal_id, di.deal_name, di.lob_name, SUM(fi.investment_amount_usd) AS total_invested_usd,
       MIN(fi.min_invested_date) AS first_investment, MAX(fi.min_invested_date) AS last_investment
FROM cleaned.fact_investment fi
JOIN cleaned.dim_deal di ON fi.deal_id = di.deal_id
WHERE fi.client_id = :client_id
GROUP BY fi.deal_id, di.deal_name, di.lob_name
ORDER BY total_invested_usd DESC;

-- 7. Two-table join: Client IRR + total invested (group level)
Question: For each client in group 346, show their latest IRR and total invested amount
Parameters: {"group_id": 346}
SQL:
SELECT c.client_id, c.display_name, p.ci_total_irr AS latest_irr, p.as_of_date,
       c.total_invested_usd
FROM cleaned.dim_client c
JOIN cleaned.v_performance_latest p ON c.client_id = p.client_id
WHERE c.group_id = :group_id
ORDER BY c.client_id;

-- 8. Two-table join: Client + Group performance
Question: Show client A12345 performance and their group performance
Parameters: {"client_id": "A12345", "group_id": 346}
SQL:
SELECT 'client' AS level, p.client_id, p.client_name, p.as_of_date,
       p.ci_total_irr, p.ci_total_moic, p.total_aum_amount
FROM cleaned.v_performance_latest p
WHERE p.client_id = :client_id
UNION ALL
SELECT 'group' AS level, p.client_group_id AS client_id, NULL AS client_name, p.as_of_date,
       p.ci_total_irr, p.ci_total_moic, p.total_aum_amount
FROM cleaned.v_performance_latest_group p
WHERE p.client_group_id = :group_id;

-- 9. Three-table join: RM -> Client -> Performance
Question: List all clients managed by Carlos Gomez with their latest IRR and total invested
Parameters: {"rm_name": "Carlos Gomez"}
SQL:
SELECT c.client_id, c.display_name, p.ci_total_irr AS latest_irr, p.as_of_date,
       c.total_invested_usd
FROM cleaned.dim_client c
JOIN cleaned.v_performance_latest p ON c.client_id = p.client_id
WHERE c.rm_name ILIKE :rm_name
ORDER BY c.total_invested_usd DESC;

-- 10. Three-table join: Performance + Investments + Meetings (hybrid filter)
Question: Show meetings for deals where client A12345's IRR is negative
Parameters: {"client_id": "A12345"}
SQL:
WITH negative_irr_deals AS (
    SELECT DISTINCT fi.deal_id, di.deal_name
    FROM cleaned.fact_investment fi
    JOIN cleaned.dim_deal di ON fi.deal_id = di.deal_id
    JOIN cleaned.v_performance_latest vp ON fi.client_id = vp.client_id
    WHERE fi.client_id = :client_id AND vp.ci_total_irr < 0
)
SELECT m.meeting_id, m.meeting_date, m.company, m.summary, m.attendees, m.action_items
FROM cleaned.v_meetings m
JOIN negative_irr_deals nid ON m.company ILIKE '%' || nid.deal_name || '%'
    OR m.summary ILIKE '%' || nid.deal_name || '%'
WHERE m.client_id = :client_id
ORDER BY m.meeting_date DESC
LIMIT 20;

-- 11. Meeting SQL with exact filters (date + company)
Question: Show meeting on 9th January 2022 with Orchid Ventures
Parameters: {"meeting_date": "2022-01-09", "company": "Orchid Ventures"}
SQL:
SELECT meeting_id, meeting_date, company, sector, region, investment_stage,
       summary, attendees, action_items
FROM cleaned.v_meetings
WHERE meeting_date = :meeting_date
  AND company ILIKE :company
ORDER BY meeting_date DESC
LIMIT 20;

-- 12. Meeting SQL with company filter only
Question: Summarize meetings for Orchid Ventures
Parameters: {"company": "Orchid Ventures"}
SQL:
SELECT meeting_id, meeting_date, company, sector, region, investment_stage,
       summary, attendees, action_items
FROM cleaned.v_meetings
WHERE company ILIKE :company
ORDER BY meeting_date DESC
LIMIT 20;

-- 13. Meeting SQL with attendee filter
Question: What meetings did Rahul Mehta attend?
Parameters: {"attendee": "Rahul Mehta"}
SQL:
SELECT meeting_id, meeting_date, company, sector, region, investment_stage,
       summary, attendees, action_items
FROM cleaned.v_meetings
WHERE :attendee = ANY(attendees)
ORDER BY meeting_date DESC
LIMIT 20;

-- 14. Meeting SQL with date range
Question: Show all meetings for group 346 in 2024
Parameters: {"group_id": 346, "date_from": "2024-01-01", "date_to": "2024-12-31"}
SQL:
SELECT meeting_id, meeting_date, company, sector, region, investment_stage,
       summary, attendees, action_items
FROM cleaned.v_meetings
WHERE group_id = :group_id
  AND meeting_date >= :date_from
  AND meeting_date <= :date_to
ORDER BY meeting_date DESC
LIMIT 20;

-- 15. Aggregation: RM with most clients
Question: Which RM manages the most clients?
SQL:
SELECT rm_name, client_count
FROM cleaned.dim_rm
ORDER BY client_count DESC
LIMIT 1;

-- 16. Aggregation: Total AUM by RM
Question: What is the total AUM across all clients managed by each RM?
SQL:
SELECT c.rm_name, SUM(p.total_aum_amount) AS total_aum
FROM cleaned.dim_client c
JOIN cleaned.v_performance_latest p ON c.client_id = p.client_id
WHERE c.rm_name IS NOT NULL
GROUP BY c.rm_name
ORDER BY total_aum DESC;

-- 17. Cross-table: Clients with investments but no performance data
Question: Which clients have investments but no performance data?
SQL:
SELECT fi.client_id, c.display_name
FROM cleaned.fact_investment fi
JOIN cleaned.dim_client c ON fi.client_id = c.client_id
LEFT JOIN cleaned.v_performance_latest vp ON fi.client_id = vp.client_id
WHERE vp.client_id IS NULL
GROUP BY fi.client_id, c.display_name;

-- 18. Temporal: Quarter fundraising trend
Question: Show quarterly fundraising for group 346 in 2024
Parameters: {"group_id": 346}
SQL:
SELECT date_trunc('quarter', as_of_date) AS quarter,
       SUM(ci_cy_fr_amount) AS total_fundraising
FROM cleaned.v_performance_history
WHERE client_group_id = :group_id
  AND as_of_date >= '2024-01-01' AND as_of_date <= '2024-12-31'
GROUP BY date_trunc('quarter', as_of_date)
ORDER BY quarter;

=== END EXAMPLES ===
"""
        
        base_prompt = f"""You are an analytics engineer writing PostgreSQL SELECT queries.
Return only one SQL SELECT statement, optionally inside a sql code fence.
Use only the allowlisted views in this schema card. Never query base tables.
Use named bind parameters for supplied canonical entity values. Available binds:
{parameters}
Resolved entity ground truth:
{entities}

Query type: {query_type}
{type_guidance.get(query_type, type_guidance["auto"])}

{few_shot_examples}

Data rules:
- IRR columns are decimals (0.0364 means 3.64%); compare percent requests to their decimal value.
- Money aggregation uses investment_amount_usd, not natural-currency amounts.
- Current client performance comes from cleaned.v_performance_latest.
- Group performance comes from cleaned.v_performance_latest_group; do not treat NULL client_id group rows as one client.
- History questions use cleaned.v_performance_history.
- Aggregate fact tables to the requested entity grain before joining; never join raw investment rows to multiple performance snapshots without pre-aggregation.
- Include as_of_date whenever reporting performance metrics.
- For meeting queries: ORDER BY meeting_date DESC, LIMIT 20.
- For structured queries: LIMIT 200 or less.

Schema card:
{self.schema_card}

Question: {question}
"""
        previous_sql = ""
        previous_error = ""
        for attempt in range(self.max_repair_attempts + 1):
            prompt = base_prompt
            if previous_error:
                prompt += (
                    f"\nPrevious SQL:\n{previous_sql}\n"
                    f"Validation/execution error:\n{previous_error}\n"
                    "Repair it. Return only the corrected SQL."
                )
            sql = _strip_sql_fence(self.llm.generate(prompt))
            validation = self.executor.validate(sql)
            if not validation.ok:
                previous_sql = sql
                previous_error = validation.reason or "SQL rejected"
                continue
            try:
                return self.executor.execute(sql, parameters)
            except Exception as exc:
                previous_sql = sql
                previous_error = str(exc)

        return SqlResult(
            sql=previous_sql,
            columns=[],
            rows=[],
            row_count=0,
            truncated=False,
            elapsed_ms=0,
            error=previous_error or "SQL generation failed",
        )