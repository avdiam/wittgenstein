# Instructions for agents

The instructions for this repository are in [`CLAUDE.md`](CLAUDE.md). They apply
to any agent or tool working here, not only to Claude. Read that file first,
then `README.md` and `CROSSCHECK_PLAN.md`.

In short:

- Edit the analysis only in the Markdown file; the HTML is rebuilt from it with
  `python tools/build_html.py` and verified with `python tools/build_html.py --check`.
- Never edit between the `FULL-ANALYSIS` markers in the HTML.
- Content in Greek, conversation in English.
- The HTML uses CRLF line endings, the Markdown LF.
