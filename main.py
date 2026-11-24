#!/usr/bin/env python3
"""One Word, First Thought.

The entry is a single word: the first thought on waking up, when the
brain has not finished loading yet. It prints exactly that word and
writes it to /output/entry.txt, nothing else.
"""

import os

ENTRY = "Buffering"


def main():
    assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry must be 1-200 non-blank chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
