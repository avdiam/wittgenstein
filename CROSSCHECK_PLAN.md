# Cross-check plan: analysis vs. outside sources

Status: **proposed, not started.** Nothing below has been checked online yet.

The quotations of the *Tractatus* in the analysis were checked against the three
PDFs in this folder. What the PDFs cannot settle is listed here.

## What the PDFs did and did not confirm

| Claim in the analysis | In the PDFs? |
| :-- | :-- |
| German text first appeared in Ostwald's *Annalen der Naturphilosophie* (1921) | Yes: Ogden's editorial note in Gutenberg #5740 |
| Wittgenstein refused Russell's introduction for a Reclam edition (1920); the Ostwald printing carried it in German | No |
| 1914 donation to artists (Rilke, Trakl) via Ficker; fortune to siblings in 1919 | No |
| "hausgewordene Logik" is Hermine Wittgenstein's phrase | No |
| Sraffa anecdote comes from Malcolm / von Wright | No |

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

## Tier A — factual and historical claims (objective, do first)

1. Title: Moore's suggestion and the allusion to Spinoza.
2. Pinsent: descent from Hume's brother; death in a test flight, May 1918.
3. Russell's introduction: the Reclam refusal and the Ostwald printing.
4. Paris courtroom model: notebook entry of 29.9.1914; the "read it in a magazine" detail.
5. Russell abandoning *Theory of Knowledge* (1913) because of Wittgenstein's criticism.
6. Ficker letter (1919): exact wording about the unwritten part and the ethical point.
7. Tolstoy's *Gospel in Brief* and "the man with the gospels".
8. The 1914 donation and the 1919 transfer of the fortune.
9. Teaching posts, the Hütteldorf gardening job, Haus Wittgenstein dates, the Hermine phrase.
10. Sraffa anecdote: source, setting, "form" vs "multiplicity".
11. 1929: "Some Remarks on Logical Form" and Ramsey's part in the colour-exclusion problem.
12. "Lecture on Ethics": date and the murder example.
13. Ladder precedents: Sextus (*Adv. Math.* VIII 481), Schopenhauer, Mauthner.
14. Lichtenberg's "Es denkt"; Schopenhauer's "eye of the world".
15. Hertz's wording ("innere Scheinbilder oder Symbole"); Kant *Prolegomena* §13; Leibniz *Monadology* §§1–3.
16. *Investigations* §43, §47, §107: wording and section numbers.
17. Who first published truth tables (the analysis says Wittgenstein "introduces" them; Peirce and Post need mentioning).
18. Sheffer stroke: whether "NOR" is the right gloss for Sheffer's 1913 operator.
19. Influence claims: Waismann and Carnap on probability; Tarski and Carnap on metalanguages; Davidson.

## Tier B — interpretive claims (compare with SEP/IEP and named scholars)

1. *Sachverhalt* as a *possible* combination vs an *existing* atomic fact (Ogden, Stenius, Black).
2. 1.11–1.12 as a rejection of Russell's general facts.
3. The nature of simple objects; the 2.0211–2.0212 argument for substance.
4. Names have only *Bedeutung*, propositions only *Sinn* (against Frege).
5. Whether the N operator really yields all of quantified logic (Fogelin, Geach, Soames debate).
6. Elimination of identity (Hintikka's exclusive readings of the variables).
7. Number as exponent of an operation; how far this rejects logicism.
8. Logical probability (5.15) and its relation to Bolzano and Keynes.
9. Solipsism and the metaphysical subject (5.6–5.641).
10. 6.3751 and the 1929 collapse: which claims the 1929 paper actually makes.
11. Traditional vs resolute readings of 6.54: fairness of both summaries, and whether intermediate positions (McGinn, Goldfarb) should be named.
12. "Logic is transcendental" (6.13) and "ethics is transcendental" (6.421): Kantian reading.
13. The characterisation of Mauthner and of the Vienna Circle.

## Tier C — translation and terminology

1. Greek terms against the published Greek translation (Kitsopoulos): *Sachverhalt*, *Sachlage*, *Sinn*, *Bedeutung*, *sinnlos*, *unsinnig*, *Bild*.
2. Contested renderings: 4.128 *zahllos*, 5.1361 *der Aberglaube*, 5.62 *die allein ich verstehe*, 6.13 / 6.421 *transzendental*.
3. Pears–McGuinness quotations (main propositions 1–7) against a second copy.

## Tier D — bibliography

Every entry in sections Β΄–Δ΄ of the bibliography was written from memory:
check author, title, publisher, year and page ranges, and confirm the Greek
translation entry (translator, publisher, year).

## Tier E — figures and text integrity

1. The ASCII figures (Necker cube labels at 5.5423, the eye diagram at 5.6331,
   the line figure at 6.36111) against page images of the 1922 edition.
2. German quotations against an online critical text, since PDF extraction loses diacritics.
3. The count of 526 propositions and the per-section counts.

## Out of scope unless requested

`Istoria_Logikis_kai_AI.docx` has not been reviewed at all.
