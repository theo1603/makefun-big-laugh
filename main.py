#!/usr/bin/env python3
"""One Line, Big Laugh entry.

Writes one original funny line to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output``). Python standard library only; no network,
no randomness, fully deterministic.
"""

import os

# The joke turns twice: the speaker mocks the privacy request, then
# "helps" by buying something for the very trust issues it caused.
# Revision: cut "for my trust issues" — the weighted blanket already
# says it, so the turn lands faster and the line is tighter.
LINE = (
    "I asked my smart speaker for privacy. It whispered, "
    "\"That's adorable,\" and added a weighted blanket to my cart."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    text = LINE
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
