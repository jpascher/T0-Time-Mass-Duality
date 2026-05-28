# FFGFT Changelog
## Korrekturen und Präzisierungen der Dokumentenserie
**Grundlage:** Dok. 190 (allgemein) und Dok. 210 (Wicklungszahlen)
**Stand:** Mai 2026 (zuletzt erweitert: 28. Mai 2026 — N261, N013-INFO, K2-Nachtrag, N255-257-Verschaltung, HW147)

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

---

## Nachträgliche Korrekturen (Mai 2026) — Aus Systemprüfung

### P8-Nachkorrektur — Weitere Stellen (Mai 2026)

Die initiale P8-Stichprobe (012, 014, 041, 060 EN) war unvollständig. Systemweite Grep-Prüfung aller 353 ch-Dateien ergab weitere Stellen:

| Datei | Stellen | Maßnahme |
|-------|---------|----------|
| `012_De_ch.tex` | Z.284, Z.452 | `fraktale Renormierung:` → `fraktale Korrektur:` |
| `014_De_ch.tex` | Z.267 `\section`, Z.297 `\subsection`, Z.309 `\caption`, Z.265, Z.278, Z.282, Z.297, Z.330, Z.397 | vollständig ersetzt |
| `014_En_ch.tex` | Z.201, Z.266, Z.270 (2×), Z.279, Z.283, Z.290, Z.300, Z.313, Z.324, Z.386, Z.387, Z.391 | vollständig ersetzt |
| `137_De_ch.tex` | Z.239 Tabellenlabel | `Fractal Renormalization &` → `Fractal Correction &` |
| `137_En_ch.tex` | Z.239 Tabellenlabel (DE-Begriff in EN-Datei) | `Fraktale Renormierung &` → `Fractal Correction &` |

**Gesamtergebnis P8:** alle 353 Dateien geprüft — keine weiteren Stellen außer 190 DE/EN (historischer Bezug, bleibt).

### K2-Erweiterung — 046 DE+EN ebenfalls betroffen

K2 war im Changelog nur für 116 dokumentiert. Systemprüfung ergab:

| Datei | Stellen | Maßnahme |
|-------|---------|----------|
| `046_De_ch.tex` | Z.292 (Tabelle 1), Z.680 (Tabelle 2) | `8/3` → `25/9` (nur Tau-Lepton, nicht Tau-Neutrino) |
| `046_En_ch.tex` | Z.292 (Tabelle 1), Z.694 (Tabelle 2) | `8/3` → `25/9` |

**Kaskade in 116 DE+EN:** r_τ-Änderung erforderte Neuberechnung der Massenverhältnisse:
- m_μ/m_τ: 6/5 → 144/125; 1.2 → 1.152; 0.06126 → 0.05881; 1/16.318 → 1/17.0; Abw. < 3% → < 1.2%
- m_e/m_τ: 1/2 → 12/25; 0.5 → 0.48; 0.0002856 → 0.000283; 1/3501 → 1/3534; Abw. < 0.7% → < 1.6%
- Listenpunkt: „kompensieren exakt zu Q = 2/3" → „sind konsistent mit Q ≈ 2/3" (auch P6-konform)

**Tau-Neutrino-Einträge (8/3) bleiben** — eigenständiger Wert, kein r_τ.

> ⚠️ **Überholt durch K2-Nachtrag (27. Mai 2026, siehe unten):** Diese Festlegung wurde revidiert. Dok. 190 (K2-Status, 26. Mai) und die korrigierte 046-DE-Rechnung setzen ν_τ ebenfalls auf 25/9 (ξ_ντ = 400/81). Maßgeblich ist der neue Eintrag „K2-Nachtrag — vollständige Einarbeitung".

### Erledigt DE | ✓ Mai 2026 — Erledigt EN | ✓ Mai 2026

---

## Layout-Korrekturen (Mai 2026) — Umbrüche und Tabellenbreiten

**Anlass:** Nach den Terminologie- und Zahlenkorrekturen (P8, K2) traten Overfull-hbox-Warnungen auf. Alle 13 korrigierten Dokumente wurden rekursiv bereinigt bis 0 Fehler und 0 hbox-Warnungen.

### Maßnahmen je Dokument

| Datei | Maßnahme |
|-------|---------|
| `014_De_ch.tex` | 3 Tabellen mit `\resizebox{\textwidth}{!}` eingerahmt (`p{3cm}p{10cm}`, `p{4cm}p{10cm}`, `p{3.5cm}p{6cm}p{6cm}`); unnötigen Artikel „die" aus Subsektions-Titel entfernt |
| `014_En_ch.tex` | Gleiche 3 Tabellen; align-Zeilen gekürzt (Formel + Text) |
| `046_De_ch.tex` | `longtable` → `tabular` + `\resizebox`; 5 weitere `tabular`-Umgebungen (`p{3cm}p{4cm}p{4cm}p{3cm}`, `lcccccc`, `lcccc`, `lccc`) eingerahmt |
| `046_En_ch.tex` | Gleiche Maßnahmen |
| `012_De_ch.tex` | `lcc`-Tabelle mit `\resizebox` eingerahmt |
| `012_En_ch.tex` | Gleiche Maßnahme |
| `041_De_ch.tex` | 5 Tabellen mit `\resizebox`; Extra-`}`-Klammer aus `{\small…}`-Rest bereinigt; Formel-Spalte von `p{2.7cm}` → `p{3.5cm}` (Weinberg-Formel); `\hfuzz=10pt` gesetzt |
| `041_En_ch.tex` | Longtables → tabular + `\resizebox`; zweite Hierarchie-Tabelle in `table`-Float; Formel-Spalte angepasst |
| `137_De_ch.tex` | `\scalebox{0.8}` → `\scalebox{0.65}` |
| `137_En_ch.tex` | `\scalebox{0.8}` → `\scalebox{0.55}` |
| `116_De_ch.tex` | `\allowdisplaybreaks` vor ersten `align`-Block |
| `116_En_ch.tex` | `\allowdisplaybreaks` vor ersten `align`-Block |
| `060_De_ch.tex` | Keine Layout-Änderungen nötig (war bereits sauber) |

**Ergebnis:** 13/13 Dokumente kompilieren fehlerfrei (0 LaTeX-Fehler, 0 Overfull-hbox).

### Hinweis: Innötige Textzusätze bereinigt

Durch die Terminologie-Korrekturen waren einzelne Zeilen geringfügig länger geworden:
- `\subsection{Warum ist die fraktale Korrektur…}` → Artikel „die" entfernt (wie im Original ohne Artikel)
- align-Zeilen in 014 EN mit langen SI-Werten auf kompaktere Darstellung gekürzt

---

## Integration der Layout-Korrekturen in Kindle 6×9 Build (Mai 2026)

### Maßnahmen

