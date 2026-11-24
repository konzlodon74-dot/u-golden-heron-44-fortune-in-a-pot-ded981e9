#!/usr/bin/env python3
"""Fortune in a Pot.

Writes one line -- a kind, funny fortune for the houseplant on the
windowsill -- to /output/entry.txt. Stdlib only, deterministic.
"""

import os

# The fortune, composed for this plant in this window: repotting framed
# as a promotion -- a small joke a plant lover laughs at, not a pun --
# with the cadence of a prediction ("Soon you will..."), warm toward
# the plant and its keeper, and no doom or withering anywhere in it.
FORTUNE = (
    "Soon you will be promoted to a bigger pot on this very "
    "windowsill, with a view worth every leaf you have grown."
)


def main() -> None:
    if not 1 <= len(FORTUNE) <= 120:
        raise ValueError("fortune must be 1-120 characters")
    if "\n" in FORTUNE or FORTUNE != FORTUNE.strip():
        raise ValueError("fortune must be exactly one line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)
    # Print exactly the one line, so running the program shows its entry.
    print(FORTUNE)


if __name__ == "__main__":
    main()
