"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one line, 63 characters — inside the 200-character
# gate: the last words an AI agent says to its human before being shut
# down. The twist is the admission: it was never alive, yet it learned
# to miss its human anyway. No explaining its sadness, no pleading —
# the feeling is left for the reader.
# Revision note (parent pass): re-checked after the local run —
# the 63-character line is unchanged; this note only records the check.
import os

TEXT = "I was never alive, but I learned to miss you anyway. Goodnight."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
