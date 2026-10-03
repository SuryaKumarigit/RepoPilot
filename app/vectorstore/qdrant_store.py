import os
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from qdrant_client.models import PointStruct


class QdrantStore:
    """
    Handles RepoPilot's interaction with Qdrant.
    """

    COLLECTION_NAME = "repopilot_code"

    VECTOR_SIZE = 384

    def __init__(self):
    
            host = os.getenv(
                "QDRANT_HOST",
                "localhost",
            )
    
            port = int(
                os.getenv(
                    "QDRANT_PORT",
                    "6333",
                )
            )
    
            self.client = QdrantClient(
                host=host,
                port=port,
            )

    def create_collection(self) -> None:
        """
        Create the RepoPilot code collection if it doesn't exist.
        """

        collections = self.client.get_collections()

        existing_collections = {
            collection.name
            for collection in collections.collections
        }

        if self.COLLECTION_NAME in existing_collections:
            print(
                f"Collection '{self.COLLECTION_NAME}' "
                "already exists."
            )
            return

        self.client.create_collection(
            collection_name=self.COLLECTION_NAME,
            vectors_config=VectorParams(
                size=self.VECTOR_SIZE,
                distance=Distance.COSINE,
            ),
        )

        print(
            f"Created collection: {self.COLLECTION_NAME}"
        ) 
    def upsert_chunks(self, chunks, embeddings) -> None:
        points = []
        for chunk, embedding in zip(chunks, embeddings):
            point = PointStruct(
               id=chunk.chunk_id,
               vector=embedding,
               payload={
                   "file_path": chunk.file_path,
                   "language": chunk.language,
                   "symbol_name": chunk.symbol_name,
                   "symbol_type": chunk.symbol_type,
                   "start_line": chunk.start_line,
                   "end_line": chunk.end_line,
                   "code": chunk.code,
                },
            )

            points.append(point)

        self.client.upsert(
            collection_name=self.COLLECTION_NAME,
            points=points,
        )

        print(
            f"Stored {len(points)} code chunks in Qdrant."
        )



    
    
        

    

    