# Wittgenstein — study folder

Greek-language study material on the history of logic and on Wittgenstein's
*Tractatus Logico-Philosophicus*.

## Layout

| Path | Role |
| :-- | :-- |
| `Istoria_Logikis_kai_AI.docx` | Essay: from Aristotle and the Stoics to AI. |
| `Tractatus Logico-Philosophicus/TRACTATUS_LOGICO_PHILOSOPHICUS_ANALYSIS_1-7.md` | **Source of truth** for the analysis text. Edit this. |
| `Tractatus Logico-Philosophicus/TRACTATUS_LOGICO_PHILOSOPHICUS_INTERACTIVE_V2.html` | Human UI. Contains hand-written summaries and labs plus the full analysis, generated from the Markdown. |
| `Tractatus Logico-Philosophicus/*.pdf` | The three source editions used for grounding (Klement side-by-side, Stern tree view, Gutenberg #5740). |
| `tools/build_html.py` | Renders the Markdown into the HTML. |
| `CROSSCHECK_PLAN.md` | What still needs checking against outside sources. |

## Workflow (for people and agents)

1. Change the analysis in the **Markdown** file only.
2. Rebuild the page: `python tools/build_html.py` (needs `pip install markdown-it-py`).
3. Verify they are in sync: `python tools/build_html.py --check` (exit code 1 if stale).
4. Commit both files together.

Rules:

- Never edit anything between `<!-- FULL-ANALYSIS:BEGIN … -->` and
  `<!-- FULL-ANALYSIS:END … -->` in the HTML; the build overwrites it.
- Everything else in the HTML (section summaries, the tree explorer data, the
  labs, the philosophers grid) is hand-written and is **not** regenerated. If a
  fact changes in the Markdown, check whether a summary or a data entry repeats it.
- Every `##` heading of the Markdown must be mapped to an HTML section in
  `target_for()` inside `tools/build_html.py`; the build stops if one is not.
- Quotations of the *Tractatus* must be checked against the PDFs. Claims that come
  from secondary literature are listed in `CROSSCHECK_PLAN.md` until verified.

The page loads KaTeX, Tailwind and web fonts from CDNs, so formulas and layout
need a network connection the first time it is opened.
