# To-do for future sessions

Noted by the owner on 2026-11-14. Items 1, 2 and 3 were done on 2026-11-14 and await
the owner's review. Items are recorded as requested;
the two readings that were open were confirmed by the owner on 2026-11-14.
More items are expected to be added.

## 1. Enhance the HTML page — done 2026-11-14, awaiting the owner's review

`docs/tractatus.html` (moved there from `Tractatus Logico-Philosophicus/` on
2026-11-14; see item 3)

As requested:

- Use a plugin to improve the page: aesthetics, colours, user-friendliness.
- Example given: the left pane should be foldable.
- The rules in `CLAUDE.md` still apply: the full analysis between the
  `FULL-ANALYSIS` markers is generated from the Markdown and must not be
  edited by hand.

What was done (plugin chosen by the owner: `frontend-design`):

- New stylesheet, header and contents pane; the text of the summaries, labs,
  tree data and philosophers grid was not changed.
- Colours: cool plaster white and anthracite, one green for whatever "is the
  case" (active item, true cell, Wittgenstein's own text), ochre for the
  dialogue boxes and search hits. Light and dark themes.
- Typefaces that carry Greek: Literata (reading), Commissioner (interface),
  JetBrains Mono (notation and ASCII figures only). The earlier faces had no
  Greek glyphs, so Greek text was drawn in a fallback font.
- The contents pane aligns the numbers on the decimal point and folds to a
  rail of numerals (button in the pane, or the `[` key); the choice is kept in
  the browser. Below 1024px it is a drawer, as before.
- The header is one row on wide screens. The tab labels are shorter; the full
  names are in their tooltips.
- Forced capitals were removed: they dropped Greek accents and changed
  notation in headings (`p` became `P`).
- Removed from the pane: the four "open lab" buttons, which repeated the tabs.
- The styles of the generated blocks live in `tools/build_html.py`.

Left as they are, for the owner to decide:

- Headings typed in capitals in the HTML and the Markdown stay in capitals.
- Done 2026-11-14 at the owner's request: the 78 exclamation marks and the
  emphatic wording in the hand-written HTML were removed (remarks are no
  longer called "axioms"), and Tailwind now loads from
  `cdn.tailwindcss.com/3.4.17`. The Markdown still has a few strong phrases
  (lines 8, 10, 14, 194, 1110) that the HTML no longer repeats.
- Not checked on a real phone or at a real 1920px window: the narrow and wide
  layouts were checked in frames of 400px and 1800px inside a 1280px window.

## 2. Review and extend the essay — done 2026-11-14, awaiting the owner's review

The first version, `Istoria_Logikis_kai_AI.docx`, was read, checked and left
unchanged. The new text is `Logiki_Glossa_Michanes.md` (source) and
`Logiki_Glossa_Michanes.docx` (generated; see `README.md`). It grew from about
3,200 to about 12,500 words (30 pages). The owner's note `Wittgenstein intro.md`
was checked and merged in on the same day (see `CROSSCHECK_PLAN.md`, rows N1–N12). The sources and verdicts are in
`CROSSCHECK_PLAN.md`, section "Results — the essay".

What was asked, and where it is now:

- a. Examples and fuller explanations: the barber, a library catalogue and the
  "heterological" words for Russell's paradox (section 5); the Turing machine
  with a worked example, the universal machine, the halting checker step by
  step, decidable and undecidable problems with examples (section 8).
- c. Philosophers of the Tractatus analysis: Plato, Aristotle (section 1),
  Ockham, Leibniz (2), Hume, Kant (3), Hertz, Schopenhauer (6); Spinoza is
  only named. Moore, Whitehead and Mauthner appear briefly or not at all.
- d. Wider history: philosophy of language from the *Cratylus* to Frege and
  Russell; a section on epistemology (3); added De Morgan, Jevons, Peirce,
  Cantor, Peano, Hilbert, Zermelo, Church, Post, Rosser, Davis, Strachey,
  Matiyasevich, Wang, von Neumann, McCulloch and Pitts, Rosenblatt.
- e. Wittgenstein: why the early work had its effect, the Vienna Circle (6);
  influence of the later work; Marxist and Hegelian readers (10).
- f. Title: «Λογική, γλώσσα και μηχανές: από τον Αριστοτέλη και τους Στωικούς
  στον Wittgenstein και την τεχνητή νοημοσύνη». A working title; the owner
  decides. The file names follow it.
- g. Final check: 23 claims of the first version were checked; 15 were
  corrected (some only in wording), 3 are contested and 5 stand (listed in `CROSSCHECK_PLAN.md`). Proposals
  for further content are below.

Decided by the owner on 2026-11-14:

