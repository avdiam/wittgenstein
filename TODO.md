# To-do for future sessions

Noted by the owner on 2026-11-14. Items 1, 2 and 3 were done on 2026-11-14 and await
the owner's review. Items are recorded as requested;
the two readings that were open were confirmed by the owner on 2026-11-14.
More items are expected to be added.

**Where to resume (status after the second session of 2026-11-15):**

- Item 4.3 done: the essay was scanned as a whole and ten proposals were
  applied one at a time with the owner's approval (details under item 4).
  The commits from `500b5ed` to `19e149a` are **local only, not pushed**:
  the live site does not show them until the owner asks for a push.
- Not yet checked: the new figures in print (PDF) and in the Word file
  opened in Word; the essay page at 1280 px with the new figures in place.

**Status at the end of the first session of 2026-11-15:**

- Everything was committed and pushed; the live site matched `main` (last
  commit `42c338d`).
- Done on 2026-11-15: the visual check of the essay's figures and its fixes,
  figures in the Word file, the new Jacquard photo with corrected photo
  licences, the light theme by default, justified essay text on phones, and
  the essay card first on the cover page (details under items 2c and 4).
- The owner checked the site on a phone and in Firefox and found it in order.
- **Next session:** item 4.3, making the essay shorter and clearer, section
  by section with the owner's approval before each change.
- Waiting on the owner: whether Greek words are hyphenated in the justified
  text on their phone (if not, some lines show wide gaps; other settings
  can be tried).
