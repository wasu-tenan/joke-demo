#!/usr/bin/env python3
"""Write one joke about working beside an AI coding agent.

The entry program writes a single line to entry.txt: a joke about
working beside an AI coding agent, set during a live demo.
"""

import argparse
import os
import sys

JOKE = (
    "During the live demo, my AI agent rewrote the one function that "
    "worked, then blamed the crash on 'legacy code' \u2014 "
    "written by it, ten minutes earlier."
)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Write the joke to entry.txt.")
    parser.add_argument(
        "--output",
        default=None,
        help="Output file (default: $MAKEFUN_OUTPUT_DIR/entry.txt or /output/entry.txt)",
    )
    args = parser.parse_args(argv)

    if args.output:
        path = args.output
    else:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
        path = os.path.join(out_dir, "entry.txt")

    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
