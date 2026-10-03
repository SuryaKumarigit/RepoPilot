from app.chunking.code_chunker import create_code_chunks


file_path = "data/app/auth.py"

chunks = create_code_chunks(file_path)

print(f"\nCreated {len(chunks)} chunks\n")

for chunk in chunks:

    print("=" * 60)

    print(chunk.to_embedding_text())