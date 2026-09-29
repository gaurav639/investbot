"""Create deterministic cross-table views in the existing cleaned schema."""

from sqlalchemy import create_engine, text

from .config import DATABASE_URL

SEMANTIC_VIEWS = (
    """
    CREATE OR REPLACE VIEW cleaned.v_performance_history AS
    SELECT * FROM cleaned.performance_data
    """,
    """
    CREATE OR REPLACE VIEW cleaned.v_performance_latest AS
    SELECT * FROM (
        SELECT p.*,
               ROW_NUMBER() OVER (
                   PARTITION BY p.client_id
                   ORDER BY p.as_of_date DESC NULLS LAST, p.source_row_num DESC
               ) AS rn
        FROM cleaned.performance_data AS p
        WHERE p.isgroup_flag IS FALSE AND p.client_id IS NOT NULL
    ) AS ranked
    WHERE rn = 1
    """,
    """
    CREATE OR REPLACE VIEW cleaned.v_performance_latest_group AS
    SELECT * FROM (
        SELECT p.*,
               ROW_NUMBER() OVER (
                   PARTITION BY p.client_group_id
                   ORDER BY p.as_of_date DESC NULLS LAST, p.source_row_num DESC
               ) AS rn
        FROM cleaned.performance_data AS p
        WHERE p.isgroup_flag IS TRUE AND p.client_group_id IS NOT NULL
    ) AS ranked
    WHERE rn = 1
    """,
    """
    CREATE OR REPLACE VIEW cleaned.dim_client AS
    WITH inv AS (
        SELECT client_id,
               mode() WITHIN GROUP (ORDER BY client_name)
                   FILTER (WHERE client_name IS NOT NULL) AS display_name,
               mode() WITHIN GROUP (ORDER BY client_group_id)
                   FILTER (WHERE client_group_id IS NOT NULL) AS group_id,
               mode() WITHIN GROUP (ORDER BY account_rm)
                   FILTER (WHERE account_rm IS NOT NULL) AS rm_name,
               mode() WITHIN GROUP (ORDER BY account_rm_email)
                   FILTER (WHERE account_rm_email IS NOT NULL) AS rm_email,
               mode() WITHIN GROUP (ORDER BY client_status)
                   FILTER (WHERE client_status IS NOT NULL) AS status,
               COUNT(DISTINCT deal_id) AS deal_count,
               SUM(investment_amount_usd) AS total_invested_usd,
               MIN(min_invested_date) AS first_investment_date,
               MAX(min_invested_date) AS last_investment_date
        FROM cleaned.investments_data
        WHERE client_id IS NOT NULL
        GROUP BY client_id
    ),
    perf AS (
        SELECT client_id,
               mode() WITHIN GROUP (ORDER BY client_name)
                   FILTER (WHERE client_name IS NOT NULL) AS display_name,
               mode() WITHIN GROUP (ORDER BY client_group_id)
                   FILTER (WHERE client_group_id IS NOT NULL) AS group_id
        FROM cleaned.performance_data
        WHERE isgroup_flag IS FALSE AND client_id IS NOT NULL
        GROUP BY client_id
    ),
    meetings AS (
        SELECT client_id,
               COUNT(*) AS meeting_count,
               MAX(meeting_date) AS last_meeting_date
        FROM cleaned.meeting_notes
        WHERE client_id IS NOT NULL
        GROUP BY client_id
    ),
    ids AS (
        SELECT client_id FROM cleaned.investments_data WHERE client_id IS NOT NULL
        UNION
        SELECT client_id FROM cleaned.performance_data
        WHERE isgroup_flag IS FALSE AND client_id IS NOT NULL
        UNION
        SELECT client_id FROM cleaned.meeting_notes WHERE client_id IS NOT NULL
    )
    SELECT ids.client_id,
           COALESCE(inv.display_name, perf.display_name, 'Client ' || ids.client_id)
               AS display_name,
           COALESCE(inv.group_id, perf.group_id) AS group_id,
           inv.rm_name, inv.rm_email, inv.status, inv.deal_count,
           inv.total_invested_usd, inv.first_investment_date,
           inv.last_investment_date,
           COALESCE(meetings.meeting_count, 0) AS meeting_count,
           meetings.last_meeting_date
    FROM ids
    LEFT JOIN inv USING (client_id)
    LEFT JOIN perf USING (client_id)
    LEFT JOIN meetings USING (client_id)
    """,
    """
    CREATE OR REPLACE VIEW cleaned.dim_group AS
    WITH inv AS (
        SELECT client_group_id AS group_id,
               COUNT(DISTINCT client_id) AS client_count,
               COUNT(DISTINCT deal_id) AS deal_count,
               SUM(investment_amount_usd) AS total_invested_usd,
               MIN(min_invested_date) AS first_investment_date,
               MAX(min_invested_date) AS last_investment_date
        FROM cleaned.investments_data
        WHERE client_group_id IS NOT NULL
        GROUP BY client_group_id
    ),
    meetings AS (
        SELECT group_id, COUNT(*) AS meeting_count, MAX(meeting_date) AS last_meeting_date
        FROM cleaned.meeting_notes
        WHERE group_id IS NOT NULL
        GROUP BY group_id
    ),
    ids AS (
        SELECT client_group_id AS group_id FROM cleaned.investments_data
        WHERE client_group_id IS NOT NULL
        UNION
        SELECT client_group_id FROM cleaned.performance_data
        WHERE isgroup_flag IS TRUE AND client_group_id IS NOT NULL
        UNION
        SELECT group_id FROM cleaned.meeting_notes WHERE group_id IS NOT NULL
    )
    SELECT ids.group_id,
           COALESCE(inv.client_count, 0) AS client_count,
           COALESCE(inv.deal_count, 0) AS deal_count,
           inv.total_invested_usd, inv.first_investment_date,
           inv.last_investment_date,
           perf.as_of_date AS performance_as_of_date,
           perf.ci_total_irr, perf.ci_total_moic, perf.total_aum_amount,
           COALESCE(meetings.meeting_count, 0) AS meeting_count,
           meetings.last_meeting_date
    FROM ids
    LEFT JOIN inv USING (group_id)
    LEFT JOIN cleaned.v_performance_latest_group AS perf
        ON perf.client_group_id = ids.group_id
    LEFT JOIN meetings USING (group_id)
    """,
    """
    CREATE OR REPLACE VIEW cleaned.dim_deal AS
    SELECT deal_id,
           mode() WITHIN GROUP (ORDER BY deal_name)
               FILTER (WHERE deal_name IS NOT NULL) AS deal_name,
           mode() WITHIN GROUP (ORDER BY nam_lob)
               FILTER (WHERE nam_lob IS NOT NULL) AS lob_name,
           COUNT(DISTINCT client_id) AS client_count,
           SUM(investment_amount_usd) AS total_invested_usd,
           MIN(min_invested_date) AS first_investment_date,
           MAX(min_invested_date) AS last_investment_date
    FROM cleaned.investments_data
    WHERE deal_id IS NOT NULL
    GROUP BY deal_id
    """,
    """
    CREATE OR REPLACE VIEW cleaned.dim_rm AS
    SELECT account_rm AS rm_name,
           ARRAY_AGG(DISTINCT account_rm_email)
               FILTER (WHERE account_rm_email IS NOT NULL) AS emails,
           COUNT(DISTINCT client_id) AS client_count,
           COUNT(DISTINCT deal_id) AS deal_count,
           SUM(investment_amount_usd) AS total_invested_usd
    FROM cleaned.investments_data
    WHERE account_rm IS NOT NULL
    GROUP BY account_rm
    """,
    """
    CREATE OR REPLACE VIEW cleaned.fact_investment AS
    SELECT source_row_num, client_id, client_name, client_group_id, deal_id,
           capital_call_id, deal_name, nam_lob, investment_amount_usd,
           investment_amount_natural_currency, natural_currency_code,
           investment_exchange_rate, min_invested_date, is_realised,
           client_status, account_name, account_rm, account_rm_email, rm_alias
    FROM cleaned.investments_data
    """,
    """
    CREATE OR REPLACE VIEW cleaned.v_meetings AS
    SELECT meeting_id, meeting_date, company, sector, region, investment_stage,
           deal_size_estimate, client_id, group_id, attendees_arr AS attendees,
           action_items_arr AS action_items, summary,
           CARDINALITY(action_items_arr) AS action_item_count
    FROM cleaned.meeting_notes
    """,
)


def build_semantic_views(db_url: str = DATABASE_URL) -> None:
    """Build or replace cross-table views while keeping one cleaned schema."""
    engine = create_engine(db_url)
    with engine.begin() as connection:
        connection.execute(text("CREATE EXTENSION IF NOT EXISTS pg_trgm"))
        for statement in SEMANTIC_VIEWS:
            connection.execute(text(statement))


def main() -> None:
    build_semantic_views()
    print("Semantic views created in the cleaned schema")


if __name__ == "__main__":
    main()