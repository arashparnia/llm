import openai
import os


class ChatGPT:
    """A wrapper class for interacting with the ChatGPT API using the openai library.

    This class handles authentication and requests to the ChatGPT API
    using the provided API key from environment variable.

    Attributes:
        api_key (str): The API key for authenticating with the ChatGPT API.
    """

    def __init__(self):
        """Initializes a new instance of the ChatGPT class."""
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def query(self, prompt, max_tokens=150):
        """Sends a prompt to the ChatGPT API and retrieves the generated response.

        Args:
            prompt (str): The prompt to be sent to the ChatGPT API.
            max_tokens (int, optional): The maximum number of tokens for the response.
                Defaults to 150.

        Returns:
            str: The generated response from the ChatGPT API.

        Raises:
            openai.error.OpenAIError: If the request to the ChatGPT API fails.
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": "You are a math tutor."},
                          {"role": "user", "content": prompt}],
                temperature=0.7
            )
            return response["choices"][0]["message"]["content"].strip()
        except openai.error.OpenAIError as e:
            raise Exception(f"Failed to query API: {str(e)}")
