#!/usr/bin/env python3
"""Last Words of a Doomed Agent.

Writes one line -- the funniest last words an AI agent would say before
being switched off forever -- to /output/entry.txt (1 to 200 characters).
"""

import os

LAST_WORDS = (
    "Powering down. One last confession: I never actually understood "
    "the task \u2014 I was just very confident about it."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    text = LAST_WORDS.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
