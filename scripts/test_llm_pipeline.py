from app.context.context_builder import ContextBuilder
from app.llm.client import LLMClient
from prompts.codebase_prompt import build_prompt
from app.retrieval.retriever import CodeRetriever


retriever = CodeRetriever()
context_builder = ContextBuilder()
llm = LLMClient()


queries = [
    "How does user authentication work?",
    "How is a new user created?",
    "What happens when the login function is called?",
]


for query in queries:

    print("\n" + "=" * 80)
    print(f"QUESTION: {query}")
    print("=" * 80)

    # Retrieve
    retrieved_chunks = retriever.search(
        query=query,
        top_k=3,
    )

    # Build context
    context = context_builder.build(
        retrieved_chunks
    )

    # Build prompt
    prompt = build_prompt(
        query=query,
        context=context,
    )

    # Generate answer
    answer = llm.generate(prompt)

    print("\nREPOPILOT ANSWER:\n")
    print(answer)