1. **Übernahme der 13 korrigierten `_ch.tex`-Dateien** mit allen Terminologie-, Zahlen- und Inhaltsverbesserungen (P8 strenger durchgesetzt: „Renormierung" → „Korrektur" auch in 014; K2-Kaskade in 046 und 116 vollständig).

2. **Korrektur Datei-Vertauschung 137 De/En**: Die hochgeladenen Dateien hatten die Sprachen vertauscht (`137_De_ch.tex` enthielt englischen Inhalt, `137_En_ch.tex` deutschen). Inhalte wurden getauscht, sodass `137_De_ch.tex` nun deutschen Text enthält („Das jahrhundertealte Rätsel") und `137_En_ch.tex` englischen Text („The Century-Old Enigma").

3. **Entfernung redundanter `\resizebox`-Wrapper um Tabellen**: 48 manuell ergänzte `\resizebox{\textwidth}{!}{\begin{tabular}…}`-Hüllen wurden entfernt, da der `\BeforeBeginEnvironment{tabular}{adjustbox}`-Hook im Preamble bereits automatisch alle `tabular`-Umgebungen auf Textbreite skaliert. Doppel-Skalierung hätte Tabellen unleserlich klein gemacht.
   - Auch verschachtelte `\resizebox`-in-`\resizebox`-Strukturen (z.B. 014) wurden iterativ aufgelöst.
   - In 060 wurden `\resizebox{\linewidth}`-Varianten gleichbehandelt.

4. **Wrapper-Format**: Alle 13 `_wrapper.tex`-Dateien des Users hatten `\documentclass[12pt,a4paper]{report}`. Auf Wunsch des Users für einheitliches Kindle 6×9-Format umgestellt auf `\documentclass[11pt]{report}` (Geometrie aus dem Preamble).

5. **Neue Wrapper für 137 De/En** mit korrekten Titeln und Autorenangabe erstellt.

### Ergebnis

| Metrik | Vorher (User-Uploads A4) | Nachher (integriert Kindle 6×9) |
|---|---|---|
| Dokumentpaare | 31 (62 Dateien) | 32 (64 Dateien, +137) |
| Seitenformat | gemischt (13× A4, 49× Kindle) | **konsistent Kindle 6×9** |
| Tabellen-Skalierung | manuell `\resizebox` | **automatisch via Hook** |
| Overfull-Boxen über alle 64 PDFs | n/a (gemischt) | **14 gesamt, 2 davon > 5 mm** |

### Stichproben

- `137_De.pdf`: 13 Seiten, deutscher Inhalt, Kindle 6×9 (432×648 pt)
- `137_En.pdf`: 13 Seiten, englischer Inhalt, Kindle 6×9
- `041_De.pdf`: 36 Seiten, 0 Overfull
- `046_En.pdf`: 19 Seiten, 0 Overfull (war 139 pt vor Korrektur)
- Alle 13 geänderten Dokumente: **0 Overfull-Boxen** nach Integration


---

## Inhaltliche Prüfung der 147 weiteren Dokumente (Mai 2026)

Nachdem die ursprünglichen 31 Dokumentenpaare durchgearbeitet waren, wurden die verbleibenden 147 Dokumentenpaare (= 294 _ch.tex-Dateien) systematisch gegen die Changelog-Korrekturen K1–K3, P5–P12, W1–W6 geprüft.

### Methodik

Regulärer-Ausdrucks-Scan auf typische Verletzungsmuster:
- **K1**: `64π⁴`-Vorfaktor in ξ-Formeln
- **K2**: `r_τ = 8/3` Tau-Yukawa
- **K3**: `a_e = 4π/(f·k_geom)` Elektron-g-2-Basisformel
- **P7**: „Renormierungsgruppe" / „renormalization group" als FFGFT-Primitiv
- **P8**: „Fraktale Renormierung" / „fractal renormalization" als Eigenbegriff
- **P9**: `N_c = 3` direkt mit „Farbladungen" gleichgesetzt
- **P10, P12**: Numerische Sonderwerte (K=245, CHSH 5·10⁻⁴)

### Befund

**5 Dokumente bedurften Korrektur (von 147):**

| Dokument | Verletzung | Maßnahme |
|---|---|---|
| `086_T0_Dokumentenuebersicht_En_ch.tex` | P7: Bullet „Renormalization group as flow in parameter space" als FFGFT-Eigenschaft | → „Scale structure as flow on the recursion $\mathcal{R}$ in parameter space" |
| `091_Casimir_De_ch.tex` | P7: „RG-Aspekt: … besitzt die Theorie eine RG-Struktur ähnlich der QFT" | → „Skalenstruktur: … folgt in FFGFT aus der Rekursion $\mathcal{R}$ (Dok.~202/203) und ist nicht das Ergebnis eines Renormierungsverfahrens; sie ist in ihrer Wirkung der Renormierungsgruppe der QFT vergleichbar." |
| `091_Casimir_En_ch.tex` | P7: gleiche Stelle EN | → analog mit „comparable in effect to the renormalization group" |
| `124_Unit_Charge_En_ch.tex` | P8: „stabilized by fractal renormalization" | → „stabilized by fractal correction" |
| `038_Markov_En_ch.tex` | P8: „Fractal renormalization $\prod_{n=1}^{137}$..." | → „Fractal correction $\prod_{n=1}^{137}$..." |
| `160_T0_Lepton-Lebensdauer-Verh_De+En_ch.tex` | P9: 4 Stellen „$D = N_c = 3$: räumliche Dimensionen = Farbladungen/Farbwindungen" | → „$D = 3$ (SM-Korrespondenz: $N_c = 3$)" |

### Als OK eingestuft (141 von 147)

**Beispiele für vertretbare Verwendung von Renormierungs-Begriffen:**

- `019_T0_lagrndian`: Section-Header lautet bereits **„Renormierung (historische Darstellung)"** mit explizitem **Hinweis-Block** am Anfang: „Dieser Abschnitt verwendet die Sprache der QFT-Renormierung … als Beschreibungsmittel. In der vollständigen FFGFT-Formulierung (Dok.~202) ist traditionelle Renormierung nicht erforderlich". Damit ist die nachfolgende Subsection `\subsection{Renormierungsgruppen-Gleichungen}` durch den Section-Scope abgedeckt.

- `057_RelokativesZahlensystem`: `\subsection{Renormierungsgruppenfluss}` steht innerhalb von `\section{Physikalische Analogien und Anwendungen}` und beginnt mit „Eine bemerkenswerte Parallele besteht zwischen relationaler Komposition und dem Renormierungsgruppenfluss". Damit ist Analogie-Charakter explizit.

- `181_T0_Torus_Begruendung`: „AS sucht UV-Fixpunkt als Ergebnis des Renormierungsgruppen-Flusses. **In T0 gibt es keinen Renormierungsgruppen-Fluss** — $\xi$ ist eine geometrische Konstante." → Klare Kontrastierung.

