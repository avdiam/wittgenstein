# Instructions for agents

The instructions for this repository are in [`CLAUDE.md`](CLAUDE.md). They apply
to any agent or tool working here, not only to Claude. Read that file first,
then `README.md`, `TODO.md` (pending work) and `CROSSCHECK_PLAN.md` (open
source checks). `DONE.md` and `CROSSCHECK_DONE.md` hold finished work and the
verdict ledger; open them only to recheck or ground something.

In short:

- Edit text only in the Markdown sources (the analysis and the essay). The
  pages in `docs/` and the Word file are rebuilt with `python tools/build_all.py`
  and verified with `python tools/build_all.py --check`.
- Never edit `docs/essay.html`, nor between the `FULL-ANALYSIS` markers in
  `docs/tractatus.html`.
- The repository is public and `docs/` is published by GitHub Pages.
- Content in Greek, conversation in English.
- `docs/tractatus.html` uses CRLF line endings; everything else LF.
