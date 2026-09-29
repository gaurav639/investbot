"""Validate and execute read-only SQL against curated cleaned-schema views."""

from __future__ import annotations

import os
import time
from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from typing import Any, Dict, Optional

import sqlglot
from sqlglot import exp
from sqlalchemy import create_engine, text

from ._config import DATABASE_URL

READONLY_URL = os.getenv("AGENT_RO_URL", DATABASE_URL)
ALLOWED_VIEWS = frozenset({
    "cleaned.v_performance_latest",
    "cleaned.v_performance_latest_group",
    "cleaned.v_performance_history",
    "cleaned.dim_client",
    "cleaned.dim_group",
    "cleaned.dim_deal",
    "cleaned.dim_rm",
    "cleaned.fact_investment",
    "cleaned.v_meetings",
})
FORBIDDEN_FUNCTIONS = frozenset({
    "pg_sleep", "pg_read_file", "pg_read_binary_file", "dblink", "copy",
    "lo_import", "lo_export",
})


@dataclass(frozen=True)
class ValidationResult:
    ok: bool
    reason: Optional[str] = None


@dataclass(frozen=True)
class SqlResult:
    sql: str
    columns: list[str]
    rows: list[dict[str, Any]]
    row_count: int
    truncated: bool
    elapsed_ms: int
    error: Optional[str] = None


def validate_sql(sql: str, allowlist: frozenset[str] = ALLOWED_VIEWS) -> ValidationResult:
    """Accept exactly one read-only SELECT over the allowlisted views."""
    try:
        statements = [statement for statement in sqlglot.parse(sql, read="postgres") if statement]
    except sqlglot.errors.ParseError as exc:
        return ValidationResult(False, f"SQL parse error: {exc}")
    if len(statements) != 1:
        return ValidationResult(False, "Exactly one SQL statement is required")

    statement = statements[0]
    if not isinstance(statement, (exp.Select, exp.Union)):
        return ValidationResult(False, "Only SELECT or UNION queries are allowed")
    if statement.find(exp.Into) or statement.find(exp.Lock):
        return ValidationResult(False, "SELECT INTO and row-locking clauses are not allowed")

    cte_names = {
        cte.alias_or_name.lower()
        for cte in statement.find_all(exp.CTE)
        if cte.alias_or_name
    }
    for table in statement.find_all(exp.Table):
        name = table.name.lower()
        if name in cte_names:
            continue
        schema = (table.db or "cleaned").lower()
        database = (table.catalog or "").lower()
        qualified_name = f"{schema}.{name}"
        if database or qualified_name not in allowlist:
            return ValidationResult(False, f"Table is not allowlisted: {qualified_name}")

    for function in statement.find_all(exp.Func):
        if isinstance(function, exp.Anonymous):
            function_name = function.name.lower()
        else:
            function_name = function.sql_name().lower()
        if function_name.startswith("pg_") or function_name in FORBIDDEN_FUNCTIONS:
            return ValidationResult(False, f"Function is not allowed: {function_name}")

    return ValidationResult(True)


def _json_value(value: Any) -> Any:
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    if isinstance(value, Decimal):
        return round(float(value), 6)
    return value


class SafeSQLExecutor:
    """SQLGlot-gated executor with transaction-level read-only and row/time limits."""

    def __init__(
        self,
        db_url: str = READONLY_URL,
        row_cap: int = 200,
        timeout_seconds: int = 10,
        allowlist: frozenset[str] = ALLOWED_VIEWS,
    ):
        if row_cap < 1 or timeout_seconds < 1:
            raise ValueError("row_cap and timeout_seconds must be positive")
        self.engine = create_engine(db_url)
        self.row_cap = row_cap
        self.timeout_seconds = timeout_seconds
        self.allowlist = allowlist

    def validate(self, sql: str) -> ValidationResult:
        return validate_sql(sql, self.allowlist)

    def execute(self, sql: str, params: Optional[Dict[str, Any]] = None) -> SqlResult:
        validation = self.validate(sql)
        if not validation.ok:
            raise ValueError(validation.reason)

        bounded_sql = sql.strip().rstrip(";")
        bounded_sql = f"SELECT * FROM ({bounded_sql}) AS _agent_result LIMIT :_agent_row_cap"
        values = dict(params or {})
        values["_agent_row_cap"] = self.row_cap + 1
        started = time.perf_counter()

        with self.engine.connect() as connection:
            transaction = connection.begin()
            try:
                connection.execute(text("SET TRANSACTION READ ONLY"))
                connection.execute(
                    text("SELECT set_config('statement_timeout', :timeout, true)"),
                    {"timeout": f"{self.timeout_seconds}s"},
                )
                result = connection.execute(text(bounded_sql), values)
                fetched = result.mappings().all()
                truncated = len(fetched) > self.row_cap
                rows = [
                    {key: _json_value(value) for key, value in row.items()}
                    for row in fetched[: self.row_cap]
                ]
                transaction.commit()
            except Exception:
                transaction.rollback()
                raise

        return SqlResult(
            sql=sql,
            columns=list(result.keys()),
            rows=rows,
            row_count=len(rows),
            truncated=truncated,
            elapsed_ms=round((time.perf_counter() - started) * 1000),
        )