import os
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security.api_key import APIKeyHeader, APIKeyCookie, APIKeyQuery

API_KEY_NAME = "access_token"
API_KEY = os.getenv("API_KEY")

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
api_key_cookie = APIKeyCookie(name=API_KEY_NAME, auto_error=False)
api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)


async def get_api_key(
        api_key_header: str = Depends(api_key_header),
        api_key_cookie: str = Depends(api_key_cookie),
        api_key_query: str = Depends(api_key_query),
):
    if api_key_header == API_KEY:
        return api_key_header
    elif api_key_cookie == API_KEY:
        return api_key_cookie
    elif api_key_query == API_KEY:
        return api_key_query
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate API key"
        )
