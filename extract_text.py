import fitz # PyMuPDF
from docx import Document  

def extract_text_from_pdf(path):
    try:
        with fitz.open(path) as doc:
            return "\n".join([page.get_text() for page in doc])
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

def extract_text_from_docx(path):
    try:
        doc = Document(path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)
    except Exception as e:
        print(f"Error reading Word Doc: {e}")
        return ""
    

    
