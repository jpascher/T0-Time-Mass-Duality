# Release Notes — v1.3.3 (August 2026)

**DOI:** wird bei Zenodo-Veröffentlichung vergeben — ersetzt v1.3.1 und v1.3.2  
Laufende Korrekturen: **[2/pdf/190_T0_Korrekturen_De.pdf](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/190_T0_Korrekturen_De.pdf)**  
Archivfassung des Registers: **[2/pdf/190_T0_Korrekturen_Archiv_De.pdf](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/190_T0_Korrekturen_Archiv_De.pdf)**  
Changelog: **[000_FFGFT_Changelog_De.md](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/000_FFGFT_Changelog_De.md)**  
A-Serie-Log: **[A_Serie_Export/A_SERIE_CHANGELOG.md](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/A_Serie_Export/A_SERIE_CHANGELOG.md)**

**FFGFT — Fundamentale Fraktale Geometrische Feldtheorie** zeigt: Alle Konstanten des
Standardmodells folgen aus einem einzigen dimensionslosen Parameter **ξ = 4/30000**
auf einem kompakten 4D-Torus T⁴. Die Grundrelation ist **T̃ · m = 1** — intrinsische
Zeit und Masse sind invers gekoppelt.

**Autor:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Überblick

Dieser Release fasst die Arbeit seit v1.3.1 zusammen: vier neue Dokumente
(324–327), den Umbau des Korrekturregisters und die Korrektur des
Neutrinosektors. Die Registereinträge R84 bis R87 sind enthalten.

**Der Schwerpunkt liegt auf zwei geschlossenen Brücken.**

Dok. 325 arbeitet den **mikroskopischen Hawking-Mechanismus** vollständig
aus FFGFT-eigenen Bausteinen aus — Dok. 313 (Kap. G) hatte den
thermodynamischen Rahmen gelegt, die Emissionsseite aber als Skizze [S]
gebucht. Der zentrale Befund: das Hawking-Quant ist das systemabhängige Bit
der Horizontskala, k_B·T_H = ħc/(4π·r_s) = E_bit(4π·r_s) exakt. Ein
universeller Bitwert wird nirgends benötigt (R85).

Dok. 327 beweist die **Selbstadjungiertheit des fundamentalen fraktalen
Operators F̂** — die seit Dok. 322 offene Frage (R82), an der die
Wohlgestelltheit von ξ = λ_min(F̂) hing. Der Beweis kommt ohne neue Axiome
aus und **ohne Restfälle**: Die Defektindex-Klassifikation tritt unter
FFGFT-Strukturen gar nicht auf, weil L₀ = ξ·ℓ_P die Skalenleiter endlich
macht. Es gibt keine Unendlichkeiten in FFGFT (R86).

Beide Resultate haben dieselbe algebraische Wurzel: Die ℤ₃-Sektorpaarung
(k,−k), die in Dok. 325 die Hawking-Information trägt, erzeugt in Dok. 327
die Symmetrie F̂ = F̂† — sie ist dort keine Forderung, sondern Folge der
Orbifold-Struktur.

Flankierend vergleichen Dok. 324 und 326 Douglas Matzkes Algebra-Frameworks
mit FFGFT: Dok. 324 schließt mit der Casimir-Herleitung
ξ = C₂(SU(3))/N_Fourier (R84), Dok. 326 arbeitet die Bitwert-Divergenz
heraus — universell (Matzke, Landauer bei T_P) vs. systemabhängig
(FFGFT, E_bit = ħc/L).

**Dok. 190 ist umgebaut**: Das Register war mit 87 Einträgen und 69 Seiten
unhandlich geworden. Die ausführliche Fassung ist als Dok. 190-Archiv
eingefroren; das neue Kompakt-Register führt alle Einträge tabellarisch auf
und schließt mit der konsolidierten Liste offener Brücken. Das
append-only-Prinzip bleibt unverändert.

**Der Neutrinosektor ist korrigiert** (R87): In Dok. 320 war die Auswertung
von ξ^(9/5) fehlerhaft; Massenformel und Exponenten waren stets korrekt.
Die Abweichung bei Δm²₃₂ beträgt +16,0 % statt der zuvor gebuchten −22 %.

