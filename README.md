# RAG-flan-t5-small-LLM

# 🚀 Lightweight Open-Source RAG System

## 📌 Overview

This project demonstrates how to build a lightweight, open-source **Retrieval-Augmented Generation (RAG)** system using:

- **FastAPI** – API framework  
- **FAISS** – Vector database for similarity search  
- **SentenceTransformers (all-MiniLM-L6-v2)** – Embedding model  
- **FLAN-T5 Small** – Open-source LLM for answer generation  
- **PDF & DOCX Support** – Document ingestion  

⚡ **No paid APIs required.**

---

## ✅ Features

The system allows users to:

- 📄 Upload PDF/DOCX documents  
- 🔄 Convert documents into semantic vector embeddings  
- 🔍 Perform similarity search using FAISS  
- 🤖 Generate contextual answers using an open-source LLM  

---

## 🧠 RAG Pipeline Flow

1. 📄 Document Upload  
2. 🔎 Text Extraction (PDF/DOCX)  
3. ✂️ Token-Based Chunking (300 tokens, 50 overlap)  
4. 🧠 Embedding Generation (MiniLM – 384 dim)  
5. 🗄️ FAISS Vector Storage (IndexFlatL2)  
6. ❓ User Query  
7. 📌 Query Embedding  
8. 🎯 Top-K Semantic Retrieval  
9. 🤖 LLM Answer Generation (FLAN-T5 Small)  
10. ✅ Final Response  



---

## ⚙️ Tech Stack

| Component | Tool Used |
|------------|------------|
| API Framework | FastAPI |
| Vector Database | FAISS (IndexFlatL2) |
| Embeddings | all-MiniLM-L6-v2 (384 dimension) |
| LLM | google/flan-t5-small |
| Tokenization | bert-base-uncased |
| File Parsing | pypdf, python-docx |

---

## 🤖 LLM Configuration

### 🔹 Model Used
LLM_MODEL_NAME: str = "google/flan-t5-small"

---


## 📥 API Endpoints

### 1️⃣ Upload Document

**POST** `/rag/upload`

Uploads a PDF or DOCX file.

#### ✅ Response

#### json
{
  "message": "File processed successfully",
  "total_chunks": 4
}


### 2️⃣ Query Document

**POST** `/rag/query`

#### Request

#### json
{
  "query": "Explain about hospitals in India"
}


### 3️⃣ Clear FAISS Index

**POST** `/clear_faiss`

Clears the vector database and stored chunks.

#### ✅ Response

#### json
{
  "message": "FAISS index cleared successfully"
}


---

## 🗂 Project Structure

```text
llm-foundations-and-rag/
│
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/
│   │       │   ├── __init__.py
│   │       │   ├── search.py
│   │       │   └── upload.py
│   │       ├── __init__.py
│   │       └── api.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── documents_loader.py
│   │   ├── embeddings.py
│   │   ├── generate_chunks.py
│   │   ├── llm_generator.py
│   │   ├── save_vector.py
│   │   └── settings.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── search_services.py
│   │   └── upload_services.py
│   ├── __init__.py
│   └── main.py
├── docker-compose.yaml
├── Dockerfile
├── requirements.txt
├── LICENSE
└── README.md


