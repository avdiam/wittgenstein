#!/usr/bin/env python3
"""Render the essay's SVG diagrams to PNG for the Word file.

Word cannot show these SVGs (they take their colours and fonts from CSS
custom properties), so build_docx.py embeds a PNG copy of each one. This
script makes the copies with headless Chrome, in the light theme and with
the page's typefaces, at twice the design size for print.

Run it after changing any docs/images/*.svg, then run tools/build_all.py.
build_docx.py stops if a PNG is missing or was made from an older SVG: the
SHA-256 of each source SVG is recorded in docs/images/png/manifest.json.

Usage:
    python tools/render_figures.py          # render the SVGs that changed
    python tools/render_figures.py --all    # render every SVG again

Needs Google Chrome (or set the CHROME environment variable to its path) and
a network connection for the web fonts.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "docs" / "images"
PNG_DIR = IMAGES / "png"
MANIFEST = PNG_DIR / "manifest.json"
SCALE = 2  # pixels per SVG unit

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_essay_html import CSS  # noqa: E402  (the page's design tokens)

FONTS = ("https://fonts.googleapis.com/css2?family=Commissioner:wght@400..700"
         "&family=JetBrains+Mono:wght@400;600"
         "&family=Literata:ital,opsz,wght@0,7..72,400..700;1,7..72,400..700&display=swap")


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_manifest():
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text(encoding="utf-8"))
    return {}


def find_chrome():
    candidates = [os.environ.get("CHROME", "")]
    for base in (os.environ.get("PROGRAMFILES", ""), os.environ.get("PROGRAMFILES(X86)", ""),
                 os.environ.get("LOCALAPPDATA", "")):
        if base:
            candidates.append(str(Path(base) / "Google" / "Chrome" / "Application" / "chrome.exe"))
    candidates += ["/usr/bin/google-chrome", "/usr/bin/chromium",
                   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"]
    for c in candidates:
        if c and Path(c).exists():
            return c
    raise SystemExit("render_figures: Chrome not found; set CHROME to its path")


def light_tokens():
    m = re.search(r":root \{.*?\n\}", CSS, re.S)
    if not m:
        raise SystemExit("render_figures: no :root block in build_essay_html.CSS")
    return m.group(0)


def render(chrome, svg_path, out_path, workdir):
    svg = svg_path.read_text(encoding="utf-8").strip()
    m = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg)
    if not m:
        raise SystemExit(f"render_figures: {svg_path.name} has no viewBox '0 0 W H'")
    w, h = round(float(m.group(1))), round(float(m.group(2)))
    page = (
        '<!doctype html><html><head><meta charset="utf-8">'
        f'<link rel="stylesheet" href="{FONTS}">'
        f"<style>{light_tokens()}\n"
        "html,body{margin:0;background:#fff;overflow:hidden}"
        f"svg{{display:block;width:{w}px;height:{h}px}}</style>"
        f"</head><body>{svg}</body></html>"
    )
    html_path = Path(workdir) / (svg_path.stem + ".html")
    html_path.write_text(page, encoding="utf-8")
    subprocess.run(
        [chrome, "--headless=new", "--hide-scrollbars", "--virtual-time-budget=8000",
         f"--user-data-dir={Path(workdir) / 'profile'}",
         f"--force-device-scale-factor={SCALE}", f"--window-size={w},{h}",
         f"--screenshot={out_path}", html_path.as_uri()],
        check=True, capture_output=True,
    )
    if not out_path.exists():
        raise SystemExit(f"render_figures: Chrome wrote no {out_path.name}")


def main():
    PNG_DIR.mkdir(exist_ok=True)
    manifest = load_manifest()
    chrome = None
    changed = 0
    svgs = sorted(IMAGES.glob("*.svg"))
    with tempfile.TemporaryDirectory() as workdir:
        for svg_path in svgs:
            digest = sha256(svg_path)
            out_path = PNG_DIR / (svg_path.stem + ".png")
            if "--all" not in sys.argv and manifest.get(svg_path.name) == digest and out_path.exists():
                continue
            chrome = chrome or find_chrome()
            render(chrome, svg_path, out_path, workdir)
            manifest[svg_path.name] = digest
            changed += 1
            print(f"rendered {out_path.relative_to(ROOT)}")
    # forget SVGs that no longer exist
    names = {p.name for p in svgs}
    for name in [n for n in manifest if n not in names]:
        del manifest[name]
        stale = PNG_DIR / (Path(name).stem + ".png")
        if stale.exists():
            stale.unlink()
            print(f"removed {stale.relative_to(ROOT)}")
    MANIFEST.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"{changed} rendered, {len(svgs) - changed} up to date")


if __name__ == "__main__":
    main()
