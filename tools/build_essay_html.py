#!/usr/bin/env python3
"""Render the essay's Markdown source into its web page (docs/essay.html).

The Markdown file is the single source of truth for the essay. Unlike the
Tractatus page, this page has no hand-written parts: the whole file is
generated, so it must never be edited by hand.

Each `##` section of the Markdown goes to one tab of the page; `tab_for()`
says which. The build stops on a `##` heading it does not know, so a new kind
of section has to be mapped here first.

Usage:
    python tools/build_essay_html.py            # rebuild docs/essay.html
    python tools/build_essay_html.py --check    # exit 1 if it is out of date

Requires: markdown-it-py  (pip install markdown-it-py)
"""
import html
import re
import sys
from pathlib import Path

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent.parent
MD_PATH = ROOT / "Logiki_Glossa_Michanes.md"
HTML_PATH = ROOT / "docs" / "essay.html"
DOCX_NAME = "Logiki_Glossa_Michanes.docx"  # built into docs/ by build_docx.py
REPO_URL = "https://github.com/avdiam/wittgenstein"

TABS = [
    # (id, label, tooltip)
    ("text", "Κείμενο", "Το δοκίμιο, σε δώδεκα ενότητες"),
    ("timeline", "Χρονολόγιο", "Τα κύρια σημεία της ιστορίας, με τη σειρά"),
    ("glossary", "Γλωσσάρι", "Οι όροι που εξηγεί το κείμενο"),
    ("sources", "Πηγές", "Πηγές και περαιτέρω ανάγνωση"),
]


# --------------------------------------------------------------------------
# 1. Markdown sections -> tabs
# --------------------------------------------------------------------------
def tab_for(heading):
    """Which tab a `##` heading of the Markdown belongs to."""
    if re.match(r"\d+\.\s", heading):
        return "text"
    if heading.startswith("Χρονολόγιο"):
        return "timeline"
    if heading.startswith("Γλωσσάρι"):
        return "glossary"
    if heading.startswith("Πηγές"):
        return "sources"
    raise SystemExit(f"build_essay_html: no tab for the heading '## {heading}'; add it to tab_for()")


# --------------------------------------------------------------------------
# 2. Parse and split
# --------------------------------------------------------------------------
def make_md():
    md = MarkdownIt("commonmark", {"html": False, "typographer": False}).enable("table")
    return md


def split_sections(tokens):
    """Return (title, subtitle, intro tokens, [(heading, tokens), ...])."""
    title, subtitle, intro, sections = "", "", [], []
    current = None
    i = 0
    while i < len(tokens):
        t = tokens[i]
        if t.type == "heading_open" and t.tag == "h1":
            title = tokens[i + 1].content
            i += 3
            # an all-italic paragraph right after the title is the subtitle
            if i + 2 < len(tokens) and tokens[i].type == "paragraph_open":
                c = tokens[i + 1].content.strip()
                if c.startswith("*") and c.endswith("*") and not c.startswith("**"):
                    subtitle = c[1:-1]
                    i += 3
            continue
        if t.type == "heading_open" and t.tag == "h2":
            current = (tokens[i + 1].content, [])
            sections.append(current)
            i += 3
            continue
        (current[1] if current else intro).append(t)
        i += 1
    return title, subtitle, intro, sections


# --------------------------------------------------------------------------
# 3. Render
# --------------------------------------------------------------------------
def section_number(heading):
    m = re.match(r"(\d+)\.\s", heading)
    return int(m.group(1)) if m else None


def prepare(tokens, sec_id, glossary=False):
    """Give ids to ### headings, classes to notes, tables and the glossary list.
    Returns the list of (id, heading text) for the ### headings."""
    subs = []
    k = 0
    for i, t in enumerate(tokens):
        if t.type == "heading_open" and t.tag in ("h3", "h4"):
            if t.tag == "h3":
                k += 1
                sid = f"{sec_id}-{k}"
                t.attrSet("id", sid)
                subs.append((sid, tokens[i + 1].content))
        elif t.type == "blockquote_open":
            # first inline token inside the quote
            for j in range(i + 1, min(i + 4, len(tokens))):
                if tokens[j].type == "inline":
                    if tokens[j].content.startswith("**Ερμηνευτική σημείωση"):
                        t.attrSet("class", "note")
                    break
        elif t.type == "table_open":
            t.attrSet("class", "timeline" if sec_id == "part-timeline" else "data")
        elif t.type == "inline" and glossary and t.children:
            # "**Term.** definition": drop the full stop after the term when displayed
            # (markdown-it may put an empty text token before the bold term)
            kids = [c for c in t.children if not (c.type == "text" and c.content == "")]
            if kids and kids[0].type == "strong_open":
                depth = 0
                end = -1
                for idx, c in enumerate(kids):
                    if c.type == "strong_open":
                        depth += 1
                    elif c.type == "strong_close":
                        depth -= 1
                        if depth == 0:
                            end = idx
                            break
                if end > 1:
                    for c in reversed(kids[1:end]):
                        if c.type == "text" and c.content:
                            if c.content.endswith("."):
                                c.content = c.content[:-1]
                            break
        elif t.type == "bullet_list_open" and glossary and t.level == 0:
            t.attrSet("class", "glossary")
            t.attrSet("id", "glossaryList")
    return subs


