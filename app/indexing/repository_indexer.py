from app.ingestion.scanner import scan_repository
from app.chunking.code_chunker import create_code_chunks
from app.embeddings.embedder import CodeEmbedder
from app.vectorstore.qdrant_store import QdrantStore


class RepositoryIndexer:
    """
    Indexes an entire repository into Qdrant.
    """

    def __init__(self):
        self.embedder = CodeEmbedder()
        self.store = QdrantStore()

    def index_repository(self, repository_path: str) -> None:
        """
        Scan, chunk, embed, and store a repository.
        """

        print("\nScanning repository...")

        files = scan_repository(repository_path)

        print(f"Found {len(files)} source files.")

        all_chunks = []

        for file_path in files:

            # Currently our parser supports Python.
            if file_path.suffix.lower() != ".py":
                continue

            print(f"Processing: {file_path}")

            chunks = create_code_chunks(str(file_path))

            all_chunks.extend(chunks)

        print(f"\nCreated {len(all_chunks)} code chunks.")

        if not all_chunks:
            print("No code chunks found.")
            return

        print("\nGenerating embeddings...")

        texts = [
            chunk.to_embedding_text()
            for chunk in all_chunks
        ]

        embeddings = self.embedder.embed_texts(texts)

        print("Embeddings generated.")

        print("\nCreating Qdrant collection...")

        self.store.create_collection()

        print("\nStoring chunks in Qdrant...")

        self.store.upsert_chunks(
            all_chunks,
            embeddings,
        )

        print("\nRepository indexing completed.")