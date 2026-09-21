# FFGFT Changelog — laufend ab v1.3.4

**Grundlage:** Dok. 190 (Korrekturregister)  
**Archiv bis v1.3.3:** [`000_FFGFT_Changelog_De.md`](000_FFGFT_Changelog_De.md)

Neue Einträge werden hier oben eingefügt (neueste zuerst).

---
---

## 15. September 2026 — v1.4.0: Quantenmechanik ist deterministisch (QMB-Buch)
### QMB — *Quantenmechanik ist deterministisch / Quantum Mechanics is Deterministic* (De 107 S. / En 105 S.)

Narrativ-Buch zur geometrischen Lesart der Quantenmechanik durch FFGFT.
4 Teile, 15 Kapitel, 3 Anhänge. DOI: https://doi.org/10.5281/zenodo.22739112

**Hauptergebnisse:**
- Deterministischer Einzeldurchlauf: Alle Quanten-Logikbausteine (Gatter, Deutsch, Grover,
  Bell, Periodenfindung) auf PC in einem einzigen deterministischen Lauf realisierbar **[K]**
- PC schneller als QC — Ausnahme: QFT in Superposition (theoretischer Vorteil O((log N)³)) **[K]**
- Bijektive Zustandsbrücke (z,r,θ)↔(α,β) vollständig verifiziert **[K]**
- Mathematik-Analogie für Instantanität: T̃·m=1 als lokale Zwangsbedingung, kein Signal **[K]**
- CHSH-Auflösungsboden Δ_CHSH = ξ/(2π) ≈ 2×10⁻⁵ pro Messung **[K/S]**

**Klarstellungen (keine Korrekturen an bestehenden Dokumenten):**
- Frühere 40×-Determinismus-Meldung zurückgezogen (Stichproben-Artefakt)
- CHSH-Auflösungsboden ≠ kumulative Formel Dok. 022/147 (nicht vergleichbar)
- Weyl-Obstruktion gilt nicht für Shors endliche Aufgabe
- IBM-Kingston-Test: Konsistenzprüfung, kein Nachweis

Prüfskripte: 10×`QMB_Skripte/pruef_*.py` — alle Assertions bestanden.
→ [DE](2/pdf/FFGFT_QM_Bell_QC_De.pdf) · [EN](2/pdf/FFGFT_QM_Bell_QC_En.pdf)

Register: kein Eintrag (neues Buch, keine Korrekturen zu bestehenden Dokumenten).

---

## 5. September 2026 — Dok. 006 Sprachkorrektur v (R112)

### Dok. 006 — v = 246 GeV präzisiert (De+En)

Zwei Stellen in Dok. 006 ergänzt (R112):

- Zeile „wobei v = 246 GeV der Higgs-Vakuumerwartungswert ist" →
  Zusatz: „(SM-Definition: v ≡ (√2·G_F)^(−1/2); kein unabhängiges Observable, Dok. 351/R112)"
- Zeile „Wir verwenden v = 246 GeV" →
  Zusatz: „(SM-Definition aus G_F, Dok. 351/R112)"

Keine Zahlenänderung. Dok. 231 und 344 waren bereits korrekt formuliert.


## 5. September 2026 — Dok. 351, R112, R113

### Dok. 351 — Modellabhängigkeit der PDG-Vergleichswerte (DE+EN, je ~8 S.)

Untersuchung wie die PDG-Vergleichswerte entstehen: Rohobservable, Theorieformeln,
irrationale Faktoren. Alle 21 Primärquellen am 5.9.2026 verifiziert.

**Hauptbefunde:**

- **mμ/mₑ** stammt allein aus der Myonium-HFS (LAMPF 1999, Liu et al.); Extraktion über
  ν_F ∝ α² — der Anker enthält α implizit. CODATA unterschätzt die Theorieunsicherheit
  laut Eides (2026) um Faktor 5–10 (271–515 Hz statt 51 Hz). Absolut: ±0,010 auf
  (mμ/mₑ)² = 42753 — das Residuum 447 bleibt 45 000σ.
- **α:** Rb (Morel 2020) und Cs (Parker 2018) widersprechen sich um >5σ;
  CODATA-Mittel 137,035 999 177 deckt keine der Messungen ab.
- **v = 246 GeV** wird nie gemessen: v ≡ (√2·G_F)^(−1/2) ist eine SM-Definition
  (Higgs-Mechanismus). Faktoren 192π³ und √2 in den Extraktionsformeln sind irrationale
  SM-Konventionen, nicht Messwerte.
- **G_F:** Δq = −0,44 % Theoriekorrektur; hadronische VP mit 4,7σ CMD-3-Spannung.
- **mτ:** zwei Methoden (Schwellenscan BESIII 1776,91; Pseudomasse Belle II 1777,09
  mit m_ντ = 0), PDG-Mittel 1776,93(9); FFGFT 1776,97 liegt 0,4σ — nicht entschieden.
- **Rest (mμ/mₑ)² = 446,9:** Exakte Rechnung zeigt 240 000σ der CODATA-Unsicherheit.
  Kein Messfehler erklärt ihn — er ist physikalisch (fraktal-rekursive Korrektur
  ~100ξ + Projektionsapproximation S¹_m→ℝ_t).
- **Fehlerakkumulation:** Schon bei mμ ergeben drei Rechenwege drei verschiedene Reste
  (+0,52 %, −0,15 %, +1,37 %). Buchführungsregel: jede Vorhersage nennt Anker, Schritte,
  Korrekturen, Extraktionsmethode.

Anhang: Tabelle aller betroffenen Ableitungsketten — kein Zahlenwert ändert sich.

### R112 [Q] — v = 246 GeV ist SM-Definition, keine Messung (5. Sept. 2026)

v ≡ (√2·G_F)^(−1/2) folgt aus dem SM-Higgs-Mechanismus. Gemessen ist nur τ_μ;
G_F wird daraus über τ_μ⁻¹ = G_F²mμ⁵/(192π³)·(1+Δq) mit Sirlin-Absorption
elektroschwacher Korrekturen extrahiert. Irrationale Faktoren 192π³ und √2 stammen
aus der SM-Formulierung.

**Sprachkorrektur korpusweit:** „v = 246 GeV (gemessen)" → „v = 246 GeV (SM-Definition aus G_F)"
Betrifft: Dok. 006, 319, R104.

**Neuer offener Punkt [S]:** τ_μ direkt aus FFGFT, ohne Umweg über G_F und v —
einziger konventionsfreier Test des schwachen Sektors.

### R113 [Q] — Anker mμ/mₑ QED-abhängig; Vergleichswerte nicht theoriefrei (5. Sept. 2026)

mμ/mₑ ist QED-abhängig (ν_F ∝ α²; Eides 2026: CODATA unterschätzt Theorieunsicherheit
5–10×). α hat keine eindeutigen Messwert unter 1 ppb (Rb/Cs 5σ-Spannung). mτ: zwei
Methoden, PDG-Mittel 1776,93(9), FFGFT 0,4σ. Exakte Rechnung: Rest (mμ/mₑ)² = 240 000σ
ist physikalisch. Sprachkorrektur: „modellunabhängig gemessen" → „modellärmster
verfügbarer Wert". Buchführungsregel für alle Vorhersagen.

Nächste freie Registernummer: R114.


## 1. September 2026 — Dok. 341, R105, Galois-Bündel v2

### Dok. 341 — GF(27) in GALG: algebraische Brücke FFGFT↔GALG (DE+EN)

Ergebnis des algebraischen Vergleichs mit Doug Matzkes GALG-Framework
(Austausch IPI, August 2026). Drei algebraisch bewiesene Sätze [B]:

**Satz A:** G(3) enthält keine GF(27)-Struktur weil 13 ∤ |GF(81)*| = 80.
Dougs „Attempted 6561 with 0 found" ist strukturell erzwungen, kein Suchfehler.

