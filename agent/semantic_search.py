"""Local CDE embeddings and pgvector-backed meeting retrieval."""

from __future__ import annotations

import hashlib
import logging
import os
import time
from datetime import date, timedelta
from typing import Any, Dict, List, Optional, Sequence

from sqlalchemy import create_engine, text

from ._config import DATABASE_URL
from .embeddings import CDEEmbeddingService

EMBEDDING_DIMENSIONS = 768
VECTOR_TABLE = "cleaned.meeting_embeddings"
logger = logging.getLogger(__name__)

if not 1 <= EMBEDDING_DIMENSIONS <= 2000:
    raise ValueError("EMBEDDING_DIMENSIONS must be between 1 and 2000 for the HNSW index")


class GroqService:
    """Adapter for Groq text generation with retry support and multi-model fallback."""

    MAX_RETRIES = 3
    RETRY_BASE_DELAY = 1.0  # seconds
    
    # Model fallback chain - ordered by preference
    FALLBACK_MODELS = [
        "qwen/qwen3.8-27b",
        "openai/gpt-oss-120b", 
        "openai/gpt-oss-20b",
    ]

    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        key = api_key or os.getenv("GROQ_API_KEY")
        if not key:
            raise RuntimeError("GROQ_API_KEY is required for answer generation")
        try:
            from groq import Groq
        except ImportError as exc:
            raise RuntimeError("Install the groq package to use Groq") from exc
        self.client = Groq(api_key=key)
        self.preferred_model = model or os.getenv("GROQ_MODEL", "qwen/qwen3.8-27b")
        self.generation_model = self.preferred_model

    def generate(self, prompt: str) -> str:
        """Generate text with automatic retry and model fallback on rate limits."""
        max_tokens = int(os.getenv("GROQ_MAX_TOKENS", "600"))
        
        # Build model chain: preferred first, then fallbacks
        models_to_try = [self.preferred_model]
        for m in self.FALLBACK_MODELS:
            if m not in models_to_try:
                models_to_try.append(m)
        
        last_error = None
        for model in models_to_try:
            for attempt in range(self.MAX_RETRIES):
                try:
                    chat = self.client.chat.completions.create(
                        messages=[{"role": "user", "content": prompt}],
                        model=model,
                        temperature=0.0,
                        max_tokens=max_tokens,
                    )
                    answer = chat.choices[0].message.content
                    if not answer:
                        raise RuntimeError("Groq returned no answer text")
                    self.generation_model = model  # Remember working model
                    if model != self.preferred_model:
                        logger.warning("Fell back to model: %s", model)
                    return answer
                except Exception as exc:
                    last_error = exc
                    error_str = str(exc).lower()
                    # Check for rate limit - trigger model fallback immediately
                    if "rate limit" in error_str or "429" in error_str or "tokens per day" in error_str:
                        logger.warning("Rate limit hit for %s, trying next model: %s", model, exc)
                        break  # Break retry loop, try next model
                    if attempt < self.MAX_RETRIES - 1:
                        delay = self.RETRY_BASE_DELAY * (2 ** attempt)
                        logger.warning("Groq API attempt %d failed on %s: %s. Retrying in %.1fs…",
                                       attempt + 1, model, exc, delay)
                        time.sleep(delay)
            # If we exhausted retries for this model, continue to next model
        raise RuntimeError(f"Groq API failed on all models after {self.MAX_RETRIES} attempts each: {last_error}")


def _display_value(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (list, tuple)):
        return "; ".join(str(item).strip() for item in value if item is not None and str(item).strip())
    return str(value).strip()


def meeting_document(row: Dict[str, Any]) -> str:
    fields = (
        ("Meeting date", row.get("meeting_date")),
        ("Company", row.get("company")),
        ("Sector", row.get("sector")),
        ("Region", row.get("region")),
        ("Investment stage", row.get("investment_stage")),
        ("Deal size estimate", row.get("deal_size_estimate")),
        ("Client ID", row.get("client_id")),
        ("Group ID", row.get("group_id")),
        ("Attendees", row.get("attendees_arr")),
        ("Meeting summary", row.get("summary")),
        ("Action items", row.get("action_items_arr")),
    )
    return "\n".join(f"{label}: {value}" for label, raw in fields if (value := _display_value(raw)))


def _vector_literal(vector: Sequence[float]) -> str:
    return "[" + ",".join(format(float(value), ".8g") for value in vector) + "]"


