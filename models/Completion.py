from pydantic import BaseModel, Field
from typing import List, Dict, Optional


# Pydantic Model
class ChatMessage(BaseModel):
    role: str
    content: str


class CompletionRequest(BaseModel):
    model: str
    messages: List[ChatMessage]