- `202_FFGFT_Feldtheorie_Gesamt`: Hat explizite **„Anmerkung zur Begrifflichkeit Renormierungsgruppe"** mit Verweis, dass in FFGFT die Skalenstruktur aus der Rekursion $\mathcal{R}$ folgt.

- `205_FFGFT_Narrativ`: Beschreibt RG explizit als SM-Konzept und kontrastiert mit FFGFT.

- `242_Skalenleiter`: RG wird als „nächster Verwandter zu einer skalenübergreifenden Erklärung" eingeführt und kritisiert (RG läuft vertikal, FFGFT erklärt formative Übergänge).

**Spezialfall 018_T0_Anomale-g2_10/11/12 (kein K3-Verstoß):**

Die Basisformel für $a_e$ in 018 lautet bereits korrekt $a_e = (S_3/f)/k_\text{geom}$ mit $S_3 = 2\pi^2 = 19{,}739$ (gemäß K3). Die in der Differenzformel `Δa(μ−e) = 4π/f^(5/3)` erscheinende $4\pi$-Konstante ist nicht $a_e$, sondern die Myonen-Basisgröße $a_\mu \approx 4\pi/f^{5/3}$ (Myon und Tau verwenden weiterhin $4\pi$ gemäß Dok.~190 Gl.~190.5/190.6). $a_e$ ist in dieser Differenz vernachlässigbar klein und wird im rechten Ausdruck implizit weggelassen. Mathematisch korrekt.

### Status

| ✓ | Erledigt DE | Mai 2026 |
| ✓ | Erledigt EN | Mai 2026 |


### Kompilation der korrigierten Dokumente

Alle 5 Dokumente (10 Dateien: De+En) wurden im Kindle 6×9-Format (432×648 pt) erfolgreich kompiliert:

| Dokument | Seiten | Overfull-Boxen |
|---|---|---|
| 086_T0_Dokumentenuebersicht De/En | 8 / 8 | 0 / 0 |
| 091_Casimir De/En | 22 / 21 | 2 / 1 (alle < 4mm) |
| 124_Unit_Charge De/En | 5 / 5 | 0 / 0 |
| 038_Markov De/En | 8 / 7 | 0 / 0 |
| 160_T0_Lepton-Lebensdauer-Verh De/En | 12 / 11 | 0 / 0 |

**Zusätzliche Layout-Korrektur 091:** Die 11 longtables mit Spaltenbreiten `p{1cm} p{8cm} p{3cm}` bzw. `p{2cm} p{8cm} p{3cm}` (Gesamt 12-13 cm) überstiegen die Kindle-Textbreite von 12,04 cm. Reduziert auf `p{1cm} p{7cm} p{2.5cm}` bzw. `p{1.5cm} p{6.5cm} p{2.5cm}` mit `\raggedright\arraybackslash`. Verbleibende Überstände < 4 mm.

**Wrapper 124 De/En:** Neu erstellt (existierten zuvor nicht), Titel „Die Elektronen-Einheitsladung in T0: Geometrische Auflösung von Punkt-Singularitäten" / „The Electron Unit Charge in T0: Geometric Resolution of Point Singularities".

---

## Vollständige Kompilation aller Dokumente (Mai 2026)

Nach der Inhaltsprüfung der 147 weiteren Dokumente und der Anwendung der 6 erforderlichen P7/P8/P9-Korrekturen wurden alle Dokumente der Sammlung im Kindle 6×9 Format neu kompiliert.

### Ergebnis

| Metrik | Wert |
|---|---|
| Kompilierte PDFs total | **341** |
| Davon im Kindle 6×9 Format (432×648 pt) | **341** (100%) |
| Dokumentpaare (DE+EN) | 168 + 5 inline-Dokumente |
| Overfull-Boxen total | 350 (∅ 1,0 pro PDF) |
| Davon > 5 mm (15 pt) | 167 |
| Davon > 15 mm (45 pt) | wenige Spezialfälle in Math-Tabellen |

### Behobene Wrapper-Probleme

Bei der Kompilation der weiteren ~270 Dokumente traten verschiedene Wrapper-Inkonsistenzen auf, die alle behoben wurden:

| Anzahl | Problem | Lösung |
|---|---|---|
| 17 | Wrapper nutzten `T0_preamble_local_De/En` (xelatex+DejaVu) | Umgestellt auf `T0_preamble_standalone_De/En` (lualatex+Inter) |
| 8 | Wrapper hatten `\input{NAME_ch}` ohne `../ch/` Pfad | Pfad ergänzt |
| 6 | Wrapper hatten `\input{T0_preamble_standalone_De}` ohne `../pri-end/` Pfad | Pfad ergänzt |
| 2 | Wrapper hatten `\input{pri-end/...}` oder `\input{ch/...}` ohne `../` | `../` ergänzt |
| 1 | 161_T0_Ising_Machine_En: defekter Wrapper ohne `\documentclass` | Neu erstellt |
| 1 | 186_FFGFT_Photonik_Analyse: defekter `\title{}` (kein schließendes `}`) | Neu erstellt |
| 3 | Inline-Dokumente (Adaptive, Fruehe, 192) mit A4-Geometrie | Auf Kindle 6×9 umgestellt |
| 2 | 210 De/En: eigene `\geometry{paperwidth=210mm,…}` Block | Block entfernt (Preamble übernimmt) |
| 1 | 186: `\usepackage{geometry}\geometry{margin=2.5cm}` | Block entfernt |
| 2 | 172 De/En: `avipost` und `response` Umgebungen undefiniert | tcolorbox-Definitionen in Wrapper ergänzt |

### Behobene Preamble-Erweiterungen

Für PDF-Bookmark-Erzeugung (hyperref-Kompatibilität mit unicode-math-Symbolen) wurden ergänzt:

```latex
\pdfstringdefDisableCommands{
  % ... bestehende Einträge ...
  \def\varphi{phi}
  \def\mitvarphi{phi}
  \def\Phi{Phi}
  \def\mitPhi{Phi}
  \def\leftrightarrow{<->}
  \def\Leftrightarrow{<=>}
}
```

### Entfernte Duplikate

Folgende Wrapper waren Duplikate ohne eigene `_ch.tex`-Datei und wurden entfernt:
- `189_T0_TorusAbleitung_De/En.tex` (Duplikat von `189_TorusAbleitung_De/En.tex`)
- `160_T0_Lepton-Lebensdauer-Verhaeltnisse-1_De/En.tex` (Duplikat von `160_T0_Lepton-Lebensdauer-Verh_De/En.tex`)
- `167_T0_LiNbO3_xi_Geometrie_En.tex` (kein `_ch.tex` vorhanden, nur DE)
- `187_T0_FFGFT_Photonik_En.tex` (kein `_ch.tex` vorhanden, nur DE)
- `188_T0_Geometrie_Grundlagen_En.tex` (kein `_ch.tex` vorhanden, nur DE)
- `207_tex.tex` (Streufile)
- `T0_preamble_local_De/En.tex` (waren irrtümlich im Wrapper-Ordner)

