from fastapi import FastAPI, HTTPException, Request

app = FastAPI(
    title="RAG Search API",
    description="RAG Search API",
    version="1.0",
    debug=True,
    docs_url="/swagger",
    redoc_url="/documentation"
    #openapi_url=None
)