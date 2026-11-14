#!/usr/bin/env python3
"""Render the essay's Markdown source into a Word (.docx) file.

The Markdown file is the single source of truth for the essay. This script
turns it into a .docx with the standard library only (a .docx is a zip of XML
files); markdown-it-py does the parsing, as in build_html.py.

Usage:
    python tools/build_docx.py            # rebuild the .docx
    python tools/build_docx.py --check    # exit 1 if the .docx is out of date

Supported Markdown: headings (# title, ## to ####), paragraphs, **bold**,
*italic*, `code`, bullet and numbered lists (nested), block quotes, tables and
horizontal rules. A paragraph that directly follows the title and is entirely
in italics becomes the subtitle. Anything else stops the build.

Requires: markdown-it-py  (pip install markdown-it-py)
"""
import sys
import zipfile
from io import BytesIO
from pathlib import Path
from xml.sax.saxutils import escape

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent.parent
MD_PATH = ROOT / "Logiki_Glossa_Michanes.md"
DOCX_PATH = ROOT / "docs" / "Logiki_Glossa_Michanes.docx"  # offered for download on the essay page

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
BODY_FONT = "Cambria"
HEAD_FONT = "Calibri"
CODE_FONT = "Consolas"
HEADING_STYLE = {"h1": "Title", "h2": "Heading1", "h3": "Heading2", "h4": "Heading3"}


# --------------------------------------------------------------------------
# 1. Inline content -> runs
# --------------------------------------------------------------------------
def run(text, bold=False, italic=False, code=False):
    props = ""
    if code:
        props += f'<w:rFonts w:ascii="{CODE_FONT}" w:hAnsi="{CODE_FONT}" w:cs="{CODE_FONT}"/>'
    if bold:
        props += "<w:b/>"
    if italic:
        props += "<w:i/>"
    rpr = f"<w:rPr>{props}</w:rPr>" if props else ""
    return f'<w:r>{rpr}<w:t xml:space="preserve">{escape(text)}</w:t></w:r>'


def runs(inline):
    """The runs of one markdown-it `inline` token."""
    out, bold, italic = [], 0, 0
    for child in inline.children or []:
        kind = child.type
        if kind == "text":
            out.append(run(child.content, bold > 0, italic > 0))
        elif kind == "code_inline":
            out.append(run(child.content, bold > 0, italic > 0, code=True))
        elif kind == "softbreak":
            out.append(run(" ", bold > 0, italic > 0))
        elif kind == "hardbreak":
            out.append("<w:r><w:br/></w:r>")
        elif kind == "strong_open":
            bold += 1
        elif kind == "strong_close":
            bold -= 1
        elif kind == "em_open":
            italic += 1
        elif kind == "em_close":
            italic -= 1
        elif kind in ("link_open", "link_close"):
            pass  # the link text is kept; addresses are written out in the text
        else:
            raise SystemExit(f"build_docx: unsupported inline element '{kind}'")
    return "".join(out)


def all_italic(inline):
    kinds = [c.type for c in inline.children or []]
    return len(kinds) >= 3 and kinds[0] == "em_open" and kinds[-1] == "em_close"


def paragraph(content, style=None, numbering=None, indent=None):
    props = f'<w:pStyle w:val="{style}"/>' if style else ""
    if numbering:
        level, num_id = numbering
        props += f'<w:numPr><w:ilvl w:val="{level}"/><w:numId w:val="{num_id}"/></w:numPr>'
    if indent:
        props += f'<w:ind w:left="{indent}"/>'
    ppr = f"<w:pPr>{props}</w:pPr>" if props else ""
    return f"<w:p>{ppr}{content}</w:p>"


