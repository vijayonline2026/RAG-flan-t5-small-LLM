from fastapi import FastAPI, HTTPException, Request

from app.core.settings import get_settings
from app.api.v1.endpoints import upload , search

settings = get_settings()
app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    debug=settings.APP_DEBUG,
    docs_url=settings.APP_SWAGGER_URL,
    redoc_url=settings.APP_REDOC_URL,
    #openapi_url=None
)

app.include_router(upload.upload_router)
app.include_router(search.srch)