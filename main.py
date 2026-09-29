"""Minimal entry point for the investment chatbot runtime."""

from agent.orchestrator import AgentOrchestrator


def main() -> None:
    orchestrator = AgentOrchestrator()
    print("Investment intelligence assistant ready. Ask about investments, meetings, or performance.")
    print("Commands: 'history' - show conversation | 'clear' - reset history | 'exit' - quit")
    while True:
        question = input("\nQuestion: ")
        if question.strip().lower() in {"exit", "quit", "q"}:
            print("Goodbye.")
            break
        if question.strip().lower() == "history":
            print("\nConversation History:")
            print(orchestrator.chat_history.get_summary())
            continue
        if question.strip().lower() == "clear":
            orchestrator.chat_history.clear()
            print("Conversation history cleared.")
            continue
        result = orchestrator.process(question)
        print("\nAnswer:")
        print(result["answer"])


if __name__ == "__main__":
    main()
