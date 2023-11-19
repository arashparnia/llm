from pydantic import BaseModel, Field
from typing import List, Dict, Optional


class Message(BaseModel):
    role: str
    content: str
    file_ids: Optional[List[str]] = None
    metadata: Optional[Dict[str, str]] = None


class Thread(BaseModel):
    messages: Optional[List[Message]] = None
    metadata: Optional[Dict[str, str]] = None


class Run(BaseModel):
    assistant_id: str
    model: Optional[str] = None
    instructions: Optional[str] = None
    tools: Optional[List[Dict]] = None
    metadata: Optional[Dict[str, str]] = None


class ToolOutput(BaseModel):
    tool_call_id: str
    output: str


class CreateThreadRequest(BaseModel):
    assistant_id: str = Field(..., example="asst_T7HClKQYmKUNOJmxlKW79XWQ")
    thread: Optional[Dict] = Field(None, example={
        "messages": [
            {"role": "user", "content": "Explain deep learning to a 5 year old."}
        ]
    })


class CreateMessageRequest(BaseModel):
    thread_id: str = Field(..., example="")
    content: str = Field(..., example="")
