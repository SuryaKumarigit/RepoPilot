from app.context.context_builder import ContextBuilder
from app.llm.client import LLMClient
from prompts.codebase_prompt import build_prompt
from app.retrieval.retriever import CodeRetriever


query = "How does the payment processing system work?"


retriever = CodeRetriever()
context_builder = ContextBuilder()
llm = LLMClient()


results = retriever.search(
    query=query,
    top_k=3,
)


context = context_builder.build(results)


prompt = build_prompt(
    query=query,
    context=context,
)


answer = llm.generate(prompt)


print("\n" + "=" * 80)
print("HALLUCINATION TEST")
print("=" * 80)

print("\nQuestion:")
print(query)

print("\nAnswer:")
print(answer)