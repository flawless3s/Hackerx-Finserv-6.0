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
    

if __name__ == "__main__":
    pdf_path = "sem-1.pdf"
    text = extract_text_from_pdf(pdf_path)
    print(text[:1000])
    doc_path = "FINAL YEAR SYNOPSIS.docx"
    text_doc = extract_text_from_docx(doc_path)
    print(text_doc[:1000])
    
