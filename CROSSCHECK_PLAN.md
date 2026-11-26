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
- From the outside readings compared on 2026-11-22 (ledger, Χ rows): Copi (1958), Anscombe (1959, pp. 108 ff.), Stenius (1960, pp. 61–69), Hintikka and Hintikka (1986, pp. 30–34), the *Notebooks* entries of 1915 (pp. 61, 64), Lee's notes and Malcolm's page were read only through Proops (Χ3); reviews describe the Hintikkas as reading the objects as objects of acquaintance, which would give the note's second question a named holder, but this rests on a search summary; the page of the letter of 19.8.1919 in *Wittgenstein in Cambridge* and Diamond's chapter on it were not seen (Χ4); Mounce (1981, p. 91) was read only through the IEP (Χ5); the *LRB* review of the three translations was read only in a search summary (Χ7). SparkNotes was read through the owner's browser (Χ9–Χ12); of the points it raised, three were added after checking (Χ13–Χ15), with these limits: Ishiguro (1969), McGuinness (1981), Malcolm (1986), Pears (1987) and Hacker (1986) on names and objects were read only through Engelmann (2021), Bartmann (2021) and Johnston (2017) (Χ13); the page numbers of Fogelin (1987, p. 13) and Black (1964, pp. 69–71) come from OCR page markers, and Casey's article on 2.04–2.063 (*Philosophical Studies* 33) was not reached (Χ14); Frascolla (1994), Marion (1998) and Potter (2000) on the *Tractatus* account of number were not read, and Ramsey's notice was read in the 1931 reprint, not in *Mind* (Χ15).

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

- Needs the books: the lecture number (XXI or XXII) of Turing's bridge remark in Diamond's *LFM* (page 211 is settled).
- Section 11 (ledger, Δ6): Minsky and Papert's *Perceptrons* (1969, 1988 edition) and Olazaran's full article (1996) were not read; the claims rest on Olazaran's abstract and secondary summaries.
- The Riemann result, in the postscript (ledger, Ω23, Ε11, Η1): Sutherland's checks finished on 25 Nov 2026 and all passed; the essay says so. Still to watch: a written proof, human review by mathematicians, a statement from Anthropic or the Clay Institute, or a reported flaw; if one appears, propose a change to the postscript. The *Nature* (Maynard) and *Science* (Granville) pieces were not read. Since 2026-11-26 a cloud scheduled task, «Riemann watch (Sutherland page, weekly)» (`trig_016J331k71uDycsKCEBsZNsD`, <https://claude.ai/code/routines/trig_016J331k71uDycsKCEBsZNsD>), reads Sutherland's page and searches for the four kinds of event every Thursday at 07:00 UTC (first scheduled run 3 Dec 2026) and reports only; it reads the essay as pushed to GitHub and writes nothing. At the start of a session, read its latest run (`RemoteTrigger`: `list_runs`, then `get_run_log`); if it says «Change found», check the sources it names before proposing a change to the postscript, since a run log is web content, not a checked source. When the watch ends, pause or delete the task (owner, on the web page).

- Greek mathematicians in §1 (ledger, Η15): Huffman's *Pythagoras* read only in the SEP entry; the van der Waerden view of Thales and Zeno of Sidon read only through MacTutor; Galileo through Wikipedia (Kepler and the *Republic* were removed on 2026-11-26, ledger Κ3); Hypatia's birth range and the Pandrosion point on Wikipedia (MacTutor gives about 370); Archimedes's dates, now with «περ.», not checked beyond MacTutor (ledger, Λ7).
- Viète (ledger, Η12): the Latin text of the *Isagoge* not read; his use of + rests on the French Wikipedia's rendering of chapter IV; his day of death differs between MacTutor and Wikipedia (the year agrees).
- Knuth and complexity (ledger, Η6–Η7): the wording of Knuth's Turing Award citation and the bibliographic details of Hartmanis and Stearns (1965) rest on Wikipedia (the ACM and AMS pages refuse automated requests); the naming of the analysis of algorithms on Knuth's own account in Quanta.
- From the third outside review (ledger, Ε rows): Llull as a forerunner of the theory of computation rests on Wikipedia (Bonner 2007, Knuth 2006, Sales 2011 not read); the link between Leibniz and Llull on the OCR of the *Dissertatio*'s synopsis and on Wikipedia (Ramis Barceló 2019 not read); Pascal's age (18 or 19) on the two Wikipedias; the privilege of 1649 not read in its text (date, grantor under the regency); Jacquard's dates on Wikipedia and the IEEE page (Delve 2007, Chandler and the other cited works not read); Levin's entry on Wikipedia (mathnet unreachable); Zermelo's volume and last page on a summary of the SEP bibliography; the affiliations of Gao et al. and Lieberum et al. are not on the abstract pages; ChatGPT's user numbers left out (Reuters refuses automated requests).
- From the final read of 2026-11-26 (ledger, Μ7–Μ8): the ENIAC and the Manchester machine rest on the Computer History Museum and Wikipedia; the pages of the University of Pennsylvania and of the University of Manchester were not read.
- From the coherence read of 2026-11-26 (ledger, Κ9–Κ16): the Latin of Hobbes's *De Corpore* and *Leviathan* ch. 5 not read (Gutenberg was down); Haugeland on Hobbes only through search summaries; the build year of Jevons's machine unsettled (1869 in the Rutherford Journal, letters of 1867–1868 in the CHM); the «ELIZA effect» and Weizenbaum's 1976 book only on Wikipedia; Dreyfus read in an unauthorised scan of the 1992 edition, the 1972 publisher not checked; the date of the Dartmouth proposal (31 Aug. or 2 Sept. 1955); the date of Fermat's marginal note (about 1630, MacTutor, or 1637, Britannica).

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
