# To-do

Only pending work. Finished work, with its details, is in [`DONE.md`](DONE.md);
open source checks are in [`CROSSCHECK_PLAN.md`](CROSSCHECK_PLAN.md). When an
item is finished, move it to `DONE.md` with the date.

## Status

- Session of 2026-11-18, later (details in `DONE.md`): an outside
  critique of the essay checked proposal by proposal with the owner;
  the essay changes are pushed (`14ca169..bbdbe37`). The critique file
  was then deleted; it was never committed.
- Session of 2026-11-19: the whole essay read for coherence and the
  owner's decisions applied, and the essay title centred over the
  text column (details in `DONE.md`); pushed (`bbdbe37..3c6e496`).
- Session of 2026-11-19, later: the «μαύρο κουτί» draft checked
  against its sources and corrected (`c074e42`). The owner then
  answered the open question (A: keep the closing paragraph) and
  decided points 1–5 (`92a1c7b`). The subsection, a neural-network
  diagram, the Mark I Perceptron photo, and the owner's checks of
  sections 5, 8 and 12 are in the essay (details in `DONE.md`);
  pushed with this status line.
- Session of 2026-11-19, evening: 3.328 in the analysis aligned with
  the essay's wording, and the Gemini review of the essay taken through
  proposal by proposal (details in `DONE.md`); pushed
  (`df56d9b..fab5fb6`). The `gemini/` folder and
  `drafts/Mavro_Kouti_draft.md` deleted (owner); the draft stays in git
  history (`git show 9eeb189:drafts/Mavro_Kouti_draft.md`).
- Session of 2026-11-19, night: a postscript on self-improvement added to
  section 12 at the owner's request (details in `DONE.md`); pushed
  (`fab5fb6..5e9a3a3`).
- Session of 2026-11-19, night: the Word file and the page justified with
  hyphenation (pushed), and a second Gemini review taken through
  (details in `DONE.md`); pushed (`661db40..a3512af`).
- Session of 2026-11-20: full redesign of `docs/tractatus.html`,
  `tools/build_html.py`, and the analysis Markdown so the Tractatus page
  is 100% mechanically generated without Tailwind CDN, with a single
  analytical view, all 25 main branches, Greek-first presentation, auto-linked
  German key terms, philosopher & Part A concept Quick-Peek drawers, a rebuilt
  «Δενδροειδής μορφή» tree view with sticky filters and KaTeX rendering,
  compact logic/visual labs, and matching flush upper-left collapsible sidebar
  + expanded folded reading width on both `tractatus.html` and `essay.html`
  (details in `DONE.md`; merged into `main`, not yet pushed).
- Session of 2026-11-21: the redesign reviewed before publishing. 4.442
  corrected, 4.12721 and 5.1363 added, six group labels made exact, and a
  coverage check added to the build (details in `DONE.md`; committed,
  not pushed). The rest of the review is listed below.

## Tractatus page: follow-ups to the review of 2026-11-21

Set by the owner on 2026-11-21 for the next session. The redesign stays
unpushed until the owner says otherwise.

1. **Commentary.** The rewrite of 2026-11-20 shortened the commentary
   (Greek words outside the quote cards: Proposition 4 about −38%, 5
   about −37%, 6 about −46%; part of this is old inline translations
   that moved into the cards). Add whatever commentary is needed to make
   the *Tractatus* readable, and restore or extend these six: the
   step-by-step guide to the N operator (5.5–5.52); the net analogy walk-
   through (6.341–6.342); the explanation of the 2 × 2 = 4 proof (6.241);
   Maupertuis and Hamilton on least action (6.321–6.3211); the difference
   between *transzendental* and *transzendent* at 6.13; the diagram of
   Kant's hands (6.36111). The old text is at
   `git show 9375bb0:"Tractatus Logico-Philosophicus/TRACTATUS_LOGICO_PHILOSOPHICUS_ANALYSIS_1-7.md"`.
   For 6.4–6.522, read Wittgenstein's own «Διάλεξη για την Ηθική» (1929)
   first, in the Greek translation on the Ludwig Wittgenstein Project
   (link saved by the owner in `Tractatus Logico-Philosophicus/`,
   untracked) beside the English text already used (ledger, A12). It is
   a primary source for the commentary, not a reading to compare with
   ours (owner, 2026-11-21); it will serve the route from 1929 later.
2. **Greek translations in the 150 quote cards**: check each against the
   German. 4.442 was a paraphrase, so others may be.
3. **Quotations cut short**: check that no card ends before its
   proposition does without a […]. (Omissions in the middle were covered
   by the phrase check of 2026-11-21.)
4. **Ledger**: check that the corrections recorded in
   `CROSSCHECK_DONE.md` for the analysis survived the rewrite.
5. **Visual check**: phone and tablet widths, the dark theme and the
   Quick-Peek drawers (only desktop light was captured on 2026-11-21).
6. **Builder**: extend `tools/build_html.py` to check content too (the
   coverage check is in; candidates: quotations against the Gutenberg
   text, an omission mark where a card is shorter than its proposition).
7. **Outside readings to compare with ours** (four links saved by the owner in
   `Tractatus Logico-Philosophicus/`, untracked):
   <https://wittgenstein.be/en/books/tractatus-logico-philosophicus/>,
   <https://www.sparknotes.com/philosophy/tractatus/>,
   <https://readtractatus.com/>, <https://iep.utm.edu/wittgens/#H2>.
   Differences go to the ledger with a verdict; where good
   sources disagree, an «Ερμηνευτική σημείωση».