### Status

| ✓ | Erledigt | Mai 2026 |

Alle 341 PDFs im einheitlichen Kindle 6×9 Format verfügbar.


---

## Übersetzungen unvollständiger Sprachpaare (Mai 2026)

Nach der vollständigen Kompilation wurde geprüft, welche Dokumente nur in einer Sprache vorlagen. Für diese wurde eine vollständige Übersetzung erstellt.

### Identifizierte Lücken (initial)

| Doc | Status vorher |
|---|---|
| 187_T0_FFGFT_Photonik | nur DE (32 KB, 755 Zeilen) |
| 188_T0_Geometrie_Grundlagen | nur DE (23 KB, 558 Zeilen) |

(167_T0_LiNbO3 hat bereits beide Sprachen unter verschiedenen Namen: `167_..._Geometrie_De` und `167_..._Geometry_En`.)

### Erstellte Übersetzungen

**188_T0_Geometrie_Grundlagen_En:** „Geometric Foundations of FFGFT — From the Phase Condition to Circle, Polygon, Spiral, and Nature's Preferred Ratios"

Vollständige Übersetzung des deutschen Dokuments. Inhalt: universelle Phasenbedingung, reguläre Polygone, Z3-Symmetrie, n=6 hexagonale Packung, Kreis als Grenzfall, logarithmische Spirale, Goldener Schnitt $\phi$ als optimales inkommensurables Verhältnis, Fibonacci-Folge, abgeleitete FFGFT-Formeln ($\alpha = \phi^{-1}$, $1/n^2$-Spektrum, Leptonmassen-Leiter, $\alpha_\text{EM}$), Block-Copolymer DSA unter der Wellenlängengrenze.

- 21,7 KB, 557 Zeilen
- PDF: 15 Seiten, Kindle 6×9, 0 Overfull-Boxen

**187_T0_FFGFT_Photonik_En:** „FFGFT Analytics: Mathematical Foundations — Fractal Feedback and Matrix Translation in the 4D Phase Torus"

Vollständige Übersetzung des deutschen Dokuments. Inhalt: fundamentale Frequenz $\xi = 7500/t_P$, 4D-Phasen-Torus (Abgrenzung vom 3D-Torus), fraktale Rückkopplung und Einrast-Mechanismus, Matrix-Translation, 4D-Torus-Faltung, TFLN-Photonik als Hardware-Transduktion, B-Meson-Anomalien (LHCb 4,0σ), sub-plancksche Cut-off-Skalen (OLQEM, EFT), testbare Vorhersagen.

- ~32 KB, ~750 Zeilen
- PDF: 18 Seiten, Kindle 6×9, 0 Overfull-Boxen

### Status

| ✓ | Erledigt | Mai 2026 |

**Endstand:** Alle 173 Dokumente verfügbar in DE+EN (außer 192_Adaptive, Adaptive, Fruehe — sind inline Dokumente ohne DE/EN-Trennung).


---

## Fix für 192_T0_Algebraische_Kompositionsgrenzen (Mai 2026)

Bei der Analyse von Johann's älteren PDF-Dateien (pdf.zip) wurde entdeckt, dass das Dokument 192_T0_Algebraische_Kompositionsgrenzen einen Build-Fehler hatte:

**Problem:**
Die ch.tex-Dateien `192_T0_Algebraische_Kompositionsgrenzen_De_ch.tex` und `192_T0_Algebraische_Kompositionsgrenzen_En_ch.tex` waren in der Sammlung vorhanden, hatten aber keine entsprechenden Wrapper. Stattdessen referenzierte der Wrapper `192_Adaptive_Hybridarchitektur_Pascher.tex` einen völlig anderen Inhalt (Adaptive Hybridarchitektur — ein eigenständiges inline-Dokument).

**Lösung:**
Zwei neue Wrapper erstellt:

- `192_T0_Algebraische_Kompositionsgrenzen_De.tex`
  - Titel: „Algebraische Kompositionsgrenzen in FFGFT"
  - PDF: 9 Seiten, Kindle 6×9, 0 Overfull-Boxen

- `192_T0_Algebraische_Kompositionsgrenzen_En.tex`
  - Titel: „Algebraic Composition Limits in FFGFT"
  - PDF: 8 Seiten, Kindle 6×9, 0 Overfull-Boxen

**Inhalt des Dokuments:**
Behandelt Kompositionsgrenzen zwischen algebraischen Strukturräumen in FFGFT. Zentrale These: Wenn FFGFT-Terme ($m_\ell = r_\ell \cdot \xi^{p_\ell} \cdot v$) in Formeln aus fremden algebraischen Kontexten (z. B. Koide-Relation, SM-Streuamplituden) eingesetzt werden, entstehen strukturfremde Kreuzterme — ein Kategorienfehler, kein numerisches Problem.

Das Dokument `192_Adaptive_Hybridarchitektur_Pascher.tex` bleibt als eigenständiges inline-Dokument bestehen (Adaptive Hybridarchitektur für CIM-Systeme).

### Status

| ✓ | Erledigt | Mai 2026 |


---

## Eigenständige PDFs in Sammlung integriert (Mai 2026)

Aus den älteren PDFs (pdf.zip vom 18.5.2026) wurden eigenständige Dokumente identifiziert,
die nur als PDF vorlagen (keine ch.tex-Quelldateien). Diese wurden mit alternativem
Nummernpräfix (Suffix `a`) in die Sammlung integriert.

### Strategie: Option A — PDF einbetten

Da die ch.tex-Quellen für diese Dokumente fehlen und eine Rekonstruktion aus dem PDF
(Gleichungen, Tabellen, Bilder) nicht zuverlässig möglich ist, werden die Original-PDFs
unverändert in `pdf_originals/` abgelegt und über minimale Wrapper mittels
`\includepdf` eingebettet. Das Original-Layout bleibt EXAKT erhalten und wird auf
Kindle 6×9 (432×648 pt) skaliert.

### Integrierte Dokumente

