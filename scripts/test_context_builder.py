from app.retrieval.retriever import CodeRetriever
from app.context.context_builder import ContextBuilder


retriever = CodeRetriever()
context_builder = ContextBuilder()


query = "How does user authentication work?"

retrieved_chunks = retriever.search(
    query=query,
    top_k=3,
)

context = context_builder.build(retrieved_chunks)


print("\n" + "=" * 80)
print("USER QUERY")
print("=" * 80)

print(query)


print("\n" + "=" * 80)
print("RETRIEVED CONTEXT")
print("=" * 80)

print(context)