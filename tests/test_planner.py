import json
import unittest

from agent.planner import QueryPlanner


class FixedPlannerLLM:
    def __init__(self, response):
        self.response = response
        self.prompt = None

    def generate(self, prompt):
        self.prompt = prompt
        return self.response


class PlannerTests(unittest.TestCase):
    def test_parses_hybrid_plan_and_iso_meeting_date(self):
        response = json.dumps({
            "intent": "hybrid",
            "tables": ["performance", "meetings"],
            "entities": [{"type": "client", "surface": "A12345"}],
            "structured_question": "Current IRR for client A12345",
            "meeting_query": "meeting discussion and action items",
            "meeting_filters": {"company": "Orchid Ventures", "meeting_date": "2022-09-01"},
            "notes": "",
        })
        llm = FixedPlannerLLM(f"```json\n{response}\n```")
        plan = QueryPlanner(llm).plan("Summarize meetings and current IRR for A12345")

        self.assertEqual(plan.intent, "hybrid")
        self.assertEqual(plan.entities[0].surface, "A12345")
        self.assertEqual(plan.meeting_filters.meeting_date.isoformat(), "2022-09-01")
        self.assertIn("Summarize meetings", llm.prompt)

    def test_rejects_non_json_planner_reply(self):
        with self.assertRaises(ValueError):
            QueryPlanner(FixedPlannerLLM("I cannot plan this query.")).plan("hello")


if __name__ == "__main__":
    unittest.main()