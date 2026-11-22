# Cross-check: open items

This file holds only what is still unchecked or weakly sourced. Every claim
already checked, with its source and verdict, is in
[`CROSSCHECK_DONE.md`](CROSSCHECK_DONE.md) (the ledger). New verdict rows go
there; when an item below is settled, record its row in the ledger and
remove it here.

## Open for the analysis

- C3 (a second Pears–McGuinness copy) needs a printed book. (C1 was done on 2026-11-16: ledger, "C1: Greek terms of the analysis against Kitsopoulos".)
- From tiers A and D: the years of most classics in section Γ΄ were not searched one by one; *Logical Foundations of Probability* and the 1919 letter were read only through other authors' quotations; several rows rest on Wikipedia, catalogues or booksellers as their only or second source (marked in the tables).
- From the commentary restored on 2026-11-21 (ledger, Σ and Τ rows): Frege's `⊢` in *Begriffsschrift* §2 and Russell's use of it (Τ4) and the consequence of dropping the Axiom of Infinity (Τ5) were not read in a source; Stenius (1960, ch. XI) and Glock's *Dictionary* on «transcendental» at 6.13 could not be reached (Σ6); the A/B page numbers of the Kant passages (Σ5); Maupertuis's memoirs read only in the Wikisource translations (Σ1); Euler's and Lagrange's part rests on Wikipedia and MacTutor (Σ2).
- From the commentary on 6.4 – 6.54 added on 2026-11-22 (ledger, Φ rows): Engelmann's memoir (1967, p. 97) and Ramsey's wording and page (1931, p. 238) were read only through Κιντή (Φ4, Φ9); Hacker's article of 2015 was not reached, so the "ground floor" and the link to 4.1213 rest on her report (Φ7); the passages she cites from Plato, Pseudo-Dionysius, Bacon and Schopenhauer were not read themselves (Φ6).
- From the outside readings compared on 2026-11-22 (ledger, Χ rows): Copi (1958), Anscombe (1959, pp. 108 ff.), Stenius (1960, pp. 61–69), Hintikka and Hintikka (1986, pp. 30–34), the *Notebooks* entries of 1915 (pp. 61, 64), Lee's notes and Malcolm's page were read only through Proops (Χ3); reviews describe the Hintikkas as reading the objects as objects of acquaintance, which would give the note's second question a named holder, but this rests on a search summary; the page of the letter of 19.8.1919 in *Wittgenstein in Cambridge* and Diamond's chapter on it were not seen (Χ4); Mounce (1981, p. 91) was read only through the IEP (Χ5); the *LRB* review of the three translations was read only in a search summary (Χ7). SparkNotes was read through the owner's browser (Χ9–Χ12); the five points it raises that the analysis does not treat (Χ12) are not yet checked in a better source.

## Open for the *Investigations* part

The research of 2026-11-18 settled most of the earlier items (ledger,
"Research for the *Investigations* part"); its notes and sources are in
`Philosophical Investigations/RESEARCH_NOTES.md`. Still open:

- Part II (*PPF*) section xi: the printed German wording of «halb
  Seherlebnis, halb ein Denken» and the PPF numbers (about §118 and
  §140) need a printed copy (1953, *Werkausgabe* 1, or Hacker–Schulte
  2009). No free online text of the published Part II exists; MS 144 on
  the BNE is the manuscript witness.
- Rhees's English preface to the *Blue and Brown Books* (1958): read it
  before quoting the closing sentence of the 1936 revision (the Greek
  translation of the preface has «vom (Anfang)», the manuscript «von
  Seite 118»).
- Dates the sources give differently: MS 140, MS 141, TS 220, TS 239;
  *Philosophische Grammatik* 1969 or 1970; *Philosophische Bemerkungen*
  1964 or 1965 (Kenny); second edition of the *Blue and Brown Books*
  1960 or 1969. Settle only those that the text will state.
- Read only through other authors so far: Kenny 1976, Kienzler 1997,
  Stern 1991, Hintikka 1986 and 1991, Engelmann 2013, Erbacher 2019.
- PI §2 vocabulary (*Würfel, Säule, Platte, Balken*) against the Brown
  Book's "cube, brick, slab, column": check on the LWP when arc 2 is
  written.
- Copyright of the English *Blue and Brown Books*: PD in the EU since
  2022; in the US probably to the end of 2053 (95 years from 1958). Not
  yet checked against a source.

## Open for the essay

- Life dates: the ancient and medieval ones, Avicenna, Searle, Gettier and Kripke were checked on 2026-11-17 (ledger, "The weakly sourced points of the essay, closed"). The other modern dates (Leibniz to Bruner) were not fetched one by one.
- From the critique of 2026-11-18 (ledger, "The critique of the essay, checked"): Tarski's life dates and the diagonal lemma were not fetched. (*Syntactic Structures* §2.4 and ch. 3 were read on 2026-11-19: ledger, Γ7.)
- Needs the books: the lecture number (XXI or XXII) of Turing's bridge remark in Diamond's *LFM* (page 211 is settled).
- Section 4 (ledger, Δ2): Boole's Rule of 0 and 1 read only through the SEP's quotation (*Laws of Thought*, pp. 37–38); Project Gutenberg returned 503. Retry #15114.
- Section 11 (ledger, Δ6): Minsky and Papert's *Perceptrons* (1969, 1988 edition) and Olazaran's full article (1996) were not read; the claims rest on Olazaran's abstract and secondary summaries.
- The postscript (ledger, Υ5): Anthropic's S-1/A filings were read only through TechCrunch's quotation; EDGAR refuses undeclared automated requests. Amendment No. 2 ("met this threshold") was left out of the essay unread.

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
