"""Integration tests for dense/lexical meeting retrieval and date fallback."""

import unittest
from datetime import date

from sqlalchemy import create_engine, text

from etl.config import DATABASE_URL
from agent.semantic_search import EMBEDDING_DIMENSIONS, ensure_vector_table, search_meetings


class FixedQueryEmbedder:
    model_id = "jxm/cde-small-v2@main"
    dataset_embeddings = object()

    def embed_query(self, query):
        return [0.001] * EMBEDDING_DIMENSIONS


class SemanticSearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine(DATABASE_URL)
        cls.embedder = FixedQueryEmbedder()
        ensure_vector_table(cls.engine, cls.embedder.model_id)

    @classmethod
    def tearDownClass(cls):
        cls.engine.dispose()

    def test_full_text_search_and_exact_company_date(self):
        rows = search_meetings(
            "Orchid Ventures meeting",
            self.embedder,
            db_url=DATABASE_URL,
            company="Orchid Ventures",
            meeting_date=date(2022, 9, 1),
            limit=5,
        )
        self.assertTrue(rows)
        self.assertEqual(rows[0]["meeting_date"], date(2022, 9, 1))
        self.assertEqual(rows[0]["date_strategy"], "exact")
        self.assertIn("Orchid Ventures", rows[0]["document_text"])

    def test_us_date_swap_fallback_finds_orchid_meeting(self):
        rows = search_meetings(
            "Orchid Ventures meeting discussion",
            self.embedder,
            db_url=DATABASE_URL,
            company="Orchid Ventures",
            meeting_date=date(2022, 1, 9),
            limit=5,
        )
        self.assertTrue(rows)
        self.assertEqual(rows[0]["meeting_date"], date(2022, 9, 1))
        self.assertEqual(rows[0]["date_strategy"], "swapped")

    def test_date_strategy_is_none_without_date_filter(self):
        rows = search_meetings(
            "Orchid Ventures",
            self.embedder,
            db_url=DATABASE_URL,
            company="Orchid Ventures",
            limit=3,
        )
        self.assertTrue(rows)
        self.assertTrue(all(row["date_strategy"] == "none" for row in rows))


if __name__ == "__main__":
    unittest.main()