from app.embeddings.embedder import CodeEmbedder
from app.vectorstore.qdrant_store import QdrantStore


class CodeRetriever:
    """
    Retrieves relevant code chunks from Qdrant
    using semantic similarity.
    """

    def __init__(self):
        self.embedder = CodeEmbedder()
        self.store = QdrantStore()

    def search(self, query: str, top_k: int = 3) -> list[dict]:
        """
        Convert the query into an embedding and retrieve
        the most relevant code chunks.
        """

        if not query.strip():
            raise ValueError("Query cannot be empty.")

        query_embedding = self.embedder.embed_text(query)

        results = self.store.client.query_points(
            collection_name=self.store.COLLECTION_NAME,
            query=query_embedding,
            limit=top_k,
        )

        retrieved_chunks = []

        for result in results.points:
            payload = result.payload

            retrieved_chunks.append({
                "score": result.score,
                "file_path": payload["file_path"],
                "language": payload["language"],
                "symbol_name": payload["symbol_name"],
                "symbol_type": payload["symbol_type"],
                "start_line": payload["start_line"],
                "end_line": payload["end_line"],
                "code": payload["code"],
            })

        return retrieved_chunks