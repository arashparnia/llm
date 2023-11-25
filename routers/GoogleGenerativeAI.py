from fastapi import APIRouter
from pydantic import BaseModel
from service.GoogleGenerativeAI import GoogleGenerativeAIWrapper

# Define the request model for generating text
class GenerateTextRequest(BaseModel):
    prompt: str

GoogleGenerativeAI_router = APIRouter()
google_generative_ai_service = GoogleGenerativeAIWrapper()
@GoogleGenerativeAI_router.post("/generate_text")
async def generate_text(request: GenerateTextRequest):
    response = google_generative_ai_service.generate_text(request.prompt)
    return response


class GenerateExerciseRequest(BaseModel):
    age: int = 4
    difficulty: int = 50
    scenario: str = "Farm"
    character: str = "Sheep"


@GoogleGenerativeAI_router.post("/generate_exercise")
async def generate_exercise(request: GenerateExerciseRequest):
    response = google_generative_ai_service.generate_exercise(request.age, request.difficulty, request.scenario,
                                                 request.character)
    return response
