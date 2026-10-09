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

### Dok. 372 — Das Matrixelement-Prinzip und seine Reichweite (De/En, je 12 Seiten)

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
- Abgleich mit Dok. 340 [B]: cos²(10π/13) ≠ 5/9 (Grad 6 gegen rational,
  nur numerisch nah); die cos²(2πk/13)-Lesungen sind Größenordnungen
  (12 Werte zu dicht). Arbeitsteilung: GF(27)* trägt Massen und
  Dirac/Majorana, A₅ trägt θ₂₃ und mit ξ θ₁₃; θ₁₂ bleibt offen [S].
  Nachtrag in Dok. 340 De/En.
- Quarks [X]: kompakte Leiter mit hergeleiteten pᵢ (Dok. 189: p = d_akt/3,
  Top −1/3 inverse Windung) und ξ-/K_frak-Gewichtung (Dok. 133, 005),
  ~1,2 % ohne freie Parameter; rᵢ angesetzt (n_φ²/(n_θ·n_c), Dok. 189),
  im Galois-Raster [B]. Q_up 0,85–0,89, Q_down 0,72–0,75 auf allen Skalen
  (PDG, M_Z, m_t, GUT) — mit A₅-Ausrollen (Q = 2/3 exakt) unverträglich;
  drei strukturelle Gründe; GF(729) als Einstieg [S]. Higgs steht in der
  p-Leiter bei p = 0 (Dok. 189), Vorfaktor r_h = 0,508 fehlt.
- Eichbosonen: v, α, sin²θ_W vorhanden [K]; M_W, M_Z bis auf Δr; Photon und
  acht Gluonen masselos [B] (Dok. 320/321/339).
- Higgs-Masse nicht hergeleitet [X]: Dok. 041 v·ξ^(1/4) liefert 26 GeV, nicht
  125; Λ_QCD = v·ξ^(1/3) liefert 12,6 GeV, nicht 200 MeV; Dok. 005
  m_t·φ·(1+ξD_f) braucht D_f ≈ −4100 (Fit). Nicht in der Achtermenge.
  Systematische Suche (17 Verhältnisse × 268 Zahlen): Treffer auf
  Zufallsniveau [X]; einziger strukturierter Kandidat M_Z : m_h : m_t =
  1 : 11/8 : (11/8)², m_h ≈ √(m_t·M_Z) (0,2 %, 1,6σ), 11 und 8 Galois-Größen,
  nachträglich ausgewählt [S].
- Matrixelement-Prinzip als allgemeine Hypothese formuliert [S].

**Prüfskript:** 2/python/Dok372_Skripte/pruef_372_matrixelement.py — 45/45 PASS
- §4 Hadronen: Q·n=1 algebraische Identität für entartete Multipletts [B] —
  Leptonen brechen sie (Q=2/3 statt 1/3, Faktor 2 ist A₅-Signatur); GMO-
  Aufspaltung konsistent mit m_s(Galois) [K]; Λ_QCD nicht aus ξ-Leiter
  ableitbar (p≈0,79, kein Leiterbruch) [X]. Ehrliche Grenze benannt.
**Register:** R122 (Higgs-Masse und Λ_QCD in Dok. 041/005 nicht haltbar [X]; offene Brücke).

---

## 21. September 2026 — Dok. 373: Yukawa-Mechanismus

### Dok. 373 — Der Yukawa-Mechanismus als Konsequenz von T̃·m=1 (De/En, je 11 Seiten)

Die massenproportionale Kopplung aller Fermionen ans Higgs-Boson (experimenteller
Fingerabdruck der Higgs-Entdeckung) folgt aus der FFGFT-Grundrelation T̃·m=1
unter räumlicher Fluktuation der Gitterskala v→v+h(x):
- y_i = r_i·ξ^{p_i} ist direkte Umschreibung der Torus-Topologie, keine freie Annahme [B]
- m_i(x) = m₀·(1+h/v) → L ⊃ -(m_i/v)·ψ̄ψ·h für alle i simultan [B]
- Yukawa-Vertex mit y_i = m_i/v folgt als Konsequenz, nicht als Parameter [B]
- Das Higgs-Teilchen h(x) ist das Schwingungsquant der Gitterskala (nicht
  eigenständiges Skalarfeld); Higgs-Potential und m_h bleiben offen [S] (R122)
- Vergleichstabelle SM vs. FFGFT

- §5: 11/8-Kette M_Z:m_h:m_t = 1:11/8:(11/8)² [K]: m_h = M_Z·11/8 = 125,383 GeV
  (0,15 %), m_t = M_Z·(11/8)² (0,10 %), M_W = M_Z·√(7/9) (0,06 %); 11 ∈
  GF(27)*-Orbit {7,11,21}, 8 = |GF(9)*|, sin²θ_W = 2/9 — alle Galois-Größen;
  V(h) ausstehend [S], R122 bleibt offen.

- §6 Spurregel [K]: M_W² + M_Z² + m_h² = v²/2 auf 0,45 %; Higgs-Teilchen =
  Reststeifigkeit des Gitters, m_h = √(v²/2 − 16/9·M_Z²) = 124,6 GeV.
  Begründet [B]: Spur unter Kopplung erhalten (Weinberg-Mischung = Drehung),
  leeres Vakuum → keine Eigensteifigkeit, W± eine komplexe Mode (Dok. 042/053),
  Faktor 1/2 aus kanonischer Normierung der komplexen Gitteramplitude.
  Mit 2/9 und 11/8: M_Z²/v² = 288/2113 → M_Z, M_W, m_h allein aus v auf
  0,17–0,31 % (Baumgraphen-Niveau); λ durch 4g²/7 + 2λ = 1/2 festgelegt.
  Fermionseite: Spurregel gilt nur für Gittermoden (W, Z, h); y_t = 1
  verworfen [X] (unbegründet, +1,2 %; Top-Masse schemaabhängig, Pol/MS-bar
  5,8 %); Top über m_t = (11/8)²·M_Z [K]. Genauigkeitsordnung: v-freie
  Polmassen-Verhältnisse 0,06–0,15 %, Relationen mit v 0,45 %; Rest der
  Spurregel vermutlich aus der SM-Definition von v (R112) [S].

- §7 Bestandsaufnahme des Teilchenzoos (Stand 21. Sept. 2026): Tabelle aller
  Sektoren mit bester Herleitung, Quelldokument und Status; Ordnungsprinzip
  (freie Moden und Gittermoden genau, Eingeschlossenes schemaabhängig,
  Galois-Verhältnisse genauer als v-Relationen); Liste der offenen Punkte.

**Prüfskript:** 2/python/Dok373_Skripte/pruef_373_yukawa.py — 35/35 PASS
**Register:** R122 aktualisiert (Higgs-Masse: Kandidaten über Galois-Kette und Spurregel; Λ_QCD bleibt offen).

---

## 22. September 2026 — Dok. 374: Gemeinsamer Anker

### Dok. 374 — Brückengleichungen zu Observer Patch Holography und die elektroschwache Skala als Treffpunkt (De/En, 9/8 Seiten)

Anlass: OPH-Tracking-Eintrag #740 (Länge und Takt folgen nicht aus den OPH-Updates).
OPH-Größen als zitierte Eingänge eines Fremdrahmens [Q]; kosmischer Sektor ausgeklammert (P39).
- B1: OPH-Zellenenergie = FFGFT-Bitenergie E_bit = ħc/L an der Zellkante √P·ℓ_P [B]
- B2: Kollapsschwelle (Dok. 329) an der Zellkante n_thr = √(P/2), Grenze P = 2, OPH darunter [B];
  unabhängig vom offenen Hadronenteil
- B3: Zellentakt T̃ = √P·t_P aus T̃·m=1 [B]; Anbindung an Laboruhr möglich, auf OPH-Seite
  noch nicht ausgeführt [S] (in FFGFT folgt sie aus T̃ = 1/m)
- B4: L_cell/L_0 = √P/ξ ≈ 9578 [K]
- Treffpunkt v: OPH v/E_star [Q, bedingt] × FFGFT m_e/v = (4/3)ξ^(3/2) [K] ergibt m_e/E_P
  auf −0,93 %; ein einziger SI-Anker legt beide Rahmen fest
- Referenzenergie E_star: OPH-Energieeinheit (Planck-Energie = 1 im Code), physikalisch per Uhr
  festzulegen; nicht reduzierte E_P auf 0,16 % [K], reduzierte um √(8π) ausgeschlossen;
  Empfindlichkeit π/(2α_U²) ≈ 929 macht 0,16 % zu enger Bedingung an α_U [B]; Lesart E_star = E_P [S]
- Zwei Wege zu m_e/E_P: eigene FFGFT-Kette ξ → G → ℓ_P → E_P (Dok. 012/013/180) auf +0,002 % [K];
  Aufteilung C_dim·C_conv in Dok. 180 gleichwertig; Genauigkeit je Rechenweg verschieden,
  Abweichungen je einer bekannten Stelle zugeordnet (bare-Leptonrest, Lesart E_star = E_P)
- Länge und Takt absolut über die FFGFT-Kette: L_cell = √P·ℓ_P = 2,064·10⁻³⁵ m,
  T̃_cell = √P·t_P = 6,885·10⁻⁴⁴ s [K]; Koeffizient der Lesart auf OPH-Seite abgeleitet,
  Issue 740 als ganzer dort offen (nachgeführt am 22.9., siehe Dok. 376)

**Prüfskript:** 2/python/Dok374_Skripte/pruef_374_anker.py — 30/30 PASS
**Register:** kein Eintrag.

---

## 22. September 2026 — Dok. 375: Die Hierarchie v/E_P

### Dok. 375 — Zwei Herleitungen im Vergleich: FFGFT und Observer Patch Holography (De/En, je 6 Seiten)

Anlass: Dok. 374 kombinierte m_e/v (FFGFT) mit v/E_star (OPH); FFGFT leitet v aber selbst ab (R104)
und erreicht E_P über die eigene Kette — v/E_P ist damit eine zweite, unabhängige Herleitung.
- FFGFT: v = m_e/((4/3)ξ^(3/2)) = 248,93 GeV; E_P über G = ξ²/(4m_e)·C_conv·K_frak;
  v/E_P = 2,0389·10⁻¹⁷ (+1,10 % gegen SM-v aus G_F) [K]
