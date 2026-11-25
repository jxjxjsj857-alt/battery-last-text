"""The Battery's Last Text to Its Charger.

Writes the phone battery's final text message to /output/entry.txt:
one line of plain text, at most 200 characters.
"""

from pathlib import Path

ENTRY = (
    "hey. it's me, 1%. waited all day by the outlet while you charged "
    "your laptop, your watch, your toothbrush \u2014 everything but me. "
    "don't reply, i'm already seeing the power bank."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} characters to {out}")


if __name__ == "__main__":
    main()
