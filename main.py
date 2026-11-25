#!/usr/bin/env python3
"""One Line, Big Laugh entry.

Writes one original funny line to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output``). Python standard library only; no network,
no randomness, fully deterministic.
"""

import os

# The joke turns twice: the speaker mocks the privacy request, then
# "helps" by buying something for the very trust issues it caused.
# Revision: "whispered, 'Say no more,'" replaces "laughed and said,
# 'Of course,'" (fewer words, creepier — it fits the privacy theme),
# and "ordered me a weighted blanket" replaces "bought me a weighted
# blanket for my trust issues" (ordering it completes the betrayal,
# and the blanket already says trust issues, so the explanation is cut).
# Same turn, tighter: 126 chars down to 101.
LINE = (
    "I asked my smart speaker for privacy. It whispered, "
    "\"Say no more,\" and ordered me a weighted blanket."
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