def ensure_vector_table(engine, model_id: str) -> None:
    """Create the CDE index and clear rows from a different embedding space."""
    with engine.begin() as connection:
        connection.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
        connection.execute(text(f"""
            CREATE TABLE IF NOT EXISTS {VECTOR_TABLE} (
                source_row_num INTEGER PRIMARY KEY,
                meeting_id INTEGER,
                meeting_date DATE,
                client_id TEXT,
                group_id INTEGER,
                document_text TEXT NOT NULL,
                content_hash CHAR(64) NOT NULL,
                embedding_model TEXT,
                embedding vector({EMBEDDING_DIMENSIONS}) NOT NULL,
                search_vector TSVECTOR GENERATED ALWAYS AS
                    (to_tsvector('english', document_text)) STORED,
                embedded_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """))
        connection.execute(text(
            f"ALTER TABLE {VECTOR_TABLE} ADD COLUMN IF NOT EXISTS embedding_model TEXT"
        ))
        stored_models = set(connection.execute(text(
            f"SELECT DISTINCT embedding_model FROM {VECTOR_TABLE}"
        )).scalars().all())
        if stored_models and stored_models != {model_id}:
            logger.warning(
                "Clearing meeting vectors created by a different embedding model: %s",
                sorted(str(model) for model in stored_models),
            )
            connection.execute(text(f"TRUNCATE TABLE {VECTOR_TABLE}"))
        connection.execute(text(f"""
            ALTER TABLE {VECTOR_TABLE}
            ADD COLUMN IF NOT EXISTS search_vector TSVECTOR GENERATED ALWAYS AS
                (to_tsvector('english', document_text)) STORED
        """))
        connection.execute(text(f"""
            CREATE INDEX IF NOT EXISTS idx_meeting_embeddings_hnsw
            ON {VECTOR_TABLE} USING hnsw (embedding vector_cosine_ops)
        """))
        connection.execute(text(f"""
            CREATE INDEX IF NOT EXISTS idx_meeting_embeddings_client_group
            ON {VECTOR_TABLE} (client_id, group_id, meeting_date DESC)
        """))
        connection.execute(text(f"""
            CREATE INDEX IF NOT EXISTS idx_meeting_embeddings_search_vector
            ON {VECTOR_TABLE} USING GIN (search_vector)
        """))


def _meeting_rows(engine) -> List[Dict[str, Any]]:
    query = text("""
        SELECT source_row_num, meeting_id, meeting_date, company, sector,
               region, investment_stage, deal_size_estimate, summary,
               client_id, group_id, attendees_arr, action_items_arr
        FROM cleaned.meeting_notes
        ORDER BY source_row_num
    """)
    with engine.connect() as connection:
        return [dict(row) for row in connection.execute(query).mappings().all()]


def build_meeting_index(
    db_url: str = DATABASE_URL,
    embedder: Optional[CDEEmbeddingService] = None,
    batch_size: int = 128,
    rebuild: bool = False,
) -> Dict[str, int]:
    """Incrementally encode meeting notes locally and upsert them into pgvector."""
    if batch_size < 1:
        raise ValueError("batch_size must be at least 1")
    service = embedder or CDEEmbeddingService()
    engine = create_engine(db_url)
    ensure_vector_table(engine, service.model_id)

    if rebuild:
        with engine.begin() as connection:
            connection.execute(text(f"TRUNCATE TABLE {VECTOR_TABLE}"))

    rows = _meeting_rows(engine)
    documents = [meeting_document(row) for row in rows]
    context_fingerprint = service.fit_corpus(documents)
    with engine.connect() as connection:
        existing = dict(connection.execute(text(
            f"SELECT source_row_num, content_hash FROM {VECTOR_TABLE}"
        )).all())

    pending = []
    for row, document in zip(rows, documents):
        fingerprint_input = f"{service.model_id}:{context_fingerprint}:{document}"
        digest = hashlib.sha256(fingerprint_input.encode("utf-8")).hexdigest()
        if existing.get(row["source_row_num"]) != digest:
            pending.append((row, document, digest))

    upsert = text(f"""
        INSERT INTO {VECTOR_TABLE} (
            source_row_num, meeting_id, meeting_date, client_id, group_id,
            document_text, content_hash, embedding_model, embedding, embedded_at
        ) VALUES (
            :source_row_num, :meeting_id, :meeting_date, :client_id, :group_id,
            :document_text, :content_hash, :embedding_model,
            CAST(:embedding AS vector({EMBEDDING_DIMENSIONS})), CURRENT_TIMESTAMP
        )
        ON CONFLICT (source_row_num) DO UPDATE SET
            meeting_id = EXCLUDED.meeting_id,
            meeting_date = EXCLUDED.meeting_date,
            client_id = EXCLUDED.client_id,
            group_id = EXCLUDED.group_id,
            document_text = EXCLUDED.document_text,
            content_hash = EXCLUDED.content_hash,
            embedding_model = EXCLUDED.embedding_model,
            embedding = EXCLUDED.embedding,
            embedded_at = CURRENT_TIMESTAMP
    """)
    for start in range(0, len(pending), batch_size):
        batch = pending[start : start + batch_size]
        vectors = service.embed_documents([document for _, document, _ in batch])
        parameters = []
        for (row, document, digest), vector in zip(batch, vectors):
            parameters.append({
                "source_row_num": row["source_row_num"],
                "meeting_id": row["meeting_id"],
                "meeting_date": row["meeting_date"],
                "client_id": row["client_id"],
                "group_id": row["group_id"],
                "document_text": document,
                "content_hash": digest,
                "embedding_model": service.model_id,
                "embedding": _vector_literal(vector),
            })
        with engine.begin() as connection:
            connection.execute(upsert, parameters)
        completed = start + len(batch)
        progress_interval = max(batch_size * 4, 256)
        if completed % progress_interval < batch_size or completed == len(pending):
            print(f"[index] CDE embedded {completed:,}/{len(pending):,} changed meetings", flush=True)

    with engine.begin() as connection:
        connection.execute(text(f"""
            DELETE FROM {VECTOR_TABLE} e
            WHERE NOT EXISTS (
                SELECT 1 FROM cleaned.meeting_notes m
                WHERE m.source_row_num = e.source_row_num
            )
        """))

    return {
        "source_rows": len(rows),
        "embedded_rows": len(pending),
        "unchanged_rows": len(rows) - len(pending),
    }


