# To store chunks data as vector id and search the data from Vector data base (FAISS)
import faiss
import numpy as np
from app.core.settings import get_settings

settings = get_settings()

dimension = settings.FAISS_VECTOR_DIMENSION
index = faiss.IndexFlatL2(dimension)
documents = []
"""
astype('float32') - converts the incoming number to float 32 compatible format for FAISS
"""
def document_add(chunks : list[str], embeddings) :
    global documents
    index.add(np.array(embeddings).astype('float32'))
    documents.extend(chunks)

def search(query_embedding, k:int = 3):
    if index.ntotal == 0:
        raise ValueError("FAISS index is empty. Upload documents first.")

    print("Searching... FAISS vectors:", index.ntotal)
    print("Query embedding shape:", query_embedding.shape)

    query_vector = np.array([query_embedding]).astype("float32")
    print("Reshaped query:", query_vector.shape)

    distances, values = index.search(query_vector, k)

    return [documents[value] for value in values[0] if value < len(documents)]


