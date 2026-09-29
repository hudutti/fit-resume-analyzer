"""Step 1: turn a resume/job file into plain text."""
from pathlib import Path

import pdfplumber
from docx import Document


def read_text(path: str) -> str:
    p = Path(path)
    suffix = p.suffix.lower()
    if suffix == ".pdf":
        with pdfplumber.open(p) as pdf:
            return "\n".join((page.extract_text() or "") for page in pdf.pages)
    if suffix == ".docx":
        return "\n".join(par.text for par in Document(str(p)).paragraphs)
    if suffix in (".txt", ".md"):
        return p.read_text(encoding="utf-8")
    raise ValueError(f"Unsupported file type: {suffix}")
