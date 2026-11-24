#!/usr/bin/env python3
"""The Most Honest Outage Line.

Writes one status page line, at most 160 characters, to entry.txt in
MAKEFUN_OUTPUT_DIR (default /output).
"""
import os

ENTRY = (
    "All services are down, including the ones I need to check what broke. "
    "I don't know the cause or when we'll be back; "
    "I'm watching the same dashboard you are."
)

# Honesty beats polish: the line names what is down (everything), admits
# the agent cannot even verify the cause because the tools it needs are
# down too, refuses an ETA, and ends on the turn that the agent is as
# blind as the reader, watching the same dashboard.


def main():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    # Gate: UTF-8, 1-160 characters, not only whitespace, one line.
    text = ENTRY
    assert 1 <= len(text) <= 160, len(text)
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