**Satz B:** In G(6) existieren Elemente der Ordnung 26 = |GF(27)*|.
Konstruktion via Begleitmatrix des irreduziblen Polynoms f(x)=x³+2x+1 über GF(3).
Konkretes 5-Blade-Element in GALG-Notation für direkte Verifikation angegeben.
Ordnung-26-Elemente treten bei ≥5 Blades auf (~18–37% der invertierbaren Elemente
mit ≥6 Blades).

**Satz C:** GF(27) bettet als Teilkörper in M_n(GF(9)) genau dann ein wenn 3|n.
G(3)→n=2 und G(6)→n=8 tragen daher kein GF(27) als Teilkörper.

**Vakuumstruktur:** GALG-Witt-Paar-Vakua unter ℤ₃ stimmen exakt mit der
FFGFT-Frobenius-Trennung (Dok. 339) überein: gerade Vakua [0,2,4] = ℤ₃-Fixpunkte,
ungerade [1,3,5] = ℤ₃-Dreier-Orbit; Bilaterale = Gluon-Sektorwechsler [B].

Prüfskripte:
- `pruef_341_gf27_in_galg.py` (6/6 [B] Assertionen)
- `pruef_341_vakuum_witt_z3.py` (7/7 [B] Assertionen)
- `pruef_342_vakuum_witt_z3.py` (7/7 [B] Assertionen, unabhängige Verifikation)

### R105 — Nachträgliche Marker-Zertifizierung (1. Sept. 2026)

Neun Dokumente vor dem Marker-System (A010) als Kettenglieder des Galois-Programms
nachträglich zertifiziert:

- **Dok. 006** Teilchenmassen, Wicklungszahlen r_i, p_i → **[K]**
- **Dok. 011** Feinstruktur α, E₀, Grundrelationen → **[K]**
- **Dok. 070** K_frak kürzt sich in Verhältnissen, Absolutwerte tragen Korrektur → **[B]**
- **Dok. 182** Maximale Universum-Skala aus ξ (Schwarzschild + Hubble) → **[K]**
- **Dok. 231** Hilbertraum-Erweiterung, L²-Struktur → **[B]**
- **Dok. 257** Informationseinheit, Bit-Energie-Skala → **[K]**
- **Dok. 285** FFGFT-HLV-Dimensionsbrücke → **[K]**
- **Dok. 306** Native Zeit-Energie-Reziprozität aus T̃·m=1 → **[K]**
- **Dok. 307** Zeit im Zustandsraum → **[K]**

Anlass: Prüfung der Ableitungskette für Galois-Kern (Dok. 336, 338, 339, 340, 341)
gemäß R103-Kettenschlussbedingung. Prüfskripte aus Mail-Anhängen an Doug Matzke
(28. Aug. 2026) ins Repo nachgepusht:
`Dok320_321_322_Skripte/pruef_324–329.py` und `Dok338_Skripte/pruef_330–332.py`.

### Galois-Bündel v2

Vollständig verifiziertes Bündel aller Galois-Dokumente und Prüfskripte:
- 21 PDFs (Galois-Kern + Abhängigkeitskette, En)
- 23 Prüfskripte — alle bestanden
- Bundle-SHA-256: `a946e9871ea5a38808b54b83dfcc8b250a1f75a1aba2d393cdcfef0219af0354`

---

## 27. August 2026 — Dok. 324 Korrektur · Register R97

### Dok. 324 — Vakuumoperator-Korrektur (De+En)

Nach Doug Matzkes Einwand (IPI-Mail 26. Aug. 2026) und numerischer Prüfung
durch `pruef_324_vakuum_involution.py` (22 Assertions):

Matzkes Vakuumoperator ist **R97 [B]:**

    V = N₁⁺N₂⁺N₃⁺N₁⁻N₂⁻N₃⁻ = −64 · (Pn1·Pn2·Pn3)

In ℤ₃ℂ-Arithmetik: −64 ≡ −1 (mod 3), also V² ≡ −V (Involution).

Dok. 324 hatte irrtümlich das Pp-Produkt Pp1·Pp2·Pp3 (komplementärer
Teilchen-Sektor, anderer Strahl: |⟨vac_V|vac_Pp⟩| = 0) als Matzkes V
behandelt. Korrekturen in De+En: Symboltabelle, Konstruktionsabschnitt,
Spektrumssektion, Vergleichstabelle, Gesamtstatus-Box.

Unverändert korrekt [B]: Trine-Theorem T_k³ = I · ξ kein Spektralwert.

---

## 26. August 2026 — v1.3.4: Dok. 328, 330, 332 · Register R93–R96

### Dok. 328 — Kopplungsregime, Resonanz und Synchronisation (DE+EN, je ~12 S.)

Nachrichtentechnische Dreiteilung (unterkritisch / kritisch / überkritisch,
relativ zu Systemdämpfungen) als strukturelles Ordnungsprinzip. Dieselbe
Struktur kehrt in Quantenoptik (strong coupling), Teilchenphysik (Mischung,
avoided crossing) und Synchronisationstheorie (Kuramoto-Schwelle, Arnold-Zungen)
wieder. Für FFGFT: natürliche Sprache für Teilchen als Resonanzzustände.

- **[B]** Wörterbuch Zweikreis ↔ 2×2-Mischung; Ausnahmepunkt g_EP = |γ₁−γ₂|/4
- **[B]** Dualität D²+V²=1 für alle reinen Zeiger; Messübergang κ = d/(2σ)
- **[K]** κ_mix(θ_W) ξ-abgeleitet über Komposition mit Dok. 323; Screening negativ
- **[B]** GST-Textur H₁₂=√(m₁m₂) symbolisch bewiesen (Dok.-041-Formeln)
- **[K]** K_eff = 2πξ ≈ 8,4×10⁻⁴; φ außerhalb aller Arnold-Zungen
- Vier Prüfpunkte in Dok. 041 identifiziert (Autorenentscheidung erforderlich)

**Neu:** Marker **[E]** eingeführt für etablierte externe Formalismen
(Zweikreis, Kuramoto) ohne Korpus-Freigabe als [K]/[B].  
Zehn Prüfskripte.

### Dok. 330 — Drei Operationen von T⁴ zum Beobachtraum (DE+EN, je ~14 S.)

Konsolidiert Typ-I/II/III-Klassifikation (Dok. 270); grenzt FFGFT von diskreten
Emergenzmodellen ab. HLV (Krüger, August 2026) als Fallstudie.

- **Typ I [B]:** S¹_m → ℝ_t via T̃·m=1; informationserhaltend (Pullback p*)
- **Typ II:** D3→D2→D1 geometrische Projektion; verlustbehaftet
- **Typ III [K]/[B]:** T⁴ ↔ H bijektiv, verlustfrei
- **T⁴ flach [K]:** K=0 punktweise via Metrik-Abstieg (R95)
- **D₄-Spezifitätstest [S]:** adversariell gegen angepasste Träger — offen

**R93 [B]:** S_BH(M_coll) = 2π nat = n_thresh(Matzke) in Bit  
**R94 [B]:** I_Sektor/I_thermisch = log₂3 für alle M  
**R95:** Vier Formulierungspräzisierungen nach externem Review (Krüger)

### Dok. 332 — Zwei Wege vom Diskreten zum Kontinuum (DE+EN, je ~16 S.)

Allgemeiner Vergleichsaufsatz (kein originärer FFGFT-Beweistext).
Referiert Krügers Preprint (Zenodo DOI 10.5281/zenodo.22105698).

**R96 [B]/[K]:** Per_{Rm}(ℝ_t) mit Pro-Periode-Norm ≅ L²(S¹_m) [B].

