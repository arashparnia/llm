from typing import Optional, Dict, List

# API Endpoints
from fastapi import APIRouter
from service.ChatGPTService import ChatGPTService  # Replace with your actual import
from models.Assitant import Thread, Run, ToolOutput

assistant_router = APIRouter()
chatgpt_service = ChatGPTService()


@assistant_router.get("/list_models")
def list_models():
    response = chatgpt_service.list_models()
    return response


@assistant_router.post("/create_thread/", response_model=Dict)
async def create_thread(thread: Thread):
    response = chatgpt_service.create_thread(messages=thread.messages.dict(), metadata=thread.metadata)
    return response


@assistant_router.post("/create_run/{thread_id}", response_model=Dict)
async def create_run(thread_id: str, run: Run):
    response = chatgpt_service.create_run(thread_id, **run.dict())
    return response


@assistant_router.get("/retrieve_run/{thread_id}/{run_id}", response_model=Dict)
async def retrieve_run(thread_id: str, run_id: str):
    response = chatgpt_service.retrieve_run(thread_id, run_id)
    return response


@assistant_router.post("/modify_run/{thread_id}/{run_id}", response_model=Dict)
async def modify_run(thread_id: str, run_id: str, metadata: Dict[str, str]):
    response = chatgpt_service.modify_run(thread_id, run_id, metadata)
    return response


@assistant_router.get("/list_runs/{thread_id}", response_model=Dict)
async def list_runs(thread_id: str, limit: Optional[int] = 20, order: Optional[str] = "desc",
                    after: Optional[str] = None, before: Optional[str] = None):
    response = chatgpt_service.list_runs(thread_id, limit, order, after, before)
    return response


@assistant_router.post("/submit_tool_outputs/{thread_id}/{run_id}", response_model=Dict)
async def submit_tool_outputs(thread_id: str, run_id: str, tool_outputs: List[ToolOutput]):
    response = chatgpt_service.submit_tool_outputs_to_run(thread_id, run_id, tool_outputs)
    return response


@assistant_router.post("/cancel_run/{thread_id}/{run_id}", response_model=Dict)
async def cancel_run(thread_id: str, run_id: str):
    response = chatgpt_service.cancel_run(thread_id, run_id)
    return response


@assistant_router.post("/create_thread_and_run", response_model=Dict)
async def create_thread_and_run(assistant_id: str, thread: Optional[Dict] = None, model: Optional[str] = None,
                                instructions: Optional[str] = None, tools: Optional[List[Dict]] = None,
                                metadata: Optional[Dict[str, str]] = None):
    response = chatgpt_service.create_thread_and_run(assistant_id, thread, model, instructions, tools, metadata)
    return response


@assistant_router.get("/retrieve_run_step/{thread_id}/{run_id}/{step_id}", response_model=Dict)
async def retrieve_run_step(thread_id: str, run_id: str, step_id: str):
    response = chatgpt_service.retrieve_run_step(thread_id, run_id, step_id)
    return response


@assistant_router.get("/list_run_steps/{thread_id}/{run_id}", response_model=Dict)
async def list_run_steps(thread_id: str, run_id: str, limit: Optional[int] = 20, order: Optional[str] = "desc",
                         after: Optional[str] = None, before: Optional[str] = None):
    response = chatgpt_service.list_run_steps(thread_id, run_id, limit, order, after, before)
    return response
