from fastapi import APIRouter
from pydantic import BaseModel
from service.GPT4AllService import GPT4AllWrapper  # Replace with your actual import


# Define the request model for generating text
class GenerateTextRequest(BaseModel):
    prompt: str
    max_tokens: int = 50


gpt4all_router = APIRouter()
gpt4all_service = GPT4AllWrapper("orca-mini-3b-gguf2-q4_0.gguf")  # Replace with your desired model name
# gpt4all_service = GPT4AllWrapper("nous-hermes-llama2-13b.Q4_0.gguf")  # Replace with your desired model name


@gpt4all_router.post("/generate_text")
async def generate_text(request: GenerateTextRequest):
    response = gpt4all_service.generate_text(request.prompt, request.max_tokens)
    return response


class GenerateExerciseRequest(BaseModel):
    age: int = 4
    difficulty: int = 50
    scenario: str = "Farm"
    character: str = "Sheep"


@gpt4all_router.post("/generate_exercise")
async def generate_exercise(request: GenerateExerciseRequest):
    response = gpt4all_service.generate_exercise(request.age, request.difficulty, request.scenario,
                                                 request.character)
    return response