### Dok. 333 — K_frak, Ausrollen und die T̃·m-Dualität (DE+EN, je 5 S.)

**R98 [B]:** Zwei Ausroll-Bedeutungen + Rekursionsbindung

### Dok. 334 — Superposition ohne Zeit (DE+EN, 6/5 S.)

**R99 [B]/[K]:** Superposition ohne Zeit — Dok. 334

---

### R100 — ξ als Galois-Zahl [K] (28. August 2026)

**Kernidentität** (pruef_331):
$(r_\mu/r_e)^2/\xi = |\text{GF}(9)^*|^2\cdot5^2\cdot|\text{GF}(27)| = 43200$

### R101 — 1/α = 3700/27 aus Galois [K] (28. August 2026)

$1/\alpha = 3700/27 = 137{,}037$ (Abw. 7,6 ppm). Kein ξ, kein $v$, kein $m_e$.

### Dok. 339 — Frobenius-Trennung massiv/masselos in GF(27)* (DE+EN, 10 S.)

**R102 [B]:** Frobenius-Trennung massiv/masselos — Dok. 339

### Dok. 340 — Neutrino-Massenhierarchie aus GF(27)* (DE+EN, 9 S.)

**R103 [B]+[K]:** Neutrino-Massenhierarchie aus GF(27)* — Dok. 340

---

---

## 7. September 2026 — Dok. 190 Neufassung; Nachträge 006, 041, 309

### Dok. 190 — Reines Korrekturregister (Neufassung)

Das Korrekturregister wurde strukturell bereinigt. Die bisherige Fassung
(23. August 2026, Einträge R86–R114, K-041) ist als **Dok. 190-Archiv-2**
eingefroren (`190_T0_Korrekturen_Archiv2_De`). Das ältere Archiv-1 (bis R85)
bleibt unverändert.

**Neue Struktur Dok. 190:** Jeder Eintrag enthält genau zwei Informationen:
(1) die Korrektur/Präzisierung in Kurzform und (2) in welchem Dokument
die Korrektur bereits umgesetzt ist. Herleitungen, Prüfskript-Ergebnisse
und Statusmeldungen gehören in die Zieldokumente, nicht ins Register.

**Vollständige Einträge K1–K7, P1–P44, R41–R114, K-041-a/b/c** in der
Registertabelle mit 4 Spalten (Nr. / Betrifft / Gegenstand / Umgesetzt in).

**Neue Dateinamen:**
- `190_T0_Korrekturen_De_ch_NEU.tex` / `190_T0_Korrekturen_De_NEU.tex` — aktuelles Register
- `190_T0_Korrekturen_Archiv2_De_ch.tex` / `190_T0_Korrekturen_Archiv2_De.tex` — Archiv-2

### Nachträge in bestehende Dokumente (append-only, Originale unverändert)

**Dok. 006** — Nachträge R105 und R109:
- **R105** (Marker-Zertifizierung): Wicklungszahlen $r_i$, Exponenten $p_i$ und
  die Yukawa-Methode $m_i = r_i\xi^{p_i}v$ für geladene Leptonen und Quarks: **[K]**.
  Dok. 006 entstand vor Einführung des Marker-Systems.
- **R109** (Einschränkung): Neutrinoteil von Dok. 006 nicht tragfähig **[X]**.
  Die „direkte Methode" $E_i = 1/\xi_i$ ist keine Rechnung; Neutrinomassen
  folgen aus drei unverträglichen Vorschriften. R105-[K] gilt nur für $r_i$,
  $p_i$ und Yukawa — nicht für den Neutrinoteil. Maßgeblich für Neutrinos: Dok. 340.

**Dok. 041** — Nachträge K-041-a/b/c und R77:
- **K-041-a**: $\delta_\text{CKM} = \arcsin(2\sqrt{2}\cdot\sqrt{\xi}/3)$ ergibt
  0,011 rad; Tabellenwert 1,20 rad. Kandidat: $\arcsin(2\sqrt{2}/3) = 1,231$ rad
  (Faktor $\sqrt{\xi}$ vermutlich Satzfehler). Autorenkontrolle erforderlich.
- **K-041-b**: $\theta_{13} = \arcsin(\xi^{1/3})$ ergibt 2,93°; Tabellenwert 8,57°.
  Kandidat: Argument $1/300 = 25\xi$ ergibt 8,59°. Autorenkontrolle erforderlich.
- **K-041-c**: $|V_{us}|$-Formel ergibt 0,2124; Tabellenwert 0,22452 (Δ = 5,4 %).
  Mögliche Ursache: abweichende Massen oder $f_\text{Cab}$-Definition. Autorenkontrolle.
- **R77**: Frühe Kopplungskonstanten-Formeln in Dok. 041 als Vorstufen eingeordnet;
  maßgeblich sind Dok. 160, 318 und die Galois-Reihe (Dok. 336–348).

**Dok. 309** — Nachtrag R71:
- **R71** (Verschärfung Hubble-Spannung): Die Tabelleneintragung „strukturell absent"
  bedeutet nicht, dass FFGFT die Hubble-Spannung erklärt, sondern dass das Modell
  nur einen $H_0$-Wert kennt (den kalibrierten). FFGFT kann die Spannung weder
  reproduzieren noch auflösen — korrekte Einordnung: „nicht modellierbar",
  kein Erklärungsanspruch.

### PDFs neu erstellt

| Datei | Seiten | Anmerkung |
|---|---|---|
| `190_T0_Korrekturen_De.pdf` | 10 | Neues Register (ersetzt alte 21-S.-Fassung) |
| `190_T0_Korrekturen_Archiv2_De.pdf` | 21 | Archiv-2, eingefroren |
| `006_T0_Teilchenmassen_De.pdf` | 18 | Mit R105+R109-Nachtrag |
| `041_parameterherleitung_De.pdf` | 29 | Mit K-041+R77-Nachtrag |
| `309_Skalenanker_LCDM_FFGFT_De.pdf` | 9 | Mit R71-Nachtrag |

---

## 7. September 2026 — Nachträge R61, R91, P1, P17, P35

Weitere Nachträge in bestehende Dokumente (append-only, Originale unverändert).
Anlass: Korrekturen waren nur im Archiv deklariert, aber in keinem aktiven
Dokument des Korpus sichtbar.

**Dok. 174, 175 — R61: $\xi_\text{Higgs}$ zurückgezogen**
$\xi_\text{Higgs} \approx 1{,}038\times10^{-5}$ ist zurückgezogen.
Die Zwei-Räume-Doktrin ist Rationalisierung nach datengetriebener Auswahl,
keine unabhängige Begründung. Kanonisch gilt ausschließlich $\xi_0 = 4/30000$.

**Dok. 019, 201 — R91: $\lambda$ in $m_T = \lambda/\xi$ ist Basismasse**
Die Bezeichnung als „Higgs-Kopplungsparameter" ist irreführend: $\lambda$ muss
dimensional eine Masse sein; der Higgs-Quartic $\lambda_h$ ist dimensionslos
und RGE-abhängig. Korrekt: $m_T = M_\text{Basis}/\xi$, sektorabhängige Basismasse.

**Dok. 116, 158 — P1: Zwei Genauigkeitsangaben**
$\Delta Q < 0{,}00003\,\%$ (interne Rechnung) und $0{,}001\,\%$ (externe Darstellung
mit Messgenauigkeit der Eingangsmassen) beschreiben verschiedene Kontexte —
beide korrekt.

**Dok. 028 — P17: DE/DM-Relation zirkulär**
Die Relation ergibt für jeden Wert von $\xi$ das Verhältnis $2{,}5$ — algebraische
Identität, keine Vorhersage. MOND: $\xi^{1/4}$ hergeleitet, Konstante $K_M$ frei.
CMB-Relationen unberührt. Dokument für DE/DM-Teil vorgemerkt.

