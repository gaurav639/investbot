"""Exact, ID-pattern, and pg_trgm entity resolution from cleaned semantic views."""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from typing import Literal, Optional

from sqlalchemy import create_engine, text

from ._config import DATABASE_URL
ENTITY_TYPES = ("client", "group", "deal", "rm", "company")
ID_PATTERNS = {
    "client": re.compile(r"^[A-Z]\d{4,6}$", re.IGNORECASE),
    "group": re.compile(r"^\d+$"),
    "deal": re.compile(r"^DL\d+$", re.IGNORECASE),
}
TRIGRAM_THRESHOLD = float(os.getenv("ENTITY_TRIGRAM_THRESHOLD", "0.55"))
DISAMBIGUATION_GAP = float(os.getenv("ENTITY_DISAMBIGUATION_GAP", "0.05"))


@dataclass(frozen=True)
class EntityCandidate:
    entity_type: str
    canonical_id: str
    canonical_name: str
    score: float
    method: str


@dataclass(frozen=True)
class EntityResolution:
    status: Literal["resolved", "ambiguous", "not_found"]
    query: str
    resolved: Optional[EntityCandidate] = None
    candidates: tuple[EntityCandidate, ...] = ()


def normalize_alias(value: str) -> tuple[str, str]:
    tokens = re.findall(r"[a-z0-9]+", value.lower())
    return " ".join(tokens), " ".join(sorted(tokens))


def ensure_entity_alias_table(engine) -> None:
    with engine.begin() as connection:
        connection.execute(text("CREATE EXTENSION IF NOT EXISTS pg_trgm"))
        connection.execute(text("""
            CREATE TABLE IF NOT EXISTS cleaned.entity_alias (
                alias_id BIGSERIAL PRIMARY KEY,
                entity_type TEXT NOT NULL CHECK (entity_type IN ('client','group','deal','rm','company')),
                canonical_id TEXT NOT NULL,
                canonical_name TEXT NOT NULL,
                alias TEXT NOT NULL,
                alias_norm TEXT NOT NULL,
                alias_norm_sorted TEXT NOT NULL,
                source TEXT NOT NULL,
                frequency INTEGER NOT NULL DEFAULT 1,
                UNIQUE (entity_type, canonical_id, alias_norm)
            )
        """))
        connection.execute(text("""
            CREATE INDEX IF NOT EXISTS idx_entity_alias_trgm
            ON cleaned.entity_alias USING GIN (alias_norm gin_trgm_ops)
        """))
        connection.execute(text("""
            CREATE INDEX IF NOT EXISTS idx_entity_alias_exact
            ON cleaned.entity_alias (entity_type, alias_norm)
        """))


def _add_alias(aliases, entity_type: str, canonical_id, canonical_name, alias, source: str) -> None:
    if canonical_id is None or canonical_name is None or alias is None:
        return
    alias = str(alias).strip()
    canonical_name = str(canonical_name).strip()
    norm, sorted_norm = normalize_alias(alias)
    if not alias or not norm or not canonical_name:
        return
    key = (entity_type, str(canonical_id), norm)
    if key in aliases:
        previous = aliases[key]
        aliases[key] = {**previous, "frequency": previous["frequency"] + 1}
        return
    aliases[key] = {
        "entity_type": entity_type,
        "canonical_id": str(canonical_id),
        "canonical_name": canonical_name,
        "alias": alias,
        "alias_norm": norm,
        "alias_norm_sorted": sorted_norm,
        "source": source,
        "frequency": 1,
    }


