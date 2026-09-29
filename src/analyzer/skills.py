"""Step 2: find known skills inside a text."""
import re

SKILLS = {
    "python", "java", "javascript", "typescript", "kotlin", "c++", "c#", "sql",
    "html", "css", "react", "node.js", "flask", "fastapi", "django", "spring",
    "android", "git", "github", "docker", "linux", "rest", "api",
    "postgresql", "mysql", "mongodb", "sqlite", "pinecone", "ollama", "rag",
    "machine learning", "nlp", "data structures", "algorithms",
    "oop", "unit testing", "agile", "networking",
}


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower())


def extract_skills(text: str) -> set[str]:
    t = normalize(text)
    found = set()
    for skill in SKILLS:
        # whole-word match; escape handles c++, c#, node.js
        if re.search(rf"(?<![a-z0-9]){re.escape(skill)}(?![a-z0-9])", t):
            found.add(skill)
    return found
