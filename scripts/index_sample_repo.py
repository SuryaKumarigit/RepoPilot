from app.chunking.code_chunker import create_code_chunks
from app.embeddings.embedder import CodeEmbedder
from app.vectorstore.qdrant_store import QdrantStore


file_path = "data/app/auth.py"


# 1. Create code chunks
chunks = create_code_chunks(file_path)

print(f"Created {len(chunks)} chunks")


# 2. Create embedding model
embedder = CodeEmbedder()


# 3. Convert chunks into embedding text
texts = [
    chunk.to_embedding_text()
    for chunk in chunks
]


# 4. Generate embeddings
embeddings = embedder.embed_texts(texts)


# 5. Connect to Qdrant
store = QdrantStore()


# 6. Create collection
store.create_collection()


# 7. Store chunks
store.upsert_chunks(
    chunks,
    embeddings,
)