def build_entity_aliases(db_url: str = DATABASE_URL) -> int:
    """Refresh aliases from only the columns retained by etl/cleaning.py."""
    engine = create_engine(db_url)
    ensure_entity_alias_table(engine)
    aliases = {}
    with engine.connect() as connection:
        for row in connection.execute(text(
            "SELECT client_id, display_name FROM cleaned.dim_client"
        )).mappings():
            _add_alias(aliases, "client", row["client_id"], row["display_name"], row["client_id"], "client_id")
            _add_alias(aliases, "client", row["client_id"], row["display_name"], row["display_name"], "client_name")
            _add_alias(aliases, "client", row["client_id"], row["display_name"], f"Client {row['client_id']}", "generated")

        for row in connection.execute(text(
            "SELECT DISTINCT client_id, display_name, account_name "
            "FROM cleaned.fact_investment JOIN cleaned.dim_client USING (client_id) "
            "WHERE account_name IS NOT NULL"
        )).mappings():
            _add_alias(aliases, "client", row["client_id"], row["display_name"], row["account_name"], "account_name")

        for row in connection.execute(text("SELECT group_id FROM cleaned.dim_group")).mappings():
            _add_alias(aliases, "group", row["group_id"], f"Group {row['group_id']}", row["group_id"], "group_id")
            _add_alias(aliases, "group", row["group_id"], f"Group {row['group_id']}", f"Group {row['group_id']}", "generated")

        for row in connection.execute(text(
            "SELECT deal_id, deal_name FROM cleaned.dim_deal"
        )).mappings():
            _add_alias(aliases, "deal", row["deal_id"], row["deal_name"] or row["deal_id"], row["deal_id"], "deal_id")
            _add_alias(aliases, "deal", row["deal_id"], row["deal_name"] or row["deal_id"], row["deal_name"], "deal_name")

        for row in connection.execute(text(
            "SELECT rm_name, emails FROM cleaned.dim_rm"
        )).mappings():
            _add_alias(aliases, "rm", row["rm_name"], row["rm_name"], row["rm_name"], "account_rm")
            for email in row["emails"] or []:
                _add_alias(aliases, "rm", row["rm_name"], row["rm_name"], email, "account_rm_email")
                _add_alias(aliases, "rm", row["rm_name"], row["rm_name"], email.split("@", 1)[0], "email_local_part")

        for row in connection.execute(text(
            "SELECT DISTINCT account_rm, rm_alias FROM cleaned.investments_data "
            "WHERE account_rm IS NOT NULL AND rm_alias IS NOT NULL"
        )).mappings():
            _add_alias(aliases, "rm", row["account_rm"], row["account_rm"], row["rm_alias"], "rm_alias")

        for row in connection.execute(text("""
            SELECT DISTINCT meetings.client_id, clients.display_name, meetings.company
            FROM cleaned.meeting_notes AS meetings
            JOIN cleaned.dim_client AS clients USING (client_id)
            WHERE meetings.client_id IS NOT NULL AND meetings.company IS NOT NULL
        """)).mappings():
            _add_alias(
                aliases, "client", row["client_id"], row["display_name"],
                row["company"], "meeting_company",
            )

        for row in connection.execute(text(
            "SELECT DISTINCT company FROM cleaned.meeting_notes WHERE company IS NOT NULL"
        )).mappings():
            _add_alias(aliases, "company", row["company"], row["company"], row["company"], "meeting_company")

    with engine.begin() as connection:
        connection.execute(text("DELETE FROM cleaned.entity_alias"))
        if aliases:
            connection.execute(text("""
                INSERT INTO cleaned.entity_alias (
                    entity_type, canonical_id, canonical_name, alias, alias_norm,
                    alias_norm_sorted, source, frequency
                ) VALUES (
                    :entity_type, :canonical_id, :canonical_name, :alias, :alias_norm,
                    :alias_norm_sorted, :source, :frequency
                )
            """), list(aliases.values()))
    return len(aliases)


