# FFGFT Changelog
## Korrekturen und Präzisierungen der Dokumentenserie
**Grundlage:** Dok. 190 (allgemein) und Dok. 210 (Wicklungszahlen)
**Stand:** Mai 2026

---

### Hinweise zur Arbeitsmethode

- Ältere Dokumente werden **nicht** verändert — Korrekturen gelten über dieses Changelog
- Jede Änderung ist **in DE und EN** vorzunehmen
- Nach jeder Änderung: **Konsistenz beider Sprachversionen prüfen**
- Eine Sprache kann derzeit ausführlicher sein als die andere — das ist ebenfalls zu dokumentieren
- Status: **offen** / **in Bearbeitung** / **erledigt**

---

## Korrekturen (K) — Inhaltliche Fehler

### K1 — Vorfaktor in der Higgs-Ableitung von ξ
| Feld | Inhalt |
|------|--------|
| Betroffene Dok. | 049 (HTML-Zwischenversion, ältere Arbeitsversionen) |
| Status | **erledigt** (LaTeX war korrekt; nur HTML betroffen) |
| Eingetragen | Mai 2026 |
| Erledigt DE | ✓ Mai 2026 |
| Erledigt EN | ✓ Mai 2026 |

**Falsch:** ξ = λ²h v² / (64π⁴ m²h) ≈ 1,0 × 10⁻⁵
**Korrekt:** ξ = λ²h v² / (16π³ m²h) ≈ 1,33 × 10⁻⁴

Begründung: 64π⁴ war ein Tippfehler in der HTML-Visualisierung. Der korrekte Vorfaktor 16π³ liefert einen Wert konsistent mit Dok. 009.

---

### K2 — Tau-Yukawa-Vorfaktor r_τ
| Feld | Inhalt |
|------|--------|
| Betroffene Dok. | 116 (Tabelle Yukawa-Koeffizienten) |
| Status | **erledigt** |
| Eingetragen | Mai 2026 |
| Erledigt DE | ✓ Mai 2026 |
| Erledigt EN | ✓ Mai 2026 |

**Falsch:** r_τ = 8/3 ≈ 2,667 → m_τ ≈ 1712 MeV (−3,6 % Abw.)
**Korrekt:** r_τ = 25/9 ≈ 2,778 → m_τ ≈ 1783 MeV (+0,4 % Abw.)

---

### K3 — Basisformel für g−2 des Elektrons
| Feld | Inhalt |
|------|--------|
| Betroffene Dok. | 018 (ältere Versionen), T0-Explorer HTML |
| Status | **erledigt** (LaTeX war korrekt; nur HTML betroffen) |
| Eingetragen | Mai 2026 |
| Erledigt DE | ✓ Mai 2026 |
| Erledigt EN | ✓ Mai 2026 |

**Falsch:** a_e = 4π / (f · k_geom)
**Korrekt:** a_e = 2π² / (f · k_geom)

Begründung: 4π ist die Oberfläche der 2D-Kugel im 3D-Raum. Korrekt ist S₃ = 2π², die Oberfläche der 3D-Sphäre als Rand des 4D-Torus. Die fraktalen Korrekturen für Myon und Tau verwenden weiterhin 4π (Gl. 190.5/190.6).

---

## Präzisierungen (P) — Klarstellungen ohne Fehler

### P1 — Genauigkeit der Koide-Formel
| Status | **erledigt** | Erledigt DE | ✓ Mai 2026 | Erledigt EN | ✓ Mai 2026 |

ΔQ < 0,00003 % (Dok. 116) = interne Konsistenz der T0-Formeln. 0,001 % (Dok. 158) = experimentelle Messunsicherheit (PDG 2022). Für **externe Kommunikation gilt 0,001 %**.

### P2 — ℏ aus dem Higgs-Feld
| Status | **erledigt** | ✓ Mai 2026 DE/EN |

Verbindliche Ableitungskette: ξ → L₀ = ξ · ℓ_P → ℏ ~ √ξ · ℓ_P · c. ℏ folgt aus ξ, ist **kein Postulat**.

### P3 — Zwei ξ-Parameter
| Status | **erledigt** | ✓ Mai 2026 DE/EN |

Zwei verschiedene Parameter: ξ₀ = 4/30000 (geometrisch) und ξ_Higgs (algebraisch). Nicht identisch.

### P4 — L₀ als geometrische Fundamentallänge
| Status | **erledigt** | ✓ Mai 2026 DE/EN |

L₀ ist **nicht** der Schwarzschild-Radius, sondern die geometrische Fundamentallänge des T0-Rahmens.

