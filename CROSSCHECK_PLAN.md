# Cross-check: open items

This file holds only what is still unchecked or weakly sourced. Every claim
already checked, with its source and verdict, is in
[`CROSSCHECK_DONE.md`](CROSSCHECK_DONE.md) (the ledger). New verdict rows go
there; when an item below is settled, record its row in the ledger and
remove it here.

## Open for the analysis

- C1 (Greek terms of the analysis vs Kitsopoulos) can now be done: both printings of the translation are in the folder (git-ignored), with OCR text in `ocr_local/`. C3 (a second Pears–McGuinness copy) needs a printed book.
- From tiers A and D: the years of most classics in section Γ΄ were not searched one by one; *Logical Foundations of Probability* and the 1919 letter were read only through other authors' quotations; several rows rest on Wikipedia, catalogues or booksellers as their only or second source (marked in the tables).
- A scan of the Kitsopoulos translation is catalogued at the University of Macedonia ([record](https://dspace.lib.uom.gr/handle/2159/20652?mode=full)), but the file asks for authorisation. With access to it, C1 could be done without a printed copy.

## Open for the essay

- Standard life dates were not checked one by one.
- Still weak: the page of Turing's bridge remark in Diamond's *LFM*; the wording of Strachey's letter; Adorno's page; Drury's page; Bays's 2004 argument. (Moore's examiner's report is no longer quoted: cut on 2026-11-15.)
- Turing's 1950 page range (433–460) and Moore's second 1954 page range are from memory.
- The Greek renderings were compared with the published translations on 2026-11-16 (ledger, "Essay review, point 7"). Still to locate and compare: *Investigations* §38 («κάνει αργία»). Proposition 3.328 was reworded in the essay; the analysis Markdown should be checked for the same wording under C1. The translator of the 1977 *Investigations* is to be confirmed from its title page.

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
