import unittest
from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from unittest.mock import MagicMock, Mock, patch

from agent.orchestrator import _build_table_query, route_question, build_sql_query
from agent.embeddings import CDEEmbeddingService, download_cde_model


class AgentRouterTests(unittest.TestCase):
    def test_sql_route_for_performance_snapshot(self):
        intent = route_question("Show me the current IRR and AUM for client A12345")
        self.assertEqual(intent["mode"], "sql")
        self.assertIn("performance", intent["tables"]) 

    def test_vector_route_for_meeting_summary(self):
        intent = route_question("Summarize the recent meetings and action items for Client A12345")
        self.assertEqual(intent["mode"], "vector")
        self.assertIn("meetings", intent["tables"])

    def test_hybrid_route_combines_meetings_and_performance(self):
        intent = route_question("Summarize recent meetings and show current IRR for Client A12345")
        self.assertEqual(intent["mode"], "hybrid")
        self.assertEqual(intent["filters"]["client_id"], "A12345")

    def test_meeting_company_and_word_date_are_extracted(self):
        intent = route_question(
            "What happened in the meeting on 1st September 2022 with Orchid Ventures?"
        )
        self.assertEqual(intent["meeting_filters"]["company"], "Orchid Ventures")
        self.assertEqual(intent["meeting_filters"]["meeting_date"], date(2022, 9, 1))

    def test_sql_generation_uses_live_schema(self):
        query = build_sql_query("Show me all performance records for client A12345")
        self.assertIn('cleaned.performance_data', query)
        self.assertIn('client_id = :client_id', query)

    def test_sql_filter_values_are_bound_parameters(self):
        sql, params = _build_table_query(
            "performance",
            {"client_id": "A12345' OR TRUE --", "group_id": None, "rm_name": None},
        )
        self.assertIn("client_id = :client_id", sql)
        self.assertEqual(params["client_id"], "A12345' OR TRUE --")
        self.assertNotIn("OR TRUE", sql)

    def test_cde_uses_fixed_context_and_retrieval_prompts(self):
        class FakeVectors:
            def __init__(self, rows):
                self.rows = rows

            def tolist(self):
                return self.rows

        model = MagicMock()
        model.get_sentence_embedding_dimension.return_value = None
        model.__getitem__.return_value.config.transductive_corpus_size = 512
        model.__getitem__.return_value.auto_model.second_stage_model.hidden_size = 768
        model.encode.side_effect = [
            "dataset-context",
            FakeVectors([[0.1] * 768, [0.2] * 768]),
            FakeVectors([[0.3] * 768]),
        ]
        embedder = CDEEmbeddingService(model=model)

        fingerprint = embedder.fit_corpus(["meeting A", "meeting B"])
        document_vectors = embedder.embed_documents(["meeting A", "meeting B"])
        query_vector = embedder.embed_query("What happened in the meeting?")

        self.assertEqual(len(fingerprint), 64)
        self.assertEqual(len(model.encode.call_args_list[0].args[0]), 512)
        self.assertEqual(model.encode.call_args_list[1].kwargs["prompt_name"], "document")
        self.assertEqual(model.encode.call_args_list[1].kwargs["batch_size"], 32)
        self.assertEqual(
            model.encode.call_args_list[1].kwargs["dataset_embeddings"],
            "dataset-context",
        )
        self.assertEqual(model.encode.call_args_list[2].kwargs["prompt_name"], "query")
        self.assertEqual(len(document_vectors), 2)
        self.assertEqual(len(query_vector), 768)

    def test_cde_download_does_not_trust_config_only(self):
        with TemporaryDirectory() as directory:
            model_path = Path(directory)
            (model_path / "config.json").write_text("{}", encoding="utf-8")

            def finish_download(**kwargs):
                (model_path / "model.safetensors").write_bytes(b"weights")

            with patch("agent.embeddings.CDE_MODEL_PATH", model_path):
                with patch("huggingface_hub.snapshot_download", side_effect=finish_download) as download:
                    self.assertEqual(download_cde_model(), model_path)
                    self.assertEqual(download_cde_model(), model_path)

            download.assert_called_once()
            self.assertTrue((model_path / ".download-complete").is_file())


if __name__ == "__main__":
    unittest.main()
