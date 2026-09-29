from typing import Callable, Optional, Tuple

import copy
import json
import math
import multiprocessing
import os

import torch
import torch.nn as nn
import transformers

class ContextualModelConfig(transformers.configuration_utils.PretrainedConfig):
    """We create a dummy configuration class that will just set properties
    based on whatever kwargs we pass in.

    When this class is initialized (see experiments.py) we pass in the
    union of all data, model, and training args, all of which should
    get saved to the config json.
    """

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                json.dumps(value)
                setattr(self, key, value)
            except TypeError:
                # value was not JSON-serializable, skip
                continue
        super().__init__()

def load_embedder_and_tokenizer(name: str) -> Tuple[
        transformers.PreTrainedModel, 
        transformers.PreTrainedTokenizer
]:
    assert name is not None, "name must be provided to load_embedder_and_tokenizer"
    if name.startswith("nomic") or (name == "bert-base-uncased"):
        model = transformers.AutoModelForMaskedLM.from_pretrained(name, trust_remote_code=True).bert
        tokenizer = transformers.AutoTokenizer.from_pretrained(name)
    elif name in ["gtr-base", "gtr_base"]:
        model = transformers.AutoModel.from_pretrained(
            "sentence-transformers/gtr-t5-base"
        ).encoder
        tokenizer = transformers.AutoTokenizer.from_pretrained(
            "sentence-transformers/gtr-t5-base"
        )
    elif name == "pile-t5-base-encoder":
        model = transformers.AutoModel.from_pretrained(
            "EleutherAI/pile-t5-base"
        ).encoder
        tokenizer = transformers.AutoTokenizer.from_pretrained(
            "EleutherAI/pile-t5-base"
        )
        tokenizer.pad_token = tokenizer.eos_token
    elif name == "pile-t5-base-decoder":
        model = transformers.AutoModel.from_pretrained(
            "EleutherAI/pile-t5-base"
        ).decoder
        tokenizer = transformers.AutoTokenizer.from_pretrained(
            "EleutherAI/pile-t5-base"
        )
        tokenizer.pad_token = tokenizer.eos_token
    elif name.startswith("gpt2") or name.startswith("meta-llama") or ("Llama" in name):
        model = transformers.AutoModelForCausalLM.from_pretrained(
            name, 
            # torch_dtype=torch.bfloat16,
            attn_implementation="flash_attention_2",
            low_cpu_mem_usage=True,
            # device_map="auto",
        )
        model.padding_side = "right"
        tokenizer = transformers.AutoTokenizer.from_pretrained(name)
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.add_eos_token = True
    else:
        model = transformers.AutoModel.from_pretrained(name, trust_remote_code=True)
        tokenizer = transformers.AutoTokenizer.from_pretrained(name)

        # if use_bettertransformer:
        #     from optimum.bettertransformer import BetterTransformer
        #     model = BetterTransformer.transform(model)
    return model, tokenizer
def get_world_size() -> int:
    try:
        return torch.distributed.get_world_size()
    except (RuntimeError, ValueError):
        return 1


def get_rank() -> int:
    try:
        return torch.distributed.get_rank()
    except (RuntimeError, ValueError):
        return 0
    
def gather(t: torch.Tensor) -> torch.Tensor:
    # torch.distributed.nn.all_gather scales by world size since the reduce op is SUM
    # https://github.com/pytorch/pytorch/issues/58005
    # only should use torch.distributed.nn.all_gather if we implement a `local_loss`
    # like: https://github.com/mlfoundations/open_clip/issues/616
    world_size = get_world_size()
    if world_size == 1:
        return t

    if t.ndim == 0:
        t = t.unsqueeze(0)

    gathered = [torch.empty_like(t) for _ in range(world_size)]
    torch.distributed.all_gather(gathered, t)
    gathered[get_rank()] = t
    return torch.cat(gathered, dim=0)


def gather_sum(t: torch.Tensor) -> torch.Tensor:
    # torch.distributed.nn.all_gather scales by world size since the reduce op is SUM
    # https://github.com/pytorch/pytorch/issues/58005
    # only should use torch.distributed.nn.all_gather if we implement a `local_loss`
    # like: https://github.com/mlfoundations/open_clip/issues/616
    world_size = get_world_size()
    if world_size == 1:
        return t

    if t.ndim == 0:
        t = t.unsqueeze(0)

    gathered = [torch.empty_like(t) for _ in range(world_size)]
    torch.distributed.all_gather(gathered, t)
    gathered = torch.stack(gathered, dim=0)
    return gathered.sum(dim=0) # Sum across workers


def get_num_proc() -> int:
    world_size: int = get_world_size()
    try:
        # os.sched_getaffinity respects schedulers, unlike cpu_count(), but it's only available
        # on some Unix platforms, so we support both!
        return len(os.sched_getaffinity(0)) // world_size  # type: ignore[attr-defined]
    except AttributeError:
        return multiprocessing.cpu_count() // world_size


