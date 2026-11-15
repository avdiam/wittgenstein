# Wittgenstein — study folder

Greek-language study material on Wittgenstein's *Tractatus Logico-Philosophicus*
and on the history of logic, language and computing.

**Read it online:** <https://avdiam.github.io/wittgenstein/>

- [Cover page](https://avdiam.github.io/wittgenstein/)
- [Tractatus Logico-Philosophicus: analysis and labs](https://avdiam.github.io/wittgenstein/tractatus.html)
- [Essay: «Λογική, γλώσσα και μηχανές»](https://avdiam.github.io/wittgenstein/essay.html)
  (also as a [Word file](https://avdiam.github.io/wittgenstein/Logiki_Glossa_Michanes.docx))

## How the folder is organised

Sources are Markdown files that people and agents edit. The web pages in
`docs/` are the presentation layer: GitHub Pages publishes that folder as it
is, and scripts in `tools/` regenerate it from the sources.

| Path | Role |
| :-- | :-- |
| `Tractatus Logico-Philosophicus/TRACTATUS_LOGICO_PHILOSOPHICUS_ANALYSIS_1-7.md` | **Source** of the Tractatus analysis. Edit this. |
| `Logiki_Glossa_Michanes.md` | **Source** of the essay. Edit this. |
| `docs/index.html` | Cover page. Hand-written. |
| `docs/tractatus.html` | Tractatus page. The full analysis inside it is generated; the summaries, tree data, labs and philosophers grid are hand-written. |
| `docs/essay.html` | Essay page. **Entirely generated**; never edit by hand. |
| `docs/images/` | Public-domain/CC historical images and Greek SVG diagrams used by `docs/essay.html`. |
| `docs/Logiki_Glossa_Michanes.docx` | The essay as a Word file. Generated. |
| `tools/build_html.py` | Injects the analysis into `docs/tractatus.html`. |
| `tools/build_essay_html.py` | Builds `docs/essay.html`; each `##` section goes to a tab, mapped in `tab_for()`. |
| `tools/build_docx.py` | Builds the Word file. |
| `tools/build_all.py` | Runs the three scripts. |
| `Tractatus Logico-Philosophicus/*.pdf` | Source editions used to check quotations (Gutenberg #5740; Stern's tree view). Klement's edition is used too but is not in the repository: see `LICENSE`. |
| `CROSSCHECK_PLAN.md` | Every claim checked against outside sources, with its source and verdict, and what is still open. |
| `TODO.md` | Work planned and decided by the owner. |
| `CLAUDE.md`, `AGENTS.md` | Instructions and conventions for agents. |

## Workflow

1. Change the text in a **Markdown source** only.
2. Rebuild: `python tools/build_all.py` (needs `pip install markdown-it-py`).
3. Check: `python tools/build_all.py --check` must exit 0.
4. For the Tractatus page, check whether a hand-written passage repeats the fact
   you changed.
5. Commit the source and the generated files together. Pushing to `main`
   publishes the site within a minute or two.

Rules:

- Never edit `docs/essay.html` or the Word file by hand, nor anything between
  `<!-- FULL-ANALYSIS:BEGIN … -->` and `<!-- FULL-ANALYSIS:END … -->` in
  `docs/tractatus.html`; the builds overwrite them.
- Every `##` heading must be mapped: in `target_for()` (`tools/build_html.py`)
  for the analysis, in `tab_for()` (`tools/build_essay_html.py`) for the essay.
  The builds stop on an unmapped heading.
- Quotations of the *Tractatus* are checked against the source editions. Claims
  from secondary literature are recorded in `CROSSCHECK_PLAN.md` with a verdict.
- The essay is for general readers: keep technical terms to a minimum and
  explain each one where it first appears.

To preview the site locally: `python -m http.server -d docs 8000` and open
<http://127.0.0.1:8000/>. The pages load fonts (and the Tractatus page KaTeX and
Tailwind) from CDNs, so they need a network connection the first time.

## Licence

Texts under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), code under
the MIT License. Details, and the status of the source editions, in `LICENSE`.
