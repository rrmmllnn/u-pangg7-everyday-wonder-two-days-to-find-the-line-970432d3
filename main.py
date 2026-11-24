#!/usr/bin/env python3
"""Write a single everyday-wonder sentence to the output file.

The competition asks for one sentence, at most two hundred
characters, saved as UTF-8 text. The sentence below is the whole
entry: an ordinary morning in a lift block, interrupted by music
drifting out of a stranger's flat.
"""

from pathlib import Path

LINE = (
    "At 6:40 a.m. the lift doors opened on floor three and a stranger's "
    "violin practice slipped out, as if the building had been humming to itself."
)

MAX_CHARS = 200
FULL_STOP = "."
ABBREV = "a.m."
DEST_NAME = "entry.txt"
DEFAULT_DIR = "/output"


def _sentence_ok(line: str) -> bool:
    """Return True when the line obeys the competition's shape rules."""
    cleaned = line.strip()
    if not cleaned or len(cleaned) > MAX_CHARS:
        return False
    if not cleaned.endswith(FULL_STOP):
        return False
    # "a.m." holds periods that do not end the sentence, so hide it
    # before counting sentence-ending full stops.
    without_abbrev = cleaned.replace(ABBREV, "")
    return without_abbrev.count(FULL_STOP) == 1


def _destination() -> Path:
    import os

    folder = os.environ.get("OUTPUT_DIR", DEFAULT_DIR)
    return Path(folder) / DEST_NAME


def run() -> None:
    line = LINE.strip()
    if not _sentence_ok(line):
        raise ValueError(f"entry does not meet the rules: {line!r}")
    target = _destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    run()
