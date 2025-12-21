#!/usr/bin/env python3
# encoding: utf-8
# neomind verify tool
# seriki yakub, 2025

"""
Neomind Embedded Signature Verifier

Verifies a file that contains an embedded ASCII-armored PGP signature
commented at the end of the file.

Design goals:
- Transparent
- Auditable
- Deterministic
- GPG-backed (no crypto reimplementation)
"""

import sys
import subprocess
from pathlib import Path


PGP_BEGIN = "-----BEGIN PGP SIGNATURE-----"
PGP_END = "-----END PGP SIGNATURE-----"


def extract_signature(data: bytes):
    """
    Extracts embedded PGP signature from file bytes.

    Signature is expected to be commented with '#'
    and may span multiple lines.
    """
    text = data.decode("latin-1").splitlines()

    sig_lines = []
    in_sig = False
    content_end = len(text)

    for i, line in enumerate(text):
        raw = line.lstrip("#")
        if PGP_BEGIN in raw:
            in_sig = True
            sig_lines.append(raw)
            content_end = i
        elif in_sig:
            sig_lines.append(raw)
            if PGP_END in raw:
                break

    if not sig_lines:
        raise ValueError("No embedded PGP signature found")

    sig_text = "\n".join(sig_lines).encode("latin-1")
    content = "\n".join(text[:content_end]).encode("latin-1") + b"\n"

    return content, sig_text


def verify(file_path: Path):
    data = file_path.read_bytes()

    content, signature = extract_signature(data)

    unsigned_file = file_path.with_suffix(file_path.suffix + ".unsigned")
    sig_file = file_path.with_suffix(file_path.suffix + ".asc")

    unsigned_file.write_bytes(content)
    sig_file.write_bytes(signature)

    cmd = ["gpg", "--verify", str(sig_file), str(unsigned_file)]
    print(f"-> verifying {file_path.name}")

    result = subprocess.run(cmd)
    return result.returncode
 

def main():
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("waf")

    if not target.exists():
        print(f"ERROR: file not found: {target}")
        sys.exit(2)

    try:
        code = verify(target)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    sys.exit(code)


if __name__ == "__main__":
    main()
