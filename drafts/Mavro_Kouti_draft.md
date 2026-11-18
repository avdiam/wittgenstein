# Draft: «Το "μαύρο κουτί"» (essay, section 11) — not applied

Proposed on 2026-11-19 at the owner's request; saved, not applied (owner,
2026-11-19). Nothing here is in `Logiki_Glossa_Michanes.md` yet. Before
writing: check Π1–Π7 and the Cammarata wording, record each in
`CROSSCHECK_DONE.md`, then decide the open question at the end.

## Why

The essay says that learning adjusts the weights (perceptron, section 11;
language models, «ρυθμίζει ελάχιστα μερικά δισεκατομμύρια αριθμούς») and that
words are points in a space (`word_space.svg`). It does not say that what a
model knows is spread over its weights with no readable rule, why such
networks are called "black boxes", or that a field (mechanistic
interpretability) tries to open them.

## Placement

Section 11, a new `###` after «Τα νευρωνικά δίκτυα και τα γλωσσικά μοντέλα»
(after its Ερμηνευτική σημείωση on Bender and Koller) and before «Τα όρια».
A `###` needs no entry in `tab_for()`.

## Proposed text

### Το «μαύρο κουτί»

Πού βρίσκονται λοιπόν όσα «ξέρει» ένα γλωσσικό μοντέλο; Όχι σε κάποιον κατάλογο από γεγονότα ή κανόνες. Ένα έμπειρο σύστημα όπως το MYCIN μπορούσε να δείξει ποιους κανόνες χρησιμοποίησε για να προτείνει μια θεραπεία [Π1]. Ένα γλωσσικό μοντέλο δεν έχει κανόνες να δείξει: ό,τι έμαθε είναι μοιρασμένο στα δισεκατομμύρια βάρη του, και κάθε απάντηση βγαίνει από πράξεις με όλους μαζί αυτούς τους αριθμούς. Μπορούμε να διαβάσουμε κάθε αριθμό χωριστά, και να δούμε πότε «ανάβει» κάθε τεχνητός νευρώνας, δηλαδή κάθε μονάδα του δικτύου που παίρνει μεγάλη ή μικρή τιμή ανάλογα με όσα δέχεται. Από τους αριθμούς αυτούς όμως δεν φαίνεται γιατί το μοντέλο έδωσε τη συγκεκριμένη απάντηση. Γι' αυτό τα δίκτυα αυτά ονομάζονται συχνά «μαύρα κουτιά»: ξέρουμε τι μπαίνει και τι βγαίνει, όχι τι γίνεται ανάμεσα.

Η προσπάθεια να ανοιχτεί το κουτί ονομάζεται ερμηνευσιμότητα (*interpretability*). Ο Chris Olah και οι συνεργάτες του (2020) εξέτασαν έναν έναν τους νευρώνες ενός δικτύου που αναγνωρίζει εικόνες. Βρήκαν πολλούς με καθαρή δουλειά: νευρώνες που ανιχνεύουν καμπύλες, άλλους που τις συνδυάζουν σε κύκλους, και πιο πάνω νευρώνες για τροχούς ή για ολόκληρα αυτοκίνητα [Π2]. Βρήκαν όμως και νευρώνες που αντιδρούν σε πράγματα φαινομενικά άσχετα· ένας από αυτούς άναβε για πρόσωπα γάτας και για το μπροστινό μέρος αυτοκινήτων [Π2].