- Still open: the print-only items in `CROSSCHECK_PLAN.md` ("Open for the
  essay", and C1/C3 under "Carried over from the cross-check" below).

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

### 2c. Paragraph-by-paragraph review, modern AI, figures and typography — done 2026-11-14, awaiting the owner's review

Reviewed `Logiki_Glossa_Michanes.md` section by section with the owner and added:

- **Intro & Section 1 (Ancient Logic):** Clarified decimal numbering vs. `§` references to *Philosophical Investigations*; linked Plato's *Cratylus* to *Tractatus* 3.342; named the Eleatic Stranger in the *Sophist*; added the letters-and-syllables analogy in the *Theaetetus*; added Aristotle's *Organon*, synthesis/division examples, general-term syllogism, letter-variables (Α, Β, Γ) in *Prior Analytics*, precursor to predicate logic, and the original Greek of the principle of non-contradiction; named propositional logic for the Stoics, added Diodorus Cronus & Callimachus's epigram, ordinal variables, and the Stoic semiotic triangle (*σημαίνον / σημαινόμενον–λεκτόν / τυγχάνον*).
- **Section 2 (Middle Ages to Leibniz):** Added Porphyry's *Isagoge* question on universals; added **al-Khwārizmī** (c. 780–850, origin of *algebra* and *algorithm*); dated al-Fārābī (c. 870–950); added Avicenna example and Byzantine *Posterior Analytics* commentaries; clarified realism vs. nominalism and Abelard's *sermones*; linked Ockham's mental language to 20th-century philosophy of mind and added the `=` example for *Tractatus* 3.328; added Leibniz's 1679 prime-number encoding of concepts (`2 × 3 = 6`).
- **Section 3 (Epistemology):** Added *tabula rasa*, Frege's critique of Locke's mentalism, Hume's problem of induction (*Tractatus* 5.1361 and link to statistical ML in section 11), Kant's forms of sensibility (*Tractatus* 6.36111), and two new paragraphs on 19th- and 20th-century epistemology (**Hegel**, **Comte**, **Mill** 1843, **Peirce, James & Dewey** on pragmatism, **Nietzsche** on perspectivism, **Husserl** on phenomenology, **Foucault** on power/knowledge, **Russell & Moore**, and **Gettier** 1963).
- **Section 4 (Babbage, Lovelace, Boole):** Explained **Jacquard's** 1801 punched-card loom and Babbage's conditional branching; named Luigi Menabrea; added everyday De Morgan example; noted Boole's propositional interpretation; corrected Shannon's publication year from 1937 to 1938.
- **Section 5 (Frege, Russell):** Explained Frege's replacement of subject/predicate with function/argument; added quantifier scope readings («Όλοι αγαπούν κάποιον»); contrasted Frege with Kant on arithmetic; added a 3-row visual walk-through of Cantor's diagonal argument; noted Frege's anti-psychologism on *Sinn*; added `p → q` alongside `p ⊃ q`; added non-cat set example and a clearer formulation of the Grelling–Nelson autological/heterological paradox; noted the axiom of infinity in *Principia* and Meinong in Russell's theory of descriptions.
- **Section 6 (Early Wittgenstein):** Added Manchester aeronautical engineering, explanation of the decimal tree structure, propositions 1 and 1.1, the 1914 Paris courtroom notebook entry and 4.014 musical score/gramophone analogy, contradiction and the `0` in arithmetic analogy (4.4611), the mold/slot analogy for `F(F)` in 3.333, musical notes & visual field (5.633) examples for showing vs. saying, the third («διαφωτιστική», McGinn/Hutto) reading of 6.54, Wittgenstein's disagreement with Russell's introduction, Ramsey's age, Gödel's attendance at the Vienna Circle, and **Karl Popper** (*Logik der Forschung* 1934/1935, falsifiability).
- **Sections 7–9 (Gödel, Turing, Shannon):** Added chess analogy for Hilbert's formalism and link to Leibniz's prime encoding; added `(αλγόριθμος)` glosses, Church's lambda calculus, encoding of instruction tables as numbers, **Bletchley Park / Enigma (*Bombes*)** and **ACE (1945)**, why truth tables do not decide quantification over infinite domains, **P vs. NP** (Cook 1971, Levin 1973, SAT / truth tables), and Wittgenstein's reply to Turing on the falling bridge; added Shannon's 1948 information theory, *bit*, and logic gates.
- **Section 10 (Later Wittgenstein):** Added the builders' language-game (§2) and a paragraph on **rule-following** (§§185, 199–202); added **Gilbert Ryle** (*The Concept of Mind* 1949, «το δόγμα του φαντάσματος μέσα στη μηχανή»); added **Lev Vygotsky** (*Thought and Language* 1934, social constructivism) and **Jean Piaget** (genetic epistemology); added **W. V. O. Quine** («Two Dogmas» 1951, «Epistemology Naturalized» 1969); linked Fodor to Ockham; cited *Tractatus* 5.6–5.64 on solipsism and `(§124)` for Marcuse.
- **Section 11 (AI):** Added Wittgensteinian parallel to the imitation game, `(Ned Block, 1981)`, **Cognitivism / Jerome Bruner / Miller / Chomsky** in the 1950s cognitive revolution, Logic Theorist's shorter proof in *Principia*, **Moravec's paradox**, word embeddings as points in multidimensional space, **AlphaGo (2016)**, **AlphaFold (2020, Nobel Prize in Chemistry 2024)**, **Transformer & attention mechanism (Vaswani et al. 2017)**, 3-stage training of LLMs, and **2024–2026 breakthroughs in mathematics and physics** (**AlphaGeometry**, **AlphaProof** with formal verification in **Lean**, IMO 2024 silver & IMO 2025 gold, open **Erdős** problems and fluid dynamics / particle physics with Terence Tao et al.).
- **Figures (`docs/images/`) and Typography (`docs/essay.html`):**
  - Added 11 figures to `Logiki_Glossa_Michanes.md` and `docs/images/`: 4 public-domain/CC historical images from Wikimedia Commons (`leibniz_reckoner.jpg`, `jacquard_cards.jpg`, `babbage_analytical.jpg`, `lovelace_note_g.jpg`) and 7 custom Greek SVG schematic diagrams (`frege_begriffsschrift.svg`, `cantor_diagonal.svg`, `stoic_frege_triangle.svg`, `tractatus_picture.svg`, `turing_machine.svg`, `shannon_switches.svg`, `attention_neurosymbolic.svg`).
  - Updated `tools/build_essay_html.py` to inline `.svg` diagrams into `<figure>` (inheriting fonts and light/dark CSS tokens) and wrap raster photos in `<figure>`, and enabled full justification with automatic Greek hyphenation (`text-align: justify; hyphens: auto`) on screens wider than `720px`.
  - Updated `tools/build_docx.py` to output italic `[Εικόνα: ...]` caption lines for figures.
  - Updated Timeline (57 entries), Glossary (36 terms), Sources, and `CROSSCHECK_PLAN.md`.

**Visual check — done 2026-11-15** (headless Chrome, light and dark, 1280 px and
390 px frames, print to PDF):

- The 4 photos and the Cantor diagram were fine.
- Fixed: text overflowing its boxes, or overlapping other text, in 6 of the 7 SVG
  diagrams (Frege, Stoic triangle, Tractatus, Turing, Shannon, attention). The
  SVGs take the page's fonts when inlined, and those are wider than the ones the
  boxes were sized for. The Tractatus nodes got opaque underlays so the lines no
  longer show through the labels.
- Fixed: with the dark theme on, figures printed as dark boxes. The dark tokens
  now apply on screen only (`@media screen`), so print always uses the light ones.
- Added at the owner's request: on phones the diagrams were too small to read
  (text about 4–5 px). A tap (or Enter / Space) now opens the diagram in a dialog
  at its design width, scrolling sideways; a «Πατήστε για μεγέθυνση» hint shows
  under each diagram on screens up to 720 px, never in print.
- Restored the CRLF line endings of `tools/build_essay_html.py` (they had been
  converted to LF, which inflated its diff to every line).

**Figures in the Word file — decided by the owner and done 2026-11-15:** the
`.docx` contains the 11 figures with their captions (centred, the picture kept
on the page of its caption). Photos are embedded as they are; the diagrams as
PNG copies made by `tools/render_figures.py` (headless Chrome, light theme,
the page's typefaces, 1520 px wide). Opened in Word and LibreOffice: all 11
pictures shown. The file grew from 71 KB to 2.3 MB, mostly the photos. The
Jacquard photo (249 × 333 px, soft in print) was replaced at the owner's
request by a 960 × 1280 photo of a hand-driven Jacquard loom (Sliven,
Edal Anton Lefterov, CC BY-SA 3.0). Checking the photo credits found two
wrong licences, now corrected (see "Figure credits of the essay" in
`CROSSCHECK_PLAN.md`).

**Checked by the owner on 2026-11-15:** the site on a phone and in Firefox.

**What needs checking next:**
1. Check the remaining print-only items under "Open for the essay" in `CROSSCHECK_PLAN.md`.

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

## 4. Owner's requests of 2026-11-15

As requested:

1. Light theme by default, not dark.
2. On phones the essay should be justified («πλήρης στοίχηση»), as it is in
   Chrome and Firefox on a computer.
3. In a next session: check the content of the essay and see whether any
   chapter or paragraph should be made shorter and clearer («πιο σύντομη και
   περιεκτική»).
4. On the cover page, the essay on the left and the Tractatus on the right.

Done on 2026-11-15:

- 1: all three pages open in the light theme unless the reader has chosen
  dark with the theme button (the choice is still kept in `hw-tlp-theme`).
  The system's dark setting is no longer followed.
- 2: the essay is justified at every width, with automatic hyphenation and
  at least 3 letters on each side of a break (`hyphenate-limit-chars`).
  Whether Greek words are hyphenated depends on the browser's dictionaries
  (Firefox has Greek). Where they are not, narrow columns can show wider
  gaps between words.
- 4: the essay card comes first: left on wide screens, on top on phones.

Done on 2026-11-15 (second session), item 3: at the owner's request the
whole essay was scanned first, then ten proposals were presented one at a
time and applied after approval. Each change is recorded in
`CROSSCHECK_PLAN.md` ("Review for length and clarity").

1. Corrections: «γνωστικισμός» (Gnosticism) → «γνωσιακή ψυχολογία»; the
   stopped clock credited to Russell (1948), not Gettier; Lean no longer a
   "direct descendant" of Hilbert's programme; Kant's causality as a category.
2. §3: 19th–20th c. epistemology shortened (Hegel, Comte, Nietzsche,
   Foucault cut; Hegel's dates moved to §10).
3. §10: influence list rewritten (Piaget and Quine 1969 cut; Vygotsky as a
   parallel idea; five shorter bullets).
4. §6: items A–J (Moore, Spinoza's *Ethics*, Paris court model, truth-table
   history, F(F(x)), 1916 notebook, Russell–Ramsey, linguistic turn,
   Vienna Circle, Popper).
5. §5: non-cat set reworded; heterological paradox shortened.
6. §11: cognitivism, Deep Blue/AlphaGo/AlphaFold and mathematics shortened;
   added at the owner's request, with sources: the Lean proof of Fermat's
   Last Theorem (Sep 2026), the Fable 5.2 30-hour run and two physics
   results as reported by Anthropic, the Aaronson–Ambainis proof (Nov 2026).
   Claims without a primary source (a train-timetabling result) left out.
7. §8, §10: Turing's war work, Moore's report, Sraffa anecdote shorter.
8. §2, §4: two long paragraphs split.
9. Four new diagrams: Euler circles (§1), Venn for Boole (§4), the halting
   proof (§8), family resemblances (§10).
10. Portrait of Wittgenstein by Moritz Nähr, 1930 (§6).

Not proposed: splitting a section (would renumber §9–§12 and every
cross-reference). The essay body is now about 17,600 words (was 17,900;
the cuts removed about 900, the 2026 results and figure captions added some).

## Carried over from the cross-check

See "Still open after this pass" at the end of `CROSSCHECK_PLAN.md`: C1 and C3
need printed books (or access to the University of Macedonia scan of the
Kitsopoulos translation).
