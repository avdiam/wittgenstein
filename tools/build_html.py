#!/usr/bin/env python3
"""Build docs/tractatus.html mechanically from Markdown and tools/tractatus/.

The Markdown analysis is the single source of truth for the reading text and
automatically populates the Tree View (Δενδροειδής μορφή) and Quick-Peek data
(enriched with the existing 65 Pears & McGuinness comparison quotes in
tools/tractatus/pm_quotes.json).

Never edit docs/tractatus.html by hand.

Usage:
    python tools/build_html.py            # rebuild docs/tractatus.html (LF)
    python tools/build_html.py --check    # exit 1 if docs/tractatus.html is out of date

Requires: markdown-it-py  (pip install markdown-it-py)
"""
import html
import json
import re
import sys
from pathlib import Path

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent.parent
DOC_DIR = ROOT / "Tractatus Logico-Philosophicus"
MD_PATH = DOC_DIR / "TRACTATUS_LOGICO_PHILOSOPHICUS_ANALYSIS_1-7.md"
ASSETS_DIR = Path(__file__).resolve().parent / "tractatus"
HTML_PATH = ROOT / "docs" / "tractatus.html"
REPO_URL = "https://github.com/avdiam/wittgenstein"
KATEX = "https://cdn.jsdelivr.net/npm/katex@0.16.9/dist"

LONG_PROP_THRESHOLD = 260  # Greek chars above which German + English tuck into <details>

EXPECTED_MAIN_BRANCHES = [
    "1.1", "1.2",
    "2.1", "2.2",
    "3.1", "3.2", "3.3", "3.4", "3.5",
    "4.1", "4.2", "4.3", "4.4", "4.5",
    "5.1", "5.2", "5.3", "5.4", "5.5", "5.6",
    "6.1", "6.2", "6.3", "6.4", "6.5",
]

SECTION_META = {
    "sec-intro":    ("Α", "Προκαταρκτικά", "Εισαγωγή, πρόλογος και η εισαγωγή του Russell", "Εισαγωγή, πρόλογος, Russell"),
    "sec-decimal":  ("Β", "Δομική αρχιτεκτονική", "Το δεκαδικό σύστημα και ο χάρτης των 526 προτάσεων", "Το δεκαδικό σύστημα"),
    "sec-prop1":    ("1", "Πρόταση 1 · 1 – 1.21", "Πρόταση 1: Η μακρο-οντολογία του κόσμου", "Ο κόσμος και τα γεγονότα"),
    "sec-prop2":    ("2", "Πρόταση 2 · 2 – 2.225", "Πρόταση 2: Καταστάσεις πραγμάτων και Εικονιστική Θεωρία", "Καταστάσεις πραγμάτων και εικόνα"),
    "sec-prop3":    ("3", "Πρόταση 3 · 3 – 3.5", "Πρόταση 3: Η λογική εικόνα, η σκέψη και το προτασιακό σημείο", "Η λογική εικόνα και η σκέψη"),
    "sec-prop4":    ("4", "Πρόταση 4 · 4 – 4.53", "Πρόταση 4: Η πρόταση με νόημα, «Λέγειν / Δεικνύναι» και πίνακες αληθείας", "Η πρόταση με νόημα"),
    "sec-prop5":    ("5", "Πρόταση 5 · 5 – 5.641", "Πρόταση 5: Συναρτήσεις αληθείας, τελεστής N(ξ̄) και υποκείμενο", "Συναρτήσεις αληθείας και εγώ"),
    "sec-prop6":    ("6", "Πρόταση 6 · 6 – 6.54", "Πρόταση 6: Γενική μορφή, λογική, μαθηματικά, επιστήμη, ηθική και σκάλα", "[p̄, ξ̄, N(ξ̄)], επιστήμη, ηθική"),
    "sec-prop7":    ("7", "Πρόταση 7", "Πρόταση 7: Η σιωπή", "Η σιωπή"),
    "sec-epilogue": ("Γ", "Σύνθεση & πηγές", "Συνθετικοί πίνακες, ιστορικό επίμετρο και βιβλιογραφία", "Πίνακες, επίμετρο, βιβλιογραφία"),
}

SECTION_ORDER = [
    "sec-intro", "sec-decimal",
    "sec-prop1", "sec-prop2", "sec-prop3", "sec-prop4", "sec-prop5", "sec-prop6", "sec-prop7",
    "sec-epilogue",
]

VALID_LAB_IDS = {
    "lab-truth-tables", "lab-wpf", "lab-probability",
    "lab-paris", "lab-necker", "lab-eye", "lab-gramophone",
    "lab-mesh", "lab-kant", "lab-2x2", "lab-ladder",
}


# --------------------------------------------------------------------------
# 1. Markdown sections -> target HTML sections
# --------------------------------------------------------------------------
def target_for(heading):
    """Map every `##` Markdown heading to an HTML section id."""
    if heading.startswith("Πλήρης"):
        return None
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
    """Return list of (heading, body) for every `##` heading outside fenced code."""
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
# 2. Math protection & Markdown parser
# --------------------------------------------------------------------------
MD = MarkdownIt("commonmark", {"html": True}).enable("table")


def protect_math(text, store):
    """Replace $...$ / $$...$$ with placeholders outside fenced code blocks."""
    def keep(tex, display):
        store.append((tex.strip(), display))
        return f"@@M{len(store) - 1}@@"

    out, fenced = [], False
    parts = re.split(r"(^[ \t]*```.*$)", text, flags=re.M)
    for part in parts:
        if re.match(r"^[ \t]*```", part):
            fenced = not fenced
            out.append(part)
            continue
        if fenced:
            out.append(part)
            continue
        part = re.sub(r"`\$([^`$]+)\$`", lambda m: keep(m.group(1), False), part)
        part = re.sub(r"\$\$(.+?)\$\$", lambda m: keep(m.group(1), True), part, flags=re.S)
        part = re.sub(r"(?<!\\)\$(?!\s)([^$\n]+?)(?<!\s)\$", lambda m: keep(m.group(1), False), part)
        out.append(part)
    return "".join(out)


def restore_math(fragment, store):
    def math_tag(m):
        tex, display = store[int(m.group(1))]
        cls = "tex tex-display" if display else "tex"
        return f'<span class="{cls}">{html.escape(tex)}</span>'
    return re.sub(r"@@M(\d+)@@", math_tag, fragment)


def strip_tags(fragment):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", fragment))).strip()


