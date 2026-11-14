# Wittgenstein study folder — instructions for agents

Greek-language study material on Wittgenstein's *Tractatus Logico-Philosophicus*.
Read `README.md` first (layout and workflow), then `CROSSCHECK_PLAN.md` (what has
been verified against outside sources, and the list of open items at its end).
`TODO.md` lists the work the owner has planned for future sessions.

## Roles of the files

- `Tractatus Logico-Philosophicus/TRACTATUS_LOGICO_PHILOSOPHICUS_ANALYSIS_1-7.md`
  is the single source of truth. Change the analysis there and nowhere else.
- `docs/tractatus.html` is the human UI. The full analysis inside it is
  generated; the summaries, the tree-explorer data, the labs and the
  philosophers grid are hand-written.
- `docs/` is published as is by GitHub Pages at https://avdiam.github.io/wittgenstein/.
  `docs/index.html` (the cover page) is hand-written.

- `Logiki_Glossa_Michanes.md` is the source of the essay on the history of
  logic. `docs/essay.html` (built by `tools/build_essay_html.py`) and
  `docs/Logiki_Glossa_Michanes.docx` (built by `tools/build_docx.py`) are
  generated from it in full: never edit them by hand. Each `##` section of the
  essay goes to a tab of the page, as mapped in `tab_for()`. The rules below on
  sources, disagreements and tone apply to the essay too. It is written for
  general readers, not for IT or mathematics people. Names are written in
  Latin script, with the Greek form at the first mention of the main figures.
  The first version (`Istoria_Logikis_kai_AI.docx`) was deleted on 2026-11-14;
  it is in git history (`git show 4e50b45:Istoria_Logikis_kai_AI.docx`).

## Workflow

1. Edit the Markdown.
2. `python tools/build_all.py` (needs `markdown-it-py`); it runs the three builds.
3. `python tools/build_all.py --check` must exit 0.
4. Check whether a hand-written HTML passage repeats the fact you changed.
5. Commit the Markdown and the generated files together, one commit per stage
   of work. Pushing to `main` publishes the site: push only when the owner asks.

## Rules

- Never edit between `<!-- FULL-ANALYSIS:BEGIN … -->` and
  `<!-- FULL-ANALYSIS:END … -->` in the HTML; the build overwrites it.
- Leave the hand-written HTML parts hand-written. Change them only where they
  contradict the Markdown or are philosophically inaccurate.
- Every `##` heading must be mapped: in `target_for()` (`tools/build_html.py`)
  for the analysis, in `tab_for()` (`tools/build_essay_html.py`) for the essay.
  The builds stop on an unmapped heading.
- The repository is public. Do not add material under copyright (such as
  Klement's PDF, which contains the Pears/McGuinness translation; it is kept
  local and git-ignored), and commit with the GitHub noreply address set in
  this repository's git config.
- Quotations of the *Tractatus* are checked against the three PDFs in the folder.
  A claim taken from secondary literature needs a source: record it in
  `CROSSCHECK_PLAN.md` with a verdict.
- Where respectable sources disagree, do not pick a winner. Add an
  «Ερμηνευτική σημείωση» that names both readings.
- Keep the tone sober: no exclamation marks, no superlatives, and the numbered
  remarks are "propositions", not "axioms".

## Editing conventions

- Content is written in Greek; conversation with the user is in English.
- Edit the Greek Markdown through a Python script saved to a file, using
  replacements that must match exactly once and abort otherwise. Shell heredocs
  mangle backslashes and quotation marks in this text.
- Line endings: `docs/tractatus.html` is CRLF; the Markdown, `docs/essay.html`
  and `docs/index.html` are LF. Read and write bytes, or preserve the endings
  explicitly. `.gitattributes` disables conversion.
- German quotations keep the original spelling of the 1921/1922 text where it
  matters for the argument (for example *transcendental*).
- In the HTML, text is often split by tags such as `<strong>`, so search the raw
  markup before assuming a phrase is absent.
- The page's design tokens, and what each colour and typeface is for, are
  described at the top of the first `<style>` block in the HTML. The styles of
  the generated blocks are in `HEAD_BLOCK` in `tools/build_html.py`. The essay
  page (`CSS` in `tools/build_essay_html.py`) and the cover page repeat the
  same tokens and share the theme setting (`hw-tlp-theme`). Use the tokens
  (`var(--primary)` and so on) and do not hard-code colours.

## Verification tools

- Pages in a background Chrome window may not produce frames for screenshots.
  Headless Chrome (`chrome --headless=new --screenshot=... --window-size=W,H URL`)
  works; check widths under about 500 px inside an `iframe`, since Chrome
  windows have a minimum width.
- `pdftotext -layout` regenerates text extracts of the PDFs (figures are lost;
  the three-column Klement layout breaks sentences across lines).
- The Ludwig Wittgenstein Project hosts the German text and the original
  figures: https://www.wittgensteinproject.org/w/index.php/Logisch-philosophische_Abhandlung
- Expected counts: 526 propositions; per section 7 / 79 / 74 / 109 / 151 / 105 / 1.
