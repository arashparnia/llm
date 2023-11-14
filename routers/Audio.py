# API Endpoints

from fastapi import FastAPI, HTTPException, APIRouter, Response
from models.Audio import SpeechRequest
from service.ChatGPTService import ChatGPTService

chatgpt_service = ChatGPTService()

audio_router = APIRouter()


@audio_router.post("/create_speech")
def create_speech(request: SpeechRequest):
    try:
        audio_data = chatgpt_service.create_speech(request.input)
        return Response(content=audio_data, media_type="audio/mpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
