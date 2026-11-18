#!/usr/bin/env python3
"""news-image-20261118 entry: write the day's news image to /output/entry.png.

The entry image (entry.png, in this repository) is a newspaper front-page
infographic summarising world news of Wednesday 18 November 2026, drawn with
PIL. This program has one job: copy that image to the output directory so the
grader can judge it, then check the written file is a real PNG within the
1 MiB limit. Standard library only, no network, deterministic: two
runs produce the same file.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1024 * 1024  # competition limit: 1 MiB


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    with open(dest, "rb") as f:
        header = f.read(8)
    size = os.path.getsize(dest)
    if header != PNG_SIGNATURE:
        print("error: output is not a PNG file", file=sys.stderr)
        return 1
    if size > MAX_BYTES:
        print(f"error: output is {size} bytes, over the 1 MiB limit", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({size} bytes, valid PNG)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