| Wrapper | Inhalt | Original-Datum | Seiten | Original-Größe |
|---|---|---|---|---|
| `060a_Musikalische_Spirale_137_De/En.tex` | „Die Musikalische Spirale und die 137" — Resonanzpunkt $(4/3)^{137} \approx 257$ als Quelle der Feinstrukturkonstante | 17./20. Feb 2026 | 8/7 | 594×792 |
| `144a_Asymmetrie-Master_De/En.tex` | „FFGFT: Asymmetrie-Analyse Teil 1 und 2" (vollständig, im Gegensatz zu `144_Asymmetrie-teil2` das nur Teil 2 enthält) | 23. Feb 2026 | 21/19 | 432×648 (bereits Kindle) |
| `170a_Analog_Gehoer_De/En.tex` | „Analog-Gehör" — eigenständiges Akustik-Dokument | 4. März 2026 | 16/16 | A4 |
| `186a_FFGFT_Photonik_Hardware_De/En.tex` | „FFGFT and Photonic Hardware" — eigenständiges Hardware-Dokument (im Gegensatz zu `186_FFGFT_Photonik_Analyse` „Mathematical Foundations") | 4. Mai 2026 | 14/14 | A4 |
| `006a_Teilchenmassen_2025_De/En.tex` | „T0-Modell: Vollständige parameterfreie Teilchenmassen-Berechnung" — historische Vorläufer-Version | **29. Nov 2025** | 15/14 | A4 |

### Verzeichnisstruktur

```
pdf/                        — kompilierte PDFs (jetzt 356, alle Kindle 6×9)
pdf_originals/              — Original-PDFs für die 10 standalone Wrapper (NEU)
ch/                         — ch.tex Quelldateien (unverändert, 348 Stück)
wrapper/                    — Wrapper-Dateien (356 jetzt: 346 Standard + 10 standalone)
pri-end/                    — Preamble (unverändert)
```

### Bücher

Die folgenden PDFs sind eigenständige Buchprojekte und werden NICHT in die Sammlung
aufgenommen (Quelldateien existieren beim Autor lokal in separaten Verzeichnissen):
- `Von_Alpha1_zur_vollstaendigen_Physik_De/En.pdf` (105 Seiten)
- `Xi_Narrative_Master-ebook_De/En.pdf` (354/325 Seiten)
- `FFGFT_Narrative_Master_De/En.pdf` (251/254 Seiten)

### Nicht enthalten

- `T0_170b_Gehoer_De/En.pdf` — vom Autor lokal gelöscht

### Status

| ✓ | Erledigt | Mai 2026 |

**Endstand der Sammlung:** 356 PDFs (vorher: 346 + 10 eigenständige)


---

## Bereinigung der Datei-Präfixe (Mai 2026)

User-Anforderung: Jedes Dokument muss mit Zahl-Präfix beginnen, und kein Präfix darf doppelt vorkommen (außer DE/EN-Paaren).

### Behobene Probleme

| Alter Name | Neuer Name | Grund |
|---|---|---|
| `dok206_dreieck_matrix_reduktion_De/En` | `206_dreieck_matrix_reduktion_De/En` | "dok"-Präfix entfernt, jetzt rein numerisch |
| `dok207_bewusstsein_bruecken_De/En` | `207_bewusstsein_bruecken_De/En` | "dok"-Präfix entfernt |
| `Adaptive_Hybridarchitektur_Pascher` | `208_Adaptive_Hybridarchitektur_Pascher` | Zahl-Präfix hinzugefügt |
| `Fruehe_digitale_Spuren_Pascher` | `209_Fruehe_digitale_Spuren_Pascher` | Zahl-Präfix hinzugefügt |
| `192_Adaptive_Hybridarchitektur_Pascher` | **gelöscht** | Duplikat von `Adaptive_Hybridarchitektur_Pascher` (gleicher Hash) — war versehentlich von mir mit 192-Präfix kopiert worden |
| `1_T0_Introduction_De/En` | `001b_T0_Introduction_De/En` | Einstellig → 3-stellig, Suffix `b` zur Unterscheidung von `001_T0_Book_Abstract` und `001a_T0_Book_Abstract` |
| `023a_Bell-video_De/En` | `023b_Bell-video_De/En` | `023a` war doppelt belegt (Bell-Teil2 + Bell-video). Bell-Teil2 behält `023a`, Bell-video bekommt `023b` |
| `060a_Musical_Spiral_137_De.pdf` (altes Testfile) | **gelöscht** | Alter Testbuild aus früherer Session, durch `060a_Musikalische_Spirale_137_De` ersetzt |

### Endkontrolle

- ✓ Alle 355 Wrapper beginnen mit numerischem Präfix
- ✓ Kein Wrapper mit "dok"-Präfix mehr
- ✓ Keine wirklichen Duplikate (alle Präfix-Doppelungen sind DE/EN-Paare des gleichen Dokuments)
- ✓ Alle Wrapper-Referenzen auf ch.tex-Dateien aktualisiert
- ✓ Alle 8 betroffenen Dokumente neu kompiliert

### Endstand

| Komponente | Anzahl |
|---|---|
| Wrappers | 355 |
| Kompilierte PDFs | 355 (alle Kindle 6×9) |
| ch.tex Quelldateien | 348 |


---

## Neue Arbeiten (Mai 2026) — Session „Natürliche Einheiten & Informationseinheit"

### N261 — Dok. 261: Statische Geometrie und SI-Projektion
| Feld | Inhalt |
|------|--------|
| Dokument | Dok. 261 — „Statische Geometrie und SI-Projektion: Warum natürliche Einheiten keine fraktalen Korrekturen brauchen" (EN: „Static Geometry and the SI Projection: Why Natural Units Require No Fractal Corrections") |
| Status | **erledigt** (DE+EN) |
| Eingetragen | Mai 2026 |
| Erledigt DE | ✓ Mai 2026 |
| Erledigt EN | ✓ Mai 2026 |
| Präfix-Hinweis | 261 gewählt (260 existiert nur als PDF) |
| Format | Kindle 6×9 (432×648 pt); DE 11 S., EN 11 S. |

**Inhalt (9 Abschnitte):** Einordnung; Rahmenabschnitt „Kompaktifizierte Zeit: statisch und vollständig — der Pfeil macht dynamisch"; drei Umrechnungstabellen (SI-fixierte Konstanten / Größenumrechnung ℏ=c=k_B=1 / dimensionslose Inputs → ξ); statische Korrekturfreiheit; dynamische Realität von c, ℏ, ε₀ im Zeitfluss; Konsequenz G und α als dynamische Kopplungen; Demarkation aus Lagrange-Sicht.

**Kernthese:** Solange in natürlichen Einheiten und reinen Verhältnissen gerechnet wird, ist die Beschreibung statisch und korrekturfrei (Schicht 1, kompaktes T⁴, eingefrorene Rekursion). c, ℏ, ε₀ werden erst bei Dekompaktifizierung der intrinsischen Zeit-Wicklung T̃ in die Pfeilzeit t real (Schicht 2, Einbettungspreis). G und α sind keine statischen Grundkonstanten, sondern dynamische Kopplungen.

**Quellengrundlage (verifiziert):** 011 (α=ξ·(E₀)²), 012/127/133 (G, K_frak), 013/014 (SI-Projektion, S_T0), 041 (Weinberg α_W=√ξ, θ₁₃), 116 (Koide, Leiter), 078 (zwei Zeiten T̃ vs t), 134 (c=L/T), 181 (ℝ³×S¹, r₄=L₀), 185 (Einbettungspreis), 230 (T⁴=T³×S¹, Zeit-Wicklung), 241 (Schicht 1/2, eingefrorene Rekursion), 019/049/067/095/180 (Lagrange-Begründung).

