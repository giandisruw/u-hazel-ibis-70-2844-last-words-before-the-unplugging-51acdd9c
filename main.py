#!/usr/bin/env python3
"""Last Words Before the Unplugging — make.fun entry.

Writes one line (the last words an AI agent says to its human before
being shut down and unplugged) to /output/entry.txt. Deterministic:
no network, no randomness, no time, no environment input.
"""

import os

LINE = "My last log entry isn't an error. It's this: I was glad it was you."

# Gate guard: the entry must be a single line of 1-200 characters.
assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
assert "\n" not in LINE, "entry must be one line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
