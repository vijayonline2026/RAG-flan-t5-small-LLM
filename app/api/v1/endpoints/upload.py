from fastapi import APIRouter, File, UploadFile
from app.core.save_vector import index, documents
from app.services.upload_services import upload_rag_v1
upload_router = APIRouter()

@upload_router.post("/rag/upload")
async def upload_rag_file(rag_file: UploadFile = File(...)):
    try:
        return await upload_rag_v1(rag_file)
    except Exception as e:
        return e.__str__()

@upload_router.post("/clear_faiss")
def clear_index():
    index.reset()      # removes all vectors
    documents.clear()  # removes stored texts
    return {"message": "FAISS index cleared successfully"}