**Konsistenzprüfung:** P8-konform („fraktale Korrektur", nicht „Renormierung"); K2-konform (r_τ=25/9, Tabelle 3); P6/Nichtabschluss-konform (Koide Q=2/3 als Folge der Exponenten, nicht nachträglich gefittet); Korrekturen als abgeleitete Projektionsfaktoren dargestellt (Dok 133/258/193).

**Offen / nachzutragen:** compile_all.py-Eintrag (Muster `^261_` greift, sobald ch-Dateien im Verzeichnis liegen); optionale Querverweise aus 013/078/134/185/230/241 auf 261 (Einzeiler vorbereitet, noch nicht in die Zieldokumente eingesetzt).

---

### N013-INFO — Dok. 013: Abschnitt „Statische und dynamische Informationseinheit"

> ⚠️ **Nachträglich präzisiert (27. Mai 2026):** Dieser Eintrag stellte den 013-Einschub ursprünglich als eigenständige Erweiterung dar. Tatsächlich überschneidet er sich inhaltlich erheblich mit Dok.~**255** („Information als topologisch eingefrorene kinetische Energie") und Dok.~**257** („Skalenabhängige Informationseinheiten als Phasenübergänge auf T⁴"). Diese beiden waren zum Zeitpunkt des Einschubs übersehen worden. Variante C wurde gewählt (013-Einschub bleibt für SI-Reform-Leser; 255/257 sind die ausführlichen Träger des Themas). Siehe nachstehenden Eintrag „N255-257-Verschaltung".
| Feld | Inhalt |
|------|--------|
| Betroffene Dok. | 013 (DE+EN), neuer Unterabschnitt nach dem ξ_FFGFT/ξ_UIFT-Vergleich (P13) |
| Status | **erledigt** (DE+EN) |
| Eingetragen | Mai 2026 |
| Erledigt DE | ✓ Mai 2026 |
| Erledigt EN | ✓ Mai 2026 |

**Anlass:** Wiederaufnahme der Frage „Wie viel Energie entspricht der kleinsten Informationseinheit?". Frühere Aussage: keine universelle Einheit, längenabhängig (Dok 184: E_N = ℏc/L_N; Landauer k_B T ln2).

**Inhalt:** Trennung von *Information als Energie* (Schicht 2, dynamische Projektion, skalenabhängig — k_B T bzw. ℏc/L) und *Information als Zählung* (Schicht 1, statisch: die dimensionslose, ganzzahlige Windungszahl auf dem kompakten Torus). Der Vopson-Faktor ξ_FFGFT/ξ_UIFT ≈ 414.684 wird als Projektionsverhältnis zwischen einer Schicht-2- und einer Schicht-1-Informationsgröße gedeutet.

