from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from app.core.settings import get_settings

settings = get_settings()

tokenizer = AutoTokenizer.from_pretrained(settings.LLM_MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(settings.LLM_MODEL_NAME)

def generate_answers(query: str, context: list[str]):

    context_text = "\n".join(context)

    base_prompt = f"""
Answer the question using the context below.

Context:
{context_text}

Question:
{query}
"""

    # Tokenize first
    tokens = tokenizer.encode(base_prompt)

    print("PROMPT TOKEN COUNT BEFORE TRIM:", len(tokens))

    # Hard trim to 480 (leave space for generation safety)
    if len(tokens) > 480:
        tokens = tokens[:480]

    trimmed_prompt = tokenizer.decode(tokens)

    inputs = tokenizer(trimmed_prompt, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_new_tokens=settings.MAX_NEW_TOKENS
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