Η εξήγηση που επικράτησε διατυπώθηκε το 2022 (Nelson Elhage και συνεργάτες) και λέγεται υπέρθεση (*superposition*) [Π3]: το δίκτυο έχει να αποθηκεύσει περισσότερες έννοιες από όσους νευρώνες διαθέτει, γι' αυτό κάθε έννοια απλώνεται σε πολλούς νευρώνες και κάθε νευρώνας συμμετέχει σε πολλές έννοιες. Αν αυτό ισχύει, οι νευρώνες δεν είναι οι πραγματικές μονάδες του δικτύου, και πρέπει πρώτα να «ξεμπλεχτούν». Αυτό επιχείρησαν ερευνητές της Anthropic (2023, 2024) με μια μέθοδο που ξαναγράφει τη δραστηριότητα των νευρώνων με ένα πολύ μεγαλύτερο «λεξικό» από χαρακτηριστικά, καθένα από τα οποία αντιστοιχεί κατά κανόνα σε μία έννοια [Π4]. Σε ένα μοντέλο Claude βρήκαν, για παράδειγμα, ένα χαρακτηριστικό για τη γέφυρα Golden Gate του Σαν Φρανσίσκο: όταν το ενίσχυσαν τεχνητά, το μοντέλο έφερνε τη γέφυρα σε κάθε συζήτηση, και έλεγε ακόμη ότι είναι το ίδιο η γέφυρα [Π5]. Το 2025 η ίδια ομάδα ακολούθησε μέσα σε ένα μοντέλο τη διαδρομή μιας απάντησης: στην ερώτηση ποια είναι η πρωτεύουσα της πολιτείας όπου βρίσκεται το Ντάλας, το μοντέλο περνούσε εσωτερικά από το «Τέξας» πριν απαντήσει «Όστιν» [Π6].

Τα αποτελέσματα αυτά δεν σημαίνουν ότι το κουτί άνοιξε. Οι ίδιοι οι ερευνητές γράφουν ότι η μέθοδός τους έδωσε ικανοποιητική εξήγηση για περίπου ένα στα τέσσερα παραδείγματα που δοκίμασαν [Π7], και η εφαρμογή της σε μοντέλα με εκατοντάδες δισεκατομμύρια βάρη μόλις αρχίζει.

> **Ερμηνευτική σημείωση.** Το πόσο «μπλεγμένοι» είναι πράγματι οι νευρώνες αμφισβητείται. Η υπέρθεση είναι η συνηθισμένη εξήγηση, και πάνω της στηρίζονται οι μέθοδοι του «λεξικού». Ο Nick Cammarata, ένας από τους συγγραφείς της εργασίας του 2020, υποστήριξε το 2026, σε δοκίμιο που ο ίδιος χαρακτηρίζει άτυπο και υπόθεση εργασίας, ότι οι περισσότεροι νευρώνες έχουν μία κύρια δουλειά και ότι η φαινομενική ανάμειξη οφείλεται κυρίως σε ατελή εργαλεία και εξηγήσεις· κατά τον ίδιο, η υπέρθεση έπρεπε να είναι η τελευταία εξήγηση που δοκιμάζουμε, όχι η πρώτη. Γράφει επίσης ότι ένας νευρώνας μοιάζει περισσότερο με ρήμα παρά με ουσιαστικό: τον ορίζει αυτό που κάνει στην πληροφορία που περνά από μέσα του. Η άποψή του δεν έχει ακόμη κριθεί από την ερευνητική κοινότητα.

**[Optional closing paragraph: the link to the *Tractatus*. Open question below.]**

Η διαφωνία αυτή θυμίζει, από απόσταση, μια φράση του *Tractatus* που είδαμε στην ενότητα 5: ότι η φαινομενική λογική μορφή μιας πρότασης δεν είναι κατ' ανάγκην η πραγματική της (4.0031). Κατά την υπόθεση της υπέρθεσης, οι νευρώνες είναι η φαινομενική μορφή και οι έννοιες η πραγματική, που βρίσκεται μόνο με ανάλυση· κατά τον Cammarata, οι δύο ως επί το πλείστον συμπίπτουν. Η αναλογία έχει όρια. Η λογική μορφή του *Tractatus* δεν ανακαλύπτεται με πειράματα, και είναι κοινή σε κάθε γλώσσα· τα μοτίβα ενός δικτύου είναι μαθημένα από δεδομένα και διαφέρουν από μοντέλο σε μοντέλο. Και η εικόνα του νευρώνα ως ρήματος θυμίζει περισσότερο τη σημασία ως χρήση των *Φιλοσοφικών Ερευνών* παρά τα ονόματα του *Tractatus*.

