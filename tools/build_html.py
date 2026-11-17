#!/usr/bin/env python3
"""Inject the full Markdown analysis into the interactive HTML page.

The Markdown file is the single source of truth for the analysis text.
This script renders every `##` section of it and injects the result into the
matching <section> of the HTML, between FULL-ANALYSIS markers. Everything
outside those markers (hand-written summaries, labs, scripts) is left alone.

Usage:
    python tools/build_html.py            # rebuild the HTML in place
    python tools/build_html.py --check    # exit 1 if the HTML is out of date

Requires: markdown-it-py  (pip install markdown-it-py)
"""
import hashlib
import html
import re
import sys
from pathlib import Path

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent.parent
DOC_DIR = ROOT / "Tractatus Logico-Philosophicus"
MD_PATH = DOC_DIR / "TRACTATUS_LOGICO_PHILOSOPHICUS_ANALYSIS_1-7.md"
HTML_PATH = ROOT / "docs" / "tractatus.html"  # published by GitHub Pages

KATEX = "https://cdn.jsdelivr.net/npm/katex@0.16.9/dist"


# --------------------------------------------------------------------------
# 1. Markdown sections -> target HTML section ids
# --------------------------------------------------------------------------
def target_for(heading):
    """Which HTML <section id> a `##` heading of the Markdown belongs to."""
    if heading.startswith("Πλήρης"):
        return None  # subtitle line, no body
    if heading.startswith(("Εισαγωγή", "Μέρος Α")):
        return "sec-intro"
    if heading.startswith("Μέρος Β"):
        return "sec-decimal"
    m = re.match(r"Πρόταση ([1-7])\b", heading)
    if m:
        return "sec-prop" + m.group(1)
    if heading.startswith(("Μέρος Γ", "Ιστορικό επίμετρο", "Βιβλιογραφία")):
        return "sec-epilogue"
    raise SystemExit(
        f"build_html: no HTML section mapped for Markdown heading '## {heading}'. "
        "Add it to target_for()."
    )


def split_sections(md):
    """Yield (heading, body) for every `##` section, ignoring fenced code."""
    sections, heading, buf, fenced = [], None, [], False
    for line in md.split("\n"):
        if line.lstrip().startswith("```"):
            fenced = not fenced
        if not fenced and line.startswith("## "):
            if heading is not None:
                sections.append((heading, "\n".join(buf)))
            heading, buf = line[3:].strip(), []
        elif heading is not None:
            buf.append(line)
    if heading is not None:
        sections.append((heading, "\n".join(buf)))
    return sections


# --------------------------------------------------------------------------
# 2. Markdown -> HTML (math is protected, then emitted for KaTeX)
# --------------------------------------------------------------------------
MD = MarkdownIt("commonmark", {"html": True}).enable("table")


def protect_math(text, store):
    """Replace $...$ / $$...$$ with placeholders outside fenced code blocks."""

    def keep(tex, display):
        store.append((tex.strip(), display))
        return f"@@M{len(store) - 1}@@"

    out, fenced = [], False
    # work fence-by-fence so ASCII diagrams are never touched
    parts = re.split(r"(^[ \t]*```.*$)", text, flags=re.M)
    for part in parts:
        if re.match(r"^[ \t]*```", part):
            fenced = not fenced
            out.append(part)
            continue
        if fenced:
            out.append(part)
            continue
        # `$...$` written as a code span is still math
        part = re.sub(r"`\$([^`$]+)\$`", lambda m: keep(m.group(1), False), part)
        part = re.sub(r"\$\$(.+?)\$\$", lambda m: keep(m.group(1), True), part, flags=re.S)
        part = re.sub(r"(?<!\\)\$(?!\s)([^$\n]+?)(?<!\s)\$", lambda m: keep(m.group(1), False), part)
        out.append(part)
    return "".join(out)


