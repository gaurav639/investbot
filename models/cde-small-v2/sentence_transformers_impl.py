from __future__ import annotations

import json
import logging
import os
from typing import Any, Optional

import torch
from torch import nn
from transformers import AutoConfig, AutoModel, AutoTokenizer

logger = logging.getLogger(__name__)


class Transformer(nn.Module):
    """Hugging Face AutoModel to generate token embeddings.
    Loads the correct class, e.g. BERT / RoBERTa etc.
    Args:
        model_name_or_path: Hugging Face models name
            (https://huggingface.co/models)
        max_seq_length: Truncate any inputs longer than max_seq_length
        model_args: Keyword arguments passed to the Hugging Face
            Transformers model
        tokenizer_args: Keyword arguments passed to the Hugging Face
            Transformers tokenizer
        config_args: Keyword arguments passed to the Hugging Face
            Transformers config
        cache_dir: Cache dir for Hugging Face Transformers to store/load
            models
        do_lower_case: If true, lowercases the input (independent if the
            model is cased or not)
        tokenizer_name_or_path: Name or path of the tokenizer. When
            None, then model_name_or_path is used
        backend: Backend used for model inference. Can be `torch`, `onnx`,
            or `openvino`. Default is `torch`.
    """

    save_in_root: bool = True

    def __init__(
        self,
        model_name_or_path: str,
        model_args: dict[str, Any] | None = None,
        tokenizer_args: dict[str, Any] | None = None,
        config_args: dict[str, Any] | None = None,
        cache_dir: str | None = None,
        **kwargs,
    ) -> None:
        super().__init__()
        if model_args is None:
            model_args = {}
        if tokenizer_args is None:
            tokenizer_args = {}
        if config_args is None:
            config_args = {}

        if not model_args.get("trust_remote_code", False):
            raise ValueError(
                "You need to set `trust_remote_code=True` to load this model."
            )

        self.config = AutoConfig.from_pretrained(model_name_or_path, **config_args, cache_dir=cache_dir)
        self.auto_model = AutoModel.from_pretrained(model_name_or_path, config=self.config, cache_dir=cache_dir, **model_args)

        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name_or_path,
            cache_dir=cache_dir,
            **tokenizer_args,
        )

    def __repr__(self) -> str:
        return f"Transformer({self.get_config_dict()}) with Transformer model: {self.auto_model.__class__.__name__} "

    def forward(self, features: dict[str, torch.Tensor], dataset_embeddings: Optional[torch.Tensor] = None, **kwargs) -> dict[str, torch.Tensor]:
        """Returns token_embeddings, cls_token"""
        # If we don't have embeddings, then run the 1st stage model.
        # If we do, then run the 2nd stage model.
        if dataset_embeddings is None:
            sentence_embedding = self.auto_model.first_stage_model(
                input_ids=features["input_ids"],
                attention_mask=features["attention_mask"],
            )
        else:
            sentence_embedding = self.auto_model.second_stage_model(
                input_ids=features["input_ids"],
                attention_mask=features["attention_mask"],
                dataset_embeddings=dataset_embeddings,
            )
        
        features["sentence_embedding"] = sentence_embedding
        return features

    def get_word_embedding_dimension(self) -> int:
        return self.auto_model.config.hidden_size

    def tokenize(
        self, texts: list[str] | list[dict] | list[tuple[str, str]], padding: str | bool = True
    ) -> dict[str, torch.Tensor]:
        """Tokenizes a text and maps tokens to token-ids"""
        output = {}
        if isinstance(texts[0], str):
            to_tokenize = [texts]
        elif isinstance(texts[0], dict):
            to_tokenize = []
            output["text_keys"] = []
            for lookup in texts:
                text_key, text = next(iter(lookup.items()))
                to_tokenize.append(text)
                output["text_keys"].append(text_key)
            to_tokenize = [to_tokenize]
        else:
            batch1, batch2 = [], []
            for text_tuple in texts:
                batch1.append(text_tuple[0])
                batch2.append(text_tuple[1])
            to_tokenize = [batch1, batch2]

        max_seq_length = self.config.max_seq_length
        output.update(
            self.tokenizer(
                *to_tokenize,
                padding=padding,
                truncation="longest_first",
                return_tensors="pt",
                max_length=max_seq_length,
            )
        )
        return output

    def get_config_dict(self) -> dict[str, Any]:
        return {}

    def save(self, output_path: str, safe_serialization: bool = True) -> None:
        self.auto_model.save_pretrained(output_path, safe_serialization=safe_serialization)
        self.tokenizer.save_pretrained(output_path)

        with open(os.path.join(output_path, "sentence_bert_config.json"), "w") as fOut:
            json.dump(self.get_config_dict(), fOut, indent=2)

    @classmethod
    def load(cls, input_path: str) -> Transformer:
        sbert_config_path = os.path.join(input_path, "sentence_bert_config.json")
        if not os.path.exists(sbert_config_path):
            return cls(model_name_or_path=input_path)

        with open(sbert_config_path) as fIn:
            config = json.load(fIn)
        # Don't allow configs to set trust_remote_code
        if "model_args" in config and "trust_remote_code" in config["model_args"]:
            config["model_args"].pop("trust_remote_code")
        if "tokenizer_args" in config and "trust_remote_code" in config["tokenizer_args"]:
            config["tokenizer_args"].pop("trust_remote_code")
        if "config_args" in config and "trust_remote_code" in config["config_args"]:
            config["config_args"].pop("trust_remote_code")
        return cls(model_name_or_path=input_path, **config)
