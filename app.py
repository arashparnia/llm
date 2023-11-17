from fastapi import FastAPI, HTTPException, Body, APIRouter, Depends, status
from fastapi.security.api_key import APIKeyHeader, APIKeyCookie, APIKeyQuery
from ApiKey import get_api_key
from routers.Completion import completion_router
from routers.Audio import audio_router

# Initialize FastAPI app without global dependencies
app = FastAPI()

# Include your routers with the API key dependency
app.include_router(completion_router, prefix="/completion", tags=["Completion"], dependencies=[Depends(get_api_key)])
app.include_router(audio_router, prefix="/audio", tags=["Audio"], dependencies=[Depends(get_api_key)])

# Health Check Endpoint (no API key required)
@app.get("/")
def health_check():
    return {"status": "healthy"}

# Main function to run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