- Title «Λογική, γλώσσα και μηχανές» with the subtitle above; file names stay.
- `Istoria_Logikis_kai_AI.docx` deleted (recoverable from git, commit 4e50b45).
- `Wittgenstein intro.md` deleted after its content was merged.
- Names in Latin script, Greek form at first mention of the main figures.
- `CLAUDE.md` keeps the paragraph on the essay.
- Add: (1) the Turing test and Searle's Chinese room; (2) a timeline and a
  glossary; (3) the medieval gap: Arabic and Byzantine logic, Babbage and
  Ada Lovelace; (4) Spinoza, Moore and Mauthner.
- Re-check the weakly sourced points ("Open for the essay" in
  `CROSSCHECK_PLAN.md`) at their sources.

Status of the decided work is recorded in the next section.

### 2b. Additions and re-checks — done 2026-11-14

- Added: Boethius, Arabic and Byzantine logic (section 2); Babbage and
  Lovelace (section 4); Spinoza, Moore and Mauthner (sections 6 and 10); the
  Turing test and the Chinese room (section 11); a timeline (46 entries) and a
  glossary (27 terms) after the epilogue. Three new interpretive notes
  (Lovelace as first programmer; the ladder and Mauthner; the Chinese room).
- Re-checked 28 weakly sourced points at their sources: 7 corrected, 1 cut
  (Geertz), the rest confirmed or left as weak and listed in
  `CROSSCHECK_PLAN.md`.
- The essay is now about 15,800 words.

The request as recorded on 2026-11-14:

`Istoria_Logikis_kai_AI.docx` — not reviewed at all so far.

Audience: general readers. It is **not** written for IT or mathematics people,
so keep jargon to a minimum throughout.

a. **More examples and fuller explanations**
   - Add examples of the kind of the barber who shaves himself, for Russell's
     paradox.
   - Explain the Turing machine a bit more.
   - Explain the halting problem in more detail, describing Turing's checker:
     the supposed program that decides whether any other program halts, and
     why it cannot exist.
   - Explain the idea and the proof of decidable versus undecidable problems.

c. **More of the philosophers the Tractatus analysis refers to**
   - Bring into the essay more of them: Leibniz, Ockham, Plato, and others.
   - The analysis names Aristotle, Plato, Leibniz, Spinoza, Hume, Kant,
     Schopenhauer, Frege, Russell, Moore, Whitehead, Mauthner and Hertz.

d. **Wider history**
   - Say more on the connection with, and the history of, the philosophy of
     language and of epistemology (γνωσιολογία).
   - Add any other logician, mathematician or computer scientist who should be
     mentioned.

e. **Tie it more closely to Wittgenstein's work**
   - How and why the early phase had such an effect.
   - How the second phase affected other philosophers and modern thinking.
   - How the Vienna Circle and the positivists saw his work, and how the
     Hegelians / Marxists saw it.

f. **Rename the essay** so the title represents its content better.

g. **Final check and proposals**
   - Check the finished essay and propose what other aspects should be
     included, within the audience limit above.

(The list as given had no item "b"; the letters are kept as given.)

## 3. Web pages and public repository — done 2026-11-14, awaiting the owner's review

As requested: the essay gets the same mechanism as the Tractatus (Markdown as
the back office, an HTML page as the presentation layer, with tabs); a cover
page linking the two pages; everything in a public GitHub repository, with
the pages on GitHub Pages so they can be shared.

Decided by the owner on 2026-11-14:

- Pages in `docs/` (served by GitHub Pages): `index.html` (cover,
  hand-written), `tractatus.html` (moved; its build writes there),
  `essay.html` (entirely generated by `tools/build_essay_html.py`).
- `tlp.pdf` (Klement; contains the copyrighted Pears/McGuinness translation)
  removed from the repository and its history; kept locally, git-ignored.
- History rewritten to the GitHub noreply address
  (93049705+avdiam@users.noreply.github.com); a backup bundle of the old
  history was kept outside the repository.
- Repository `avdiam/wittgenstein`; site https://avdiam.github.io/wittgenstein/.
- Licence: CC BY 4.0 for the texts, MIT for the code (`LICENSE`).

Done:

- Essay page: tabs Κείμενο / Χρονολόγιο / Γλωσσάρι / Πηγές, foldable contents
  pane (`[`), drawer on phones, interpretive notes in the commentary colour,
  links from every «ενότητα N», glossary filter, truth-table colouring,
  print layout, Word download. Same tokens and theme setting as the
  Tractatus page.
- `tools/build_all.py` runs the three builds; `--check` for all.
- The Tractatus page header links to the cover and the essay.
- Checked in Chrome (links, tabs, filter, no console errors) and in headless
  Chrome at 1280 px and in 390 px frames.

Possible next steps, for the owner to decide: split long passages (the
halting proof, the decidability examples) into folding blocks; a search box
on the essay page like the Tractatus one; a custom domain.

## Carried over from the cross-check

See "Still open after this pass" at the end of `CROSSCHECK_PLAN.md`: C1 and C3
need printed books (or access to the University of Macedonia scan of the
Kitsopoulos translation).
