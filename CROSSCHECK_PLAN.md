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

- Standard life dates were not checked one by one.
- The year 1995 for Wiles's proof (section 11, added 2026-11-17) is the standard date and was not searched.
- Still weak: the page of Turing's bridge remark in Diamond's *LFM*; the wording of Strachey's letter; Adorno's page; Drury's page; Bays's 2004 argument. (Moore's examiner's report is no longer quoted: cut on 2026-11-15.)
- Turing's 1950 page range (433–460) and Moore's second 1954 page range are from memory.
- The Greek renderings were compared with the published translations on 2026-11-16 (ledger, "Essay review, point 7"). *Investigations* §38 was located and compared later the same day. Not checked: the year (1977) of the Papazisis *Investigations*, which the OCR text does not show.

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
