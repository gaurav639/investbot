"""Integration tests for the cleaned-schema semantic views."""

import os
import unittest

from sqlalchemy import create_engine, text

from etl.build_semantic import build_semantic_views


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:postgres@localhost:5432/investbot",
)


class SemanticViewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine(DATABASE_URL)
        build_semantic_views(DATABASE_URL)

    @classmethod
    def tearDownClass(cls):
        cls.engine.dispose()

    def scalar(self, statement, **params):
        with self.engine.connect() as connection:
            return connection.execute(text(statement), params).scalar()

    def test_latest_client_view_has_one_row_per_client(self):
        source_clients = self.scalar(
            """SELECT COUNT(DISTINCT client_id)
               FROM cleaned.performance_data
               WHERE isgroup_flag IS FALSE AND client_id IS NOT NULL"""
        )
        latest_rows = self.scalar("SELECT COUNT(*) FROM cleaned.v_performance_latest")
        distinct_latest_clients = self.scalar(
            "SELECT COUNT(DISTINCT client_id) FROM cleaned.v_performance_latest"
        )
        self.assertEqual(latest_rows, source_clients)
        self.assertEqual(distinct_latest_clients, source_clients)

    def test_group_rollups_are_not_collapsed_into_null_client(self):
        source_groups = self.scalar(
            """SELECT COUNT(DISTINCT client_group_id)
               FROM cleaned.performance_data
               WHERE isgroup_flag IS TRUE AND client_group_id IS NOT NULL"""
        )
        latest_groups = self.scalar("SELECT COUNT(*) FROM cleaned.v_performance_latest_group")
        self.assertEqual(latest_groups, source_groups)
        self.assertEqual(
            self.scalar("SELECT COUNT(DISTINCT client_group_id) FROM cleaned.v_performance_latest_group"),
            source_groups,
        )

    def test_client_invested_total_matches_fact_aggregate(self):
        with self.engine.connect() as connection:
            client_id = connection.execute(text(
                "SELECT client_id FROM cleaned.investments_data "
                "WHERE client_id IS NOT NULL ORDER BY client_id LIMIT 1"
            )).scalar_one()
            view_total = connection.execute(text(
                "SELECT total_invested_usd FROM cleaned.dim_client WHERE client_id=:client_id"
            ), {"client_id": client_id}).scalar_one()
            fact_total = connection.execute(text(
                "SELECT SUM(investment_amount_usd) FROM cleaned.investments_data "
                "WHERE client_id=:client_id"
            ), {"client_id": client_id}).scalar_one()
        self.assertEqual(view_total, fact_total)

    def test_deal_total_matches_fact_aggregate(self):
        with self.engine.connect() as connection:
            deal_id = connection.execute(text(
                "SELECT deal_id FROM cleaned.investments_data "
                "WHERE deal_id IS NOT NULL ORDER BY deal_id LIMIT 1"
            )).scalar_one()
            view_total = connection.execute(text(
                "SELECT total_invested_usd FROM cleaned.dim_deal WHERE deal_id=:deal_id"
            ), {"deal_id": deal_id}).scalar_one()
            fact_total = connection.execute(text(
                "SELECT SUM(investment_amount_usd) FROM cleaned.investments_data "
                "WHERE deal_id=:deal_id"
            ), {"deal_id": deal_id}).scalar_one()
        self.assertEqual(view_total, fact_total)

    def test_views_cover_source_client_ids(self):
        expected = self.scalar("""
            SELECT COUNT(*) FROM (
                SELECT client_id FROM cleaned.investments_data WHERE client_id IS NOT NULL
                UNION
                SELECT client_id FROM cleaned.performance_data
                WHERE isgroup_flag IS FALSE AND client_id IS NOT NULL
                UNION
                SELECT client_id FROM cleaned.meeting_notes WHERE client_id IS NOT NULL
            ) ids
        """)
        self.assertEqual(self.scalar("SELECT COUNT(*) FROM cleaned.dim_client"), expected)


if __name__ == "__main__":
    unittest.main()