def torch_main_worker_finish_first(func: Callable):
    def wrapper(*args, **kwargs):
        # Get local rank (need to support non-DDP).
        try:
            local_rank = torch.distributed.get_rank()
            ddp_enabled = True
        except (RuntimeError, ValueError):
            local_rank = -1
            ddp_enabled = False
        is_main_worker = local_rank <= 0
        # Run on main worker first.
        if is_main_worker:
            result = func(*args, **kwargs)
        # Then everyone waits.
        if ddp_enabled:
            torch.distributed.barrier()
        # Run on other workers now.
        if not is_main_worker:
            result = func(*args, **kwargs)
        # Now everyone waits again.
        if ddp_enabled:
            torch.distributed.barrier()
        return result

    return wrapper


def print0(*args, **kwargs) -> None:
    if get_rank() == 0:
        print(*args, **kwargs)


def verify_ddp_weights_equal(model: torch.nn.Module, atol: float = 1e-5) -> None:
    if hasattr(model, "module"):
        model = model.module
    
    world_size = get_world_size()

    if world_size > 8:
        print0(f"[verify_ddp_weights_equal] Skipping with world_size={world_size} ⚠️")
        return

    for name, param in model.named_parameters():
        if param is None: continue
        if param.grad is None: 
            print0(f"[verify_ddp_weights_equal] Skipping param [{name}] with no grad")
            continue
        gathered_param = gather(param).reshape((world_size, -1))
        absolute_diffs = (gathered_param[None, 0, :] - gathered_param).abs()
        rank_params_eq = (absolute_diffs < atol).all()
        assert rank_params_eq, f"❌ param [{name}] not equal - got max_absolute_diff={absolute_diffs.max()}"
        ###################################################################################################################
        gathered_param_grad = gather(param.grad).reshape((world_size, -1))
        absolute_grad_diffs = (gathered_param_grad[None, 0, :] - gathered_param_grad).abs()
        rank_grad_params_eq = (absolute_grad_diffs < atol).all()
        assert rank_grad_params_eq, f"❌ param [{name}] grad not equal - got max_absolute_diff={absolute_grad_diffs.max()}"
        ###################################################################################################################
        
    
    print0("[verify_ddp_weights_equal] Verified DDP parameter correctness ✅")
    


def mean_pool_3d(
    hidden_states: torch.Tensor, attention_mask: torch.Tensor
) -> torch.Tensor:
    B, T, S, D = hidden_states.shape
    unmasked_outputs = hidden_states * attention_mask[..., None]
    pooled_outputs = unmasked_outputs.sum(dim=2) / (attention_mask.sum(dim=2)[..., None] + 1e-9)

    # fix for gradient flow: fill empty rows with the mean of the rest of the sequence
    sequence_means = (
        hidden_states.reshape((B, S * T, D))
            .mean(dim=1, keepdim=True)
            .expand(-1, T, -1)
    )
    pooled_outputs = pooled_outputs.where(
        (attention_mask.sum(dim=2)[..., None] > 0), 
        sequence_means
    )
    assert pooled_outputs.shape == (B, T, D)

    return pooled_outputs

def mean_pool(
    hidden_states: torch.Tensor, attention_mask: torch.Tensor
) -> torch.Tensor:
    B, _S, D = hidden_states.shape
    unmasked_outputs = hidden_states * attention_mask[..., None]
    pooled_outputs = unmasked_outputs.sum(dim=1) / (attention_mask.sum(dim=1)[:, None] + 1e-20)
    
    assert pooled_outputs.shape == (B, D)
    return pooled_outputs


def mean_pool_weighted(
    hidden_states: torch.Tensor, attention_mask: torch.Tensor
) -> torch.Tensor:
    B, _S, D = hidden_states.shape
    attention_mask *= attention_mask.cumsum(dim=1) # [0,1,1,1,0,0] -> [0,1,2,3,0,0]
    s = torch.sum(hidden_states * attention_mask.unsqueeze(-1).float(), dim=1)
    d = attention_mask.sum(dim=1, keepdim=True).float()
    return s / d


def slice_sparse_tensor_rows(t: torch.sparse.Tensor, min_row: int, max_row: int) -> torch.sparse.Tensor:
    assert min_row < max_row, f"can't slice from row {min_row} to {max_row}"
    t = t.coalesce()
    row_idxs = t.indices()[0]
    index_mask = (min_row <= row_idxs) & (row_idxs < max_row)

    num_rows = (max_row - min_row)
    num_cols = t.shape[1]

    idxs = t.indices()[:, index_mask]
    vals = t.values()[index_mask]
    return torch.sparse_coo_tensor(idxs, vals, size=(num_rows, num_cols)).coalesce()


def slice_tensor_rows(t: torch.Tensor, min_row: int, max_row: int) -> torch.Tensor:
    if t.is_sparse:
        return slice_sparse_tensor_rows(t=t, min_row=min_row, max_row=max_row)
    else:
        return t[min_row:max_row]


