# Release Notes — v1.3.0 (August 2026)

**DOI:** wird bei Zenodo-Veröffentlichung vergeben — ersetzt v1.2.9  
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

Dieser Release markiert einen natürlichen Ruhepunkt für den FFGFT-Korpus. Die
Kern-Ableitungskette — vom einzigen Geometrieparameter ξ über den Leptonen-Sektor,
die Feinstrukturkonstante, die Gravitationskonstante bis zum kosmologischen Sektor —
ist vollständig. Alle Ergebnisse sind dokumentiert, durch Python-Skripte mit exakter
Arithmetik verifiziert und im append-only Korrekturregister (Dok. 190) eingetragen.
Kein Quelldokument wurde modifiziert; alle Präzisierungen gehen über das Register ein.

Die A-Serie (A010–A273, vier Blöcke) ist die kanonische auditierbare Ausgabe des
Korpus. Jede Aussage trägt einen expliziten epistemischen Marker ([K] abgeleitet,
[B] bewiesen, [SETZUNG] gesetzt, [S] Skizze). Die neuesten Ergänzungen —
Thermodynamik der Berechnung (A271–A273), Abschlussskala und Zeitzyklus (Dok. 312–313),
das D4-Gitter im Hilbertraum (Dok. 314) und die Form der fraktalen Korrektur K_frak
(Dok. 315) — sind eingearbeitet und verifiziert.

## Einstieg für neue Leser

Dok. 205 „FFGFT in einfacher Sprache" (DE+EN, 13–14 Seiten) ist der empfohlene
Einstieg. Es übersetzt den Lagrange-Rahmen in Alltagssprache — schwingende Saiten,
fraktale Küstenlinien, ein gestimmtes Klavier — ohne mathematischen Hintergrund
vorauszusetzen. Jede Aussage ist im formalen Korpus verankert.

Der einzige offene Falsifikationstest ist explizit benannt: m_τ = 1776,97 MeV,
durch Belle-II zu entscheiden, ohne Ausweichmöglichkeit.

## Was sich nicht geändert hat

ξ, die Grundrelation T̃ · m = 1 und alle Ableitungsketten sind unverändert.
Der Korpus ist append-only.

---

## Neue Dokumente seit v1.2.9

### Dok. 311 — Vier auf Drei (1. August 2026, DE+EN)

Wie T⁴/ℤ₃-Kompaktifizierung drei beobachtbare Dimensionen erzeugt.
Eingerollt/ausgerollt-Dualität als Interpretationsrahmen für alle nachfolgenden
Geltungsbereich-Dokumente.  
→ [DE](2/pdf/311_Vier_auf_Drei_De.pdf) · [EN](2/pdf/311_Vier_auf_Drei_En.pdf)

### Dok. 312 — Die Abschlussskala (3. August 2026, DE+EN)

Λ* = 1/R_H² als kosmologischer Λ-Funktionsträger. Antipodaler Befund
η₀ · K_frak ≈ πR_H auf 0,14 %. Vorhersage Ω_m* = 0,3136.  
→ [DE](2/pdf/312_Abschlussskala_De.pdf) · [EN](2/pdf/312_Abschlussskala_En.pdf)

### Dok. 313 — Kein Anfang (3. August 2026, DE+EN)

Zyklische Zeit ohne zeitlichen Ursprung aus der T⁴-Topologie.  
→ [DE](2/pdf/313_Kein_Anfang_De.pdf) · [EN](2/pdf/313_Kein_Anfang_En.pdf)

### Dok. 314 — D4-Gitter im Hilbertraum (5. August 2026, DE+EN)

D4-Gitter als diskrete Struktur der Sub-Planck-Zelle. Negativbefund: 5 ∤ 1152,
daher ist θ = 2/9 kein D4-Gitter-Invariant (gruppentheoretisch).
Trialitätsklassifikation; halbzahlige Darstellungen → Fermion-Statistik [K].  
→ [DE](2/pdf/314_D4_Hilbert_De.pdf) · [EN](2/pdf/314_D4_Hilbert_En.pdf)

### Dok. 315 — Die Form von K_frak (6. August 2026, DE+EN)

Diskriminiert additiv 1 − 100ξ = 74/75 gegen multiplikativ (1 − ξ)^100.
A270-Zeuge diskriminiert 31:1 additiv. Status: Wert [K], Form additiv [B]
(bedingt bestätigt).  
→ [DE](2/pdf/315_Kfrak_Form_De.pdf) · [EN](2/pdf/315_Kfrak_Form_En.pdf)

