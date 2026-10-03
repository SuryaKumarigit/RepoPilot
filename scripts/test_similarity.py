import torch

from app.embeddings.embedder import CodeEmbedder


embedder = CodeEmbedder()


texts = [
    "How does user authentication work?",
    "Where are users authenticated?",
    "How is the database connection created?",
]


embeddings = embedder.embed_texts(texts)


vectors = torch.tensor(embeddings)


similarity = torch.mm(vectors, vectors.T)


print("\nSimilarity Matrix:\n")
print(similarity)