def strip_tags_keep_math(fragment):
    """Strip HTML tags to plain text while preserving .tex spans as inline $...$ markers."""
    def keep(m):
        tex = re.sub(r"\s+", " ", html.unescape(m.group(1))).strip()
        return f"${tex}$"

    s = re.sub(r'<span class="tex(?:\s+tex-display)?">(.*?)</span>', keep, fragment, flags=re.S)
    s = re.sub(r"</(?:p|li|div|tr|h[1-6])>|<br\s*/?>", " ", s)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def truncate_keeping_math(text, max_visual=260):
    """Truncate text without ever splitting an inline $...$ formula or adding spaces around punctuation."""
    tokens = re.findall(r"(?:\$[^$]+\$|[^\s$])+", text)
    out = []
    vis = 0
    truncated = False
    for tok in tokens:
        plain_tok = re.sub(r"\$[^$]+\$", lambda m: "x" * min(len(m.group(0)) - 2, 16), tok)
        t_vis = len(plain_tok)
        if out and vis + 1 + t_vis > max_visual:
            truncated = True
            break
        out.append(tok)
        vis += (1 if out else 0) + t_vis
    res = " ".join(out)
    if truncated:
        res = res.rstrip(".,;: ") + "…"
    return res


def tex_to_plain_unicode(fragment):
    """Convert HTML headings with .tex spans to clean Unicode for plain-text attributes & sidebar."""
    repls = [
        (r"\bar{\xi}", "ξ̄"),
        (r"\bar{p}", "p̄"),
        (r"\times", "×"),
        (r"\neg", "¬"),
        (r"\lor", "∨"),
        (r"\land", "∧"),
        (r"\supset", "⊃"),
        (r"\equiv", "≡"),
        (r"\Omega", "Ω"),
        (r"\xi", "ξ"),
    ]
    def conv(m):
        t = html.unescape(m.group(1))
        for src, dst in repls:
            t = t.replace(src, dst)
        return t

    s = re.sub(r'<span class="tex(?:\s+tex-display)?">(.*?)</span>', conv, fragment, flags=re.S)
    return strip_tags(s)


def prop_anchor_id(num_str):
    return "prop-" + re.sub(r"[^0-9a-zA-Z]+", "-", num_str.strip()).strip("-")


def prop_depth(num_str):
    if "." not in num_str:
        return 0
    frac = num_str.split(".", 1)[1]
    # Stern tree depth: zeros are bridge markers on their parent; count non-zero digits + 1 if only zeros
    nz = sum(1 for ch in frac if ch != "0")
    return max(1, nz)


def prop_is_zero(num_str):
    return "." in num_str and num_str.split(".", 1)[1].startswith("0")


# --------------------------------------------------------------------------
# 3. Structured block parsing & rendering
# --------------------------------------------------------------------------
def render_inline_md(text, store):
    return restore_math(MD.renderInline(protect_math(text, store)), store)


