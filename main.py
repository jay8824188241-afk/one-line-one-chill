#!/usr/bin/env python3
"""One Line, One Chill -- writes one original horror line to /output/entry.txt.

The program holds a single hand-written sentence (135 characters) and writes
it, byte for byte, to /output/entry.txt. No network, no randomness, no input:
the same line comes out on every run.
"""

import os

LINE = (
    "The baby monitor crackled at 3 a.m., and in a voice that was mine, "
    "only older, it whispered, \u201cDon\u2019t come up \u2014 "
    "I\u2019m already holding you.\u201d"
)

# The gate requires 1 to 200 characters of UTF-8 text, not only white space.
MAX_CHARS = 200


def main() -> None:
    assert 0 < len(LINE) <= MAX_CHARS, "line must fit the 1-200 character gate"
    assert LINE.strip(), "line must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