# --------------------------------------------------------------------------
# 2. Block tokens -> body XML
# --------------------------------------------------------------------------
def table(tokens, i):
    """Render the table that starts at tokens[i]; return (xml, next index)."""
    rows, cells, header = [], [], False
    while tokens[i].type != "table_close":
        t = tokens[i]
        if t.type == "thead_open":
            header = True
        elif t.type == "thead_close":
            header = False
        elif t.type in ("th_open", "td_open"):
            content = runs(tokens[i + 1])
            if header:
                content = content.replace("<w:r><w:t", "<w:r><w:rPr><w:b/></w:rPr><w:t")
            shade = '<w:tcPr><w:shd w:val="clear" w:color="auto" w:fill="EDEDED"/></w:tcPr>' if header else ""
            cells.append(f"<w:tc>{shade}{paragraph(content, 'TableText')}</w:tc>")
        elif t.type == "tr_close":
            head = "<w:trPr><w:tblHeader/></w:trPr>" if header else ""
            rows.append(f"<w:tr>{head}{''.join(cells)}</w:tr>")
            cells = []
        i += 1
    xml = (
        '<w:tbl><w:tblPr><w:tblStyle w:val="TableGrid"/>'
        '<w:tblW w:w="5000" w:type="pct"/></w:tblPr>' + "".join(rows) + "</w:tbl>"
        + paragraph("")
    )
    return xml, i + 1


def render_body(tokens):
    """Return (body xml, number of numbered lists)."""
    out = []
    lists = []          # stack of numIds; 1 is the bullet list
    first_in_item = []  # stack: is the next paragraph the first of its item?
    quote = 0
    ordered_count = 0
    after_title = False
    i = 0
    while i < len(tokens):
        t = tokens[i]
        kind = t.type
        if kind == "heading_open":
            if t.tag not in HEADING_STYLE:
                raise SystemExit(f"build_docx: heading level {t.tag} is not supported")
            out.append(paragraph(runs(tokens[i + 1]), HEADING_STYLE[t.tag]))
            after_title = t.tag == "h1"
            i += 3
            continue
        if kind == "paragraph_open":
            inline = tokens[i + 1]
            if lists:
                level = len(lists) - 1
                if first_in_item[-1]:
                    out.append(paragraph(runs(inline), "ListParagraph", (level, lists[-1])))
                    first_in_item[-1] = False
                else:
                    out.append(paragraph(runs(inline), "ListParagraph", indent=720 * (level + 1)))
            elif quote:
                out.append(paragraph(runs(inline), "Quote"))
            elif after_title and all_italic(inline):
                inline.children = inline.children[1:-1]
                out.append(paragraph(runs(inline), "Subtitle"))
            else:
                out.append(paragraph(runs(inline)))
            after_title = False
            i += 3
            continue
        after_title = False
        if kind == "bullet_list_open":
            lists.append(1)
        elif kind == "ordered_list_open":
            ordered_count += 1
            lists.append(1 + ordered_count)
        elif kind in ("bullet_list_close", "ordered_list_close"):
            lists.pop()
        elif kind == "list_item_open":
            first_in_item.append(True)
        elif kind == "list_item_close":
            first_in_item.pop()
        elif kind == "blockquote_open":
            quote += 1
        elif kind == "blockquote_close":
            quote -= 1
        elif kind == "table_open":
            xml, i = table(tokens, i)
            out.append(xml)
            continue
        elif kind == "hr":
            out.append(paragraph("", "Rule"))
        else:
            raise SystemExit(f"build_docx: unsupported block element '{kind}'")
        i += 1
    return "".join(out), ordered_count


# --------------------------------------------------------------------------
# 3. The fixed parts of the package
# --------------------------------------------------------------------------
CONTENT_TYPES = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
    '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
    '<Default Extension="xml" ContentType="application/xml"/>'
    '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
    '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
    '<Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>'
    '<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>'
    "</Types>"
)

PACKAGE_RELS = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    f'<Relationship Id="rId1" Type="{R_NS}/officeDocument" Target="word/document.xml"/>'
    "</Relationships>"
)

DOCUMENT_RELS = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    f'<Relationship Id="rId1" Type="{R_NS}/styles" Target="styles.xml"/>'
    f'<Relationship Id="rId2" Type="{R_NS}/numbering" Target="numbering.xml"/>'
    f'<Relationship Id="rId3" Type="{R_NS}/footer" Target="footer1.xml"/>'
    "</Relationships>"
)