def search_meetings(
    question: str,
    embedder: CDEEmbeddingService,
    db_url: str = DATABASE_URL,
    client_id: Optional[str] = None,
    group_id: Optional[int] = None,
    company: Optional[str] = None,
    sector: Optional[str] = None,
    region: Optional[str] = None,
    investment_stage: Optional[str] = None,
    meeting_date: Optional[date] = None,
    date_from: Optional[date] = None,
    date_to: Optional[date] = None,
    attendee: Optional[str] = None,
    limit: int = 5,
    dense_k: int = 50,
    lexical_k: int = 50,
    rrf_k: int = 60,
    date_fallback_window_days: int = 90,
) -> List[Dict[str, Any]]:
    """Fuse CDE vector and PostgreSQL lexical search with structured filters."""
    if not 1 <= limit <= 50:
        raise ValueError("limit must be between 1 and 50")
    if min(dense_k, lexical_k, rrf_k, date_fallback_window_days) < 1:
        raise ValueError("retrieval limits and date fallback window must be positive")
    engine = create_engine(db_url)
    if embedder.dataset_embeddings is None:
        corpus_rows = _meeting_rows(engine)
        embedder.fit_corpus([meeting_document(row) for row in corpus_rows])
    vector = _vector_literal(embedder.embed_query(question))

    def retrieve(filters: Dict[str, Any]) -> List[Dict[str, Any]]:
        query = text(f"""
            WITH dense AS (
                SELECT m.source_row_num,
                       ROW_NUMBER() OVER (
                            ORDER BY m.embedding <=> CAST(:embedding AS vector({EMBEDDING_DIMENSIONS}))
                       ) AS r
                FROM {VECTOR_TABLE} AS m
                WHERE m.embedding_model = :embedding_model
                  AND (:client_id IS NULL OR m.client_id = :client_id)
                  AND (:group_id IS NULL OR m.group_id = :group_id)
                  AND (:company IS NULL OR m.document_text ILIKE :company)
                  AND (:sector IS NULL OR m.document_text ILIKE :sector)
                  AND (:region IS NULL OR m.document_text ILIKE :region)
                  AND (:investment_stage IS NULL OR m.document_text ILIKE :investment_stage)
                  AND (:attendee IS NULL OR m.document_text ILIKE :attendee)
                  AND (:meeting_date IS NULL OR m.meeting_date = :meeting_date)
                  AND (:date_from IS NULL OR m.meeting_date >= :date_from)
                  AND (:date_to IS NULL OR m.meeting_date <= :date_to)
                ORDER BY m.embedding <=> CAST(:embedding AS vector({EMBEDDING_DIMENSIONS}))
                LIMIT :dense_k
            ), lexical AS (
                SELECT m.source_row_num,
                       ROW_NUMBER() OVER (
                            ORDER BY ts_rank_cd(m.search_vector, plainto_tsquery('english', :query_text)) DESC
                       ) AS r
                FROM {VECTOR_TABLE} AS m
                WHERE m.embedding_model = :embedding_model
                  AND m.search_vector @@ plainto_tsquery('english', :query_text)
                  AND (:client_id IS NULL OR m.client_id = :client_id)
                  AND (:group_id IS NULL OR m.group_id = :group_id)
                  AND (:company IS NULL OR m.document_text ILIKE :company)
                  AND (:sector IS NULL OR m.document_text ILIKE :sector)
                  AND (:region IS NULL OR m.document_text ILIKE :region)
                  AND (:investment_stage IS NULL OR m.document_text ILIKE :investment_stage)
                  AND (:attendee IS NULL OR m.document_text ILIKE :attendee)
                  AND (:meeting_date IS NULL OR m.meeting_date = :meeting_date)
                  AND (:date_from IS NULL OR m.meeting_date >= :date_from)
                  AND (:date_to IS NULL OR m.meeting_date <= :date_to)
                ORDER BY ts_rank_cd(m.search_vector, plainto_tsquery('english', :query_text)) DESC
                LIMIT :lexical_k
            ), ranked AS (
                SELECT source_row_num, r FROM dense
                UNION ALL
                SELECT source_row_num, r FROM lexical
            ), fused AS (
                SELECT source_row_num, SUM(1.0 / (:rrf_k + r)) AS rrf_score
                FROM ranked
                GROUP BY source_row_num
            )
                 SELECT source.source_row_num, source.meeting_id, source.meeting_date,
                     source.company, source.sector, source.region,
                     source.investment_stage, source.client_id, source.group_id,
                     source.attendees_arr, source.action_items_arr, source.summary,
                     vectors.document_text, fused.rrf_score
            FROM fused
                 JOIN {VECTOR_TABLE} AS vectors USING (source_row_num)
                 JOIN cleaned.meeting_notes AS source USING (source_row_num)
                 ORDER BY fused.rrf_score DESC, source.meeting_date DESC
            LIMIT :limit
        """)
        params = {
            "embedding": vector,
            "embedding_model": embedder.model_id,
            "query_text": question,
            "client_id": client_id,
            "group_id": group_id,
            "company": f"%{filters.get('company')}%" if filters.get("company") else None,
            "sector": f"%{filters.get('sector')}%" if filters.get("sector") else None,
            "region": f"%{filters.get('region')}%" if filters.get("region") else None,
            "investment_stage": (
                f"%{filters.get('investment_stage')}%"
                if filters.get("investment_stage") else None
            ),
            "attendee": f"%{filters.get('attendee')}%" if filters.get("attendee") else None,
            "meeting_date": filters.get("meeting_date"),
            "date_from": filters.get("date_from"),
            "date_to": filters.get("date_to"),
            "dense_k": dense_k,
            "lexical_k": lexical_k,
            "rrf_k": rrf_k,
            "limit": limit,
        }
        with engine.connect() as connection:
            return [dict(row) for row in connection.execute(query, params).mappings().all()]

    filters: Dict[str, Any] = {
        "company": company,
        "sector": sector,
        "region": region,
        "investment_stage": investment_stage,
        "attendee": attendee,
        "meeting_date": meeting_date,
        "date_from": date_from,
        "date_to": date_to,
    }
    strategies = [("exact", filters.copy())]
    if meeting_date is not None:
        if meeting_date.day <= 12 and meeting_date.month <= 12:
            swapped_date = date(meeting_date.year, meeting_date.day, meeting_date.month)
            if swapped_date != meeting_date:
                swapped = filters.copy()
                swapped["meeting_date"] = swapped_date
                strategies.append(("swapped", swapped))
        window = filters.copy()
        window["meeting_date"] = None
        window["date_from"] = meeting_date - timedelta(days=date_fallback_window_days)
        window["date_to"] = meeting_date + timedelta(days=date_fallback_window_days)
        strategies.append(("window", window))
        dropped = filters.copy()
        dropped["meeting_date"] = None
        dropped["date_from"] = None
        dropped["date_to"] = None
        strategies.append(("dropped", dropped))

    for strategy, candidate_filters in strategies:
        rows = retrieve(candidate_filters)
        if rows:
            return [{**row, "date_strategy": strategy if meeting_date else "none"} for row in rows]
    return []