## Einstieg für neue Leser

Dok. 205 „FFGFT in einfacher Sprache" (DE+EN, 13–14 Seiten) bleibt der empfohlene
Einstieg. Der einzige offene Falsifikationstest ist unverändert explizit benannt:
m_τ = 1776,97 MeV, durch Belle-II zu entscheiden, ohne Ausweichmöglichkeit.

## Was sich nicht geändert hat

ξ, die Grundrelation T̃ · m = 1 und alle Ableitungsketten sind unverändert.
Dok. 327 sichert die Wohlgestelltheit ab, es ändert keinen Zahlenwert.

---

## Neue Dokumente seit v1.3.1

### Dok. 324 — G(6,ℤ₃C)-Vakuumstruktur und FFGFT (DE+EN, je 9 S.)

Numerische Untersuchung der Verbindungsfragen zwischen Matzkes
G(6,ℤ₃C)-Vakuumstruktur und der FFGFT-Spektraltheorie.

- **Trine-Theorem [B]:** T_k³ = 1 in 8-dim. Spinordarstellung (δ < 6,5×10⁻¹⁶).
- **Vakuumoperator V [B]:** Rang-1-Projektor, Spektrum {0⁽⁷⁾, 1⁽¹⁾}.
- **ξ kein Spektralwert [K]:** abgeschlossener negativer Befund.
- **Casimir-Herleitung [K]:** ξ = C₂(SU(3)_fund)/N_Fourier = (4/3)/10⁴ = 4/30000,
  mit C₂ = 4/3 aus N_c = 3 [B] (Dok. 321) und N_Fourier = 10⁴ aus der
  T⁴-Topologie. Physikalischer Casimir-Effekt (Dok. 009) und algebraischer
  Casimir-Operator liefern unabhängig denselben Faktor 4/3. (R84)

Prüfskript: 16 Assertionen.

→ [DE](2/pdf/324_G6_Z3C_FFGFT_Vergleich_De.pdf) · [EN](2/pdf/324_G6_Z3C_FFGFT_Vergleich_En.pdf)

### Dok. 325 — Der FFGFT-Hawking-Mechanismus (DE+EN, je 7 S.)

Schließt die Emissionsseite von Dok. 313 Kap. G aus FFGFT-eigenen
Bausteinen (R85). Die fünf Bausteine:

1. **Temperatur [K]** — KMS-Regel T = ħ/(k_B·τ) mit Membran-Periode
   τ = 8πGM/c³ aus T̃·m = 1; ein Prinzip für Unruh, Gibbons-Hawking und
   Schwarze Löcher.
2. **Quant [K]** — k_B·T_H = ħc/(4π·r_s) = E_bit(4π·r_s) exakt:
   das Hawking-Quant ist das Bit der Horizontskala.
3. **Selektion [B]** — nur T_R = 0 entkommt; Absorption des Partnerquants
   ist die ℤ₃-Projektor-Orthogonalität P_j·P_k = 0 (exakt, kein Tunneln).
   Confinement (Dok. 321) und Hawking-Selektion sind ein Prinzip.
4. **Träger [K]** — masselose n₄=0-Torusmode; massive Moden fallen zurück
   (Uhrenstauchung an der Membran).
5. **Information [K]/[B]** — Sektorpaar (k,−k) orthogonal lesbar
   (log₂3 ≈ 1,585 Bit/Quant); Flächenquant −4ℓ_P²/nat aus
   Bekenstein+Clausius; feinkörnige Entropie konstant (Unitarität,
   Dok. 322). Kein Informationsparadoxon.

Zusätzlich verifiziert: Leistungskorrektur (1−ξ·ln(M/m_P)) = 0,6–1,4 %;
M* = 3,3×10¹¹ kg; Familienleiter r_s = R_H/2 exakt bei M = 4,66×10⁵² kg.
Offen [S]: Graukörper-Faktoren, Fixpunkt-Rückreaktion.

Prüfskripte: 18 + 20 Assertionen.

→ [DE](2/pdf/325_Hawking_FFGFT_De.pdf) · [EN](2/pdf/325_Hawking_FFGFT_En.pdf)

