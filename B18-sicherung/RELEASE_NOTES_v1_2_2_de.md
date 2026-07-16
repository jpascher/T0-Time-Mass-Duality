# Release Notes — v1.2.2 (Juli 2026)

**DOI:** wird beim Zenodo-Upload vergeben (löst v1.2.1 ab · [10.5281/zenodo.21203746](https://doi.org/10.5281/zenodo.21203746))

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

## Was ist neu in v1.2.2

v1.2.2 sammelt **FFGFT-interne Klärungen** rund um die kompakte Projektion und
den fraktalen Korrekturfaktor. Kein neues Grundgerüst — Schärfung bestehender
Ableitungen.

### Das Standardmodell als dekompaktifizierte Projektion (Dok. 298)

Der Standardmodell-Inhalt erscheint als **dekompaktifizierte Projektion** der
kompakten T⁴-Struktur: Windungszahl und fraktales Komma leben auf der
aufgerollten Ebene, die projizierte Ebene sieht die geschlossene Näherung. Das
ordnet die SI-/Messebene konsistent unter das kompakte Bild (Anschluss an
Dok. 270 Projektionskette).

### Der Korrekturfaktor K_frak = 1 − 100ξ, aus dem Schließungs-Komma gelesen (Dok. 300)

Die aufgerollte Rekursion schließt erst nach **75 = 1/(100ξ₀)** gleichen
Teilstücken. Die Näherung „eine Umdrehung deckt sich" vernachlässigt ein
kleines **Schließungs-Komma** ε = 100ξ = 1/75; der Pro-Schritt-Faktor der
Skalen-Rekursion ξ_{n+1} = ξ_n(1−100ξ_n) ist damit

  **K_frak = 1 − 100ξ = 74/75 = 0,9867.**

Wichtig (P35): 75 und K_frak sind **beide** nur 100ξ — das Komma
*re-exprimiert* die schon verankerte 100ξ, es leitet sie nicht neu ab. Der
tatsächliche Anker bleibt **Dok. 133**: der Faktor 100 emergiert aus dem
RG-Lauf von D_f = 3−ξ (effektiv D_f^eff ≈ 2,973; geometrisch 100 = 4·5²,
Dok. 042), und K_frak ist durch die Konsistenz zweier unabhängiger Herleitungen
des Massenverhältnisses m_e/m_μ fixiert; ξ selbst über Higgs/α/Koide. Das ist
eine **Klärung eines bestehenden Korpuswerts**, keine neue Zahl.

### ι-Einbettungsprotokoll (Dok. 299) — FFGFT-intern

Das Protokoll fixiert Definitionsbereich, Zielraum H = L²(T⁴)⊗ℂ³ und die
Prüfnullen **vor** der Ausarbeitung (P35). Der FFGFT-relevante Befund: die
Prüfung nutzt einen **abgeleiteten** Zeugen (BLP-Rückfluss 5,125, Dok. 283),
keine Kopie des geprüften Objekts — Selbstreferenz durch Ableitung, nicht durch
Kopie. Ergebnis im Zeitsektor: **zugelassen, nicht erzwungen**, bedingt auf den
Windungswinkel des nativen Trägers.

---

## Verhältnis zu HLV (extern, nachrangig)

Die obigen Klärungen entstanden am Berührungspunkt mit HLV (Marcel Krüger,
Information Physics Institute), sind aber **FFGFT-intern** formuliert. Weil
FFGFT die absolute Skala besitzt (Referenzpunkt E₀) und HLV nicht, läuft die
Prüfrichtung einseitig FFGFT→HLV; der Korrekturfaktor 1−100ξ ist unabhängig
verankert (Dok. 133), nicht aus dem externen Rahmen gewählt. HLV bleibt ein
nachrangiger Gegencheck, kein tragender Bestandteil.

---

## Kernableitungen (Stand v1.2.2)

| Ergebnis | Dokument |
|----------|----------|
| Ableitungskette ξ → G → ℓ_P → L₀ | [Dok. 180](2/pdf/180_T0_L0_Herleitung_De.pdf) |
| Leptonmassen aus rationalen Invarianten | [Dok. 006](2/pdf/006_T0_Teilchenmassen_De.pdf) / [046](2/pdf/046_Teilchenmassen_De.pdf) |
| Koide-Skalar Q = 2/3 (berechnet) | [Dok. 258](2/pdf/258_Koide_2-3_De.pdf) |
| θ = 2/9 als Z₃-Zirkulant-Phase / parameterfreier Invariant | [Dok. 291](2/PDFs/291_Dynamischer_Ort_Theta_2_9_De.pdf) / [293](2/PDFs/293_Ikosaeder_Theta_2_9_De.pdf) |
| Fraktale Korrektur K_frak = 1 − 100ξ (RG-Lauf, m_e/m_μ-Konsistenz) | [Dok. 133](2/pdf/133_Fraktale_Korrektur_Herleitung_De.pdf) / [300](2/PDFs/300_ZweiRollen_Kfrak_De.pdf) |
| Standardmodell als dekompaktifizierte Projektion | [Dok. 298](2/PDFs/298_SM_Projektion_De.pdf) |
| α⁻¹ = 137,036, zwei unabhängige E₀-Wege | [Dok. 011](2/pdf/011_T0_Feinstruktur_De.pdf) / [292](2/PDFs/292_Leptonen_Empirie_Check_De.pdf) |
| Hilbertraum-Bijektion FFGFT ↔ QM (Zeit mitbeschrieben) | [Dok. 230](2/pdf/230_Hilbertraum_Uebersetzung_De.pdf) / [282](2/PDFs/282_FFGFT_HLV_CP_Teilbarkeit_De.pdf) |
| SI-Brücke | [Dok. 013](2/pdf/013_T0_SI_De.pdf) |

---

## Reproduzierbarkeit

`2/Dok300_Skripte/` — Schließungs-Komma-Prüfung (K_frak = 1−100ξ), numpy-only.
`2/Dok299_Skripte/` — Zeitsektor-Gegenlauf mit abgeleitetem Zeugen (BLP-Rückfluss 5,125), numpy-only.
`2/Dok295_Skripte/` — Zeit-Windung: 75-Schließung, log-Spirale, numpy-only.
`2/Dok283_Skripte/` — Gedächtniskern, Revivals, numpy-only.
`2/Dok292_Skripte/` — Leptonen-Empirie-Check (Teile A–L).

---

## Plattformen

| Ressource | Link |
|-----------|------|
| 🔬 Interaktives Portal | [huggingface.co/spaces/jpascher/T0-FFGFT-Portal](https://huggingface.co/spaces/jpascher/T0-FFGFT-Portal) |
| 📁 GitHub Pages | [jpascher.github.io/T0-Time-Mass-Duality](https://jpascher.github.io/T0-Time-Mass-Duality/) |
| 📺 YouTube | [@Time-MassDuality](https://www.youtube.com/@Time-MassDuality) |

---

© 2025–2026 Johann Pascher · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