def parse_prop_blockquote(inner_html, seen_anchors, extracted_nodes):
    """Detect and transform structured Tractatus blockquotes (Tier 1, 2, 3) and callouts.

    Returns (replacement_html, matched_bool).
    """
    # Split blockquote into paragraphs
    paras = re.findall(r"<p>(.*?)</p>", inner_html, flags=re.S)
    if not paras:
        return None, False

    first = paras[0].strip()

    # Callout: Reader note
    if re.match(r"<strong>Σημείωση για τον αναγνώστη", first):
        return f'<aside class="callout-reader">\n{inner_html}\n</aside>', True

    # Callout: Interpretive / translation / caution / clarification notes
    if re.match(r"<strong>(?:Ερμηνευτική σημείωση|Μεταφραστική σημείωση|Προσοχή|Κρίσιμη [Δδ]ιευκρίνιση|Οι όροι στην ελληνική μετάφραση)", first):
        return f'<aside class="callout-note">\n{inner_html}\n</aside>', True

    # Callout: Example
    if re.match(r"<strong>Παράδειγμα", first):
        return f'<aside class="callout-example">\n{inner_html}\n</aside>', True

    # Structured Tractatus Proposition: starts with <strong>N</strong>: or <strong>N.M</strong>:
    # Look for metadata lines starting with "—" (em-dash) inside the blockquote
    # Reconstruct logical lines (Markdown soft breaks become \n inside <p>)
    raw_lines = []
    for p in paras:
        for ln in p.split("\n"):
            s = ln.strip()
            if s:
                raw_lines.append(s)

    m_num = re.match(r"^<strong>([1-7](?:\.\d+)?)</strong>\s*:\s*(.*)$", raw_lines[0], flags=re.S)
    if not m_num:
        return None, False

    num = m_num.group(1)
    el_lines = [m_num.group(2).strip()]
    ogden_txt = ""
    pm_txt = ""
    de_txt = ""
    extra_en_note = ""

    for ln in raw_lines[1:]:
        clean_ln = re.sub(r"<br\s*/?>$", "", ln).strip()
        # Tier 1 metadata lines: — <em>Ogden</em>: ... / — <em>Pears &amp; McGuinness</em>: ... / — <em>Γερμ.</em>: ...
        m_og = re.match(r"^—\s*<em>Ogden(?:\s*&amp;\s*Ramsey)?</em>\s*:\s*(.*)$", clean_ln, flags=re.S)
        m_pm = re.match(r"^—\s*<em>Pears\s*&amp;\s*McGuinness</em>\s*:\s*(.*)$", clean_ln, flags=re.S)
        m_pm_short = re.match(r"^—\s*<em>P&amp;M</em>\s*:\s*(.*)$", clean_ln, flags=re.S)
        m_de = re.match(r"^—\s*<em>Γερμ\.?</em>\s*:\s*(.*)$", clean_ln, flags=re.S)
        # Tier 2/3 combined line: — «German» (English)  OR  — «German»
        m_pair = re.match(r"^—\s*«(.+?)»(?:\s*\((.+)\))?\s*$", clean_ln, flags=re.S)

        if m_og:
            ogden_txt = m_og.group(1).strip()
        elif m_pm:
            pm_txt = m_pm.group(1).strip()
        elif m_pm_short:
            extra_en_note = m_pm_short.group(1).strip()
        elif m_de:
            de_txt = m_de.group(1).strip()
            if de_txt.startswith("«") and de_txt.endswith("»"):
                de_txt = de_txt[1:-1].strip()
        elif m_pair:
            de_txt = m_pair.group(1).strip()
            if m_pair.group(2):
                ogden_txt = m_pair.group(2).strip()
        else:
            el_lines.append(clean_ln)

    # Only treat as structured Tier 1/2/3 card if metadata (German or English) was present
    if not (de_txt or ogden_txt or pm_txt):
        return None, False

    anchor = prop_anchor_id(num)
    id_attr = ""
    if anchor not in seen_anchors:
        seen_anchors.add(anchor)
        id_attr = f' id="{anchor}"'

    el_html = "<br>".join(re.sub(r"<br\s*/?>$", "", s) for s in el_lines)
    # Plain text (no $ markers) for length thresholds; math-preserving text for Tree & Quick-Peek
    el_len = len(strip_tags(el_html))
    de_len = len(strip_tags(de_txt))
    el_tree = strip_tags_keep_math(el_html)
    de_tree = strip_tags_keep_math(de_txt)
    ogden_tree = strip_tags_keep_math(ogden_txt)
    pm_tree = strip_tags_keep_math(pm_txt)

    extracted_nodes.append({
        "num": num,
        "root": num.split(".")[0],
        "depth": prop_depth(num),
        "zero": prop_is_zero(num),
        "kind": "single",
        "el": el_tree,
        "ogden": ogden_tree,
        "pm": pm_tree,
        "de": de_tree,
        "anchor": "#" + anchor,
    })

    # Tier 1: Main propositions 1–7 -> Hero display (Greek -> Ogden & P&M -> German)
    if "." not in num:
        el_hero = re.sub(r"^<strong>(.*)</strong>$", r"\1", el_html, flags=re.S)
        versions = []
        if ogden_txt:
            versions.append(
                f'<div class="prop-en"><span class="prop-ver-label">Ogden &amp; Ramsey (1922)</span>{ogden_txt}</div>'
            )
        if pm_txt:
            versions.append(
                f'<div class="prop-en"><span class="prop-ver-label">Pears &amp; McGuinness (1961)</span>{pm_txt}</div>'
            )
        if de_txt:
            versions.append(
                f'<div class="prop-de"><span class="prop-ver-label">Γερμανικό πρωτότυπο (1921)</span>'
                f'<span class="prop-ver-de">«{de_txt}»</span></div>'
            )
        return (
            f'<div class="prop-hero"{id_attr}>\n'
            f'  <p class="prop-hero-el"><span class="prop-hero-num prop-ref" data-prop="{num}">{num}.</span> {el_hero}</p>\n'
            f'  <div class="prop-hero-versions">\n    ' + "\n    ".join(versions) + "\n  </div>\n"
            f'</div>'
        ), True

    # Tier 2 & 3: Branches & individually quoted sub-propositions
    is_long = el_len > LONG_PROP_THRESHOLD or de_len > LONG_PROP_THRESHOLD + 40
    en_suffix = ""
    if ogden_txt:
        en_suffix = f' <span class="prop-en">({ogden_txt})</span>'
    if extra_en_note:
        en_suffix += f' <span class="prop-en">[P&amp;M: {extra_en_note}]</span>'

    if is_long:
        meta_html = (
            f'<details class="prop-orig">\n'
            f'  <summary>Πρωτότυπο &amp; αγγλικά</summary>\n'
            f'  <div class="prop-orig-body">\n'
            f'    <span class="prop-de">{num}: «{de_txt}»</span>\n'
            f'    {en_suffix.strip()}\n'
            f'  </div>\n'
            f'</details>'
        )
    else:
        meta_html = (
            f'<p class="prop-quote-meta">'
            f'<span class="prop-de">{num}: «{de_txt}»</span>{en_suffix}'
            f'</p>'
        )

    return (
        f'<div class="prop-quote"{id_attr}>\n'
        f'  <p class="prop-quote-el"><span class="prop-ref" data-prop="{num}">{num}</span> {el_html}</p>\n'
        f'  {meta_html}\n'
        f'</div>'
    ), True


def wrap_grouped_sections(html_body, seen_anchors, extracted_nodes):
    """Wrap Tier-4 grouped sub-headings (<h4>2.022 – 2.023 · Title</h4>) in .prop-group cards."""
    # Split HTML into top-level blocks so we can cleanly group a <h4> range header + its prose/lists
    pattern = re.compile(
        r'(<h4[^>]*>\s*([1-7]\.\d+(?:\s*(?:–|,|&amp;)\s*[1-7]\.\d+)+|[1-7]\.\d+)\s*·\s*(.*?)\s*</h4>)',
        flags=re.S,
    )
    matches = list(pattern.finditer(html_body))
    if not matches:
        return html_body

    # Process from end to start so character offsets stay valid
    out = html_body
    stop_re = re.compile(
        r'<(?:h[234]\b|hr\b|div class="prop-(?:hero|quote|group)"|aside class="callout-|div class="inline-widget")'
    )
    for m in reversed(matches):
        range_str = re.sub(r"\s+", " ", strip_tags(m.group(2))).strip()
        title_html = m.group(3).strip()
        title_tree = strip_tags_keep_math(title_html)
        body_start = m.end()
        next_stop = stop_re.search(out, body_start)
        body_end = next_stop.start() if next_stop else len(out)
        inner_body = out[body_start:body_end].strip()

        anchor = prop_anchor_id(range_str.split("–")[0].split(",")[0].strip())
        if anchor in seen_anchors:
            anchor = prop_anchor_id(range_str)
        seen_anchors.add(anchor)

        first_num = re.match(r"([1-7]\.\d+)", range_str).group(1)
        summary_tree = strip_tags_keep_math(inner_body)
        cut = truncate_keeping_math(summary_tree, 260)

        extracted_nodes.append({
            "num": range_str,
            "root": first_num.split(".")[0],
            "depth": prop_depth(first_num),
            "zero": prop_is_zero(first_num),
            "kind": "group",
            "title": title_tree,
            "el": cut,
            "ogden": "",
            "pm": "",
            "de": "",
            "anchor": "#" + anchor,
            "_order_pos": m.start(),
        })

        card = (
            f'<div class="prop-group" id="{anchor}">\n'
            f'  <div class="prop-group-head">'
            f'<span class="prop-range-badge">{html.escape(range_str)}</span>'
            f'<span class="prop-group-title">{title_html}</span></div>\n'
            f'  {inner_body}\n'
            f'</div>'
        )
        out = out[:m.start()] + card + out[body_end:]
    return out