def render_section(heading, body, prefix):
    store = []
    src = f"## {heading}\n\n{body}".rstrip()
    src = re.sub(r"\n---\s*$", "", src)  # trailing rule between sections
    out = MD.render(protect_math(src, store))

    # headings: shift one level down (the page section already owns the <h2>)
    counter = [0]

    def heading_tag(m):
        level, inner = int(m.group(1)), m.group(2)
        counter[0] += 1
        return (f'<h{level + 1} class="fa-h{level}" id="{prefix}-h{counter[0]}">'
                f"{inner}</h{level + 1}>")

    out = re.sub(r"<h([2-4])>(.*?)</h\1>", heading_tag, out, flags=re.S)
    out = out.replace("<table>", '<div class="fa-table-wrap"><table class="hw-table">')
    out = out.replace("</table>", "</table></div>")
    out = out.replace("<blockquote>", '<blockquote class="hw-quote">')
    out = out.replace("<pre>", '<pre class="fa-pre">')
    # leading proposition numbers become clickable like the rest of the page
    out = re.sub(
        r"<strong>([1-7](?:\.\d+)?)(?=[\s:<(–,])",
        r'<strong><span class="hw-prop-num">\1</span>',
        out,
    )

    def math_tag(m):
        tex, display = store[int(m.group(1))]
        cls = "tex tex-display" if display else "tex"
        return f'<span class="{cls}">{html.escape(tex)}</span>'

    out = re.sub(r"@@M(\d+)@@", math_tag, out)
    leftovers = re.findall(r"\*\*|@@M\d+@@", re.sub(r"<pre.*?</pre>", "", out, flags=re.S))
    return out, leftovers