- Abweichung vollständig der bare-Rest der Leptonleiter (Dok. 352); Planck-Kette < 10⁻⁴ [K]
- OPH Theorem A: v/E_star = 2,0200·10⁻¹⁷ (+0,16 %) [Q], bedingt; Abstand der Herleitungen 0,93 %
- Empfindlichkeit: FFGFT ∂ln v/∂ln ξ = −3/2 [B], OPH π/(2α_U²) ≈ 929 in α_U
- FFGFT-Eintrag für die gehashte Vergleichstabelle mit Weg und SHA-256 (84fac85f…)

**Prüfskript:** 2/python/Dok375_Skripte/pruef_375_hierarchie.py — 11/11 PASS
**Register:** kein Eintrag.

---

## 22. September 2026 — Dok. 376: Der Koeffizient 8π und der Status von Issue 740

### Dok. 376 — Ein abgeleiteter Koeffizient auf OPH-Seite und die Rücknahme einer Aussage aus Dok. 374 (De/En, je 6 Seiten)

Anlass: Der OPH-Autor hat auf Johanns Frage (G oder 8πG) ein Theorem vorgelegt und den Stand von
Issue 740 ausführlicher dargestellt.
- Theorem [Q]: zwei Beobachter mit verschiedener Spannung erzwingen κ = b·L²/q; mit b = 2π
  (modularer Fluss) und q = 1/4 (Flächengesetz) folgt κ = 8π·L² und G = L² [K]
- Folge: E_star = ħc/L ist die nicht reduzierte Planck-Energie [B]; reduzierte Lesart um √(8π)
  daneben, also andere Normierung, keine Einheitenwahl
- Rücknahme: Die Aussage in Dok. 374, Issue 740 sei unter der Lesart E_star = E_P geschlossen,
  ist zurückgenommen und in Dok. 374 direkt korrigiert [X]; Längenidentität, Takt und Matching-Faktor bleiben auf OPH-Seite offen [Q].
  Brückengleichungen B1–B4 und absolute Skala über die FFGFT-Kette bleiben gültig
- Matching-Faktoren beider Rahmen: OPH v_F/v_Quelle = 0,9984 (0,16 %, offen),
  FFGFT v_F/v(ξ) = 0,98912 (1,10 %, bare-Rest der Leiter, Dok. 352/375) [K]

**Prüfskript:** 2/python/Dok376_Skripte/pruef_376_koeffizient.py — 9/9 PASS
**Register:** R124 (Rücknahme der Issue-740-Aussage in Dok. 374).

---

## 23. September 2026 — Dok. 377: Schnittstellen der FFGFT zu anderen Rahmen

### Dok. 377 — Vergleichs- und Brückendokumente, Berührungspunkte und überschneidende Größen (De/En, je 6 Seiten)

Übersichtsdokument, rechnet nichts Neues; fasst die vorhandenen Vergleichs- und Brückenarbeiten
zusammen und dient als Vorlage für eine Vergleichstabelle nach außen.
- Elf Rahmen mit Dokumenten: HLV (271, 272, 276, 282, 283, 285, 294, 297), OPH (364, 374, 375, 376),
  Hyperbit/Z₃C (324, 326, 336), XYLATIC (252), RA/PMT (269), Vopson (251), Matsas (105),
  ΛCDM (309), Kagome (361), SM-Lagrangedichte (049), Literatur (345); UIFT nur in 013/257 berührt
- Sieben überschneidende Größen mit Weg und Abweichung: α⁻¹ = 3700/27 (+7,6 ppm), sin²θ_W = 2/9
  (−0,52 %), λ_CKM = ξ^(1/6) (+0,46 %), v/E_P (+1,10 %), E_bit = ħc/L, Dimension 3+1, kosmischer
  Sektor ausgeklammert [K]
- Nur α⁻¹ und v/E_P werden von mehr als einem Rahmen beziffert; der Hadronsektor kommt in keinem
  Vergleich vor
- Brückenkriterium aus Dok. 283 als Maßstab übernommen

**Prüfskript:** 2/python/Dok377_Skripte/pruef_377_schnittstellen.py — 20/20 PASS
**Register:** kein Eintrag.

---

## 28. September 2026 — Dok. 378: Begutachtung unter heutigen Bedingungen

### Dok. 378 — Was im IPI-Austausch, in der Dot-Theory-Governance und in der FFGFT-Buchführung bereits vorliegt und was davon für ein Regelwerk verwertbar ist (De/En, je 12 Seiten)

Anlass: Diskussion, wie ein Peer-Review-Regelwerk an heutige Verhältnisse anzupassen ist
(Korpusumfang, unabhängige Forscher, Sprachmodelle, Mustersuche-Verdacht, Vereinfachung und Vorurteil).
- Ausgangslage: vier stille Voraussetzungen des klassischen Verfahrens, keine trägt heute allgemein
- Bestand: FFGFT-Statusmarker, Dok. 190, Prüfskripte/Nulltests, Negativbefunde (342, 361, 276), P35;
  Dot-Theory-Governance (Dok. 272: Lexicon/OAP/Matrix/FAH, O0/O2); CIL (Prinzipien 3, 6, 7, 8;
  Geltungsbereich an der Stelle der Herleitung); F O R M v1.0 (R = Residual); FER-Rekursion;
  Audit-Praxis (Hash-Freeze, Status wird vergeben, Reihenfolge deklarieren→einfrieren→implementieren→
  prüfen, Invarianten aus Block II, Rollentrennung, versiegelte Vorab-Vorhersage); Untaugliches
- Vorschlag: zehn Bausteine B1–B10 und gestufte Prüftiefe (Einstieg / Objekt / Tiefe)
- Grenzen: Aufwand, knappe neutrale Prüfer, Anerkennung, Vorurteil, Deutungshoheit gegen Prüfbefund
- Keine physikalischen Aussagen; methodische Bestandsaufnahme mit Vorschlagscharakter

**Prüfskript:** 2/python/Dok378_Skripte/pruef_378_verweise.py — 25/25 PASS
**Register:** kein Eintrag.

---

## 29. September 2026 — Dok. 379: Das akustische Plenum und das Photon

### Dok. 379 — Lien (2026) im Licht von Dok. 267, 290, 340, A265 und R128 (De/En, je 8 Seiten)

Anlass: Zenodo-Arbeit von C. C. Lien („Electromagnetic Illusion“, DOI 10.5281/zenodo.21800087), die den Raum als kompressibles Superfluid deutet und Elektron, Myon, Tau, Neutrino und Photon daraus ableiten will. Fallstudie mit Prüfskript.
- Nachrechnung: alle sechs Zahlenangaben reproduzierbar [K]
- Elektron aus 2π·α⁻⁴·k_BT_CMB/h: +1,84 %, rund 88 σ neben dem Messwert; Nulltest: dieselbe Formelfamilie (546 Formeln) trifft 61 % zufälliger Zielwerte ebenso gut — nicht signifikant [X]
- Leptonformel ist Baruts Formel (PRL 42, 1251, 1979) unverändert [B]; n = 3 ergäbe ein geladenes Lepton bei 10,3 GeV, ausgeschlossen [X]
- Neutrino m_ν = k_BT_CMB = 0,235 meV unverträglich mit Δm²_atm [X]; Dok. 340 erfüllt die Bedingung [K]
- Rotverschiebung durch Dämpfung: Dämpfung ändert die Amplitude, nicht die Frequenz [K]; ∝ f² wäre chromatisch [X]; FFGFT: achromatische (1+z)-Dehnung aus T̃·m = 1 (Dok. 312, A265, R128)
- Photon als Längs- plus Querwelle ergäbe drei statt zwei Freiheitsgrade [X]; FFGFT-Photon exakt masselos, reiner Phasenanker (Dok. 290)
- Gemeinsamer Anker m_ec²/k_BT_CMB (A265): Liens Kandidat schließt P20 nicht [S]
- Übereinstimmung nur im Ausgangspunkt (stationärer Hintergrund, keine Singularitäten); ρ_E zirkulär über r_e

**Prüfskript:** 2/python/Dok379_Skripte/pruef_379_lien_photon.py — 20/20 PASS
**Register:** kein Eintrag.

---

## 29. September 2026 — Dok. 380: Warum D₄

### Dok. 380 — Spezifität des Trägers gegen angepasste Vergleichsgitter (R95) (De/En, je 7 Seiten)

Anlass: offene Brücke R95 (adversarieller D₄-Spezifitätstest nach GAE-Logik); Werkzeug: EpsteinLib (Buchheit, Busse, Gutendorf, arXiv:2412.16317).
- Vergleichsträger bei gleichem Volumen der Grundmasche: ℤ⁴ (Gewinner im HLV-Audit), A₄, A₂⊕A₂, D₄, Zufallsgitter
- K1 fixpunktfreie ℤ₃ mit 9 Fixpunkten (Korpusbedingung, Dok. 330): ℤ⁴ und A₄ ausgeschlossen, A₂⊕A₂ und D₄ verträglich [K]
- Klassifikation: |Aut(D₄)| = 1152, davon 80 der Ordnung 3 — 64 mit 2D-Fixraum (darunter die Dynkin-Trialität), 16 fixpunktfrei mit 9 Fixpunkten = die 16 Elemente aus Dok. 330 [K]
- K2 Kusszahl D₄ 24, A₄ 20, A₂⊕A₂ 12, ℤ⁴ 8 — nur Konsistenz, da 24 in Dok. 340 verwendet [K]
- K3 Gitterenergie (Epstein-Zeta, ν = 5, 6, 8), einziges FFGFT-unabhängiges Kriterium: D₄ jeweils minimal; keines von 600 Zufallsgittern darunter; 200/200 Störungen erhöhen die Energie [K]; bewiesen nur lokale Optimalität (Sarnak–Strömbergsson 2006) [Q], globale Minimalität in 4D offene Vermutung
- Ergebnis: D₄ als Träger besser motiviert, bleibt motivierte Setzung; R95 nicht geschlossen, Operatortest offen [S]

**Prüfskript:** 2/python/Dok380_Skripte/pruef_380_d4_spezifitaet.py — 13/13 PASS
**Register:** kein Eintrag.

---

## 29. September 2026 — Dok. 381: Die laufende Rekursion exakt aufsummiert

### Dok. 381 — Teleskopprodukt, zweite Ordnung und Ein-Schleifen-Lesart zu Dok. 295 und 333 (De/En, je 7 Seiten)

