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
  (details in `DONE.md`); committed, not pushed.

## Next session

**Start with the essay, not with the third part** (owner, 2026-11-18).

1. The owner is checking the essay passage by passage (2026-11-19:
   sections 5, 8, 12 done, and the Gemini review taken through;
   `DONE.md`). Continue if the owner has more. Until the essay checks
   are finished, do not read or start anything for the *Investigations*
   part (`Philosophical Investigations/`, `RESEARCH_NOTES.md`, the OCR
   files).

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