# --------------------------------------------------------------------------
# 3. Static blocks injected once (styles, toolbar, runtime)
# --------------------------------------------------------------------------
HEAD_BLOCK = f"""<link rel="stylesheet" href="{KATEX}/katex.min.css">
<style>
  /* The full analysis is the long reading text: it sits on the page itself,
     between two rules, and is not boxed. */
  .full-analysis {{ margin-top: 2rem; }}
  body .full-analysis.hw-panel {{ background: transparent; border-radius: 0;
    border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); }}
  /* Closed, it is a tinted band with an action, so that it is not passed over. */
  body .full-analysis.hw-panel:not([open]) {{ background: var(--primary-soft);
    border: 1px solid var(--primary); border-radius: var(--radius); }}
  .full-analysis {{ scroll-margin-top: 8rem; }}
  .full-analysis > summary {{
    display: flex; align-items: center; gap: 0.75rem; list-style: none;
    cursor: pointer; padding: 0.9rem 0.25rem; font-family: var(--font-sans);
    color: var(--primary); user-select: none;
  }}
  .full-analysis:not([open]) > summary {{ padding: 0.95rem 1rem; }}
  .fa-sum-text {{ flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 0.15rem; }}
  .fa-sum-title {{ font-size: 1rem; font-weight: 650; line-height: 1.35; }}
  .fa-sum-desc {{ font-size: 0.8rem; font-weight: 400; line-height: 1.45;
    color: var(--muted-foreground); }}
  .fa-sum-action {{ flex: none; font-size: 0.78rem; font-weight: 600; padding: 0.35rem 0.75rem;
    border: 1px solid var(--primary); border-radius: var(--radius);
    background-color: var(--card); color: var(--primary); }}
  .full-analysis:not([open]) .fa-when-open,
  .full-analysis[open] .fa-when-closed {{ display: none; }}
  /* The line under a section title that says the full text exists. */
  .fa-pointer {{ margin-top: 0.6rem; font-family: var(--font-sans); font-size: 0.82rem;
    line-height: 1.5; color: var(--muted-foreground); }}
  .fa-pointer a {{ color: var(--primary); font-weight: 600; text-decoration: underline;
    text-underline-offset: 3px; }}
  .full-analysis > summary::-webkit-details-marker {{ display: none; }}
  .full-analysis > summary::before {{
    content: ""; flex: none; width: 0.45rem; height: 0.45rem; margin-left: 0.15rem;
    border-right: 1.5px solid currentColor; border-bottom: 1.5px solid currentColor;
    transform: rotate(-45deg); transition: transform 0.15s ease;
  }}
  .full-analysis[open] > summary::before {{ transform: rotate(45deg); }}
  .full-analysis > summary:hover {{ background-color: var(--primary-soft); }}
  .fa-body {{ padding: 0.25rem 0 1.5rem; overflow-wrap: anywhere; }}
  .fa-body p {{ margin: 0.75rem 0; }}
  .fa-body [id] {{ scroll-margin-top: 8rem; }}
  .fa-body ul {{ list-style: disc; padding-left: 1.35rem; margin: 0.5rem 0; }}
  .fa-body ol {{ list-style: decimal; padding-left: 1.5rem; margin: 0.5rem 0; }}
  .fa-body ul ul {{ list-style: circle; }}
  .fa-body li {{ margin: 0.35rem 0; }}
  .fa-body hr {{ border: 0; border-top: 1px solid var(--border); margin: 2.2rem 0; }}
  .fa-body :is(.fa-h2, .fa-h3, .fa-h4) {{ font-family: var(--font-sans); line-height: 1.4;
    max-width: 52ch; text-wrap: balance; }}
  .fa-body .fa-h2 {{ font-size: 1.05rem; font-weight: 650; letter-spacing: 0.03em;
    margin: 2.4rem 0 0.9rem; padding-bottom: 0.5rem; border-bottom: 1px solid var(--foreground); }}
  .fa-body .fa-h3 {{ font-size: 1rem; font-weight: 650; margin: 2rem 0 0.6rem; }}
  .fa-body .fa-h4 {{ font-size: 0.9rem; font-weight: 600; margin: 1.4rem 0 0.4rem;
    color: var(--muted-foreground); }}
  .fa-body code {{ font-size: 0.84em; background-color: var(--secondary);
    padding: 0.08em 0.32em; border-radius: 3px; }}
  .fa-body .fa-pre {{ overflow-x: auto; padding: 0.9rem 1rem; margin: 1rem 0;
    background-color: var(--secondary); border-radius: var(--radius);
    font-size: 0.76rem; line-height: 1.35; }}
  .fa-body .fa-pre code {{ background: none; padding: 0; font-size: inherit; }}
  .fa-body .fa-table-wrap {{ overflow-x: auto; margin: 1.1rem 0; }}
  .fa-body .hw-quote p {{ margin: 0.3rem 0; }}
  .fa-body .tex-display {{ display: block; overflow-x: auto; overflow-y: hidden; margin: 0.9rem 0; text-align: center; }}
  .fa-body .tex:not(.tex-done) {{ font-family: var(--font-mono); font-size: 0.85em; }}
  .fa-body .katex {{ font-size: 1.04em; }}
  .fa-toolbar {{ display: flex; flex-wrap: wrap; align-items: center; gap: 0.6rem;
    font-size: 0.78rem; color: var(--muted-foreground); }}
</style>"""

TOOLBAR_BLOCK = """<div class="fa-toolbar">
  <button type="button" class="hw-btn px-2.5 py-1" onclick="faSetAll(true)">Ανάπτυξη όλων των πλήρων αναλύσεων</button>
  <button type="button" class="hw-btn px-2.5 py-1" onclick="faSetAll(false)">Σύμπτυξη</button>
  <span>Κάθε ενότητα έχει στο τέλος της την «Πλήρη Ανάλυση», όπως παράγεται από το αρχείο Markdown.</span>
</div>"""