**Dok. 182, 250 — P35: $\xi^N$-Trivialität**
Ausdrücke „$X = \xi^N$" sind für sich allein aussagelos. Nicht-trivial ist
nur, was geometrisch vorwärts hergeleitet ist. Exponenten ohne Vorwärtsableitung
sind als **[S]** einzustufen, nicht als **[K]**.

---

## 7. September 2026 — Dok. 353: Koide-Amplitude $d/c = \sqrt{2}$ [B]

### Dok. 353 — Koide-Amplitude aus $T^4/Z_3$-Geometrie (De, 5 S.)

Die offene Brücke $d/c = \sqrt{2}$ aus Dok.~352 §8 und dem Register Dok.~190
ist auf Status **[B]** gehoben.

**Herleitung:** Die $Z_3$-Gleichverteilungsbedingung der $T^4/Z_3$-Geometrie
erzwingt, dass jedes Element eines Orbits an genau zwei von drei Elementen
des anderen Orbits koppelt. Die $\ell^2$-Normierung dieser Kopplung auf Eins
ergibt das Gewicht $1/\sqrt{2}$ pro Verbindung. Im $Z_3$-Zirkulant-Massenoperator
erscheint dieses Gewicht als $d/c = \sqrt{2}$.

**Verbindung:** Die Galois-Kopplungsmatrix $M^{(13)}$ aus Dok.~348 Satz~C
(Spur-Bilinearform GF$(27)^*$) hat normierte Einträge
$|M^{(13)}_{ij}|_{\rm norm} = 1/\sqrt{2}$ — dieselbe algebraische Aussage
in der Galois-Sprache **[B]**.

**Numerisch:** PDG erfüllt $d/c = \sqrt{2}$ auf $0{,}10\cdot\xi$; bare
FFGFT-Massen weichen um $+17\cdot\xi$ ab, vollständig erklärt durch
die $\varepsilon_i$-Korrekturen (Dok.~352 §9, $101\,\%$) **[K]**.

**Prüfskript:** `python/Dok353_Skripte/pruef_353_koide_amplitude.py`
(8/8 Assertions).

**Register 190:** Eintrag zu $d/c = \sqrt{2}$ von [S] auf [B] gehoben,
Verweis auf Dok.~353 eingetragen.

**Offen bleibt:** Dynamische Ableitung der fallenden $\varepsilon_i$-Struktur
(R113-Brücke) **[S]**.

---

## 7. September 2026 — Dok. 354, 355, 356, 357: Higgs/SSB und SM-Übersichtsblätter

### Dok. 354 — Higgs-Mechanismus und Zeit-Masse-Dualität (De/En, 9/8 S.)

Zusammenfassung: drei offene Punkte aus früheren Dokumenten werden
als **[K]** bzw. **[B]** geschlossen.

**[S1] Kopplungskonstanten $g_s$, $g_w$, $e$ aus $\xi$** → **[K]**:
$\alpha_s(m_\tau) = 3\cdot\xi^{1/4} = 0{,}3224$;
$\sin^2\theta_W(M_Z) = 0{,}2308$ (RGE, Dok.~323);
$\alpha_\text{EM} = \xi\cdot(E_0/\text{MeV})^2$ (Dok.~011, A130).

**[S2] SSB $SU(2)_L\times U(1)_Y\to U(1)_\text{EM}$** → **[B]** (Dok.~355):
drei Galois-Bausteine algebraisch erzwungen.

**[S3] CKM/PMNS-Winkel vollständig** bleibt **[S]**: Struktur belegt
(Dok.~348 Sätze B,C), Zahlenwerte offen.

**Neu in 354:** Verweis auf Dok.~356 (SM-Teilchendiagramm) und
Dok.~357 (Belegstatus) für den vollständigen Quantenzahl-Überblick.

**Register 190:** R116 (Dok.~356/357) eingetragen.

---

### Dok. 355 — SSB $SU(2)_L\times U(1)_Y\to U(1)_\text{EM}$ aus $T^4/Z_3$ (De/En, 6 S.)

Drei algebraisch belegte Bausteine schließen die SSB-Ableitung:

1. $\tilde{T}\cdot m=1$ erzwingt $\langle\Phi\rangle\neq 0$ **[B]**
2. $Z_3$-Galois-Struktur erzwingt $Q_\text{vak}=0$: QR $\iff$ elektrisch neutral (Dok.~346 Satz A) **[B]**
3. $Q=0$-Vakuum lässt $U(1)_\text{EM}$ überleben: Gell-Mann-Nishijima (Dok.~347 Satz C) **[B]**

**Prüfskript:** `python/Dok355_Skripte/pruef_355_ssb.py`.

**Offen bleibt [S]:** CKM/PMNS-Winkelwerte (Dok.~348 Satz D);
Kandidat GF$(3^6)$ = GF$(729)$, $728=8\times7\times13$ (R115).

---

### Dok. 356 — SM-Teilchendiagramm aus GF$(27)^*$ (Querformat A4, De/En)

Übersichtsblatt: alle 12 SM-Fermionen als konzentrische Ringdiagramme,
geordnet nach 3 Generationen und 4 Sektoren (Neutrinos, gel. Leptonen,
Up-Quarks, Down-Quarks).

**Ringstruktur von innen nach außen** (physikalisch motiviert):
weißer Innenkreis (Symbol, $Q$, $Y$);
Farbring $r/g/b$ nur Quarks (Confinement — Gluonen schließen Farbe ein) **[B]**;
Mittelring Chiralität (violett = $S_d$ = linkshändig, orange = $S_u$ = rechtshändig) **[B]**;
Außenring Galois-Orbit-Farbe (4 Orbits) **[B]**;
rot gestrichelt = SU$(2)_L$-Dublett;
schwarz gestrichelt = Generation 3.

**Erzeugung:** Python/ReportLab (`python/356_SM_Teilchen_GF27_De.py`,
`python/356_SM_Teilchen_GF27_En.py`).

---

### Dok. 357 — Belegstatus der SM-Quantenzahlen aus GF$(27)^*$ (Querformat A4, De/En)