FOOTER = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    f'<w:ftr xmlns:w="{W_NS}"><w:p><w:pPr><w:jc w:val="center"/></w:pPr>'
    '<w:r><w:fldChar w:fldCharType="begin"/></w:r>'
    '<w:r><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>'
    '<w:r><w:fldChar w:fldCharType="end"/></w:r></w:p></w:ftr>'
)


def style(style_id, name, ppr="", rpr="", based_on="Normal", kind="paragraph", next_style="Normal"):
    based = f'<w:basedOn w:val="{based_on}"/>' if based_on else ""
    nxt = f'<w:next w:val="{next_style}"/>' if kind == "paragraph" else ""
    return (
        f'<w:style w:type="{kind}" w:styleId="{style_id}"><w:name w:val="{name}"/>{based}{nxt}<w:qFormat/>'
        + (f"<w:pPr>{ppr}</w:pPr>" if ppr else "")
        + (f"<w:rPr>{rpr}</w:rPr>" if rpr else "")
        + "</w:style>"
    )


def heading_fonts(size, colour="1F2A33"):
    return (
        f'<w:rFonts w:ascii="{HEAD_FONT}" w:hAnsi="{HEAD_FONT}" w:cs="{HEAD_FONT}"/>'
        f'<w:b/><w:color w:val="{colour}"/><w:sz w:val="{size}"/><w:szCs w:val="{size}"/>'
    )


def styles_xml():
    border = '<w:{0} w:val="single" w:sz="4" w:space="0" w:color="999999"/>'
    parts = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        f'<w:styles xmlns:w="{W_NS}">',
        "<w:docDefaults><w:rPrDefault><w:rPr>",
        f'<w:rFonts w:ascii="{BODY_FONT}" w:hAnsi="{BODY_FONT}" w:cs="{BODY_FONT}" w:eastAsia="{BODY_FONT}"/>',
        '<w:sz w:val="23"/><w:szCs w:val="23"/><w:lang w:val="el-GR" w:eastAsia="el-GR" w:bidi="ar-SA"/>',
        "</w:rPr></w:rPrDefault><w:pPrDefault><w:pPr>",
        '<w:spacing w:after="160" w:line="288" w:lineRule="auto"/>',
        "</w:pPr></w:pPrDefault></w:docDefaults>",
        '<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/></w:style>',
        style("Title", "Title", '<w:spacing w:before="0" w:after="120"/>', heading_fonts(48)),
        style("Subtitle", "Subtitle", '<w:spacing w:after="480"/>',
              '<w:i/><w:color w:val="555555"/><w:sz w:val="26"/><w:szCs w:val="26"/>'),
        style("Heading1", "heading 1",
              '<w:keepNext/><w:spacing w:before="480" w:after="160"/><w:outlineLvl w:val="0"/>',
              heading_fonts(32)),
        style("Heading2", "heading 2",
              '<w:keepNext/><w:spacing w:before="320" w:after="120"/><w:outlineLvl w:val="1"/>',
              heading_fonts(26)),
        style("Heading3", "heading 3",
              '<w:keepNext/><w:spacing w:before="240" w:after="80"/><w:outlineLvl w:val="2"/>',
              heading_fonts(23, "444444")),
        style("ListParagraph", "List Paragraph", '<w:spacing w:after="100"/>'),
        style("Quote", "Quote",
              '<w:pBdr><w:left w:val="single" w:sz="18" w:space="12" w:color="999999"/></w:pBdr>'
              '<w:ind w:left="567" w:right="284"/>',
              '<w:color w:val="333333"/>'),
        style("TableText", "Table Text", '<w:spacing w:before="40" w:after="40" w:line="252" w:lineRule="auto"/>',
              '<w:sz w:val="20"/><w:szCs w:val="20"/>'),
        style("Rule", "Rule",
              '<w:pBdr><w:bottom w:val="single" w:sz="6" w:space="1" w:color="999999"/></w:pBdr>'
              '<w:spacing w:before="240" w:after="240"/>'),
        '<w:style w:type="table" w:styleId="TableGrid"><w:name w:val="Table Grid"/><w:tblPr><w:tblBorders>',
        "".join(border.format(side) for side in ("top", "left", "bottom", "right", "insideH", "insideV")),
        '</w:tblBorders><w:tblCellMar><w:left w:w="100" w:type="dxa"/><w:right w:w="100" w:type="dxa"/>',
        "</w:tblCellMar></w:tblPr></w:style>",
        "</w:styles>",
    ]
    return "".join(parts)


