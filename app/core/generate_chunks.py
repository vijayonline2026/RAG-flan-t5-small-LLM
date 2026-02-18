#creates chunks based on total tokens and provided check size and overlap limit
from app.core.settings import get_settings
from transformers import AutoTokenizer

settings = get_settings()
tokenizer = AutoTokenizer.from_pretrained(settings.LLM_MODEL_NAME)

def create_chunks(text:str , chunk_size:int = settings.CHUNK_LIMIT, overlap:int = settings.CHUNK_OVERLAP_LIMIT):
    tokens = tokenizer.encode(text)
    chunks = []
    start = 0
    while start < len(tokens):
        end = start + chunk_size
        chunk_text = tokens[start:end]
        chunk_data = tokenizer.decode(chunk_text)
        chunks.append(chunk_data)
        #start += end - overlap
        start += chunk_size - overlap
    return chunks