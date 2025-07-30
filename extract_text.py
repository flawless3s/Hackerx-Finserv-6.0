import fitz  # PyMuPDF

def extract_text_from_pdf(path):
    try:
        with fitz.open(path) as doc:
            return "\n".join([page.get_text() for page in doc])
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

if __name__ == "__main__":
    pdf_path = "sem-1.pdf"
    text = extract_text_from_pdf(pdf_path)
    print(text[:1000])
