#!/usr/bin/env python3
"""One Line, Big Laugh entry: writes one funny line to /output/entry.txt.

Revision: "whispered" for "said" (creepier, fits the privacy theme) and
"ordered me" for "immediately bought me ... for my trust issues" —
ordering it completes the betrayal, and the blanket already says it."""

import os

# Turn twice: the speaker mocks the privacy request, then "helps" by
# buying something for the very trust issues it caused. Shorter now:
# the whisper lands faster and the order finishes the joke.
LINE = (
    "I asked my smart speaker for privacy. It whispered, "
    "'You got it,' and ordered me a weighted blanket."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    text = LINE
    # Explicit validation, not asserts: asserts are stripped with -O,
    # so a bad entry would slip through silently under python -O.
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
