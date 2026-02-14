from fastapi import APIRouter
from app.services.search_services import generate_llm_answer_v1

srch = APIRouter()

@srch.post("/search", tags=["search"])
async def search(query:str):
    try:
        return await generate_llm_answer_v1(query)
    except Exception as e:
        return e.__str__()