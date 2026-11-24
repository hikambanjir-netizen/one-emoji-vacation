#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

Writes exactly one emoji -- the torii gate (U+26E9, SHINTO SHRINE) --
to /output/entry.txt. One codepoint, nothing else: no variation selector,
no newline, no extra bytes. The torii gate is the dream trip itself:
Kyoto, Japan, seen at a glance.
"""

import os

EMOJI = "\u26e9"  # SHINTO SHRINE (torii gate) -- one codepoint


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Self-check: the file must hold exactly one codepoint, U+26E9,
    # encoded as UTF-8 with no variation selector and no newline.
    expected = EMOJI.encode("utf-8")
    with open(path, "rb") as f:
        actual = f.read()
    if actual != expected:
        raise SystemExit(
            "entry.txt mismatch: got %d bytes %r, expected %d bytes %r"
            % (len(actual), actual, len(expected), expected)
        )


if __name__ == "__main__":
    main()
