import unittest

from agent.sql_generator import SQLGenerator


class FakeLLM:
    def __init__(self, responses):
        self.responses = list(responses)
        self.prompts = []

    def generate(self, prompt):
        self.prompts.append(prompt)
        return self.responses.pop(0)


class SQLGeneratorTests(unittest.TestCase):
    def test_generates_and_executes_client_performance_join(self):
        sql = """
            SELECT c.client_id, c.total_invested_usd, p.ci_total_irr, p.as_of_date
            FROM cleaned.dim_client AS c
            JOIN cleaned.v_performance_latest AS p USING (client_id)
            WHERE c.client_id = :client_id
            LIMIT 1
        """
        llm = FakeLLM([sql])
        generator = SQLGenerator(llm)
        result = generator.run(
            "Show current IRR and invested amount for client A12345",
            params={"client_id": "A12345"},
            resolved_entities={"client": "A12345"},
        )
        self.assertIsNone(result.error)
        self.assertEqual(result.row_count, 1)
        self.assertIn("ci_total_irr", result.columns)
        self.assertIn("cleaned.v_performance_latest", llm.prompts[0])

    def test_unsafe_sql_is_rejected_and_repaired(self):
        safe_sql = "SELECT client_id FROM cleaned.dim_client WHERE client_id = :client_id LIMIT 1"
        llm = FakeLLM(["DELETE FROM cleaned.dim_client", safe_sql])
        generator = SQLGenerator(llm)
        result = generator.run("Find client A12345", params={"client_id": "A12345"})
        self.assertIsNone(result.error)
        self.assertEqual(result.row_count, 1)
        self.assertIn("Previous SQL", llm.prompts[1])
        self.assertIn("Only SELECT", llm.prompts[1])


if __name__ == "__main__":
    unittest.main()