### Dok. 326 — Schwarze Löcher aus Hyperbits und aus FFGFT (DE+EN, je 11 S.)

Vergleich mit Matzkes Hyperbit-Framework (IPI 2026) — Schwerpunkt
Landauer, Bitwerte, systemabhängige Bit-Energie. Eingeleitet durch einen
narrativen Abschnitt „Warum Matzkes Algebra so einfach wirkt", der den
Zugang würdigt, bevor die Detailkritik folgt: Geometrie als Buchhaltung
über Unterscheidbarkeit (e_i² = +1), das Herausfallen der Drei aus Cl(6),
der Schwarzschild-Radius ohne Einstein-Gleichungen, die
0,41-Bit-Stabilitätsgeschichte — und wo die Eleganz erkauft ist.

- **Konvergenzen [B]:** Fermion-Generation = algebraische Grundeinheit;
  N_c = 3 erzwungen; r_s ohne ART; beide Hawking-Mechanismen strukturell
  exakt korrespondierend.
- **Divergenz:** universeller Bitwert (Matzke, Landauer bei T_P) vs.
  systemabhängige Bit-Energie E_bit = ħc/L (FFGFT [K]).
- **Numerisch:** T_H(Matzke)/T_H(KMS) = 1,000000 — der universelle Bitwert
  ist eine Umparametrisierung der KMS-Relation, keine unabhängige
  physikalische Eingabe.
- Matzkes Stabilitätsschwelle n_thresh = 6,41 als universelle Zahl: [X]
  (in Dok. 329 numerisch entschieden, R88).

Prüfskript: 15 Assertionen.

→ [DE](2/pdf/326_Matzke_FFGFT_Vergleich_De.pdf) · [EN](2/pdf/326_Matzke_FFGFT_Vergleich_En.pdf)

### Dok. 327 — Selbstadjungiertheit von F̂ (DE+EN, je 6 S.)

Schließt R82 vollständig, ohne Restfälle. Drei Feststellungen aus dem Korpus
(keine neuen Axiome): (F1) L₀ = ξ·ℓ_P macht die Stufenzahl endlich;
(F2) ℤ₃-kovariante Sektorphasen; (F3) endliche 100er-Rekursion des fraktalen Maßes.

**Beweiskette:**

| Schritt | Aussage | Status |
|---|---|---|
| Lemma 1 | Dok.-322-Axiome = Skalen-Filtrierung, exakt | [B] |
| Satz 2 | Blockdiagonal; ‖F̂‖ ≤ Σr_n < ∞ ⟹ D(F̂) = H | [B] |
| Satz 3 | ℤ₃-Paarung (k,−k) ⟹ F̂ = F̂† (mit Gegenprobe) | [B] |
| Korollar 4 | Defektindizes (0,0); genau eine Realisierung | [B] |
| Satz 5 | Fraktales Maß erhält Selbstadjungiertheit | [B] |
| Satz 6 | ℤ₃-Restriktion, alle drei χ-Twist-Klassen s.a. | [B] |
| Korollar 7 | ξ = λ_min(F̂_D4) wohldefiniert, trunkierungsstabil | [B] |

Prüfskript: 21 Assertionen, alle bestanden.

**Dok. 322 nachgezogen:** Statustabelle, Definitionsstelle und Schlussfolgerung
führten die Selbstadjungiertheit und die Defektindex-Klassifikation noch als [S] —
beide stehen jetzt auf **[B], Dok. 327**.

→ [DE](2/pdf/327_Selbstadjungiertheit_F_De.pdf) · [EN](2/pdf/327_Selbstadjungiertheit_F_En.pdf)


### Dok. 329 — Ist die Stabilitätsschwelle n_thresh universell? (DE+EN, je 7 S.)

Entscheidet die in Dok. 326 als [S] geführte Frage numerisch (R88).
**Antwort: nein.**

Der skalenunabhängige Kern bleibt: Compton = Schwarzschild liefert
M_coll = m_P/√2 rein geometrisch, ohne Bits, Landauer oder Temperatur [B].
Alles Nichtgeometrische an n_thresh = M_coll/m_bit steckt im Nenner.

