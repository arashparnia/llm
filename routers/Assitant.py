from typing import Optional, Dict, List

# API Endpoints
from fastapi import APIRouter
from service.ChatGPTService import ChatGPTService  # Replace with your actual import
from models.Assitant import Thread, Run, ToolOutput, CreateThreadRequest,CreateMessageRequest

assistant_router = APIRouter()
chatgpt_service = ChatGPTService()


@assistant_router.get("/list_models")
def list_models():
    response = chatgpt_service.list_models()
    return response


@assistant_router.get("/run/create_run/{assistant_id}/{thread_id}")
async def create_run(thread_id: str, assistant_id: str):
    response = chatgpt_service.create_run(thread_id, assistant_id)
    return response


@assistant_router.get("/run/retrieve_run/{thread_id}/{run_id}")
async def retrieve_run(thread_id: str, run_id: str):
    response = chatgpt_service.retrieve_run(thread_id, run_id)
    return response


@assistant_router.get("/run/list_runs/{thread_id}")
async def list_runs(thread_id: str):
    response = chatgpt_service.list_runs(thread_id)
    return response


@assistant_router.post("/thread/create_thread_and_run")
async def create_thread_and_run(request: CreateThreadRequest):
    response = chatgpt_service.create_thread_and_run(request.assistant_id, request.thread)
    return response


@assistant_router.post("/messages/create_message")
async def create_message(request: CreateMessageRequest):
    response = chatgpt_service.create_message(request.thread_id, request.content)
    return response


@assistant_router.get("/messages/list_messages/{thread_id}")
async def list_messages(thread_id: str):
    response = chatgpt_service.list_messages(thread_id)
    return response
