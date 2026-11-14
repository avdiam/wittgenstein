# Wittgenstein study folder — instructions for agents

Greek-language study material on Wittgenstein's *Tractatus Logico-Philosophicus*.
Read `README.md` first (layout and workflow), then `CROSSCHECK_PLAN.md` (what has
been verified against outside sources, and the list of open items at its end).

## Roles of the files

- `Tractatus Logico-Philosophicus/TRACTATUS_LOGICO_PHILOSOPHICUS_ANALYSIS_1-7.md`
  is the single source of truth. Change the analysis there and nowhere else.
- `Tractatus Logico-Philosophicus/TRACTATUS_LOGICO_PHILOSOPHICUS_INTERACTIVE_V2.html`
  is the human UI. The full analysis inside it is generated; the summaries, the
  tree-explorer data, the labs and the philosophers grid are hand-written.

## Workflow

1. Edit the Markdown.
2. `python tools/build_html.py` (needs `markdown-it-py`).
3. `python tools/build_html.py --check` must exit 0.
4. Check whether a hand-written HTML passage repeats the fact you changed.
5. Commit the Markdown and the HTML together, one commit per stage of work.

## Rules

- Never edit between `<!-- FULL-ANALYSIS:BEGIN … -->` and
  `<!-- FULL-ANALYSIS:END … -->` in the HTML; the build overwrites it.
- Leave the hand-written HTML parts hand-written. Change them only where they
  contradict the Markdown or are philosophically inaccurate.
- Every `##` heading in the Markdown must be mapped in `target_for()` in
  `tools/build_html.py`; the build stops on an unmapped heading.
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
- Line endings: the HTML is CRLF, the Markdown is LF. Read and write bytes, or
  preserve the endings explicitly. `.gitattributes` disables conversion.
- German quotations keep the original spelling of the 1921/1922 text where it
  matters for the argument (for example *transcendental*).
- In the HTML, text is often split by tags such as `<strong>`, so search the raw
  markup before assuming a phrase is absent.

## Verification tools

- `pdftotext -layout` regenerates text extracts of the PDFs (figures are lost;
  the three-column Klement layout breaks sentences across lines).
- The Ludwig Wittgenstein Project hosts the German text and the original
  figures: https://www.wittgensteinproject.org/w/index.php/Logisch-philosophische_Abhandlung
- Expected counts: 526 propositions; per section 7 / 79 / 74 / 109 / 151 / 105 / 1.
