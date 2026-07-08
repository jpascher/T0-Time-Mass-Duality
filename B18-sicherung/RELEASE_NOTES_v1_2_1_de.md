# Release Notes — v1.2.1 (Juli 2026)

**DOI:** wird beim Zenodo-Upload vergeben (löst v1.1.9 ab · [10.5281/zenodo.21193007](https://doi.org/10.5281/zenodo.21193007))

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

## Was ist neu in v1.2.1

v1.2.1 ist eine **FFGFT-interne Klärung zur Zeit-Windung**. In v1.1.9 stand
[Dok. 295](2/PDFs/295_Zeit_Logspirale_De.pdf): die K_frak-Rekursion
ξ_{n+1} = ξ_n(1−100ξ_n) zwingt die Zeit-Windung zu einer **logarithmischen
Spirale mit Selbstähnlichkeits-Verhältnis e**. v1.2.1 hält fest, dass dieses
Ergebnis **nicht an ein Bild gebunden** ist — dieselbe Nichtschließung liegt
in zwei gleichwertigen Darstellungen vor.

### Zwei gleichwertige Darstellungen — die Zeit ist mitbeschrieben

- **Geometrisch:** als log-Spirale ρ = 75·e^{β/2π} aus der Rekursion; eingefroren
  schließt die Windung nach genau 75 Umläufen (75 = 1/(100ξ₀)), läuft ξ, zerfällt
  ξ_n ≈ 1/(100(n+75)), der kumulierte Defekt wird logarithmisch (Dok. 295).
- **Im Hilbertraum:** als **Gedächtniskern** — die Fourier-Transformierte der
  diskreten Spektraldichte Σ_k g_k²·δ(ω−ω_k) des T⁴-Connection-Laplace (Dok. 283);
  ein oszillierender, diskret-spektraler Kern mit Revivals (BLP-Rückfluss 5,125).

Beide sind **dasselbe untrennbare Objekt** auf der **verlustfreien Bijektion**
H = L²(T⁴)⊗ℂ³ (Dok. 230/282, Typ III der Projektionskette Dok. 270). Die
Hilbertraum-Übersetzung von FFGFT beschreibt damit **auch die Zeit** mit — es
gibt mehrere gleichwertige Wege zum selben Ergebnis, die Zeit inbegriffen.

### Was das ist und was nicht (P35)

Gleichwertige Darstellungen *müssen* übereinstimmen — dasselbe Objekt in T⁴, in
verschiedener Kleidung. Das ist **Darstellungs-Robustheit, keine zusätzliche
Evidenz**: *Übersetzung ist nicht Begründung.* Das generative Original bleibt T⁴
(Dok. 206/270/287); die anderen Formen sind Rechenformen. Die eigentliche
Beweiskraft sitzt bei den **unabhängigen Zeugen** — verschiedene Methoden,
derselbe Wert, wie θ = 2/9 aus Koide (aus den Massen) **und** aus der Geometrie
(parameterfrei, ohne 2/9-Eingabe, Dok. 293) —, nicht bei gleichwertigen
Übersetzungen.

---

## Kernableitungen (Stand v1.2.1)

| Ergebnis | Dokument |
|----------|----------|
| Ableitungskette ξ → G → ℓ_P → L₀ | [Dok. 180](2/pdf/180_T0_L0_Herleitung_De.pdf) |
| Leptonmassen aus rationalen Invarianten | [Dok. 006](2/pdf/006_T0_Teilchenmassen_De.pdf) / [046](2/pdf/046_Teilchenmassen_De.pdf) |
| Koide-Skalar Q = 2/3 (berechnet) | [Dok. 258](2/pdf/258_Koide_2-3_De.pdf) / [259](2/pdf/259_Koide_Kreuzterme_De.pdf) |
| θ = 2/9 als Z₃-Zirkulant-Phase | [Dok. 291](2/PDFs/291_Dynamischer_Ort_Theta_2_9_De.pdf) |
| θ = 2/9 als parameterfreier C₃-in-A₅-Geometrie-Invariant (zweiter Zeuge) | [Dok. 293](2/PDFs/293_Ikosaeder_Theta_2_9_De.pdf) |
| Zeit-Windung als log-Spirale mit Verhältnis e (geometrisch + Hilbertraum-Gedächtniskern) | [Dok. 295](2/PDFs/295_Zeit_Logspirale_De.pdf) / [283](2/PDFs/283_FFGFT_HLV_Bruecke_De.pdf) |
| α⁻¹ = 137,036, zwei unabhängige E₀-Wege | [Dok. 011](2/pdf/011_T0_Feinstruktur_De.pdf) / [292](2/PDFs/292_Leptonen_Empirie_Check_De.pdf) |
| SI-Brücke | [Dok. 013](2/pdf/013_T0_SI_De.pdf) |
| Hilbertraum-Bijektion FFGFT ↔ QM (Zeit mitbeschrieben) | [Dok. 230](2/pdf/230_Hilbertraum_Uebersetzung_De.pdf) / [282](2/PDFs/282_FFGFT_HLV_CP_Teilbarkeit_De.pdf) |
| Leptonen-Empirie-Check, m_τ-Vorhersage, Toleranz-Bilanz | [Dok. 292](2/PDFs/292_Leptonen_Empirie_Check_De.pdf) |
| Falsifikation: Casimir / Rotverschiebung / Lithium | [Dok. 220](2/pdf/220_Casimir_De.pdf) / [221](2/pdf/221_Rotverschiebung_De.pdf) / [222](2/pdf/222_Lithium_De.pdf) |

---

## Reproduzierbarkeit

`2/Dok295_Skripte/` — Zeit-Windung: 75-Schließung, log-Spirale (Verhältnis e),
duale Zeit↔Masse-Projektion (Faktor 100 achsensymmetrisch), numpy-only.
`2/Dok283_Skripte/` — Gedächtniskern als Fourier-Transformierte der diskreten
Spektraldichte des T⁴-Connection-Laplace (Revivals, BLP-Rückfluss 5,125), numpy-only.
`2/Dok293_Skripte/` — ikosaedrische Umverteilung (p₀ = 2/9 exakt, Robustheit
über zufällige Achsen und die n-zählige Reihe), numpy-only.
`2/Dok292_Skripte/` — Leptonen-Empirie-Check (Teile A–L).
`2/Dok291_Skripte/` — θ = 2/9-Mechanismus-Skripte.

---

## Plattformen

| Ressource | Link |
|-----------|------|
| 🔬 Interaktives Portal | [huggingface.co/spaces/jpascher/T0-FFGFT-Portal](https://huggingface.co/spaces/jpascher/T0-FFGFT-Portal) |
| 📁 GitHub Pages | [jpascher.github.io/T0-Time-Mass-Duality](https://jpascher.github.io/T0-Time-Mass-Duality/) |
| 📺 YouTube | [@Time-MassDuality](https://www.youtube.com/@Time-MassDuality) |

---

© 2025–2026 Johann Pascher · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
