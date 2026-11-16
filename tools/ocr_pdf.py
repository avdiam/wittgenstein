"""OCR a scanned PDF to text with Tesseract, one text file per page plus one joined file.

Usage: python tools/ocr_pdf.py SOURCE.pdf OUT_DIR [LANGS]

Needs PyMuPDF and Tesseract (https://github.com/UB-Mannheim/tesseract) with the
language data named in LANGS (default "ell"). Set TESSERACT and TESSDATA if they
are not in the default places. The output is for locating passages: check the
page image before quoting anything.
"""
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

import fitz

TESSERACT = os.environ.get("TESSERACT", r"C:\Program Files\Tesseract-OCR\tesseract.exe")
TESSDATA = os.environ.get("TESSDATA", os.path.expanduser(r"~\tessdata_best"))


def main():
    src, out = sys.argv[1], sys.argv[2]
    langs = sys.argv[3] if len(sys.argv) > 3 else "ell"
    os.makedirs(out, exist_ok=True)
    count = fitz.open(src).page_count

    def page(n):
        txt = os.path.join(out, f"p{n:03d}.txt")
        if os.path.exists(txt) and os.path.getsize(txt) > 0:
            return
        png = os.path.join(out, f"p{n:03d}.png")
        doc = fitz.open(src)
        pix = doc[n - 1].get_pixmap(dpi=300, colorspace=fitz.csGRAY)
        if max(pix.width, pix.height) > 4000:  # already a high-resolution scan
            pix = doc[n - 1].get_pixmap(dpi=150, colorspace=fitz.csGRAY)
        pix.save(png)
        r = subprocess.run([TESSERACT, png, "stdout", "--tessdata-dir", TESSDATA,
                            "-l", langs, "--psm", "6"], capture_output=True)
        with open(txt, "wb") as f:
            f.write(r.stdout)
        os.remove(png)

    with ThreadPoolExecutor(4) as ex:
        list(ex.map(page, range(1, count + 1)))
    with open(os.path.join(out, "all.txt"), "wb") as f:
        for n in range(1, count + 1):
            f.write(f"\n\n===== page {n} =====\n".encode())
            with open(os.path.join(out, f"p{n:03d}.txt"), "rb") as g:
                f.write(g.read())
    print("done", src, count, "pages")


if __name__ == "__main__":
    main()