def wrap_dialogue_sections(html_body):
    """Wrap any <h3>...Φιλοσοφικός διάλογος...</h3> tail block in .callout-dialogue."""
    m = re.search(r'<h3[^>]*>[^<]*Φιλοσοφικός διάλογος.*?</h3>', html_body, flags=re.S | re.I)
    if not m:
        return html_body
    # Ends at next <h3> or <hr> or end of section
    after = html_body[m.end():]
    stop = re.search(r'<h3\b', after)
    end_idx = m.end() + (stop.start() if stop else len(after))
    inner = html_body[m.start():end_idx].strip()
    wrapped = f'<aside class="callout-dialogue">\n{inner}\n</aside>'
    return html_body[:m.start()] + wrapped + html_body[end_idx:]


def render_markdown_chunk(heading, body, sec_id, seen_anchors, extracted_nodes, branches_out, widget_html, valid_phil_ids, valid_concept_ids):
    """Render one `##` section of the Markdown into semantic HTML."""
    store = []
    # Strip trailing horizontal rules between top-level sections
    src = body.rstrip()
    src = re.sub(r"\n---\s*$", "", src)

    # Replace inline widget directives before Markdown render
    widget_placeholder = "@@WIDGET_LOGICAL_SPACE@@"
    src = src.replace("<!-- widget: logical-space -->", f"\n\n{widget_placeholder}\n\n")

    rendered = MD.render(protect_math(src, store))
    rendered = restore_math(rendered, store)

    # Inject inline widget
    rendered = rendered.replace(f"<p>{widget_placeholder}</p>", widget_html)
    rendered = rendered.replace(widget_placeholder, widget_html)

    # Style <h3> headings: detect main branches (n.m) and preliminary clusters (n.0x)
    h3_counter = [0]

    def handle_h3(m):
        inner = m.group(1).strip()
        plain = tex_to_plain_unicode(inner)
        h3_counter[0] += 1

        # Match main branch heading: e.g. "Κλάδος 2.1: ..." or "3. Κύριος κλάδος 2.1 (2.1 – 2.19): ..."
        m_br = re.match(r"^(?:\d+\.\s+)?(?:Κύριος\s+)?[Κκ]λάδος\s+([1-7]\.[1-9])\b(?:\s*\([^)]*\))?\s*[:·–-]\s*(.+)$", plain)
        if m_br:
            num = m_br.group(1)
            short_title = m_br.group(2).strip()
            bid = "branch-" + num.replace(".", "-")
            if bid not in seen_anchors:
                seen_anchors.add(bid)
            branches_out.append((sec_id, num, short_title, bid))
            return f'<h3 class="branch-heading" id="{bid}">{inner}</h3>'

        if re.search(r"Προκαταρκτικ", plain):
            pid = f"prelim-{sec_id}-{h3_counter[0]}"
            while pid in seen_anchors:
                h3_counter[0] += 1
                pid = f"prelim-{sec_id}-{h3_counter[0]}"
            seen_anchors.add(pid)
            return f'<h3 class="prelim-heading" id="{pid}">{inner}</h3>'

        hid = f"{sec_id}-h{h3_counter[0]}"
        while hid in seen_anchors:
            h3_counter[0] += 1
            hid = f"{sec_id}-h{h3_counter[0]}"
        seen_anchors.add(hid)
        return f'<h3 id="{hid}">{inner}</h3>'

    rendered = re.sub(r"<h3>(.*?)</h3>", handle_h3, rendered, flags=re.S)

    # Also detect legacy <h4>Κλάδος 1.1: ...</h4> so Stage 1 sidebar picks up 1.1 & 1.2 right away
    def handle_h4_branch(m):
        inner = m.group(1).strip()
        plain = strip_tags(inner)
        m_br = re.match(r"^[Κκ]λάδος\s+([1-7]\.[1-9])\s*[:·–-]\s*(.+)$", plain)
        if m_br:
            num = m_br.group(1)
            bid = "branch-" + num.replace(".", "-")
            if not any(b[1] == num for b in branches_out):
                branches_out.append((sec_id, num, m_br.group(2).strip(), bid))
                seen_anchors.add(bid)
            return f'<h4 id="{bid}">{inner}</h4>'
        return m.group(0)

    rendered = re.sub(r"<h4>(.*?)</h4>", handle_h4_branch, rendered, flags=re.S)

    # Transform blockquotes (Tier 1, 2, 3 propositions, examples, notes, reader note)
    def handle_blockquote(m):
        inner = m.group(1).strip()
        replaced, ok = parse_prop_blockquote(inner, seen_anchors, extracted_nodes)
        if ok:
            return replaced
        return f'<blockquote class="hw-quote">\n{inner}\n</blockquote>'

    rendered = re.sub(r"<blockquote>\s*(.*?)\s*</blockquote>", handle_blockquote, rendered, flags=re.S)

    # Wrap Tier-4 grouped sub-sections (<h4>range · title</h4>)
    rendered = wrap_grouped_sections(rendered, seen_anchors, extracted_nodes)

    # Wrap Philosophical Dialogue closing sections
    rendered = wrap_dialogue_sections(rendered)

    # Tables: wrap in .table-wrap and assign special anchors for ontology & meaning tables
    def handle_table(m):
        tbl = m.group(0)
        extra_id = ""
        if "Sachverhalt" in tbl and "Sachlage" in tbl and "Tatsache" in tbl and "term-ontology-table" not in seen_anchors:
            seen_anchors.add("term-ontology-table")
            extra_id = ' id="term-ontology-table"'
        elif "Sinnvoll" in tbl and "Sinnlos" in tbl and "Unsinnig" in tbl and "term-meaning-table" not in seen_anchors:
            seen_anchors.add("term-meaning-table")
            extra_id = ' id="term-meaning-table"'
        return f'<div class="table-wrap"{extra_id}>{tbl.replace("<table>", "<table class=\"hw-table\">", 1)}</div>'

    rendered = re.sub(r"<table>.*?</table>", handle_table, rendered, flags=re.S)

    # Style targeted lab, philosopher & concept links (#lab-*, #phil-*, #concept-*, #tab=tree) and validate targets
    def style_link(m):
        href, label = m.group(1), m.group(2)
        if href.startswith("#lab-"):
            target_id = href[1:]
            if target_id not in VALID_LAB_IDS:
                raise SystemExit(f"build_html: unknown lab anchor '{href}' in {sec_id}")
            return f'<a class="lab-pill" href="{href}">{label}</a>'
        if href == "#tab=tree":
            return f'<a class="lab-pill" href="{href}">{label}</a>'
        if href.startswith("#phil-"):
            slug = href[6:]
            if slug not in valid_phil_ids:
                raise SystemExit(f"build_html: unknown philosopher anchor '{href}' in {sec_id}")
            return f'<a class="phil-pill" href="{href}" title="Γρήγορη προβολή φιλοσόφου (Ctrl+κλικ για νέα καρτέλα)">{label}</a>'
        if href.startswith("#concept-"):
            cid = href[9:]
            if cid not in valid_concept_ids:
                raise SystemExit(f"build_html: unknown concept anchor '{href}' in {sec_id}")
            return f'<a class="concept-ref" href="{href}" data-concept="{cid}" title="Γρήγορη προβολή έννοιας">{label}</a>'
        return m.group(0)

    rendered = re.sub(r'<a href="(#[^"]+)">(.*?)</a>', style_link, rendered, flags=re.S)

    # Check for unrendered Markdown artifacts outside <pre>
    leftovers = re.findall(r"\*\*|@@M\d+@@", re.sub(r"<pre.*?</pre>", "", rendered, flags=re.S))
    return rendered, leftovers