Anlass: Frage nach der gegenseitigen Beeinflussung von Rekursionen und fraktaler Korrektur, Vergleich mit Cluster-Entwicklungen (Buchheit, GZL/EpsteinLib).
- Teleskopprodukt ∏(1 − 100ξ_k) = ξ_n/ξ_0 exakt [B], in Bruchrechnung für n = 1..12 bestätigt [K]
- Kontinuum zweiter Ordnung 1/ξ_n ≈ 100(n+75) + 100·ln((n+75)/75): 50- bis 700-mal genauer als die erste Ordnung aus Dok. 295 (max. 0,49 % bei n ≈ 100) [K]
- Multiplikative minus additive Buchhaltung → ψ′(75)/2 = 0,00671 [K]
- Beschränkte Konstante ≈ 0,0134 zwischen Masse- und Zeitdefekt aus Dok. 295 = ψ′(75) = Σ(k+75)⁻² [K]
- Ein-Schleifen-Form dξ/dn = −100ξ² eindeutig, Koeffizient b = 100/ln s konventionsabhängig (e: 100, 2: 144, 3/2: 247, Dekade: 43) [S]
- Potenzform A040: D_f^eff = 2,973032 für exakt 74/75 [K]
- Offen: physikalische Schrittkonvention; Überschneidung gleichzeitig laufender Korrekturen (Inklusion–Exklusion) [S]
- Dok. 295 bleibt in allen Aussagen gültig

**Prüfskript:** 2/python/Dok381_Skripte/pruef_381_rekursion_ansaetze.py — 14/14 PASS
**Register:** kein Eintrag.

---

## 29. September 2026 — Dok. 382: Myon g−2: Stand 2025

### Dok. 382 — Fermilab-Endergebnis, White Paper 2025 und Einordnung der FFGFT-Aussagen (De/En, je 8 Seiten)

Nachfolgedokument zum Stand der Myon-g−2-Anomalie; die betroffenen älteren Dokumente verweisen darauf.
- Weltmittel 2025 (E821 + E989) 116 592 071,5(14,5)·10⁻¹¹, White Paper 2025 (HVP aus Gitter-QCD) 116 592 033(62)·10⁻¹¹; Differenz 38(63)·10⁻¹¹ ≈ 0,6σ statt 251(59)·10⁻¹¹ ≈ 4,2σ (2021); geändert hat sich die SM-Rechnung, der Messwert nur um ≈ 10·10⁻¹¹ [K]
- Typ (a), T0-Zusatzbeitrag Δa_μ = 251·10⁻¹¹ als Erklärung der Anomalie (Dok. 019, 030, 033, 049, 053, 059, 070, 081, 095; A138): überholt, läge heute ≈ 3,4σ über der Differenz [K]; Spielraum für einen Zusatzbeitrag bei 2σ etwa −88 bis +164·10⁻¹¹ [K]; ein T0-Beitrag dieser Größe ist nicht hergeleitet [S]
- Tragende Verhältnis-Linie (Dok. 018 Rev. 12, 158, A138) nicht betroffen: Δa(τ−μ)/Δa(μ−e) = f^{1/3} − 1 = 18,57, Brücke Δa(τ−e)/Δa(μ−e) = (144/125)·m_τ/m_μ = 19,37 [K]; Absolutwert durch Verankerung an gemessenem a_e, a_μ: a_τ = 1,2811·10⁻³ (Stand 2025), besser als die direkte Formel 1,2454·10⁻³ [K]; Anker a_μ − a_e seit 2021 praktisch unverändert [K]; 1,04·10⁻⁴ über dem SM-Wert, heutige Schranken rund 600-mal weiter, offen bis zur Messung [S]
- Direkte Absolutformeln (K_frak^{3/2}): a_e 0,014 %, a_μ −0,15 % – kein Präzisionsvergleich auf 10⁻⁹-Niveau; die direkte Differenz 4π/f^{5/3} liegt 30 % unter der gemessenen, was den verankerten Weg begründet [K]; der Vergleich mit der „Myon-Diskrepanz“ in A138 ist gegenstandslos
- Hinweis nach dem Abstract in Dok. 019, 030, 033, 049, 053, 059, 070, 081, 095 und A138 (De/En)

- Prüfskript angepasst (2. Okt. 2026): Die Schranken-Prüfung rechnete mit der älteren DELPHI-Schranke (−0,052 … 0,013, Faktor 626), der Text nennt CMS 2024 (−0,0042 < a_τ < 0,0046, 95 % CL); jetzt geprüft: Intervall 84,7-mal breiter als der Abstand zum SM-Wert, beide Werte darin

**Prüfskript:** 2/python/Dok382_Skripte/pruef_382_myon_g2_stand.py — 21/21 PASS
**Register:** kein Eintrag (Hinweise direkt in den betroffenen Dokumenten).

---

## 29. September 2026 — Dok. 383: Massen und Planck-Skala ohne v

### Dok. 383 — Eine Kette, ein Anker (De/En, je 8 Seiten)

Anlass: Frage, ob sich Planck-Länge und Massen aus ξ allein mit nur einem Anker herleiten lassen; v ist Zwischengröße und lässt sich auflösen.
- Beziehung aus Dok. 149: v = E_P/(f⁴·(π/2)·10) ⇔ v/E_P = ξ⁴/(5π) [B]; = 2,0120·10⁻¹⁷, −0,23 % gegen Messung, dimensionslos, ohne Anker [K]; Faktor 10 motivierte Setzung, nicht hergeleitet [S]
- Dok. 149 rechnet mit f = 7491,91 → 246,71 GeV; mit f = 7500 → 245,65 GeV [K]
- Massen ohne v: m_i = r_i/(5π)·ξ^{p_i+4}·E_P [B]; e 4/(15π)ξ^{11/2}E_P = 0,5043 MeV (−1,32 %), μ 16/(25π)ξ⁵E_P = 104,81 MeV (−0,80 %), τ 5/(9π)ξ^{14/3}E_P = 1780,9 MeV (+0,23 %) [K]
- Ein Anker m_e → E_P = 1,2372·10¹⁹ GeV (+1,34 %), G = ħc⁵/E_P² = 6,4995·10⁻¹¹ (−2,6 %), ℓ_P = 1,5950·10⁻³⁵ m, L₀ = ξℓ_P = 2,1266·10⁻³⁹ m [K]; Ankerwahl frei: μ → E_P +0,81 %, τ → −0,23 %, v → +0,23 % [K]; Streuung = bare-Rest der Leiter
- C_conv bleibt SI-Umrechnung von G (enthält den Messwert von G); die Ein-Anker-Kette entspricht C_conv = 7,58·10⁻³ statt 7,783·10⁻³ [K]; Weg von Dok. 375 (2,0389·10⁻¹⁷) und direkter Wert unterscheiden sich um genau den Elektronrest (Faktor 1,0134) [K]
- Vermerke (29. Sept. 2026) in Dok. 149 (Hinweis bei v; Tippfehler f⁴ = 3,155 → 3,150·10¹⁵, ρ_4D 3869 → 3875 GeV korrigiert), Dok. 150 (Formel für v in Tabelle und Gleichung korrigiert), Dok. 180 (ℓ_P-Wert ist Messwert als Anker; Ein-Anker-Wert), Dok. 375 (v/E_P direkt = ξ⁴/(5π)), jeweils De/En

**Prüfskript:** 2/python/Dok383_Skripte/pruef_383_ein_anker.py — 20/20 PASS
**Register:** kein Eintrag (Korrekturen und Hinweise direkt in den betroffenen Dokumenten).

---

## 1. Oktober 2026 — Dok. 384: FFGFT in Kurzfassung

### Dok. 384 — Grundlagen, Ergebnisse und Status nach der Rechenprüfung (De/En, je 23 Seiten)

Zusammenfassung des gesamten Korpus (Dok. 001–383, A-Serie) auf dem Stand nach der Nachrechnung vom 29. Sept. bis 1. Okt. 2026; jedes Ergebnis mit Formel, Zahlenwert, Vergleichswert, Status und tragenden Dokumenten.
- Architektur: drei Grundannahmen T̃·m = 1, T⁴, ℤ₃ (R56) und D₄ als motivierte Wahl [S]; einziger Parameter ξ = 4/30000 [S]; α = 1 mit angepasstem e [Q]; kosmischer Sektor ausgeklammert (P39)
- Grundlagen: K_frak = 74/75 Wert [K], Rest 1,7·10⁻⁴ und Form offen (R135, R139); E₀ = 7,348/7,397 MeV, α-Übereinstimmung Eigenschaft des Ankers (R135); Ein-Anker-Kette v/E_P = ξ⁴/(5π), m_i = r_i ξ^{p_i+4} E_P/(5π) [B], Ankertabelle [K]; L₀, T₀, Rekursion und Log-Spirale; F̂ selbstadjungiert auf P₀ (R145); Galois-Struktur
- Teilchen: Leptonleiter (+0,52 %, +1,03 %) [K], r_i, p_i [S]; Koide −0,017 ξ (PDG 2024); (√2, 2/9) für m_μ/m_e 442σ [X]; v-Wege 248,3/248,9/245,6/245,65 GeV; Quarktabelle als Kodierung [S]; Neutrinos Δm² −1,0 %/+0,46 %, m_ee 6,0/0,13/0 meV; a_τ = 1,2811·10⁻³; M_W 3,8σ; m_h, m_t Kandidaten; Ladungsquantisierung [B], Hyperladung geladener Leptonen offen (R146)
- Gravitation und Kosmos: G-Form [K], Präzision kein Beleg (R141); Schwarze Löcher (R144); Casimir-CMB Identität (R136); H₀/Λ bedingt auf P20; Galaxien
- QM: Bell-Verletzung bleibt, ξ-Effekt nicht auflösbar (R142, R143); IBM-Messung 28. Mai 2026
- Higgs-Geometrie als Konsistenzprüfung von ξ: ξ_EFT = m_h²/(64π³v²) = 1,30·10⁻⁴, rund −2,3 % mit PDG 2024 (−2,6 % nur mit gerundetem λ_h = 0,129; Dok. 354, A190, 385) [K]; die Verkürzung auf 1/(16π³) steht als Vermerk in Dok. 320
- Unabhängig gegengeprüft (rund 75 Aussagen); ν₃-Dirac-Zuordnung (R108) als Spannung zu Dok. 346 ausgewiesen
- Überarbeitet (1. Okt. 2026, abends): Schwerpunkt auf Verhältnisse und natürliche Einheiten. Neue Gliederung: Was FFGFT ist (zuerst „Verhältnisse in natürlichen Einheiten“) → Die Grundform (ħ = c = 1, α = 1, e = √(4π), α = r_e/λ_C, ξE₀² = 1; Dualität; ξ mit Higgs-Prüfung als Verhältnis m_h/v; Skalen als Verhältnisse L₀/ℓ_P = T₀/t_P = ξ, v/E_P = ξ⁴/(5π), m_i/E_P; Rekursion mit Rotationszahl 74/75) → Teilchen als Verhältnisse (Leiter m_i/v, Koide, Neutrino-Verhältnisse 1 : √(14/3) : 11 und Δm²_atm/Δm²_sol = 32,7 (−1,4 %), m_h/M_Z = 11/8, m_t/M_Z = (11/8)², Ladung) → Die Übersetzung in SI (ein Anker, v, K_frak nur hier, E₀ und α_SI mit Bezugsenergie, G); Tabelle der prüfbaren Aussagen getrennt nach Verhältnissen und Absolutwerten; Leseführer um A080/A085, A130/A267, 122, 385, 386 ergänzt
- Tabellen: prüfbare Aussagen, Statusbilanz, Leseführer; Abschnitte „Was nicht mehr gilt“ und „Offene Brücken“ (Stand R147)
- Erweitert (2. Okt. 2026): neuer Abschnitt „Ikosaeder und goldener Schnitt: das φ-Skelett“ aus den Dokumenten über 300, die in der A-Serie noch fehlen (Dok. 293, 364, 367, 368, 370). A₅-Gewichte p₀ = θ = 2/9, p₁/p₂ = φ⁸, p₀/p₂ = 2φ⁴ [B]; m_τ/m_e = (74 + 1/45)φ⁸ = 3477,469 gegen PDG 3477,37 ± 0,18 (+3,0·10⁻⁵, 0,6σ) [K], so genau wie Koide; 74φ⁸ allein −5,3σ; Faktoren 74 und 1/45 beobachtet [S]; 37 kommt nicht aus dem Ikosaeder [B]; für m_μ/m_e kein φ-Weg auf diesem Niveau (30φ⁴ −0,55 %). Abgrenzung zur widerlegten φ-Massenleiter; Kurzfassung, prüfbare Aussagen, Statusbilanz, offene Brücken, Leseführer und Fazit ergänzt