XREF = re.compile(r"(ενότητ(?:α|ας|ες|ων|ών) )(\d{1,2}(?:(?:, | και )\d{1,2})*)")


def link_sections(fragment, valid):
    """Turn «ενότητα 8» / «ενότητες 5, 7 και 8» into links to the sections."""
    def numbers(m):
        def one(n):
            k = int(n.group(0))
            return f'<a class="xref" href="#sec-{k}">{k}</a>' if k in valid else n.group(0)
        return m.group(1) + re.sub(r"\d{1,2}", one, m.group(2))

    # only in text nodes: split on tags
    parts = re.split(r"(<[^>]+>)", fragment)
    inside_a = 0
    for idx, p in enumerate(parts):
        if p.startswith("<"):
            if p.startswith("<a "):
                inside_a += 1
            elif p == "</a>":
                inside_a -= 1
            continue
        if not inside_a:
            parts[idx] = XREF.sub(numbers, p)
    return "".join(parts)


FIG_RE = re.compile(r'<p><img src="([^"]+)" alt="([^"]*)"(?: title="([^"]*)")?\s*/?></p>')


def render_figure(m):
    src, alt, title = m.group(1), m.group(2), m.group(3) or m.group(2)
    caption = f"<figcaption>{title}</figcaption>" if title else ""
    if src.endswith(".svg"):
        svg_path = HTML_PATH.parent / src
        if not svg_path.exists():
            raise SystemExit(f"build_essay_html: missing SVG file '{svg_path}'")
        svg_body = svg_path.read_text(encoding="utf-8").strip()
        return (f'<figure class="essay-figure essay-diagram"><div class="figure-svg" role="button" tabindex="0" '
                f'aria-label="Μεγέθυνση διαγράμματος: {alt}" title="Μεγέθυνση">{svg_body}</div>{caption}</figure>')
    img_path = HTML_PATH.parent / src
    if not img_path.exists():
        raise SystemExit(f"build_essay_html: missing image file '{img_path}'")
    return f'<figure class="essay-figure essay-photo"><img src="{src}" alt="{alt}" loading="lazy">{caption}</figure>'


def polish(fragment):
    """Small presentational touches on rendered HTML."""
    fragment = FIG_RE.sub(render_figure, fragment)
    fragment = fragment.replace("<table", '<div class="table-wrap"><table').replace("</table>", "</table></div>")
    # truth-table cells: true / false
    fragment = fragment.replace('<td style="text-align:center">Α</td>', '<td style="text-align:center" class="t">Α</td>')
    fragment = fragment.replace('<td style="text-align:center">Ψ</td>', '<td style="text-align:center" class="f">Ψ</td>')
    return fragment


def render_page():
    md = make_md()
    source = MD_PATH.read_text(encoding="utf-8")
    tokens = md.parse(source)
    title, subtitle, intro, sections = split_sections(tokens)
    if not title:
        raise SystemExit("build_essay_html: the Markdown has no '# ' title")

    valid = {section_number(h) for h, _ in sections if section_number(h)}
    panels = {tab: [] for tab, _, _ in TABS}
    toc = []  # (id, number or None, text, [(sub id, text)])

    if intro:
        body = md.renderer.render(intro, md.options, {})
        panels["text"].append(f'<div class="lede" id="intro">{polish(link_sections(body, valid))}</div>')

    for heading, toks in sections:
        tab = tab_for(heading)
        n = section_number(heading)
        sec_id = f"sec-{n}" if n else f"part-{tab}"  # not the tab name: avoids the browser's own jump
        subs = prepare(toks, sec_id, glossary=(tab == "glossary"))
        body = md.renderer.render(toks, md.options, {})
        body = polish(link_sections(body, valid))
        head = md.renderInline(heading)
        if tab == "text":
            head_text = md.renderInline(re.sub(r"^\d+\.\s*", "", heading))
            toc.append((sec_id, n, head_text, [(sid, md.renderInline(s)) for sid, s in subs]))
            panels[tab].append(
                f'<section class="essay-section" id="{sec_id}">\n'
                f'<h2><span class="sec-num">{n}</span>{head_text}</h2>\n{body}</section>'
            )
        else:
            extra = ""
            if tab == "glossary":
                extra = (
                    '<div class="filter"><label for="glossaryFilter">Αναζήτηση όρου</label>'
                    '<input id="glossaryFilter" type="search" autocomplete="off" '
                    'placeholder="π.χ. ταυτολογία" oninput="filterGlossary(this.value)">'
                    '<span id="glossaryCount" aria-live="polite"></span></div>\n'
                )
            panels[tab].append(f'<section class="essay-section" id="{sec_id}">\n<h2>{head}</h2>\n{extra}{body}</section>')

    for tab, label, _ in TABS:
        if not panels[tab]:
            raise SystemExit(f"build_essay_html: the tab '{label}' would be empty")

    return assemble(md.renderInline(title), md.renderInline(subtitle), title, toc, panels)


