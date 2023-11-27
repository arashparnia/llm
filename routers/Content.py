# API Endpoints
from fastapi import HTTPException, APIRouter, Body

from service.ChatGPTService import ChatGPTService  # Replace with your actual import
from service.GoogleGenerativeAI import GoogleGenerativeAIWrapper
from models.Completion import CompletionRequest
from service.factories.ChatGPTServiceFactory import ChatGPTServiceFactory
from service.factories.GoogleGenerativeAIServiceFactory import GoogleGenerativeAIServiceFactory
from service.ExerciseGenerator import ExerciseGenerator

chatgpt_service = ChatGPTService()
google_generative_ai_service = GoogleGenerativeAIWrapper()
content_router = APIRouter()


@content_router.post('/generate-content')
def generate_content(service_type: str, content_type: str, params: dict = Body(...)):
    try:
        # Choose the correct factory based on the service type
        if service_type == "ChatGPT":
            factory = ChatGPTServiceFactory(chatgpt_service)
        elif service_type == "GoogleGenerativeAI":
            factory = GoogleGenerativeAIServiceFactory(google_generative_ai_service)
        else:
            raise HTTPException(status_code=400, detail="Invalid service type")

        exercise_generator = ExerciseGenerator(factory)

        # Generate content based on content type
        if content_type == "story":
            content = exercise_generator.generate_story(**params)
        elif content_type == "exercise":
            content = exercise_generator.generate_exercise(**params)
        elif content_type == "multiple_choice_question":
            content = exercise_generator.generate_multiple_choice_question(**params)
        else:
            raise HTTPException(status_code=400, detail="Invalid content type")

        return {"content": content}

    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Missing parameter: {str(e)}")

    # Additional error handling and response formatting
    # ...
