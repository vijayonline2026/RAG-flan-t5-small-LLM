from app.core.llm_generator import generate_answers
from app.core.embeddings import  embed_text
from app.core.save_vector import search

async def generate_llm_answer_v1(query:str):
    #query sent for embedding
    query_embedding = embed_text(query)

    #semantic search based on query
    context = search(query_embedding, k=3)

    # send the query and semantic searched data to Mistral LLM for re-ranking the answers
    answer = generate_answers(query, context)

    return {
        "query": query,
        "retrieved_chunks": context,
        "answer": answer
    }