### Dok. 316 — FFGFT und die Riemannsche Zeta-Funktion (7. August 2026, DE+EN, 23 S. + 12 Skripte)

Überwiegend negatives Ergebnis: Sechs Wege mit Beweis ausgeschlossen. Zwei Identitäten [K]:
Torus-Spektral-Zeta enthält ζ(s) als Faktor; Casimir-Punkt s = −1/2 symmetrisch zur
kritischen Linie. Weyl-Obstruktion [X]: Keine kompakte Mannigfaltigkeit irgendeiner
Dimension hat Laplace-Spektrum gleich den Nullstellen. Bikoherenzmessung [K]:
Kopplung bei Primzahlpotenzen bestätigt. ξ kann nicht helfen: ln(1/ξ) ist eine
Summe von Primzahlenlängen — struktureller Ausschluss.  
→ [DE](2/pdf/316_Riemann_Zeta_De.pdf) · [EN](2/pdf/316_Riemann_Zeta_En.pdf)

### Dok. 317 — Topologischer Ursprung der Leptonen-Generationen: KSAU und FFGFT (20. August 2026, DE+EN, je 7 S.)

Vergleichs- und Synthesedokument KSAU-Theorie ↔ FFGFT. Vollständige
Quantenzahltabellen (n_θ, n_φ, r_i, p_i) für alle sechs Leptonen. Knotenstruktur
3₁/6₃/7₁, Möbius-Energie-Status, Torus-Knoten-Brückentheorem [S].
FFGFT-Seite [K]/[B], KSAU-Knotenzuordnung [S]/[SETZUNG].
Dok. 006 DE+EN um Wicklungszahlen-Unterabschnitt ergänzt.  
→ [DE](2/pdf/317_KSAU_FFGFT_Leptonen_De.pdf) · [EN](2/pdf/317_KSAU_FFGFT_Leptonen_En.pdf)

### Dok. 318 — Geltungsbereich der Masseableitungen in FFGFT (20. August 2026, DE+EN, je 8 S.)

Explizite Grenzziehung: Leptonen-Ruhemassen [K], Hadronmassen offene Brücke,
m_p/m_e nicht beansprucht. Eingerollt/ausgerollt (Dok. 311) als struktureller Grund.
K_frak als Interface-Faktor. α_s(m_τ) = 3ξ^(1/4) [K] (Dok. 160) vs.
α_s(M_Z) = 0,118 als SM-Input.  
→ [DE](2/pdf/318_Masseableitung_Geltungsbereich_De.pdf) · [EN](2/pdf/318_Masseableitung_Geltungsbereich_En.pdf)

### Dok. 319 — Das Proton als schwingender Torus (21. August 2026, DE+EN, je 6 S.)

Geometrische Beschreibung des Protons als schwingender Torus T⁴/ℤ₃. Einschluss ist
relational (Dok. 248): Photon erscheint frei weil wir im selben System sitzen; Gluon
erscheint gebunden weil wir dem Proton-Torus von außen gegenüberstehen. Für m=0 gilt
lokal immer E=pc — reine Energie (Dok. 312). Gluon: nicht-lokalisierbare
ℤ₃/SU(3)-Feldmode, stehende Welle, kein Teilchen. *Aktualisiert 22. Aug.:*
[S]-Markierungen für SU(3)_c und Fixpunkt-Randbedingungen auf [B]/[K] aktualisiert.  
→ [DE](2/pdf/319_Proton_Torus_De.pdf) · [EN](2/pdf/319_Proton_Torus_En.pdf)

### Dok. 320 — Ausführliche Feldgeometrische Spektraltheorie (22. August 2026, DE+EN, 12/8 S.)

Schritt-für-Schritt-Herleitung aller Leptonmassen und Neutrinospektren aus ξ = 4/30000
und T⁴/ℤ₃-Topologie. Verifiziert durch `320_verify.py`.

