"""Excel -> Postgres ETL (simplified: single cleaned schema).

Pipeline per sheet:
  1. Clean (typed parsers, mojibake repair, normalize names)
  2. Create/replace table in cleaned schema with proper types
  3. Add indexes
  4. Print summary
"""
import re
import time
from datetime import datetime, timezone

import pandas as pd
from sqlalchemy import create_engine, text

from .config import (DATABASE_URL, EXCEL_PATH, SHEET_MAP, TABLE_NAMES,
                     COLUMN_RENAMES, TYPE_OVERRIDES, BASE_TYPE_OVERRIDES,
                     MOJIBAKE_COLUMNS)
from .cleaning import clean_dataframe, infer_type
from .build_semantic import build_semantic_views

PG_TYPES = {"percent": "NUMERIC", "multiple": "NUMERIC", "numeric": "NUMERIC",
            "int": "INTEGER", "bool": "BOOLEAN", "date": "DATE", "text": "TEXT"}

POST_LOAD_SQL = {
    "meetings": [
        r"CREATE INDEX IF NOT EXISTS idx_meet_client  ON cleaned.meeting_notes (client_id)",
        r"CREATE INDEX IF NOT EXISTS idx_meet_group   ON cleaned.meeting_notes (group_id)",
        r"CREATE INDEX IF NOT EXISTS idx_meet_date    ON cleaned.meeting_notes (meeting_date)",
        r"CREATE INDEX IF NOT EXISTS idx_meet_att_gin ON cleaned.meeting_notes USING GIN (attendees_arr)",
    ],
    "performance": [
        r"CREATE INDEX IF NOT EXISTS idx_perf_client_asof ON cleaned.performance_data (client_id, as_of_date)",
    ],
    "investments": [
        r"CREATE INDEX IF NOT EXISTS idx_inv_client ON cleaned.investments_data (client_id)",
        r"CREATE INDEX IF NOT EXISTS idx_inv_deal   ON cleaned.investments_data (deal_id)",
        r"CREATE INDEX IF NOT EXISTS idx_inv_rm     ON cleaned.investments_data (account_rm)",
        r"CREATE INDEX IF NOT EXISTS idx_inv_group  ON cleaned.investments_data (client_group_id)",
    ],
}


# --------------------------------------------------------------------- helpers
def _norm_name(s: str) -> str:
    return re.sub(r"[^0-9a-z]+", "_", str(s).strip().lower()).strip("_")


def read_sheets(path: str) -> dict:
    all_sheets = pd.read_excel(path, sheet_name=None)
    out = {}
    for name, df in all_sheets.items():
        key = SHEET_MAP.get(_norm_name(name))
        if key is None:
            print(f"[warn] sheet '{name}' not in SHEET_MAP — skipped")
            continue
        out[key] = df
    missing = set(TABLE_NAMES) - set(out)
    if missing:
        raise SystemExit(
            f"[error] expected sheets {sorted(missing)} not found. "
            f"Sheets in file: {list(all_sheets)}")
    return out


def ensure_schema(engine):
    with engine.begin() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS cleaned"))


def create_cleaned_table(engine, key, cleaned_df):
    """DDL generated from the same type rules that parsed the data."""
    table = TABLE_NAMES[key]
    overrides = {**BASE_TYPE_OVERRIDES, **TYPE_OVERRIDES[key]}
    col_defs = []
    for c in cleaned_df.columns:
        if c.endswith("_arr"):
            pg_type = "TEXT[]"
        else:
            pg_type = PG_TYPES[overrides.get(c, infer_type(c))]
        col_defs.append(f'    "{c}" {pg_type}')
    stmts = [
        f'DROP TABLE IF EXISTS cleaned."{table}" CASCADE',
        f'CREATE TABLE cleaned."{table}" (\n' + ",\n".join(col_defs) + "\n)",
    ]
    with engine.begin() as conn:
        for s in stmts:
            conn.execute(text(s))


def load_cleaned(engine, key, cleaned_df):
    df = cleaned_df.astype(object)
    df = df.where(pd.notna(df), None)
    df.to_sql(TABLE_NAMES[key], engine, schema="cleaned", if_exists="append",
              index=False, method="multi", chunksize=5000)


def post_load(engine, key):
    with engine.begin() as conn:
        for stmt in POST_LOAD_SQL.get(key, []):
            conn.execute(text(stmt))


# ----------------------------------------------------------------------- main
def main():
    t0 = time.perf_counter()
    print(f"[etl] start | excel={EXCEL_PATH}")

    sheets = read_sheets(EXCEL_PATH)
    engine = create_engine(DATABASE_URL)
    ensure_schema(engine)

    for key, df in sheets.items():
        print(f"[{key}] input rows: {len(df):,}")

        cdf, st = clean_dataframe(
            df, key,
            renames=COLUMN_RENAMES.get(key, {}),
            type_overrides={**BASE_TYPE_OVERRIDES, **TYPE_OVERRIDES[key]},
            mojibake_cols=MOJIBAKE_COLUMNS.get(key, []),
        )
        create_cleaned_table(engine, key, cdf)
        load_cleaned(engine, key, cdf)
        post_load(engine, key)
        print(f"[{key}] cleaned rows: {len(cdf):,} | "
              f"parse failures: {sum(st['parse_failures'].values())} | "
              f"mojibake fixes: {sum(st['mojibake_fixes'].values())}")

    print("\n[etl] creating semantic views...")
    build_semantic_views(DATABASE_URL)

    print(f"\n[etl] done in {time.perf_counter() - t0:.1f}s | "
          f"Cleaned tables and semantic views ready in 'cleaned' schema")


if __name__ == "__main__":
    main()