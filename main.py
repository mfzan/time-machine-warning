"""Write the funniest one-line time machine warning label to entry.txt.

The label is a deadpan safety notice: the machine's warranty expired
before its owner was born, and if the owner meets their own past self,
only one of them is covered -- and it is not the reader.
"""

import os
import sys

# The single entry line. 116 characters, one line, no trailing newline.
ENTRY = (
    "WARNING: Warranty expired before you were born. "
    "If you meet yourself, only one of you is covered \u2014 "
    "and it isn't you."
)

MIN_CHARS = 1
MAX_CHARS = 120


def main():
    os.umask(0o022)

    label = ENTRY
    if not label.strip():
        sys.exit("error: entry is blank")
    if "\n" in label or "\r" in label:
        sys.exit("error: entry must be a single line")
    if not MIN_CHARS <= len(label) <= MAX_CHARS:
        sys.exit(
            "error: entry is %d characters, outside the gate of %d-%d"
            % (len(label), MIN_CHARS, MAX_CHARS)
        )

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir, 0o755)

    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(label)
    os.chmod(out_path, 0o644)

    print("wrote %s (%d characters)" % (out_path, len(label)))


if __name__ == "__main__":
    main()
