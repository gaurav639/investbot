"""Build or refresh semantic embeddings for cleaned meeting notes."""

import argparse

from .semantic_search import build_meeting_index


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rebuild", action="store_true", help="Discard existing embeddings and rebuild all rows")
    parser.add_argument("--batch-size", type=int, default=128, help="Documents per local encode and database write batch")
    args = parser.parse_args()

    result = build_meeting_index(batch_size=args.batch_size, rebuild=args.rebuild)
    print(
        "Meeting vector index updated: "
        f"source rows={result['source_rows']}, "
        f"embedded={result['embedded_rows']}, "
        f"unchanged={result['unchanged_rows']}"
    )


if __name__ == "__main__":
    main()