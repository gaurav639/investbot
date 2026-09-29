"""Shared agent configuration — single source of truth for DATABASE_URL and env loading."""

import os
from dotenv import load_dotenv

# Load .env once at import time; all agent modules import from here.
load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:postgres@localhost:5432/investbot",
)
