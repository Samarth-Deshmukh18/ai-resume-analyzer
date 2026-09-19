from io import BytesIO

from docx import Document


def extract_text_from_docx(file_data: bytes) -> str:
    document = Document(BytesIO(file_data))

    text_parts = []

    for paragraph in document.paragraphs:
        text = paragraph.text.strip()

        if text:
            text_parts.append(text)

    return "\n\n".join(text_parts).strip()