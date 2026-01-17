import pdfplumber
import docx
import os

def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return extract_pdf(file_path)
    elif ext == ".docx":
        return extract_docx(file_path)
    else:
        raise ValueError("Unsupported file format")

def extract_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()
    return text.lower()

def extract_docx(path):
    doc = docx.Document(path)
    return " ".join(p.text for p in doc.paragraphs).lower()
