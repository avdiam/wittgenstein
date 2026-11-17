# Cross-check: open items

This file holds only what is still unchecked or weakly sourced. Every claim
already checked, with its source and verdict, is in
[`CROSSCHECK_DONE.md`](CROSSCHECK_DONE.md) (the ledger). New verdict rows go
there; when an item below is settled, record its row in the ledger and
remove it here.

## Open for the analysis

- C3 (a second Pears–McGuinness copy) needs a printed book. (C1 was done on 2026-11-16: ledger, "C1: Greek terms of the analysis against Kitsopoulos".)
- From tiers A and D: the years of most classics in section Γ΄ were not searched one by one; *Logical Foundations of Probability* and the 1919 letter were read only through other authors' quotations; several rows rest on Wikipedia, catalogues or booksellers as their only or second source (marked in the tables).

## Open for the essay

- Life dates: the ancient and medieval ones, Avicenna, Searle, Gettier and Kripke were checked on 2026-11-17 (ledger, "The weakly sourced points of the essay, closed"). The other modern dates (Leibniz to Bruner) were not fetched one by one.
- Needs the books: the lecture number (XXI or XXII) of Turing's bridge remark in Diamond's *LFM* (page 211 is settled); Adorno's page (pp. 101–102, from two secondary sources).

## Method

1. One row per claim: location in the Markdown, the claim, two independent
   sources, verdict (confirmed / corrected / contested / unverifiable), action.
2. Prefer primary or archival sources, then peer-reviewed reference works, then
   university course material. No blogs, no unsourced summaries.
3. Fix the Markdown, run `python tools/build_html.py`, and check whether an HTML
   summary or data entry repeats the fact.
4. Where respectable sources disagree, do not pick a winner: add an
   «Ερμηνευτική σημείωση» that names both readings.

## Sources to use

- **Text and archive:** Wittgenstein Source / Wittgenstein Archives at the
  University of Bergen; the Ludwig Wittgenstein Project; the University of Iowa
  *Tractatus* Map (Stern); Klement's edition page (UMass); Brenner-Archiv,
  Innsbruck (Ficker correspondence).
- **Reference works:** Stanford Encyclopedia of Philosophy (Wittgenstein;
  Wittgenstein's Logical Atomism; Wittgenstein's Philosophy of Mathematics;
  Russell's Logical Atomism); Internet Encyclopedia of Philosophy.
- **Scholarship:** *Nordic Wittgenstein Review*; Oxford (*Oxford Handbook of
  Wittgenstein*; Beaney's 2023 OUP translation); Harvard (Goldfarb); Chicago
  (Conant); Cambridge (Potter; Trinity College archive); British Wittgenstein Society.
