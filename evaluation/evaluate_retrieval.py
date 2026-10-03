from app.retrieval.retriever import CodeRetriever
from evaluation.questions import EVALUATION_QUESTIONS


def evaluate():

    retriever = CodeRetriever()

    total = len(EVALUATION_QUESTIONS)
    passed = 0

    print("\nRepoPilot Retrieval Evaluation")
    print("=" * 70)

    for item in EVALUATION_QUESTIONS:

        question = item["question"]

        results = retriever.search(
            query=question,
            top_k=5,
        )

        symbols = {
            result["symbol_name"]
            for result in results
        }

        files = {
            result["file_path"]
            for result in results
        }

        expected_symbols = set(
            item["expected_symbols"]
        )

        expected_files = set(
            item["expected_files"]
        )

        symbol_match = expected_symbols.intersection(
            symbols
        )

        file_match = any(
            expected_file in file
            for expected_file in expected_files
            for file in files
        )

        success = bool(symbol_match or file_match)

        if success:
            passed += 1

        print(f"\nQuestion: {question}")
        print(f"Expected symbols: {expected_symbols}")
        print(f"Retrieved symbols: {symbols}")
        print(f"Result: {'PASS' if success else 'FAIL'}")

    accuracy = passed / total

    print("\n" + "=" * 70)
    print(f"Passed: {passed}/{total}")
    print(f"Retrieval accuracy: {accuracy:.2%}")


if __name__ == "__main__":
    evaluate()