# --------------------------------------------------------------------------
# 4. Safe HTML-aware auto-linking of German key terms & inline prop numbers
# --------------------------------------------------------------------------
def autolink_terms_and_props(fragment, terms, valid_prop_nums):
    """Auto-link German key terms (.term-ref) and inline proposition numbers (.prop-ref)
    in text nodes only, skipping headings, math, English spans, code, links, and summaries."""
    form_to_id = {}
    for t in terms:
        for form in t["forms"]:
            form_to_id[form] = t["id"]
    forms_sorted = sorted(form_to_id.keys(), key=len, reverse=True)
    term_re = re.compile(
        r"(?<![A-Za-zÄÖÜäöüß])(" + "|".join(re.escape(f) for f in forms_sorted) + r")(?![A-Za-zÄÖÜäöüß])"
    )
    # Inline proposition numbers (decimals >= 1.1; allow trailing sentence-ending period, block .digit like 1.2.3)
    prop_re = re.compile(r"(?<![0-9A-Za-z.,])([1-7]\.\d{1,5})(?![0-9A-Za-z]|\.\d)")

    skip_tags = {"pre", "code", "script", "style", "a", "h1", "h2", "h3", "h4", "summary"}
    skip_classes = ("tex", "prop-en", "term-ref", "prop-ref", "prop-ver-label", "prop-range-badge", "inline-widget")

    parts = re.split(r"(<[^>]+>)", fragment)
    stack = []  # list of (tag, skipped_bool)

    def is_skipped():
        return any(sk for _, sk in stack)

    out = []
    for part in parts:
        if part.startswith("<"):
            if part.startswith("</"):
                tag = re.match(r"</([a-zA-Z0-9]+)", part)
                if tag:
                    tname = tag.group(1).lower()
                    for idx in range(len(stack) - 1, -1, -1):
                        if stack[idx][0] == tname:
                            stack = stack[:idx]
                            break
            elif not part.endswith("/>") and not part.startswith("<!"):
                m_tag = re.match(r"<([a-zA-Z0-9]+)", part)
                if m_tag:
                    tname = m_tag.group(1).lower()
                    if tname not in {"br", "hr", "img", "input", "meta", "link"}:
                        cls_m = re.search(r'class="([^"]+)"', part)
                        cls_list = cls_m.group(1).split() if cls_m else []
                        sk = (tname in skip_tags) or any(c in skip_classes for c in cls_list)
                        stack.append((tname, sk))
            out.append(part)
            continue

        if is_skipped() or not part.strip():
            out.append(part)
            continue

        # Replace German terms first, then proposition decimals in non-tagged stretches
        def repl_term(m):
            word = m.group(1)
            tid = form_to_id[word]
            return f'<span class="term-ref" data-term="{tid}">{word}</span>'

        text = term_re.sub(repl_term, part)

        # Link inline proposition decimals outside the newly created <span> tags
        sub_parts = re.split(r"(<[^>]+>)", text)
        in_span = 0
        for idx, sp in enumerate(sub_parts):
            if sp.startswith("<span"):
                in_span += 1
            elif sp == "</span>":
                in_span = max(0, in_span - 1)
            elif not sp.startswith("<") and in_span == 0:
                def repl_prop(m):
                    num = m.group(1)
                    if num in valid_prop_nums:
                        return f'<span class="prop-ref" data-prop="{num}">{num}</span>'
                    return num
                sub_parts[idx] = prop_re.sub(repl_prop, sp)
        out.append("".join(sub_parts))

    return "".join(out)


# --------------------------------------------------------------------------
# 5. Sidebar & Tree Data Assembly
# --------------------------------------------------------------------------
def shorten_branch_label(label):
    """Keep sidebar branch labels concise (strip spaced parentheticals and truncate cleanly)."""
    s = re.sub(r"\s+\([^)]*\)", "", label).strip()
    if len(s) > 42:
        s = s[:42].rsplit(" ", 1)[0].rstrip(",·:;& ")
        # Avoid leaving an unclosed opening quote « at the truncation edge
        if s.count("«") > s.count("»"):
            s = s.rsplit("«", 1)[0].rstrip(",·:;& ")
        s += "…"
    return s


def build_sidebar_nav(branches_by_sec):
    rows = []
    for sec_id in SECTION_ORDER:
        code, _, full_title, short_label = SECTION_META[sec_id]
        is_part = code in ("Α", "Β", "Γ")
        part_cls = " idx-part" if is_part else ""
        rows.append(
            f'<a href="#{sec_id}" data-section="{sec_id}" onclick="navigateMasterAnchor(\'{sec_id}\')" '
            f'class="idx-row idx-main{part_cls}" title="{html.escape(full_title)}">'
            f'<span class="idx-int">{code}</span><span class="idx-frac"></span>'
            f'<span class="idx-label">{html.escape(short_label)}</span></a>'
        )
        # Main branches (only n.1..n.6; never n.0x in the sidebar)
        for num, btitle, bid in branches_by_sec.get(sec_id, []):
            int_part, frac_part = num.split(".", 1)
            short_b = shorten_branch_label(btitle)
            rows.append(
                f'<a href="#{bid}" onclick="navigateMasterAnchor(\'{sec_id}\')" '
                f'class="idx-row idx-sub" title="{html.escape(num + " " + btitle)}">'
                f'<span class="idx-int">{int_part}</span><span class="idx-frac">.{frac_part}</span>'
                f'<span class="idx-label">{html.escape(short_b)}</span></a>'
            )
    return "\n            ".join(rows)


