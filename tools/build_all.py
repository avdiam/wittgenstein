#!/usr/bin/env python3
"""Run every generator of the site in one go.

    python tools/build_all.py            # rebuild everything generated
    python tools/build_all.py --check    # exit 1 if anything is out of date

Generated files:
    docs/tractatus.html   (the full analysis between the FULL-ANALYSIS markers)
    docs/essay.html       (the whole page)
    docs/Logiki_Glossa_Michanes.docx
"""
import subprocess
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
SCRIPTS = ["build_html.py", "build_essay_html.py", "build_docx.py"]


def main():
    args = ["--check"] if "--check" in sys.argv else []
    failed = []
    for name in SCRIPTS:
        result = subprocess.run([sys.executable, str(TOOLS / name), *args])
        if result.returncode != 0:
            failed.append(name)
    if failed:
        print("FAILED: " + ", ".join(failed))
        sys.exit(1)


if __name__ == "__main__":
    main()
