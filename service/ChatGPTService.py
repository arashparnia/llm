import os
from openai import OpenAI
from typing import Dict, List, Any

from openai._base_client import HttpxBinaryResponseContent
from openai.types.beta import Thread, ThreadDeleted
from openai.types.beta.threads import ThreadMessage, Run

from models.Completion import ChatMessage


class ChatGPTService:
    """
    A service class for interacting with the OpenAI GPT-3 API to perform various tasks.

    Args:
        None

    Attributes:
        client (OpenAI): An instance of the OpenAI client for making API requests.

    Methods:
        list_models(): List available GPT-3 models.
        create_chat_completion(model, messages): Create a chat completion using GPT-3.
        create_speech(text): Generate speech from text using GPT-3.
        create_image(text, size): Generate an image from text using GPT-3.
        create_moderation(input): Perform content moderation using GPT-3.
        create_thread(): Create a new conversation thread.
        retrieve_thread(thread_id): Retrieve information about a conversation thread.
        modify_thread(thread_id): Modify a conversation thread.
        delete_thread(thread_id): Delete a conversation thread.
        create_message(thread_id, content): Create a new message in a conversation thread.
        retrieve_message(thread_id, message_id): Retrieve a specific message from a conversation thread.
        list_messages(thread_id): List all messages in a conversation thread.
        create_run(thread_id, assistant_id): Create a run within a conversation thread.
        retrieve_run(thread_id, run_id): Retrieve information about a run within a conversation thread.
        list_runs(thread_id): List all runs within a conversation thread.
        cancel_run(thread_id, run_id): Cancel a run within a conversation thread.
        create_thread_and_run(assistant_id, thread): Create a new thread and run within it.

    """

    def __init__(self):
        org_id = "org-WZf8EXH15mF8OQPNu5AaUwJp"
        open_api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=open_api_key, organization=org_id)

    def list_models(self):
        """
        List available GPT-3 models.

        Returns:
            List: A list of available GPT-3 models.
        """
        return self.client.models.list()

    def create_chat_completion(self, messages: List[dict[str, str]], model: str = "gpt-3.5-turbo-1106") -> dict[str, Any]:
        """
        Create a chat completion using GPT-3.

        Args:
            model (str): The GPT-3 model to use for completion.
            messages (List[dict[str, str]]): A list of chat messages in the conversation.
        Returns:
            dict: The response from the GPT-3 API.
        """
        response = self.client.chat.completions.create(
            model=model,
            response_format={"type": "json_object"},
            messages=messages
        ).model_dump()
        print(response)
        return response

    def create_speech(self, text: str) -> bytes:
        """
        Generate speech from text using GPT-3.

        Args:
            text (str): The text content to convert into speech.

        Returns:
            HttpxBinaryResponseContent: The generated audio data.
        """
        response = self.client.audio.speech.create(
            model="tts-1",
            voice="onyx",  # alloy, echo, fable, onyx, nova, and shimmer
            response_format='mp3',
            input=text
        )
        return response.content

    def create_image(self, text: str) -> str:
        """
        Generate an image from the given text using GPT-3.

        Args:
            text (str): The text content to use for generating the image.

        Returns:
            str: The generated image data.
        """
        text += " Make an image with No text or writing for the given scenario."
        response = self.client.images.generate(
            model="dall-e-3",
            prompt=text,
            n=1,
            size="1024x1024",
            style="natural"
        )
        # Access the URL from the first item in the 'data' list
        generated_image_url = response.data[0].url
        return generated_image_url

    def create_moderation(self, text: str) -> str:
        """
        Perform content moderation using GPT-3.

        Args:
            text (str): The content to be moderated.

        Returns:
            str: The moderated content.
        """
        response = self.client.moderations.create(input=text)
        return response["results"]

    def create_thread(self) -> Thread:
        """
        Create a new conversation thread.

        Returns:
            Thread: The created conversation thread.
        """
        return self.client.beta.threads.create()

    def retrieve_thread(self, thread_id: str) -> Thread:
        """
        Retrieve information about a conversation thread.

        Args:
            thread_id (str): The ID of the conversation thread to retrieve.

        Returns:
            Thread: Information about the conversation thread.
        """
        return self.client.beta.threads.retrieve(thread_id)

    def modify_thread(self, thread_id: str) -> Thread:
        """
        Modify a conversation thread.

        Args:
            thread_id (str): The ID of the conversation thread to modify.

        Returns:
            Thread: The modified conversation thread.
        """
        return self.client.beta.threads.update(thread_id)

    def delete_thread(self, thread_id: str) -> ThreadDeleted:
        """
        Delete a conversation thread.

        Args:
            thread_id (str): The ID of the conversation thread to delete.

        Returns:
            ThreadDeleted: Information about the deleted conversation thread.
        """
        return self.client.beta.threads.delete(thread_id)

    def create_message(self, thread_id: str, content: str) -> ThreadMessage:
        """
        Create a new message in a conversation thread.

        Args:
            thread_id (str): The ID of the conversation thread.
            content (str): The content of the message.

        Returns:
            ThreadMessage: The created message.
        """
        return self.client.beta.threads.messages.create(thread_id, role="user", content=content)

    def retrieve_message(self, thread_id: str, message_id: str) -> ThreadMessage:
        """
        Retrieve a specific message from a conversation thread.

        Args:
            thread_id (str): The ID of the conversation thread.
            message_id (str): The ID of the message to retrieve.

        Returns:
            ThreadMessage: The retrieved message.
        """
        return self.client.beta.threads.messages.retrieve(thread_id=thread_id, message_id=message_id)

    def list_messages(self, thread_id: str) -> [ThreadMessage]:
        """
        List all messages in a conversation thread.

        Args:
            thread_id (str): The ID of the conversation thread.

        Returns:
            List[ThreadMessage]: A list of messages in the conversation thread.
        """
        return self.client.beta.threads.messages.list(thread_id=thread_id)

    def create_run(self, thread_id: str, assistant_id: str) -> Run:
        """
        Create a run within a conversation thread.

        Args:
            thread_id (str): The ID of the conversation thread.
            assistant_id (str): The ID of the assistant for the run.

        Returns:
            Run: The created run.
        """
        return self.client.beta.threads.runs.create(thread_id=thread_id, assistant_id=assistant_id)

    def retrieve_run(self, thread_id: str, run_id: str) -> Run:
        """
        Retrieve information about a run within a conversation thread.

        Args:
            thread_id (str): The ID of the conversation thread.
            run_id (str): The ID of the run to retrieve.

        Returns:
            Run: Information about the run.
        """
        return self.client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)

    def list_runs(self, thread_id: str) -> [Run]:
        """
        List all runs within a conversation thread.

        Args:
            thread_id (str): The ID of the conversation thread.

        Returns:
            List[Run]: A list of runs in the conversation thread.
        """
        return self.client.beta.threads.runs.list(thread_id=thread_id)

    def cancel_run(self, thread_id: str, run_id: str) -> Run:
        """
        Cancel a run within a conversation thread.

        Args:
            thread_id (str): The ID of the conversation thread.
            run_id (str): The ID of the run to cancel.

        Returns:
            Run: Information about the canceled run.
        """
        return self.client.beta.threads.runs.cancel(thread_id=thread_id, run_id=run_id)

    def create_thread_and_run(self, assistant_id: str, thread: Dict = None) -> Run:
        """
        Create a new thread and run within it.

        Args:
            assistant_id (str): The ID of the assistant for the run.
            thread (Dict, optional): Additional thread data.

        Returns:
            Run: The created run within the new thread.
        """
        return self.client.beta.threads.create_and_run(assistant_id=assistant_id, thread=thread)
