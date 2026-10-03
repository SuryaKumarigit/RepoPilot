import os

from dotenv import load_dotenv
from google import genai


load_dotenv()


class LLMClient:
    """
    Handles communication with the LLM.
    """

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY environment variable is not set."
            )

        self.client = genai.Client(api_key=api_key)

        self.model = "gemini-3.8-flash"

    def generate(self, prompt: str) -> str:
        """
        Generate a response from the LLM.
        """

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        return response.text