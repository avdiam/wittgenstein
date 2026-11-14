# To-do for future sessions

Noted by the owner on 2026-11-14. Items 1 and 2 were done on 2026-11-14 and await
the owner's review. Items are recorded as requested;
the two readings that were open were confirmed by the owner on 2026-11-14.
More items are expected to be added.

## 1. Enhance the HTML page — done 2026-11-14, awaiting the owner's review

`Tractatus Logico-Philosophicus/TRACTATUS_LOGICO_PHILOSOPHICUS_INTERACTIVE_V2.html`

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
3,200 to about 11,000 words (27 pages). The sources and verdicts are in
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

For the owner to decide:

- The title and the file names.
- Whether to delete `Istoria_Logikis_kai_AI.docx` once the new text is accepted.
- Names are written in Latin script with the Greek form at first mention; the
  first version used Greek forms more often.
- Proposals for further content, within the audience limit: (1) a one-page
  timeline; (2) a short glossary of the dozen terms the text explains;
  (3) Spinoza, Moore and Mauthner, who are in the Tractatus analysis but
  hardly in the essay; (4) women in this history beyond Anscombe, Robinson
  and Masterman, for example Ada Lovelace and Susan Stebbing; (5) the Turing
  test (1950) and Searle's Chinese room, which bear directly on whether a
  machine that uses words understands them; (6) Arabic and Byzantine logic
  between the Stoics and Abelard, a gap of a thousand years in the text.
- Weakly sourced points are listed under "Open for the essay" in
  `CROSSCHECK_PLAN.md`.

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

## Carried over from the cross-check

See "Still open after this pass" at the end of `CROSSCHECK_PLAN.md`: C1 and C3
need printed books (or access to the University of Macedonia scan of the
Kitsopoulos translation).
