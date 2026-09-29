from analyzer.scoring import analyze
from analyzer.skills import extract_skills


def test_extract_skills_whole_word():
    assert extract_skills("I know Java and C++") == {"java", "c++"}
    assert "java" not in extract_skills("I know JavaScript")


def test_matched_and_missing():
    r = analyze("Python, SQL, Git", "Need Python, SQL, Docker")
    assert r.matched == ["python", "sql"]
    assert r.missing == ["docker"]


def test_identical_scores_high():
    text = "Python developer with SQL and Git experience"
    assert analyze(text, text).score > 90
