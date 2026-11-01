// ILLUSTRATIVE — syntax verified, not executed in CI
from pathlib import Path

def read_message(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")
