class ContextBuilder:
    """
    Converts retrieved code chunks into
    structured context for an LLM.
    """

    def build(self, retrieved_chunks: list[dict]) -> str:
        """
        Build a readable context string from
        retrieved code chunks.
        """

        if not retrieved_chunks:
            return "No relevant code was found."

        context_parts = []

        for index, chunk in enumerate(retrieved_chunks, start=1):

            section = (
                f"\n--- Retrieved Code {index} ---\n\n"
                f"File: {chunk['file_path']}\n"
                f"Language: {chunk['language']}\n"
                f"Symbol: {chunk['symbol_name']}\n"
                f"Type: {chunk['symbol_type']}\n"
                f"Lines: {chunk['start_line']}-{chunk['end_line']}\n"
                f"Relevance Score: {chunk['score']:.4f}\n\n"
                f"Code:\n"
                f"```{chunk['language']}\n"
                f"{chunk['code']}\n"
                f"```\n"
            )

        context_parts.append(section)

        return "\n".join(context_parts)