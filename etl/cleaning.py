"""Typed parsers and normalization.

Contract for every parser:
  - blank -> None
  - unparseable -> None + failure counter (NEVER raise — one bad cell
    can't kill the load, and every silent coercion is counted for the DQ report)
"""
import re
from collections import defaultdict
from datetime import date, datetime

import pandas as pd

BLANK_TOKENS = {"", "-", "--", "na", "n/a", "nan", "none", "null"}

# Characters that only appear when UTF-8 bytes were decoded as cp1252/latin-1.
_MOJIBAKE_HINTS = ("Ã", "Â", "â€", "™", "œ")


def is_blank(v) -> bool:
    try:
        if pd.isna(v):
            return True
    except (TypeError, ValueError):
        pass
    return isinstance(v, str) and v.strip().lower() in BLANK_TOKENS


def fix_mojibake(v, stats=None, col=None):
    """Repair 'Sanjay LÃ³pez' -> 'Sanjay López', 'â€"' -> '—'.

    Classic double-encoding: UTF-8 bytes were decoded as cp1252. Re-encode as
    cp1252 and decode as UTF-8; fall back to latin-1; give up silently if neither works.
    """
    if not isinstance(v, str) or not any(h in v for h in _MOJIBAKE_HINTS):
        return v
    for enc in ("cp1252", "latin-1"):
        try:
            fixed = v.encode(enc).decode("utf-8")
            if stats is not None:
                stats["mojibake_fixes"][col] += 1
            return fixed
        except (UnicodeEncodeError, UnicodeDecodeError):
            continue
    return v


def parse_percent(v, stats, col):
    """'6.84%' -> 0.0684. If Excel already stored a numeric cell, assume it's a decimal."""
    if is_blank(v):
        return None
    if isinstance(v, (int, float)):
        return round(float(v), 8)
    s = str(v).strip().rstrip("%").strip()
    try:
        return round(float(s) / 100.0, 8)
    except ValueError:
        stats["parse_failures"][col] += 1
        return None


def parse_multiple(v, stats, col):
    """'3.0x' -> 3.0"""
    if is_blank(v):
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip().lower().rstrip("x").strip()
    try:
        return float(s)
    except ValueError:
        stats["parse_failures"][col] += 1
        return None


def parse_date(v, stats, col):
    """'4/24/12' -> date(2012, 4, 24).

    FORMAT DECISION (made once, here): US M/D/Y. Evidence in source: '9/14/24'
    cannot be D/M. The raw string survives in raw.* so a day/month swap fallback
    remains possible at query time (see Orchid-trace behavior).
    """
    if is_blank(v):
        return None
    if isinstance(v, (datetime, pd.Timestamp)):
        return v.date()
    if isinstance(v, date):
        return v
    s = str(v).strip()
    ts = pd.to_datetime(s, format="%m/%d/%y", errors="coerce")
    if pd.isna(ts):
        ts = pd.to_datetime(s, errors="coerce")   # last resort, still M/D default
    if pd.isna(ts):
        stats["parse_failures"][col] += 1
        return None
    return ts.date()


def parse_int(v, stats, col):
    if is_blank(v):
        return None
    try:
        return int(float(str(v).strip()))
    except ValueError:
        stats["parse_failures"][col] += 1
        return None


def parse_numeric(v, stats, col):
    if is_blank(v):
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).replace(",", "").strip()
    try:
        return float(s)
    except ValueError:
        stats["parse_failures"][col] += 1
        return None


def parse_bool(v, stats, col):
    if is_blank(v):
        return None
    if isinstance(v, bool):
        return v
    s = str(v).strip().lower()
    if s in {"y", "yes", "true", "t", "1"}:
        return True
    if s in {"n", "no", "false", "f", "0"}:
        return False
    stats["parse_failures"][col] += 1
    return None


PARSERS = {
    "percent": parse_percent,
    "multiple": parse_multiple,
    "date": parse_date,
    "int": parse_int,
    "numeric": parse_numeric,
    "bool": parse_bool,
    "text": None,
}


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """'Client Name' -> 'client_name', 'Client_Id__c' -> 'client_id__c'."""
    def norm(c):
        c = re.sub(r"[^0-9a-zA-Z]+", "_", str(c).strip())
        return c.strip("_").lower()
    df = df.copy()
    df.columns = [norm(c) for c in df.columns]
    return df


def infer_type(col: str) -> str:
    """Suffix rules — the SINGLE SOURCE OF TRUTH for column typing.

    Both the parsers and the generated DDL consult this function, so the
    data and the schema can never drift apart.
    """
    if col.endswith("_irr"):
        return "percent"
    if col.endswith("_moic"):
        return "multiple"
    if col.endswith("_date"):
        return "date"
    if col.endswith("_number"):
        return "int"
    if col.endswith("_amount"):
        return "numeric"
    return "text"


def clean_dataframe(df, table_key, renames, type_overrides, mojibake_cols):
    """Normalize names -> repair mojibake -> apply typed parsers -> add lineage key."""
    df = normalize_columns(df)
    df = df.rename(columns=renames or {})

    stats = {"parse_failures": defaultdict(int), "mojibake_fixes": defaultdict(int)}

    for col in mojibake_cols or []:
        if col in df.columns:
            df[col] = [fix_mojibake(v, stats, col) for v in df[col]]

    if table_key == "meetings":
        if "attendees" in df.columns:
            df["attendees_arr"] = df["attendees"].fillna("").astype(str).apply(
                lambda s: [x.strip() for x in s.split(";") if x and x.strip()]
            )
        if "action_items" in df.columns:
            df["action_items_arr"] = df["action_items"].fillna("").astype(str).apply(
                lambda s: [x.strip() for x in s.split("|") if x and x.strip()]
            )

    cols_to_drop = {
        "investments": ["client_id_c", "account_rm_org", "account_rm_email_org",
                        "cod_lob", "account_name_org"],
        "meetings": ["attendees", "action_items"],
    }.get(table_key, [])

    df = df.drop(columns=[c for c in cols_to_drop if c in df.columns], errors="ignore")

    for col in df.columns:
        kind = type_overrides.get(col, infer_type(col))
        parser = PARSERS.get(kind)
        if parser is not None:
            df[col] = [parser(v, stats, col) for v in df[col]]

    df = df.copy()
    df.insert(0, "source_row_num", range(1, len(df) + 1))   # joins clean <-> raw
    return df, stats