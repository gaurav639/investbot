"""Build deterministic client, group, deal, RM, and company aliases."""

from agent.entity_resolver import build_entity_aliases


def main() -> None:
    count = build_entity_aliases()
    print(f"Refreshed {count:,} entity aliases in cleaned.entity_alias")


if __name__ == "__main__":
    main()