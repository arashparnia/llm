from fastapi import FastAPI, HTTPException, Body, APIRouter, Depends, status,Request
from fastapi.security.api_key import APIKeyHeader, APIKeyCookie, APIKeyQuery
import logging


from APILogger import APILogger
from ApiKey import get_api_key
from routers.Content import content_router
from routers.Completion import completion_router
from routers.Audio import audio_router
from routers.Assitant import assistant_router
from routers.GoogleGenerativeAI import  GoogleGenerativeAI_router
from block_path import blocked_paths
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
# Initialize FastAPI app without global dependencies
app = FastAPI()
# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# Include your routers with the API key dependency
app.include_router(content_router, prefix="/content", tags=["Content"], dependencies=[Depends(get_api_key)])
app.include_router(completion_router, prefix="/completion", tags=["Completion"], dependencies=[Depends(get_api_key)])
app.include_router(audio_router, prefix="/audio", tags=["Audio"], dependencies=[Depends(get_api_key)])
app.include_router(assistant_router, prefix="/assistant", tags=["Assistant"], dependencies=[Depends(get_api_key)])
app.include_router(GoogleGenerativeAI_router, prefix="/GoogleGenerativeAI", tags=["GoogleGenerativeAI"], dependencies=[Depends(get_api_key)])

app_logger = APILogger("app")
@app.middleware("http")
async def log_requests(request: Request, call_next):
    return await app_logger.log_request(request, call_next)




@app.middleware("http")
async def block_404_requests(request: Request, call_next):
    if request.url.path in blocked_paths:
        raise HTTPException(status_code=403, detail="Forbidden")
    response = await call_next(request)
    return response

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve files from the 'static' directory under the '/static' route
app.mount("/", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root():
    return FileResponse('static/index.html')


# Health Check Endpoint (no API key required)
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Main function to run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
