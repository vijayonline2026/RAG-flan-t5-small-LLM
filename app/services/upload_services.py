import os
import shutil
from fastapi import UploadFile, File, HTTPException
from pathlib import Path
from app.core.documents_loader import pdf_extract , docx_extract
from app.core.generate_chunks import create_chunks
from app.core.embeddings import batch_text
from app.core.save_vector import document_add

BASE_DIR = Path(__file__).resolve().parent.parent.parent
UPLOAD_DIR = BASE_DIR / "app" / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

async def upload_rag_v1(rag_file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, rag_file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(rag_file.file, buffer)

    files = os.path.splitext(rag_file.filename)
    file_extension = files[1]

    if file_extension.lower() == ".pdf":
        data = pdf_extract(file_path)
    elif file_extension.lower() == ".docx":
        data = docx_extract(file_path)
    else:
        raise HTTPException(status_code=400, detail="File extension not allowed")

    #chunking
    chunks = create_chunks(data)

    #embeddings
    embed_texts = batch_text(chunks)

    #FAISS Storage
    document_add(chunks,embed_texts)

    return {
        "message": "File processed successfully",
        "total_chunks": len(chunks)
    }