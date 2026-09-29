"""ETL configuration — pure data: paths, mappings, type overrides. No logic."""
import os
from dotenv import load_dotenv

load_dotenv()

# ------------------------------------------------------------------ connections
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:postgres@localhost:5432/investbot",
)
EXCEL_PATH = os.getenv("EXCEL_PATH", "data/source_data.xlsx")

# ------------------------------------------------------------------ sheet map
# Normalized sheet name (lower, non-alnum -> '_') -> internal key.
SHEET_MAP = {
    "performance_data": "performance",
    "investments_data_50k": "investments",
    "investment_daat_50k": "investments",     # tolerate the typo'd sheet name
    "meeting_notes_20k": "meetings",
    "meeting_notes": "meetings",
}

# internal key -> physical table name (created as raw.<name> and clean.<name>)
TABLE_NAMES = {
    "performance": "performance_data",
    "investments": "investments_data",
    "meetings": "meeting_notes",
}

# ------------------------------------------------------------------ renames
# Keys are column names AFTER normalization (lowercase, non-alnum -> '_').
COLUMN_RENAMES = {
    "performance": {},
    "investments": {
        "client_group_id_c": "client_group_id",
        "id_capitalcall": "capital_call_id",
        "investment_amount_usd_for_agg": "investment_amount_usd",
        "dat_mininvested": "min_invested_date",
        "flg_realised": "is_realised",
        "clientstatus": "client_status",
        "accountname": "account_name",
        "accountname_org": "account_name_org",
        "accountrm": "account_rm",
        "accountrm_org": "account_rm_org",
        "accountrmemail": "account_rm_email",
        "accountrmemail_org": "account_rm_email_org",
        "accountownerid": "account_owner_id",
    },
    "meetings": {"date": "meeting_date"},   # rename makes the '_date' rule apply
}

# ------------------------------------------------------------------ types
# Applied to every table; per-table overrides below.
BASE_TYPE_OVERRIDES = {"source_row_num": "int"}

TYPE_OVERRIDES = {
    "performance": {
        "client_group_id": "int",
        "client_id": "text",
        "isgroup_flag": "bool",
    },
    "investments": {
        "client_group_id": "int",
        "investment_amount_usd": "numeric",
        "investment_amount_natural_currency": "numeric",
        "investment_exchange_rate": "numeric",
        "capital_call_id": "text",
        "deal_id": "text",
        "is_realised": "bool",
    },
    "meetings": {
        "meeting_id": "int",
        "group_id": "int",
        "summary_char_length": "int",
    },
}

# Columns where mojibake repair is applied (meeting notes are the offender).
MOJIBAKE_COLUMNS = {
    "meetings": ["attendees", "summary", "action_items",
                 "company", "sector", "region", "investment_stage"],
}