# End-to-End System Architecture

```mermaid
flowchart TD
    %% Base Nodes
    User([User Query]) --> AgentBrain["🧠 Agent Core / Orchestrator\n(agent/orchestrator.py)"]
    Memory[("💬 Chat Memory\n(Last 5 Turns)")] <--> AgentBrain

    %% Cognitive Loop
    subgraph CognitiveCore ["Cognitive Loop"]
        AgentBrain --> Router{"1. Router & Scope"}
        Router -->|Out of Scope| Refusal([Polite Refusal])
        Router -->|In Scope| Planner["2. LLM Query Planner\n(agent/planner.py)"]
    end

    %% Tools
    subgraph ToolLayer ["Specialized Tool Execution"]
        Planner -->|Entity Strings| T_Entity["🔍 Tool 1: Entity Resolver\n(Exact + pg_trgm fuzzy)"]
        Planner -->|Metrics / Allocations| T_SQL["💻 Tool 2: Text-to-SQL Engine\n(Few-Shot + SQLGlot AST Safety)"]
        Planner -->|Meeting Narrative| T_Vector["📑 Tool 3: Hybrid Retrieval\n(Dense CDE + BM25 RRF)"]
        
        T_SQL -. Syntax / DB Error .-> T_Repair["Auto-Repair Loop\n(Max 2 retries)"]
        T_Repair -. Fixed Query .-> T_SQL
    end

    %% Data Environment
    subgraph DataEnv ["Environment (PostgreSQL 15+)"]
        T_Entity <--> DB_Alias[("cleaned.entity_alias")]
        T_SQL --> DB_Views[("9 Cleaned Semantic Views\n(dim_*, fact_*, v_*)")]
        T_Vector --> DB_Vector[("cleaned.meeting_embeddings\n(pgvector + tsvector)")]
    end

    %% Synthesis & Output
    DB_Views --> Synth["📝 Grounded Response Synthesizer\n(Row Budgeting + Anti-Hallucination)"]
    DB_Vector --> Synth
    Synth --> ModelFallback{"Model Fallback\n(qwen-27b -> 120b -> 20b)"}
    ModelFallback --> Response([Verified Answer with Trace])
```