def toc_html(toc):
    items = []
    for sec_id, n, text, subs in toc:
        sub_html = ""
        if subs:
            sub_html = '<ol class="toc-sub">' + "".join(
                f'<li><a href="#{sid}" data-target="{sid}">{s}</a></li>' for sid, s in subs
            ) + "</ol>"
        items.append(
            f'<li><a href="#{sec_id}" data-target="{sec_id}" class="toc-sec">'
            f'<span class="toc-num">{n}</span><span class="toc-text">{text}</span></a>{sub_html}</li>'
        )
    return '<ol class="toc">' + "".join(items) + "</ol>"


def assemble(title_html, subtitle_html, title_plain, toc, panels):
    tab_buttons = "".join(
        f'<button type="button" role="tab" id="tab-btn-{tid}" aria-controls="panel-{tid}" '
        f'aria-selected="{"true" if k == 0 else "false"}" class="tab{" active" if k == 0 else ""}" '
        f'title="{html.escape(tip)}" onclick="showTab(\'{tid}\', true)">{label}</button>'
        for k, (tid, label, tip) in enumerate(TABS)
    )
    panel_html = []
    for k, (tid, label, _) in enumerate(TABS):
        hidden = "" if k == 0 else " hidden"
        inner = "\n".join(panels[tid])
        if tid == "text":
            inner = (
                '<div class="text-layout">\n'
                '<aside id="toc" class="toc-pane" aria-label="Περιεχόμενα">\n'
                '<div class="toc-head"><span class="toc-label">Περιεχόμενα</span>'
                '<button type="button" id="tocFold" class="icon-btn" onclick="toggleToc()" '
                'aria-expanded="true" aria-controls="tocBody" title="Δίπλωμα των περιεχομένων (πλήκτρο [)">'
                '<svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><path d="M10 3 5 8l5 5" '
                'fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
                '</button></div>\n'
                f'<nav id="tocBody">{toc_html(toc)}</nav>\n</aside>\n'
                f'<article class="reading">\n{inner}\n</article>\n</div>'
            )
        else:
            inner = f'<article class="reading reading-wide">\n{inner}\n</article>'
        panel_html.append(
            f'<div role="tabpanel" id="panel-{tid}" aria-labelledby="tab-btn-{tid}" class="panel"{hidden}>\n{inner}\n</div>'
        )

    return TEMPLATE.format(
        title_plain=html.escape(title_plain),
        title_html=title_html,
        subtitle_html=subtitle_html,
        description=html.escape(re.sub(r"<[^>]+>", "", subtitle_html)),
        tab_buttons=tab_buttons,
        panels="\n".join(panel_html),
        docx=DOCX_NAME,
        repo=REPO_URL,
        css=CSS,
        js=JS,
    )


