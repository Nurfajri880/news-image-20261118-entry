#!/usr/bin/env python3
"""news-image-20261118 entry: write the day's news image to /output/entry.png.

The entry image (entry.png, in this repository) is a newspaper front-page
infographic summarising world news of Wednesday 18 November 2026, drawn with
PIL. This program has one job: copy that image to the output directory so the
grader can judge it. Standard library only, no network, deterministic: two
runs produce the same file.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