Mit E_bit(L) = ħc/L (Dok. 257) folgt exakt

    n_thresh(L) = L / (√2 · ℓ_P)

— linear in der Skala, kein invarianter Zahlenwert [B]. Über die Skalen des
Korpus (L₀ = ξℓ_P bis 1 nm) variiert der Wert um Faktor 4,6×10²⁹.

**Matzkes Skala ist rekonstruierbar:** L = 2πℓ_P/ln2 = 9,0647 ℓ_P, und dort
gibt die Formel exakt 6,4097 zurück [B]. Der „universelle" Bitwert *ist* die
FFGFT-Bit-Energie bei rund neun Plancklängen.

Empfindlichkeit: 10 % Temperaturabweichung verschiebt n_thresh um 10 % und
kippt die Stabilitätsaussage — bei 1,1·T_KMS wäre n_thresh = 5,83 < 6,000,
Cl(6) läge oberhalb der Schwelle.

Nebenbefund: Die Temperatur ist nicht T_P, sondern die KMS-Temperatur
T_P/(2π) — dasselbe 2π, das in Dok. 325 die Hawking-Temperatur *ohne*
Bitwert erzeugt.

Unberührt [B]: Compton = Schwarzschild, r_s ohne Feldgleichungen,
Cl(6)-Struktur, die Hawking-Korrespondenzen.

Prüfskript: 12 Assertionen.

→ [DE](2/pdf/329_nthresh_Skalenanalyse_De.pdf) · [EN](2/pdf/329_nthresh_Skalenanalyse_En.pdf)

---

## Korrigierte Dokumente

### Dok. 320 + 322 — Δm²₃₂: Zahlenwerte korrigiert (R87)

Die Auswertung von ξ^(9/5) in Dok. 320 war fehlerhaft (8,717×10⁻⁸ statt
1,059×10⁻⁷). Die Massenformel m_νi = m_e·ξ^pi und die Exponenten
p_i ∈ {9/4, 2, 9/5} waren stets korrekt — betroffen war nur die ausgerechnete
Zahl für ν₃. Dok. 320 und die zwei übernommenen Tabellenzeilen in Dok. 322
sind auf die richtigen Werte gebracht:

| | vorher | jetzt |
|---|---|---|
| m_ν3 | 44,51 meV | **54,11 meV** |
| Δm²₃₂ | 1,90×10⁻³ eV² | **2,846×10⁻³ eV²** |
| Abweichung | −22 % | **+16,0 %** |
| Σm_ν | 54,57 meV | 64,17 meV (< 120 meV ✓) |

Unberührt: m_ν1, m_ν2, Δm²₂₁ (+8,3 %) und die Fixpunkt-Zuordnung.

Die Abweichung bleibt [S], hat jetzt aber dasselbe Vorzeichen wie die solare
und etwa die doppelte Größe — Hinweis auf eine gemeinsame Ursache.
Dok. 320 wurde um eine **Kandidatenanalyse** erweitert: K_frak am Fixpunkt F₇
(+12,9 %, unzureichend); Mischungsterm F₅–F₇ (richtiges Vorzeichen, erfordert
die vollständige Massenmatrix — aussichtsreichster Kandidat); alternative
Exponenten (unwahrscheinlich: p₃ = 1,8081 liegt nur 0,45 % über 9/5).

Prüfskript: `320_dm32_neutrino_verify.py` (10 Assertionen).

→ [DE](2/pdf/320_Spektraltheorie_De.pdf) · [EN](2/pdf/320_Spektraltheorie_En.pdf)

---

## Umbau des Korrekturregisters

### Dok. 190 neu — Kompakt-Register (DE 10 S. / EN 8 S.)

Registertabelle mit **allen 86 Einträgen** (K1–K7 bzw. C1–C7, P1–P44, R41–R86):
Nummer, betroffene Dokumente, Gegenstand in Kurzform, mit Verweis aufs Archiv.
Abschließend der konsolidierte Abschnitt „Aktuell offene Brücken (Stand R86)".

### Dok. 190-Archiv — eingefrorene Vollfassung (DE 69 S. / EN 58 S.)

