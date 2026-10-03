from app.vectorstore.qdrant_store import QdrantStore


store = QdrantStore()

store.create_collection()