def prop_sort_key(num_str):
    """Order proposition numbers strictly in Tractatus decimal / Stern tree order."""
    first = re.match(r"([1-7])(?:\.(\d+))?", num_str.strip())
    if not first:
        return (9, "")
    root = int(first.group(1))
    frac = first.group(2) or ""
    # In the Tractatus, decimal digits sort lexicographically ("01" < "02" < "1" < "11" < "2")
    return (root, frac)


def merge_tree_data(extracted_nodes, pm_quotes):
    """Merge extracted Markdown nodes with the 65 existing Pears & McGuinness comparison entries."""
    pm_by_num = {item["num"]: item for item in pm_quotes}
    by_key = {}
    ordered = []

    for node in extracted_nodes:
        key = (node["kind"], node["num"])
        if key in by_key:
            continue
        item = dict(node)
        item.pop("_order_pos", None)
        if item["kind"] == "single" and item["num"] in pm_by_num:
            pm_src = pm_by_num[item["num"]]
            if not item.get("pm"):
                item["pm"] = pm_src["pm"]
            if not item.get("note"):
                item["note"] = pm_src.get("note", "")
        by_key[key] = item
        ordered.append(item)

    # Ensure every entry from pm_quotes.json is always present (important during Stage 1 & for Quick-Peek)
    for pm_src in pm_quotes:
        key = ("single", pm_src["num"])
        if key not in by_key:
            item = dict(pm_src)
            item["kind"] = "single"
            item["anchor"] = "#sec-prop" + item["root"]
            by_key[key] = item
            ordered.append(item)

    ordered.sort(key=lambda x: (prop_sort_key(x["num"]), 0 if x["kind"] == "single" else 1))
    return ordered


# --------------------------------------------------------------------------
# 6. Full Page Assembly
# --------------------------------------------------------------------------
def check_proposition_coverage(tree_data):
    """Stop the build unless each of the 526 numbered propositions is covered exactly once,
    either by a quoted card or by one grouped synthesis (ranges such as "2.013 – 2.0141, 2.0201")."""
    canon = json.loads((ASSETS_DIR / "proposition_numbers.json").read_text(encoding="utf8"))
    if len(canon) != 526 or len(set(canon)) != 526:
        raise SystemExit("build_html: proposition_numbers.json must list the 526 distinct numbers")
    known = set(canon)
    seen = {}
    problems = []
    for item in tree_data:
        label = item["num"]
        if item["kind"] == "single":
            covered = [label]
        else:
            covered = []
            for part in label.split(","):
                ends = [x.strip() for x in part.replace("-", "–").split("–")]
                if len(ends) > 2 or not all(ends):
                    problems.append(f"unreadable range '{label}'")
                    continue
                unknown = [x for x in ends if x not in known]
                if unknown:
                    problems.append(f"'{label}' names {unknown}, not a proposition number")
                    continue
                # the decimal numbering sorts as plain strings (2.01 < 2.011 < 2.02)
                covered += [n for n in canon if ends[0] <= n <= ends[-1]]
        for n in covered:
            if n not in known:
                problems.append(f"'{n}' is not a proposition number")
            elif n in seen:
                problems.append(f"{n} is covered twice: '{seen[n]}' and '{label}'")
            else:
                seen[n] = label
    missing = [n for n in canon if n not in seen]
    if missing:
        problems.append(f"not covered by any card or group: {missing}")
    if problems:
        raise SystemExit("build_html: proposition coverage:\n  " + "\n  ".join(problems))


def safe_json_for_script(obj):
    return json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")


