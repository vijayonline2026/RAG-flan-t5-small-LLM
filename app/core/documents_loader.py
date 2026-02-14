#Extract text from given documents to calculate total available token
from pypdf import PdfReader
from docx import Document

def pdf_extract(file_path:str) -> str:
    pdf_reader = PdfReader(file_path)
    text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n\n"
    return text

def docx_extract(file_path:str) -> str:
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])