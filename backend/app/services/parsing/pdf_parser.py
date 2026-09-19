import io

import pdfplumber
import pymupdf


def extract_text_from_pdf(file_data: bytes) -> str:
    text_parts = []

    try:
        with pdfplumber.open(io.BytesIO(file_data)) as pdf:
            for page in pdf.pages:
                text = page.extract_text()

                if text:
                    text_parts.append(text)

    except Exception:
        text_parts = []

    extracted_text = "\n\n".join(text_parts).strip()

    if extracted_text:
        return extracted_text

    # Fallback to PyMuPDF
    document = pymupdf.open(stream=file_data, filetype="pdf")

    try:
        for page in document:
            text = page.get_text()

            if text:
                text_parts.append(text)

        return "\n\n".join(text_parts).strip()

    finally:
        document.close()