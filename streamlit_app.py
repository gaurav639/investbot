"""Streamlit UI for the Text-to-SQL Investment Agent."""

import time
from typing import Any, Dict, List

import pandas as pd
import streamlit as st
from dotenv import load_dotenv

load_dotenv()


# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="InvestBot – Text-to-SQL Agent",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---------------------------------------------------------------------------
# Trace-aware orchestrator wrapper
# ---------------------------------------------------------------------------

class TracedOrchestrator:
    """Wraps AgentOrchestrator.process() and captures a step-by-step trace."""

    def __init__(self):
        from agent.orchestrator import AgentOrchestrator

        self._orch = AgentOrchestrator()

    def run(self, question: str) -> Dict[str, Any]:
        trace: List[Dict[str, Any]] = []

        overall_start = time.perf_counter()

        result = self._orch.process(question, trace=trace)

        total_ms = round((time.perf_counter() - overall_start) * 1000)

        return {
            "answer": result.get("answer", ""),
            "sql": result.get("sql", {}),
            "rows": result.get("rows", {}),
            "trace": trace,
            "total_ms": total_ms,
            "history_summary": result.get("history_summary", ""),
            "mode": result.get("mode", ""),
            "tables": result.get("tables", []),
            "warnings": result.get("warnings", []),
        }

    def clear_history(self) -> None:
        self._orch.chat_history.clear()

    def get_history_summary(self) -> str:
        return self._orch.chat_history.get_summary()


# ---------------------------------------------------------------------------
# Session state
# ---------------------------------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "show_trace" not in st.session_state:
    st.session_state.show_trace = False

if "selected_message_idx" not in st.session_state:
    st.session_state.selected_message_idx = None


@st.cache_resource
def get_orchestrator():
    return TracedOrchestrator()


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def render_trace(trace: List[Dict[str, Any]]) -> None:
    """Render execution trace."""

    if not trace:
        st.info("No execution trace available.")
        return

    for item in trace:
        status = item.get("status", "")
        step_name = item.get("step", "Unknown step")
        duration = item.get("duration_ms", 0)
        details = item.get("details", {})

        if status == "success":
            status_icon = "✅"
        elif status == "error":
            status_icon = "❌"
        elif status == "warn":
            status_icon = "⚠️"
        else:
            status_icon = "ℹ️"

        st.markdown(
            f"**{status_icon} {step_name}**  \n"
            f"Duration: `{duration} ms`"
        )

        if details:
            with st.expander("Details"):
                st.json(details)


def render_message_details(details: Dict[str, Any]) -> None:
    """Render expandable details for a message."""

    if not details:
        return

    with st.expander("🔎 View Details"):

        # SQL
        sql_stmts = details.get("sql", {})

        if sql_stmts:
            st.subheader("SQL")

            for label, sql_text in sql_stmts.items():
                if len(sql_stmts) > 1:
                    st.caption(label)

                st.code(sql_text, language="sql")

        # Data
        rows = details.get("rows", {})

        if rows:
            st.subheader("Data")

            for label, data in rows.items():
                if data:
                    st.caption(f"{label.title()} — {len(data)} row(s)")

                    df = pd.DataFrame(data[:10])

                    st.dataframe(
                        df,
                        use_container_width=True,
                        hide_index=True,
                    )
                else:
                    st.info(f"No data returned for {label}.")

        # Trace
        trace = details.get("trace", [])

        if trace:
            st.subheader("Agent Trace")
            render_trace(trace)

        # Metadata
        st.subheader("Execution Information")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Mode",
                details.get("mode", "N/A"),
            )

        with col2:
            tables = details.get("tables", [])
            st.metric(
                "Tables",
                len(tables),
            )

        with col3:
            st.metric(
                "Execution Time",
                f"{details.get('total_ms', 0)} ms",
            )

        if details.get("tables"):
            st.caption(
                "Tables used: "
                + ", ".join(details.get("tables", []))
            )

        # Warnings
        warnings = details.get("warnings", [])

        if warnings:
            st.warning(
                "⚠️ " + "; ".join(warnings)
            )


# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------

with st.sidebar:

    st.title("📊 InvestBot")

    st.caption(
        "Text-to-SQL Agent for investment intelligence"
    )

    st.divider()

    orch = get_orchestrator()

    # Conversation context
    st.subheader("💬 Conversation Context")

    history_summary = orch.get_history_summary()

    if history_summary != "No previous conversation.":
        st.write(history_summary)
    else:
        st.caption("No previous conversation.")

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True,
    ):
        orch.clear_history()

        st.session_state.messages = []
        st.session_state.selected_message_idx = None

        st.rerun()

    st.divider()

    # Message history
    st.subheader("📜 Message History")

    if st.session_state.messages:

        for i, msg in enumerate(
            st.session_state.messages
        ):

            role_icon = (
                "🧑"
                if msg["role"] == "user"
                else "🤖"
            )

            preview = msg["content"].replace(
                "\n",
                " ",
            )

            if len(preview) > 50:
                preview = preview[:50] + "…"

            if st.button(
                f"{role_icon} {preview}",
                key=f"sidebar_msg_{i}",
                use_container_width=True,
            ):
                st.session_state.selected_message_idx = i
                st.rerun()

    else:
        st.caption("No messages yet.")

    st.divider()

    st.caption(
        "v1.0 | Powered by Groq + CDE + pgvector"
    )


# ---------------------------------------------------------------------------
# Main interface
# ---------------------------------------------------------------------------

st.title("📊 InvestBot")

st.caption(
    "Ask about **client performance**, "
    "**investments**, and **meeting notes**"
)


# ---------------------------------------------------------------------------
# Chat messages
# ---------------------------------------------------------------------------

if not st.session_state.messages:

    st.info(
        "Welcome to InvestBot! "
        "Ask questions about your investment data."
    )

    st.markdown("### Example questions")

    st.markdown(
        """
        **Performance**

        What's the IRR for client A12345?

        **Investments**

        Show total invested for group 346.

        **Meetings**

        What was discussed with Orchid Ventures?

        **Hybrid**

        Performance and meetings for client A12345.
        """
    )

else:

    for i, msg in enumerate(
        st.session_state.messages
    ):

        role = msg["role"]
        content = msg["content"]
        details = msg.get("details", {})

        if role == "user":

            with st.chat_message("user"):
                st.write(content)

        else:

            with st.chat_message("assistant"):

                st.markdown(content)

                if details:
                    render_message_details(details)


# ---------------------------------------------------------------------------
# Input area
# ---------------------------------------------------------------------------

st.divider()

with st.form(
    "question_form",
    clear_on_submit=True,
):

    col1, col2 = st.columns(
        [6, 1],
        vertical_alignment="bottom",
    )

    with col1:

        question = st.text_area(
            "Ask InvestBot",
            height=70,
            placeholder=(
                "Ask about investments, "
                "performance, or meetings..."
            ),
            label_visibility="collapsed",
            key="question_input",
        )

    with col2:

        submitted = st.form_submit_button(
            "Send",
            use_container_width=True,
        )


# ---------------------------------------------------------------------------
# Process question
# ---------------------------------------------------------------------------

if submitted and question.strip():

    question = question.strip()

    # Add user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
            "details": {},
        }
    )

    # Process with orchestrator
    with st.spinner("Thinking..."):

        orch = get_orchestrator()

        result = orch.run(question)

    # Add assistant message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": result["answer"],
            "details": result,
        }
    )

    st.session_state.selected_message_idx = (
        len(st.session_state.messages) - 1
    )

    st.rerun()


# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------

st.caption(
    "💡 Tip: Ask follow-up questions — "
    "InvestBot remembers the last 5 turns of conversation."
)