Die bisherige ausführliche Fassung mit Archiv-Vermerk. Enthält für jeden Eintrag
die vollständige Begründung, die fehlerhaften und korrekten Ausdrücke im Wortlaut
sowie alle Nachträge. Wird nicht mehr fortgeschrieben.

Das append-only-Prinzip bleibt unverändert (vgl. R50): Quelldokumente werden nicht
revidiert. Neue Einträge werden künftig direkt im Kompakt-Register ausgeführt.

---

## Korrekturen — R84 bis R88

**R84** (23. Aug.): ξ = C₂(SU(3)_fund)/N_Fourier = (4/3)/10⁴ = 4/30000 [K]
(Dok. 324). ξ ist kein Spektralwert eines G(6)-Operators; die Verbindung
zwischen G(6,ℤ₃C) und FFGFT liegt im Casimir-Quotienten, nicht im Spektrum.

**R85** (23. Aug.): Hawking-Mechanismus mikroskopisch geschlossen [K]/[B]
(Dok. 325). Die in Dok. 313 Kap. G als [S] geführte Emissionsseite
(Membran-Thermometer, Selektion, Träger, Informationskodierung) ist auf
[K]/[B] gehoben. Offen bleiben Graukörper-Faktoren und
Fixpunkt-Rückreaktion [S].

**R86** (23. Aug.): Selbstadjungiertheit von F̂ vollständig geschlossen [B]
(Dok. 327). Die Endlichkeit der Skalenleiter ist durch L₀ = ξ·ℓ_P (Dok. 180 [K])
garantiert — keine Unendlichkeiten in FFGFT, damit F̂ beschränkt und D(F̂) = H.
Die Symmetrie folgt aus der ℤ₃-Paarung (k,−k) (dieselbe wie in Dok. 325 [B]).
Defektindizes (0,0): genau eine selbstadjungierte Realisierung [B].
Fraktales Maß, ℤ₃-Restriktion und alle drei χ-Twist-Klassen erhalten die
Selbstadjungiertheit [B]. ξ = λ_min(F̂_D4) wohldefiniert und trunkierungsstabil [B].
Es verbleiben keine Restfälle. **R82 ist aus der Liste offener Brücken gestrichen.**

**R87** (23. Aug.): Δm²₃₂ — korrigierte Zahlenwerte und Kandidatenanalyse [K].
In Dok. 320 war die Auswertung von ξ^(9/5) fehlerhaft; Massenformel und Exponenten
waren stets korrekt. Dok. 320 und 322 auf die richtigen Werte gebracht:
m_ν3 = 54,11 meV, Δm²₃₂ = 2,846×10⁻³ eV² (+16,0 % vs. NuFIT 5.3),
Σm_ν = 64,17 meV (im Planck-Limit). Unberührt: m_ν1, m_ν2, Δm²₂₁, Fixpunkt-Zuordnung.
Die verbleibende Abweichung bleibt [S]; aussichtsreichster Kandidat ist ein
Mischungsterm F₅–F₇.

**R88** (24. Aug.): n_thresh ist skalenabhängig; Matzkes Skala rekonstruiert
[B] (Dok. 329). n_thresh(L) = L/(√2·ℓ_P); Matzkes Wert entspricht
L = 2πℓ_P/ln2 = 9,0647 ℓ_P. Als universelle Zahl abgeschlossen negativ [X].
Unberührt: Compton = Schwarzschild, r_s ohne Feldgleichungen, Cl(6)-Struktur [B].

---

## Prüfskripte

`python/Dok320_321_322_Skripte/`:
- `324_G6_FFGFT_verify.py` — Trine-Theorem, Vakuumoperator, Casimir-Herleitung (16)
- `320_dm32_neutrino_verify.py` — Neutrinomassen, Δm²₂₁, Δm²₃₂, Massensumme,
  K_frak-Kandidat, Exponentenvergleich (10)

`python/Dok325_Skripte/`:
- `325_hawking_ffgft_mechanismus.py` — KMS, Membran-Thermometer, Horizont-Bit,
  Flächenbilanz, Verdampfung, Familienleiter (18)
- `325_hawking_z3_selektion.py` — ℤ₃-Projektoren, Absorption,
  Trialitätsselektion, Sektorinformation (20)

