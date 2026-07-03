# Release Notes — v1.1.7 (Juli 2026)

**DOI:** _wird beim Zenodo-Upload vergeben_ (löst v1.1.6 ab · [10.5281/zenodo.21061423](https://doi.org/10.5281/zenodo.21061423))

Laufende Korrekturen: **[2/PDFs/190_T0_Korrekturen_De.pdf](2/PDFs/190_T0_Korrekturen_De.pdf)**
Änderungsprotokoll: **[000_FFGFT_Changelog_De.md](000_FFGFT_Changelog_De.md)**

---

**FFGFT — Fraktale Feldgeometrische Fundamentaltheorie** zeigt:
Alle Konstanten des Standardmodells folgen aus einem einzigen
dimensionslosen Parameter **ξ = 4/30000** auf einem kompakten
4D-Torus T⁴. Die Grundrelation ist **T̃ · m = 1** — intrinsische Zeit
und Masse sind invers gekoppelt.

**Autor:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Was ist neu in v1.1.7

v1.1.7 ergänzt eine ausführliche, ehrlich deklarierte Prüfung des
**Leptonsektors** (Dok. 292) und schließt die Behandlung der **Koide-Phase
θ = 2/9** ab (Dok. 291). Der Fokus ist FFGFT-intern: wie weit die Geometrie
die Leptonmassen festlegt, wo die Präzision sitzt und wie die Koide-Phase
als Zirkulant-Winkel charakterisiert ist.

### Leptonsektor — zwei Schichten, ein Referenzpunkt, eine scharfe Vorhersage

[Dok. 292](2/PDFs/292_Leptonen_Empirie_Check_De.pdf) prüft den Leptonsektor
von der Datenseite (P35/P40) und trennt sauber zwei Schichten, die dasselbe
ξ teilen, aber nicht vermischt werden dürfen:

- der **Zirkulant** (Z₃-symmetrischer Massenoperator) trägt die *Präzision*
  — er trifft μ/e auf wenige Millionstel;
- die gröbere **ξ-Leiter** trägt die *Größenordnung* — dieselben
  Verhältnisse auf etwa ein Prozent.

Unter **P42** ist das μ/e-Verhältnis ein *deklarierter Referenzpunkt*
(analog P39): einmal als Anker gesetzt, ist es verbraucht und keine
Prüfgröße mehr. Die eine unausweichliche Prüfung, die bleibt, ist die
Tau-Masse: FFGFT sagt **m_τ = 1776,97 MeV** voraus, worüber die
Belle-II-Präzision ohne Ausweichmöglichkeit entscheidet.

### α ist keine Kalibrierung

Die Feinstrukturkonstante läuft über **zwei unabhängige Wege** zur
charakteristischen Energie E₀ — empirisch (√(m_e·m_μ)) und rein geometrisch
(aus ξ und m_μ allein, ohne m_e zu benutzen). Beide treffen sich auf
~8·10⁻⁵: Überbestimmung, kein Fit. Der Rest ist ein modusunabhängiger
Zeuge, dass die gemessene „angezogene" Polmasse nicht ganz die geometrisch
fundamentale Größe ist — eine dünne Verkleidungsschicht zwischen der nackten
Geometrie und dem, was das Experiment sieht.

### Ein generationslineares Korrekturgesetz

Die ξ-Leiter-Reste sind keine drei unabhängigen Zahlen: die Exponenten sind
multiplikativ konsistent (p₃ = p₁ + p₂ exakt) und die effektiven Faktoren
skalieren 1 : 2 : 3 mit der Generationszahl, N_g ≈ g·N₀. Deshalb kann eine
*konstante* Korrektur die Leiter nie schließen. Die Grundeinheit N₀ ≈ 38,6
ist noch nicht hergeleitet (100/φ² = 38,20 ist ein zulässiger Kandidat,
innerhalb der N₀-Toleranz, kein Beweis).

### Die Koide-Phase θ = 2/9 — die Zirkulant-Phase

θ = 2/9 ist **kein freier Parameter**: es ist die Phase des Z₃-Zirkulanten,
der Wert, den die Diagonalisierung ausgibt — gefunden, nicht gesucht (aus der
Hilbertraum-Übersetzung, Dok. 230/231/232 → 282).
[Dok. 291](2/PDFs/291_Dynamischer_Ort_Theta_2_9_De.pdf) charakterisiert ihn
positiv, indem es ausschließt, was er nicht ist (keine symmetrische Invariante,
nichts Abzählbares/Topologisches — 2/(9π) transzendent, kein statischer
Ikosaeder-Winkel): was er *ist*, ist eine dynamische, betragserhaltende
Holonomie-Phase (χ = π/2). Das Transzendenz-Resultat ist selbst positives
Wissen — 2/9 kann aus keiner flachen/topologischen Quelle stammen. Der Wert
steht fest und seine Herkunft ist geklärt: die Koide-Phase ist erledigt.

### Methodik — der Toleranz-Maßstab

In Dok. 292 durchgängig explizit gemacht: Der Maßstab einer geometrischen
Herleitung ist **nicht** die punktgenaue Übereinstimmung auf der letzten
Ziffer — die ist prinzipiell unerreichbar —, sondern die Verträglichkeit
**innerhalb der Toleranzen**, in denen die Größen bestimmbar sind.
Vollständigkeit heißt: kein Rest mehr, der über diese Toleranzen hinausragt
und nur durch einen freien Parameter zu schließen wäre. Das narrative
Überblicksdokument (Dok. 205) trägt jetzt eine Standortbestimmung in diesem
Geist.

### Anmerkung: externer Gegencheck (HLV / BD17A)

Die Frage, ob θ = 2/9 erzwungen wird, wurde zusätzlich blind gegen einen
externen Holonomie-Mechanismus geprüft (Marcel Krügers HLV / BD17A,
Information Physics Institute), unter symmetrischer Vorregistrierung. Das
Verdikt war negativ (BLOCKED / nicht separiert) — die vorhergesagte Richtung,
da eine flache Determinanten-Linien-Holonomie einen transzendenten Winkel
nicht als topologische Invariante tragen kann. Das betrifft den externen
Rahmen, nicht FFGFTs eigene Ergebnisse: die 2/9-Struktur im FFGFT-Massen-
Zirkulanten und Q = 2/3 bleiben unberührt. Der Vollständigkeit halber
dokumentiert in `2/Dok291_Skripte/` (Verdikt + Siegel).

---

## Kernableitungen (Stand v1.1.7)

| Ergebnis | Dokument |
|----------|----------|
| Ableitungskette ξ → G → ℓ_P → L₀ | [Dok. 180](2/pdf/180_T0_L0_Herleitung_De.pdf) |
| Leptonmassen aus rationalen Invarianten | [Dok. 006](2/pdf/006_T0_Teilchenmassen_De.pdf) / [046](2/pdf/046_Teilchenmassen_De.pdf) |
| Koide-Skalar Q = 2/3 (berechnet) | [Dok. 258](2/pdf/258_Koide_2-3_De.pdf) / [259](2/pdf/259_Koide_Kreuzterme_De.pdf) |
| α⁻¹ = 137,036, zwei unabhängige E₀-Wege | [Dok. 011](2/pdf/011_T0_Feinstruktur_De.pdf) / [292](2/PDFs/292_Leptonen_Empirie_Check_De.pdf) |
| SI-Brücke | [Dok. 013](2/pdf/013_T0_SI_De.pdf) |
| Hilbertraum-Bijektion FFGFT ↔ QM | [Dok. 230](2/pdf/230_Hilbertraum_Uebersetzung_De.pdf) |
| Leptonen-Empirie-Check, m_τ-Vorhersage, Toleranz-Bilanz | [Dok. 292](2/PDFs/292_Leptonen_Empirie_Check_De.pdf) |
| θ=2/9 als Z₃-Zirkulant-Phase; dynamische Charakterisierung | [Dok. 291](2/PDFs/291_Dynamischer_Ort_Theta_2_9_De.pdf) / [286](2/pdf/286_Dynamischer_Sektor_Kinetik_De.pdf) |
| Falsifikation: Casimir / Rotverschiebung / Lithium | [Dok. 220](2/pdf/220_Casimir_De.pdf) / [221](2/pdf/221_Rotverschiebung_De.pdf) / [222](2/pdf/222_Lithium_De.pdf) |

---

## Reproduzierbarkeit

`2/Dok292_Skripte/` — Leptonen-Empirie-Check (Teile A–L).
`2/Dok291_Skripte/` — θ=2/9-Mechanismus-Skripte (und, der Vollständigkeit
halber, das Verdikt und die Siegel des externen Gegenchecks).

---

## Plattformen

| Ressource | Link |
|-----------|------|
| 🔬 Interaktives Portal | [huggingface.co/spaces/jpascher/T0-FFGFT-Portal](https://huggingface.co/spaces/jpascher/T0-FFGFT-Portal) |
| 📁 GitHub Pages | [jpascher.github.io/T0-Time-Mass-Duality](https://jpascher.github.io/T0-Time-Mass-Duality/) |
| 📺 YouTube | [@Time-MassDuality](https://www.youtube.com/@Time-MassDuality) |

---

© 2025–2026 Johann Pascher · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
