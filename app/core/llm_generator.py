import torch
from sympy.physics.units import temperature
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from app.core.settings import get_settings

settings = get_settings()

tokenizer = AutoTokenizer.from_pretrained(settings.LLM_MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(settings.LLM_MODEL_NAME)

def generate_answers(query:str,context:list[str]):
    prompt = f"""
    Answer the question using the context below.

    Context:
    {'\n'.join(context)}

    Question:
    {query}
    """

    """ Below commented one is for Mistral LLM model """
    # inputs = tokenizer(prompt,return_tensor="pt").to(model.device)
    # outputs = model.generate(**inputs, max_new_tokens=settings.MAX_NEW_TOKENS ,temperature=settings.TEMPERATURE)

    """ This for Google LLM model - learning purposes """
    inputs = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_new_tokens=150
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

