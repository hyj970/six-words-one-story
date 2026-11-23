#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes exactly one six-word story to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: constant output, no randomness, no network, no time.
"""

import os

STORY = "She kept his letters. Burned mine."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(STORY + "\n")

if __name__ == "__main__":
    main()
