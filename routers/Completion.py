# API Endpoints
from fastapi import HTTPException, APIRouter
from service.ChatGPTService import ChatGPTService  # Replace with your actual import
from models.Completion import CompletionRequest

chatgpt_service = ChatGPTService()

completion_router = APIRouter()

@completion_router.get("/list_models")
def list_models():
    response = chatgpt_service.list_models()
    return response

@completion_router.post("/create")
def create_completion(request: CompletionRequest):
    try:
        response = chatgpt_service.create_chat_completion(model=request.model, messages=request.messages)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
