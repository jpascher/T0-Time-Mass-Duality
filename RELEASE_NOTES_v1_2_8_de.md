# Release Notes — v1.2.8 (August 2026)

**DOI:** *(wird bei Veröffentlichung eingetragen)* — ersetzt v1.2.7 ([10.5281/zenodo.21628364](https://doi.org/10.5281/zenodo.21628364))

Laufende Korrekturen: **[2/pdf/190_T0_Korrekturen_De.pdf](2/pdf/190_T0_Korrekturen_De.pdf)**  
Änderungsprotokoll: **[000_FFGFT_Changelog_De.md](000_FFGFT_Changelog_De.md)**  
A-Serie-Protokoll: **[A_Serie_Export/A_SERIE_CHANGELOG.md](A_Serie_Export/A_SERIE_CHANGELOG.md)**

---

**FFGFT — Fraktale Feldgeometrische Fundamentaltheorie** zeigt:
Alle Konstanten des Standardmodells folgen aus einem einzigen
dimensionslosen Parameter **ξ = 4/30000** auf einem kompakten
4D-Torus T⁴. Die Grundrelation ist **T̃ · m = 1** — intrinsische Zeit
und Masse sind invers gekoppelt.

**Autor:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Neu in v1.2.8

Zwei Dokumente des kosmologisch-geometrischen Blocks überarbeitet.
Keine Änderung an der A-Serie, keine Änderung an ξ oder an einer
Ableitungskette.

### Dok. 314 „Gitter im Hilbertraum" — erweitert (DE 26 / EN 25 S.)

Das Dokument ist jetzt **eigenständig**: sämtliche Rückbezüge auf
frühere Fassungen sind entfernt. Die Änderungshistorie lebt in der
Git-Historie und im Changelog, nicht im Dokument.

**Die Störungsrechnung ist ausgeführt** (Kap. J.3, Status von „offen"
auf **[K]**). Multiplettgrößen folgen den **Irrep-Dimensionen** der
respektierten Symmetrie, nicht den Orbits:

| Störung respektiert | Aufspaltung der 24 |
|---|---|
| volle Aut(D4) | 9 + 8 + 4 + 2 + 1 |
| Trialität (Z₃) | 8×1 + 8×2 |
| nur −1 / nichts | 24×1 |

Grund: Jede ortsabhängige Störung bricht die **Translations**invarianz
— und die trug die 24er-Entartung, nicht die Punktsymmetrie. Z₃ ist
abelsch, alle Irreps eindimensional; die Dubletts sind die
antiunitäre χ₁/χ₂-Paarung. Je drei unabhängige Seeds pro
Symmetrieklasse, Ergebnis seedunabhängig.

**Neues Kapitel D1 „Zeit aus dem Massenkreis" [K].** T_k = 2πR₄/k₄
ist eine **Bogenlänge**, also ein Ort-Intervall — λ₄·m = 2π ist die
**de-Broglie-Relation** auf der Massenrichtung, keine Zeitaussage.
Dauer entsteht erst in der ausgerollten Koordinate
t = w·2πR₄ + x₄ (Umlaufzahl plus Ort auf dem Zyklus). Drei Aussagen
in drei Richtungen:

| Ablesung | Relation | Gleichheit bei |
|---|---|---|
| Ort (de Broglie) | = 2π | immer |
| Zeit, bewegte Mode | = 2π/γ ≤ 2π | p_Raum = 0 |
| Massengemisch (Jensen) | ≥ 2π | scharfe Schale |

Exakt wird die Relation nur für die **ruhende, scharfe** Mode; Bewegung
drückt das Produkt herunter, Massenstreuung hebt es an.

**Neues Kapitel D2 „Die Schließungsgabelung ist spektral unsichtbar"
[K].** Im eingerollten Zustand gibt es **keine fraktalen Korrekturen**:
Eindeutigkeit der Mode erzwingt k₄ ∈ ℤ, eine Wicklungszahl ist
topologisch und hat keinen Platz für 1/75. Korrekturen brauchen
Akkumulation, und akkumulieren kann nur ein durchlaufener Weg. Die
naheliegende Twist-Lesart (Scherk–Schwarz, k₄ → k₄ + 1/75) ist damit
**falsch**. Folge: die Fälle A/B/C aus Dok. 313/295 lassen das
Modenspektrum unberührt, und die Kapitel E–H sind
**fallunabhängig**.

**Kapitel J neu gefasst: „Was hier noch nackt ist — und was nicht"
[K].** D_f und K_frak sind **verschiedene Dinge** (Dok. 133):

| Größe | Charakter | Wirkung |
|---|---|---|
| D_f^Raum = 3 − ξ | lokal | 6,67 × 10⁻⁵ |
| K_frak = 1 − 100ξ | kumulativ (RG-Lauf) | 1,33 × 10⁻² |

Verhältnis exakt 200. Zwei Klarstellungen: der Korpus kennt keine
Größe D_f = 4 − ξ (Dok. 133 definiert die **räumliche** Dimension
3 − ξ; auch der Exponent 3/2 in K_frak^{3/2} ist die halbe
**Raum**dimension), und O(100ξ) scheidet als Störungsstärke aus, weil
eine kumulative Größe nicht auf einen lokalen Operator gehört. Die
Störung liegt damit **zwei Größenordnungen unter** dem, was eine
Abschätzung über K_frak ergäbe. **Bilanz: nackt sind nur die
SI-Absolutwerte, und zwar über den Anker, nicht über den Operator** —
Entartungen, Verhältnisse, Kongruenzen, Container sowie Casimir- und
Wärmekern-Verhältnisse sind nicht nackt, sondern korrekt.

**Verifikation:** `2/python/Dok314_Skripte/` — vier Skripte mit
README, alle Sollwerte als Assertions, deterministisch:
`d4_skript_1_spektrum_deformation.py` (Thetareihen, 24 = 12+12,
exakte Kreuzungskarte r = √2 und √3),
`d4_skript_2_trialitaet_orbifold_phasen.py` (|Aut(D4)| = 1152,
5 ∤ 1152, |det(1−A)| = 9, Zirkulant, Nennerspektrum {1,2,3,6} ohne
2/9, 24 = 4×6),
`d4_skript_3_schalen_casimir.py` (Schalensätze, Epstein-Zeta bei
s = −1/2 mit doppelter Verifikation, Wärmekern),
`d4_skript_4_stoerung_reziprozitaet.py` (Störungsmultipletts,
Reziprozität).

### Dok. 313 „Kein Anfang" — zwei Korrekturen, zwei Erweiterungen (DE 25 / EN 24 S.)

**Korrektur 1 (π gegen 2π).** Beim Kondensieren aus Dok. 295 war eine
Qualifikation verlorengegangen: 313 schrieb „eine Windung, die pro
**Umlauf um 2π** vorrücken sollte, rückt nur um **π·K_frak** vor" —
das mischt zwei Bezugsgrößen und liest sich wie ein Defekt von ~50 %,
während gleich darauf d = 1/75 steht. Dok. 295 hat die
**Halbdrehung**. Nach dem Wortlaut von 295 korrigiert, mit
Quellenangabe; der Übergang zu Umlauf-Einheiten ist jetzt explizit.

**Korrektur 2 (ggT).** „Die 75 fällt exakt heraus" war behauptet, nicht
begründet. Ergänzt: **ggT(74, 75) = 1**, also ist das kleinste n mit
n·74/75 ∈ ℤ genau n = 75 — die Schließung tritt nicht früher ein.

**Erweiterung 1 — Abschnitt F.4 „Reichweite: Gleichgewichte an anderen
Orten des Zyklus" [K].** Die übliche Rückwärtsextrapolation
T(z) = T₀(1+z) setzt **eine** durchgehende thermodynamische Kette
voraus — genau die grobkörnige Verkettung, die nach D(ii) offen ist.
In der Ortslesart ist eine frühe Epoche kein früherer Zustand
desselben Systems, sondern eine Stelle mit anderer lokaler Struktur
(kleinere Massen, langsamere Uhren) und einem eigenen, lokal
bestimmten Gleichgewicht. Der Korpus zeigt das an sich selbst: T₀ wird
nicht extrapoliert, sondern strukturell aus ξ gewonnen
(k_BT₀ = (16/9)ξ, Dok. 061). **Abgrenzung:** Die Ω_m*-Kette läuft über
ξ, H₀ und K_frak, nicht über adiabatische Rückrechnung, und ist
unberührt.

**Erweiterung 2 — „Welche Größen bleiben dann aussagekräftig?" [K].**
Kriterium dreiteilig: **keine Skalenbrücke, keine Dauer, gleiche
Ebene.**

| Klasse | Beispiele | Status |
|---|---|---|
| Zählungen | \|Aut(D4)\| = 1152, Kusszahl 24, 9 Fixpunkte | exakt; Sätze, keine Messungen |
| Verhältnisse gleicher Ebene | α, m_μ/m_e, Koide Q | belastbar; testbar auf 10⁻¹⁰ bis 10⁻⁵ |
| mit Skalenbrücke | E₀, G, H₀, T₀, absolute Massen | nur mit Anker; Verhältnisse daraus wieder frei (A040) |
| Zahl- und Dauergrößen | η, Fensterdauern, Zeitspannen | nicht übertragbar |

**Alle drei BBN-Observablen fallen in die unteren beiden Klassen —
auch Y_p:** Es hängt zwar an den dimensionslosen Größen Q/T_f und
t/τ_n, aber T_f ist **nicht gemessen** (folgt aus einer Ratengleichung
mit H, also aus dem kosmologischen Modell), und t/τ_n enthält eine
**Dauer**. Das Kürzungsargument ist eine **Implikation**, keine
Prüffläche. **Folge für die ⁷Li-Position:** Die Korpusbuchung
(Dok. 025/063, Nukleosynthese ohne feste Zeitschranke) bleibt
konsistent, ist aber **keine quantitative Vorhersage**. **Gegenprobe:**
Dieselbe Klassifikation trifft ΛCDM genauso — Dok. 267 hält bereits
fest: „keiner ist zirkelfrei". Die Klassifikation entlastet FFGFT
nicht, sie stellt beide Seiten unter dasselbe Kriterium.

**Verifikation:** `2/python/Dok313_Skripte/ffgft_bbn_skaleninvarianz.py`
— Skalenexponenten unter Massenskalierung (als Einheitenwechsel
eingeordnet), Y_p-Sensitivität, ξ-Drift als einzige verbleibende
Bruchstelle, parametrisiert nach p = dln(Q/T_f)/dln ξ. Ausdrücklich als
**Nicht-Befund** gebucht: G = ξ²/(4 m_char) (Dok. 012) und
α = ξE₀² (Dok. 011) sind aus ξ **abgeleitet**, keine unabhängigen
Skalen — ihre SI-Werte brauchen Verankerung, und Verankerung ist
Umrechnung, nicht Anpassung (A040, R72). Sie taugen daher nicht als
eigenständige Bruchstellen.

---

## Kein Registereintrag nötig

Dok. 313 und 314 sind **aktuelle** Dokumente desselben Zyklus; ihre
Korrekturen und Erweiterungen sind direkt eingearbeitet. Das
Korrekturregister (Dok. 190) nimmt ausschließlich Einträge auf, die
**ältere**, bereits ausgelieferte Dokumente präzisieren — hier ist
keines betroffen. Die Änderungshistorie steht im Changelog und in der
Git-Historie.

---

## Statistik (v1.2.8)

| | Anzahl |
|---|---|
| A-Serie-Dokumente (DE + EN) | 48 × 2 = 96 (unverändert) |
| überarbeitete Dokumente | 2 (313, 314) × 2 Sprachen |
| neue Prüfskripte | 2 (`d4_skript_4_…`, `ffgft_bbn_skaleninvarianz`) |
| neue READMEs | 1 (`python/Dok314_Skripte/README.md`) |
| Korrekturregister | K1–K7, R1–R73 |