# --------------------------------------------------------------------------
# 4. Page template, styles and behaviour
# --------------------------------------------------------------------------
TEMPLATE = """<!DOCTYPE html>
<!-- GENERATED by tools/build_essay_html.py from Logiki_Glossa_Michanes.md. Do not edit by hand. -->
<html lang="el">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_plain}</title>
<meta name="description" content="{description}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Commissioner:wght@400..700&family=JetBrains+Mono:wght@400;600&family=Literata:ital,opsz,wght@0,7..72,400..700;1,7..72,400..700&display=swap" rel="stylesheet">
<script>
  // Apply the saved theme before first paint (shared with the Tractatus page).
  (function () {{
    var mode = null;
    try {{ mode = localStorage.getItem('hw-tlp-theme'); }} catch (e) {{}}
    if (mode !== 'dark' && mode !== 'light') {{
      mode = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }}
    if (mode === 'dark') document.documentElement.classList.add('dark');
  }})();
</script>
<style>
{css}
</style>
</head>
<body>
<a class="skip" href="#panel-text">Μετάβαση στο κείμενο</a>
<header class="site-header">
  <div class="hdr">
    <button type="button" class="icon-btn only-narrow" onclick="openDrawer()" aria-label="Άνοιγμα περιεχομένων">
      <svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><path d="M2 4h12M2 8h12M2 12h12" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
    </button>
    <a class="brand" href="index.html" title="Αρχική σελίδα">
      <span class="brand-main">{title_html}</span>
      <span class="brand-sub">Δοκίμιο</span>
    </a>
    <div class="tabs" role="tablist" aria-label="Μέρη της σελίδας">{tab_buttons}</div>
    <div class="hdr-actions">
      <a class="hdr-link" href="tractatus.html" title="Η ανάλυση του Tractatus">Tractatus</a>
      <a class="hdr-link" href="{docx}" download title="Το δοκίμιο ως αρχείο Word">.docx</a>
      <button type="button" id="themeBtn" class="hdr-link" onclick="toggleTheme()">Σκοτεινό θέμα</button>
    </div>
  </div>
</header>
<div id="drawerBackdrop" class="backdrop" hidden onclick="closeDrawer()"></div>
<dialog id="figZoom" class="fig-zoom" aria-label="Μεγεθυμένο διάγραμμα">
  <div class="fig-zoom-bar"><span class="fig-zoom-hint">Σύρετε για να δείτε όλο το σχήμα</span><button type="button" class="hdr-link" id="figZoomClose">Κλείσιμο</button></div>
  <div class="fig-zoom-body"></div>
</dialog>
<div class="page-head">
  <h1>{title_html}</h1>
  <p class="subtitle">{subtitle_html}</p>
</div>
<main id="main">
{panels}
</main>
<footer class="site-footer">
  <p>Το κείμενο διατίθεται με την άδεια <a href="https://creativecommons.org/licenses/by/4.0/deed.el">CC BY 4.0</a>.
  Η σελίδα παράγεται αυτόματα από το αρχείο <a href="{repo}/blob/main/Logiki_Glossa_Michanes.md">Logiki_Glossa_Michanes.md</a>·
  οι πηγές κάθε ισχυρισμού καταγράφονται στο <a href="{repo}/blob/main/CROSSCHECK_PLAN.md">CROSSCHECK_PLAN.md</a>.</p>
  <p><a href="index.html">Αρχική</a> · <a href="tractatus.html">Tractatus Logico-Philosophicus</a> · <a href="{repo}">Αποθετήριο στο GitHub</a></p>
</footer>
<script>
{js}
</script>
</body>
</html>
"""