### P5 — Massenstruktur aus ξ, nicht exakte Massen
| Status | **erledigt** | ✓ Mai 2026 DE/EN (Dok 030, 061, 028) |

"FFGFT berechnet Massen exakt" → "FFGFT leitet die Massenstruktur aus ξ ab; Übereinstimmung mit Experiment ~1 %."

### P6 — Koide nur mit numerischen Werten
| Status | **erledigt** | ✓ Mai 2026 DE/EN |

Koide-Relation nur mit numerischen PDG-Werten ausdrücken (Nichtabschluss, Dok. 193).

### P7 — Renormierungsgruppe ist kein FFGFT-Werkzeug
| Status | **erledigt** | ✓ Mai 2026 DE/EN |

"Renormierungsgruppe" als FFGFT-Werkzeug → "Skalenstruktur aus der Rekursion R".

### P8 — Fraktale Renormierung ist kein Eigenbegriff
| Status | **erledigt** | ✓ Mai 2026 DE/EN |
| Nachträgliche Korrektur EN | ✓ Mai 2026 (012, 014, 041, 060) |

"Fraktale Renormierung" / "Fractal Renormalization" → "fraktale Korrektur" / "Fractal Correction".
**Stichprobe Mai 2026:** EN-Dateien hatten noch "Fractal Renormalization" in 012, 014, 041, 060 — nachträglich auf "Fractal Correction" korrigiert. Dok. 190 EN behält den Begriff als historischen Bezug.

### P9 — Farbladung-Spalten in Tabellen
| Status | **erledigt** | ✓ Mai 2026 DE/EN |

Spalten "Symmetrie" + "Farbe" + N_c = 3 → Spalten "Skalierungsklasse" + "SM-Korrespondenz".

### P10 — Faktor K = 245 und empirischer Anker
| Status | **erledigt** | ✓ Mai 2026 DE/EN |

K = R_pe / (4/3)⁷: ein empirischer Anker. Faktor 1,314 ist implizit definiert, nicht hergeleitet.

### P11 — K_frak und T_CMB-Korrektur
| Status | **erledigt** | ✓ Mai 2026 DE/EN |

Korrekte Formel: (1 − 275/4 · ξ), Δ = 0,0002 %. Dok. 003 und Dok. 133 verwenden **verschiedene Modelle** für K_frak.

### P12 — ΔCHSH-Werte in Dok. 022 und Dok. 230
| Status | **erledigt** | ✓ Mai 2026 DE/EN |

Zwei verschiedene Observablen: kumulativ (Dok. 022, N=73: 5×10⁻⁴) vs. elementar ξ/(2π) (Dok. 230: 10⁻⁵).

### P13 — Brückenformel ξ_FFGFT vs. ξ_UIFT
| Status | **erledigt** | ✓ Mai 2026 DE/EN |

ξ_FFGFT / ξ_UIFT = m_e c² / ((16/9)·ln2·eV) ≈ 414.684.

---

## Wicklungszahl-Präzisierungen (W)

### W1–W6
Alle erledigt Mai 2026, DE und EN konsistent.
- W1: f = 7500 universal, nicht teilchenspezifisch (060, 018, 149)
- W2: (n_θ, n_φ) = Spin; alle Fermionen (1,1) (051, 202)
- W3: Generationen = fraktale Verzweigungen (018, 149)
- W4: (n,l,j) mehrdeutig → (k_x,k_y,k_z,k_t) primär (005, 006, 042, 202)
- W5: f_i mehrdeutig; Yukawa-Form kanonisch (005, 006, 032)
- W6: Arithmetisch → geometrische Folge q = 2/3 (116, 158, 203, 202)

---

## Neue Dokumente (N)

| ID | Dokument | Status | Datum |
|----|---------|--------|-------|
| N246 | Dok. 246 — RSG und FFGFT: Ein struktureller Vergleich (DE+EN) | **erledigt** | Mai 2026 |
| N247 | Dok. 247 — Information, Zustand und Prozess (DE+EN) | **erledigt** | Mai 2026 |

---

## DE/EN-Symmetrierung (S) — Mai 2026

Übernahme der jeweils längeren Version unter Konsistenzprüfung gegen das Changelog (P7, P8 etc.) bevor Inhalte adoptiert wurden:

### S1 — Dok 009: DE „Schlussfolgerung" → EN „Conclusion"
| Status | **erledigt** | Mai 2026 |
| Übersetzungsrichtung | DE → EN |

Vollständige `\section{Conclusion}` aus DE übertragen mit 3 Unterabschnitten (κ=7 nicht angepasst, 10⁻⁴-Begründung, Fundamental Derivation tcolorbox).

