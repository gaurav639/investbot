"""Locally downloaded CDE embeddings for meeting search."""

from __future__ import annotations

import hashlib
import os
from pathlib import Path
from typing import Any, List, Optional, Sequence

CDE_MODEL_ID = "jxm/cde-small-v2"
CDE_MODEL_REVISION = os.getenv("CDE_MODEL_REVISION", "main")
CDE_ENCODE_BATCH_SIZE = int(os.getenv("CDE_ENCODE_BATCH_SIZE", "32"))
CDE_MODEL_PATH = Path(os.getenv(
    "CDE_MODEL_PATH",
    str(Path(__file__).resolve().parents[1] / "models" / "cde-small-v2"),
))

if CDE_ENCODE_BATCH_SIZE < 1:
    raise ValueError("CDE_ENCODE_BATCH_SIZE must be positive")


def download_cde_model() -> Path:
    """Download CDE weights into the configured local model directory once."""
    completion_marker = CDE_MODEL_PATH / ".download-complete"
    if (
        completion_marker.is_file()
        and (CDE_MODEL_PATH / "config.json").is_file()
        and (CDE_MODEL_PATH / "model.safetensors").is_file()
    ):
        return CDE_MODEL_PATH
    try:
        from huggingface_hub import snapshot_download
    except ImportError as exc:
        raise RuntimeError("Install huggingface-hub to download the CDE model") from exc
    CDE_MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    snapshot_download(
        repo_id=CDE_MODEL_ID,
        revision=CDE_MODEL_REVISION,
        local_dir=str(CDE_MODEL_PATH),
    )
    if not (CDE_MODEL_PATH / "model.safetensors").is_file():
        raise RuntimeError("Hugging Face download finished without model.safetensors")
    completion_marker.write_text(CDE_MODEL_REVISION, encoding="ascii")
    return CDE_MODEL_PATH


def _minicorpus(documents: Sequence[str], size: int) -> List[str]:
    if not documents:
        raise ValueError("Cannot prepare CDE context without meeting documents")
    if size < 1:
        raise ValueError("CDE transductive corpus size must be positive")
    if len(documents) <= size:
        return [documents[index % len(documents)] for index in range(size)]
    return [documents[index * len(documents) // size] for index in range(size)]


class CDEEmbeddingService:
    """CDE small v2 encoder with the required corpus-conditioned context."""

    def __init__(self, model: Optional[Any] = None, device: Optional[str] = None):
        if model is None:
            try:
                from sentence_transformers import SentenceTransformer
            except ImportError as exc:
                raise RuntimeError(
                    "Install sentence-transformers to use local CDE embeddings"
                ) from exc

            model_path = download_cde_model()
            if device is None:
                import torch

                device = os.getenv("CDE_DEVICE") or (
                    "mps" if torch.backends.mps.is_available() else "cpu"
                )
            model = SentenceTransformer(
                str(model_path),
                trust_remote_code=True,
                device=device,
            )

        self.model = model
        dimension = model.get_sentence_embedding_dimension()
        if dimension is None:
            dimension = model[0].auto_model.second_stage_model.hidden_size
        self.embedding_dimensions = int(dimension)
        if self.embedding_dimensions != 768:
            raise RuntimeError(
                f"Expected {CDE_MODEL_ID} to return 768-dimensional vectors, "
                f"got {self.embedding_dimensions}"
            )
        self.model_id = f"{CDE_MODEL_ID}@{CDE_MODEL_REVISION}"
        self.dataset_embeddings = None
        self.context_fingerprint: Optional[str] = None

    def fit_corpus(self, documents: Sequence[str]) -> str:
        """Build CDE's required first-stage context from a deterministic sample."""
        corpus_size = int(self.model[0].config.transductive_corpus_size)
        context_documents = _minicorpus(documents, corpus_size)
        context = self.model.encode(
            context_documents,
            prompt_name="document",
            convert_to_tensor=True,
            show_progress_bar=False,
        )
        digest = hashlib.sha256("\n".join(context_documents).encode("utf-8")).hexdigest()
        self.dataset_embeddings = context
        self.context_fingerprint = digest
        return digest

    def _encode(self, texts: Sequence[str], prompt_name: str) -> List[List[float]]:
        if self.dataset_embeddings is None:
            raise RuntimeError("Call fit_corpus() before embedding CDE queries or documents")
        if not texts:
            return []
        vectors = self.model.encode(
            list(texts),
            prompt_name=prompt_name,
            dataset_embeddings=self.dataset_embeddings,
            convert_to_numpy=True,
            show_progress_bar=False,
            batch_size=CDE_ENCODE_BATCH_SIZE,
        )
        result = vectors.tolist()
        if len(result) != len(texts) or any(len(vector) != self.embedding_dimensions for vector in result):
            raise RuntimeError("CDE returned embeddings with an unexpected count or dimension")
        return result

    def embed_documents(self, documents: Sequence[str]) -> List[List[float]]:
        return self._encode(documents, "document")

    def embed_query(self, query: str) -> List[float]:
        return self._encode([query], "query")[0]