@torch.no_grad
def maxsim(
    X: torch.Tensor, y: torch.Tensor, 
    maximize: bool, chunk_size: int = 8_000,
    debug_mem_usage: bool = False) -> torch.Tensor:
    device = X.device
    n_samples = X.shape[0]

    max_sim_v = torch.zeros(n_samples, device=device, dtype=X.dtype)
    max_sim_i = torch.zeros(n_samples, device=device, dtype=torch.int64)

    # TODO: Implement faster max (without going to dense tensors).
    # TODO: Use multiple GPUs.
    rank = get_rank()
    world_size = get_world_size()

    worker_worklist_size = int(math.ceil(n_samples / world_size))
    splits_start_idx = worker_worklist_size * rank
    splits_end_idx = worker_worklist_size * (rank + 1)

    for i in range(splits_start_idx, splits_end_idx, chunk_size):
        start, end = i, min(i + chunk_size, n_samples)
        sub_x = slice_tensor_rows(X, start, end)
        if debug_mem_usage: print(f"[maxsim] step {i} cuda mem free/total = {torch.cuda.mem_get_info()}")
        if debug_mem_usage: print("[maxsim] sub_x.shape:", sub_x.shape, "//", "y.shape:", y.shape)
        sub_sim = sub_x @ y # TODO – Implement sparse max here to save mem!
        sub_sim = sub_sim
        if maximize:
            sub_max_sim_v, sub_max_sim_i = sub_sim.to_dense().max(dim=-1)
        else:
            sub_max_sim_v, sub_max_sim_i = sub_sim.to_dense().min(dim=-1)
        del sub_sim
        del sub_x
        torch.cuda.empty_cache() # needs to happen after maxsim for some reason.
        max_sim_v[start: end] = sub_max_sim_v
        max_sim_i[start: end] = sub_max_sim_i
    
    # gather
    max_sim_v = gather_sum(max_sim_v)
    max_sim_i = gather_sum(max_sim_i)
    k = y.shape[1]

    assert max_sim_v.shape == (n_samples,)
    assert max_sim_i.shape == (n_samples,)
    assert max_sim_i.min() >= 0
    assert max_sim_i.max() <= k

    return max_sim_v, max_sim_i


def forward_batched(
        model: torch.nn.Module,
        input_ids: torch.Tensor,
        attention_mask: torch.Tensor,
        batch_size: int,
        dataset_input_ids: Optional[torch.Tensor] = None,
        dataset_attention_mask: Optional[torch.Tensor] = None,
        **second_stage_model_kwargs,
) -> torch.Tensor:
    if hasattr(model, "module"):
        model = model.module
    
    if hasattr(model, "first_stage_model"):
        # Support pooling over 3D dataset_input_ids inputs.
        if len(dataset_input_ids.shape) == 2:
            dataset_input_ids = dataset_input_ids[None]
            dataset_attention_mask = dataset_attention_mask[None]

        dataset_embeddings = []
        for j in range(len(dataset_input_ids)):
            i = 0
            dataset_embeddings_batch = []
            while i < dataset_input_ids.shape[1]:
                dataset_embeddings_batch.append(
                    model.first_stage_model(
                        input_ids=dataset_input_ids[j][i:i+batch_size],
                        attention_mask=dataset_attention_mask[j][i:i+batch_size],
                    )
                )
                i += batch_size
            dataset_embeddings.append(
                torch.cat(dataset_embeddings_batch, dim=0)
            )
       
        # Automatically pool over 3D dataset_input_ids.
        dataset_embeddings = torch.stack(dataset_embeddings, dim=0).mean(dim=0)

        j = 0
        outputs = []
        while j < len(input_ids):
            outputs.append(
                model.second_stage_model(
                    input_ids=input_ids[j:j+batch_size],
                    attention_mask=attention_mask[j:j+batch_size],
                    dataset_embeddings=dataset_embeddings,
                    **second_stage_model_kwargs,
                )
            )
            j += batch_size
        return torch.cat(outputs, dim=0)

    else:
        i = 0
        outputs = []
        while i < len(input_ids):
            outputs.append(
                model(
                    input_ids=input_ids[i:i+batch_size],
                    attention_mask=attention_mask[i:i+batch_size],
                    **second_stage_model_kwargs,
                )
            )
            i += batch_size
        return torch.cat(outputs, dim=0)


