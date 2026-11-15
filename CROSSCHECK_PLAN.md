# Cross-check plan: analysis vs. outside sources

Status: **all tiers (A–E) checked online on 2026-11-14 and the corrections applied.** A few items need printed sources. The essay was checked on the same day; its results are the last section of this file.

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

## The essay

`Istoria_Logikis_kai_AI.docx` was out of scope for tiers A–E. It was reviewed afterwards: see "Results — the essay" at the end.

---

# Results — tiers A and D (checked 2026-11-14)

Verdicts: **confirmed** (sources agree with the analysis), **corrected** (the
analysis needs a change), **contested** (respectable sources disagree),
**unverifiable** (not settled in this pass). "Line" is the line number in
`TRACTATUS_LOGICO_PHILOSOPHICUS_ANALYSIS_1-7.md` at commit `7299538` (`1b600c8` before the history was rewritten on 2026-11-14).
Source quality is uneven: where the second source is only Wikipedia or a
bookseller's record, the row says so. The proposed actions were approved and applied on 2026-11-14 (Carnap weakened to «συγγενεύει με»; Lorentzatos left out).

## Tier A — factual and historical claims

| # | Claim (line) | Sources | Verdict | Proposed action |
| :-- | :-- | :-- | :-- | :-- |
| A1 | Title suggested by Moore, echoing Spinoza (8) | [Klagge, "Some Early Reactions to Wittgenstein's Tractatus"](http://jamesklagge.net/perch/resources/klagge-some-early-reactions.pdf); [Standard Ebooks essay](https://standardebooks.org/blog/the-book-that-solved-philosophy); [Wikipedia: TLP](https://en.wikipedia.org/wiki/Tractatus_Logico-Philosophicus) | confirmed | none |
| A2 | Pinsent: descendant of Hume's brother; killed in a test flight, 1918 (35) | [Univ. of Reading research blog](https://research.reading.ac.uk/research-blog/2018/05/16/how-ludwig-wittgensteins-secret-boyfriend-helped-deliver-the-philosophers-seminal-work/); [Wikipedia: David Pinsent](https://en.wikipedia.org/wiki/David_Pinsent) | confirmed (8 May 1918, Farnborough; he flew as observer, not pilot) | optional: add «Μάιος 1918, Farnborough» |
| A3 | Wittgenstein withheld Russell's introduction from Reclam (1920); Ostwald's 1921 printing carried it in German (64) | [Klagge](http://jamesklagge.net/perch/resources/klagge-some-early-reactions.pdf) (Reclam declined, May 1920); [*Russell* journal, "Russell's Introduction to Wittgenstein's Tractatus"](https://mulpress.mcmaster.ca/russelljournal/article/download/1473/1500) (introduction translated into German for Ostwald) | confirmed | none |
| A4 | Paris courtroom model, notebook entry 29.9.1914, "read it in a magazine" (302) | [Tagebücher 1914–1916, Ludwig Wittgenstein Project](https://wittgensteinproject.org/w/index.php/Tageb%C3%BCcher_1914-1916); [Sterrett, "Pictures, Models and Measures"](https://wittgenstein-initiative.com/pictures-models-and-measures/) | **corrected** | The entry says only that a motor-car accident is represented with dolls etc. in a Paris law-court. The magazine detail comes from von Wright's biographical sketch, not from the notebook. "Car and cart", "pedestrian dolls" and the labels a′, b′, c′ are the analysis's own illustration: mark them as such. |
| A5 | Russell abandoned *Theory of Knowledge* (1913) because of Wittgenstein's criticism (829) | [Connelly, Anthem Press blog](https://blog.anthempress.com/?p=2995); [NDPR review of *Russell and Wittgenstein on the Nature of Judgement*](https://ndpr.nd.edu/news/russell-and-wittgenstein-on-the-nature-of-judgement/); [Russell letters, McMaster](https://dearbertie.mcmaster.ca/letter/wittgenstein) | confirmed (which objection, and how decisive, is debated) | soften «ακριβώς εξαιτίας» to «κυρίως εξαιτίας» |
| A6 | Ficker letter 1919: ethical point; two parts; the unwritten part is the important one (1100) | [Wittgenstein Archives Bergen, "Wittgenstein and the Unwritten Part of the Tractatus"](https://wab.uib.no/ojs/index.php/agora-alws/article/view/2785/3294); [KIT Scientific Publishing chapter](https://books.openedition.org/ksp/1855) | confirmed | none |
| A7 | Tolstoy's *Gospel in Brief*: "the only book he carried"; "the man with the gospels" (1170) | [Westergaard, Wittgenstein Archives Bergen](https://wab.uib.no/agora-alws/article/viewFile/2838/3399); [*The Philosopher* (2001)](https://www.the-philosopher.co.uk/2001/04/wittgenstein-tolstoy-and-the-gospel-in.html) | **corrected** (nickname confirmed) | It was the only book *in the shop* (Tarnów, 1914), and he then carried it everywhere; it was not the only book he carried. Reword. |
| A8 | 1914 donation via Ficker (Rilke, Trakl); fortune to siblings 1919 (1248) | [Brenner-Archiv, Sammlung Wittgenstein](https://www.uibk.ac.at/de/brenner-archiv/bestaende/wittgenstein/); [literaturnische.de, Trakl material](https://literaturnische.de/Trakl/english/material/wittgenstein-e.htm); [ALWS, "His Life – His Work"](https://www.alws.at/his-life-his-work/) | confirmed (100,000 crowns; Trakl never drew his share; 1919 gift to Hermine, Helene and Paul) | none |
| A9 | "Left Cambridge" (1919–28); teaching at Trattenbach, Puchberg, Otterthal; gardener at Hütteldorf; Haus Wittgenstein 1926–28; Hermine's "hausgewordene Logik" (1248) | [Wittgenstein Initiative](https://wittgenstein-initiative.com/wittgensteins-dictionary-for-elementary-schools/); [Deutsche Biographie](https://www.deutsche-biographie.de/gnd118634313.html); [Barmherzige Brüder yearbook 2025](https://barmherzige-brueder.at/dl/nnruJKJKLnmNNonJqx4KJK/Ein_Heim_in_H_tteldorf-Granatapfel-Jahrbuch-2025-Barmherzige-Brueder-Oesterreich_pdf); [Meta-Biography of the Wittgensteins](https://www.researchgate.net/publication/368997847_A_Meta-Biography_of_the_Wittgensteins_Das_Familiengedachtnis) | **corrected** in one point, rest confirmed | He had left Cambridge in 1913, so «Εγκατέλειψε το Cambridge» under 1919 is wrong: say he withdrew from philosophy. Posts 1920–1926, gardener at the Brothers of Mercy in Hütteldorf (1926; the order has no employment record, only the tradition), house 1926–1928, phrase from Hermine's *Familienerinnerungen*: all confirmed. |
| A10 | Sraffa anecdote "preserved by Malcolm and von Wright"; "form" vs "multiplicity" as the two versions (1252) | [Language Log, "What is the logical form of that?"](https://languagelog.ldc.upenn.edu/nll/?p=59026); [Unterhuber, "Sraffa's Impact on Wittgenstein", Wittgenstein Archives Bergen](https://wab.uib.no/ojs/index.php/agora-alws/article/view/2647/3018) | **corrected** | Malcolm's *Memoir* gives the story with *both* "logical form" and "logical multiplicity". The other version is von Wright's, reported by Malcolm: the question was whether every proposition must have a "grammar", and Sraffa asked for the grammar of the gesture. Rewrite the two versions accordingly. |
| A11 | 1929 "Some Remarks on Logical Form" and Ramsey's part in colour exclusion (1251) | [Ometiță, "Logic and Phenomenology: Wittgenstein / Ramsey / Schlick in Colour-Exclusion"](https://philarchive.org/rec/OMELAP); [Wikipedia: Some Remarks on Logical Form](https://en.wikipedia.org/wiki/Some_Remarks_on_Logical_Form) (second source weak) | **corrected** in one point | The paper and its thesis are confirmed. Ramsey's role was his 1923 *Mind* review, which raised the objection; "studying 6.3751 again together with Ramsey" is not supported. Reword. |
| A12 | "Lecture on Ethics", 1929, murder example (1109) | [Lecture on Ethics, Ludwig Wittgenstein Project](https://www.wittgensteinproject.org/w/index.php/Lecture_on_Ethics); [LWP blog on the lecture](https://www.wittgensteinproject.org/w/index.php/Blog:Why_to_Read_Wittgenstein%E2%80%99s_Lecture_on_Ethics) | confirmed (read to the Heretics, Cambridge, 17 Nov 1929; the world-book, the murder and the falling stone are in the text) | none; the «ηθικό σωματίδιο» image is the analysis's own gloss and already stands outside quotation marks |
| A13 | Ladder precedents: Sextus *Adv. Math.* VIII 481, Schopenhauer WWR II, Mauthner (1167) | [Wittgenstein Archives Bergen, "Throwing Away the Ladder Before Climbing it"](https://wab.uib.no/ojs/index.php/agora-alws/article/view/2891/3506); [Wikipedia: Wittgenstein's ladder](https://en.wikipedia.org/wiki/Wittgenstein%27s_ladder) (citing Black's *Companion*, p. 377) | confirmed; wording to tighten | Mauthner's title is *Beiträge zu einer Kritik der Sprache* (vol. I), not *Kritik der Sprache*. «προέρχεται από» overstates, since the *Tractatus* names no source: say «απαντά ήδη στον». |
| A14 | Lichtenberg "Es denkt"; Schopenhauer's "eye of the world" (902, 1227) | Lichtenberg K 76: [Mengaldo (Univ. of Padua)](https://www.research.unipd.it/retrieve/e14fb26b-39be-3de1-e053-1705fe0ac030/Sonderdruck_Lichtenberg_K%26amp%3bK_2017.pdf); Schopenhauer: [WWV I §36, Projekt Gutenberg-DE](https://projekt-gutenberg.org/authors/arthur-schopenhauer/books/die-welt-als-wille-und-vorstellung-band-i/chapter/38) ("klares Weltauge") | confirmed (one primary or scholarly source each) | none |
| A15 | Hertz "innere Scheinbilder oder Symbole"; Kant *Prolegomena* §13; Leibniz *Monadology* §§1–3 (316, 1052, 318) | Hertz: [Badische Landesbibliothek scan](https://digital.blb-karlsruhe.de/download/pdf/7388303.pdf), [LMU handout](https://statsoz-neu.userweb.mwn.de/lehre/2013_WiSe/historische_und_philosophische_grundlagen/Folien/1_Die_Modelldefinition_von_Heinrich_Hertz_-_kurzeTexte.pdf); Kant: [*Auslegung* (Univ. of Kansas)](https://journals.ku.edu/auslegung/article/download/12856/12152/25487); Leibniz: [Monadology, tr. Duncan (Wikisource)](https://en.wikisource.org/wiki/Monadology_(Leibniz,_tr._Duncan)), [Rutherford (UCSD)](https://pages.ucsd.edu/faculty/rutherford/papers/Monads.pdf) | confirmed | none |
| A16 | *Investigations* §43, §47, §107 (1253, 1257, 1258) | [Hauptli, FIU lecture supplement](https://faculty.fiu.edu/~hauptli/Wittgenstein--PhilosophicalInvestigationsI1-242.htm); [PI §§39–50 text](https://topologicalmedialab.net/xinwei/classes/readings/Wittgenstein/lw39-50c.htm); [Philosophische Untersuchungen, LWP](https://books.wittgensteinproject.org/pdf/german/Philosophische%20Untersuchungen.pdf) | §47 and §107 confirmed; §43 **corrected** | §43 is qualified: "for a *large class* of cases, though not for all". The analysis quotes it without the qualifier; add it. The 1953 spelling is *rauhen Boden*. |
| A17 | Wittgenstein "introduces" truth tables (599) | [Anellis, "Peirce's Truth-functional Analysis and the Origin of Truth Tables"](https://arxiv.org/pdf/1108.2429); [Wikipedia: Truth table](https://en.wikipedia.org/wiki/Truth_table) | **corrected** | Wittgenstein and Post (1921) published them independently; Peirce has truth-table matrices in manuscripts of 1893 and c. 1902, and Russell's papers contain matrices from 1912–14. Say he gave them their familiar form and philosophical role, with a note on Peirce and Post. |
| A18 | Sheffer stroke glossed as NOR, written $p \downarrow q$ (691, 760) | [Wikipedia: Henry M. Sheffer](https://en.wikipedia.org/wiki/Henry_M._Sheffer) and [Sheffer stroke](https://en.wikipedia.org/wiki/Sheffer_stroke) (both citing Sheffer 1913 and Nicod 1917); Tractatus 5.1311 in the folder's PDFs | **corrected** (clarification) | Sheffer's 1913 stroke is indeed NOR, and 5.1311 uses $p \mid q$ for "neither p nor q". But since Nicod (1917) "Sheffer stroke" means NAND, and $\downarrow$ is Peirce's arrow. Add one sentence so a modern reader is not misled. The outside sources are weak: reading Sheffer's paper itself would close this. |
| A19a | Logical probability influenced Waismann and Carnap (721) | [Wikipedia: Friedrich Waismann](https://en.wikipedia.org/wiki/Friedrich_Waismann) (Waismann, *Erkenntnis* 1, 1930/31, 228–248); [SEP, Interpretations of Probability](https://plato.stanford.edu/ENTRIES/probability-interpret/) | Waismann confirmed; Carnap **unverifiable** in this pass | Keep Waismann. For Carnap, SEP names Johnson, Keynes and Jeffreys as predecessors and does not mention Wittgenstein; no source found here for a direct acknowledgment. Check *Logical Foundations of Probability* itself, or weaken to «συγγενεύει με». |
| A19b | Russell's hierarchy of languages "inspired Tarski and Carnap" (66) | [Awodey & Carus, "Carnap's Dream"](https://www.andrew.cmu.edu/user/awodey/preprints/CD.pdf); [Russell, *An Inquiry into Meaning and Truth*, ch. 4](https://www.ditext.com/russell/meaning/4.html) | Carnap supported; Tarski **corrected** | Carnap "may have been guided" by Russell's suggestion (Awodey & Carus), and Russell himself says the Vienna school developed it. No source ties Tarski's hierarchy to Russell's introduction. Say it anticipates the object-language / metalanguage distinction later developed by Carnap and Tarski. |
| A19c | Truth-conditional semantics developed by Carnap, Tarski, Davidson (502) | not searched separately | unverifiable in this pass | none proposed: the sentence is already hedged («θεωρείται… μία από τις αφετηρίες»). Belongs with tier B. |

## Tier D — bibliography

| Entry | Sources | Verdict | Proposed action |
| :-- | :-- | :-- | :-- |
| Stern, tree-structured editions, NWR 11 (2023), DOI …3675 | [NWR article 3677](https://www.nordicwittgensteinreview.com/article/view/3677); [NWR article 3675](https://www.nordicwittgensteinreview.com/article/view/3675) | **corrected** | The editions are DOI `10.15845/nwr.v11.3677`; `…3675` is Stern's companion essay "Tree-structured readings of the Tractatus". German text edited by Stern, Schulte and Saporiti. (Section Α΄, but wrong as it stands.) |
| *Notebooks 1914–1916*, ed. von Wright & Anscombe, Blackwell 1961 | [Maggs Bros. record](https://www.maggs.com/departments/philosophy_economics_and_social_sciences/authors/wittgenstein/notebooks-1914-1916/244783/); [AbeBooks record](https://www.abebooks.co.uk/book-search/title/notebooks-1914-1916-edited-wright-anscombe/author/wittgenstein-ludwig) | confirmed (booksellers' records only) | add «μτφρ. G. E. M. Anscombe» |
| "Some Remarks on Logical Form", PAS Suppl. 9 (1929), 162–171 | [Wikipedia](https://en.wikipedia.org/wiki/Some_Remarks_on_Logical_Form); [Ometiță](https://philarchive.org/rec/OMELAP) | confirmed | none |
| "A Lecture on Ethics", *Phil. Review* 74 (1965), 3–12 | [CSULB copy of the 1965 printing](https://cla.csulb.edu/departments/philosophy/wp-content/uploads/2025/12/Wittgenstein-1965-A-lecture-on-ethics.pdf); [LWP](https://www.wittgensteinproject.org/w/index.php/Lecture_on_Ethics) | confirmed (vol. 74, no. 1) | none |
| *Philosophical Investigations*, tr. Anscombe, Blackwell 1953 | [Erbacher, table of Nachlass editions](https://www.mediacoop.uni-siegen.de/wp-content/uploads/2017/11/Erbacher-2015-Philosophical_Investigations.pdf) | confirmed; incomplete | add «επιμ. G. E. M. Anscombe & R. Rhees» |
| *Briefe an Ludwig von Ficker*, ed. von Wright, Otto Müller 1969 | [RelBib catalogue](https://relbib.de/Record/1071589539); [Brenner-Archiv](https://www.uibk.ac.at/de/brenner-archiv/projekte/ludwig-wittgenstein-briefe/) | confirmed; incomplete | add «με τη συνεργασία του W. Methlagl» and «Brenner-Studien 1» |
| Greek translation, Κιτσόπουλος, Παπαζήσης 1978 | [Univ. of Ioannina thesis](https://olympias.lib.uoi.gr/jspui/bitstream/123456789/6693/1/%ce%9c.%ce%95.%ce%95%ce%9b%ce%95%ce%9d%ce%97%20%ce%95%ce%a5%ce%98%ce%a5%ce%9c%ce%99%ce%91%ce%94%ce%97.pdf); [Univ. of Patras catalogue](https://find.library.upatras.gr/Record/1131/Similar) | confirmed (series «Φιλοσοφία – Πηγές») | Expand to «Θανάσης Κιτσόπουλος». One source also names Ζ. Λορεντζάτος; his exact role (introduction or co-translation) is **unverifiable** here: check a copy before adding him. |
| Frege, "Über Sinn und Bedeutung", ZPhK 100 (1892), 25–50 | [IEP: Frege](https://iep.utm.edu/frege); University of Konstanz scan of the essay (header reproduced in the search result) | confirmed (NF 100) | none |
| Russell, "On Denoting", *Mind* 14 (1905), 479–493 | [TAMUCC](https://philosophy.tamucc.edu/node/445); JSTOR record as reported in the search result | confirmed (no. 56) | none |
| Russell, "Philosophy of Logical Atomism", *Monist* 28–29 (1918–19) | [Notre Dame early-analytic bibliography](https://www3.nd.edu/~jspeaks/courses/2007-8/43904/_HANDOUTS/early-analytic-bibliography.pdf); [*Russell* journal](https://mulpress.mcmaster.ca/russelljournal/article/download/1427/1454/1742) | confirmed | none |
| Russell, *Theory of Knowledge: The 1913 Manuscript*, Collected Papers 7, 1984 | [Routledge](https://www.routledge.com/The-Collected-Papers-of-Bertrand-Russell-Volume-7-Theory-of-Knowledge/Blackwell-Eames/p/book/9780415104500) | confirmed | add «επιμ. E. R. Eames με K. Blackwell, London: Allen & Unwin» |
| Sheffer, TAMS 14 (1913), 481–488 | [Wikipedia: Henry M. Sheffer](https://en.wikipedia.org/wiki/Henry_M._Sheffer); [UNM Boolean-algebra notes](https://www.cs.unm.edu/~veroff/BA) | confirmed; title truncated | full title ends «…, with application to logical constants» |
| Σέξτος, *Πρὸς Λογικούς* Β΄ (= M VIII), 481 | [Wittgenstein Archives Bergen paper](https://wab.uib.no/ojs/index.php/agora-alws/article/view/2891/3506) (cites 2:480–81) | confirmed | write «480–481» |
| Tolstoy, *Σύνοψη του Ευαγγελίου* (1881) | [Britannica](https://www.britannica.com/topic/The-Gospel-in-Brief) (1883); [Wikipedia](https://en.wikipedia.org/wiki/The_Gospel_in_Brief) (1892 / 1896) | **contested** date; 1881 unsupported | drop the single year: «(δεκαετία του 1880· δημοσ. δεκαετία του 1890)» |
| Ramsey, Critical Notice, *Mind* 32 (1923), 465–478 | [Notre Dame bibliography](https://www3.nd.edu/~jspeaks/courses/2007-8/43904/_HANDOUTS/early-analytic-bibliography.pdf); [copy of the notice](https://www.gwern.net/doc/philosophy/epistemology/1923-ramsey.pdf) | confirmed (no. 128) | none |
| Anscombe, *Introduction*, Hutchinson 1959 | [CiNii](https://ci.nii.ac.jp/ncid/BA59122454?l=en); [Texas A&M catalogue](https://libcat.library.tamu.edu/Record/in00000061857/Similar) | confirmed | none |
| Stenius, Blackwell 1960 | library record as reported in the search result | year confirmed; imprint not confirmed | none |
| Black, *Companion*, CUP 1964 | [*Spectator*, 13 Nov 1964](https://archive.spectator.co.uk/article/13th-november-1964/20/books); [Cambridge bibliography](https://www.cambridge.org/core/product/identifier/9781009067690%23EMT-RL-1/type/BOOK_PART) (lists Cornell UP) | confirmed (CUP in the UK, Cornell in the US) | none |
| Hacker, *Insight and Illusion*, 1972, rev. 1986 | [PhilPapers](https://api.philpapers.org/rec/HACIAI); [Anthem Press](https://anthempress.com/insight-and-illusion-hb) | confirmed | none |
| Diamond, *The Realistic Spirit*, MIT 1991 | [*The New Wittgenstein*, notes](https://philarchive.org/archive/CRATNW-2); [NWR, Mulhall](https://wab.uib.no/ojs/index.php/nwr/article/view/NWR-1_2012-Mulhall/html) | confirmed | none |
| Crary & Read, *The New Wittgenstein*, Routledge 2000, with Conant | [front matter](https://philarchive.org/archive/CRATNW-2) | confirmed (chapter 8 title matches; the author line was not visible in the source) | none |
| Malcolm, *Memoir*, OUP 1958 — "source of the Sraffa anecdote" | [PhilPapers](https://api.philpapers.org/rec/MALLW); [Broad's 1959 review](https://stafforini.com/docs/Broad1959ReviewNormanMalcolm.pdf) | confirmed | add that von Wright's variant is reported there too (see A10) |
| McGuinness, *Young Ludwig*, Duckworth 1988 | [LRB review](https://www.lrb.co.uk/v10/n12/george-steiner/whereof-one-cannot-speak); [*New Criterion*](https://newcriterion.com/article/the-philosophical-porcupine) | confirmed | none |
| Monk, *The Duty of Genius*, Cape 1990 | [NYRB review](https://www.nybooks.com/articles/1991/01/31/a-wonderful-life/); [*Russell* journal review](https://mulpress.mcmaster.ca/russelljournal/article/download/1820/1846/2136) | confirmed | none |
| Carroll, *Mind* 4 (1895), 278–280; Pears, *The False Prison* I (1987); Janik & Toulmin (Simon & Schuster 1973); Mauthner (Stuttgart 1901–02); Hertz (Leipzig 1894); *Principia* (CUP 1910–13) | searched, no usable record returned | **unverifiable** in this pass | none; no reason to doubt them, but they stay under the "from memory" caveat |
| Frege *Begriffsschrift* / *Grundgesetze*, Kant, Schopenhauer, Leibniz, Spinoza, Hume, Bradley (years only) | not searched | not checked | none (standard publication years) |

## Summary

- Tier A: 21 rows. 10 confirmed (three of them with small wording fixes: A2, A5, A13), 9 corrected (A4, A7, A9, A10, A11, A16, A17, A18, A19b), 2 unverifiable in this pass (A19a Carnap, A19c).
- The four claims the PDFs could not settle: Reclam **confirmed**; 1914 donation **confirmed**; Hermine's phrase **confirmed**; Sraffa sourcing **corrected**.
- Tier D: one wrong DOI (Stern), one unsupported date (Tolstoy), eight entries to complete, six entries plus the Stenius imprint still unverified, and the role of Lorentzatos in the Greek edition open.

---

# Results — tiers B, C and E (checked 2026-11-14)

Same verdict vocabulary as above. For interpretive claims, "contested" means
respectable sources disagree, and the action is an «Ερμηνευτική σημείωση» that
names both readings rather than picking one. All actions in this section have
been applied to the Markdown.

## Tier B — interpretive claims

| # | Claim | Sources | Verdict | Action taken |
| :-- | :-- | :-- | :-- | :-- |
| B1 | *Sachverhalt* defined as a *possible* combination of objects | [SEP, Wittgenstein's Logical Atomism](https://plato.stanford.edu/entries/wittgenstein-atomism/); [Hauptli, FIU lecture supplement](https://faculty.fiu.edu/~hauptli/Wittgenstein'sTractatus.html) (atomic-fact reading) | **contested** | Note added under the terminology table: possible combination (Stenius, Black, "state of affairs") vs existing atomic fact (Ogden's "atomic fact", Russell's introduction). The 1919 letter to Russell that is often quoted for the second reading could not be confirmed online, so it is not cited. |
| B2 | 1.11–1.12 as a rejection of Russell's general facts | [Notre Dame course notes (Speaks)](https://www3.nd.edu/~jspeaks/courses/mcgill/370/winter2004/wittgenstein-tractatus.htm); text of 1.11–1.12 and 2.04–2.05 | contested, already flagged | none: the existing «Ερμηνευτική σημείωση» covers it. No source found that settles it. |
| B3 | Reconstruction of the substance argument (2.0211–2.0212) | [SEP, Wittgenstein's Logical Atomism, §3.2](https://plato.stanford.edu/entries/wittgenstein-atomism/); [WAB, "Sense and Substance in Wittgenstein's Tractatus"](https://wab.uib.no/ojs/index.php/agora-alws/article/view/2501/2726) | confirmed as one standard reconstruction | Note added: the passage is compressed and other reconstructions exist; the broom example is borrowed from *Investigations* §60. |
| B4 | Names have only *Bedeutung*, propositions only *Sinn* | [Tractatus 3.3, 3.142 (Wikisource)](https://en.wikisource.org/wiki/Tractatus_Logico-Philosophicus/3); [Trebaul, early Wittgenstein's criticism of Frege](https://halshs.archives-ouvertes.fr/halshs-01532039/file/The%20early%20Wittgenstein%27s%20truth-conditional%20conception%20of%20sense%20in%20the%20light%20of%20his%20criticism%20of%20Frege%20%28Dewi%20Trebaul%29.pdf) | confirmed | none |
| B5 | The N operator yields quantified logic | [Fogelin, "Wittgenstein's Operator N" (citations)](https://philarchive.org/citations/FOGWON); [Rogers & Wehmeier, "Tractarian First-Order Logic", *Review of Symbolic Logic*](https://www.cambridge.org/core/journals/review-of-symbolic-logic/article/tractarian-firstorder-logic-identity-and-the-noperator/500C8C420D172A776C815A229A7601A6) | **contested** | Note added: the examples cover single generality only; Fogelin's objection about mixed multiple generality, the Geach and Soames replies, Rogers & Wehmeier (2012). |
| B6 | Elimination of identity | [Hintikka, "Identity, Variables, and Impredicative Definitions", JSL 1956](https://resolve-he.cambridge.org/core/journals/journal-of-symbolic-logic/article/identity-variables-and-impredicative-definitions/F1C920A3AF94F4DD32E2AC07E6B67920); [Wehmeier, "On Ramsey's 'Silly Delusion' Regarding Tractatus 5.53"](https://api.philpapers.org/rec/WEHORS) | confirmed; scholarship missing | Note added on Hintikka's weakly / strongly exclusive readings of the variables. The translation table itself matches 5.531–5.5321. |
| B7 | Number as exponent of an operation; "demolition" of logicism | [SEP, Wittgenstein's Philosophy of Mathematics](https://plato.stanford.edu/entries/wittgenstein-mathematics/) and its [notes](https://plato.stanford.edu/entries/wittgenstein-mathematics/notes.html) | **corrected** and contested | Corrected: the dependence on how many objects exist is Russell's problem (axiom of infinity), not Frege's; «Κατάρριψη» → «Απόρριψη», «αποδεικνύει» → «υποστηρίζει». Note added: whether the Tractatus keeps a class-free logicism (6.2, 6.234) is disputed. |
| B8 | Logical probability (5.15) and its relatives | [Ongaro, "The Interpretation of Probability in the Tractatus"](https://dc2.philarchive.org/rec/ONGTIO-2); [Coates, "Keynes, Wittgenstein, and Probability in the Tractatus"](https://philsci-archive.pitt.edu/24159/) | confirmed as a logical interpretation; relation to Keynes contested | Historical note added: von Kries's *Spielraum* and Keynes (1921). Bolzano is **unverifiable** here (no source found) and is not mentioned. |
| B9 | Solipsism and the metaphysical subject | [Hacker, *Insight and Illusion*, "Empirical Realism and Transcendental Solipsism"](https://core-prod.cambridgecore.org/core/books/insight-and-illusion/empirical-realism-and-transcendental-solipsism/4FF01EB81BC95E4A2547FE736BE9D548); [Heflik on transcendental solipsism](https://philarchive.org/archive/HEFSCO) | confirmed as the traditional reading; contested by resolute readers | Note added at 5.62 naming both. |
| B10 | 6.3751 and the 1929 paper | [Some Remarks on Logical Form (LWP)](https://books.wittgensteinproject.org/pdf/english/Some%20Remarks%20on%20Logical%20Form.pdf); [Notre Dame handout on colour incompatibility](https://www3.nd.edu/~jspeaks/courses/2007-8/43904/_HANDOUTS/tractatus-color-incompatibility.pdf) | confirmed | none (the paper says outright that the mutual exclusion of unanalysable statements of degree contradicts the *Tractatus*) |
| B11 | Traditional vs resolute readings of 6.54 | [Bronzo, "The Resolute Reading and Its Critics"](https://static.hum.uchicago.edu/philosophy/conant/Bronzo-ResoluteReadingsandItsCritics-W-S2012.pdf); [Hutchinson & Read, "An Elucidatory Interpretation of Wittgenstein's Tractatus"](https://philpapers.org/rec/HUTAEI) | both summaries fair; incomplete | Item Γ added: McGinn's and Hutto's elucidatory reading, the origin of "resolute" (Ricketts; Goldfarb 1997), and that Diamond and Conant do not call their reading "therapeutic". |
| B12 | "Transcendental" in 6.13 and 6.421 read in a Kantian sense | [Fairhurst, "'Ethics is transcendental'", *JAPA*](https://cambridge.org/core/journals/journal-of-the-american-philosophical-association/article/ethics-is-transcendental-tractatus-logicophilosophicus-6421/F3F3289810EB161F581162FB5AEEDFFA); [Tejedor draft (Univ. of Hertfordshire)](https://uhra.herts.ac.uk/id/eprint/4583/1/TejedorWReligionDraft.pdf) | 6.421 **contested**; 6.13 not covered by the sources found | Note added at 6.421: the *Notebooks* have "transcendent", the *Tractatus* "transcendental"; some read "transcendent", others take the change as deliberate. |
| B13 | Characterisation of Mauthner and of the Vienna Circle | [Nájera, "Wittgenstein versus Mauthner", WAB](https://wab.uib.no/ojs/index.php/agora-alws/article/view/2659/3042); [Cambridge excerpt on the positivist reading](https://assets.cambridge.org/97811087/44409/excerpt/9781108744409_excerpt.pdf) | confirmed | none |
| A19c | 4.024 and truth-conditional semantics (carried over from tier A) | [Trebaul](https://halshs.archives-ouvertes.fr/halshs-01532039/file/The%20early%20Wittgenstein%27s%20truth-conditional%20conception%20of%20sense%20in%20the%20light%20of%20his%20criticism%20of%20Frege%20%28Dewi%20Trebaul%29.pdf) (one source) | plausible, single source | none; the sentence is already hedged and has its own note |

## Tier C — translation and terminology

| # | Item | Sources | Verdict | Action taken |
| :-- | :-- | :-- | :-- | :-- |
| C1 | Greek terms against the Kitsopoulos translation | none found online (no glossary, review or excerpt) | **unverifiable** | none. Needs a printed copy of the Papazisis edition. |
| C2a | 4.128 *zahllos* | both local editions: Ogden "anumerical"; analysis already explains it is "without number", not "countless" | confirmed | none |
| C2b | 5.1361 *der Aberglaube* | both local editions: "Superstition is the belief in the causal nexus" | confirmed | none |
| C2c | 5.62 *die allein ich verstehe* | [Hintikka, "On Wittgenstein's 'Solipsism'"](https://www.taylorfrancis.com/chapters/edit/10.4324/9781315823270-13/wittgenstein-solipsism-1-jaakko-hintikka); Anscombe's report of Lewy's find, as quoted in the search result | analysis follows the now-standard reading; history missing | Translation note added (older "which only I understand" vs "the only language I understand"; Wittgenstein's own correction in a first-edition copy). |
| C2d | 6.13 / 6.421 *transzendental* | LWP German text | **corrected** (spelling) | The original reads *transcendental*; German quotation fixed in the Markdown and in two hand-written HTML passages. See B12 for the sense. |
| C3 | Pears–McGuinness wording of propositions 1–7 against a second copy | Klement's edition in the folder | **unverifiable** as specified | The Stern PDF in the folder carries Ogden only and the Pears–McGuinness text is not freely online, so there is no second copy to compare. The seven quotations read as in Klement where the three-column extraction allows a check. |

## Tier E — figures and text integrity

| # | Item | Source | Verdict | Action taken |
| :-- | :-- | :-- | :-- | :-- |
| E1a | Necker cube, 5.5423 | [figure in the LWP edition](https://www.wittgensteinproject.org/w/index.php/Logisch-philosophische_Abhandlung) | **corrected** | In the original the *a* corners form the lower-left face and the *b* corners the upper-right face; the ASCII figure had them the other way round. Labels swapped. |
| E1b | Eye diagram, 5.6331 | same | **corrected** | The original is a teardrop with "Auge" at its pointed end, i.e. the eye drawn as part of the field's outline, not inside it. ASCII figure redrawn; wording fixed in the Markdown and in two hand-written HTML passages. The interactive SVG in the visual lab was redrawn the same way afterwards (teardrop, "Auge" at the tip), and its caption reworded to match 5.633. |
| E1c | Line figure, 6.36111 | same | confirmed | none (o—x labelled *a*, x—o labelled *b*) |
| E2 | German quotations | LWP German text, compared by script (87 fragments, whitespace and punctuation ignored) | confirmed, two spelling variants | All Tractatus fragments found except *transzendental* (original: *transcendental*, fixed) and *lässt* (original: *läßt*; modern spelling kept). |
| E3 | 526 propositions; 7 / 79 / 74 / 109 / 151 / 105 / 1 | proposition anchors in the LWP edition, counted by script | confirmed | none. Wikipedia's "525" does not match either the PDFs or this count. |

# Results — online follow-up and browser check (2026-11-14)

Items left open by the two passes above that could be settled from online
sources. Printed-book items (C1, C3) and the essay were left for a later pass.

| # | Item | Sources | Verdict | Action taken |
| :-- | :-- | :-- | :-- | :-- |
| B1 | Letter to Russell, 19.8.1919, on *Sachverhalt* / *Tatsache* | [Dožudić, "Thoughts in Exchange: A Note on Frege's Tractatus Letters", *Filozofia* 76 (2021), 531–541](https://www.sav.sk/journals/uploads/10031758filozofia.2021.76.7.4.pdf) (quotes both sentences); [Sullivan & Johnston, "Judgements, Facts and Propositions", *Oxford Handbook of Truth* (2018)](https://dspace.stir.ac.uk/bitstream/1893/23779/1/PMS-CJ%20paper%20for%20OUP%20Truth%20Handbook.pdf) (quotes the first). Both cite *Wittgenstein in Cambridge*, ed. McGuinness (2008), p. 98 | **confirmed** | Quotation added to the «Ερμηνευτική σημείωση» on *Sachverhalt*, as the evidence usually given for the atomic-fact reading; the edition added to section Β΄ of the bibliography. The letter itself was read only as quoted by these two papers. |
| B8 | Bolzano as a precursor of 5.15 | [SEP, Bolzano's Logic, §6.4](https://plato.stanford.edu/entries/bolzano-logic/): "It is possible that in his Tractatus 5.15, Wittgenstein took over Bolzano's treatment of probability, perhaps through the mediation of … R. Zimmermann (1853)" | **confirmed** as a possibility (one source) | Sentence added to the historical note under 5.15, with the same hedge. |
| A19a | Carnap and the *Tractatus* on probability | [Carnap, "On Inductive Logic", *Philosophy of Science* 12 (1945), 72–97](http://www.fitelson.org/probability/carnap_1945.pdf), footnote 13 | **confirmed**, and more specific than the analysis | Carnap says the definition of 5.15 "coincides with the function c_W", and rejects c_W because it would never let past experience influence expectations. Added to the historical note; article added to section Δ΄. «συγγενεύει με» in the running text stays. *Logical Foundations of Probability* itself was not read. |
| D | Carroll, *Mind* 4 (1895), 278–280 | [Wikipedia](https://en.wikipedia.org/wiki/What_the_Tortoise_Said_to_Achilles) (N.S. vol. 4, no. 14, doi 10.1093/mind/IV.14.278) | confirmed (weak source) | none |
| D | Pears, *The False Prison* I, Clarendon 1987 | [Texas A&M catalogue](https://libcat.library.tamu.edu/Record/in00000009644/Details); [LRB review (Hacking)](https://www.lrb.co.uk/v10/n03/ian-hacking/solipsism) | confirmed | none |
| D | Janik & Toulmin, Simon & Schuster 1973 | [*Slavic Review* notice](https://www.cambridge.org/core/journals/slavic-review/article/wittgensteins-vienna-by-allan-janik-and-stephen-toulmin-new-york-simon-and-schuster-1973-314-pp-895-cloth-395-paper/D5E125F39FC6A36B2D8B034908509DF1); [Texas A&M catalogue](https://libcat.library.tamu.edu/Record/in00000269577) | confirmed | none |
| D | Mauthner, 3 vols, Stuttgart 1901–02 | [letter edition, Univ. Wuppertal](https://elekpub.bib.uni-wuppertal.de/download/pdf/7877894.pdf); [*Grenzboten* review](https://brema.suub.uni-bremen.de/grenzboten/download/pdf/342809) (both as reported in the search result) | confirmed (some lists give 1901–1903) | publisher «Cotta» added |
| D | Hertz, Leipzig 1894 | [TIB record](https://goobi.tib.eu/viewer/metadata/1884377475/1); [AMS *Bulletin* review, 1894](https://www.ams.org/bull/1894-01-03/S0002-9904-1894-00248-1) (both as reported in the search result) | confirmed | publisher «J. A. Barth» added |
| D | *Principia Mathematica*, 3 vols, CUP 1910–13 | [SEP, Principia Mathematica](https://plato.stanford.edu/entries/principia-mathematica/) | confirmed (1910, 1912, 1913) | none |
| D | Stenius, Oxford: Blackwell 1960 | [CiNii](https://ci.nii.ac.jp/ncid/BA19243748); [Maggs Bros.](https://www.maggs.com/departments/philosophy_economics_and_social_sciences/authors/wittgenstein-stenius/wittgensteins-tractatus-a-critical-exposition-of-its-main-lines-of-thought/243079/) | confirmed (one catalogue lists a Cornell UP issue of the same year) | none |
| D | Role of Lorentzatos in the 1978 Greek edition | [Univ. of Patras catalogue](https://find.library.upatras.gr/Record/1131): Κιτσόπουλος (Μεταφραστής), Λορεντζάτος and Russell (each «Συγγραφέας εισαγωγής κ.λπ.»); [Univ. of Macedonia record](https://dspace.lib.uom.gr/handle/2159/20652?mode=full) (translator only, 143 pp.) | **confirmed** from one catalogue | Entry now reads «με εισαγωγικά κείμενα του Ζήσιμου Λορεντζάτου και του B. Russell». A bookseller listing reported in a search result gives the title of Lorentzatos's text as «Ο Tractatus του Wittgenstein και ο άναξ ού το μαντείον» and says the translation first appeared in *Δευκαλίων* 7/8 (1971); neither was read directly, so neither is in the Markdown. |
| D | Years of the classics | [Wikipedia, list of publications in philosophy](https://en.wikipedia.org/wiki/List_of_important_publications_in_philosophy); [Wikipedia: Frege](https://en.wikipedia.org/wiki/Gottlob_Frege) | *Monadologie* and *Grundgesetze* confirmed; the rest not searched | *Monadologie*: «(1714· δημοσ. 1720)». The caveat under the bibliography heading was shortened accordingly. |
| E1a | Necker cube in the visual lab (hand-written SVG) | compared with the Markdown figure, corrected under E1a above | **corrected** | The lab still had the *a* corners on the upper-right face. Faces and labels swapped, and the two viewpoint captions with them. |
| — | Browser check of the built page | Chrome, page served from `127.0.0.1` | passed | All six tabs render; 553 KaTeX spans, no KaTeX errors, no unrendered `$…$`; all 33 `onclick` handlers resolve; no dead in-page anchors or duplicate ids; no console errors. KaTeX logs about 400 warnings for Greek letters inside math (no font metrics); they render with a fallback font. Re-checked after the final rebuild (554 spans). |

## Still open after this pass

- C1 (Greek terms vs Kitsopoulos) and C3 (a second Pears–McGuinness copy) need printed books.
- From tiers A and D: the years of most classics in section Γ΄ were not searched one by one; *Logical Foundations of Probability* and the 1919 letter were read only through other authors' quotations; several rows rest on Wikipedia, catalogues or booksellers as their only or second source (marked in the tables).
- A scan of the Kitsopoulos translation is catalogued at the University of Macedonia ([record](https://dspace.lib.uom.gr/handle/2159/20652?mode=full)), but the file asks for authorisation. With access to it, C1 could be done without a printed copy.
- `Istoria_Logikis_kai_AI.docx`: reviewed on 2026-11-14, see the next section.

---

# Results — the essay (checked 2026-11-14)

`Istoria_Logikis_kai_AI.docx` was read in full and its claims checked online.
It was not edited. The corrected and extended text is
`Logiki_Glossa_Michanes.md` (source) and `Logiki_Glossa_Michanes.docx`
(generated by `tools/build_docx.py`). Same verdict vocabulary as above.
"SEP" is the Stanford Encyclopedia of Philosophy
(`https://plato.stanford.edu/entries/<name>/`), "MacTutor" the St Andrews
archive (`https://mathshistory.st-andrews.ac.uk/Biographies/<name>/`).
"Snippet" means the fact was seen only in a search result, not on a page that
was opened.

## Claims of the original essay

| # | Claim in the original | Sources | Verdict | Action in the new text |
| :-- | :-- | :-- | :-- | :-- |
| S1 | Chrysippus "father of propositional logic" | SEP `logic-ancient` | confirmed in substance; the label is the essay's | Label dropped; Philo's and Diodorus's conditional and the *lekta* added. |
| S2 | Boole's "+" was an exclusive or | SEP `boole`, `algebra-logic-tradition`; *Laws of Thought* (Project Gutenberg #15114) | **corrected** | "+" was defined only for classes with no common member; inclusive "+" from Jevons (1864) and Peirce (1867). |
| S3 | x² = x "proves that logic has two truth values" | same | **corrected** | Boole notes that only 0 and 1 satisfy it and derives x(1 − x) = 0, the principle of contradiction; he speaks of classes, not truth values. |
| S4 | Frege (1879) introduced the quantifiers ∀ and ∃ | SEP `frege`, `pm-notation`; MacTutor, Earliest Uses of Symbols of Set Theory and Logic | **corrected** | Frege had his own notation; ∃ is Peano's (1897), ∀ Gentzen's (1935). |
| S5 | *Wertverläufe* glossed as "extensions of concepts", placed in 1879 | SEP `frege` | **corrected** | The term is left out; Basic Law V is placed in the *Grundgesetze* (1893/1903). |
| S6 | Russell wrote to Frege in 1901 | SEP `russell-paradox`, `frege` | **corrected** | Paradox found in spring 1901; letter of 16 June 1902. Frege's appendix: "my law V … is false" (as quoted by SEP). |
| S7 | *Principia* "established" ∨ and ⊃ | SEP `principia-mathematica`, `pm-notation` | corrected in wording | The notation owes much to Peano; *Principia* made the signs familiar. |
| S8 | ZFC by Zermelo and Fraenkel | SEP `zermelo-set-theory` | confirmed; incomplete | Zermelo 1908; Fraenkel and Skolem 1922. |
| S9 | Wittgenstein visited Frege in 1911; Russell's "most exciting intellectual adventures" | SEP `wittgenstein`; MacTutor `Wittgenstein` | confirmed; the Russell sentence was seen only as quoted by MacTutor | Kept, without quotation marks. Its original place (probably Russell's obituary note in *Mind*, 1951) was not seen. |
| S10 | Truth tables "established" by Wittgenstein and Post | row A17 above | corrected as in A17 | Peirce's manuscripts mentioned. |
| S11 | Tractatus says almost nothing of Boole | the two PDFs in the folder (no occurrence of "Boole") | confirmed | «δεν αναφέρει πουθενά τον Boole». |
| S12 | Hilbert posed the *Entscheidungsproblem* "after Gödel's blow" | SEP `church-turing` | **corrected** | Hilbert & Ackermann, 1928. Church published the negative answer a few months before Turing. |
| S13 | Gödel's sentence is "an equation"; first theorem assumes consistency | SEP `goedel-incompleteness` | corrected in wording | A statement of arithmetic; Gödel used ω-consistency, Rosser (1936) reduced it to consistency. SEP's warning that "G says it is unprovable" is to be taken loosely is reflected («χαλαρά μιλώντας»). |
| S14 | Hilbert believed every mathematical truth provable | SEP `hilbert-program`; MacTutor `Hilbert` | confirmed if put as completeness and solvability | Reworded; 1930 "Wir müssen wissen, wir werden wissen". |
| S15 | Wittgenstein "rejected" Gödel's theorem | SEP `wittgenstein-mathematics`; [Lampert, WAB](https://wab.uib.no/ojs/index.php/agora-alws/article/view/2593/2910) | **contested** | «Ερμηνευτική σημείωση»: Gödel, Kreisel, Bernays versus Floyd & Putnam (2000); Bays and Rodych against the latter. Floyd & Putnam and Bays were read only through other authors. The original's football-goal analogy was dropped. |
| S16 | Turing was 24 in 1936 and "proved the halting problem" | SEP `church-turing`, `turing-machine`; Turing's paper; [S. Lucas, "The origins of the halting problem" (2021)](https://riunet.upv.es/handle/10251/189460) | **corrected** | Aged 23 at submission (May 1936). The paper proves that being "circle-free", and printing a given symbol, are undecidable; name and usual form of the halting problem from Davis (1950s); the short proof from Strachey (1965; snippet). |
| S17 | The universal machine is the basis of the modern computer | SEP `computing-history` and `turing-machine` (they differ) | **contested** | Both views stated. |
| S18 | Shannon revived a "forgotten" Boolean algebra in 1937, aged 21 | MacTutor `Shannon`; [MIT DSpace](https://dspace.mit.edu/handle/1721.1/11173) | date and age confirmed; "forgotten" **corrected** | «σχεδόν άγνωστη στους μηχανικούς»; Nakashima 1935–36 mentioned (snippet, [IPSJ museum](https://museum.ipsj.or.jp/en/computer/dawn/0002.html)). |
| S19 | Symbolic AI 1950–1980, "millions of rules", triumph in chess | SEP `artificial-intelligence`; [IBM, Deep Blue](https://www.ibm.com/history/deep-blue); Buchanan & Shortliffe 1984 (snippet) | **corrected** | Dartmouth 1956; MYCIN had some hundreds of rules; Deep Blue (1997) worked by search. "GOFAI" from Haugeland 1985 (weak source). |
| S20 | LLMs "vindicate" the later Wittgenstein | [Bender & Koller, ACL 2020](https://aclanthology.org/2020.acl-main.463.pdf); [Molino & Tagliabue, arXiv 2302.01570](https://arxiv.org/abs/2302.01570) (abstract) | **contested** | «Ερμηνευτική σημείωση». Firth's 1957 phrase and Masterman's unit rest partly on snippets. |
| S21 | LLMs are "subject to Gödel's theorems" | SEP `goedel-incompleteness`, `computational-mind`; [IEP, Lucas–Penrose argument](https://iep.utm.edu/lp-argue/) | **corrected** | Limits of computability apply to any program; Gödel's theorems concern axiom systems; Lucas–Penrose and the standard reply; Gödel's 1951 disjunction. |
| S22 | Neuro-symbolic AI is "the cutting edge" | Garcez & Lamb, *Artificial Intelligence Review* 56 (2023), doi 10.1007/s10462-023-10448-w | corrected in wording | «Μια ενεργή κατεύθυνση»; its advocates call it the next wave. |
| S23 | *Investigations*: "meaning is use", "illnesses of language" | German text of the Ludwig Wittgenstein Project | §43 corrected as in A16; "illnesses of language" **not in the text** | §43 with its qualifier; §§23, 38, 66–67, 108, 109, 255 and the preface (Sraffa) checked against the German text. |

## New material

| Topic | Sources | Status |
| :-- | :-- | :-- |
| Plato (*Cratylus*, *Sophist*, *Theaetetus*), Aristotle | SEP `plato-cratylus`, `plato-sophstate`, `plato-theaetetus`, `aristotle-logic`, `aristotle-noncontradiction`; *De Interpretatione* 1 (Edghill, MIT Classics) | confirmed |
| Megarians or "Dialectical school"; Stoic *lekta* | SEP `dialectical-school`, `logic-ancient` | confirmed; the school label is contested and the text says so |
| Abelard, Ockham, the razor | SEP `abelard`, `ockham`; [IEP, Ockham](https://iep.utm.edu/ockham/); Tractatus 3.328 in the folder's PDFs | confirmed. The Latin wordings were seen only in snippets and are not quoted. |
| Leibniz | SEP `leibniz`, `leibniz-logic-influence`; MacTutor `Leibniz` | confirmed. "Calculemus" was not found in a good source and is not used. No documented link to the Tractatus: the text says the kinship with logical space is interpretation. |
| Locke, Hume, Kant; rationalism and empiricism | SEP `locke`, `hume`, `kant`, `analytic-synthetic`, `rationalism-empiricism`; [Hume, *Enquiry* 4](https://davidhume.org/texts/e/4); Tractatus preface, 4.0031, 6.36311 | confirmed. "Kantian" reading marked as interpretation. |
| Cantor's diagonal argument | MacTutor `Cantor`; SEP `settheory-early` (dates it 1892; often given as 1891) | confirmed; the text says «αρχές της δεκαετίας του 1890» |
| Frege on sense and reference; Russell on descriptions | SEP `frege`, `descriptions`; Tractatus 4.0031 | confirmed |
| Barber paradox | SEP `russell-paradox`; Russell's 1918 wording seen only via Wikipedia | confirmed (weak for the wording). Who suggested it to Russell is **unverifiable** and not stated. |
| Grelling–Nelson "heterological" (1908) | SEP `paradoxes-contemporary-logic` | confirmed |
| Library-catalogue illustration | none | the essay's own illustration; no source found, none claimed |
| Wittgenstein's 1931 list of influences | [Malcolm, *LRB* 3/3 (1981)](https://www.lrb.co.uk/the-paper/v03/n03/norman-malcolm/wittgenstein-s-bag-of-raisins), quoting *Culture and Value* | confirmed (as quoted by Malcolm) |
| Hilbert's programme; Gödel's theorems | SEP `hilbert-program`, `goedel-incompleteness` | confirmed |
| Turing machine in Turing's own terms; Church–Turing thesis | Turing 1936, §§1 and 9; SEP `church-turing` | confirmed. The tally-mark adding machine and the music-box comparison are the essay's own illustrations. |
| Goldbach example for the halting checker | none | the essay's own illustration (a standard one); not sourced |
| Decidable and undecidable problems | SEP `church-turing`; MacTutor `Matiyasevich`; Presburger and Wang/Berger from snippets (the latter via Wikipedia) | first-order logic and Hilbert's tenth confirmed; Presburger (1929 or 1930) and the tiling problem **weakly sourced**; the statement that tilings can encode programs is not sourced |
| McCulloch & Pitts, Rosenblatt, Logic Theorist | SEP `computational-mind`, `artificial-intelligence`; Carnap's notation and the 38-of-52 count from snippets | confirmed in outline |
| How language models are trained; hallucination | Jurafsky & Martin, *Speech and Language Processing*, 3rd ed. draft (Aug. 2026), ch. 1 and 7; Ji et al., *ACM Computing Surveys* 55(12), 2023, doi 10.1145/3571730 | confirmed |
| Early reception; Ramsey; "linguistic turn" | SEP `wittgenstein`, `ramsey`, `logical-atomism`, `rorty`; [IEP, Analytic Philosophy](https://iep.utm.edu/analytic-philosophy/) | confirmed; who began the turn is contested and the text says so (Dummett's view from a snippet) |
| Vienna Circle | SEP `vienna-circle`, `schlick`, `carnap`, `ayer`; [manifesto excerpt (Pittsburgh)](https://sites.pitt.edu/~jdnorton/teaching/Phil_Sci_Core/Phil_Sci_Core_2022/docs/Vienna_Circle_manifesto_JDN.pdf); Neurath in Ayer (ed.), *Logical Positivism* (archive.org OCR); Ficker letter: row A6 | confirmed; fidelity of the Circle's reading **contested** (note added). Carnap's "artist" remark and the Tagore episode could not be traced to Carnap's own text and are not used. |
| Later influence: Oxford, Anscombe, Kuhn, Kripke, Rorty, Russell's verdict | [IEP, Wittgenstein](https://iep.utm.edu/wittgens/) and [Ordinary Language Philosophy](https://iep.utm.edu/ord-lang/); SEP `anscombe`, `thomas-kuhn`, `private-language`, `rorty`; Russell, *My Philosophical Development* (archive.org OCR) | confirmed |
| Winch, Rosch & Mervis, Geertz | snippets only | **weakly sourced**; the sparrow and penguin example is the essay's own |
| Marxist reception: Cornforth, Marcuse, Adorno, Eagleton, Sen on Sraffa and Gramsci, the 1935 journey | Cornforth 1946 (scan); [Marcuse, ch. 7](https://www.marcuse.org/herbert/pubs/64onedim/odm7.html); Adorno as quoted in *Philosophy Now* 19 (book not seen); [Eagleton, *NLR* I/135](https://newleftreview.org/issues/i135/articles/terry-eagleton-wittgenstein-s-friends); [Sen, *JEL* 2003](https://econpapers.repec.org/RePEc:aea:jeclit:v:41:y:2003:i:4:p:1240-1255) (abstract); [Malcolm, *LRB* 3/21](https://www.lrb.co.uk/the-paper/v03/n21/norman-malcolm/wittgenstein-s-confessions); [Moran, *NLR* I/73](https://newleftreview.org/issues/i73/articles/john-moran-wittgenstein-and-russia) | confirmed with the limits stated; Rossi-Landi from a snippet. No Soviet critic could be sourced by name, so none is mentioned. |
| Hegelian reception: Bradley, the remark to Drury, Sellars, Brandom, McDowell, Taylor | SEP `hegel`; Malcolm, *LRB* 3/21 (quoting Drury) | confirmed; Drury's own text not seen |
| *On Certainty* | SEP `wittgenstein` §5; IEP, Wittgenstein | confirmed |

## The owner's note `Wittgenstein intro.md` (checked 2026-11-14)

The note was read, its claims checked, and what held up was merged into the
essay (sections 6, 8 and 10). The note itself was not edited.

| # | Claim in the note | Sources | Verdict | Action in the essay |
| :-- | :-- | :-- | :-- | :-- |
| N1 | The *Tractatus* is the only book he published in his lifetime | [IEP, Wittgenstein](https://iep.utm.edu/wittgens/) ("the only philosophy book"); SEP `wittgenstein` (cites the 1929 paper); [Austria-Forum](https://austria-forum.org/af/AEIOU/Wittgenstein%2C_Ludwig/Wittgenstein%2C_Ludwig_english) (dictionary 1926) | **corrected** | «το μόνο φιλοσοφικό βιβλίο»; the 1926 school dictionary and the 1929 article named. |
| N2 | Russell was deeply influenced by his pupil | SEP `russell`, `wittgenstein-atomism`, `principia-mathematica`, `logical-atomism`; Russell's 1918 acknowledgement as quoted by SEP and by Landini (CUP) | confirmed, with a dissent | Added to section 6, with Landini's view that Russell "embellished matters" for his friend's sake. The 1918 text itself was not opened. |
| N3 | Picture theory: a proposition has sense only if testable, or if a tautology | SEP `wittgenstein`; Tractatus 4.003, 4.461, 4.4611 (LWP German text) | **corrected** | The note mixes the *Tractatus* with the Vienna Circle's verificationism, which the essay keeps apart. Tautologies are *sinnlos* but not *unsinnig*; added to section 6, using the analysis's terms («χωρίς νόημα» / «ανόητες»). The essay's rendering of 6.54 and the resolute-reading note were aligned with this. |
| N4 | Influenced philosophy of mind: Dennett, Fodor | [Dennett, *TIME* 100 (1999)](https://time.com/archive/6735017/ludwig-wittgenstein-philosopher/); [Dennett, autobiography, *Philosophy Now* 68](https://philosophynow.org/issues/68/Daniel_Dennett_Autobiography_Part_1); SEP `private-language` (Fodor 1975, pp. 68–73) | Dennett confirmed; Fodor **corrected** (a critic) | Both added, Fodor as a critic. Dennett's two sources are his own words but not peer-reviewed. |
| N5 | Turing attended the 1939 lectures and argued with Wittgenstein | SEP `turing` (Diamond 1976); [Matthíasson, *BJHP* 29 (2021)](https://research-portal.st-andrews.ac.uk/en/publications/contradictions-and-falling-bridges-what-was-wittgensteins-reply-t/) (abstract); [Floyd, BU slides (2012)](https://www.bu.edu/cphs/files/2013/08/Floyd.pdf) | confirmed; influence ran both ways | New subsection at the end of section 8: the falling-bridge exchange; Turing's 1944–45 acknowledgement; RPP I §1096 ("These machines are humans who calculate"). Diamond's edition and Turing's typescript were not opened; Floyd's are slides, not a paper. |
| N6 | He "proved" that a private language is impossible | SEP `private-language`; *Investigations* §§243, 258, 293 (LWP German text) | **contested**; "proved" too strong | Added to section 10 with the diary and beetle examples and an «Ερμηνευτική σημείωση». |
| N7 | The fly and the fly-bottle | *Investigations* §309 (LWP German text) | confirmed | Added to the passage on therapy. The toolbox (§11), also checked, added to meaning as use. |
| N8 | He showed Austin that language does things | SEP `austin-jl`; [Harris & Unnsteinsson, *BJHP* 2018](https://opinvisindi.is/handle/20.500.11815/1981) (abstract); [Austin, *How to Do Things with Words* (1962), p. 5](https://web.english.upenn.edu/~cavitch/pdf-library/Austin_How_To_Do_Things_with_Words.pdf) | **contested** | Austin's performatives added with his own examples (ship, bet; not "I do", which Austin's editor flags as a slip); «Ερμηνευτική σημείωση» on the dispute over influence. |
| N9 | "Forms of life" gave the social sciences a non-judging tool (Winch) | SEP `relativism` | confirmed; charge of relativism live | Winch's 1964 Azande article and Lukes's reply added. "Western positivist standards" is the note's own framing and was not kept. Winch's own reply to the charge was not read. |
| N10 | The only 20th-century thinker who set off two revolutions | SEP `wittgenstein`; IEP | **unverifiable** as worded | Not used. SEP's "two commonly recognized stages" and its remark that the division "has been questioned" are reflected in the new comparison table's caption. |
| N11 | Returned to philosophy in the 1930s | SEP `wittgenstein`; IEP | **corrected** | 1929 (the essay already had it). |
| N12 | Comparison table of the two phases | — | two cells **corrected** | Kept as a table. "Correspondence with physical facts" became the shared logical form of proposition and possible situation; "delimiting the scientifically sayable" became clarification and the limit between saying and showing. |

## Re-check of weakly sourced points (2026-11-14, second pass)

| Point | Source now read | Verdict | Action in the essay |
| :-- | :-- | :-- | :-- |
| Russell's barber (1918) | Russell, "The Philosophy of Logical Atomism", Lecture VII, *The Monist* 29 (1919), pp. 354–355 ([archive.org](https://archive.org/details/sim_monist_1919-07_29_3)) | **corrected** | Russell calls it a form suggested to him "which was not valid"; the essay now says so. |
| Russell's acknowledgement of Wittgenstein (1918) | *The Monist* 28 (1918), p. 495 ([archive.org](https://archive.org/details/sim_monist_1918-10_28_4)) | confirmed | none |
| Russell, "most exciting intellectual adventures" | Russell, "Ludwig Wittgenstein", *Mind* 60 (1951), p. 298 ([scan](https://sites.ualberta.ca/~francisp/NewPhil448/RussellWittObituary1951.pdf)) | confirmed | none |
| Strachey 1965 | [OUP record](https://academic.oup.com/comjnl/article/7/4/313/354243): *Computer Journal* 7(4), p. 313 | data confirmed; wording of the letter still second-hand | none |
| Presburger | Stansifer's translation, Cornell TR84-639 ([PDF](https://cs.fit.edu/~ryan/papers/presburger.pdf)) | **corrected** | Warsaw 1929, proceedings 1930; integers, not naturals; he proved completeness, and decidability follows from the method. |
| Wang 1961, Berger 1966; tilings and Turing machines | Robinson, *Inventiones math.* 12 (1971), pp. 177–178, 209 ([scan](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0012/LOG_0023.pdf)) | confirmed | none |
| Nakashima | Yamada, *IEEJ Trans. FM* 124 (2004) ([J-STAGE](https://www.jstage.jst.go.jp/article/ieejfms/124/8/124_8_720/_article)); IPSJ museum | **corrected** | Papers from 1934 (not 1935) to 1936. |
| Shannon's thesis | Crossref: *Trans. AIEE* 57 (1938), 713–723; MIT DSpace dates the degree 1940 | 1938 confirmed; "1937, aged 21" **not supported** | Date and age removed; only the 1938 publication kept. |
| MYCIN's rules | Buchanan & Shortliffe (1984), pp. 72, 79, 697 ([Columbia](https://people.dbmi.columbia.edu/shortliffe/Buchanan-Shortliffe-1984/)) | confirmed | none |
| Logic Theorist, 38 of 52 | Newell, Shaw & Simon, *Psychological Review* 65 (1958), p. 155 | confirmed | Exact count added. |
| McCulloch & Pitts and Carnap | the 1943 paper, p. 118 | confirmed | none |
| Firth 1957 | Firth, "A Synopsis of Linguistic Theory", p. 11 ([scan](https://languagelog.ldc.upenn.edu/myl/Firth1957.pdf)) | confirmed | The adjacent sentence citing Wittgenstein restored. (The original ends with an exclamation mark; the Greek rendering does not.) |
| Masterman | Sowa, *Computational Linguistics* 32 (2006); Léon, *HEL* 29 (2007) | confirmed; CLRU founded 1955 (Léon; Sowa: "late 1950s") | «το 1955» |
| Turing on falling bridges (1939) | Matthíasson, *BJHP* 29 (2021); Vanrie (2024) | exchange confirmed; page in Diamond's *LFM* not seen | none |
| Turing 1944–45 on Wittgenstein's lectures | Turing typescript AMT/C12 p. 6, as quoted by Floyd; Floyd's chapter (Elsevier 2013) exists | confirmed | Floyd's chapter added to the sources. |
| Rosser 1936 | Crossref, *JSL* 1(3), 87–91 | confirmed | Added to the sources. |
| Winch 1958 | Routledge page; SEP `understanding` §5.1 | confirmed | Publisher added. |
| Geertz, "my master" | still only snippets | **still weak** | Sentence removed. |
| Rosch & Mervis; the bird example | *Cognitive Psychology* 7 (1975), pp. 574–575 (no birds); Rosch, *JEP: General* 104 (1975) for birds | **corrected** | Bird example attributed to Rosch's other 1975 paper; robin instead of sparrow. |
| Rossi-Landi | Routledge table of contents; Stern, *NDPR* 2003 | confirmed | none |
| Dummett and §62 | Dummett, *Frege: Philosophy of Mathematics* (1991), p. 111, quoted in SEP `analysis` | **corrected** (source) | The paragraph of the *Grundlagen* named; both Dummett books in the sources. |
| Floyd & Putnam 2000; Bays 2004 | PDC records; Lampert (2006); Plebani | data confirmed; Bays's argument known only from another paper | none |
| Adorno on Tractatus 7 | *Philosophy Now* 19; a transcription citing pp. 100–102 | **still weak** (page) | Kept; reading the book would close this. |
| Drury on Hegel | Malcolm, *LRB* 3/21 (1981) | wording confirmed; page in Rhees (ed.) not seen | none |
| *Culture and Value*, 1931 list | German text (LWP, *Vermischte Bemerkungen*); CV (1980), p. 19 | confirmed | none |
| Harris & Unnsteinsson | University of Iceland record: *BJHP* 26(2) (2018), 371–395 | confirmed | Full reference restored. |
| Dennett under Ryle | *Filozofia* 79 (2024) obituary | confirmed | none |
| Wittgenstein and the USSR, 1935 | Moran, *NLR* I/73 (1972), quoting von Wright | confirmed | none |

## Additions decided by the owner (2026-11-14)

| Topic | Sources | Verdict | Notes |
| :-- | :-- | :-- | :-- |
| Boethius | SEP `boethius` | confirmed | SEP gives c. 475–7 to 526?; the essay uses «περ. 475/477–526». |
| al-Khwārizmī (algebra, algorithm) | MacTutor `Al-Khwarizmi` | confirmed | c. 780–850; *al-jabr* (c. 830) and *Algoritmi*. |
| al-Fārābī, Avicenna; reception in the West | SEP `al-farabi`, `arabic-islamic-language`, `ibn-sina-logic`, `arabic-islamic-influence` | confirmed | The text says the innovative parts did not reach the Latin West, as SEP does. al-Fārābī dated c. 870–950 per SEP `al-farabi`. |
| Byzantine logic | SEP `byzantine-philosophy` | confirmed; sources thin | Stated as thin in the text. |
| Jacquard loom (1801) and Babbage | SEP `computing-history`; MacTutor `Babbage`; Menabrea/Lovelace (1843), [fourmilab transcription](https://www.fourmilab.ch/babbage/sketch.html) | confirmed | Punched cards controlling hooks/threads; Babbage's conditional branching of cards. |
| Lovelace: Notes, Note G, music, "no pretensions whatever to originate anything" | the 1843 text (fourmilab); MacTutor `Lovelace` | confirmed | Turing's 1950 quotation omits "whatever"; the essay follows Lovelace. |
| Lovelace as "first programmer" | MacTutor; Oxford Mathematics; Rojas, *IEEE Annals* 43 (2021); Hollings, Martin & Rice, *CACM* 67 (2024) | **contested** | «Ερμηνευτική σημείωση». |
| Turing 1950 | the paper (*Mind* 59) | confirmed | Prediction, objections and the "polite convention" from the text. Page range 433–460 from memory. |
| Whether passing the test shows thinking | SEP `turing-test` (Block's "Blockhead") | **contested** | Stated as debated. |
| Searle 1980 | the paper (BBS 3, 417–457; penultimate draft read); SEP `chinese-room` | confirmed; replies **contested** | «Ερμηνευτική σημείωση». Bender & Koller cite Searle explicitly. |
| Spinoza and the title | Churchill (2009): Moore proposed the Latin title; the Spinoza allusion only via Wikipedia citing Monk | Moore confirmed; allusion **weak** | Worded as «θυμίζει», not as an intended allusion. |
| Form of the Tractatus and Spinoza's *Ethics* | Churchill (2009) | confirmed (one source) | Stated without claiming influence. Cut on 2026-11-15 (review for length); no longer in the essay. |
| 6.45 *sub specie aeterni*; Notebooks 7.10.16 | LWP German texts; Spinoza, *Ethica* V | confirmed | "Probably through Schopenhauer" (Somavilla, ALWS) stated as the scholars' view. The Notebooks entry was cut on 2026-11-15 (review for length); 6.45 and the Schopenhauer remark stay. |
| Moore: Norway 1914; 1929 doctorate; lectures 1930–33 | LWP (Notes dictated to Moore); Moore, *Mind* 63 (1954), pp. 1–2 | confirmed | The "work of genius" sentence survives only in recollections (Braithwaite and others) in different wordings: the essay says so and does not quote it. On 2026-11-15 (review for length) the mention was cut altogether. |
| Moore and *On Certainty* | IEP `witt-epi` | confirmed | none |
| Mauthner: ladder, 4.0031 | Mauthner, *Beiträge* I (1901), pp. 1–2 (archive.org); LWP German text of 4.0031 | confirmed | none |
| Source of the ladder; Wittgenstein's debt to Mauthner | Gakis and Nájera (ALWS); Le Rider, *ÖZG* 23 (2012); Janik & Toulmin (1973) | **contested** | «Ερμηνευτική σημείωση». |
| Turing at Bletchley Park (Enigma, *Bombes*) and ACE (1945) | SEP `turing`; MacTutor `Turing` | confirmed | Polish precursor noted. |
| Cook (1971), Levin (1973) and P vs NP | SEP `computational-complexity` | confirmed | SAT (propositional truth tables) as the starting point (Cook–Levin theorem). |
| Ryle, *The Concept of Mind* (1949), "ghost in the machine" | SEP `ryle` | confirmed | Added to section 10. |
| 19th–20th c. epistemology in section 3 (Hegel, Comte, Mill 1843, Peirce & James pragmatism, Nietzsche perspectivism, Husserl phenomenology, Foucault power/knowledge, Gettier 1963) | SEP `hegel`, `comte`, `mill`, `pragmatism`, `nietzsche`, `husserl`, `foucault`, `knowledge-analysis` | confirmed | Added to section 3. Shortened on 2026-11-15 (review for length): Hegel, Comte, Nietzsche and Foucault cut from section 3 (Hegel stays in section 10); Mill, the pragmatists, Husserl, Russell/Moore and Gettier kept. |
| Popper, *Logik der Forschung* (1934/1935), falsifiability | SEP `popper` | confirmed | Added to section 6 (after Vienna Circle). |
| Quine, "Two Dogmas" (1951), "Epistemology Naturalized" (1969) | SEP `quine`, `epistemology-naturalized` | confirmed | Added to section 10. On 2026-11-15 (review for length) "Epistemology Naturalized" was cut, with its source entry; "Two Dogmas" kept. |
| Dewey (pragmatism), Piaget (genetic epistemology), Vygotsky (*Thought and Language*, 1934), Bruner & 1950s cognitive revolution | SEP `dewey`, `cognitive-science` | confirmed | Added to sections 3, 10 and 11. On 2026-11-15 (review for length) Piaget was cut from section 10 and Vygotsky reduced to one sentence, presented as a parallel idea, not an influence. |
| AlphaGo (2016), Transformer / attention (Vaswani et al. 2017), AlphaFold (2020, Nobel 2024), AlphaGeometry & AlphaProof / Lean (2024–2025), IMO 2025 gold & 2025–2026 research problems (Erdős, fluid dynamics, particle physics) | Silver et al., *Nature* 529 (2016); Vaswani et al., *NeurIPS* 30 (2017); Jumper et al., *Nature* 596 (2021); Trinh et al., *Nature* 625 (2024); Hubert et al., *Nature* (2025) | confirmed | Added to sections 11.4 and 11.6. |
| Timeline and glossary | the essay itself | — | No new claims; every date and definition is stated in the body. |

## Figure credits of the essay (2026-11-15)

Each photo's author and licence checked against its Wikimedia Commons page
(by SHA-1 where our copy is the original file, otherwise by subject and
proportions; our copies of the Leibniz and Lovelace files are scaled down).

| Figure | Commons file | Verdict | Action |
| :-- | :-- | :-- | :-- |
| Leibniz's calculating machine | [Leibnitzrechenmaschine.jpg](https://commons.wikimedia.org/wiki/File:Leibnitzrechenmaschine.jpg): Kolossos, CC BY-SA 3.0 | confirmed | none |
| Jacquard punched cards (old photo, Manchester) | [Jacquard.loom.cards.jpg](https://commons.wikimedia.org/wiki/File:Jacquard.loom.cards.jpg): George H. Williams (en.wikipedia user Ghw), public domain; 249 × 333 px, no larger version | **corrected** (licence was given as CC BY-SA 3.0) | Photo replaced: too small for print. |
| Jacquard loom (new photo, Sliven) | [Hand-driven-jacquard-loom.jpg](https://commons.wikimedia.org/wiki/File:Hand-driven-jacquard-loom.jpg): Edal Anton Lefterov, CC BY-SA 3.0; Austrian hand-driven loom, end of the 19th century, National Museum of the Textile Industry, Sliven | confirmed | The 960 px copy served by Commons is used (the original is 3.9 MB). |
| Babbage's Analytical Engine (mill) | [Babbages Analytical Engine, 1834-1871. (9660574685).jpg](https://commons.wikimedia.org/wiki/File:Babbages_Analytical_Engine,_1834-1871._(9660574685).jpg): Science Museum, London collection, CC BY-SA 2.0 | **corrected** (licence was given as CC BY 4.0) | Caption corrected. |
| Lovelace, Note G diagram | [Diagram for the computation of Bernoulli numbers.jpg](https://commons.wikimedia.org/wiki/File:Diagram_for_the_computation_of_Bernoulli_numbers.jpg): public domain | confirmed | none |
| Portrait of Wittgenstein, 1930 (added 2026-11-15) | [Ludwig Wittgenstein.jpg](https://commons.wikimedia.org/wiki/File:Ludwig_Wittgenstein.jpg): Moritz Nähr (1859–1945), Austrian National Library, Pf 42.805 : C (1); `PD-old-auto-expired` (author died 1945) | confirmed (wikitext read) | Commons' 960 px copy used; caption names photographer, holder and licence. |
| Four diagrams added 2026-11-15 (Euler circles, Venn/Boole, halting proof, family resemblances) | drawn for the essay | — | Euler circles dated to Euler (1768), Venn's diagrams to 1880; the family-resemblance grid is marked as a simplified example after *PI* §§66–67. |

## Review for length and clarity (2026-11-15)

Corrections made during the section-by-section review (TODO item 4.3).

| Claim | Source | Verdict | Action |
| :-- | :-- | :-- | :-- |
| The stopped clock given as Gettier's example (section 3) | Russell, *Human Knowledge: Its Scope and Limits* (1948), pp. 170–171, as cited in [Wikipedia, "Gettier problem"](https://en.wikipedia.org/wiki/Gettier_problem) and [OpenStax, *Introduction to Philosophy* 7.2](https://openstax.org/books/introduction-philosophy/pages/7-2-knowledge); Gettier's own cases are Smith/Jones (ten coins) and Ford/Barcelona | **corrected** | The clock is now credited to Russell (1948) as an earlier example of the same point. |
| «γνωστικισμός» for cognitivism (section 11) | Greek usage: «γνωστικισμός» is Gnosticism | **corrected** | «γνωσιακή ψυχολογία». |
| Lean as «άμεσο απόγονο» of Frege, the *Principia* and Hilbert's programme (section 11) | Lean is based on dependent type theory (calculus of inductive constructions), which descends from Russell's type theory through Church and Martin-Löf; not searched separately | **weakened** | «απόγονο της παράδοσης που ξεκινά από την Εννοιογραφία του Frege και τη θεωρία των τύπων των *Principia*». |
| Fermat's Last Theorem: first complete computer-checked proof in Lean by a Claude research model, 11 days (section 11) | [Anthropic, 4 Sep 2026](https://www.anthropic.com/research/formalizing-fermats-last-theorem): "roughly comparable to Claude Fable 5.1"; only Lean's three standard axioms; comparator against Mathlib's statement | confirmed (company's own report; Lean-checked) | Added to section 11, timeline and sources. |
| Fable 5.2: 1,000 agents re-formalized FLT in 30 hours (section 11) | [Anthropic, 9 Nov 2026, edited 11 Nov](https://www.anthropic.com/claude-fable-and-mythos-5-2), footnote 4: started from 60 statements, a sketch and 47 lemmas of the first formalization | reported by the company only | Stated as «η εταιρεία ανέφερε», «ξεκινώντας από ορισμένα λήμματα της πρώτης». |
| Fable 5.2: two open problems in theoretical physics (Hawking-Page at weak coupling; limit of a quantum-gravity technique) | Same announcement; preprints [Hexagon 2611.00175v1](https://hexagonmath.org/2611.00175v1) ("an internal Claude research model, prompted by a physicist"; 42 pp.) and Hexagon 2611.00174v1 (not read) | reported by the company; not peer-reviewed | Stated as reported, «δεν έχουν ακόμη κριθεί από άλλους ειδικούς». Note: arXiv 2611.00175 is an unrelated paper. |
| Aaronson–Ambainis conjecture proved (PSI, Turturean and Halverson, internal Claude model) | [Aaronson, *Shtetl-Optimized*, 8 Nov 2026](https://scottaaronson.blog/?p=10295); expositions [Blanc et al., arXiv 2611.11626](https://arxiv.org/abs/2611.11626), [arXiv 2611.12795](https://arxiv.org/html/2611.12795) | confirmed in outline; Lean certificate; community review ongoing | Added; the model is not named, as in the sources. |
| Not used: a 42-train timetabling result beating MIPLIB by 2.6%; Fable 5.2 named for Aaronson–Ambainis | not found in any primary source | unsupported | Left out. |
| Deep Blue "neither expert rules nor neural networks" (section 11) | Deep Blue's evaluation function was tuned with grandmaster input | **weakened** | Now says only that it did not use neural networks. |
| Kant: causality listed with space and time as «η μορφή» (section 3) | Kant, *KrV*: space and time are forms of intuition, causality a category of the understanding | **corrected** | «τις μορφές (τον χώρο και τον χρόνο) και τις βασικές έννοιες (όπως η αιτιότητα)». |
| Augustine (354–430): Platonist, read through the Neoplatonists; little Aristotle (section 2) | SEP `augustine` | confirmed (standard account; not searched in this session) | Added at the owner's request. |
| *Philosophical Investigations* §1 opens with *Confessions* I.8 on learning words by naming and pointing (section 10) | PI §1 (German text, LWP) | confirmed (well known; quotation not repeated) | Added. |
| Ibn Rushd (Averroes, 1126–1198), Córdoba; commentaries on nearly all of Aristotle, Latin translations in the 13th c., «the Commentator» (section 2) | SEP `ibn-rushd`; SEP `arabic-islamic-influence` | confirmed (standard account; not searched in this session) | Added; the sentence on Latin reception now names his commentaries next to Avicenna. |
| Aquinas (c. 1225–1274): commentaries on *De interpretatione* and *Posterior Analytics*; William of Moerbeke's Greek translations; moderate realism on universals (section 2) | SEP `aquinas`, `medieval-problem-universals` | confirmed (standard account; not searched in this session) | Added. Moerbeke named only as a translator, not as working at Aquinas's request (contested). |

## Open for the essay

- Standard life dates were not checked one by one.
- Still weak: the page of Turing's bridge remark in Diamond's *LFM*; the wording of Strachey's letter; Adorno's page; Drury's page; Bays's 2004 argument; Moore's examiner's report.
- Turing's 1950 page range (433–460) and Moore's second 1954 page range are from memory.
- The Greek renderings of Tractatus and *Investigations* sentences are the essay's own; they were not compared with the published Greek translations (see C1).
