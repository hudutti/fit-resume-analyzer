"""Step 3: compute the fit score."""
from dataclasses import dataclass

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .skills import extract_skills, normalize

SKILL_WEIGHT = 0.6
TEXT_WEIGHT = 0.4


@dataclass
class Result:
    score: float
    matched: list[str]
    missing: list[str]
    skill_coverage: float
    text_similarity: float


def analyze(resume_text: str, job_text: str) -> Result:
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    matched = sorted(resume_skills & job_skills)
    missing = sorted(job_skills - resume_skills)
    coverage = len(matched) / len(job_skills) if job_skills else 0.0

    vec = TfidfVectorizer(stop_words="english")
    matrix = vec.fit_transform([normalize(resume_text), normalize(job_text)])
    similarity = float(cosine_similarity(matrix[0], matrix[1])[0][0])

    score = 100 * (SKILL_WEIGHT * coverage + TEXT_WEIGHT * similarity)
    return Result(round(score, 1), matched, missing, coverage, similarity)
