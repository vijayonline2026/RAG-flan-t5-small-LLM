from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_text(text:str):
    embeddings = model.encode(text, convert_to_numpy=True)
    return embeddings

def batch_text(texts:list[str]):
    embeddings = model.encode(texts)
    return embeddings
