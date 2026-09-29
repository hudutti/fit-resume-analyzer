# fit-resume-analyzer

Scores how well a resume fits a job description.

## How it works
1. Extract text from resume and job (PDF/DOCX/TXT)
2. Detect known skills in both
3. Skill coverage = matched skills / job skills
4. Text similarity = TF-IDF cosine similarity
5. Score = 60% skill coverage + 40% text similarity

## Setup
```
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

## Run
```
set PYTHONPATH=src            # Windows cmd (PowerShell: $env:PYTHONPATH="src")
python -m analyzer.cli data/samples/resume.txt data/samples/job.txt
```

## Test
```
pytest
```