## Checks before writing

| # | Claim | Source to check |
| :-: | :-- | :-- |
| Π1 | MYCIN could explain which rules it used | Buchanan & Shortliffe 1984 (already in the bibliography) |
| Π2 | Curves → circles → wheels/cars; neuron 4e:55 (cat faces, car fronts) | Olah et al., «Zoom In: An Introduction to Circuits», *Distill* 2020 |
| Π3 | Superposition, 2022 | Elhage et al., «Toy Models of Superposition», 2022 |
| Π4 | Dictionary of features (sparse autoencoders) | Bricken et al., «Towards Monosemanticity», 2023; Templeton et al., «Scaling Monosemanticity», 2024 |
| Π5 | Golden Gate feature; amplified, the model said it was the bridge | Templeton et al. 2024; Anthropic's announcement (May 2024) |
| Π6 | Dallas → Texas → Austin | Lindsey et al., «On the Biology of a Large Language Model», 2025 |
| Π7 | Satisfying insight for "about a quarter" of the prompts | the same, limitations section |
| — | Cammarata 2026: wording, quotations, date | the text version `essay.md` linked from the page |

Follow-on entries: the five works in «Πρωτότυπες εργασίες»; glossary
«Ερμηνευσιμότητα» and «Υπέρθεση»; timeline rows 2020, 2022, 2024, 2025;
possibly a «Μαύρο κουτί» glossary entry.

## Notes on the Goodfire essay (read 2026-11-19 through a fetch agent)

- Nick Cammarata (Goodfire), «Neural Networks Are Already Clean. An informal
  research essay and working hypothesis about neural networks»,
  https://already-clean.goodfire.com/ ; contributions from Curt Tigges and
  Tarun Gogineni. No publication date in the text read; a footnote says
  "Revised October 30, 2026". A text version (`essay.md`) and a PDF are linked
  from the page.
- Read word for word: introduction, the InceptionV1 sections, «Recursive
  Generalization», «Superposition», and from «What Dictionaries Learn» to the
  Miyazaki example. Read only as a summary: roughly the middle third (image
  models). Not read: the appendices and references.
- Claims: "superposition was the wrong explanation for InceptionV1"; "I now
  think I was making superposition the null hypothesis when it should have
  been the last hypothesis"; a neuron is "better understood as a verb than a
  noun"; recursive generalization ("iy" → "diy" → "do it yourself");
  neuron 4e:55 read as a "V" detector, later called "too strong" by the author
  (footnote, revised 2026-10-30); "roughly 90% of neuron poles have one main
  job" in Qwen3-32B, with the warning that one score "should be taken as a
  broad pointer"; attribution graph of Kimi K3. No mention of Wittgenstein or
  logical form.

## The analysis given to the owner (2026-11-19)

- Touches the *Tractatus* by analogy: shared structure between picture and
  pictured (2.15–2.18; 4.014, score / groove / sound waves; 4.0141, the "law of
  projection"); and, most closely, apparent and real form (4.0031):
  superposition says the neurons are the apparent units and the concepts the
  real ones; Cammarata says they coincide.
- Breaks: logical form is not empirical, cannot be depicted, only shown
  (2.172, 4.12), is common to every language and concerns possibility;
  activations are graded, learned, model-specific, found by experiment.
  Researchers describe a network from outside (cf. Tarski's metalanguage),
  so "cannot be said" is not contradicted.
- Cammarata is closer to the late Wittgenstein: "verb, not noun" ~ meaning as
  use, tools (§11); recursive offshoots ~ family resemblances (§§66–67), with
  the caution that his "V-shape" reading seeks a common element.
- No scholar found who draws the link: if written, it is the essay's own
  analogy, worded «θυμίζει».

## Open question for the owner

The optional closing paragraph:

- **A (recommended):** keep it as worded, with its limits stated.
- **B:** leave it out; the subsection stays on the AI side.
- **C:** keep only the last sentence (verb, meaning as use), without 4.0031.