class EntityResolver:
    def __init__(
        self,
        db_url: str = DATABASE_URL,
        trigram_threshold: float = TRIGRAM_THRESHOLD,
        disambiguation_gap: float = DISAMBIGUATION_GAP,
    ):
        self.engine = create_engine(db_url)
        self.trigram_threshold = trigram_threshold
        self.disambiguation_gap = disambiguation_gap

    def resolve(self, query: str, entity_type: Optional[str] = None) -> EntityResolution:
        if entity_type is not None and entity_type not in ENTITY_TYPES:
            raise ValueError(f"Unsupported entity type: {entity_type}")
        query = query.strip()
        if not query:
            return EntityResolution("not_found", query)
        norm, sorted_norm = normalize_alias(query)
        if not norm:
            return EntityResolution("not_found", query)

        with self.engine.connect() as connection:
            if entity_type is None:
                for candidate_type, pattern in ID_PATTERNS.items():
                    if pattern.fullmatch(query):
                        exact = self._lookup_id(connection, query, candidate_type)
                        if exact:
                            return EntityResolution("resolved", query, exact, (exact,))
            elif entity_type in ID_PATTERNS and ID_PATTERNS[entity_type].fullmatch(query):
                exact = self._lookup_id(connection, query, entity_type)
                if exact:
                    return EntityResolution("resolved", query, exact, (exact,))

            exact_rows = connection.execute(text("""
                SELECT entity_type, canonical_id, canonical_name, MAX(frequency) AS frequency
                FROM cleaned.entity_alias
                                WHERE (alias_norm = :norm OR alias_norm_sorted = :sorted_norm)
                  AND (:entity_type IS NULL OR entity_type = :entity_type)
                GROUP BY entity_type, canonical_id, canonical_name
                ORDER BY frequency DESC, canonical_name
                LIMIT 8
            """), {
                "norm": norm,
                "sorted_norm": sorted_norm,
                "entity_type": entity_type,
            }).mappings().all()

            exact_candidates = [self._candidate(row, 1.0, "exact") for row in exact_rows]
            if len(exact_candidates) == 1:
                candidate = exact_candidates[0]
                return EntityResolution("resolved", query, candidate, (candidate,))
            if exact_candidates:
                return EntityResolution("ambiguous", query, candidates=tuple(exact_candidates[:4]))

            connection.execute(text(
                "SELECT set_config('pg_trgm.similarity_threshold', :threshold, true)"
            ), {"threshold": str(self.trigram_threshold)})
            fuzzy_rows = connection.execute(text("""
                SELECT entity_type, canonical_id, canonical_name,
                       MAX(similarity(alias_norm, :norm)) AS score,
                       MAX(frequency) AS frequency
                FROM cleaned.entity_alias
                WHERE alias_norm % :norm
                  AND (:entity_type IS NULL OR entity_type = :entity_type)
                GROUP BY entity_type, canonical_id, canonical_name
                ORDER BY score DESC, frequency DESC, canonical_name
                LIMIT 8
            """), {"norm": norm, "entity_type": entity_type}).mappings().all()

        candidates = [self._candidate(row, float(row["score"]), "trigram") for row in fuzzy_rows]
        if not candidates or candidates[0].score < self.trigram_threshold:
            return EntityResolution("not_found", query)
        if len(candidates) == 1 or candidates[0].score - candidates[1].score >= self.disambiguation_gap:
            return EntityResolution("resolved", query, candidates[0], tuple(candidates[:4]))
        return EntityResolution("ambiguous", query, candidates=tuple(candidates[:4]))

    @staticmethod
    def _lookup_id(connection, query: str, entity_type: str) -> Optional[EntityCandidate]:
        row = connection.execute(text("""
            SELECT entity_type, canonical_id, canonical_name
            FROM cleaned.entity_alias
            WHERE entity_type = :entity_type AND lower(canonical_id) = lower(:query)
            GROUP BY entity_type, canonical_id, canonical_name
            ORDER BY canonical_name
            LIMIT 1
        """), {"entity_type": entity_type, "query": query}).mappings().first()
        return EntityResolver._candidate(row, 1.0, "id_pattern") if row else None

    @staticmethod
    def _candidate(row, score: float, method: str) -> EntityCandidate:
        return EntityCandidate(
            entity_type=row["entity_type"],
            canonical_id=str(row["canonical_id"]),
            canonical_name=row["canonical_name"],
            score=score,
            method=method,
        )


def main() -> None:
    count = build_entity_aliases()
    print(f"Refreshed {count:,} cleaned.entity_alias rows")


if __name__ == "__main__":
    main()