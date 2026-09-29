import unittest
from unittest.mock import patch

from agent.entity_resolver import EntityCandidate, EntityResolution
from agent.orchestrator import AgentOrchestrator
from agent.planner import PlannedEntity, PlannedMeetingFilters, QueryPlan
from agent.sql_safety import SqlResult


class FixedResolver:
    def resolve(self, query, entity_type):
        candidate = EntityCandidate(
            entity_type=entity_type,
            canonical_id=query,
            canonical_name=f"Canonical {query}",
            score=1.0,
            method="id_pattern",
        )
        return EntityResolution("resolved", query, candidate, (candidate,))


class FixedSQLGenerator:
    def __init__(self):
        self.calls = []

    def run(self, question, params=None, resolved_entities=None):
        self.calls.append((question, params, resolved_entities))
        return SqlResult(
            sql="SELECT ... JOIN ...",
            columns=["client_id", "total_invested_usd", "ci_current_irr"],
            rows=[{
                "client_id": params["client_id"],
                "total_invested_usd": 1000.0,
                "ci_current_irr": 0.12,
            }],
            row_count=1,
            truncated=False,
            elapsed_ms=4,
        )


class OrchestratorTests(unittest.TestCase):
    def test_cross_table_question_uses_one_joined_sql_plan(self):
        generator = FixedSQLGenerator()
        agent = AgentOrchestrator(
            sql_generator=generator,
            entity_resolver=FixedResolver(),
        )

        result = agent.process(
            "Compare total invested amount with current IRR for client A12345"
        )

        self.assertEqual(len(generator.calls), 1)
        self.assertEqual(generator.calls[0][1], {"client_id": "A12345"})
        self.assertEqual(result["mode"], "sql")
        self.assertEqual(result["rows"]["structured"][0]["client_id"], "A12345")
        self.assertIn("structured", result["sql"])

    def test_unresolved_ambiguous_entity_stops_sql_execution(self):
        class AmbiguousResolver:
            def resolve(self, query, entity_type):
                candidate = EntityCandidate(entity_type, "1", "One", 0.7, "trigram")
                other = EntityCandidate(entity_type, "2", "Two", 0.68, "trigram")
                return EntityResolution("ambiguous", query, candidates=(candidate, other))

        generator = FixedSQLGenerator()
        agent = AgentOrchestrator(sql_generator=generator, entity_resolver=AmbiguousResolver())
        result = agent.process("Show the current IRR and investments for client A12345")

        self.assertEqual(generator.calls, [])
        self.assertEqual(result["clarification"]["entity_type"], "client")
        self.assertTrue(result["warnings"])

    def test_planner_hybrid_uses_structured_and_meeting_tools(self):
        class FixedPlanner:
            def plan(self, question):
                return QueryPlan(
                    intent="hybrid",
                    tables=["performance", "meetings"],
                    entities=[PlannedEntity(type="client", surface="A12345")],
                    structured_question="current IRR for the client",
                    meeting_query="meeting discussion and action items",
                    meeting_filters=PlannedMeetingFilters(company="Orchid Ventures"),
                )

        class FixedEmbedder:
            pass

        generator = FixedSQLGenerator()
        agent = AgentOrchestrator(
            planner=FixedPlanner(),
            sql_generator=generator,
            entity_resolver=FixedResolver(),
            embedder=FixedEmbedder(),
        )
        with patch(
            "agent.orchestrator.search_meetings",
            return_value=[{"meeting_id": 1, "document_text": "meeting evidence"}],
        ) as search:
            result = agent.process(
                "Summarize meetings and compare current IRR for client A12345"
            )

        self.assertEqual(result["mode"], "hybrid")
        self.assertEqual(set(result["rows"]), {"structured", "meetings"})
        self.assertEqual(search.call_args.kwargs["company"], "Orchid Ventures")
        self.assertEqual(generator.calls[0][1], {"client_id": "A12345"})

    def test_out_of_scope_plan_skips_retrieval_tools(self):
        class OutOfScopePlanner:
            def plan(self, question):
                return QueryPlan(intent="out_of_scope")

        generator = FixedSQLGenerator()
        agent = AgentOrchestrator(planner=OutOfScopePlanner(), sql_generator=generator)
        result = agent.process("What is the weather today?")

        self.assertEqual(result["mode"], "out_of_scope")
        self.assertEqual(generator.calls, [])
        self.assertIn("not that request", result["answer"])


if __name__ == "__main__":
    unittest.main()