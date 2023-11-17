# Import necessary libraries
from fastapi import FastAPI, HTTPException, Body, APIRouter
from routers.Completion import completion_router
from routers.Audio import audio_router
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security.api_key import APIKeyHeader, APIKeyCookie, APIKeyQuery
from ApiKey import get_api_key
# Initialize FastAPI app and ChatGPTService
app = FastAPI(dependencies=[Depends(get_api_key)])


app.include_router(completion_router, prefix="/completion", tags=["Completion"])
app.include_router(audio_router, prefix="/audio", tags=["Audio"])

# Health Check Endpoint
@app.get("/")
def health_check():
    return {"status": "healthy"}


# Main function to run the app
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
