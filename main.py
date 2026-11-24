#!/usr/bin/env python3
"""One Word for Your Wi-Fi entry.

Writes one original word offered as the funniest and most accurate
description of the entrant's Wi-Fi to /output/entry.txt (1-20
characters, UTF-8, a single word). Standard library only, no network,
no input.

The word is built from two fragments: a root ("Ghost" — the router
vanishes mid-call like a bad date) and a suffix ("ing" — the ongoing
act, because the Wi-Fi does it again and again). ``assemble`` joins
them into the single word; ``validate`` checks the entry gate before
anything is written: exactly one word, 1-20 characters, no spaces.
"""

from pathlib import Path

ROOT = "Ghost"
SUFFIX = "ing"

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(root: str, suffix: str) -> str:
    """Join the root and suffix fragments into one word."""
    return f"{root}{suffix}"


def validate(word: str) -> str:
    """Check the word meets the entry gate before it is written.

    Must be 1-20 characters, UTF-8-encodable, a single word with no
    whitespace at all. Raises ValueError otherwise.
    """
    if not 1 <= len(word) <= 20:
        raise ValueError(f"word must be 1-20 characters, got {len(word)}")
    if any(c.isspace() for c in word):
        raise ValueError("word must be a single word (no whitespace)")
    if not word.strip():
        raise ValueError("word must not be only whitespace")
    word.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return word


def main() -> None:
    word = validate(assemble(ROOT, SUFFIX))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(word, encoding="utf-8")


if __name__ == "__main__":
    main()