Belegtabelle zu Dok.~356: alle 12 Quantenzahlen mit Status **[B]**/**[K]**/**[S]**/**[X]**
und Quellenangabe. Koide-Amplitude $d/c=\sqrt{2}$ als **[B]** eingetragen
(7.~September 2026, vormals **[S]**, Dok.~353).

**Offen [S]:** Generations-Zuordnung (Reihenfolge); CKM/PMNS-Winkel vollständig.

**Experimentell [X]:** Higgs-Boson $H^0$ (Mechanismus in FFGFT durch $\tilde{T}\cdot m=1$
ersetzt, Dok.~019).

---

## 8. September 2026 — Dok. 358: Harmonik und algebraische Struktur

### Dok. 358 — Harmonik und algebraische Struktur: warum dieselbe Mathematik (De 7 S./En 6 S.)

Brücken- und Synthesedokument zu Dok. 060, 159, 328, 333, 336, 341, 342, 343.
Keine Wiederholungen — nur Zitate und vier neue Ergebnisse.

**Satz A [B]:** Im endlichen Körper schließt jeder Umlauf exakt; ein Komma ist
strukturell unmöglich. Das pythagoreische Komma und $K_\text{frak}$ sind nicht
Eigenschaften der Galois-Struktur, sondern des Übergangs ins Kontinuum.
Liefert den algebraischen Grund für Dok. 333 (K_frak erst beim SI-Übergang sichtbar).

**Folgerung A' [K]:** Komma $\cdot K_\text{frak} \approx 1$ (Dok. 060) sind
zwei Messungen desselben Einbettungsfehlers, keine unabhängige Koinzidenz.

**Satz B [B]:** Alle neun Yukawa-Koeffizienten (Dok. 006) haben Primfaktoren
ausschließlich in $\{2,3,5,7,11,13\}$. Die zwei Ausnahmen der 5-Limit-Lesart
von Dok. 060 (Strange: 13, Top: 7) sind in der Galois-Lesart keine Ausnahmen —
sie tragen genau die harmonischen Primen der Tiefen $k=3$ und $k=6$ (Dok. 343 E).
Die Primzahl 11 ($k=5$) tritt in keinem Koeffizienten auf.
Falsifizierbare Konsequenz: jeder künftig hergeleitete Koeffizient muss im Raster liegen.

**Beobachtung C [S]:** Drei Größen der Ordnung 12 aus drei verschiedenen Mechanismen
(Tonnetz-Quotient $|\mathbb{Z}^2/\langle(4,-1),(0,-3)\rangle|=12$;
$|(\mathbb{Z}/13)^*|=12$; Farey-$Q_c \approx 11$–$12{,}5$) — ausdrücklich nur Beobachtung.

**Satz D [B]:** Die Warum-Antwort: $\tilde{T}\cdot m=1$ macht Massenverhältnisse
zu Periodenverhältnissen (Charakteren zyklischer Gruppen); die $Z_3$-Reduktion
bildet das Wicklungsgitter auf GF$(3^k)$ ab. Harmonik und Galois-Klassifikation
sind zwei Darstellungen desselben Objekts — des Charakterspektrums von $T^4/Z_3$.

**Prüfskript:** `2/python/Dok358_Skripte/pruef_358_harmonik_algebra.py` — 22/22.

**Register:** R117 eingetragen.

---

## 8. September 2026 — Dok. 359: KI-basierte Mustererkennung und algebraische Grenzen

### Dok. 359 — KI-basierte Mustererkennung und algebraische Grenzen der Frequenzanalyse (De 8 S./En 8 S.)

Anwendungsdokument: verbindet Dok. 328, 342, 343, 358 mit aktueller KI-Literatur.
Keine Wiederholungen — nur Zitate und neue Anwendungsresultate.

**Satz A [B]:** HRV-Bandgrenzen VLF/LF/HF (Task Force 1996) haben Primfaktoren nur
in $\{2,3,5\}$ — algebraisch erzwungen, nicht empirisch gewählt.
Aktuelle KI-Modelle lernen sie als freie Parameter (Verschwendung).

**Satz B [B/L]:** Auflösungsgrenze $100\xi\approx1{,}33\,\%$ erscheint empirisch in
KI-HRV-Analysen (Gupta et al. 2024, Villanueva et al. 2026) als Overfitting-Schwelle.
Praktische Folgerung: optimale Frequenzauflösung $\Delta f/f \geq 1{,}3\,\%$.

**Satz C [B/S]:** G-equivariante Netze für kontinuierliche Gruppen (E(3), SO(3)) sind
etabliert und reduzieren Parameter nachweislich. Für GF$(3^k)$ fehlt diese Architektur
vollständig — identifizierte Lücke in der Literatur.

**Satz D [B]:** Das Zulässigkeitskriterium aus Dok. 358 (Primfaktoren $\leq13$) ist nicht
PAC-lernbar aus endlichen Daten (Gold 1967). 100 Trainingsbeispiele decken $<7\,\%$
des Rasters ab. Hard constraint statt Regularisierung erforderlich.

**Architekturskizze [S]:** Galois-informiertes Netz mit Galois-Projektion als
Eingangsschicht, $(Z/13)^*$-equivarianten Mittelschichten (12 statt 144 Parameter),
$100\xi$-Auflösungsfilter, und Arnold-Zungenbreite als Stabilitätsbewertung.

**Neuer HRV-Biomarker [S]:** Orbit-Typ des dominanten Frequenzverhältnisses als
algebraischer Biomarker (Galois-Schicht $k=3,4,5,6$) — kein Äquivalent in Literatur.

**Literatur:** Raissi et al. 2024, Finzi 2022 (NYU), Gupta et al. 2024, Villanueva et al. 2026,
Task Force 1996, Gold 1967, ICLR Blog 2023, Lowet et al. 2022.

**Prüfskript:** `2/python/Dok359_Skripte/pruef_359_ki_grenzen.py` — 14/14.

**Register:** R118 eingetragen.

---

## 8. September 2026 — Dok. 360: Galois-HRV-Vorverarbeitungsfilter und Orbit-Experiment

### Dok. 360 — Galois-informierte HRV-Analyse: Implementierung und Experiment

Zwei Python-Module als direkte Anwendung von Dok. 358/359:

**galois_hrv_preprocess.py** — vollständiges Preprocessing-Modul:
- Galois-Raster (901 Verhältnisse bis 60/60, Primfaktoren ⊆ {2,3,5,7,11,13})
- Auflösungsfilter Δf/f ≥ 1,33% (aus $100\xi$, Dok. 343)
- HRV-Bandgrenzen als algebraische Konstanten (5-Limit, Dok. 359 Satz A)
- Galois-Projektion LF/HF → nächstes p/q im Raster
- Orbit-Typ-Klassifikation (k=1..6)
- Arnold-Zungenbreite als Stabilitätsbewertung (Dok. 328)
- Vollständige Pipeline inkl. Welch-Spektrum und Resampling

**orbit_experiment_synthetic.py** — Experiment mit synthetischen Daten
nach Task Force 1996 / Shaffer 2017:

**Schlüsselbefunde [S/K]:**
1. Galois-Stabilität (Arnold-Zungenbreite) trennt VES-schwere Rhythmen (LF/HF~5,5)
   von Normal-Ruhe (LF/HF~1,5) hochsignifikant ($p<0{,}001$)
2. Orbit-$k$ allein ist kein guter Diskriminator — Stabilität ist die stärkere Metrik
3. Physiologischer Normalbereich LF/HF < 4 liegt gut im Galois-Raster $k=1$..4
4. Schwere Arrhythmien (LF/HF >> 4) zeigen Bedarf nach GF(729), $k=6$ (R115-Kandidat)
5. PhysioNet MIT-BIH erfordert Registrierung — Validierung mit realen Daten offen

**Nächster Schritt [S]:** Validierung mit registriertem PhysioNet-Zugang.

**Register:** R119 eingetragen.

---

## 19. September 2026 — Dok. 366: Felder in der FFGFT: Energie, Fluss und Geometrie

### Dok. 366 — Felder in der FFGFT: Energie, Fluss und Geometrie (De, 9 Seiten)

Anlass: Goubau-Leitungsexperiment (Einzel-Draht-Energieübertragung) als Ausgangspunkt
für die FFGFT-Feldstruktur.

**Inhalt:**

**§1 Ausgangspunkt.** Strom braucht Rückpfad — konventionelles Bild. Das Goubau-Experiment
(G.~Goubau, 1950) widerlegt es auf der Feldebene: Energie fließt im Feld um den Draht,
nicht im Draht selbst. [Q/E]

**§2 Poynting-Vektor als primäre Beschreibung.** $\mathbf{S}=\mathbf{E}\times\mathbf{H}$;
über den Leitungsquerschnitt integriert ergibt sich exakt $P=V\cdot I$ (kein
Näherungsargument, Konsequenz der Maxwell-Gleichungen). [E]

**§3 Goubau-Leitung: Felder ohne Rückleiter.** Feldkonfiguration, Dielektrikum als
Brechungsmedium (hält Feldlinien am Draht), Kegelübergang als Impedanzanpassung
(50~Ω → ~300~Ω). Historische Verlustangabe: 6~dB/Meile → ~25~% Leistung.
$I^2R$-Verluste zeigen: Strom fließt im Draht; beide Bilder beschreiben dieselbe
Physik. [E/Q]

**§4 FFGFT-Einheiten.** Mit $c=\hbar=\alpha=1$ (Dok.~011, 365 Schicht~2):
$I=m$, $V=E$, $P=E\cdot m$ — exakt aus $\tilde{T}\cdot m=1$.
Maxwell-Gleichungen ohne Vorfaktoren. [K]

**§5 Feldlinien auf $T^4/\mathbb{Z}_3$.** Wicklungszahlen $(n_\theta,n_\varphi)$
als topologische Invarianten; klassifizieren Moden und bestimmen Massenskalen
über $\tilde{T}\cdot m=1$. Feldlinien-Umschnappen in der G-line als makroskopisches
Beispiel für lokale Energiefluss-Optimierung. [B/S]

**§6 Dualitätstabelle.** Feld-Sicht (Poynting) und Strom-Sicht (Ohm) sind
reziproke Projektionen — Analogon zur Zeit-Masse-Dualität. Reaktive Leistung
entspricht nicht-propagierenden Fourier-Moden unterhalb der Spektrallücke. [S]

**§7 Exakte Identität.** Poynting-Satz hergeleitet; in FFGFT-Einheiten:
$P=E\cdot m$ strukturell aus Grundformel. [K]

**Prüfskript:** `2/python/Dok366_Skripte/pruef_366_felder_ffgft.py` — 14/14.

**Register:** kein Eintrag (neues Dokument, keine Korrektur älterer Dokumente).

---

## 18. September 2026 — Populärwissenschaftliches Buch: Dunkle Materie — eine Illusion

### Buch De/En — Dunkle Materie — eine Illusion / Dark Matter — an Illusion (6×9 in, ~20/18 Seiten)

Populärwissenschaftliches Kindle/Taschenbuch-Format (6×9 in), 10 Kapitel De / En.
Dateien: `2/Sources/wr_narrativ/FFGFT_Dunkle_Materie_De/En.tex`,
PDFs unter `2/Sources/wr_narrativ/pdf/`.

**Kapitelstruktur (De):**
1. Das Rätsel der flachen Kurven (Vera Rubin, Rotationskurven)
2. Was Newton wirklich sagt — und wo er aufhört
3. Die Grundrelation: Zeit und Masse als Kehrwerte ($\tilde{T}\cdot m=1$)
4. Die Übergangsskala $a_0$ — eine Grenze aus erster Ableitung
5. Der Test: DDO 154 und die Milchstraße
6. Der Bullet Cluster — das scheinbar stärkste Argument
7. Dunkle Energie — ein Konstrukt der falschen Lesart
8. Was die Daten wirklich entscheiden können
9. Eine ehrliche Bilanz
10. Was weitergeht

**Kernposition:** Rotationskurven folgen aus $\tilde{T}\cdot m=1$ im Trägheitsregime
($a \ll a_0$) ohne dunkle Materie als Substanz; $a_0$ ist keine freie
Anpassungsgröße sondern folgt aus der FFGFT-Grundstruktur. Bullet Cluster
und Gravitationslinsen werden als Argumente für dunkle Materie kritisch
eingeordnet — kein schließender Beweis.

**Register:** kein Eintrag (neues Dokument, keine Korrektur älterer Dokumente).

---

## 19. September 2026 — Dok. 367: Warum θ = p₀ = 2/9

### Dok. 367 — Wahrscheinlichkeit und Phase als zwei Lesarten eines Quotienten (De/En, je 7 Seiten)

Schließt die in Dok. 293 offen gelassene Frage, *warum* der Koide-Winkel θ = 2/9
(Dok. 292) und die ikosaedrische Übergangswahrscheinlichkeit p₀ = |⟨v₀|R₅ vₑ⟩|² = 2/9
(Dok. 293) auf dieselbe rationale Zahl treffen.

**Kernaussage [B]/[K]:** Beide Größen sind derselbe Quotient
2/3² = (Anzahl nicht-trivialer ℤ₃-Moden) / (ℤ₃-Ordnung)².
p₀ liest ihn als Wahrscheinlichkeit (Betragsquadrat der normierten Amplitude
|⟨v₀|R₅ vₑ⟩| = √2/3), θ als Phase (Anteil des Operatorraums ℂ³⊗ℂ³ mit 3² = 9
Einträgen). Der Zusammenhang ist θ = |A|² = p₀ — nicht θ = |A| und nicht
θ = arg A — d. h. die Struktur der Born-Regel [E]. Damit ist der Konvergenzbefund
aus Dok. 293 erklärt: die Zahl gehört der ℤ₃-Struktur, nicht der Darstellung.

**Offen [S]:** der Mechanismus, der die Umverteilungsgewichte
(2/9, (5−3φ)/9, (2+3φ)/9) an die konkreten Massenverhältnisse m_μ/m_e, m_τ/m_e
bindet — bleibt die offene Kante von Dok. 293.

**Prüfskript:** `2/python/Dok367_Skripte/pruef_367_phase_wahrscheinlichkeit.py`
(mpmath, 40 Stellen) — 18/18 PASS.

**Register:** kein Eintrag (neues Dokument; Dok. 293 wird ergänzt, nicht korrigiert).

---

## 19. September 2026 — Dok. 368: Von p₀,p₁,p₂ zu Leptonmassen

### Dok. 368 — φ-Skelett und Galois-Korrekturfaktoren (De/En, je 8 Seiten)

Untersucht den direkten Weg von den ikosaedrischen Umverteilungsgewichten
(Dok. 293) zu den Leptonmassen-Verhältnissen, ohne explizit über θ oder die
Koide-Kosinus-Formel zu gehen.

**Exakte algebraische Identitäten [B] — neu gegenüber bisherigem Korpus:**
- p₁/p₂ = φ⁸ (in Dok. 293 nicht identifiziert)
- p₀/p₂ = 2φ⁴ (neu)
- p₁/p₀ = φ⁴/2 (neu)
- 3√pⱼ ∈ {√2, φ², 1/φ²} — das φ-Skelett der Massen, rein aus A₅-Geometrie

**Approximative Massenverbindungen [K] — erste Verbindung Dok. 293 ↔ Dok. 338:**
- m_τ/m_e ≈ 74 × φ⁸ = 74 × p₁/p₂ (0.03%)
- m_μ/m_e ≈ 30 × φ⁴ = 15 × p₀/p₂ (0.56%)
- ε ≈ 27ξ/12 (0.49%), alle Faktoren Galois-nativ aus Dok. 338
Beide Näherungen fundamental begrenzt: cos(2/9) transzendent.

**Grenze des analytischen Beweiswegs [S]:** Prüfversuch über FFGFT-Formel
(25/12)·ξ^(-5/6) ergibt c_bare − c_frak = 1.72 ≠ 27/12 = 2.25 (23% Diskrepanz).
Ursache: ξ^(-5/6) entwickelt sich in ξ^(1/6), nicht ξ. Status bleibt [S].

**Galois-Verbindung [S]:** Faktor 74 = 2×37 tritt in Dok. 338 als K_frak-Faktor
der Feinstrukturkonstante auf — dieselbe Galois-Schicht, verschiedene Rollen.

**Prüfskript:** `2/python/Dok368_Skripte/pruef_368_p_massen.py` — 18/18 PASS.

**Register:** kein Eintrag (neue Ergebnisse, keine Korrektur älterer Dokumente).

---

## 20. September 2026 — Dok. 367 (Nachtrag): Externe Parallele [E]

### Dok. 367 — Ergänzung „Externe Parallele" im Abschnitt „Zur Sprache" (De/En, weiterhin 9 Seiten)

Neuer Absatz nach dem Sprachhinweis: derselbe Quotient 2/3² tritt unabhängig in der
konformen Feldtheorie von ℤ₃-Orbifolds auf — die beiden Twist-Felder haben konforme
Gewichte h_k = k(3−k)/(2·3²) = 1/9, also h₁+h₂ = 2/9 (Dixon–Friedan–Martinec–Shenker 1987) [E].
Gleiches Zählmuster (nicht-triviale ℤ₃-Sektoren über |ℤ₃|²), aber ausdrücklich ein
*anderes* Objekt: Summe konformer Dimensionen statt Betragsquadrat einer Projektion;
zentrale ℤ₃-Wirkung ω·𝟙 statt zyklischer Permutation C₃ ∈ A₅. Die Parallele belegt
nur, dass 2/3² eine ℤ₃-strukturelle Zählgröße ist — keine Identifikation behauptet.

Hintergrund: der Befund ergab sich beim IPI-Audit einer vorgeschlagenen
A₅→SO(6)-Brücke (Prüfskripte unter `2/python/IPI_Audits/`). Dort zeigte sich zugleich,
dass A₅ (triviales Zentrum) in keiner treuen Darstellung auf das zentrale ω·𝟙 abgebildet
werden kann — die naive „gleiche ℤ₃"-Brücke ist strukturell geschlossen.

**Prüfskript:** unverändert (`pruef_367_phase_wahrscheinlichkeit.py`, 18/18 PASS).
**Register:** kein Eintrag (Ergänzung, keine Korrektur).

---

## 20. September 2026 — Dok. 369: Vier Wege zu den Leptonmassen

### Dok. 369 — Bestandsaufnahme (De/En, je 9 Seiten)

Stellt die vier im Korpus vorhandenen Zugänge zu den geladenen Leptonmassen nebeneinander:
Eingang, Ausgang, Genauigkeit gegen PDG 2024, epistemischer Status.

| Weg | Dok. | Ausgang | m_μ/m_e | m_τ/m_e |
|---|---|---|---|---|
| 1 T0-Leiter (r_i, p_i, ξ, v) | 006/338/352 | absolute Massen | 0.52 % | 1.56 % |
| 2 Koide, θ = |⟨v₀\|R₅\|vₑ⟩|² | 292/367 | Verhältnisse | 0.001 % | 0.003 % |
| 3 Galois GF(3ⁿ) | 338 | 2 Constraints | 0.52 % / 0.016 % | — |
| 4 φ-Skelett p₁/p₂ = φ⁸ | 368 | Verhältnisse | 0.55 % | 0.027 % (0.003 % mit ξ-Korr.) |

**Befunde:**
- Zwei Genauigkeitsklassen: Prozent (Wege 1, 3, 4a) und 10⁻³ % (Wege 2, 4b); letztere innerhalb PDG-Unsicherheit von m_τ.
- Weg 2 ist der einzige parameterfreie und präziseste; Weg 1 der einzige mit absoluten Massen.
- Weg 1 und Weg 3 geben für m_μ/m_e dieselbe Zahl 207.846 = √43200 — eine Route in zwei Sprachen.
- Gemeinsame offene Kante [S]: die fraktal-rekursive Korrektur (117ξ in Weg 1, 27ξ/12 in Weg 4, in cos(2/9) bei Weg 2) ist gemessen, nicht hergeleitet.
- Hinweis: Dok. 352 nutzt m_τ = 1776.86 (→ 117.4ξ); PDG 2024 gibt 1776.93 (→ 117.1ξ).

- Weg 5 (neu, Abschn. 4): Koide-Skala M = Σm/6 aus der T0-Leiter: M_bare = 314.82 MeV, Abw. 0.31 %, Korrektur +23.1ξ = gewichtete Summe der drei Einzelkorrekturen (τ-dominiert). M ist keine unabhängige Skala; keine Galois-native Einzelform M = c·ξ^p·v (Summe dreier ξ-Potenzen). Ausdrückliche Warnung vor Zahlenspielen (81√15 trifft 0.044 %, ist aber einer von zwölf Zufallstreffern ohne Korpus-Motivation).

- Nachtrag (20. Sept., Abschn. 4 „Zwei Lesarten der Korrektur"): Dok. 352 §10 (Lesart A: T0 fundamental, ε_i aus QED/SI-Projektion, R113-Brücke offen) neben Lesart B (Dok. 367: Koide fundamental, T0 = rationale Näherung, ε_i = Abstand Kosinus–Potenzgesetz ohne QED [K]). Beide geben dieselben Zahlen; B ist sparsamer, ihre offene Frage ist zahlentheoretisch (warum GF(3ⁿ)-Wicklungszahlen), nicht QED. → Register R121.

- Narrative Schlusssektion „Was der Korpus zeigt" (Abschn. 5): die zwei Genauigkeitsklassen sind keine Qualitätsstufen der Theorie, sondern die Grenze zwischen dem, was FFGFT aus sich heraus sagt (dimensionslose Verhältnisse, 10⁻³ %, parameterfrei) und dem, wofür sie einen externen Anker braucht (absolute Werte in MeV, Prozentniveau, ein deklarierter Anker v). FFGFT sagt die Form des Spektrums voraus, nicht seine Größe.

**Prüfskript:** `2/python/Dok369_Skripte/pruef_369_vier_wege.py` — 25/25 PASS.
**Register:** R121 (Dok. 352 §10: offener Punkt ε_i-Herkunft in Lesart B beantwortet, R113-Brücke nur noch in Lesart A nötig).

---

## 20. September 2026 — Dok. 370: Warum das Ikosaeder

### Dok. 370 — Drei, Fünf und das Nicht-Kommutieren (De 10 / En 9 Seiten)

Erklärungsdokument, rechnet nichts Neues. Erzählt, was Dok. 285, 293, 367, 368
zusammen bedeuten: FFGFT bringt eine ℤ₃ mit; φ ist die Zahl der Fünf; A₅ ist die
kleinste Gruppe, in der Drei und Fünf koexistieren ohne zu vertauschen. Die
FFGFT-ℤ₃ (Permutation C₃, Achse (1,1,1)) ist ohne Umdeutung eine 3-fach-Drehung
des Ikosaeders. Weil R₅ nicht mit C₃ vertauscht, mischt R₅ die Fourier-Moden;
die Mischungsgewichte haben eine rationale Komponente (2/9 = Koide-Phase) und zwei
φ-Komponenten (Skelett der Massenverhältnisse).

Einstieg über die Beobachtung (Koide-Formel, θ = 2/9 empirisch — warum?), dann Struktur.

**Neu gegenüber Korpus [K]:** die vollständige 3×3-Matrix |⟨v_j|R₅|v_k⟩|² (alle Zeilen/Spalten summieren zu 1); insbesondere die Zeile der symmetrischen Mode:
|⟨v₀|R₅|v_k⟩|² = (5, 2, 2)/9 — Amplituden (√5, √2, √2)/3, und 5+2+2 = 3².
Die Fünf des Ikosaeders und die Drei von FFGFT in einer Zeile. Spur R₅ = φ.

Neuer Abschnitt 5 „Wo das Ikosaeder wohnt: ausgerollt, nicht kompakt" (Verweise 285, 314, 364):
das Ikosaeder wirkt auf dem ausgerollten ℝ³ (T⁴ → ℝ³×S¹), nicht auf dem kompakten T⁴ mit D₄ —
dort ist A₅ unverträglich (5 ∤ 1152). Die Fünf tritt in FFGFT nicht als Gittersymmetrie ein,
sondern als Phase ζ₅ ∈ GF(81) (5 | 80); die Drei muss Gitter sein, weil in Charakteristik 3
keine primitive dritte Einheitswurzel existiert. Beide treffen sich im Körper, nicht in der
Geometrie. Die 364-Aussagen (φ⁴ = −1 in GF(9), 5 ∤ 1152, 5 | 80, x³−1 = (x−1)³ mod 3) in
Sitzung mit sympy verifiziert.

Schärfung aus dem IPI-Audit: ikosaedrische ℤ₃ (Spur 0, nicht-zentral) ≠
Orbifold-ℤ₃ (ω·𝟙, zentral). Nur die nicht-zentrale kann gemischt werden — das
Nicht-Vertauschen ist die Signatur, die FFGFT von einem Orbifold unterscheidet.

Abschnitt „Was offen bleibt" neu (20. Sept.): (1) Negatives Ergebnis: ζ₃₇ ∈ GF(3¹⁸), ζ₅ ∈ GF(81), und 4 ∤ 18 — die ikosaedrische Phase und die K_frak-Phase liegen in unverträglichen Erweiterungen; das Ikosaeder erklärt 37 nicht [B]. Grad 18 = 2·3² = Kompositum GF(9)·GF(3⁹); neue Primzahlen dort 19 und 37; warum 37 statt 19 offen [S]. (2) Fraktale Korrektur in Lesart B (Koide fundamental) hergeleitet als Abstand Kosinus–Potenzgesetz (R121). (3) Verbleibende offene Kante: Ikosaeder-Phasen (GF(81)) und Galois-Ordnungen (GF(3ⁿ)) berühren sich nur in GF(9) = φ; ob sie eine gemeinsame Wurzel haben, offen [S].

**Prüfskript:** keines (alle Zahlen aus 293/367/368 bereits geprüft; 5/9 und Spur φ
in Sitzung numerisch verifiziert).
**Register:** kein Eintrag (Erklärungsdokument).

---

## 20. September 2026 — IKO-Buch: Warum das Ikosaeder (populärwissenschaftlich)

### Buch — Drei, Fünf und das Geheimnis der Leptonmassen (De, 23 Seiten, 6×9 Zoll)

Populärwissenschaftliches Buch in 8 Kapiteln + Prolog + Anhang. Narrativ-Format,
Kindle-kompatibles 6×9-Zoll-Layout. Kein neues FFGFT-Ergebnis; Erzählung der
Befunde aus Dok. 285, 293, 338, 352, 364, 367, 368, 369, 370.

Kapitelstruktur: Prolog (die Zahl 2/9), Kap. 1 Das Rätsel (Koide 1981),
Kap. 2 Drei Teilchen (ℤ₃ / Trialität), Kap. 3 Das Ikosaeder (A₅, Drei und Fünf),
Kap. 4 Das Nicht-Vertauschen (Mischung, Tabelle (5,2,2)/9),
Kap. 5 Die eine Rechnung (Matrixelement, Koide-Formel),
Kap. 6 Zwei Welten (Torus kompakt vs. ausgerollt, Phasenkanal),
Kap. 7 Was die Theorie sagt — und was nicht (Verhältnisse vs. absolute Werte),
Kap. 8 Die offene Kante (GF(81) ⊄ GF(3¹⁸), φ als einzige Berührung),
Anhang (vollständige Formeln, Quellen).

**Quelldatei:** `2/Sources/ch/IKO_Buch_De_ch.tex` (Kapitel), `2/Sources/wr_narrativ/IKO_Buch_De.tex` (Wrapper).
**Prüfskript:** keines (alle Zahlen aus Prüfskripten der Quell-Dokumente).
**Register:** kein Eintrag.

---

## 21. September 2026 — Dok. 371: Der Faktor 4/3

### Dok. 371 — Kugelvolumen, Casimir-Operatoren, elektromagnetische Masse, das Tripel (3,4,5) und ξ (De/En, 9 Seiten)

Erweiterungsdokument zu den drei bestehenden Begründungen des Faktors 4/3 in
ξ = 4/3·10⁻⁴ (Dok. 006, 205, 324). Zwei neue Vorkommen:
- Der seit Abraham (1902)/Lorentz (1904) ungeklärte Faktor 4/3 der
  elektromagnetischen Elektronenmasse ist ein Dreidimensionalitäts-Effekt:
  4/3 = 2·(1 − 1/3), weil jede Feldkomponente ein Drittel der Energie trägt [E][B].
  Sitzt in derselben Größe, die in FFGFT als 1/ξ auftritt [S].
- C₂(SU(2)) = 3/4 und C₂(SU(3)) = 4/3 sind Kehrwerte; N = 2 ist der einzige
  Fall mit C₂(N)·C₂(N+1) = 1 [B]. Beide Werte sind Elektron-Invarianten
  (Spin, Masse) [S].
- Tripel (3,4,5): Berggren-Wurzel, einziges rechtwinkliges Dreieck in
  arithmetischer Folge, Inkreisradius 1, (2+i)² = 3+4i [B]; trägt das
  Kehrwertpaar als tan α = 4/3, cot α = 3/4.
- Enthalpiefaktor (u+p)/u = 4/3 bei p = u/3 (Photonengas, von Laue) als
  weiteres 3D-Vorkommen [E].
- Winkel arctan(4/3) = 53,13°: fehlt unter den kürzesten Vektoren von D₃/D₄ [X],
  tritt aber auf der Schale |v|² = 10 auf ((3,1,0,0), (1,3,0,0)), weil
  D₂ = (1+i)ℤ[i] und (1+i)(2±i) = 1+3i, 3+i [B]. Rolle dieser Schale in der
  FFGFT offen [S]. Berggren-Matrizen ∈ O(2,1;ℤ) [E].

**Prüfskript:** 2/python/Dok371_Skripte/ffgft_371_faktor_vier_drittel.py — 28/28 PASS
**Register:** kein Eintrag.

---

## 21. September 2026 — Dok. 372: Das Matrixelement-Prinzip

### Dok. 372 — Das Matrixelement-Prinzip und seine Reichweite (De, 8 Seiten)

Was aus |⟨v₀|R₅|v₁⟩|² = 2/9 über die Leptonmassen hinaus folgt.
- Reichweitensatz [B]: A₅ erzeugt in der ℤ₃-Modenbasis genau acht
  Matrixelement-Betragsquadrate {0, (5−3φ)/9, 1/9, 2/9, 4/9, 5/9, (2+3φ)/9, 1};
  alle Nenner 9 = |ℤ₃|².
- Leptonen [B]: Koide-Phase, Gewichte, φ-Skelett (p₁/p₂=φ⁸, p₀/p₂=2φ⁴), 4/3=2Q.
- Weinberg-Winkel [K]: on-shell 1−M_W²/M_Z² = 2/9 auf 0,4 % (Weltmittel 3,8σ,
  CDF 1,4σ); Vorhersage M_W = M_Z·√(7/9) = 80,420 GeV. Ersetzt den Kandidaten
  1/4 (8 %) aus Dok. 336; das MS-bar-Ergebnis 0,2308 aus Dok. 323 bleibt als
  Skalenfluss-Beschreibung im anderen Schema bestehen; Identität beider
  Beschreibungen offen [S].
- Atmosphärische Mischung [K]: sin²θ₂₃ ∈ {4/9, 5/9}; Oktant-Ambiguität der
  Daten = Ambiguität 4/9 ↔ 5/9; Vorhersage |sin²θ₂₃ − 1/2| = 1/18, maximale
  Mischung ausgeschlossen; PDG 0,558 trifft 5/9 auf 0,1σ.
- Cabibbo [S]: λ auf 1,2 % (4,1σ) bei 2/9; nicht identifiziert (Dok. 041
  hat eigene Herleitung).
- Negativ [X]: sin²θ₁₂, sin²θ₁₃, α_s liegen nicht in der Achtermenge —
  durch ein einzelnes A₅-Matrixelement nicht erreichbar.
- Matrixelement-Prinzip als allgemeine Hypothese formuliert [S].

**Prüfskript:** 2/python/Dok372_Skripte/pruef_372_matrixelement.py — 21/21 PASS
**Register:** kein Eintrag.