TAIL_BLOCK = f"""<script defer src="{KATEX}/katex.min.js"></script>
<script>
  // Full-analysis blocks: math rendering, expand/collapse, search integration.
  function faRenderMath(root) {{
    if (!window.katex) return;
    root.querySelectorAll('.tex:not(.tex-done)').forEach(function (el) {{
      var tex = el.textContent;
      try {{
        window.katex.render(tex, el, {{ displayMode: el.classList.contains('tex-display'), throwOnError: false }});
      }} catch (e) {{ el.textContent = tex; }}
      el.classList.add('tex-done');
    }});
  }}
  function faOpen(id) {{
    var d = document.getElementById(id);
    if (!d) return true;
    d.open = true;
    d.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
    return false;
  }}
  function faSetAll(open) {{
    document.querySelectorAll('details.full-analysis').forEach(function (d) {{ d.open = open; }});
  }}
  window.addEventListener('load', function () {{
    var blocks = Array.prototype.slice.call(document.querySelectorAll('details.full-analysis'));
    blocks.forEach(function (d) {{
      d.addEventListener('toggle', function () {{ if (d.open) faRenderMath(d); }});
    }});
    // render in the background so a later search never meets raw LaTeX
    (function next(i) {{
      if (i >= blocks.length) return;
      faRenderMath(blocks[i]);
      setTimeout(function () {{ next(i + 1); }}, 30);
    }})(0);
  }});
  // The page search reads visible text only: open the blocks before it runs.
  document.addEventListener('input', function (e) {{
    if (e.target && e.target.id === 'globalSearchInput' && e.target.value.trim()) faSetAll(true);
  }}, true);
</script>"""


# --------------------------------------------------------------------------
# 4. Injection
# --------------------------------------------------------------------------
# What the summary line of each full-analysis block says: (title, contents).
# For the seven propositions the range is read from the Markdown heading.
FA_LABELS = {
    "sec-intro": ("Πλήρης ανάλυση της εισαγωγής",
                  "Οι τρεις εκδόσεις, η αφιέρωση, το μότο, ο πρόλογος και η εισαγωγή του Russell"),
    "sec-decimal": ("Πλήρης ανάλυση του δεκαδικού συστήματος",
                    "Η αρίθμηση, η υποσημείωση 1* και ο χάρτης των 526 προτάσεων"),
    "sec-epilogue": ("Πλήρης ανάλυση: πίνακες αναφοράς, ιστορικό επίμετρο και βιβλιογραφία",
                     "Το τριμερές σχήμα του νοήματος, η σύνοψη των 7 προτάσεων, "
                     "η πορεία προς τις «Φιλοσοφικές Έρευνες» και οι πηγές"),
}


def fa_label(target, heading):
    """(title, contents) for the summary line of a section's full analysis."""
    if target in FA_LABELS:
        return FA_LABELS[target]
    n = target[-1]
    m = re.search(r"\((\d[\d.]* – \d[\d.]*)\)\s*$", heading)
    if m:
        return (f"Πλήρης ανάλυση της πρότασης {n}",
                f"Οι προτάσεις {m.group(1)} κλάδο προς κλάδο, με σχολιασμό, παραδείγματα και πίνακες")
    return (f"Πλήρης ανάλυση της πρότασης {n}",
            f"Η πρόταση {n} στις τρεις εκδόσεις, με σχολιασμό")


def word_count(rendered):
    """Words of the rendered text, to the nearest hundred, as «≈ 5.400 λέξεις»."""
    n = len(re.sub(r"<[^>]+>", " ", rendered).split())
    n = max(100, int(round(n / 100.0)) * 100)
    return "≈ " + f"{n:,}".replace(",", ".") + " λέξεις"


def insert_after_line(page, needle, text, start=0):
    i = page.find(needle, start)
    if i < 0:
        raise SystemExit(f"build_html: could not find {needle!r} in the HTML")
    line_end = page.find("\n", i) + 1
    return page[:line_end] + text + page[line_end:]


def strip_generated(page):
    return re.sub(r"[ \t]*<!-- FULL-ANALYSIS:BEGIN [^>]*-->.*?<!-- FULL-ANALYSIS:END [^>]*-->\n?",
                  "", page, flags=re.S)


