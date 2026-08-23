# Release Notes — v1.3.2 (August 2026)

**DOI:** wird bei Zenodo-Veröffentlichung vergeben — ersetzt v1.3.1  
Laufende Korrekturen: **[2/pdf/190_T0_Korrekturen_De.pdf](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/190_T0_Korrekturen_De.pdf)**  
Changelog: **[000_FFGFT_Changelog_De.md](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/000_FFGFT_Changelog_De.md)**  
A-Serie-Log: **[A_Serie_Export/A_SERIE_CHANGELOG.md](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/A_Serie_Export/A_SERIE_CHANGELOG.md)**

**FFGFT — Fundamentale Fraktale Geometrische Feldtheorie** zeigt: Alle Konstanten des
Standardmodells folgen aus einem einzigen dimensionslosen Parameter **ξ = 4/30000**
auf einem kompakten 4D-Torus T⁴. Die Grundrelation ist **T̃ · m = 1** — intrinsische
Zeit und Masse sind invers gekoppelt.

**Autor:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Überblick

Dieser Release schließt eine der ältesten offenen Brücken des Korpus: den
mikroskopischen Hawking-Mechanismus. Dok. 313 (Kap. G) hatte den thermodynamischen
Rahmen gelegt — die eine KMS-Regel für Unruh, Gibbons-Hawking und Schwarze Löcher —,
die Emissionsseite aber als Skizze [S] gebucht. Dok. 325 arbeitet sie vollständig
aus FFGFT-eigenen Bausteinen aus: Temperatur, Quant, Selektion, Träger und
Informationserhaltung stehen jetzt auf [K]/[B] (Register R85).

Der zentrale neue Befund: **das Hawking-Quant ist das systemabhängige Bit der
Horizontskala** — k_B·T_H = ħc/(4π·r_s) = E_bit(L = 4π·r_s) exakt. Die
FFGFT-Position, dass Bitwerte systemabhängig sind (Dok. 257, 302, A271–A273),
ist damit kein Hindernis für die Hawking-Physik, sondern ihre Erklärung.
Ein universeller Bitwert wird nirgends benötigt.

Flankiert wird der Mechanismus von zwei Vergleichsdokumenten zu Douglas Matzkes
Algebra-Frameworks: Dok. 324 (G(6,ℤ₃C)-Vakuumstruktur, mit der Casimir-Herleitung
ξ = C₂(SU(3))/N_Fourier, Register R84) und Dok. 326 (Hyperbit-Schwarzloch-Physik,
Schwerpunkt Landauer und Bitwerte). Beide dokumentieren bemerkenswerte strukturelle
Konvergenzen — und die eine tiefe Divergenz: universelle vs. systemabhängige
Bitwerte.

Kein Quelldokument wurde modifiziert; alle Präzisierungen gehen über das
append-only Korrekturregister (Dok. 190, R84–R85) ein.

## Einstieg für neue Leser

Dok. 205 „FFGFT in einfacher Sprache" (DE+EN, 13–14 Seiten) bleibt der empfohlene
Einstieg. Der einzige offene Falsifikationstest ist unverändert explizit benannt:
m_τ = 1776,97 MeV, durch Belle-II zu entscheiden, ohne Ausweichmöglichkeit.

## Was sich nicht geändert hat

ξ, die Grundrelation T̃ · m = 1 und alle Ableitungsketten sind unverändert.
Die Hawking-Temperaturformel selbst ist Standard — neu ist ihre Herleitung
und Mikrostruktur innerhalb der FFGFT.

---

## Neue Dokumente seit v1.3.1

### Dok. 324 — G(6,ℤ₃C)-Vakuumstruktur und FFGFT (DE+EN, je 8 S.)

Numerische Untersuchung der Verbindungsfragen zwischen Matzkes
G(6,ℤ₃C)-Vakuumstruktur und der FFGFT-Spektraltheorie.

- **Trine-Theorem [B]:** T_k³ = 1 in 8-dim. Spinordarstellung (δ < 6,5×10⁻¹⁶).
- **Vakuumoperator V [B]:** Rang-1-Projektor, Spektrum {0⁽⁷⁾, 1⁽¹⁾}.
- **ξ kein Spektralwert [K]:** abgeschlossener negativer Befund (R84).
- **Casimir-Herleitung [K]:** ξ = C₂(SU(3)_fund)/N_Fourier = (4/3)/10⁴ = 4/30000.
  C₂ = 4/3 aus N_c = 3 [B] (Dok. 321); N_Fourier = 10⁴ aus der T⁴-Topologie.

→ [DE](2/pdf/324_G6_Z3C_FFGFT_Vergleich_De.pdf) · [EN](2/pdf/324_G6_Z3C_FFGFT_Vergleich_En.pdf)

### Dok. 325 — Der FFGFT-Hawking-Mechanismus (DE+EN, je 7 S.)

Vollständige Ausarbeitung aus FFGFT-eigenen Bausteinen; schließt die
Emissionsseite von Dok. 313 Kap. G. Die fünf Bausteine:

1. **Temperatur [K]** — KMS-Regel T = ħ/(k_B·τ) mit Membran-Periode
   τ = 8πGM/c³ aus T̃·m=1; ein Prinzip für Unruh, Gibbons-Hawking, Schwarze Löcher.
2. **Quant [K]** — k_B·T_H = ħc/(4π·r_s) = E_bit(4π·r_s) exakt:
   das Hawking-Quant ist das Bit der Horizontskala.