- Neu formatiert (2. Okt. 2026), Inhalt unverändert: farbige Statusmarker, Kernformeln in Kästen, Leitlinien, zurückgenommene Ansprüche, Lesarten von ξ, v-Wege, „Was nicht mehr gilt“ und Leitplanken als Listen bzw. Tabelle, Higgs-Prüfung und Grenzen des φ-Wegs als Kästen, Zeilenfarben in den Tabellen

- HTML-Fassung (2. Okt. 2026): 2/html/384_FFGFT_Kurzfassung_{De,En}.html (eigenständig, Formeln als MathML), erzeugt mit 2/python/Dok384_Skripte/mk_384_docx_html.py aus der LaTeX-Quelle; die Word-Fassung liegt nicht im Repo (Skript mit --docx erzeugt sie als Vorlage für Google Docs)
- Abschnitt „Verwendung von KI-Werkzeugen“ ergänzt (De/En)
- Erweitert (2. Okt. 2026, abends): neuer Abschnitt „Resonanz als Grundgedanke: das Eulersche Tonnetz“ (Dok. 060, 189, 310, 315, 316, 328, 343, 358): Teilchen als Schwingungsmoden, Massenverhältnisse als Periodenverhältnisse, Harmonik und Galois als zwei Darstellungen eines Objekts (358 Satz D) [B]; Messwert als Kammerton (310); 1/ξ = 7500 = 2²·3·5⁴ als Tonnetz-Punkt (−2, −1, −4) [K]; sieben von neun Yukawa-Vorfaktoren 5-Limit, Ausnahmen 13 und 7 als Galois-Primen (358 Satz B) [B]; Massenleiter als logarithmische Resonanzskala mit Terz ξ^(1/3); Komma als Einbettungsfehler, im endlichen Körper kein Komma (358 Satz A) [B], ξ-Zyklus schließt nach 75 Umläufen mit Rotationszahl 74/75 (315) [B]; Kopplungsregime (328); Grenzen der harmonischen Lesart (316, 343). Zusammenfassung, Leseführer und Fazit ergänzt; PDF und HTML neu erzeugt
- Quantenmechanik ausgebaut (2. Okt. 2026, abends): deterministische Lesart in drei Punkten — Messung als Polübergang A(z,λ) = sgn(z − λ) statt Kollaps (Dok. 230, 175), Born-Regel als geometrischer Quotient (1+z)/2 nach Archimedes [B], Zufall epistemisch, Hidden-Measurement-Modell von Aerts als nächster Verwandter [Q]; Rauschen als ungeordnete Phase, Vakuumrauschen als Überlagerung deterministischer Harmonischer [S], deterministisch, aber nicht nachrechenbar (Dok. 183); Bell und Kochen–Specker schließen nur lokale bzw. nicht-kontextuelle Modelle aus. Neuer Absatz „Shor in der deterministischen Lesart“: Aufbereitung O(n³) gegen Transformation O(n²) als Resonanz (Dok. 176), Quantenrechner als Analogrechner mit QM-Präzision, Schwellentheorem bei Skalierung [S] (Dok. 343, Satz G′); bisheriger Satz „ein von Shor unterscheidbares Verfahren existiert nicht“ präzisiert: zurückgezogen ist nur das eigene T0/ξ-Verfahren (R65), nicht die deterministische Deutung desselben Algorithmus; Leseführer um 176, 183, 343 ergänzt
- Präzisiert (2. Okt. 2026, abends): deterministisch und nachrechenbar bis zur Rauschgrenze (Phasenfehler erreicht sie nach etwa π/(2ε) Schritten, Dok. 183), darüber keine Unterscheidung; wiederholte Messungen braucht die deterministische Lesart nicht, die probabilistische Auswertung stößt an denselben Boden mit natürlicher Skala ξ (Dok. 343, G′). Shor: Vorteil sitzt allein in der Periodenfindung, Aufbereitung (fester Faktor) und Fehlerkorrektur kosten auf Quantenhardware mehr als klassisch; netto entscheidet die Fehlerkorrektur bei Skalierung [S]; im erreichbaren Bereich faktorisiert ein klassischer Rechner ebenso schnell; mit ξ als Boden N_max ≈ 1/ξ = 7500 (13 Bit), Zeitvorteil verschwindet strukturell [S]
- Casimir und CMB: Hinweis auf Dok. 388 (T_CMB/m_e = (8π)^(1/4)ξ^(5/2), 0,12σ; T⁴ = 16 H₀ m_e³; L_ξ ohne CMB) [S]; Korpusumfang 001–388; Leseführer ergänzt
- Ergänzt (2. Okt. 2026, abends): vierter Punkt der deterministischen Lesart „Gatter sind geometrische Drehungen“ — Pauli-Matrizen als Rotationen auf dem Bloch-Zylinder, CNOT als geometrische Konditionierung, mit {H, T, CNOT} universell, jedes Gatter deterministisch und ohne Wiederholung nachbildbar bis zur Rauschgrenze (Dok. 230, 175); Shor-Absatz: alternative Rechenoperationen (optische bzw. Resonator-FT Dok. 176, analoge Matrixfaltung und Resonator-Einrasten Dok. 186, BAW-Ising-Maschine Dok. 362), alle mit demselben Auflösungsboden, Standard-QM-Rechnungen bleiben verwendbar; R65 präzisiert (zurückgezogen nur die Behauptung von Shor unterscheidbarer Ergebnisse); [X] hinter verneinten Sätzen entfernt, Legende: hinter einem verneinten Satz gilt [X] der verneinten Behauptung
- Statusmarker im QM-Abschnitt nach Prüfung der Quellen (2. Okt. 2026, abends): Polübergang und Born-Quotient [K] (pruef_230_zylinder_born.py, 9/9), Gatter als Drehungen [K] (neu nachgerechnet: exp(−iθn·σ/2) = Drehung R_n(θ), Pauli, Hadamard, CNOT als konditionierte Drehung in einem Lauf), Rückrechnung eines Zufallsphasen-Spektrums mit bekannten Phasen [K], Nachrechenbarkeit bis N_krit = π/(2ε) und Mittelung am Boden [S], Bell/Kochen–Specker [Q], Shor-Ressourcen [K] (Shor_Skripte/s2_grenzen.py); „95 % der Gatterkosten“ (aus einer Wiki-Quelle in Dok. 176, dort als [K] geführt) ersetzt durch den gerechneten Anteil 1 − 1/(n+1) = 99,95 % bei 2048 Bit [K]. Tabelle „Prüfbare Aussagen“: Zeilen m_τ aus Koide und a_τ mit ausgeschriebenen Fußnoten unter der Tabelle („offen (Fußnote 1)“: Koide-Wert 1776,97 MeV, 0,4σ, aber BESIII-Schwellenscan und Belle-II-Pseudomasse streuen um 0,18 MeV, das Doppelte der Unsicherheit, R113; „offen (Fußnote 2)“ zu a_τ (noch nicht gemessen, CMS 2024 −0,0042 < a_τ < 0,0046, Intervall 85-mal breiter als der Abstand FFGFT–SM, Entscheidung mit etwa hundertfach genauerer Messung, Belle II), Faktor 85 im Prüfskript nachgerechnet. Vorgemerkt: Dok. 175 hat weder Marker noch Prüfskript, Dok. 183 nur [S], Dok. 176 führt die 95 % als [K] ohne Rechnung
- Einordnung „Erklärung statt Präzision“ (2. Okt. 2026, abends): neuer erster Punkt unter „Was der Korpus heute nicht mehr behauptet“ (FFGFT ist keine Präzisionserweiterung des Standardmodells; wo dieses rechnet, dieselben Werte oder gemessene Anker, kein messbarer genauerer ξ-Zusatz, R142, Dok. 382; bei freien Parametern Struktur auf Prozent- bis Promille-Niveau); fünfte Leitlinie „Erklärung vor Präzision“; Fazit eröffnet mit „liefert Erklärungen, keine größere Genauigkeit als das Standardmodell“
- Neuer Unterabschnitt „Feldtheorie: Lagrange-Dichte, Moden-Operator, Schrödinger-Limes“ (2. Okt. 2026, abends; A075, A070, A142, Dok. 019, 129): Lagrangian ½(∂δm)² + εξ[…], Funktionen f(ϑ), k^{μν} offen [S]; T̃·m = 1 folgt nicht aus einer Variation (Dok. 129); Brückenformel ∫½(∂δm)² = ½⟨ψ|Φ²|ψ⟩ [B], am Torus-Beispiel nachgerechnet [K] — Massen als Eigenwerte, nicht als Lagrangian-Parameter; Schrödinger als Niederenergielimit über die Madelung-Zerlegung [Q], nachgerechnet [K]; Dirac über Clifford-Algebra; Gravitation mit konformer Kopplung und Γ = −∂m/m [K]; drei Stellen aus A075/A142 mit Vermerk (SM-Grenzfall nur skalar [S], a_e-Zusatz ausgeschlossen [X]); modifizierte Schrödinger-Gleichung: mit 𝒯/𝒯₀ = 1/Ω homogen, Amplitude folgt der lokalen Energiedichte (keine Wahrscheinlichkeit, Dok. 230), Phase im lokalen Takt = gravitative Rotverschiebung (Dok. 078) — die Gravitation ist enthalten [B][K]; Leseführer um Zeile „Feldtheorie“ ergänzt
- Vermerke vom 2. Okt. 2026 in den älteren Dokumenten zur Schrödinger-Gleichung und zum Lagrangian (De/En, mit Korrekturkasten wo vorhanden): zeitfeldabhängige Schrödinger-Formen in Dok. 004, 020, 037, 067, 095, 129, 131 — mit dimensionsbehaftetem T inhomogen, mit T/T₀ Phase im lokalen Takt und Amplitude als Energiedichte (keine Wahrscheinlichkeit, Dok. 230), also die gravitative Rotverschiebung; kein zusätzliches Feld, kein Graviton, die Gravitation zeigt sich als Wirkung in der Rotverschiebung, gelesen als Raumkrümmung, Massenänderung (Dok. 078) oder fraktale Wegverlängerung (Dok. 041); zusätzlich Dok. 067 Dimensionsprüfung unzutreffend, Dok. 095/131 V_T0 keine Energie, Dok. 095 Myon-Anomalie überholt (Dok. 382), Dok. 037 fraktale Terme spekulativ; Dok. 129 |ψ|² als Energiedichte; Dok. 202 Hinweis bei den Parallelableitungen; Dok. 067 a_e-Zusatz: 2,34·10⁻¹⁰ nur mit α = 1, physikalisch 1,7·10⁻¹², gegen Messung minus QED (+3,4(1,6)·10⁻¹³ Rb, −10,1(2,7)·10⁻¹³ Cs) 8,6σ bzw. 10σ, ausgeschlossen; Dok. 354 „enthält den SM-Lagrangian als Grenzfall“ nur QED-Teil der Leptonen

**Prüfskript:** 2/python/Dok384_Skripte/pruef_384_zusammenfassung.py — 118/118 PASS
**Register:** kein Eintrag.

---

## 1. Oktober 2026 — Dok. 385: Der Higgs-Vakuum-Weg zu ξ

### Dok. 385 — Herkunft, Formeln und Status einer Konsistenzprüfung (De/En, je 8 Seiten)

Anlass: Der ursprüngliche Weg zu den Zusammenhängen der FFGFT lief über Vakuum und Higgs-Feld; die Formel mit ε₀ wird anhand der Versionsgeschichte (Feb. 2025 bis heute) verfolgt und nachgerechnet.
- Formelkette 2025: 31.3. Faktor 16π³ mit r₀; 5.4. ξ = λ_h²v²/(16π³m_h²) (genannt 1,33·10⁻⁴, richtig 1,30·10⁻⁴) [B]; 6.4. Vakuumformel λ_h²v²e²/(64π⁴ε₀ħc m_h²) = 1; 18.4. Variante mit μ₀/ε₀; 25.5. ε₀ eliminiert (64π⁴ → 16π³); ab 1.6. Ableger 64π⁴ mit 1,04·10⁻⁵; 22.8.2026 Verkürzung in Dok. 320
- Vakuumformel ausgeschrieben = ξ_EFT·α [B]; SI-Wert 9,5·10⁻⁷ [K]; mit α = 1 genau ξ_EFT [B]; 64π⁴ = 16π³·4π, das 4π aus 4πε₀
- Heutiger Stand: ξ_EFT = m_h²/(64π³v²) = λ_h/(32π³) = 1,30·10⁻⁴, rund −2,3 % mit PDG 2024, Spanne −2,2 bis −2,4 %, −2,6 % nur mit gerundetem λ_h = 0,129 [K]; Konsistenzprüfung, Abweichung strukturell gedeutet [S] (R59)
- Nicht tragfähig [X]: Gleichsetzung mit 1 (β_T = 0,977), μ₀/ε₀-Variante (Dimension GeV⁴, ~4·10⁵), 64π⁴-Form 1,04·10⁻⁵, Verkürzung λ_h = m_h/v auf 1/(16π³) mit Iteration (läuft gegen 0); Verwechslung y = λ_h schon in Dok. 097
- Angeglichene Stellen (Vermerke 1. Okt. 2026): Dok. 006, 046, 049, 054, 061, 067, 068, 073, 175, 189, 310, 320, 354, A142 (De/En), Dok. 186 (Herkunft 64π⁴), OntologischeAequivalenz (De/En), T0-test (De/En) rechnet λ_h aus m_h und v (T0-test_En zusätzlich a_rad mit Faktor 15 statt 30 wie in der De-Fassung); Dok. 384 auf rund 2,3 % und Verweis auf Dok. 385

**Prüfskript:** 2/python/Dok385_Skripte/pruef_385_higgs_vakuum.py — 17/17 PASS
**Register:** kein Eintrag.

---

## 1. Oktober 2026 — Dok. 386: Wo α steckt

### Dok. 386 — Ladungseinheit, zwei Kugeln und ξ als Fläche (De/En, je 8 Seiten)

Anlass: Die FFGFT ist in ihrer Grundform verhältnisbasiert (natürliche Einheiten, α = 1, umdefinierte Ladung, ohne fraktale Korrektur); gefragt war, wohin α bei der Umdefinition wandert und welche geometrische Bedeutung es dort hat.
- Umdefinition: ħ = c = ε₀ = 1 → e² = 4πα; mit α = 1 ist e = √(4π), die Ladung wird über die volle Kugeloberfläche gemessen [B]; α = (e_hist/e_geo)², e_geo/e_hist = 11,706 [B]; α = 1 als Recheneinheit [Q] (A267)
- Geometrisches Bild: α = r_e/λ_C, a₀/λ_C = 1/α; Coulomb- und Compton-Kugel des Elektrons, α = 1 lässt sie zusammenfallen [B]; dasselbe 4π wie im Faktor 64π⁴ der Vakuumformel (Dok. 385)
- Verhältnisform der Brücke: ξE₀² = 1, also E₀² = 1/ξ = 7500 in T0-Einheiten [B]; geometrisch ξ = λ_e·λ_μ = r_e·λ_μ, die Fläche der Compton-Kugeln von Elektron und Myon [B]; 7500 = 100·75 ist dieselbe Zahl wie in der Rekursion (ξ₀ = 1/7500, Rotationszahl 74/75) [B]; r : λ_C : a₀ = α : 1 : α⁻¹ für jedes geladene Teilchen [B]; T0-Energieeinheit √(ξ m_e m_μ) = 84,85 keV [K]; SI-Gegenstück r_e·λ_μ = (ξ/K)(ħc/MeV)² (+1,7·10⁻⁴) [K]
- Gliederung: Grundform (natürliche Einheiten, Verhältnisse) vorne und ausgebaut, Übersetzung in SI als ein zusammengefasster Abschnitt
- SI-Brücke α_SI = ξ(E₀/1 MeV)²: verlangt Bezugsenergie 0,99992 MeV (korrigiert) bzw. 0,99323 MeV = √K_frak·MeV (nackt) [K]; Eigenschaft des Ankers (R135)
- Wo das MeV herkommt: 1 MeV = 10⁶ · 1,602176634·10⁻¹⁹ J, Zahlenfaktor = Zahlenwert von e aus der alten Ampere-Definition (μ₀ = 4π·10⁻⁷), also dieselbe historische Ladungseinheit, in der α steckt [Q]; Messweg m_e c² = 2 Ry/α² [B]; die SI-Brücke ist gleichbedeutend mit m_e/MeV = √(αK/(ξ m_μ/m_e)) = 0,51104 (+8·10⁻⁵) [K]; Lesart der zwei Kugeln: Compton-Kugel (nur Masse) nackt, Korrektur auf der Seite der Coulomb-Kugel bzw. der Einheit, ergibt 1 MeV bis auf 8·10⁻⁵ [S]; der Rest bleibt offen
- Fraktale Korrektur: Der von α verlangte Faktor zwischen nacktem und korrigiertem Weg (A130) ist das Quadrat der nackten Bezugsenergie in MeV, K_α = ξ m_e m_μ α⁻¹ = 0,98650 [B], 1,7·10⁻⁴ neben 74/75 [K]; in der Grundform ξE₀² = 1 kein Korrekturfaktor; K_frak tritt im α-Sektor nur in der SI-Übersetzung auf [K] (vgl. Dok. 122), sein Wert 74/75 stammt aus der Geometrie (A040, Rotationszahl der Rekursion); dieselbe Gleichung wie A130, keine neue Messung
- Vermerke (1. Okt. 2026), die Korrekturen stehen nur dort: Dok. 005 (E₀ = 1/ξ = 7500 GeV; Parameter, zwei Tabellenzeilen, Korrekturkasten; bisher ohne Vermerk), Dok. 032, 133, 165 (bestehende Vermerke zu E₀ = 1/ξ um E₀² = 1/ξ ergänzt), Dok. 013 (S_T0 per Konstruktion; Korrekturkasten), A130 (Lücke der beiden Wege = Quadrat der Bezugsenergie), jeweils De/En; Dok. 384 stellt die Grundform α = 1, E₀² = 1/ξ voran und nennt die Bezugsenergie (Prüfskript 79/79)

**Prüfskript:** 2/python/Dok386_Skripte/pruef_386_alpha_geometrie.py — 25/25 PASS
**Register:** kein Eintrag (Vermerke direkt in den betroffenen Dokumenten).

---

## 2. Oktober 2026 — Dok. 387: Die Abweichungen im Überblick

### Dok. 387 — Verhältnisse, SI-Übersetzung und Korrekturgrößen (De/En, je 8 Seiten)

Anlass: Alle Restabweichungen an einer Stelle festhalten, getrennt nach Grundform (Verhältnisse in natürlichen Einheiten, α = 1) und SI-Übersetzung, jeweils mit Messwert und Unsicherheit; dazu die Korrekturgrößen und ihre Zusammenhänge.
- Verhältnisse: m_μ/m_e +0,52 %, m_τ/m_μ +1,03 % bei Messfehlern 10⁻⁸ und 10⁻⁵, also echte Reste der Leiter [K]; Koide −0,017 ξ (0,4σ); v/E_P −0,23 %; β_T = 0,977 (Messfehler 0,18 %); Δm²-Verhältnis −1,4 % (0,5σ); θ₁₃ 0,4σ; M_W 3,8σ; m_h 1,7σ; m_t 0,6σ; λ_CKM 1,5σ
- SI-Übersetzung: α⁻¹ +1,7·10⁻⁴ = Abstand m_e m_μ gegen 54 MeV² (Galois 3700/27 auf 7,6 ppm) [K]; Kette e −1,32 % (= K_frak − 1 bis auf 1,6·10⁻⁴), μ −0,80 %, τ +0,22 % [K]; v aus der Leiter nackt +1,10 %, mit K −0,25 %
- β_T: schon in den frühesten Dokumenten (März/April 2025) β_T = 1 neben α = 1 mit kleiner Abweichung (r₀ ≈ ℓ_P/7519); heute 0,977, mit FFGFT-eigenem v 0,982, mit nacktem v 0,956 [K]; Rest nicht hergeleitet [S]
- K_frak-Varianten: 74/75 einzige mit ganzer Umlaufzahl, Galois auf 7,6 ppm [K]; (1−ξ)¹⁰⁰, exp, 1/(1+100ξ) überall schlechter; 1 − ψ′(75) halbiert den α-Rest, verliert die ganze Umlaufzahl
- Faktor 10 in v/E_P: an den Messwert angepasst (Feb. 2026); 8πG-Lesart nicht tragfähig wegen Dok. 374/376 [X]; mit nacktem v der Leiter wird er zu 10 K_frak ≈ π² [S]
- Messgenauigkeit: für Leptonen, α, v/E_P und die SI-Kette nur minimaler Beitrag; begrenzend bei m_h, m_t, M_W, Neutrinos und Mischungswinkeln
- Vermerke (2. Okt. 2026): Faktor 10 in Dok. 149, 150, 383, 041, 372 (De/En) und Dok. 384 auf „angepasst, mit nacktem v 10 K_frak ≈ π²“ (Dok. 387)

**Prüfskript:** 2/python/Dok387_Skripte/pruef_387_abweichungen.py — 27/27 PASS
**Register:** kein Eintrag (Vermerke direkt in den betroffenen Dokumenten).

---

## 2. Oktober 2026 — Dok. 388: Die CMB-Temperatur in der Grundform

### Dok. 388 — eV-Relation, Verhältnis zur Elektronenmasse und die H₀-Formen (De/En, je 8 Seiten)

Anlass: Die Casimir-CMB-Verbindung ist eine Identität, weil L_ξ nur über T_CMB festgelegt ist (R136). Alle Wege, T_CMB ohne diese Zirkularität aus ξ zu gewinnen, werden in der Grundform (natürliche Einheiten, α = 1, ein Anker m_e) gegenübergestellt.
- eV-Relation (P11): (16/9) ξ (1 − 275ξ/4) eV trifft auf 2·10⁻⁶ [K], gilt aber nur in eV; in meV, K oder m_e liegt sie um Größenordnungen daneben; die Umdefinition von α ändert Energien nicht [B]; das eV ist gesetzt (Volt 1881, exakt seit 20. Mai 2019) [Q]; verlangter Koeffizient 68,766, 275/4 nächster Bruch mit Nenner 4; Einstufung nach R137 (i) bleibt [S]
- Andere Bezugsenergien: u = √ξ E₀ = 84,85 keV und α² m_e geben keinen glatten Vorfaktor
- Grundform: T_CMB/m_e = K ξ^(5/2), K = 2,23897 [K]; Kandidat K = (8π)^(1/4), +0,0025 %, 0,12σ FIRAS [S]; Zufallsprüfung über 3370 Ausdrücke: 3 Treffer, 1,6 erwartet; bei p, q ≤ 10 einziger Treffer, 0,2 erwartet
- Folgerungen: T_CMB⁴ = 16 H₀ m_e³ [B], daraus H₀ = 66,81 ± 0,06 km/s/Mpc (1,2σ zu Planck); Ω_γ = (4096/10125) ξ [B]; L_ξ = (15/8π³)^(1/4) ξ^(−9/4) λ̄_e = 100,24 μm ohne T_CMB [K]
- H₀-Formen: (π/2) ξ¹⁰ m_e passt (0,1σ in T), E₀ ξ^(41/4) liegt 11σ bzw. 20σ daneben [X], sofern der Kandidat gilt; keine unabhängige Bestätigung des Exponenten 10
- Offen: Vorfaktor (8π)^(1/4), Exponent 10 und π/2 (P20), warum Ω_γ ein fester Bruchteil von ξ ist

**Prüfskript:** 2/python/Dok388_Skripte/pruef_388_cmb_grundform.py — 27/27 PASS
**Register:** kein Eintrag.

---

## 6. Oktober 2026 — Dok. 389: Parabelflug, Trägheit und die Darstellungen der Gravitation

### Dok. 389 — Freier Fall, Gegenbahn, Licht und Horizont in der Zeit-Masse-Dualität (De/En, je 9 Seiten)

Anlass: die eingehende Frage zum Parabelflug — was das Gewicht ist, wenn es im freien Fall verschwindet — und die alternative Sicht der Gravitation als Massen- bzw. Taktänderung und fraktale Wegverlängerung statt Raumkrümmung.
- Uhr im Potential: ω = ω₀√g₀₀, m(x) = m₀√g₀₀ ist die Killing-Energie, g₀₀ = (m/m₀)² [B]; Trägheit als Gegenbahn a_Träg = −c²∇ln λ₄ = −a_Fall [B]; Poisson für das Massenfeld ∇²ln m = 4πGρ/c², außen c²∂²ᵣln m = −2GM/r³ [B]; isotrope ART g_ij = (1−2Φ/c²)δ_ij: ℓ_koord = ℓ(1+Φ/c²), λ₄,koord = λ₄(1−Φ/c²), räumlicher Brechungsanteil −Φ/c² [B]
- Freier Fall: L = −m(x)c²√(1−v²/c²) mit m = m₀ e^(Φ/c²) gibt a = −c²∇ln m = c²∇ln λ₄ = −∇Φ [B]; g/c² = 1,09·10⁻¹⁶ pro Meter = Uhrengang pro Meter [K]; Vorzeichen durch die Rotverschiebung festgelegt (Pound–Rebka 1,05 ± 0,10) [K]
- Gewicht als Gegenbahn: Die Ruhe-Weltlinie ist nicht stationär, der Rest −m g muss vom Boden ausgeglichen werden; im Parabelflug entfällt die Abweichung [B]
- Gezeiten: Hesse-Matrix von Φ, Eigenwerte (−2, 1, 1) GM/r³, nicht wegtransformierbar [B]
- Drei Darstellungen (Raumkrümmung, Massen-/Taktänderung, fraktale Wegverlängerung) als mathematische Modelle ohne ontologische Aussage, Mischformen zulässig; für Licht Takt und Weg komplementäre Hälften: konform flach 0, nur Takt 0,875″, beide 1,751″ und γ = 1 (Dok. 308) [K]; die konforme Kopplung der Materiefelder (A142) lässt Licht unberührt [B]
- Periheldrehung: logarithmische Form ergibt β = 1 und mit γ = 1 den ART-Wert 42,98″/Jh. [K]; lineare Form 7/6 (50,1″), Nordström −1/6; die logarithmische Form ist gesetzt [S]
- Horizont: statischer Beobachter E/√(1−r_s/r) divergiert, T₀ schneidet bei ρ_min = 2 r_s ξ E/E_P ab; frei fallend E/2, endlich [B]; T₀ betrifft den Vergleich, nicht den Durchgang (wie Dok. 306)
- Namensklärung M_coll = m_P/√2 gegen m_P/ξ; m_char·G = ξ²/4 (R58, A142) gegen mitlaufendes G (Dok. 350); keine eigene Quantisierung der Gravitation (R58, A142)
- Vermerk (6. Okt. 2026) in A142 (De/En): konforme Kopplung und Licht; Prüfskript a142_gravitation_lagrange.py 18/18
- Dok. 384 (De/En): Darstellungen mit Takt und Weg (Dok. 308, 389), m_char in m·G = ξ²/4, Lichtablenkung mit Mechanismus und Periheldrehung, konforme Kopplung und Licht; Prüfskript 121/121
- Prüfskript ffgft_308_p36_stufeB1_faktor2_fe.py lief unter Python 3.11 nicht (Backslash im f-String), behoben; Ergebnis unverändert 0,875″ / 0,875″ / 1,750″

**Prüfskript:** 2/python/Dok389_Skripte/pruef_389_parabelflug.py — 34/34 PASS
**Register:** kein Eintrag (Vermerke direkt in den betroffenen Dokumenten).

---

## 6. Oktober 2026 — Bereinigung, Block 1: Dok. 001–052

### Fassung ohne Korrekturvermerke (De/En)

Anlass: v1.4.4 ist die letzte Fassung mit datierten Korrekturvermerken (Vermerk in Dok. 190, Vorbemerkung). Ab jetzt enthalten die Dokumente nur noch die korrigierte letzte Fassung; Nachweis der Korrekturen sind Dok. 190 und v1.4.4.
- Bereinigt (je De/En, PDFs neu): Dok. 001, 001a, 002, 003, 004, 005, 006, 007, 008, 009, 010, 011, 012, 013, 014, 015, 016, 018 (Rev. 10, 11, 12), 019, 020, 021, 022, 023, 023a (Teil 2, Video), 023b, 024, 025, 026, 028, 030, 032, 033, 034, 035, 036, 037, 039, 040, 041, 042, 043, 044, 046, 047, 049, 051, 052
- Korrekturkästen entfernt, Vermerke aufgelöst: Der Text trifft die korrigierte Aussage selbst; widerlegte Aussagen sind so umgeschrieben, dass nur noch steht, was gilt; Abstracts, Überschriften, Tabellen und Fazits angepasst; Registerverweise, die nur die Korrektur belegten, entfernt
- Ältere datierte Nachträge mit aufgelöst: 006 (Neutrinoteil gekürzt, maßgeblich Dok. 340), 007 (Anschluss an Dok. 340), 024 (Kryptographie-Behauptungen gestrichen), 025 und 041 (achromatische Rotverschiebung); Stellen ohne eigenen Vermerk, die einer belegten Korrektur widersprachen, angeglichen (u. a. 018 K_frak nicht in der Leiter, 023/023a/035 kein lokaler Realismus, 013 Anker für SI-Absolutwerte); Videoverweise 023a/023b (Veritasium) und 023a Teil 2 (Richard Behiel) richtiggestellt
- Korpusweite Prüfskripte unverändert (378: 26/26, 377: 20/20, 320/322 bestanden, Maxwell 6/8 wie vorher)

**Register:** kein Eintrag.

---

## 6. Oktober 2026 — Bereinigung, Block 2: Dok. 053–150

### Fassung ohne Korrekturvermerke (De/En)

- Bereinigt (je De/En, PDFs neu): Dok. 053, 054 (nur De-PDF), 055, 056, 057, 059, 060, 061, 062, 063, 064, 066, 067, 068, 070, 073, 074, 077, 078, 080, 081, 083, 086, 089, 091, 093, 095, 097, 101, 105, 114, 116, 122, 124, 127, 129, 131, 132, 133, 134, 137, 141, 143, 144, 145, 146, 147, 148, 149, 150
- Korrekturkästen, Vermerke, „Hinweis zum Korpusstand“ und ältere Nachträge aufgelöst; korpusweit gültige Korrekturen aus Dok. 190 auch dort angewandt, wo der Eintrag das Dokument nicht nennt: achromatische Rotverschiebung (K6; u. a. 053, 061, 063, 066, 067, 068, 081, 146), H₀ kalibriert, Form mit Exponent 10 (P39, R137, Dok. 388; 064), α als Eigenschaft des Ankers E₀ (R135; 056, 070, 086), Casimir-CMB-Verhältnis als Identität (R136; 061, 063, 086, 091), G-Präzision (R141), keine Lokalität durch die ξ-Dämpfung (R142; 074, 147), Ordnungssuche statt ξ-Resonanz (R65; 057, 147), g−2 nach Dok. 382 (u. a. 053, 059, 061, 070, 081, 095), Begründung des ewigen Universums nach Dok. 306 statt Heisenberg (R50; 061, 063)
- Korpusweite Prüfskripte unverändert

**Register:** kein Eintrag.

---

## 6. Oktober 2026 — Bereinigung, Block 3: Dok. 152–241

### Fassung ohne Korrekturvermerke (De/En)

- Bereinigt (je De/En, PDFs neu): Dok. 152, 153, 154, 155, 156, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 172, 173, 174, 175, 178, 180, 181, 182, 183, 184, 185 (Zeit-Einbettungspreis; Dialog nur De, ohne PDF), 186 (Photonik-Analyse; Korrekturen nur De, ohne PDF), 187, 188, 189, 191, 192, 193, 201, 202, 203, 204, 205, 206, 207, 210, 230, 231, 232, 241
- Korrekturkästen, Vermerke und datierte Nachträge aufgelöst; korpusweite Korrekturen aus Dok. 190 auch ohne eigenen Vermerk angewandt: α als Eigenschaft des Ankers E₀ (R135), G-Präzision (R141), H₀ und Exponent 10 bzw. 41/4 kalibriert (P39, R137), Casimir-CMB-Identität (R136), keine Lokalität durch die ξ-Dämpfung und QND kein Determinismusbeweis (R142), ξ_Higgs kein Zweitparameter (R61), r_i als Setzungen (R138), achromatische Rotverschiebung (K6), g−2 nach Dok. 382, kein eigenes ξ-Faktorisierungsverfahren (R65)
- Größere Umbauten: 159 (Vakuumenergie nicht durch ξ konvergent), 167 (Δn = √3 ξ^(1/2) gilt nicht; Dokument als Prüfung umformuliert, Wrapper-Untertitel angepasst), 175 (QND, IBM-Läufe, Zwei-ξ-Abschnitt), 182 (R_H als Hubble-Länge statt Größe des Universums, P36), 186/187 (f₀ = 1/t₀ statt ξ als Frequenz; B-Meson-Deutung gilt nicht)
- Offen gemeldet, nicht geändert: Wrapper-Titel 182 („Maximale Größe des Universums aus xi“), B-Meson-Vorhersage in 187, CHSH-Form QM-5 in 202, Δp = 1/3 in 158 und 192
- Korpusweite Prüfskripte unverändert (378: 26/26, 377: 20/20); 180: 16/16, 230: 9/9

**Register:** kein Eintrag.

---

## 6. Oktober 2026 — Bereinigung, Block 4: Dok. 243–310

### Fassung ohne Korrekturvermerke (De/En)

- Bereinigt (je De/En, PDFs neu): Dok. 243, 244, 245, 246, 247, 250, 251, 253, 257 (ohne PDF), 258, 259, 261, 262, 263, 267, 268, 270, 274, 276, 279, 281, 282, 284, 285, 286, 287, 288, 290, 291, 292, 293, 295, 296, 297, 299, 301, 304, 306, 307 (Quelle; PDF siehe unten), 308, 309, 310
- Korrekturkästen, Vermerke und datierte Nachträge aufgelöst; korpusweite Korrekturen aus Dok. 190 auch ohne eigenen Vermerk angewandt (R135, R136, R137/P39, R138, R139, R141, R142, R65, R71, Dok. 382)
- Größere Umbauten: 243 (Landauer-Vorhersage für Torus-Chips gilt nicht; Abschnitt als Analogie), 259 (Polynomabschnitt neu: Normprodukt vom Grad 72), 268 (Faktor 3 als Setzung, Retrodiktion), 291/293 (K_frak-Steigung und Leak (7−3φ)/9 nicht verträglich), 308 (Bullet Cluster offen, Spiralgalaxien offen; Lichtablenkung unverändert)
- Wrapper 308, 309, 310 binden jetzt die Quelldatei ein (vorher veraltete Volltextkopien); Wrapper 307 ist weiterhin eine eigenständige ältere Fassung mit Literaturverzeichnis und wurde nicht umgestellt
- Prüfskripte: 263 7/7, 267 14/14, 268 8/8, 276 3/3, 282 6/6, 285 19/19, 286 12/12, 288 5/5, 308 C1 3/3; übrige laufen fehlerfrei ohne Zählung

**Register:** kein Eintrag.


---

## 6. Oktober 2026 — Bereinigung, Block 5: Dok. 311–389

### Fassung ohne Korrekturvermerke (De/En)

- Bereinigt (je De/En, PDFs neu): Dok. 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 381, 382, 383, 384, 385, 386, 387, 388, 389
- Korrekturkästen, Vermerke und datierte Nachträge aufgelöst; korpusweite Korrekturen aus Dok. 190 auch ohne eigenen Vermerk angewandt (R135, R136, R137/P39, R138, R139, R141, R142, R65, R71, Dok. 382)
- Titelkorrekturen und strukturelle Fixes: Fehlende `\title`-Blöcke in Wrapper 016, 046, 116 ergänzt; fehlende `\documentclass`-Zeile in Wrapper 252 De/En ergänzt; „Revolution" aus Titeln/Überschriften entfernt (Dok. 046, 053, 062, 086, 122, 183); doppelter Titelblock und `\tableofcontents` aus Ch-Dateien 187, 188, 189 entfernt; Wrapper-Titel für 187, 188, 189 auf Volltitel gesetzt
- Größere Umbauten: 349 (SU(2)_L-Chiralität: Sätze A neu gefasst, Sätze B–E als ungestützt markiert); Wrapper 311/312/313 sind ältere eigenständige Fassungen ohne Literatur, wurden so gemeldet
- 384 De/En: datierter Inline-Vermerk zu $f = 1/\xi$ in Fließtext aufgelöst; Querverweise auf Vermerke in anderen Dokumenten auf normale Dokumentreferenzen umgestellt
- 389 De/En: Querverweise auf Vermerke in Dok. 143 und A142 auf Dokumentreferenzen umgestellt
- Vermerke zur KI-Assistenz (`\section*{Vermerk zur Verwendung von KI-Assistenz}`) bleiben als methodische Angaben erhalten — dies sind keine Korrekturschilder
- Prüfskripte: 384 121/121, 389 34/34; 341 Z₃-Skript 9/9; übrige laufen fehlerfrei

**Register:** kein Eintrag.

---

## 6. Oktober 2026 — Bereinigung, A-Serie: A010–A284

### Fassung ohne Korrekturvermerke (De/En)

- Bereinigt (je De/En, PDFs neu): A010, A015, A020, A030, A040, A050, A070, A075, A080, A110, A120, A130, A138, A142, A145, A150, A155, A165, A180, A220, A230, A250, A260, A261, A263, A264, A265, A266, A267, A270, A271, A272, A273, A280, A283, A284
- Datierte `\textit{(Vermerk vom …)}`- und `\textit{(Korrigiert am …)}`-Inline-Notizen aufgelöst; Inhalt der Vermerke als regulärer Text integriert, Datumszeile entfernt; keine tcolorbox-Korrekturkästen in der A-Serie vorhanden
- Inhaltliche Integrationen u. a.: A010 (E₀ als SI-Kalibrierwert, geometrisches Mittel ungeeignet), A015 (κ=7 als Zerlegungswahl, nicht erzwungen; Casimir-Bestätigung des Faktors 4/3 gestrichen), A020 (kristallographische Restriktion nur 2D/3D), A050 (Defektasymmetrie 1/75 vs. 1/74), A070 (f(k_t) als periodische Funktion der Zeitwicklung), A075 (l als Zählindex der transversalen Anregungsstufe, nicht geometrischer Betrag; ξ→0 gilt nur für Skalarfeld δm), A080 (K_frak wirkt auf α⁻¹, quadratisch im Skalenfaktor), A110 (Tabellenwerte schon korrekt im Haupttext), A120 (Leck (7−3φ)/9 ≈ 3,5σ inkompatibel mit δ*, als offener Punkt benannt), A130 (Weg-2-Formel aus A080 entfernt), A138 (f = 1/ξ = 7500 Grundwindungszahl, keine Frequenz), A142 (Maxwell konform invariant in 4D; T/T₀ statt T für Homogenität; g−2-Schleifenkorrektur durch Messung ausgeschlossen), A145 (E_char hebt sich in G auf; C_conv ist SI-Umrechnung der Ein-Anker-Kette), A150 (Up-Typ-Quarks folgen keiner rekursiven Formel; lineare Resonanzleiter mit Schrittweite 1/3), A155 (π⁰-Auswertung: Wahlabhängigkeit von n_eff als reguläre Anmerkung), A165 (6 Inline-Notizen zu Notation, Pisot/Weyl, k-Schranken, Δ-Spalte aufgelöst), A230 (κ=4 als Eintrittspunkt), A260 (3 Energiedichte-/Tabellen-Korrekturen), A261 (Skalenhierarchie, E₀, α-Kette, K_frak), A265 (H₀=ξc/ℓ integriert; Weg-2 gestrichen), A266 (G-Rückrechnung ×ℏc⁵; f als Grundwindungszahl), A283 (Ω_r 0,0096→0,0098), A284 (f(n,l,j)-Bezeichnung, Tsirelson-Klarstellung)
- Prüfskripte: a142 18/18, a271 10/10, a273 16/16, a150 BESTANDEN, a155 BESTANDEN, a165 BESTANDEN, a180 BESTANDEN, a220 BESTANDEN, a260 BESTANDEN, a261 BESTANDEN, a263 BESTANDEN, a264–a270 BESTANDEN; Dok. 190-Abgleich: 0 Abweichungen (144/144 Einträge)

**Register:** kein Eintrag.

---

## 8. Oktober 2026 — v1.4.5: HTML-Seiten, deterministischer Simulator und Gesamtausgabe in acht Bänden

### Release v1.4.5 — erste Fassung ohne Korrekturvermerke

Anlass: Mit den Bereinigungsblöcken vom 6. Oktober enthalten alle Dokumente nur noch die korrigierte letzte Fassung. v1.4.5 fasst das mit den seither erfolgten Arbeiten zusammen; Release Notes: [`RELEASE_NOTES_v1_4_5_De.md`](RELEASE_NOTES_v1_4_5_De.md) · [`RELEASE_NOTES_v1_4_5_En.md`](RELEASE_NOTES_v1_4_5_En.md).

- **Dok. 006, 073, 382** (De/En, PDFs neu): Korrekturen nach R149 — 382 mit k_geom aus Dok. 018 (Rev. 12), Verhältnis-Linie unberührt; 006 Quarkvergleich auf PDG 2024 umgestellt (wie Dok. 384), Quark-Vorfaktoren aus Messwerten **[S]**; 073 Simulationsparameter σ statt ξ_num. Prüfskript `2/python/Dok382_Skripte/pruef_382_myon_g2_stand.py` 21/21
- **Dok. 384** (De/En, PDF und HTML neu): Registerstand R149; Prüfskript 121/121
- **HTML-Seiten** unter `2/html/`, `rsa/`, `sig/`: auf den Korpusstand gebracht (Status wie Dok. 384, Statusmarker mit Legende, α = 1 als Heaviside-Lorentz-Einheiten); Startseite mit unveränderter Überschrift; Diagramme `rsa/diagrams/t0_framework_{de,en}.mmd` neu erzeugt
- **Quantensimulator** `2/html/quantum_simulator_deterministic.html` neu aufgebaut nach der Messregel A(z, λ) = sgn(z − λ) aus Dok. 230; neue Hilfeseite `quantum_help_guide.html`; `step_by_step_modules_bilingual.html` überarbeitet
- **Shor-/Faktorisierungswerkzeuge** ein zweites Mal geprüft: Rechen- und Programmfehler behoben, Beschreibung als klassische Simulation der Ordnungssuche (R65)
- **Gesamtausgabe** (KDP, Band 1–8, De/En, Paperback und Hardcover): Innenteile von Band 1, 2, 5, 6 und 8 unter `2/pdf/buecher/` neu gebaut; Dok. 190 nicht mehr in Band 5 abgedruckt, Einleitungen von Band 5 und 6 verweisen auf das laufende Register im Repository; Umschläge Band 5 (De/En) mit neuer Rückenbreite und angepasstem Rückseitentext
- Dok. 190-Abgleich: 0 Abweichungen (146/146 Einträge, Registerstand R149)

**Register:** R148 und R149 (in Dok. 190).

---

## 9. Oktober 2026 — Dok. 390: Lose Puzzleteile

### Dok. 390 — Kaluza-Klein und andere etablierte Bausteine der Zeit-Masse-Dualität (De/En, je 11 Seiten)

Anlass: die Frage im einführenden Gespräch der Website, ob $\tilde T\cdot m=1$ nicht nach Kaluza-Klein klinge, und die Frage, warum die bekannte Dualität von Masse und Zeit nicht zu Ende gedacht wurde. Das Dokument ordnet elf etablierte Bausteine ein und hält zu jedem fest, was er bereits enthielt, welches Stück fehlte und wo er sich im Korpus einfügt. Die Geschichte des Einstein-Falls steht in Dok. 312 und wird nur zitiert.

Kaluza-Klein liefert die kompakte Richtung mit $m_n\propto n/R$; im Korpus ist $\tilde T\cdot m=1$ die Kaluza-Klein-Relation der zeitartigen vierten Torusrichtung ohne freien Radius und ohne zusätzlichen Turm (Dok. 330, 270, 307, 231, 311, 318). De Broglies innere Uhr und die Compton-Uhr von 2013 stehen hinter $\lambda_4\cdot m=2\pi$ (Dok. 312, 314). Die Zitterbewegung (Schrödinger, Hestenes) wird als Parallele eingeordnet, ohne Identifikation mit $S^1_m$ **[S]**. Paulis Einwand trifft eine kompakte Zeit nicht (Dok. 307, 334); die relationalen Ansätze nehmen die Zeit heraus statt hinein (Dok. 307). Wigners Masse als Casimir-Label, der Casimir-Wert $4/3$ der $SU(3)$ mit $\xi=C_2/N_{\mathrm{Fourier}}$ (Dok. 324: Formel **[B]**, Modenzahl **[K]**) und die Heaviside-Lorentz-Einheiten mit $\alpha=1$ als Einheitenwahl (Dok. 365; Übereinstimmung von 137 am Anker $E_0$, Dok. 338) bilden die zweite Gruppe. Die dritte sind Orbifold-Kompaktifizierung (Dixon–Harvey–Vafa–Witten; $T^4/\mathbb{Z}_3$ auf $D_4$ als **[SETZUNG]**, R131), endliche Körper mit Frobenius (Dok. 336, 346, 348 **[B]**, 338 **[K]**; Hyperladung offen nach R146) und die Koide-Formel ($\theta=2/9$ **[B]**, Amplitude $\sqrt2$ **[S]** nach Dok. 353, exaktes Paar für $m_\mu/m_e$ ausgeschlossen nach Dok. 369).

Ergebnis: Die Teile lagen in verschiedenen Fächern, galten als Werkzeug oder Kuriosität, und zwei Weichen (Paulis Einwand, räumliche statt zeitliche Kompaktifizierung) standen falsch. Die Bausteine waren nicht Grundlage der FFGFT: Die Theorie entstand unabhängig aus $\tilde T\cdot m=1$, die Literaturstellen wurden erst nachträglich gefunden und fügen sich ein (Abschnitt „Zur Reihenfolge“). Die Abgrenzung aus Dok. 342/343 gilt: Herleitungsanspruch nur für einfache, konventionsfreie Verhältnisse; $\Lambda_{\mathrm{QCD}}$ und andere schemaabhängige Größen sind ausgenommen.

Koide-Abschnitt ergänzt um die 45°-Lesart nach Foot (1994) als nachträglich gefundenes Puzzleteil; im Korpus ist das die Gleichverteilung der Massensumme auf die symmetrische Mode und das nicht-triviale Paar (Dok. 353, **[B]**). Die Amplitude $\sqrt2$ ist nach R150 in Dok. 353 und 367 als Setzung mit richtigem Wert geführt **[S]**; der frühere Widerspruch zwischen Dok. 367 und 353 ist damit bereinigt.

**Prüfskript:** 2/python/Dok390_Skripte/pruef_390_puzzleteile.py — 59/59 PASS (48 Fundstellen-Prüfungen in den Kapiteldateien, 11 Zahlenwerte)
**Register:** kein Eintrag.

---

## 9. Oktober 2026 — Dok. 391: Lose Puzzleteile II: Kosmologie

### Dok. 391 — Rotverschiebung, Skalen und die Grenze des kosmischen Sektors (De 10 / En 9 Seiten)

Anlass: Fortsetzung von Dok. 390 für die Kosmologie. Acht etablierte Bausteine werden eingeordnet, jeweils mit dem, was sie enthielten, was fehlte und wo sie sich im Korpus einfügen. Wie in Dok. 390 waren die Bausteine nicht Grundlage der FFGFT; die Literaturstellen wurden nachträglich gefunden. Anders als in der Teilchenphysik liegt der kosmische Sektor außerhalb des Herleitungsanspruchs: $H_0$ ist kalibriert, der Exponent 10 ist **[SETZUNG]** (P20), das Standardmodell leitet den Sektor ebenso wenig her (P39). Die Bausteine zeigen deshalb Lesarten, keine Herleitungen.

Rotverschiebung ohne Expansion: Zwickys Ermüdung des Lichts scheiterte an der Zeitdehnung; mit $\tilde T\cdot m=1$ werden Wellenlänge und Uhrentakt gemeinsam gebucht, Zeitdehnung $(1+z)$ für alle $z$ **[B]** (R128, Dok. 312). Hoyle–Narlikar und Wetterichs Universum ohne Expansion: Äquivalenz von Expansion und Massenlauf **[K]** (Dok. 312, Entartung Dok. 267), mit der Grenze „möglich und beobachtungsgleich, nicht bewiesen richtig“. Einsteins statisches Universum und Steady State: Träger ohne Rand, „Anfang“ als Antipode des Zeitzyklus **[K]** mit P20-Kalibrierung (Dok. 313); offen bleibt die Periodizität als Randbedingung.

Skalen: Diracs große Zahlen als $\xi$-Verhältnis zweier Skalen (P20, P39), im Korpus bisher nicht genannt **[S]**; Hubble-Länge als Maximalskala, kein Expansionshorizont (Dok. 182, 365); Milgroms $a_0=cH_0/(2\pi)$ **[K]** (Dok. 365) mit Querverankerung (Dok. 309) und Interpolationsformel aus der Unruh-Kopplung **[K]/[S]** (Dok. 308).

Grenze: Vakuumenergie und $\Lambda$ passen bisher nicht (R136 **[S]**, R137 **[X]**; $\Lambda$ als Lesart-Artefakt nach Dok. 308). Die Hintergrundstrahlung fügt sich nur als Kandidat ein: $T_{\mathrm{CMB}}/m_e=(8\pi)^{1/4}\xi^{5/2}$ aus Dok. 388 **[S]**, Zufall nicht ausgeschlossen; $T(z)$ aus Dok. 039 **[X]**, Faktor 3 der Peak-Folge gesetzt (R139).

**Prüfskript:** 2/python/Dok391_Skripte/pruef_391_kosmologie.py — 51/51 PASS (37 Fundstellen-Prüfungen in den Kapiteldateien, 14 Konsistenzprüfungen der Zahlen)
**Register:** kein Eintrag.