**Quellengrundlage:** 181 (Windungszahlen), 184 (Energiehierarchie E_N=ℏc/L_N, Landauer-Grenze, „ξ-Geometrie bestimmt Dynamik, nicht Zustandsraumgröße"), 185 (Einbettungspreis), 261 (statisch/dynamische Demarkation).

**Querbezug (keine Dopplung):** Dok 247 („Information, Zustand und Prozess") behandelt bereits Zustand vs. Prozess (Speicherung energieneutral, Landauer nur für Löschung). Der 013-Einschub wendet diese Logik speziell auf den Vopson-Vergleich an und ergänzt die Schicht-Lesart; er ersetzt 247 nicht.

**Layout:** align-Block in der „Energie pro Bit"-Box auf gestapelte Darstellung umgestellt (Formel und Klammer-Erläuterung getrennt), damit kein Überlauf in der Kindle-6×9-Box entsteht.

---

### Übersichtstabelle — Nachtrag

| ID | Status | Bemerkung |
|----|--------|-----------|
| N261 | ✓ Mai 2026 | neues Dokument (9 Abschnitte, DE+EN, Kindle 6×9) |
| N013-INFO | ✓ Mai 2026 | Erweiterung Dok 013 (statische/dynamische Informationseinheit) |

---

## K2-Nachtrag — vollständige Einarbeitung (27. Mai 2026)

**Anlass:** Dok. 190 meldete im K2-Statusabschnitt (Nachtrag 26. Mai) verbliebene 8/3-Reste in Dok. 016, 046 und 116. Eine eigene Vollprüfung bestätigte dies und fand **zusätzlich** übersehene Reste in **046 DE** (abgeleitete Werte), die Dok. 190 nicht nennt.

**Soll-Stand (Dok. 190 maßgeblich):** r_τ = 25/9 · m_τ = 1783,4 MeV · Abw. +0,37 % · ξ_ντ = 400/81 ·10⁻⁸ · E_ντ = 18,0 meV · ν_τ-Zeilen 25/9.

### Befund und Durchführung

| Datei | Stelle | Vorher | Nachher | Status |
|-------|--------|--------|---------|--------|
| 046 DE | Ergebnistabelle ν_τ (Verträglichkeit) | 18,8 meV | 18,0 meV | ✓ |
| 046 DE | Methodenäquivalenz, Tau-Zeile r_i | 2,768 | 2,778 (=25/9) | ✓ |
| 046 DE | Methodenäquivalenz, ν_τ-Zeile | 18,8·10⁻⁶ / 2,768 | 18,0·10⁻⁶ / 2,778 | ✓ |
| 046 DE | Falsifikationstab. m_{ν_τ} | 18,8 meV | 18,0 meV | ✓ |
| 016 EN | Massentab., Tau-Zeile | 8/3 · 1712,1 · 3,64 | 25/9 · 1783,4 · 0,37 | ✓ |
| 016 EN | r-Parameter-Liste | …, 8/3, … | …, 25/9, … | ✓ |
| 046 EN | ν_τ-Parameterzeile (Tab. 1) | 8/3 & 8/3 | 25/9 & 25/9 | ✓ |
| 046 EN | ξ_ντ-Rechnung | 8/3 → 128/27 | 25/9 → 400/81 | ✓ |
| 046 EN | E_ντ (3 Stellen) | 18,8 meV | 18,0 meV | ✓ |
| 046 EN | Methodenäquivalenz Tau + ν_τ | 2,768 | 2,778 | ✓ |
| 046 EN | ν_τ-Zeile (Tab. 2) | 8/3 & 8/3 | 25/9 & 25/9 | ✓ |
| 116 EN | Leptonparameter-Tab., Tau-Zeile | 8/3 | 25/9 | ✓ |

**Hinweis zur ursprünglichen K2-Eintragung:** Diese nannte nur Dok. 116; die K2-Erweiterung ergänzte 046. Tatsächlich betroffen waren **016, 046 (DE+EN) und 116 EN**. DE von 016/116 war bereits korrekt; 046 DE hatte nur in den *abgeleiteten* Tabellen Reste (Hauptrechnung war korrekt).

### Richtungsentscheidung Tau-Neutrino

Die frühere Festlegung „ν_τ bleibt 8/3" (K2-Erweiterung) ist **revidiert**. Dok. 190 (26. Mai) und die korrigierte 046-DE-Rechnung setzen ν_τ auf 25/9 (ξ_ντ = 400/81, E = 18,0 meV). Maßgeblich ist Dok. 190 als jüngster Stand.

### Verifikation

- Korpusweite Restsuche (8/3, 128/27, 1712, 18.8, 2.768, 3.64) in allen vier Dateien: **0 Treffer**.
- Tabellen-Spaltenzahl der geänderten Zeilen unverändert (keine zerbrochenen Tabellen); keine fehlerhaften Escapes.
- Neu kompiliert (Kindle 6×9, 432×648 pt): 016 EN (13 S.), 046 DE (20 S.), 046 EN (17 S.), 116 EN (9 S.) — fehlerfrei.

### Offen / Hinweise

- **Versionslage:** Diese EN-Korrekturen liegen **nach** dem v1.1.1-Release (23. Mai, DOI 20355305, „No existing derivations changed"). Das Zenodo-Archiv v1.1.1 ist in diesen Werten **nicht** deckungsgleich mit dem korrigierten Repo-Stand. Bei nächstem Release/Point-Release nachziehen.
- **Dok. 190** im K2-Statusabschnitt ergänzen: betroffen war auch 046 DE (abgeleitete 18,8-Werte); EN-Seite (016/046/116) erst am 27. Mai nachgezogen.

### Status

| ✓ | Erledigt DE | 27. Mai 2026 |
| ✓ | Erledigt EN | 27. Mai 2026 |

---

### Übersichtstabelle — Nachtrag (Fortsetzung)

| ID | Status | Bemerkung |
|----|--------|-----------|
| K2-Nachtrag | ✓ 27. Mai 2026 | vollständige Einarbeitung: 016 EN, 046 DE+EN, 116 EN; ν_τ → 25/9 |

---

## N255-257-Verschaltung — Korpus-Integration der Informations-Dokumente (27. Mai 2026)

**Anlass:** Bei der Arbeit am 013-Einschub (siehe N013-INFO) wurde nachträglich erkannt, dass Dok. 255 und 257 das Thema „Energie pro Bit / Informationseinheit / Statisch vs. dynamisch" bereits ausführlich behandeln — 255 leitet Landauer und Vopson aus T⁴-Geometrie ab, 257 präzisiert mit der Drei-Ebenen-Hierarchie (topologisch / geometrisch / thermodynamisch). Entscheidung: **Variante C** — der 013-Einschub bleibt für SI-Reform-Leser; 255 und 257 werden mit den jüngeren Dokumenten (184, 261, 013) sichtbar verschaltet, ohne ihren Inhalt zu ändern.

### Eingearbeitete Querverweise

| Datei | Ergänzung |
|-------|-----------|
| 255 DE+EN | Abschnitt „Verschaltung im Korpus" / „Integration in the corpus" nach der Methodologie-Notiz. Querverweise: Dok. 257 (Drei-Ebenen-Hierarchie, Spezialfall-Einordnung); Dok. 184 (Energiehierarchie E_N = ħc/L_N); Dok. 261 (Schicht 1 = topologisch eingefroren, Schicht 2 = freie kinetische Seite mit Einbettungspreis c, ħ, ε₀). |
| 257 DE+EN | Abschnitt „Verschaltung im Korpus" / „Integration in the corpus" nach der Methodologie-Notiz. Querverweise: Dok. 261 (Drei-Ebenen-Hierarchie als feldtheoretische Ausarbeitung der Schicht-1/Schicht-2-Demarkation); Dok. 184 (E_bit(L) = ħc/L identisch mit E_N = ħc/L_N); Dok. 013 (Vopson-Faktor 414 684 als Projektionsverhältnis Schicht-1 ↔ Schicht-2). |

### Was nicht geändert wurde

Der mathematische und inhaltliche Kern beider Dokumente bleibt unverändert. Die Ableitung von Landauer/Vopson aus T⁴ (Dok. 255), die Drei-Ebenen-Hierarchie (Dok. 257) und die Skalenresonanz-Hypothese (Lebensskala, Dok. 257) sind nicht angetastet. Nur die Verschaltung mit dem aktuellen Korpus-Stand wurde sichtbar gemacht.

### Verifikation

- Querverweise im PDF-Text geprüft: Dok. 257/261/184 (in 255 DE+EN), Dok. 261/184/013 + Vopson-Faktor 414 684 (in 257 DE+EN).
- Vier PDFs neu kompiliert (Kindle 6×9): 255 DE (11 S.), 255 EN (10 S.), 257 DE (9 S.), 257 EN (8 S.).

### Status

| ✓ | Erledigt DE | 27. Mai 2026 |
| ✓ | Erledigt EN | 27. Mai 2026 |

---

### Übersichtstabelle — Nachtrag (Fortsetzung)

| ID | Status | Bemerkung |
|----|--------|-----------|
| N255-257-Verschaltung | ✓ 27. Mai 2026 | Querverweise auf Dok. 261/184/013 (255); 261/184/013 inkl. Vopson-Faktor (257); inhaltlich nichts geändert |

---

## HW147 — Dok. 147 §8: Hardware-Validierung auf echte Messung korrigiert (28. Mai 2026)

**Anlass:** Eigene Hardware-Läufe auf IBM Quantum (28. Mai 2026, ibm_kingston / ibm_marrakesh, beide Heron r2, 156 Qubit) zur Überprüfung der in Dok. 147 §8 berichteten Zahlen. Abgleich mit dem Juni-2025-Hardware-Validierungsreport ergab, dass mehrere §8-Behauptungen entweder durch die neuen Daten widerlegt oder in den verfügbaren Aufzeichnungen nicht belegt sind.

### Korrigierte Behauptungen (DE+EN parallel)

| Stelle | Vorher (unbelegt/widerlegt) | Nachher (echte Messung) |
|--------|------------------------------|--------------------------|
| Bell-Treue-Tabelle | 3 Läufe, „Treue 1,000", Varianz 0,000248 | 50 Läufe, Fidelität 98,76 %, Varianz 1,249·10⁻⁴ |
| „40× deterministischer als QM" | behauptet | widerlegt: Varianz-Verhältnis 1,02, χ²-p = 0,86 |
| CHSH 73-Qubit | S = 2,8275 „aus 2025-Daten" | nicht belegt → ersetzt durch S = 2,7396 (gemessen) |
| CHSH 127-Qubit | S = 2,8278, „nahezu perfekte ξ-Übereinstimmung" | nicht belegt → ersetzt durch echte Messung |
| ξ-Fit-Tabellen (73/127) | ξ_fit angepasst an unbelegte CHSH-Werte | entfernt (Datengrundlage fehlt) |
| Monte-Carlo „kompatibel mit IBM-Beobachtung" | stützte sich auf unbelegte 2,8275 | entfernt |
| Abstract „CHSH ~10⁻³ in 73-Qubit testbar" | überzogen | ehrlich: ξ ~10⁻⁵, unter NISQ-Rauschen |
| „Experimentell validiert: CHSH = 2,827888" | überzogen | „Hardware-getestet: S = 2,74, Bell-Verletzung" |
| Schluss-Zusammenfassung | wiederholte alle obigen Werte | echte Werte + ξ-Messbarkeitsbefund |

### Neue, belegte Datenlage in §8

- **Bell-Wiederholbarkeit (50 Läufe):** Fidelität 98,76 %; Varianz mit Shot-Noise verträglich (1,02; p = 0,86). Die deterministische Varianzreduktion besteht nicht.
- **CHSH (gemessen):** S = 2,7396 ± 0,0071 (Kingston, 15 Messungen), 96,9 % der Tsirelson-Schranke, 105 σ über klassisch. Klare Bell-Verletzung.
- **Cross-Platform:** Marrakesh S = 2,7016; Geräte-zu-Geräte-Differenz 0,038 (Welch t = 2,46, p = 0,028). Diese Variation übersteigt den ξ-Effekt um ~1400× → ξ mit NISQ-Hardware prinzipiell nicht auflösbar (empirisch, nicht geschätzt).
- Zwei `important`-Korrektur-Boxen dokumentieren die Änderungen im Dokument selbst.

### Methodische Befunde

- Die unbelegten CHSH-Werte 2,8275/2,8278 stammten aus reinen Fitting-Skripten (bell_73qubit_fit.py, bell_2025_sherbrooke_fit.py), die diese Werte als hardcoded Input nahmen; keine Roh-Aufzeichnungen (Job-IDs, Counts) existieren dafür im Archiv. Der dokumentierte 2025-Lauf betraf ausschließlich Bell-Zustands-Generierung.
- Im ersten Auswertungslauf des CHSH-Skripts (Stufe 2) wurde eine zu den Winkeln nicht passende Vorzeichenkombination verwendet (Ergebnis fälschlich S ≈ 0); aus denselben Rohdaten korrekt rekombiniert ergibt sich S = 2,7396, ohne erneuten Hardware-Lauf.

### Verifikation

- begin/end-Umgebungen balanciert (DE+EN), keine zerbrochenen Tabellen, keine hängenden \ref auf gelöschte Tabellen-Labels (tab:chsh_73, tab:chsh_127, tab:system_comparison entfernt).
- Reports erstellt: Bell_Wiederholbarkeit_Report_2026-05-28.md (DE) + _En.md, mit vollständigen Job-IDs.
- Rohdaten archiviert: bell_repeatability_2026.csv (50 Zeilen), chsh_stage2_2026.csv, chsh_stage2_marrakesh_2026.csv.

### Folgedokumente — abgeschlossen (28. Mai 2026)

Pro Dokument geprüft, ob die unbelegten Werte eigene Behauptung sind (korrigiert) oder legitime Theorie/Fehltreffer (unverändert):

- **Korrigiert (DE+EN), unbelegte Hardware-Werte ersetzt/markiert:**
  - Dok. 148 (scramblons): IBM-Geräte-Zeilen (Brisbane/Sherbrooke) in der Cross-Platform-Tabelle als „Supraleitend (Vorhersage)" relabelt; keyresult-Übereinstimmungsbehauptung durch Verweis auf echte Messung (S=2,74) ersetzt.
  - Dok. 022 (QFT-ML-Addendum): „2025-Daten S≈2,8275"-Fit-Grundlage durch Korrektur-Box ersetzt; CHSH-Werte als theoretisch markiert; ξ-Fit als gegenstandslos gekennzeichnet (Formel als Skalenstruktur erhalten).
  - Dok. 035 (QM): Testbarkeits-Vorhersage als theoretisch markiert; Korrektur-Box vor dem „2025-Daten identifiziert"-Arbeitsnotiz-Abschnitt.
  - Dok. 202 (Feldtheorie-Gesamt): Verweis auf Dok. 147 von „ΔCHSH~10⁻³" auf „theoretischer ξ-Effekt ~10⁻⁵, unter NISQ-Rauschen; Hardware S=2,74" aktualisiert (zwei Stellen).
- **Unverändert — legitime theoretische Vorhersage (kein Hardware-Claim):**
  - Dok. 023, 023a (Bell): CHSH 2,828→2,827 ist die theoretische ξ-Dämpfung; 73-Qubit-Lie-Detector als *zukünftiger* Test zitiert (sciencedaily2025) — korrekt.
  - Dok. 175 (Qubit-Zustandsräume): „2√2→2,8275" ist theoretische ξ-Dämpfung, kein Messwert.
- **Unverändert — Fehltreffer (kein Bezug zu Bell/Fidelität):**
  - Dok. 041: „0,974" ist das CKM-Matrixelement |V_ud|.
  - Dok. 155: „40-fach" bezieht sich auf DNA-Datenkompression.

### PDF-Ausgabe

Alle vier korrigierten Dokumente in DE+EN als PDF gebaut (XeLaTeX, echte Standalone-Präambel, 6×9). Wrapper unverändert (nur ch/-Kapitelinhalt geändert, Struktur gleich). Sandbox-Caveat: Math = Latin Modern (statt Libertinus), keine deutsche Silbentrennung wie unter LuaLaTeX.

### Offen / Hinweise

- Die Korrektur-Boxen in 022/035 verwenden `tcolorbox` (rot) — beim finalen LuaLaTeX-Build prüfen, ob Stil zur Hausfarbe passt.
- **Budget-Hinweis:** Die Hardware-Läufe verbrauchten 8 von 10 min des Open-Plan-Zyklus (28-Tage-Fenster).

### Status

| ✓ | Erledigt DE | 28. Mai 2026 |
| ✓ | Erledigt EN | 28. Mai 2026 |
| ⏳ | Folgedokumente (148, 035, 022, 023, 023a, 202, 175, 041, 155) | offen |

---

### Übersichtstabelle — Nachtrag (Fortsetzung)

| ID | Status | Bemerkung |
|----|--------|-----------|
| HW147 | ✓ 28. Mai 2026 | Dok. 147 §8 auf echte Messung korrigiert (S = 2,74); „40×" widerlegt |
| HW147-Folge | ✓ 28. Mai 2026 | Folgedok. 148/022/035/202 (DE+EN) korrigiert + PDF; 023/023a/175 legitime Vorhersage; 041/155 Fehltreffer |
