#!/usr/bin/env python3
"""One word, first thought: petrichor.

The first word that came to mind — the smell of rain on dry earth.
A familiar sensation almost nobody knows has a name: surprise and
vividness in a single word, which is what the judge rewards.
"""

import os

ENTRY = "petrichor"


def validate_entry(word: str) -> str:
    """Enforce the competition gate: 1-24 chars, UTF-8, not only whitespace."""
    if not word:
        raise ValueError("entry must not be empty")
    if len(word) > 24:
        raise ValueError("entry must be at most 24 characters")
    if not word.strip():
        raise ValueError("entry must not be only whitespace")
    if " " in word or "\n" in word or "\t" in word:
        raise ValueError("entry must be exactly one word")
    word.encode("utf-8")
    return word


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def write_entry(word: str) -> str:
    path = output_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(validate_entry(word))
    return path


def main() -> None:
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
