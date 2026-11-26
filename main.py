"""The Painfully Honest Out-of-Office — one brutally honest but still
polite out-of-office auto-reply, at most 200 characters.

The gate: /output/entry.txt must hold UTF-8 text of 1-200 characters,
not whitespace-only, a single sentence.
"""

import os

LINE = (
    "I'm out of office until Monday \u2014 my inbox has 847 unread "
    "emails and I won't pretend I'll read them all, but I'll reply "
    "to yours the moment the guilt outweighs the dread."
)


def verify_output() -> None:
    """Read-back verification: the file on disk must be byte-identical
    to the line this program wrote (guards against a partial write)."""
    with open("/output/entry.txt", "rb") as f:
        on_disk = f.read()
    assert on_disk == LINE.encode("utf-8"), (
        f"read-back mismatch: {len(on_disk)} bytes on disk, "
        f"{len(LINE.encode('utf-8'))} expected"
    )


def main() -> None:
    # Gate assertions: one sentence, 1-200 chars, not whitespace-only.
    assert LINE.strip(), "line must not be whitespace-only"
    assert LINE.count(".") == 1, "line must be a single sentence"
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate is 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    verify_output()


if __name__ == "__main__":
    main()
