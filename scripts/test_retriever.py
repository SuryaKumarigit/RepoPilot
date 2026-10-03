from app.retrieval.retriever import CodeRetriever


retriever = CodeRetriever()

queries = [
    "How does user authentication work?",
    "Where is the database connection created?",
    "How is a new user created?",
]


for query in queries:

    print("\n" + "=" * 80)
    print(f"QUERY: {query}")
    print("=" * 80)

    results = retriever.search(query, top_k=2)

    for index, result in enumerate(results, start=1):

        print(f"\nResult {index}")
        print(f"Score: {result['score']:.4f}")
        print(f"File: {result['file_path']}")
        print(f"Symbol: {result['symbol_name']}")
        print(
            f"Lines: "
            f"{result['start_line']}-{result['end_line']}"
        )

        print("\nCode:")
        print(result["code"])