CSS = r"""
/* Design tokens: the same as the Tractatus page (see the top of its first
   <style> block). Green marks "what is the case" and the active item; ochre
   marks commentary, here the interpretive notes. */
:root {
  --background: #eff1ee; --content: #fbfbf9; --sidebar: #e8ebe7;
  --border: #cdd3cd; --border-soft: #e0e4df;
  --foreground: #1c2022; --muted-foreground: #57605d;
  --primary: #1e5c4e; --primary-foreground: #ffffff; --primary-soft: rgba(30, 92, 78, 0.10);
  --secondary: #eceeea;
  --mark: #91590a; --mark-soft: rgba(184, 128, 30, 0.12);
  --truth-fg: #1e5c4e; --truth-bg: rgba(30, 92, 78, 0.12);
  --false-fg: #57605d; --false-bg: rgba(87, 96, 93, 0.07);
  --header-h: 56px; --toc-w: 18.5rem; --rail-w: 3.5rem; --radius: 4px;
  --font-sans: 'Commissioner', 'Segoe UI', system-ui, -apple-system, Roboto, sans-serif;
  --font-serif: 'Literata', 'Palatino Linotype', Georgia, 'Times New Roman', serif;
  --font-mono: 'JetBrains Mono', Consolas, ui-monospace, SFMono-Regular, Menlo, monospace;
}
/* Dark tokens apply on screen only: print always uses the light tokens. */
@media screen {
html.dark {
  --background: #131618; --content: #1a1e20; --sidebar: #101315;
  --border: #333a3d; --border-soft: #262c2f;
  --foreground: #e3e6e2; --muted-foreground: #9aa4a2;
  --primary: #86cdb5; --primary-foreground: #0f1d19; --primary-soft: rgba(134, 205, 181, 0.13);
  --secondary: #23282b;
  --mark: #e2b45e; --mark-soft: rgba(226, 180, 94, 0.10);
  --truth-fg: #86cdb5; --truth-bg: rgba(134, 205, 181, 0.14);
  --false-fg: #9aa4a2; --false-bg: rgba(154, 164, 162, 0.10);
}
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { margin: 0; background: var(--background); color: var(--foreground); font-family: var(--font-sans); font-kerning: normal; }
a { color: var(--primary); }
:focus-visible { outline: 2px solid var(--primary); outline-offset: 2px; }
[hidden] { display: none !important; }
.skip { position: absolute; left: -999px; top: 0; background: var(--content); padding: .5rem 1rem; z-index: 100; }
.skip:focus { left: 1rem; }

/* Header */
.site-header { position: sticky; top: 0; z-index: 40; background: var(--content); border-bottom: 1px solid var(--border); }
.hdr { height: var(--header-h); display: flex; align-items: center; gap: 1rem; padding: 0 1rem; max-width: 1600px; margin: 0 auto; }
.brand { display: flex; flex-direction: column; line-height: 1.15; text-decoration: none; color: var(--foreground); min-width: 0; }
.brand-main { font-weight: 650; font-size: .98rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.brand-sub { font-size: .75rem; color: var(--muted-foreground); }
.tabs { display: flex; gap: .25rem; margin-left: auto; }
.tab { font: inherit; font-size: .88rem; background: none; border: 1px solid transparent; border-radius: var(--radius); padding: .4rem .75rem; color: var(--muted-foreground); cursor: pointer; }
.tab:hover { color: var(--foreground); background: var(--secondary); }
.tab.active { color: var(--primary); border-color: var(--border); background: var(--primary-soft); font-weight: 600; }
.hdr-actions { display: flex; gap: .25rem; }
.hdr-link { font: inherit; font-size: .82rem; color: var(--muted-foreground); text-decoration: none; background: none; border: 1px solid var(--border-soft); border-radius: var(--radius); padding: .35rem .6rem; cursor: pointer; white-space: nowrap; }
.hdr-link:hover { color: var(--foreground); border-color: var(--border); }
.icon-btn { display: inline-flex; align-items: center; justify-content: center; width: 2rem; height: 2rem; background: none; border: 1px solid var(--border-soft); border-radius: var(--radius); color: var(--muted-foreground); cursor: pointer; }
.icon-btn:hover { color: var(--foreground); border-color: var(--border); }
.only-narrow { display: none; }

/* Title block */
.page-head { max-width: 1600px; margin: 0 auto; padding: 2rem 1rem 0; }
.page-head h1 { font-family: var(--font-serif); font-weight: 600; font-size: clamp(1.7rem, 3vw, 2.4rem); margin: 0; }
.page-head .subtitle { font-family: var(--font-serif); font-style: italic; color: var(--muted-foreground); margin: .4rem 0 0; font-size: 1.1rem; }

/* Layout */
main { max-width: 1600px; margin: 0 auto; padding: 1.5rem 1rem 3rem; }
.text-layout { display: grid; grid-template-columns: var(--toc-w) minmax(0, 1fr); gap: 2.5rem; align-items: start; }
body.toc-folded .text-layout { grid-template-columns: var(--rail-w) minmax(0, 1fr); }
.reading { max-width: 44rem; font-family: var(--font-serif); font-size: 1.06rem; line-height: 1.72; }
.reading-wide { max-width: 60rem; margin: 0 auto; }

/* Contents pane */
.toc-pane { position: sticky; top: calc(var(--header-h) + 1rem); max-height: calc(100vh - var(--header-h) - 2rem); overflow-y: auto; background: var(--sidebar); border: 1px solid var(--border-soft); border-radius: 6px; padding: .75rem; font-size: .86rem; }
.toc-head { display: flex; align-items: center; justify-content: space-between; margin-bottom: .5rem; }
.toc-label { font-weight: 600; color: var(--muted-foreground); font-size: .78rem; }
.toc, .toc-sub { list-style: none; margin: 0; padding: 0; }
.toc > li { margin: .1rem 0; }
.toc a { display: flex; gap: .5rem; text-decoration: none; color: var(--foreground); padding: .28rem .4rem; border-radius: var(--radius); line-height: 1.3; }
.toc a:hover { background: var(--secondary); }
.toc a.current { background: var(--primary-soft); color: var(--primary); font-weight: 600; }
.toc-num { min-width: 1.4rem; text-align: right; font-variant-numeric: tabular-nums; color: var(--muted-foreground); }
.toc a.current .toc-num { color: var(--primary); }
.toc-sub { margin: 0 0 .3rem 1.9rem; }
.toc-sub a { font-size: .8rem; color: var(--muted-foreground); padding: .18rem .4rem; }
body.toc-folded .toc-label, body.toc-folded .toc-text, body.toc-folded .toc-sub { display: none; }
body.toc-folded .toc-pane { padding: .5rem .25rem; }
body.toc-folded .toc-head { justify-content: center; }
body.toc-folded #tocFold svg { transform: rotate(180deg); }
body.toc-folded .toc-num { min-width: 0; margin: 0 auto; }

/* Text */
.essay-section { scroll-margin-top: calc(var(--header-h) + 1rem); margin-bottom: 3rem; }
.essay-section h2 { font-family: var(--font-sans); font-size: 1.45rem; font-weight: 650; line-height: 1.25; margin: 0 0 1rem; padding-top: .5rem; border-top: 1px solid var(--border); }
.sec-num { color: var(--primary); margin-right: .6rem; font-variant-numeric: tabular-nums; }
.reading h3 { font-family: var(--font-sans); font-size: 1.1rem; font-weight: 650; margin: 2rem 0 .6rem; scroll-margin-top: calc(var(--header-h) + 1rem); }
.reading h4 { font-family: var(--font-sans); font-size: 1rem; margin: 1.5rem 0 .5rem; }
.reading p { margin: 0 0 1rem; }
.reading ul, .reading ol { padding-left: 1.4rem; margin: 0 0 1rem; }
.reading li { margin: .3rem 0; }
#panel-text .reading p, #panel-text .reading li, ul.glossary li { text-align: justify; -webkit-hyphens: auto; hyphens: auto; }
.reading code { font-family: var(--font-mono); font-size: .88em; background: var(--secondary); padding: .05em .3em; border-radius: 3px; }
.lede { font-size: 1.1rem; color: var(--foreground); margin-bottom: 2.5rem; }
.xref { text-decoration: none; border-bottom: 1px dotted var(--primary); }
blockquote { margin: 1.25rem 0; padding: .75rem 1rem; border-left: 3px solid var(--border); background: var(--secondary); border-radius: 0 var(--radius) var(--radius) 0; }
blockquote p:last-child { margin-bottom: 0; }
blockquote.note { border-left-color: var(--mark); background: var(--mark-soft); font-size: .98rem; }
blockquote.note strong:first-child { color: var(--mark); font-family: var(--font-sans); font-size: .9rem; }

/* Figures and schematic diagrams */
.essay-figure { margin: 1.6rem 0; padding: .9rem 1rem .75rem; background: var(--content); border: 1px solid var(--border); border-radius: 6px; break-inside: avoid; }
.essay-figure img { display: block; max-width: 100%; max-height: 360px; width: auto; height: auto; margin: 0 auto; border-radius: 3px; }
.essay-figure .figure-svg svg { display: block; width: 100%; height: auto; max-height: 330px; margin: 0 auto; }
.essay-figure .figure-svg { cursor: zoom-in; border-radius: var(--radius); }
/* Enlarged diagram: a native dialog; on phones the diagram keeps its design
   width (760) and the body scrolls sideways. */
.fig-zoom { width: min(1100px, 96vw); max-width: none; max-height: 94dvh; padding: 0; border: 1px solid var(--border); border-radius: 6px; background: var(--content); color: var(--foreground); }
.fig-zoom::backdrop { background: rgba(0, 0, 0, .55); }
.fig-zoom-bar { display: flex; align-items: center; justify-content: space-between; gap: .5rem; padding: .45rem .6rem .45rem .9rem; border-bottom: 1px solid var(--border); font-family: var(--font-sans); font-size: .8rem; color: var(--muted-foreground); }
.fig-zoom-hint { visibility: hidden; }
.fig-zoom-body { overflow: auto; max-height: calc(94dvh - 3rem); padding: 1rem; }
.fig-zoom-body svg { display: block; width: 100%; min-width: 760px; height: auto; }
.essay-figure figcaption { margin-top: .65rem; padding-top: .5rem; border-top: 1px solid var(--border-soft); font-family: var(--font-sans); font-size: .85rem; line-height: 1.45; color: var(--muted-foreground); text-align: center; }

/* Tables */
.table-wrap { overflow-x: auto; margin: 1.25rem 0; }
table { border-collapse: collapse; font-family: var(--font-sans); font-size: .9rem; line-height: 1.45; width: 100%; }
th, td { border: 1px solid var(--border); padding: .45rem .6rem; vertical-align: top; text-align: left; }
th { background: var(--secondary); font-weight: 600; }
table.data td.t { color: var(--truth-fg); background: var(--truth-bg); font-weight: 600; }
table.data td.f { color: var(--false-fg); background: var(--false-bg); }
table.timeline td:first-child { white-space: nowrap; font-variant-numeric: tabular-nums; color: var(--primary); font-weight: 600; width: 11rem; }
table.timeline tr:nth-child(even) td { background: var(--content); }

/* Glossary */
.filter { display: flex; flex-wrap: wrap; gap: .5rem 1rem; align-items: center; margin: 0 0 1.25rem; font-family: var(--font-sans); font-size: .9rem; }
.filter input { font: inherit; padding: .45rem .6rem; border: 1px solid var(--border); border-radius: var(--radius); background: var(--content); color: var(--foreground); min-width: 16rem; }
#glossaryCount { color: var(--muted-foreground); }
ul.glossary { list-style: none; padding: 0; }
ul.glossary li { padding: .7rem 0; border-bottom: 1px solid var(--border-soft); margin: 0; }
ul.glossary li strong:first-child { display: block; font-family: var(--font-sans); color: var(--primary); }

/* Footer */
.site-footer { border-top: 1px solid var(--border); color: var(--muted-foreground); font-size: .82rem; padding: 1.5rem 1rem 2.5rem; max-width: 1600px; margin: 0 auto; }
.site-footer p { margin: .3rem 0; }

/* Narrow screens: the contents pane becomes a drawer */
.backdrop { position: fixed; inset: 0; background: rgba(0, 0, 0, .35); z-index: 45; }
@media (max-width: 1023px) {
  .only-narrow { display: inline-flex; }
  .text-layout, body.toc-folded .text-layout { grid-template-columns: minmax(0, 1fr); }
  .toc-pane { position: fixed; top: 0; left: 0; bottom: 0; width: min(20rem, 85vw); max-height: none; z-index: 50; border-radius: 0; transform: translateX(-105%); transition: transform .2s ease; }
  body.drawer-open .toc-pane { transform: none; }
  body.toc-folded .toc-label, body.toc-folded .toc-text, body.toc-folded .toc-sub { display: revert; }
  #tocFold { display: none; }
  .reading { max-width: none; }
}
@media (max-width: 720px) {
  .hdr { gap: .5rem; padding: 0 .6rem; }
  .brand-sub, .hdr-actions .hdr-link:not(#themeBtn) { display: none; }
  .tab { padding: .35rem .45rem; font-size: .8rem; }
  .page-head { padding-top: 1.25rem; }
  .reading { font-size: 1rem; }
  #panel-text .reading p, #panel-text .reading li, ul.glossary li { text-align: left; -webkit-hyphens: manual; hyphens: manual; }
  table.timeline td:first-child { width: auto; white-space: normal; }
}
@media (max-width: 520px) {
  .hdr { flex-wrap: wrap; height: auto; padding: .4rem .6rem; }
  .tabs { order: 3; width: 100%; margin: 0; overflow-x: auto; }
  :root { --header-h: 92px; }
}

/* Phones: say that a diagram can be enlarged. Screen only: an A4 page is
   about 718 CSS px wide and would match the width query too. */
@media screen and (max-width: 720px) {
  .essay-diagram .figure-svg::after { content: 'Πατήστε για μεγέθυνση'; display: block; margin-top: .4rem; text-align: center; font-family: var(--font-sans); font-size: .78rem; color: var(--primary); }
  .fig-zoom-hint { visibility: visible; }
}

/* Print: the whole essay, no interface */
@media print {
  .site-header, .toc-pane, .filter, .site-footer, .skip { display: none !important; }
  .panel[hidden] { display: block !important; }
  .text-layout { display: block; }
  body { background: #fff; color: #000; }
  .reading { max-width: none; font-size: 11pt; }
}
"""

