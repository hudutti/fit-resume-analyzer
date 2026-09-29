"""Step 4: command-line entry point."""
import argparse

from .parser import read_text
from .scoring import analyze


def main() -> None:
    ap = argparse.ArgumentParser(description="Score how well a resume fits a job.")
    ap.add_argument("resume", help="path to resume (.pdf/.docx/.txt)")
    ap.add_argument("job", help="path to job description (.pdf/.docx/.txt)")
    args = ap.parse_args()

    r = analyze(read_text(args.resume), read_text(args.job))
    print(f"Fit score:        {r.score}/100")
    print(f"Skill coverage:   {r.skill_coverage:.0%}")
    print(f"Text similarity:  {r.text_similarity:.0%}")
    print(f"Matched skills:   {', '.join(r.matched) or '-'}")
    print(f"Missing skills:   {', '.join(r.missing) or '-'}")


if __name__ == "__main__":
    main()
