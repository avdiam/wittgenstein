# Cross-check plan: analysis vs. outside sources

Status: **tiers A and D checked online (2026-11-14) and the approved corrections applied.** Tiers B, C and E not started. Results are at the end of this file.

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

---

# Results — tiers A and D (checked 2026-11-14)

Verdicts: **confirmed** (sources agree with the analysis), **corrected** (the
analysis needs a change), **contested** (respectable sources disagree),
**unverifiable** (not settled in this pass). "Line" is the line number in
`TRACTATUS_LOGICO_PHILOSOPHICUS_ANALYSIS_1-7.md` at commit `1b600c8`.
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