### S2 — Dok 175: 8 DE-Unterabschnitte → EN
| Status | **erledigt** | Mai 2026 |
| Übersetzungsrichtung | DE → EN |
| Zähler | 32/32 (war 32/24) |

Übernommen:
- "Limits of QND Measurement"
- "Not Restricted to Two States: Infinitely Many Analog Transitions"
- "The Analog Resolution Limit --- and Its Continuation in High-Frequency Technology" (mit großer Frequenz-Tabelle AM bis UV)
- "Above Optics --- Three Regimes up to the Pair-Production Threshold"
- "The Cannonball Limit in FFGFT: Scale Incompatibility of Two Torsion Patterns"
- "The Pair-Production Threshold as Natural Endpoint of the ξ-Ladder"
- "Convergence: Carrier Frequency Meets Internal Transition Frequency on ξ-Level N≈8-9"
- "Restructuring between Levels: When Does It Happen and When Not?"

Konsistenzprüfung: kein Konflikt mit Changelog P7/P8 (keine "Renormierungsgruppe", keine "fraktale Renormierung" als FFGFT-Primitiv); "exakt" nur in Frequenz-Skalen-Kontexten verwendet, nicht in Massen-Genauigkeitsclaims.

### S3 — Dok 022: 5 EN-Sektionen → DE
| Status | **erledigt** | Mai 2026 |
| Übersetzungsrichtung | EN → DE |
| Zähler | 34/34 (war 28/34) |

Übernommen:
- "Die ξ-Anpassungs-Frage: emergent oder ad-hoc?"
- "Lokalität und Bell-Theorem"
- "Anhang: ML-Trainingsdetails (zur Reproduzierbarkeit)"
- "ξ-Anpassungs-Methodik"
- "Vergleichstabelle: T0-Original vs. T0-ML" (inkl. Comparison Table)

Konsistenzprüfung: Lokalitätsabschnitt rahmt T0 als "lokale Modifikation der Erwartungswerte, kein Verstoß gegen lokale Kausalität" — konsistent mit Dok 230 (Z.522-524: Bell als topologische Verbindung, nicht nicht-lokale Korrelation). Historischer Kontext: 022 ist explizit Nov-2025-Addendum, vor Dok 230 (Mai 2026); Sprachgebrauch "lokale verborgene Variablen" ist die ältere Formulierung, in 230 zur "topologischen Verbindung" auf T⁴ reformuliert.

### S4 — Dok 012: 3 DE-Unterabschnitte → EN
| Status | **erledigt** | Mai 2026 |

- "T0 Perspective: G in Two Representations"
- "Document Structure"
- "Connection to the Planck Scale"

### S5 — Dok 013: DE-„Schlussfolgerung" und „Bibliografie" → EN
| Status | **erledigt** | Mai 2026 |

`\section{Conclusion: Geometric Unity}` mit keyresult-Box und finalem Einsichten-fbox; sowie `\section{Bibliography}` als Titel vor existierendem `\begin{thebibliography}`.

### S6 — Dok 014: DE-„Fazit" → EN „Conclusion"
| Status | **erledigt** | Mai 2026 |

Sektion „Conclusion" und Unterabschnitt „Conclusion: The Duality of Geometric Idealization and Physical Measurement" übernommen. Begriff „renormalization" (allgemein) statt „fractal renormalization" — konform mit P8.

### S7 — Dok 042: DE-„Schlussfolgerungen und zukünftige Richtungen" + Bibliografie → EN
| Status | **erledigt** | Mai 2026 |

Section „Conclusions and Future Directions" mit Unterabschnitten „Revolutionary Achievements" und „Final Philosophical Reflection". Bibliografie übersetzt.

### S8 — Dok 046: DE-„Abschließende Bewertung" + Bibliografie → EN
| Status | **erledigt** | Mai 2026 |

Section „Final Assessment" mit „Scientific Status" und „Significance for Fundamental Physics". Bibliografie übersetzt.

### S9 — Dok 133: bidirektional
| Status | **erledigt** | Mai 2026 |

DE → EN: „Multiple Perspektiven auf K_frak" Section mit Perspektiven 1/2/3 (Power Formula, Linearized Form, Ratios are Exact) übersetzt und in EN eingefügt.
EN → DE: „Distinction: Fractal Corrections vs. Rounding Errors" Section + „References" Section übersetzt und in DE eingefügt.

### S10 — Dok 189: DE
| Status | **erledigt** | Mai 2026 |

DE hatte einen Texteditierungs-Artefakt „LATEX" als eigene Zeile nach „Querverweise" — entfernt. Hinzugefügt: `\section{Planck-Größen als Übersetzungsfaktoren}` als Wrapper für „Zwei verschiedene Rollen der Planck-Größen" (war in DE als orphan-Subsection ohne Section, in EN korrekt als Section).

