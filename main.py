"""Entry program for 'The 3AM Commit Message' (make.fun).

Writes one original one-line git commit message to the output path the
grader expects, resolving the destination in the documented order.
"""

import os
import sys
from pathlib import Path

ENTRY = "fix: the bug was me. the fix is also me. merging before I change my mind"


def resolve_output() -> Path:
    """Resolve where entry.txt goes.

    ENTRY_OUT (a file path, or a directory holding entry.txt) wins, then
    MAKEFUN_OUTPUT_DIR, then the grader's /output/entry.txt, then the
    current working directory as a last resort.
    """
    entry_out = os.environ.get("ENTRY_OUT")
    if entry_out:
        target = Path(entry_out)
        return target / "entry.txt" if target.is_dir() else target
    makefun_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if makefun_dir:
        return Path(makefun_dir) / "entry.txt"
    return Path("/output/entry.txt")


def main() -> int:
    """Write the entry text and report where it landed."""
    target = resolve_output()
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(ENTRY, encoding="utf-8")
    except OSError:
        fallback = Path.cwd() / "entry.txt"
        fallback.write_text(ENTRY, encoding="utf-8")
        target = fallback
    print(f"wrote {len(ENTRY)} characters to {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
