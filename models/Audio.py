from pydantic import BaseModel

class SpeechRequest(BaseModel):
    input: str