3. **Selektion [B]** — nur T_R = 0 entkommt; Absorption = ℤ₃-Projektor-Orthogonalität
   P_j·P_k = 0. Confinement (Dok. 321) und Hawking-Selektion sind ein Prinzip.
4. **Träger [K]** — masselose n₄=0-Torusmode; massive Moden fallen zurück
   (Uhrenstauchung).
5. **Information [K]/[B]** — Sektorpaar (k,−k) orthogonal lesbar (log₂3 Bit/Quant);
   Flächenquant −4ℓ_P²/nat aus Bekenstein+Clausius; feinkörnige Entropie konstant
   (Unitarität, Dok. 322). Kein Informationsparadoxon.

Zusätzlich: Leistungskorrektur (1−ξ·ln(M/m_P)) = 0,6–1,4 %; M* = 3,3×10¹¹ kg;
Familienleiter r_s = R_H/2 exakt. Offen [S]: Graukörper-Faktoren,
Fixpunkt-Rückreaktion.

→ [DE](2/pdf/325_Hawking_FFGFT_De.pdf) · [EN](2/pdf/325_Hawking_FFGFT_En.pdf)

### Dok. 326 — Schwarze Löcher aus Hyperbits und aus FFGFT (DE+EN, je 10 S.)

Vergleich mit Matzkes Hyperbit-Framework (IPI 2026) — Schwerpunkt Landauer,
Bitwerte, systemabhängige Bit-Energie.

- **Konvergenzen [B]:** Fermion-Generation = algebraische Grundeinheit;
  N_c = 3 erzwungen; r_s ohne ART; beide Hawking-Mechanismen strukturell
  exakt korrespondierend.
- **Divergenz:** universeller Bitwert (Matzke, Landauer bei T_P) vs.
  systemabhängige Bit-Energie E_bit = ħc/L (FFGFT [K]).
- **Numerisch:** T_H(Matzke)/T_H(KMS) = 1,000000 — der universelle Bitwert
  ist eine Umparametrisierung, keine unabhängige physikalische Eingabe.
- Matzkes Stabilitätsschwelle n_thresh = 6,41 als universelle Zahl: [X]
  (hängt an der Setzung T = T_P).

→ [DE](2/pdf/326_Matzke_FFGFT_Vergleich_De.pdf) · [EN](2/pdf/326_Matzke_FFGFT_Vergleich_En.pdf)

---

## Korrekturen — R84 bis R85

**R84** (23. Aug.): ξ = C₂(SU(3)_fund)/N_Fourier = (4/3)/10⁴ = 4/30000 [K]
(Dok. 324). ξ ist kein Spektralwert eines G(6)-Operators; die Verbindung
zwischen G(6,ℤ₃C) und FFGFT liegt im Casimir-Quotienten, nicht im Spektrum.

**R85** (23. Aug.): Hawking-Mechanismus mikroskopisch geschlossen [K]/[B]
(Dok. 325). Die in Dok. 313 Kap. G als [S] geführte Emissionsseite ist auf
[K]/[B] gehoben. Offen bleiben Graukörper-Faktoren und Fixpunkt-Rückreaktion [S].

---

## Prüfskripte

`python/Dok320_321_322_Skripte/`:
- `324_G6_FFGFT_verify.py` — Trine-Theorem, Vakuumoperator, Casimir-Herleitung (16 Assertions)

`python/Dok325_Skripte/`:
- `325_hawking_ffgft_mechanismus.py` — KMS, Membran-Thermometer, Horizont-Bit, Flächenbilanz, Verdampfung, Familienleiter (18 Assertions)
- `325_hawking_z3_selektion.py` — ℤ₃-Projektoren, Absorption, Trialitätsselektion, Sektorinformation (20 Assertions)

`python/Dok326_Skripte/`:
- `326_Matzke_FFGFT_verify.py` — Bitwerte, Stabilitätsschwelle, Bekenstein, Weinberg-Winkel, T_H-Äquivalenz (15 Assertions)

Alle 69 Assertions bestanden.

---

## Geschlossene Brücken in diesem Release

| Brücke | vorher | nachher | Dok. |
|--------|--------|---------|------|
| ξ als Spektralwert von G(6)-Operator? | offen | **[K]** Nein (negativ abgeschlossen) | 324 |
| ξ = C₂(SU(3))/N_Fourier | — | **[K]** | 324 |
| Hawking: Quant = Horizont-Bit | [S] | **[K]** | 325 |
| Hawking: ℤ₃-Selektion (T_R = 0) | [S] | **[B]** | 325 |
| Hawking: Absorption P_jP_k = 0 | [S] | **[B]** | 325 |
| Hawking: Träger n₄ = 0 | [S] | **[K]** | 325 |
| Hawking: Sektorpaar-Kodierung | [S] | **[B]** | 325 |
| Flächenquant −4ℓ_P²/nat | [S] | **[B]** | 325 |

## Verbleibende offene Brücken

| Brücke | Status |
|--------|--------|
| Graukörper-Faktoren | [S] |
| Rückreaktion auf Orbifold-Fixpunkte | [S] |
| Δm²₃₂ (−22 %, atmosphärisch) | [S] |
| Selbstadjungiertheits-Beweis für F̂ | [S] |
| 2-loop-Korrekturen zu α_s(M_Z) | [S] |
| m_Pl und α_em(M_Z) aus ξ | [S] |
| Quark-/Hadronsektor | offene Brücke (Dok. 318) |

---

## Lizenz

© 2025–2026 Johann Pascher · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

*Bestätigte Ergebnisse sind im Korpus dokumentiert; offene Vorhersagen
bedürfen experimenteller Überprüfung.*
