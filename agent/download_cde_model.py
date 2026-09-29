"""Download CDE small v2 to the local model cache."""

from .embeddings import CDE_MODEL_ID, CDE_MODEL_PATH, download_cde_model


def main() -> None:
    path = download_cde_model()
    print(f"{CDE_MODEL_ID} is available locally at {path}")


if __name__ == "__main__":
    main()