| Teilchen | Formel | Ergebnis | PDG | Abw. |
|----------|--------|----------|-----|------|
| Elektron | (4/3)ξ^(3/2)v | 0,511 MeV | 0,511 MeV | <0,1 % |
| Myon | (16/5)ξ¹v | 104,96 MeV | 105,66 MeV | −0,66 % |
| Tau | (25/9)ξ^(2/3)v | 1783,5 MeV | 1776,86 MeV | +0,38 % |
| ν₁ (F₂) | m_e · ξ^(9/4) | 0,976 meV | <0,8 eV | [K] |
| ν₂ (F₅) | m_e · ξ² | 9,084 meV | ~8,7 meV | [K] |
| ν₃ (F₇) | m_e · ξ^(9/5) | 44,51 meV | ~49 meV | [K] |
| Δm²₂₁ | m_ν2²−m_ν1² | 8,16×10⁻⁵ eV² | 7,53×10⁻⁵ eV² | +8,3 % [K] |
| Δm²₃₂ | m_ν3²−m_ν2² | 1,90×10⁻³ eV² | 2,44×10⁻³ eV² | −22 % [S] |
| Σm_ν | Summe | 0,0546 eV | <0,12 eV | ✓ |

→ [DE](2/pdf/320_Spektraltheorie_De.pdf) · [EN](2/pdf/320_Spektraltheorie_En.pdf)

### Dok. 321 — Algebraische Herleitung der SU(3)_c-Eichstruktur (22. August 2026, DE+EN, 11/8 S.)

Schließt die in Dok. 319/320/322 als [S] offene Brücke. Verifiziert durch
`321_verify.py` (50+ Assertions bestanden).

**Ergebnisse [B]:**
- Drei ℤ₃-Projektoren P_k auf L²(T⁴): Idempotenz, Orthogonalität, Vollständigkeit bewiesen
- Acht Gell-Mann-Operatoren aus Eigensektoren H₀, H₁, H₂: 𝔰𝔲(3)-Kommutatorrelationen
  mit kanonischen Strukturkonstanten bewiesen
- N_c = 3 algebraisch notwendig (Ordnung der ℤ₃-Gruppe), nicht gesetzt
- Confinement = Trialitäts-Selektion T_R = 0 (algebraische Form von Dok. 049)
- α_s(m_τ) = 3ξ^(1/4) (Dok. 160) jetzt vollständig parameterfrei
- U(1)_Y aus vierter Torus-Richtung T¹ [B]
- SU(2)_L aus ℤ₂-Paarung H₁↔H₂ [B]
- sin²θ_W|_GUT = 3/8 aus Spurformel der fünf Orbifold-Zustände [B]
  (klassisches SU(5)-GUT-Ergebnis, Georgi-Glashow 1974, jetzt aus FFGFT-Geometrie)

→ [DE](2/pdf/321_SU3_Z3_Emergenz_De.pdf) · [EN](2/pdf/321_SU3_Z3_Emergenz_En.pdf)

### Dok. 322 — Spektraltheorie und Hilbertraum-Abbildung (22. August 2026, DE+EN, 12/8 S.)

Mathematisches Fundament der FFGFT-Spektraltheorie.

**Ergebnisse [K]:**
- ξ = λ_min(F̂_D4): Geometrieparameter als kleinster Eigenwert des D4-Sub-Operators
- Zustandsraum H_FFGFT = H_geom ⊗ H_spin ⊗ H_flavor
- Fraktales Maß mit 100-facher Rekursion; D_f = 3 − ξ emergent
- Fixpunkt-Randbedingungen ψ_χ(x₀+y) = χ·ψ_χ(x₀+g*(y)) begründen Neutrino-Lokalisierung
- Verallgemeinerte Fourier-Transformation (GFT), MASA-Basis
- Gell-Mann-Matrizen aus Orbifold-Moden: [B] (Dok. 321)

Offen [S]: vollständiger Selbstadjungiertheits-Beweis für F̂.  
→ [DE](2/pdf/322_Spektraltheorie_Hilbert_De.pdf) · [EN](2/pdf/322_Spektraltheorie_Hilbert_En.pdf)

### Dok. 323 — Herleitung des Weinberg-Winkels bei M_Z (22. August 2026, DE+EN, 8/5 S.)

Schließt die in R78 und Dok. 321 als [S] deklarierte RGE-Brücke. Verifiziert durch
`323_verify.py`.

**Hauptresultat [K]:**

sin²θ_W(M_Z) = 3/8 − (55 α_em(M_Z))/(24π) [ln(m_Pl/M_Z) + (19/12) ln ξ] = **0,2308**