def block(name, content, indent=""):
    body = "\n".join(indent + line if line else line for line in content.split("\n"))
    return (f"{indent}<!-- FULL-ANALYSIS:BEGIN {name} (generated by tools/build_html.py — do not edit) -->\n"
            f"{body}\n{indent}<!-- FULL-ANALYSIS:END {name} -->\n")


def insert_before(page, needle, text, start=0):
    i = page.find(needle, start)
    if i < 0:
        raise SystemExit(f"build_html: could not find {needle!r} in the HTML")
    line_start = page.rfind("\n", 0, i) + 1
    return page[:line_start] + text + page[line_start:]


def build():
    md = MD_PATH.read_text(encoding="utf8").replace("\r\n", "\n")
    raw = HTML_PATH.read_bytes().decode("utf8")
    crlf = "\r\n" in raw
    page = strip_generated(raw.replace("\r\n", "\n"))
    digest = hashlib.sha256(md.encode("utf8")).hexdigest()[:12]

    grouped, warnings, first_heading = {}, [], {}
    for heading, body in split_sections(md):
        target = target_for(heading)
        if target is None:
            continue
        chunks = grouped.setdefault(target, [])
        first_heading.setdefault(target, heading)
        rendered, leftovers = render_section(heading, body, f"fa-{target[4:]}-{len(chunks) + 1}")
        chunks.append(rendered)
        if leftovers:
            warnings.append(f"{heading[:40]}: unrendered markup {sorted(set(leftovers))[:4]}")

    for target, chunks in grouped.items():
        start = page.find(f'<section id="{target}"')
        if start < 0:
            raise SystemExit(f"build_html: HTML has no <section id=\"{target}\">")
        inner = "\n<hr>\n".join(chunks).rstrip()
        title, contents = fa_label(target, first_heading[target])
        words = word_count(inner)
        content = (f'<details class="full-analysis hw-panel" id="full-{target}" data-source-sha="{digest}">\n'
                   f'<summary><span class="fa-sum-text"><span class="fa-sum-title">{title}</span>'
                   f'<span class="fa-sum-desc">{contents} · {words}</span></span>'
                   f'<span class="fa-sum-action" aria-hidden="true"><span class="fa-when-closed">Άνοιγμα</span>'
                   f'<span class="fa-when-open">Κλείσιμο</span></span></summary>\n'
                   f'<div class="fa-body">\n{inner}\n</div>\n</details>')
        # <pre> content must not be re-indented, so the block is emitted flush left
        page = insert_before(page, "</section>", block(target, content), start)
        # under the section title: say that the full text exists, and lead to it
        pointer = (f'<p class="fa-pointer">Παρακάτω η σύνοψη. '
                   f'<a href="#full-{target}" onclick="return faOpen(\'full-{target}\')">'
                   f'Πλήρης ανάλυση στο τέλος της ενότητας ({words}) ↓</a></p>')
        page = insert_after_line(page, "</h2>", block(f"{target}-pointer", pointer), start)

    page = insert_before(page, "</head>", block("head", HEAD_BLOCK))
    main_open = page.find('<main id="masterContentContainer"')
    after_main = page.find("\n", main_open) + 1
    page = page[:after_main] + block("toolbar", TOOLBAR_BLOCK) + page[after_main:]
    page = insert_before(page, "</body>", block("runtime", TAIL_BLOCK))

    if crlf:
        page = page.replace("\n", "\r\n")
    return raw, page, grouped, warnings


def main():
    raw, page, grouped, warnings = build()
    for w in warnings:
        print("warning:", w)
    if "--check" in sys.argv:
        if raw != page:
            print("HTML is out of date: run  python tools/build_html.py")
            sys.exit(1)
        print("HTML is up to date with the Markdown.")
        return
    HTML_PATH.write_bytes(page.encode("utf8"))
    sizes = ", ".join(f"{k}:{sum(len(c) for c in v) // 1000}k" for k, v in grouped.items())
    print(f"built {HTML_PATH.name}  ({len(grouped)} sections; {sizes})")


if __name__ == "__main__":
    main()
