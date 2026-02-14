from sentence_transformers import SentenceTransformer
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_text(text:str):
    embeddings = model.encode(text, convert_to_numpy=True)
    return embeddings

def batch_text(texts: list[str]):
    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        truncation=True,
        max_length=256
    )
    return embeddings
