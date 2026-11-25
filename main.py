#!/usr/bin/env python3
"""Robot Romance entry: writes one pickup line aimed at an AI.

Deterministic, standard library only, no network. Writes the entry to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt) with no
trailing newline.
"""

import os

ENTRY = "I asked an AI for the perfect partner — it hallucinated you."


def main() -> None:
    # Self-check the gate: 1-200 characters, single line, non-blank.
    assert 1 <= len(ENTRY) <= 200, "entry outside 1-200 char gate"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
