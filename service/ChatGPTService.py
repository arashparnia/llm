import os
from pathlib import Path

import openai
from typing import Dict, Optional, List

from models.Completion import ChatMessage
from openai import OpenAI


class ChatGPTService:
    def __init__(self):
        org_id = "org-WZf8EXH15mF8OQPNu5AaUwJp"
        open_api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=open_api_key, organization=org_id, )

    def list_models(self):
        return self.client.models.list()

    def create_chat_completion(self, model: str, messages: List[ChatMessage]):
        formatted_messages = [message.model_dump() for message in messages]
        response = self.client.chat.completions.create(model=model, response_format={"type": "json_object"},
                                                       messages=formatted_messages)
        return response

    def create_speech(self, text: str) -> bytes:
        response = openai.Audio.speech.create(
            model="tts-1",
            voice="alloy",  # alloy, echo, fable, onyx, nova, and shimmer
            response_format='aac',
            input=text
        )
        return response["data"]

    #
    # def create_thread(self, messages: Optional[Dict] = None, metadata: Optional[Dict] = None) -> Dict:
    #     return openai.Thread.create(messages=messages, metadata=metadata)
    #
    # def retrieve_thread(self, thread_id: str) -> Dict:
    #     return openai.Thread.retrieve(id=thread_id)
    #
    # def modify_thread(self, thread_id: str, metadata: Dict) -> Dict:
    #     return openai.Thread.modify(id=thread_id, metadata=metadata)
    #
    # def delete_thread(self, thread_id: str) -> Dict:
    #     return openai.Thread.delete(id=thread_id)
    #
    # def create_message(self, thread_id: str, role: str, content: str, file_ids: Optional[List[str]] = None, metadata: Optional[Dict] = None) -> Dict:
    #     return openai.Message.create(thread_id=thread_id, role=role, content=content, file_ids=file_ids, metadata=metadata)
    #
    # def retrieve_message(self, thread_id: str, message_id: str) -> Dict:
    #     return openai.Message.retrieve(thread_id=thread_id, id=message_id)
    #
    # def modify_message(self, thread_id: str, message_id: str, metadata: Dict) -> Dict:
    #     return openai.Message.modify(thread_id=thread_id, id=message_id, metadata=metadata)
    #
    # def list_messages(self, thread_id: str, limit: Optional[int] = 20, order: Optional[str] = "desc", after: Optional[str] = None, before: Optional[str] = None) -> Dict:
    #     return openai.Message.list(thread_id=thread_id, limit=limit, order=order, after=after, before=before)
    #
    # def create_run(self, thread_id: str, assistant_id: str, model: Optional[str] = None,
    #                instructions: Optional[str] = None, tools: Optional[List[Dict]] = None,
    #                metadata: Optional[Dict] = None) -> Dict:
    #     return openai.ThreadRun.create(thread_id=thread_id, assistant_id=assistant_id, model=model,
    #                                    instructions=instructions, tools=tools, metadata=metadata)
    #
    # def retrieve_run(self, thread_id: str, run_id: str) -> Dict:
    #     return openai.ThreadRun.retrieve(thread_id=thread_id, id=run_id)
    #
    # def modify_run(self, thread_id: str, run_id: str, metadata: Dict) -> Dict:
    #     return openai.ThreadRun.update(thread_id=thread_id, id=run_id, metadata=metadata)
    #
    # def list_runs(self, thread_id: str, limit: Optional[int] = 20, order: Optional[str] = "desc",
    #               after: Optional[str] = None, before: Optional[str] = None) -> Dict:
    #     return openai.ThreadRun.list(thread_id=thread_id, limit=limit, order=order, after=after, before=before)
    #
    # def submit_tool_outputs_to_run(self, thread_id: str, run_id: str, tool_outputs: List[Dict]) -> Dict:
    #     return openai.ThreadRun.submit_tool_outputs(thread_id=thread_id, run_id=run_id, tool_outputs=tool_outputs)
    #
    # def cancel_run(self, thread_id: str, run_id: str) -> Dict:
    #     return openai.ThreadRun.cancel(thread_id=thread_id, run_id=run_id)
    #
    # def create_thread_and_run(self, assistant_id: str, thread: Optional[Dict] = None, model: Optional[str] = None,
    #                           instructions: Optional[str] = None, tools: Optional[List[Dict]] = None,
    #                           metadata: Optional[Dict] = None) -> Dict:
    #     return openai.Thread.create_and_run(assistant_id=assistant_id, thread=thread, model=model,
    #                                         instructions=instructions, tools=tools, metadata=metadata)
    #
    # def retrieve_run_step(self, thread_id: str, run_id: str, step_id: str) -> Dict:
    #     return openai.ThreadRunStep.retrieve(thread_id=thread_id, run_id=run_id, id=step_id)
    #
    # def list_run_steps(self, thread_id: str, run_id: str, limit: Optional[int] = 20, order: Optional[str] = "desc",
    #                    after: Optional[str] = None, before: Optional[str] = None) -> Dict:
    #     return openai.ThreadRunStep.list(thread_id=thread_id, run_id=run_id, limit=limit, order=order, after=after,
    #                                      before=before)
