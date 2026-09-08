# FFGFT Changelog — laufend ab v1.3.4

**Grundlage:** Dok. 190 (Korrekturregister)  
**Archiv bis v1.3.3:** [`000_FFGFT_Changelog_De.md`](000_FFGFT_Changelog_De.md)

Neue Einträge werden hier oben eingefügt (neueste zuerst).

---
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