JS = r"""
var TABS = ['text', 'timeline', 'glossary', 'sources'];

function showTab(id, updateHash) {
  TABS.forEach(function (t) {
    var on = t === id;
    document.getElementById('panel-' + t).hidden = !on;
    var b = document.getElementById('tab-btn-' + t);
    b.classList.toggle('active', on);
    b.setAttribute('aria-selected', on ? 'true' : 'false');
  });
  if (updateHash) {
    history.replaceState(null, '', id === 'text' ? location.pathname : '#' + id);
    window.scrollTo(0, 0);
  }
}

function goTo(targetId, instant) {
  var el = document.getElementById(targetId);
  if (!el) return false;
  var panel = el.closest('.panel');
  if (panel) showTab(panel.id.replace('panel-', ''), false);
  closeDrawer();
  el.scrollIntoView({ behavior: instant ? 'instant' : 'smooth', block: 'start' });
  history.replaceState(null, '', '#' + targetId);
  return true;
}

document.addEventListener('click', function (e) {
  var a = e.target.closest('a[href^="#"]');
  if (!a) return;
  var id = a.getAttribute('href').slice(1);
  if (TABS.indexOf(id) >= 0) { e.preventDefault(); showTab(id, true); return; }
  if (id && goTo(id)) e.preventDefault();
});

function openFromHash() {
  var id = decodeURIComponent(location.hash.slice(1));
  if (!id) return;
  if (TABS.indexOf(id) >= 0) { showTab(id, false); window.scrollTo(0, 0); } else goTo(id, true);
}
/* The web fonts change line lengths when they arrive, which moves the target:
   jump again once they are ready. */
function openFromHashWhenSettled() {
  openFromHash();
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(openFromHash);
  window.addEventListener('load', openFromHash, { once: true });
}

/* Theme: shared key with the Tractatus page */
function setThemeLabel() {
  var dark = document.documentElement.classList.contains('dark');
  document.getElementById('themeBtn').textContent = dark ? 'Φωτεινό θέμα' : 'Σκοτεινό θέμα';
}
function toggleTheme() {
  var dark = document.documentElement.classList.toggle('dark');
  try { localStorage.setItem('hw-tlp-theme', dark ? 'dark' : 'light'); } catch (e) {}
  setThemeLabel();
}

/* Contents pane: fold to a rail of numbers ([ key); drawer on narrow screens */
function setToc(folded, persist) {
  document.body.classList.toggle('toc-folded', folded);
  document.getElementById('tocFold').setAttribute('aria-expanded', folded ? 'false' : 'true');
  if (persist) { try { localStorage.setItem('hw-essay-toc', folded ? 'folded' : 'open'); } catch (e) {} }
}
function toggleToc() { setToc(!document.body.classList.contains('toc-folded'), true); }
function openDrawer() { showTab('text', false); document.body.classList.add('drawer-open'); document.getElementById('drawerBackdrop').hidden = false; }
function closeDrawer() { document.body.classList.remove('drawer-open'); document.getElementById('drawerBackdrop').hidden = true; }
document.addEventListener('keydown', function (e) {
  var tag = (e.target.tagName || '').toLowerCase();
  if (tag === 'input' || tag === 'textarea') return;
  if (e.key === '[') toggleToc();
  if (e.key === 'Escape') closeDrawer();
});

/* Diagrams: tap (or Enter / Space) to enlarge in a dialog */
function openFigZoom(box) {
  var dlg = document.getElementById('figZoom');
  if (!dlg || typeof dlg.showModal !== 'function') return;
  var body = dlg.querySelector('.fig-zoom-body');
  body.innerHTML = '';
  body.appendChild(box.querySelector('svg').cloneNode(true));
  dlg.showModal();
  body.scrollLeft = 0;
}
function initFigZoom() {
  var dlg = document.getElementById('figZoom');
  if (!dlg) return;
  document.querySelectorAll('.essay-diagram .figure-svg').forEach(function (box) {
    box.addEventListener('click', function () { openFigZoom(box); });
    box.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openFigZoom(box); }
    });
  });
  document.getElementById('figZoomClose').addEventListener('click', function () { dlg.close(); });
  /* A click on the backdrop lands on the dialog element itself. */
  dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });
  /* The copy carries the diagram's marker ids: remove it on close. */
  dlg.addEventListener('close', function () { dlg.querySelector('.fig-zoom-body').innerHTML = ''; });
}

/* Highlight the section being read */
function watchSections() {
  if (!('IntersectionObserver' in window)) return;
  var links = {};
  document.querySelectorAll('.toc a.toc-sec').forEach(function (a) { links[a.dataset.target] = a; });
  var obs = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (!en.isIntersecting) return;
      Object.keys(links).forEach(function (k) { links[k].classList.toggle('current', k === en.target.id); });
    });
  }, { rootMargin: '-20% 0px -70% 0px' });
  document.querySelectorAll('#panel-text .essay-section').forEach(function (s) { obs.observe(s); });
}

/* Glossary filter (accents and case ignored) */
function fold(s) { return s.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase(); }
function filterGlossary(q) {
  var f = fold(q.trim()), shown = 0, items = document.querySelectorAll('#glossaryList > li');
  items.forEach(function (li) { var hit = !f || fold(li.textContent).indexOf(f) >= 0; li.hidden = !hit; if (hit) shown++; });
  document.getElementById('glossaryCount').textContent = f ? shown + ' από ' + items.length : '';
}

(function init() {
  setThemeLabel();
  var saved = null;
  try { saved = localStorage.getItem('hw-essay-toc'); } catch (e) {}
  setToc(saved === 'folded', false);
  watchSections();
  initFigZoom();
  openFromHashWhenSettled();
  window.addEventListener('hashchange', openFromHash);
})();
"""


# --------------------------------------------------------------------------
# 5. Main
# --------------------------------------------------------------------------
def main():
    page = render_page()
    if "--check" in sys.argv:
        if not HTML_PATH.exists() or HTML_PATH.read_text(encoding="utf-8") != page:
            print(f"OUT OF DATE: {HTML_PATH.relative_to(ROOT)} does not match {MD_PATH.name}")
            sys.exit(1)
        print(f"up to date: {HTML_PATH.relative_to(ROOT)}")
        return
    HTML_PATH.parent.mkdir(exist_ok=True)
    HTML_PATH.write_bytes(page.encode("utf-8"))
    print(f"wrote {HTML_PATH.relative_to(ROOT)} ({len(page):,} characters)")


if __name__ == "__main__":
    main()