`python/Dok326_Skripte/`:
- `326_Matzke_FFGFT_verify.py` — Bitwerte, Stabilitätsschwelle, Bekenstein,
  Weinberg-Winkel, T_H-Äquivalenz (15)
- `326_nthresh_skalenabhaengigkeit.py` — Matzkes Kette, Kollapsmasse,
  n_thresh(L), Skalenrekonstruktion, Temperaturempfindlichkeit (12)

`python/Dok327_Skripte/`:
- `327_selbstadjungiertheit_F_verify.py` — Filtrierungs-Lemma, Diagonalform,
  Beschränktheit, ℤ₃-Symmetrie mit Gegenprobe, Defektindizes, fraktales Maß,
  ℤ₃-Restriktion, χ-Twists, λ_min-Stabilität (21)

Gesamt: 112 Assertionen, alle bestanden.

## Geschlossene Brücken in diesem Release

| Brücke | vorher | nachher | Dok. |
|--------|--------|---------|------|
| ξ als Spektralwert eines G(6)-Operators? | offen | **[K]** Nein (negativ abgeschlossen) | 324 |
| ξ = C₂(SU(3))/N_Fourier | — | **[K]** | 324 |
| Hawking: Quant = Horizont-Bit | [S] | **[K]** | 325 |
| Hawking: ℤ₃-Selektion (T_R = 0) | [S] | **[B]** | 325 |
| Hawking: Absorption P_jP_k = 0 | [S] | **[B]** | 325 |
| Hawking: Träger n₄ = 0 | [S] | **[K]** | 325 |
| Hawking: Sektorpaar-Kodierung | [S] | **[B]** | 325 |
| Flächenquant −4ℓ_P²/nat | [S] | **[B]** | 325 |
| Selbstadjungiertheit von F̂ (R82) | [S] | **[B]** vollständig | 327 |
| Defektindex-Klassifikation | [S] | **[B]** (0,0), trivial | 327 |
| ξ = λ_min(F̂_D4) wohldefiniert | implizit | **[B]** Min-Max | 327 |
| Fraktales Maß und Selbstadjungiertheit | offen | **[B]** erhält sie | 327 |
| χ-Twist-Klassen selbstadjungiert | offen | **[B]** alle drei | 327 |
| Δm²₃₂: Zahlenwerte korrigiert | −22 % | **+16,0 %** [K] | 320/322 |
| n_thresh: universell oder skalenabhängig? | [S] | **[B]** skalenabhängig | 329 |
| n_thresh = 6,41 als universelle Zahl | offen | **[X]** negativ abgeschlossen | 329 |

## Verbleibende offene Brücken

| Brücke | Status |
|--------|--------|
| Δm²₃₂ (+16,0 % nach R87; Mischungsterm F₅–F₇) | [S] |
| 2-loop-Korrekturen zu α_s(M_Z) | [S] |
| m_Pl und α_em(M_Z) aus ξ | [S] |
| Quark-/Hadronsektor | offene Brücke (Dok. 318, R76) |
| Graukörper-Faktoren; Fixpunkt-Rückreaktion | [S] (R85) |
| Kosmischer Exponent 41/4 vorwärts (P20) | offen — größter Hebel |
| CMB-Peak-Selektion {1,6,14,26}; \|n\|²=30 | offen (P29/P31) |
| C_ℓ-Quell-/Fensterfunktion | offen (P30) |
| Ω_DM quantitativ modellneutral | offen (P17) |
| Spektraldimension d_s = 1,86 vs. ≈ 2 | offen |
| H₀-Sprachbereinigung; Dok. 026 überarbeiten | offen (P34/P16) |
| ξ als Linienbreite; ι-Einbettung HLV ⊂ FFGFT | vorregistriert (P44, Dok. 297) |

Der Teilchen- und Spektralsektor ist damit weitgehend geschlossen; die
substanziellen offenen Fragen liegen jetzt überwiegend im kosmologischen Sektor,
wo das meiste bei P20 zusammenläuft.

---

## Lizenz

© 2025–2026 Johann Pascher · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

*Bestätigte Ergebnisse sind im Korpus dokumentiert; offene Vorhersagen
bedürfen experimenteller Überprüfung.*