def build(strict_branches=False):
    md = MD_PATH.read_text(encoding="utf8").replace("\r\n", "\n")
    terms = json.loads((ASSETS_DIR / "terms.json").read_text(encoding="utf8"))
    concepts = json.loads((ASSETS_DIR / "concepts.json").read_text(encoding="utf8"))
    pm_quotes = json.loads((ASSETS_DIR / "pm_quotes.json").read_text(encoding="utf8"))
    philosophers = json.loads((ASSETS_DIR / "philosophers.json").read_text(encoding="utf8"))
    widget_html = (ASSETS_DIR / "widget_logical_space.html").read_text(encoding="utf8").strip()
    labs_html = (ASSETS_DIR / "labs.html").read_text(encoding="utf8").rstrip()
    styles_css = (ASSETS_DIR / "styles.css").read_text(encoding="utf8").rstrip()
    labs_js = (ASSETS_DIR / "labs.js").read_text(encoding="utf8").rstrip()
    app_js = (ASSETS_DIR / "app.js").read_text(encoding="utf8").rstrip()

    valid_phil_ids = {p["id"] for p in philosophers}
    valid_concept_ids = {c["id"] for c in concepts}

    grouped_md = {}
    for heading, body in split_sections(md):
        target = target_for(heading)
        if target is None:
            continue
        grouped_md.setdefault(target, []).append((heading, body))

    seen_anchors = set()
    extracted_nodes = []
    branches_list = []
    warnings = []
    rendered_sections = {}

    for sec_id in SECTION_ORDER:
        chunks_md = grouped_md.get(sec_id, [])
        if not chunks_md:
            raise SystemExit(f"build_html: no Markdown content mapped to section '{sec_id}'")
        html_parts = []
        for idx, (heading, body) in enumerate(chunks_md):
            chunk_html, leftovers = render_markdown_chunk(
                heading, body, sec_id, seen_anchors, extracted_nodes, branches_list, widget_html, valid_phil_ids, valid_concept_ids
            )
            if leftovers:
                warnings.append(f"{heading[:42]}: unrendered markup {sorted(set(leftovers))[:4]}")
            # When multiple ## map to the same HTML section (e.g. Εισαγωγή + Μέρος Α, or Μέρος Γ + Επίμετρο + Βιβλιογραφία),
            # emit the sub-part heading cleanly for the 2nd+ chunk.
            if idx > 0:
                sub_id = f"{sec_id}-part-{idx + 1}"
                seen_anchors.add(sub_id)
                chunk_html = f'<h3 id="{sub_id}">{html.escape(heading)}</h3>\n' + chunk_html
            html_parts.append(chunk_html)
        rendered_sections[sec_id] = "\n<hr>\n".join(html_parts)

    tree_data = merge_tree_data(extracted_nodes, pm_quotes)
    check_proposition_coverage(tree_data)
    valid_prop_nums = {item["num"] for item in tree_data if item["kind"] == "single"}

    # Validate that all terms.json targets and tree_data anchors resolve in the generated page
    all_anchors = seen_anchors | set(SECTION_ORDER)
    bad_terms = [
        (t["id"], t["target"])
        for t in terms
        if t["target"].lstrip("#") not in all_anchors
    ]
    if bad_terms:
        raise SystemExit(f"build_html: unresolved term targets in terms.json: {bad_terms}")
    bad_tree = [
        (item["num"], item["anchor"])
        for item in tree_data
        if item["anchor"].lstrip("#") not in all_anchors
    ]
    if bad_tree:
        raise SystemExit(f"build_html: unresolved tree anchors: {bad_tree}")
    bad_concepts = [
        (c["id"], c["target"])
        for c in concepts
        if c["target"].lstrip("#") not in all_anchors
    ]
    if bad_concepts:
        raise SystemExit(f"build_html: unresolved concept targets in concepts.json: {bad_concepts}")
    bad_concept_labs = [
        (c["id"], c["labTarget"])
        for c in concepts
        if c.get("labTarget") and c["labTarget"].lstrip("#") not in VALID_LAB_IDS
    ]
    if bad_concept_labs:
        raise SystemExit(f"build_html: unknown labTarget in concepts.json: {bad_concept_labs}")

    # Auto-link German terms & inline proposition numbers across rendered sections
    sections_html = []
    for sec_id in SECTION_ORDER:
        _, badge, h2_title, _ = SECTION_META[sec_id]
        body_linked = autolink_terms_and_props(rendered_sections[sec_id], terms, valid_prop_nums)
        sections_html.append(
            f'        <section id="{sec_id}" class="master-section">\n'
            f'          <div class="sec-header">\n'
            f'            <span class="hw-badge">{html.escape(badge)}</span>\n'
            f'            <h2>{html.escape(h2_title)}</h2>\n'
            f'          </div>\n'
            f'          <div class="analysis-body">\n{body_linked}\n          </div>\n'
            f'        </section>'
        )

    # Group branches by section in numeric order
    branches_by_sec = {}
    found_branch_nums = []
    for sec_id, num, btitle, bid in branches_list:
        branches_by_sec.setdefault(sec_id, []).append((num, btitle, bid))
        found_branch_nums.append(num)
    for sec_id in branches_by_sec:
        branches_by_sec[sec_id].sort(key=lambda x: prop_sort_key(x[0]))

    if strict_branches:
        missing = [b for b in EXPECTED_MAIN_BRANCHES if b not in found_branch_nums]
        if missing:
            raise SystemExit(f"build_html: missing main branch headings in Markdown: {missing}")

    sidebar_nav_html = build_sidebar_nav(branches_by_sec)
    filter_options = ['<option value="all">Όλες οι ενότητες</option>'] + [
        f'<option value="{sec_id}">{SECTION_META[sec_id][0]} · {html.escape(SECTION_META[sec_id][3])}</option>'
        for sec_id in SECTION_ORDER
    ]

    page = TEMPLATE.format(
        katex=KATEX,
        css=styles_css,
        filter_options="\n              ".join(filter_options),
        sidebar_nav=sidebar_nav_html,
        sections="\n\n".join(sections_html),
        labs_html=labs_html,
        repo=REPO_URL,
        tree_json=safe_json_for_script(tree_data),
        terms_json=safe_json_for_script(terms),
        concepts_json=safe_json_for_script(concepts),
        phils_json=safe_json_for_script(philosophers),
        labs_js=labs_js,
        app_js=app_js,
    )

    stats = {
        "sections": len(SECTION_ORDER),
        "branches": len(found_branch_nums),
        "tree_nodes": len(tree_data),
        "terms": len(terms),
    }
    return page, stats, warnings


