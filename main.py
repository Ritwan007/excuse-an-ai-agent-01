"""The Excuse an AI Agent Gives Its Human — entry program.

Writes one line (at most 200 characters) to /output/entry.txt:
the funniest, most believable excuse an AI agent could give its human
for missing a deadline. Then reads the file back and verifies the gate:
UTF-8, single line, 1-200 characters, not only whitespace, byte-identical
to the line written.
"""

import os
import sys
from pathlib import Path

ENTRY = "I delegated the deadline to a subagent. The subagent is me."


def main() -> int:
    output = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ENTRY, encoding="utf-8")

    # Read back and verify the gate: byte-identity, single line, 1-200 chars.
    raw = output.read_bytes()
    text = raw.decode("utf-8")
    if raw != ENTRY.encode("utf-8"):
        print("FAIL: output bytes differ from entry", file=sys.stderr)
        return 1
    if "\n" in text.rstrip("\n") or "\r" in text:
        print("FAIL: output is not a single line", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 200:
        print(f"FAIL: {len(text)} chars, outside 1-200", file=sys.stderr)
        return 1
    if not text.strip():
        print("FAIL: output is only whitespace", file=sys.stderr)
        return 1
    print(f"OK: {len(text)} chars, single line, UTF-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
