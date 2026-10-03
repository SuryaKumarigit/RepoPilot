from app.embeddings.embedder import CodeEmbedder


embedder = CodeEmbedder()


texts = [
    "How does user authentication work?",
    "Where are users authenticated?",
    "How is the database connection created?",
    "What is the weather today?",
]


embeddings = embedder.embed_texts(texts)


print("\nEmbedding Results\n")


for text, embedding in zip(texts, embeddings):

    print("=" * 60)

    print(f"Text: {text}")
    print(f"Dimensions: {len(embedding)}")
    print(f"First 5 values: {embedding[:5]}")