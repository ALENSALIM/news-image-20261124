#!/usr/bin/env python3
"""Write the bundled front-page image to the output directory.

Copies the entry.png bundled next to this script to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output), creating the output
directory if needed. Verifies the copy matches the bundled file by size
and by SHA-256 hash, then prints the byte count and hash of the copy.

Standard library only. No network access.
"""

import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def _sha256(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)

    src_size = os.path.getsize(SRC)
    dst_size = os.path.getsize(dst)
    if dst_size != src_size:
        raise SystemExit(
            "size mismatch: copied %d bytes, expected %d" % (dst_size, src_size)
        )

    src_hash = _sha256(SRC)
    dst_hash = _sha256(dst)
    if dst_hash != src_hash:
        raise SystemExit("sha256 mismatch: copy differs from bundled entry.png")

    print("wrote %s (%d bytes)" % (dst, dst_size))
    print("sha256: %s" % dst_hash)


if __name__ == "__main__":
    main()