def last_token_pool(hidden_state: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor:
    # https://github.com/ContextualAI/gritlm/blob/main/gritlm/gritlm.py#L190
    b, n, d = hidden_state.size()
    # Get the last `1` in the attention mask of each item
    # Often it is just `gather_indices = torch.argmin(attention_mask, 1, keepdim=False) - 1`
    # except when 1) There's all 1's 2) There's 0's before the 1's
    reversed_mask = torch.flip(attention_mask, dims=(1,))
    argmax_reverse = torch.argmax(reversed_mask, dim=1, keepdim=False)
    gather_indices = attention_mask.size(1) - argmax_reverse - 1
    # If there are empty sequences, where the index would become -1 it will crash so set them to 0
    gather_indices = torch.clamp(gather_indices, min=0)
    # Turn indices from shape [b] -> [b, 1, d]
    gather_indices = gather_indices.unsqueeze(-1).repeat(1, d)
    gather_indices = gather_indices.unsqueeze(1)
    assert gather_indices.shape == (b, 1, d)
    # Gather along the seq len: [b, n, d] -> [b, d]
    # Actually no need for the attention mask as we gather the last token where attn_mask=1 but
    # as some indices (which shouldn't be attended to) may be 0 due to clamp, use mask to ignore them again
    input_mask_expanded = attention_mask.unsqueeze(-1).expand((b, n, d)).float()
    return torch.gather(hidden_state * input_mask_expanded, 1, gather_indices).squeeze(dim=1)

def print0(*args, **kwargs) -> None:
    if get_rank() == 0:
        print(*args, **kwargs)


def limit_layers(model: transformers.PreTrainedModel, n_layers: int) -> None:
    if hasattr(model, 'transformer'):
        if hasattr(model.transformer, 'h'):
            # gpt2
            model.transformer.h = model.transformer.h[:n_layers]
        else:
            model.transformer.layer = model.transformer.layer[:n_layers]
    elif hasattr(model, 'encoder'):
        if hasattr(model.encoder, 'layers'):
            model.encoder.layers = model.encoder.layers[:n_layers]
        else:
            model.encoder.layer = model.encoder.layer[:n_layers]
    else:
        raise RuntimeError(f"unknown how to limit layers of model {type(model)}")
    


def disable_dropout(model: torch.nn.Module):
    dropout_modules = [m for m in model.modules() if isinstance(m, torch.nn.Dropout)]
    for m in dropout_modules:
        m.p = 0.0
    print0(
        f"Disabled {len(dropout_modules)} dropout modules from model type {type(model)}"
    )


def disable_causality(model: torch.nn.Module):
    disabled_modules = 0
    for m in model.modules():
        if hasattr(m, "is_causal"):
            m.is_causal = False
            disabled_modules += 1
    print0(
        f"Set is_causal=False in {disabled_modules} modules from model type {type(model)}"
    )

class ContextualModelMixin(nn.Module):
    @property
    def num_corpus_tokens(self) -> int:
        return self.transductive_corpus_size * self.transductive_tokens_per_document

    def contextual_init(self):
        self.n_soft_prompt = 8
        self.prompt_projection = torch.nn.Sequential(
            torch.nn.Linear(self.hidden_size, self.hidden_size),
            torch.nn.ReLU(),
            torch.nn.Linear(self.hidden_size, self.hidden_size * self.n_soft_prompt)
        )
        self.transductive_corpus_size = vars(self.config).get("transductive_corpus_size", 1)
        self.transductive_tokens_per_document = vars(self.config).get("transductive_tokens_per_document", 1)
        self.randomize_dataset_sequence_order = True
        self.sequence_dropout_prob = vars(self.config).get("transductive_sequence_dropout_prob", 0.0)
        if self.sequence_dropout_prob > 0.0:
            self.sequence_dropout_null_embedding = torch.nn.Parameter(
                torch.randn(self.hidden_size) * 0.01,
                requires_grad = True
            )       
        self.output_projection = torch.nn.Sequential(
            torch.nn.Linear(self.hidden_size, self.hidden_size),
            torch.nn.ReLU(),
            torch.nn.Linear(self.hidden_size, self.hidden_size)
        )

    def _prepare_dataset_embeddings(
            self, 
            input_ids: torch.Tensor, dataset_embeddings: torch.Tensor,
            null_dataset_embedding: bool = False,
        ) -> torch.Tensor:
        if not isinstance(dataset_embeddings, torch.Tensor):
            dataset_embeddings = torch.tensor(dataset_embeddings)

        if len(dataset_embeddings.shape) == 2:
            # Auto-expand for a batch.
            dataset_embeddings = dataset_embeddings[None, :, :] # (b, d) -> (1, b, d)
        dataset_embeddings = dataset_embeddings.to(input_ids.device)
    
        batch_size = input_ids.shape[0]
        if (self.transductive_tokens_per_document > 1):
            if self.training:
                # Choose N random documents to fill our context window with.
                # This logic is a little confusing but allows us to sample a
                # different batch *per-document*
                assert dataset_embeddings.shape[1] == self.transductive_tokens_per_document
                R = torch.randint(
                    low=0, 
                    high=len(dataset_embeddings), 
                    size=(batch_size, self.config.transductive_corpus_size), 
                    device=dataset_embeddings.device
                )
                # TODO make this deterministic somehow for evaluation?
                dataset_embeddings = dataset_embeddings[R].reshape((batch_size, self.num_corpus_tokens, self.hidden_size))
            else:
                dataset_embeddings = dataset_embeddings.reshape((1, self.num_corpus_tokens, self.hidden_size))
                # print("reshaped to dataset_embeddings.shape =", dataset_embeddings.shape)

        if dataset_embeddings.shape[1] > self.num_corpus_tokens:
            # If too many dataset embeddings are passed in, just take the first N until
            # we have the proper number.
            dataset_embeddings = dataset_embeddings[:, :self.num_corpus_tokens, :]
        
        _, corpus_size, _hidden_size = dataset_embeddings.shape
        if _ == 1:
            # Auto-expand for a batch.
            dataset_embeddings = dataset_embeddings.expand((batch_size, -1, -1))

        if self.training and self.sequence_dropout_prob > 0.0:
            sequence_dropout_mask = (
                torch.rand((batch_size, corpus_size), device=dataset_embeddings.device) < self.sequence_dropout_prob
            )
            null_embeddings = self.sequence_dropout_null_embedding[None, None].expand(batch_size, corpus_size, -1)
            dataset_embeddings = torch.where(
                sequence_dropout_mask[..., None], null_embeddings, dataset_embeddings
            )
        elif null_dataset_embedding:
            null_embeddings = self.sequence_dropout_null_embedding[None, None].expand(batch_size, corpus_size, -1)
            dataset_embeddings = null_embeddings
        
        # print(f"[ContextualModelMixin] dataset_embeddings.shape = {dataset_embeddings.shape}")
        
        # backbone_max_seq_length = self.backbone.config.max_trained_positions
        # assert batch_size + (2 * self.n_soft_prompt + corpus_size) <= backbone_max_seq_length, "too many hard negatives for backbone model"
        soft_prompt = torch.ones((1, self.hidden_size), device=dataset_embeddings.device, dtype=dataset_embeddings.dtype)
        soft_prompt = self.prompt_projection(soft_prompt).reshape((1, self.n_soft_prompt, self.hidden_size))
        soft_prompt = soft_prompt.expand((len(dataset_embeddings), -1, -1)) # -> (b, 4+b, d) # soft_prompt.repeat((len(input_ids), 1, 1))  
        soft_prompt = torch.cat((dataset_embeddings, soft_prompt), dim=1)

        # print(f"[ContextualModelMixin] soft_prompt.shape = {soft_prompt.shape}")

        if self.training and self.randomize_dataset_sequence_order:
            randomized_order = torch.stack(
                [
                    torch.cat(
                        (
                            torch.randperm(corpus_size, device=soft_prompt.device), 
                            torch.arange(self.n_soft_prompt, device=soft_prompt.device) + corpus_size
                        ), dim=0) 
                        for _ in range(batch_size)])
            randomized_order = randomized_order.to(soft_prompt.device)
            soft_prompt = soft_prompt.gather(1, randomized_order[..., None].expand_as(soft_prompt))
        
        return soft_prompt

class BiEncoder(transformers.PreTrainedModel):
    embedder: transformers.PreTrainedModel
    def __init__(
            self, 
            config, #: transformers.PreTrainedConfig, 
        ):
        super().__init__(config=config)
        embedder, _ = load_embedder_and_tokenizer(
            config.embedder,
        )

        if config.limit_layers:
            print0(f"Limiting layers to {config.limit_layers}")
            limit_layers(embedder, config.limit_layers)
    
        self.embedder = embedder
        # if ("t5" in embedder.config.model_type):
        #     print0(f"using torch.compile() on embedder of type `{embedder.config.model_type}`")
        #     self.embedder = torch.compile(self.embedder) 
        self.hidden_size = self.embedder.config.hidden_size
        # Allow pooling to multiple tokens per document
        self.transductive_tokens_per_document = vars(self.config).get("transductive_tokens_per_document", 1)
        self.mlp = torch.nn.Sequential(
            torch.nn.Linear(self.hidden_size, self.hidden_size),
            torch.nn.GELU(),
            torch.nn.Linear(self.hidden_size, self.config.embedding_output_dim or self.hidden_size),
        )
        self.temp = config.logit_scale

        if config.disable_dropout:
            disable_dropout(self)
        self.pooling_strategy = vars(config).get("pooling_strategy", "mean")

    def forward(
            self, 
            input_ids: torch.Tensor,
            attention_mask: torch.Tensor,
            dataset_input_ids: Optional[torch.Tensor] = None,
            dataset_attention_mask: Optional[torch.Tensor] = None,
            token_type_ids = None,
            output_hidden_states: bool = False,
        ) -> torch.Tensor:
        """
        query_embedding (float torch.Tensor) - shape (batch_size, embedding_dim)
        document_embeddings (float torch.Tensor) - shape (corpus_size, embedding_dim)
            where the corpus_size >= batch_size and is structured like this:
                [d1, d2, d3, hn1_1, hn1_2, hn2_1, hn2_2, hn3_1, hn3_2]
                for a corpus with three documents and two hard negatives per document
        """
        # del dataset_input_ids
        # del dataset_attention_mask
        del token_type_ids

        # from cde.lib.dist import get_rank
        # tokenizer = transformers.AutoTokenizer.from_pretrained("bert-base-uncased")
        # if get_rank() == 0:
        #     breakpoint()
        # torch.distributed.barrier()
        outputs = (
            self.embedder(
                input_ids=input_ids,
                attention_mask=attention_mask,
            ).last_hidden_state
        )

        if self.transductive_tokens_per_document > 1:
            document_embeddings = None
            batch_size, seq_length, output_dim = outputs.shape

            if seq_length % self.transductive_tokens_per_document != 0:
                # Pad to nearest multiple
                n_extra_embeds = self.transductive_tokens_per_document - (seq_length % self.transductive_tokens_per_document)
                outputs = torch.cat(
                    (outputs, torch.zeros((batch_size, n_extra_embeds, output_dim), device=outputs.device)),
                    dim=1
                )
                attention_mask = torch.cat(
                    (attention_mask, torch.zeros((batch_size, n_extra_embeds), device=attention_mask.device)),
                    dim=1
                )
                seq_length += n_extra_embeds
                print(f"Added {n_extra_embeds} padding tokens to input_ids and attention_mask")
            
            # print("ftransductive_tokens_per_document {self.transductive_tokens_per_document} outputs.shape =", outputs.shape)

            outputs = outputs.reshape(
                (batch_size,  self.transductive_tokens_per_document, seq_length // self.transductive_tokens_per_document, output_dim)
            )

            attention_mask = attention_mask.reshape((batch_size, self.transductive_tokens_per_document, -1))
            document_embeddings = mean_pool_3d(outputs, attention_mask)
            
            document_embeddings = document_embeddings.reshape((batch_size, self.transductive_tokens_per_document, output_dim))
        else:
            if self.pooling_strategy == "mean":
                document_embeddings = mean_pool(outputs, attention_mask)
            else:
                document_embeddings = document_embeddings.max(dim=1)
        output = self.mlp(document_embeddings)

        if output_hidden_states:
            return {
                "hidden_states": outputs,
                "pooled": output,
            }
        else:
            return output


class DatasetConditionedAutoregressive(transformers.PreTrainedModel, ContextualModelMixin):
    def __init__(
            self, 
            config,
            dataset_backbone: transformers.PreTrainedModel,
            first_stage_hidden_size: int,
        ):
        super().__init__(config=config)
        self.backbone = dataset_backbone
        self.backbone_hidden_size = self.backbone.config.hidden_size
        self.hidden_size = first_stage_hidden_size # Input token size
        self.contextual_init()
        disable_causality(self.backbone)
        
        self.input_ln = torch.nn.LayerNorm(
            self.backbone_hidden_size, 
            eps=1e-5
        )
        
        # Override contextual init
        self.output_projection = torch.nn.Sequential(
            torch.nn.Linear(self.backbone_hidden_size, self.backbone_hidden_size),
            torch.nn.ReLU(),
            torch.nn.Linear(self.backbone_hidden_size, self.backbone_hidden_size)
        )
        self._shift_rotary_embedding()
                
    @property
    def num_corpus_tokens(self) -> int:
        return self.config.transductive_corpus_size * self.transductive_tokens_per_document

    @property
    def corpus_token_ratio(self) -> float:
        # How many tokens from the first stage make one token in the second
        # stage?
        return self.backbone_hidden_size / self.hidden_size
    
    def corpus_token_pad_size(self, n_tokens: int) -> int:
        return self.hidden_size % self.backbone_hidden_size
    
    def _shift_rotary_embedding(self) -> None:
        disable_transductive_rotary_embedding = vars(self.config).get("disable_transductive_rotary_embedding", True)
        # TODO: Can we do this for LLAMA?
        print("Warning: Positional embedding disabling not implemented for LLAMA.")
    
    def forward(
            self, 
            input_ids: torch.Tensor,
            attention_mask: torch.Tensor,
            dataset_embeddings: torch.Tensor,
            output_hidden_states: bool = False,
            null_dataset_embedding: bool = False,
        ) -> torch.Tensor:
        soft_prompt = self._prepare_dataset_embeddings(
            input_ids=input_ids,
            dataset_embeddings=dataset_embeddings,
            null_dataset_embedding=null_dataset_embedding,
        )
        
        # Reshape for this model.
        # print("[DatasetConditionedAutoregressive] 1 -> soft_prompt.shape =", soft_prompt.shape)
        num_soft_elements = torch.prod(torch.tensor(soft_prompt.shape[1:])).item()
        soft_prompt = soft_prompt.reshape((soft_prompt.shape[0], num_soft_elements))
        num_padding_elements = self.backbone_hidden_size - (num_soft_elements % self.backbone_hidden_size)
        padding = torch.ones((soft_prompt.shape[0], num_padding_elements), device=soft_prompt.device)
        soft_prompt = torch.cat((soft_prompt, padding), dim=1)
        soft_prompt = soft_prompt.reshape(
            (soft_prompt.shape[0], -1, self.backbone_hidden_size)
        )
        soft_prompt = self.input_ln(soft_prompt)
        # print("[DatasetConditionedAutoregressive] 2 -> soft_prompt.shape =", soft_prompt.shape)

        backbone_attention_mask = torch.ones(
            soft_prompt.shape[0:2],
            dtype=torch.long,
            device=soft_prompt.device,
        )
        token_embeddings = self.backbone.get_input_embeddings()
        inputs_embeds = token_embeddings(input_ids) # (b, s) -> (b, s, d)
        # print("[2] inputs_embeds.shape =", inputs_embeds.shape)
        inputs_embeds = torch.cat((soft_prompt, inputs_embeds), dim=1) # (v, 4+b+s, d)
        # print("[3.a] inputs_embeds.shape =", inputs_embeds.shape)
        input_attention_mask = torch.cat((backbone_attention_mask, attention_mask), dim=1)
        # print("[3.b] attention_mask.shape =", attention_mask.shape)

        output = self.backbone(
            inputs_embeds=inputs_embeds,
            attention_mask=input_attention_mask,
            output_hidden_states=True,
        ) # (1, 4 + b + s, d)
        # trim soft prompt
        last_hidden_state = output.hidden_states[-1]
        n_soft_prompt_tokens = soft_prompt.shape[1]

        output_vectors = last_hidden_state[:, n_soft_prompt_tokens:, :]
        output_attention_mask = input_attention_mask[:, n_soft_prompt_tokens:]

        # Take last token position
        if vars(self.config).get("pooling_strategy") == "last_token":
            output_pooled = last_token_pool(output_vectors, output_attention_mask)
        elif vars(self.config).get("pooling_strategy") == "mean":
            output_pooled = mean_pool(output_vectors, output_attention_mask)
        else:
            output_pooled = mean_pool_weighted(output_vectors, output_attention_mask)

        # average with original vectors
        # TODO: Argparse for pooling strategy.
        output = self.output_projection(output_pooled) # (b, 2d) -> (b, d)

        if output_hidden_states:
            return {
                "hidden_states": output_vectors,
                "pooled": output,
            }
        else:
            return output


class DatasetConditionedBiencoder(transformers.PreTrainedModel, ContextualModelMixin):
    def __init__(
            self, 
            config,
            dataset_backbone: transformers.PreTrainedModel,
        ):
        super().__init__(config=config)
        self.backbone = dataset_backbone
        self.hidden_size = self.backbone.config.hidden_size
        self.hidden_size = dataset_backbone.config.hidden_size
        # self.input_ln = torch.nn.LayerNorm(
        #     self.hidden_size, 
        #     eps=self.backbone.config.layer_norm_epsilon
        # )
        self.contextual_init()
        self._shift_rotary_embedding()
                
    @property
    def num_corpus_tokens(self) -> int:
        return self.config.transductive_corpus_size * self.transductive_tokens_per_document
    
    def _shift_rotary_embedding(self) -> None:
        disable_transductive_rotary_embedding = vars(self.config).get("disable_transductive_rotary_embedding", True)
        if self.backbone.config.model_type.startswith("nomic") and disable_transductive_rotary_embedding:
            # We only want to apply positional embeddings to the
            # *text* portion of the backbone network.
            self.backbone.config.rotary_start_pos = 0.0
            rotary_disabled = 0

            rotary_start_pos = self.num_corpus_tokens
            for module in self.backbone.modules():
                if hasattr(module, "rotary_emb_dim"):
                    module.rotary_start_pos = rotary_start_pos
                    rotary_disabled += 1
            print0(f"modified {rotary_disabled} rotary modules – set rotary_start_pos to {rotary_start_pos}")
    
    def forward(
            self, 
            input_ids: torch.Tensor,
            attention_mask: torch.Tensor,
            dataset_embeddings: torch.Tensor,
            output_hidden_states: bool = False,
            null_dataset_embedding: bool = False,
        ) -> torch.Tensor:
        # print(f"[DatasetConditionedBiencoder - 0] input_ids.shape => {input_ids.shape} // dataset_embeddings.shape =", dataset_embeddings.shape)
        soft_prompt = self._prepare_dataset_embeddings(
            input_ids=input_ids,
            dataset_embeddings=dataset_embeddings,
            null_dataset_embedding=null_dataset_embedding,
        )
        # print(f"[DatasetConditionedBiencoder - 1] soft_prompt.shape => {soft_prompt.shape}")
        backbone_attention_mask = torch.ones(
            soft_prompt.shape[0:2],
            dtype=torch.long,
            device=soft_prompt.device,
        )
        inputs_embeds = self.backbone.embeddings(input_ids) # (b, s) -> (b, s, d)
        # print("[2] inputs_embeds.shape =", inputs_embeds.shape)
        inputs_embeds = torch.cat((soft_prompt, inputs_embeds), dim=1) # (v, 4+b+s, d)
        # print("[3.a] inputs_embeds.shape =", inputs_embeds.shape)
        attention_mask = torch.cat((backbone_attention_mask, attention_mask), dim=1)
        # print("[3.b] attention_mask.shape =", attention_mask.shape)
        output = self.backbone(
            inputs_embeds=inputs_embeds,
            attention_mask=attention_mask,
        ) # (1, 4 + b + s, d)
        # trim soft prompt
        output_vectors = output.last_hidden_state

        # use only these tokens
        n_soft_prompt_tokens = soft_prompt.shape[1]
        # print("n_soft_prompt_tokens =", n_soft_prompt_tokens)

        output_vectors = output.last_hidden_state[:, n_soft_prompt_tokens:, :]
        output_attention_mask = attention_mask[:, n_soft_prompt_tokens:]

        # print("pooling output_vectors.shape =", output_vectors.shape, "and output_attention_mask.shape =", output_attention_mask.shape)
        output_pooled = mean_pool(output_vectors, output_attention_mask)

        # average with original vectors
        # TODO: Argparse for pooling strategy.
        # output_vectors = torch.cat((soft_prompt_pooled, output_pooled), dim=1) # (b, d) + (b, d) -> (b, 2d)
        # print("output_pooled.shape =", output_pooled.shape)
        output = self.output_projection(output_pooled) # (b, 2d) -> (b, d)

        # print("returning output.shape =", output.shape)

        if output_hidden_states:
            return {
                "hidden_states": output_vectors,
                "pooled": output,
            }
        else:
            return output


class DatasetPrefixBiencoder(transformers.PreTrainedModel, ContextualModelMixin):
    def __init__(
            self, 
            config, #: transformers.PreTrainedConfig, 
            embedder: transformers.PreTrainedModel, 
        ):
        super().__init__(config=config)
        self.embedder = embedder
        self.hidden_size = self.embedder.config.hidden_size
        self.contextual_init()
    
    def forward(
            self, 
            input_ids: torch.Tensor,
            attention_mask: torch.Tensor,
            dataset_input_ids: torch.Tensor,
            dataset_attention_mask: torch.Tensor,
            output_hidden_states: bool = False,
        ) -> torch.Tensor:
        R = torch.randint(low=0, high=len(dataset_input_ids), size=(len(input_ids),), device=dataset_input_ids.device)
        
        dataset_input_ids = dataset_input_ids[R]
        input_ids = torch.cat((dataset_input_ids, input_ids), dim=1)

        dataset_attention_mask = torch.ones_like(dataset_attention_mask, device=dataset_attention_mask.device)
        input_attention_mask = torch.cat((dataset_attention_mask, attention_mask), dim=1)
        output_attention_mask = torch.cat(
            (torch.zeros_like(dataset_input_ids), attention_mask), dim=1
        )

        output = self.embedder(
            input_ids=input_ids,
            attention_mask=input_attention_mask,
        ) 
        
        output_vectors = output.last_hidden_state
        output_pooled = mean_pool(output_vectors, output_attention_mask)
        output = self.output_projection(output_pooled) # (b, 2d) -> (b, d)

        if output_hidden_states:
            S_d = dataset_attention_mask.shape[1]
            output_vectors = output_vectors[:, S_d:, :]
            return {
                "hidden_states": output_vectors,
                "pooled": output,
            }
        else:
            return output


class ContextualDocumentEmbeddingTransformer(transformers.PreTrainedModel):
    config_class = ContextualModelConfig
    embedder: transformers.PreTrainedModel
    dataset_backbone: transformers.PreTrainedModel
    def __init__(
            self, 
            config,
        ):
        super().__init__(config=config)
        dataset_backbone, _ = load_embedder_and_tokenizer(
            vars(config).get("dataset_backbone") or config.embedder
        )

        if config.limit_layers:
            print0(f"Limiting layers to {config.limit_layers}")
            limit_layers(dataset_backbone, config.limit_layers)
        
        biencoder_config = copy.deepcopy(config)
        biencoder_config.embedding_output_dim = None
        biencoder_config.limit_layers = vars(self.config).get("limit_layers_first_stage", None)
        self.first_stage_model = BiEncoder(
            config=biencoder_config,
        )

        if vars(config).get("autoregressive_backbone", False):
            self.second_stage_model = DatasetConditionedAutoregressive(
                config=config,
                dataset_backbone=dataset_backbone,
                first_stage_hidden_size=self.first_stage_model.hidden_size,
            )
        else:
            self.second_stage_model = DatasetConditionedBiencoder(
                config=config,
                dataset_backbone=dataset_backbone
            )
        
        self.temp = config.logit_scale
        if config.disable_dropout:
            disable_dropout(self)
        
        transductive_tie_token_embeddings = vars(self.config).get("transductive_tie_token_embeddings", False)
        if transductive_tie_token_embeddings:
            self.second_stage_model.backbone.embeddings.word_embeddings.weight = (
                self.first_stage_model.embedder.embeddings.word_embeddings.weight
            )

    def forward(
            self, 
            input_ids: torch.Tensor,
            attention_mask: torch.Tensor,
            dataset_input_ids: Optional[torch.Tensor],
            dataset_attention_mask: Optional[torch.Tensor],
            output_hidden_states: bool = False,
        ) -> torch.Tensor:
        """
        input_ids (long torch.Tensor) – ids of input tokens
        attention_mask (bool torch.Tensor)
        """
        dataset_embeddings = self.first_stage_model(
            input_ids=dataset_input_ids, 
            attention_mask=dataset_attention_mask
        )
        return self.second_stage_model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            dataset_embeddings=dataset_embeddings,
            output_hidden_states=output_hidden_states,
        )



def get_model_class(name: str):
    if name in 'transductive': 
        return ContextualDocumentEmbeddingTransformer
    elif name == 'biencoder':
        return BiEncoder
    elif name == "dataset_prefix_biencoder":
        return DatasetPrefixBiencoder
    else:
        raise ValueError(f'unknown model cls {name}')