8. **`Κιντή_Σκάλα_Tractatus.pdf`** (local, git-ignored): read it and see
   what it gives for the analysis, the ladder (6.54) above all.

## Next session

**Start with the essay, not with the third part** (owner, 2026-11-18).
On 2026-11-21 the owner put the Tractatus follow-ups above on the next
session; the choice below is still open.

1. The owner is checking the essay passage by passage (2026-11-19:
   sections 5, 8, 12 done, and the Gemini review taken through;
   `DONE.md`). Continue if the owner has more. Until the essay checks
   are finished, do not read or start anything for the *Investigations*
   part (`Philosophical Investigations/`, `RESEARCH_NOTES.md`, the OCR
   files).
   At the end of the session of 2026-11-19 the owner left this choice
   for the next session: (A) Claude does the open essay checks that can
   be done online (`CROSSCHECK_PLAN.md`: modern life dates, Tarski and the
   diagonal lemma, Boole's wording); (B) the owner continues the passage
   checks; (C) the essay checks are declared finished and the
   *Investigations* part starts (points 5–6 of §6 in `RESEARCH_NOTES.md`,
   then stage 1).

Then, for the *Investigations* part (no writing of the third part yet;
owner, 2026-11-17):

2. Questions 1–4 of §6 in `RESEARCH_NOTES.md` answered by the owner on
   2026-11-18: arc 1 with the *Blue and Brown Books* at the centre and a
   short account of the route from 1929 (the *Philosophical Grammar*
   named as Rhees's edition); key sentences quoted from the manuscripts
   with page and date, naming the published book; each interpretive
   note in the arc where it belongs; Part II deferred until more sources
   are searched. Still to discuss: points 5 (*Über Gewißheit*) and 6
   (library access).
3. Then settle stage 1.

## Third part: the *Philosophical Investigations*

Decided by the owner on 2026-11-17, after reading the Gemini 4 Argon
proposal (assessed in this session; its errors are in the ledger, "The
Gemini proposal for the *Investigations*, checked"; the file was then
deleted).

- **Scope: a focused companion**, not a twin of the Tractatus page.
  Commentary on about 50–60 central remarks, grouped in thematic arcs;
  Part II as one section, with a note that its status is debated
  (Hacker–Schulte print it as *Philosophy of Psychology – A Fragment*);
  *Über Gewissheit* as a short epilogue; two or three labs at the end.
  Essay §10 and the Tractatus epilogue link to it and are not repeated.
- **Page: generated, like `essay.html`.** One Markdown source,
  `Philosophical Investigations/PHILOSOPHICAL_INVESTIGATIONS_ANALYSIS.md`
  (LF), and a new `tools/build_investigations_html.py` that reuses the
  essay builder's tokens, tabs and search; added to `build_all.py` and
  `--check`. Nothing on the page is hand-written.
- **Quotations: key sentences only.** For each remark, the one or two
  sentences that matter in German (LWP text, §§1–693), with our own Greek
  translation. Christodoulidis (Papazisis 1977) for single terms only, as
  with Kitsopoulos; English only for standard terms ("language-game").
  No whole remarks.

Arcs (from the proposal, kept): 1. introduction: the bridge from the
*Tractatus* (the *Blue and Brown Books*, 1933–35, as the most readable of
the middle-period texts, not the only one; owner, 2026-11-17), the 1945
preface, how to read the book, table of terms; 2. §§1–38 Augustine, builders, language-
games; 3. §§39–64 names, simples, meaning as use; 4. §§65–88 family
resemblances, vagueness; 5. §§89–133 philosophy, *übersichtliche
Darstellung*, therapy; 6. §§138–242 understanding and rule-following
(«Ερμηνευτική σημείωση» on Kripke and his critics); 7. §§243–315 private
language; 8. §§316–693 and Part II xi, thinking, intention, seeing-as;
9. epilogue on *Über Gewissheit*, comparison table, bibliography.

Stages, one commit each:

0. Done 2026-11-17: decisions, ledger rows, open checks, `LICENSE` §3.
1. After the research and the discussion above: skeleton of the
   Markdown, arc 1 (the middle period: *Blue and Brown Books*, and the
   *Big Typescript* and *Philosophical Grammar* as the owner decides
   after the research) and the table of terms against Christodoulidis
   (OCR in `ocr_local/investigations/`, page images).
2. Arcs 2–3. 3. Arcs 4–5. 4. Arcs 6–7. 5. Arc 8 and the epilogue
   (*Über Gewißheit*: LWP text; Part II: printed wording and PPF
   numbers still needed, see `CROSSCHECK_PLAN.md`).
6. Build script, cover card on `docs/index.html`, links from essay §10,
   the Tractatus epilogue and the page headers; `README.md`, `CLAUDE.md`.
7. Labs, two or three, chosen then (candidates: the rule-following
   sequence of §185, the beetle box of §293, the duck-rabbit).

Not published until the owner says so: stages may be committed and kept
local, or pushed with the page not yet linked from the cover.

## For the owner to decide

1. A custom domain name for the site: to be discussed once the
   *Investigations* part is finished (owner, 2026-11-17).

## Needs printed books or library access

See [`CROSSCHECK_PLAN.md`](CROSSCHECK_PLAN.md): C3 (a second
Pears–McGuinness copy) and the weakly sourced points of the essay.