PDG: 0,2312 · Abweichung: **−0,19 %**

- M_GUT = m_Pl · ξ^(19/12) = 8,94×10¹² GeV
- Exponent p = 19/12 = p_e + 1/(4N_c) = 3/2 + 1/12 (Elektron-Massenexponent +
  D4-Phasenkorrektur)
- Externe Eingaben: m_Pl und α_em(M_Z) — offene Brücke [S]

→ [DE](2/pdf/323_Weinberg_Winkel_RGE_De.pdf) · [EN](2/pdf/323_Weinberg_Winkel_RGE_En.pdf)

---

## Korrekturen — R75 bis R83

**R75** (17.–20. Aug.): Shor-/Quantencomputing-Dokumente neu geschrieben. ξ/σ-Trennung,
Aufbereitung ≠ Transformation (95%/5%), Weyl-Obstruktion universell, Fouriertransformation
als Projektion. Dok. 024, 034, 075, 076, 147, 173, 176, 190, 006.

**R76** (20. Aug.): Geltungsbereich der Masseableitungen. Leptonen [K], Hadronsektor
offene Brücke, m_p/m_e nicht beansprucht. → Dok. 318

**R77** (20. Aug.): Dok. 041 — Strukturskizzen in natürlichen Einheiten, keine
SI-Präzisionsableitungen. ξ^(−1/3) = 9,65 (nat.) ≠ α_s(M_Z) = 0,118 (SI). Status: [S].

**R78** (20. Aug.): α_s ist laufende Kopplung. α_s(m_τ) ≈ 0,33 und α_s(M_Z) ≈ 0,118
— verschiedene Werte derselben Konstante. RGE-Brücke offen [S]. *(Geschlossen durch R81.)*

**R79** (22. Aug.): SU(3)_c-Emergenz aus ℤ₃-Trialität [B]. Schließt [S] aus
Dok. 319/320/322. → Dok. 321

**R80** (22. Aug.): SU(2)_L, U(1)_Y, sin²θ_W|_GUT = 3/8 [B]. → Dok. 321

**R81** (22. Aug.): Weinberg-Winkel sin²θ_W(M_Z) = 0,2308 [K], −0,19 %. Schließt R78.
→ Dok. 323

**R82** (22. Aug.): Hilbertraum-Einbettung, Fixpunkt-Randbedingungen [K]. → Dok. 322

**R83** (22. Aug.): Statusbilanz. Geschlossen: 8 Brücken. Verbleibend offen:
Δm²₃₂ (−22 %), Selbstadjungiertheit F̂, 2-loop α_s, m_Pl und α_em aus ξ,
Quark-/Hadronsektor (Dok. 318).

---

## Prüfskripte

`python/Dok320_321_322_Skripte/`:
- `320_verify.py` — Leptonmassen, Neutrinospektrum, Massendifferenzen
- `321_verify.py` — SU(3)-Algebra, Gell-Mann-Matrizen, Weinberg-Spurformel (50+ Assertions)
- `320_322_verify.py` — kombinierte Prüfung Dok. 320 + 322
- `323_verify.py` — Weinberg-Winkel RGE-Herleitung

`python/Shor_Skripte/` (R75):
- `s1_periodensuche.py`, `s2_grenzen.py`, `s3_thermik_zustandsraum.py`

---

## Geschlossene Brücken in diesem Release

| Brücke | vorher | nachher | Dok. |
|--------|--------|---------|------|
| SU(3)_c-Emergenz aus ℤ₃-Trialität | [S] | **[B]** | 321 |
| N_c = 3 algebraisch notwendig | [S] | **[B]** | 321 |
| SU(2)_L, U(1)_Y aus Orbifold-Geometrie | [S] | **[B]** | 321 |
| sin²θ_W\|_GUT = 3/8 (Spurformel) | [S] | **[B]** | 321 |
| Weinberg-Winkel sin²θ_W(M_Z) = 0,2308 | [S] | **[K]** −0,19 % | 323 |
| RGE-Brücke zu sin²θ_W(M_Z) (R78) | [S] | **[K]** | 323 |
| Fixpunkt-Randbedingungen auf T⁴/ℤ₃ | [S] | **[K]** | 322 |
| Gell-Mann-Matrizen aus Orbifold-Moden | [S] | **[B]** | 321 |

## Verbleibende offene Brücken

| Brücke | Status |
|--------|--------|
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