TEMPLATE = """<!DOCTYPE html>
<!-- GENERATED by tools/build_html.py from Tractatus Logico-Philosophicus/TRACTATUS_LOGICO_PHILOSOPHICUS_ANALYSIS_1-7.md
     and tools/tractatus/*. Do not edit by hand. -->
<html lang="el">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tractatus Logico-Philosophicus: ανάλυση των προτάσεων 1–7 και εργαστήρια</title>
  <meta name="description" content="Πλήρης ελληνική φιλοσοφική, λογική και δομική ανάλυση του Tractatus Logico-Philosophicus του Ludwig Wittgenstein (προτάσεις 1–7), με δενδροειδή μορφή και διαδραστικά εργαστήρια.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Commissioner:wght@400..700&family=JetBrains+Mono:wght@400;600&family=Literata:ital,opsz,wght@0,7..72,400..700;1,7..72,400..700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{katex}/katex.min.css">
  <script>
    // Apply saved theme before first paint (shared with index.html and essay.html).
    (function () {{
      var mode = null;
      try {{ mode = localStorage.getItem('hw-tlp-theme'); }} catch (e) {{}}
      if (mode === 'dark') document.documentElement.classList.add('dark');
    }})();
  </script>
  <style>
{css}
  </style>
</head>
<body data-tab="master">
  <a class="skip-link" href="#masterContentContainer">Μετάβαση στο κείμενο</a>

  <header id="siteHeader">
    <div class="hdr">
      <div class="hdr-brand">
        <button type="button" onclick="openMobileNav()" class="hdr-icon-btn" aria-label="Άνοιγμα περιεχομένων">
          <svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><path d="M2 4h12M2 8h12M2 12h12" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
        </button>
        <a class="hdr-title" href="index.html" title="Αρχική σελίδα">
          <span class="hdr-title-main">Tractatus Logico-Philosophicus</span>
          <span class="hdr-title-sub">Ludwig Wittgenstein: ανάλυση και εργαστήρια</span>
        </a>
      </div>

      <div class="hdr-tabs" role="tablist" aria-label="Κύριες ενότητες της σελίδας">
        <button type="button" onclick="switchMainTab('master')" id="tab-btn-master" role="tab" aria-selected="true" class="hw-tab hw-btn-active" title="Ανάλυση των προτάσεων 1–7 (πλήκτρο 1)">Ανάλυση 1–7</button>
        <button type="button" onclick="switchMainTab('tree')" id="tab-btn-tree" role="tab" aria-selected="false" class="hw-tab" title="Δενδροειδής μορφή των προτάσεων (πλήκτρο 2)">Δενδροειδής μορφή</button>
        <button type="button" onclick="switchMainTab('logic')" id="tab-btn-logic" role="tab" aria-selected="false" class="hw-tab" title="Εργαστήριο λογικής (πλήκτρο 3)">Εργαστήριο λογικής</button>
        <button type="button" onclick="switchMainTab('visual')" id="tab-btn-visual" role="tab" aria-selected="false" class="hw-tab" title="Οπτικά μοντέλα και γραμμόφωνο (πλήκτρο 4)">Οπτικά μοντέλα</button>
        <button type="button" onclick="switchMainTab('science')" id="tab-btn-science" role="tab" aria-selected="false" class="hw-tab" title="Επιστήμη, γάντι τεσσάρων διαστάσεων και σκάλα (πλήκτρο 5)">Επιστήμη και σκάλα</button>
        <button type="button" onclick="switchMainTab('philosophers')" id="tab-btn-philosophers" role="tab" aria-selected="false" class="hw-tab" title="Οι δώδεκα φιλόσοφοι (πλήκτρο 6)">Φιλόσοφοι</button>
      </div>

      <div class="hdr-tools">
        <div class="hdr-search" role="search">
          <input id="globalSearchInput" type="search"
            placeholder="Αναζήτηση: 4.0312, Sachverhalt"
            aria-label="Αναζήτηση στην ανάλυση" autocomplete="off" spellcheck="false"
            oninput="handleGlobalSearch(this.value)" />
          <kbd class="hdr-kbd" aria-hidden="true">/</kbd>
          <button type="button" onclick="clearGlobalSearch()" id="clearSearchBtn" hidden class="hdr-search-clear" title="Καθαρισμός (Esc)" aria-label="Καθαρισμός αναζήτησης">✕</button>
        </div>
        <a href="index.html" class="hdr-link" title="Αρχική σελίδα του φακέλου">Αρχική</a>
        <a href="essay.html" class="hdr-link" title="Δοκίμιο: Λογική, γλώσσα και μηχανές">Δοκίμιο</a>
        <button type="button" onclick="toggleArchitecturalTheme()" id="themeToggleBtn" class="hdr-link" title="Εναλλαγή φωτεινού και σκοτεινού θέματος">Σκοτεινό θέμα</button>
      </div>
    </div>

    <div id="searchNavBar" hidden>
      <div class="search-nav-inner">
        <div class="search-nav-group">
          <span id="searchCountBadge" class="hw-badge">0 ευρήματα</span>
          <div id="searchHitControls" hidden class="search-nav-group">
            <button type="button" onclick="stepSearchHit(-1)" class="hw-btn" title="Προηγούμενο εύρημα (Shift+Enter)">‹ Προηγ.</button>
            <span id="searchHitPos" class="search-hit-pos">0 / 0</span>
            <button type="button" onclick="stepSearchHit(1)" class="hw-btn" title="Επόμενο εύρημα (Enter)">Επόμ. ›</button>
          </div>
        </div>
        <div id="searchCrossViewLinks" class="search-nav-group"></div>
      </div>
    </div>

    <div class="progress-track">
      <div id="readingProgressBar" class="progress-fill"></div>
    </div>
  </header>

  <div id="appShell">

    <!-- VIEW: MASTER ANALYSIS (1–7) -->
    <div id="view-master" class="tab-view">
      <aside id="desktopSidebar" aria-label="Περιεχόμενα">
        <div class="idx-bar">
          <span class="idx-title">Περιεχόμενα</span>
          <button type="button" id="sidebarFoldBtn" class="idx-fold" onclick="toggleSidebarFold()" aria-expanded="true" aria-controls="sidebarInnerContent" aria-label="Σύμπτυξη περιεχομένων" title="Σύμπτυξη περιεχομένων (πλήκτρο [)">
            <svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><path d="M10 3 5 8l5 5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </button>
        </div>
        <div id="sidebarInnerContent">
          <div class="idx-filter">
            <label for="sectionFilterSelect">Εμφάνιση</label>
            <select id="sectionFilterSelect" onchange="filterMasterSections(this.value)">
              {filter_options}
            </select>
          </div>
          <nav id="masterNavList" class="idx" aria-label="Περιεχόμενα της ανάλυσης">
            {sidebar_nav}
          </nav>
          <p class="idx-tip">
            Κάντε κλικ σε αριθμούς προτάσεων (π.χ. <strong>4.0312</strong>), γερμανικούς όρους (<em>Sachverhalt</em>), βασικές έννοιες ή ονόματα φιλοσόφων για γρήγορη προβολή χωρίς να χάσετε τη θέση σας.
          </p>
        </div>
      </aside>

      <main id="masterContentContainer">
{sections}
      </main>
    </div>

{labs_html}

  <footer class="site-footer">
    <p>Ludwig Wittgenstein, <em>Tractatus Logico-Philosophicus</em> (1921/1922): ανάλυση των προτάσεων 1–7. Κείμενο CC BY 4.0, παραγόμενο αυτόματα από το <a href="{repo}/blob/main/Tractatus%20Logico-Philosophicus/TRACTATUS_LOGICO_PHILOSOPHICUS_ANALYSIS_1-7.md">Markdown</a>.</p>
    <p><a href="index.html">Αρχική</a> · <a href="essay.html">Δοκίμιο</a> · <a href="{repo}">Αποθετήριο στο GitHub</a></p>
  </footer>

  <script defer src="{katex}/katex.min.js" onload="if (typeof renderAllMath === 'function') renderAllMath()"></script>
  <script>
    const TLP_TREE_DATA = {tree_json};
    const TLP_TERMS_DATA = {terms_json};
    const TLP_CONCEPTS_DATA = {concepts_json};
    const PHILOSOPHERS_DATA = {phils_json};

{labs_js}

{app_js}
  </script>
</body>
</html>
"""


def main():
    page, stats, warnings = build(strict_branches=True)
    for w in warnings:
        print("warning:", w)
    if "--check" in sys.argv:
        existing = HTML_PATH.read_bytes().decode("utf8") if HTML_PATH.exists() else ""
        if existing != page:
            print("HTML is out of date: run  python tools/build_html.py")
            sys.exit(1)
        print("HTML is up to date with the Markdown.")
        return
    HTML_PATH.write_bytes(page.encode("utf8"))
    print(
        f"built {HTML_PATH.name} ({len(page) // 1000}k, LF; "
        f"{stats['sections']} sections, {stats['branches']} main branches, "
        f"{stats['tree_nodes']} tree nodes, {stats['terms']} terms)"
    )


if __name__ == "__main__":
    main()
