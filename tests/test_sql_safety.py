import unittest

from agent.sql_safety import SafeSQLExecutor, validate_sql


class SQLSafetyTests(unittest.TestCase):
    def test_select_from_allowlisted_view_is_valid(self):
        result = validate_sql(
            "SELECT client_id, total_invested_usd FROM cleaned.dim_client"
        )
        self.assertTrue(result.ok, result.reason)

    def test_cte_can_reference_allowlisted_view(self):
        result = validate_sql("""
            WITH client_totals AS (
                SELECT client_id, total_invested_usd FROM cleaned.dim_client
            )
            SELECT client_id FROM client_totals
        """)
        self.assertTrue(result.ok, result.reason)

    def test_rejects_multiple_statements(self):
        result = validate_sql(
            "SELECT client_id FROM cleaned.dim_client; SELECT 1"
        )
        self.assertFalse(result.ok)

    def test_rejects_non_select_statements(self):
        result = validate_sql("DELETE FROM cleaned.dim_client")
        self.assertFalse(result.ok)

    def test_rejects_non_allowlisted_tables(self):
        result = validate_sql("SELECT * FROM cleaned.investments_data")
        self.assertFalse(result.ok)

    def test_rejects_dangerous_functions(self):
        result = validate_sql("SELECT pg_sleep(1)")
        self.assertFalse(result.ok)

    def test_executor_caps_rows_and_marks_truncation(self):
        executor = SafeSQLExecutor(row_cap=2)
        result = executor.execute(
            "SELECT client_id FROM cleaned.dim_client ORDER BY client_id"
        )
        self.assertEqual(result.row_count, 2)
        self.assertTrue(result.truncated)


if __name__ == "__main__":
    unittest.main()