### S11 — Dok 005, 028, 030, 116: jeweils kleine DE-Conclusion fehlte in EN
| Status | **erledigt** | Mai 2026 |

- 005 EN: `\subsection{Conclusion}` zwischen „Connection to Other T0 Documents" und „Detailed Explanation of the Fractal Mass Formula"
- 028 EN: `\section{Conclusion}` zwischen „Hierarchy of ξ-Coupling" und Appendix-Sektion
- 030 EN: `\section{Conclusion}` vor `\begin{thebibliography}`
- 116 EN: `\section{Conclusion}` (mit `\begin{theorem}`-Box) am Dokumentende

---

## Übersichtstabelle — Alle Einträge

| ID | Status | Bemerkung |
|----|--------|-----------|
| K1–K3 | ✓ Mai 2026 | inhaltliche Fehler |
| P1–P13 | ✓ Mai 2026 | Präzisierungen |
| W1–W6 | ✓ Mai 2026 | Wicklungszahlen |
| N246, N247 | ✓ | neue Dokumente |
| S1–S11 | ✓ Mai 2026 | DE/EN-Symmetrierung |

---

## Dok 190 Verweise entfernt

| Dokument | Maßnahme |
|---------|---------|
| Dok 013 DE+EN | P13 Inhalt (ξ_UIFT Brückenformel) direkt eingebaut |
| Dok 202 DE+EN | P5, P7 Verweise entfernt |
| Dok 205 DE+EN | P5 Verweise entfernt |
| Dok 243 DE+EN | R12 Verweise ersetzt durch Querverweise auf Dok 022 und 230 |
| Dok 244 DE+EN | R13 Verweise ersetzt durch Querverweise auf Dok 013 |
| Dok 241 DE+EN | Dok 190 und 210 aus Lesepfad-Liste entfernt |

---

## Anhang — Technische LaTeX-Korrekturen (Mai 2026)

| Datei | Korrektur |
|-------|-----------|
| `175_De_ch.tex` Z.1161 | `\textbf{Paarerzeugung.\\ Natürl.~Obergrenze.}` → `\textbf{Paarerzeugung, Natürl.~Obergrenze.}` (das `\\` in `\textbf{}` brach die Tabellenzelle) |
| `244_{De,En}_ch.tex` | Unicode-Mathezeichen außerhalb von Math-Mode ($ℓ$, $ℝ$, $ℤ$, $ℂ$, $ℕ$) durch LaTeX-Befehle ersetzt |
| `244_{De,En}.tex` Wrapper | `\title{}` mit `$L^2(T^4)$` und `$\ell^2(P_N)$` statt Unicode |
| `189_De_ch.tex` | Stray-Text „LATEX" auf eigener Zeile entfernt |
| Diverse EN-Dateien (012, 014, 041, 060) | „Fractal Renormalization" → „Fractal Correction" (P8-konform) |

---

## Anhang — Symmetrie-Status DE/EN

Stand Mai 2026: **alle 31 Dokumentpaare strukturell symmetrisch** (gleiche Anzahl `\section` + `\subsection` in beiden Sprachen). Stichproben des inhaltlichen Gleichlaufs erfolgten gegen das Changelog (Terminologie P7/P8, Formeln K2/K3, Wertangaben P11/P12).

---

## Anhang — Technische Build-Anpassungen (Mai 2026)

Standalone-Präambel auf LuaLaTeX angepasst:
- Babel: `\usepackage[provide=*,german]{babel}` / `[provide=*,english]`
- Schriftarten: `\usepackage{fontspec}` mit `\setmainfont{Latin Modern Roman}`, `\setsansfont{Latin Modern Sans}`, `\setmonofont{Latin Modern Mono}`
- `unicode-math` nicht aktiviert: Konflikt mit `\th` aus dem `physics`-Paket. Mathematik nutzt weiterhin Computer Modern.
- Hinzugefügt: `csquotes`, `fancyhdr`
- T0-Farben definiert (`T0blue`, `T0gray`, `T0green`, `T0red`, `T0orange`) + Lowercase-Aliase für TikZ
- Kurzkommandos als `\providecommand`: `\xipar`, `\xigeom`, `\Kfrak`, `\Tfield`, `\Dfrak`, `\Efield`, `\tT`, `\Lagr`, `\Order`
- Alle Custom-tcolorbox-Environments definiert

**Wrapper:** 28 Wrapper neu erzeugt für Dateien ohne Wrapper im Originalmaterial.

**Ergebnis:** alle 62 PDFs (31 Dokumente × DE/EN) erfolgreich kompiliert.
