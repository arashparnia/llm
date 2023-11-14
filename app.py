# Import necessary libraries
from fastapi import FastAPI, HTTPException, Body, APIRouter
from routers.Completion import completion_router
from routers.Audio import audio_router
# Initialize FastAPI app and ChatGPTService
app = FastAPI()


app.include_router(completion_router, prefix="/completion", tags=["Completion"])
app.include_router(audio_router, prefix="/audio", tags=["Audio"])

# Main function to run the app
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