def numbering_xml(ordered_count):
    def levels(numbered):
        out = []
        for lvl in range(4):
            left = 720 * (lvl + 1)
            if numbered:
                fmt, text, font = ("decimal", f"%{lvl + 1}.", "")
            else:
                glyph = "•" if lvl == 0 else "–"
                fmt, text = "bullet", glyph
                font = f'<w:rPr><w:rFonts w:ascii="{BODY_FONT}" w:hAnsi="{BODY_FONT}" w:hint="default"/></w:rPr>'
            out.append(
                f'<w:lvl w:ilvl="{lvl}"><w:start w:val="1"/><w:numFmt w:val="{fmt}"/>'
                f'<w:lvlText w:val="{text}"/><w:lvlJc w:val="left"/>'
                f'<w:pPr><w:ind w:left="{left}" w:hanging="360"/></w:pPr>{font}</w:lvl>'
            )
        return "".join(out)

    parts = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        f'<w:numbering xmlns:w="{W_NS}">',
        f'<w:abstractNum w:abstractNumId="0"><w:multiLevelType w:val="hybridMultilevel"/>{levels(False)}</w:abstractNum>',
        f'<w:abstractNum w:abstractNumId="1"><w:multiLevelType w:val="hybridMultilevel"/>{levels(True)}</w:abstractNum>',
        '<w:num w:numId="1"><w:abstractNumId w:val="0"/></w:num>',
    ]
    for n in range(ordered_count):  # one <w:num> per numbered list, so each restarts at 1
        overrides = "".join(
            f'<w:lvlOverride w:ilvl="{lvl}"><w:startOverride w:val="1"/></w:lvlOverride>' for lvl in range(4)
        )
        parts.append(f'<w:num w:numId="{n + 2}"><w:abstractNumId w:val="1"/>{overrides}</w:num>')
    parts.append("</w:numbering>")
    return "".join(parts)


def document_xml(body):
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        f'<w:document xmlns:w="{W_NS}" xmlns:r="{R_NS}"><w:body>{body}'
        '<w:sectPr><w:footerReference w:type="default" r:id="rId3"/>'
        '<w:pgSz w:w="11906" w:h="16838"/>'
        '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="708" w:footer="708" w:gutter="0"/>'
        "</w:sectPr></w:body></w:document>"
    )


# --------------------------------------------------------------------------
# 4. Build
# --------------------------------------------------------------------------
def build():
    """Return the bytes of the .docx. The output is the same on every run."""
    md = MarkdownIt("commonmark").enable("table")
    tokens = md.parse(MD_PATH.read_text(encoding="utf-8"))
    body, ordered_count = render_body(tokens)
    files = [
        ("[Content_Types].xml", CONTENT_TYPES),
        ("_rels/.rels", PACKAGE_RELS),
        ("word/document.xml", document_xml(body)),
        ("word/_rels/document.xml.rels", DOCUMENT_RELS),
        ("word/styles.xml", styles_xml()),
        ("word/numbering.xml", numbering_xml(ordered_count)),
        ("word/footer1.xml", FOOTER),
    ]
    buffer = BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as z:
        for name, text in files:
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))  # fixed date: stable bytes
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, text.encode("utf-8"))
    return buffer.getvalue()


def main():
    data = build()
    if "--check" in sys.argv:
        if not DOCX_PATH.exists() or DOCX_PATH.read_bytes() != data:
            print(f"OUT OF DATE: {DOCX_PATH.name} does not match {MD_PATH.name}")
            sys.exit(1)
        print(f"up to date: {DOCX_PATH.name}")
        return
    DOCX_PATH.write_bytes(data)
    print(f"wrote {DOCX_PATH.name} ({len(data):,} bytes)")


if __name__ == "__main__":
    main()
