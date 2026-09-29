# Investment Intelligence Agent (InvestBot)

A text-to-SQL + semantic search agent for investment intelligence. Answers questions about client performance, investments, and meeting notes using PostgreSQL, local CDE embeddings with pgvector, and Groq LLM.

## Architecture Overview

```
source_data.xlsx → ETL → PostgreSQL (cleaned views + pgvector) → Agent → Answers
                              ↓
                       CDE small v2 embeddings (local, no API calls)
                              ↓
                       Groq (qwen/qwen3.8-27b) for planning, SQL, synthesis
```
---

## Prerequisites

- **Python 3.11+**
- **PostgreSQL 15+** with **pgvector** extension
- **Groq API Key** (get from https://console.groq.com)

---

## Quick Start

```bash
# 1. Clone and enter project
cd investbot

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# Edit .env with your DATABASE_URL and GROQ_API_KEY

# 5. Setup database (PostgreSQL with pgvector)
# Connect to PostgreSQL and enable pgvector:
# CREATE DATABASE investbot;
# \c investbot;
# CREATE EXTENSION IF NOT EXISTS vector;

# 6. Run ETL pipeline (loads source_data.xlsx → cleaned tables + semantic views)
python -m etl.ingest_simple

# 7. Build semantic search indexes
python -m agent.download_cde_model
python -m agent.index_meetings     # Takes ~5-10 mins on CPU, ~2 mins on Apple Silicon
python -m etl.build_alias

# 8. Run the agent
# CLI:
python main.py

# Web UI:
streamlit run streamlit_app.py
```

---

## Detailed Setup

### 1. Database Setup

```sql
-- Connect to PostgreSQL and run:
CREATE DATABASE investbot;
\c investbot;
CREATE EXTENSION IF NOT EXISTS vector;
```

### 2. Environment Configuration

Create `.env` from `.env.example`:

```bash
cp .env.example .env
```

Edit `.env` with your values:
```env
# Database (required)
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/investbot

# Groq API (required for planning, SQL generation, synthesis)
GROQ_API_KEY=gsk_your_key_here
GROQ_MODEL=qwen/qwen3.8-27b

# Optional: CDE model location
# CDE_MODEL_PATH=models/cde-small-v2
# CDE_DEVICE=cpu  # or 'mps' for Apple Silicon
```

### 3. ETL Pipeline (Excel → Cleaned Tables)

The `source_data.xlsx` contains three sheets:
- `Performance_Data` → `cleaned.performance_data`
- `Investments_Data_50k` → `cleaned.investments_data`
- `Meeting_Notes_20k` → `cleaned.meeting_notes`

Run the full ETL:

```bash
python -m etl.ingest_simple
```

This:
- Reads Excel sheets into `raw.*` tables
- Normalizes column names (lowercase, snake_case)
- Applies type conversions and mojibake repair
- Creates cleaned tables in `cleaned` schema
- Builds semantic views (`v_performance_latest`, `v_performance_latest_group`, `dim_client`, etc.)

**Re-run only when source data changes** — drops and recreates all cleaned tables.

### 4. Semantic Search Indexes

**Download CDE model (one-time, ~1.2GB):**
```bash
python -m agent.download_cde_model
```

**Build meeting embeddings index:**
```bash
python -m agent.index_meetings
```

This:
- Samples 512 meeting documents for CDE corpus context
- Embeds all meetings locally (no external API)
- Stores vectors in `cleaned.meeting_embeddings` (pgvector)
- Removes embeddings for deleted rows
- Use `--rebuild` to force full rebuild

**Build entity alias index:**
```bash
python -m etl.build_alias
```

Creates `cleaned.entity_alias` for fuzzy entity resolution (client names, RMs, groups, deals, companies).

---

## Usage

### Command Line Interface

```bash
python main.py
```

Commands:
- `history` — Show conversation context
- `clear` — Reset conversation history
- `exit` / `quit` — Exit

Example queries:
```
Question: What is the current IRR for client A12345?
Question: Show meetings for group 346 in 2024
Question: What meetings discussed governance concerns?
Question: Tell me about client A12345
Question: And their meetings?  (multi-turn context)
```

### Streamlit Web UI

```bash
streamlit run streamlit_app.py
```

Features:
- ChatGPT-like interface with message bubbles
- Expandable "View Details" showing SQL, data, trace
- Sidebar with conversation history and context
- Fixed input at bottom

### Evaluation Suite

Run the golden test set (59 queries across 11 categories):

```bash
python -m eval.run_eval
```

Outputs pass/fail per query and overall score.

---

## Project Structure

```
investbot/
├── agent/                      # Core agent pipeline
│   ├── __init__.py
│   ├── _config.py              # Shared config (DATABASE_URL)
│   ├── orchestrator.py         # Main pipeline (7 steps)
│   ├── planner.py              # LLM query planner (50+ few-shot)
│   ├── sql_generator.py        # SQL gen + validation (30+ examples)
│   ├── entity_resolver.py      # Exact + pg_trgm fuzzy resolution
│   ├── semantic_search.py      # Vector search + Groq fallback
│   ├── embeddings.py           # CDE local embeddings
│   ├── index_meetings.py       # Meeting vector index builder
│   ├── download_cde_model.py   # CDE model downloader
│   └── sql_safety.py           # SQLGlot validator (allowlist)
├── etl/                        # ETL pipeline
│   ├── __init__.py
│   ├── config.py               # Sheet maps, renames, types
│   ├── ingest_simple.py        # Excel → raw → cleaned
│   ├── cleaning.py             # Normalization, mojibake repair
│   ├── build_semantic.py       # Semantic views
│   └── build_alias.py          # Entity alias index builder
├── eval/                       # Evaluation
│   ├── golden.jsonl            # 59 test queries
│   ├── run_eval.py             # Test runner
│   └── judge.py                # LLM-based answer judge
├── tests/                      # Unit tests
├── main.py                     # CLI entry point
├── streamlit_app.py            # Web UI
├── requirements.txt
├── .env.example
└── data/
    └── source_data.xlsx        # Input data (provided)
```

---

## Key Features

| Feature | Implementation |
|---------|----------------|
| **SQL Generation** | 30+ few-shot examples, 3-way joins, CTEs, aggregations |
| **Vector Search** | CDE small v2 + BM25 + RRF fusion, date fallback |
| **Hybrid Execution** | SQL for meetings when filter exists (skip vector) |
| **Entity Resolution** | Planner entities > router filters; pg_trgm fuzzy |
| **Multi-turn** | Last 3 turns passed to planner for context |
| **Token Limiting** | Hybrid: 5 meeting rows + 5 structured rows max |
| **Groq Fallback** | qwen/27b → gpt-oss-120b → gpt-oss-20b on 429 |
| **SQL Safety** | Allowlisted 9 views, no forbidden functions, row limits |

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `pgvector` not found | `CREATE EXTENSION vector;` in database |
| CDE model download fails | Check internet, retry `python -m agent.download_cde_model` |
| Groq 429 rate limit | Wait for quota reset or upgrade to Dev tier |
| No meetings found | Re-run `python -m agent.index_meetings --rebuild` |
| Entity not resolved | Run `python -m etl.build_alias` |
| Import errors | `pip install -r requirements.txt` in fresh venv |

---

## License

Internal use only.