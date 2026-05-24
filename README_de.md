# T0 Zeit-Masse-Dualität · FFGFT

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20355305.svg)](https://doi.org/10.5281/zenodo.20355305)

**FFGFT (Fundamentale Fraktale Geometrische Feldtheorie)** leitet alle Standardmodell-Konstanten — Teilchenmassen, α, G, ℏ, c — aus einem einzigen dimensionslosen Parameter **ξ = 4/3 × 10⁻⁴** auf einem 4D-Identifikationstorus T⁴ her. Die Grundrelation lautet **T̃ · m = 1** (Zeit-Masse-Dualität). Keine freien Parameter. Alle Konstanten sind geometrische Konsequenzen.

**Autor:** Johann Pascher · johann.pascher@gmail.com  
**ORCID:** 0009-0000-6518-4064

---

## Plattformen

| Ressource | Link |
|-----------|------|
| 🔬 Interaktives Portal (Hugging Face) | [huggingface.co/spaces/jpascher/T0-FFGFT-Portal](https://huggingface.co/spaces/jpascher/T0-FFGFT-Portal) |
| 📁 GitHub Pages (Tools & HTML) | [jpascher.github.io/T0-Time-Mass-Duality](https://jpascher.github.io/T0-Time-Mass-Duality/) |
| 📦 Zenodo Archiv v1.1.1 | [DOI 10.5281/zenodo.20355305](https://doi.org/10.5281/zenodo.20355305) |
| 🎵 Audiobibliothek (Spotify) | [T0 Podcast](https://creators.spotify.com/pod/show/0PwnOIqjFepxA7NQ5i3fwR/episodes) |
| 📺 YouTube | [@Time-MassDuality](https://www.youtube.com/@Time-MassDuality) |

---

## Kernergebnisse

- **Null freie Parameter:** Alle 20+ Standardmodell-Parameter aus ξ hergeleitet
- **Teilchenmassen:** 98% Durchschnittsgenauigkeit aus einer einzigen Formel
- **Feinstrukturkonstante:** α⁻¹ = 137,036 aus fraktaler Dimension D_f = 3 − ξ
- **Myon g-2:** 0,05σ Übereinstimmung mit dem Experiment
- **Hubble-Spannung:** ℏH₀/mₑc² = (π/2)·ξ¹⁰, Abweichung 0,000%
- **Hilbertraum-Bijektion:** Vollständige FFGFT ↔ Standard-QM-Übersetzung (Dok. 230)
- **Falsifikationskriterien:** Casimir (Dok. 220), Rotverschiebung (Dok. 221), Lithium (Dok. 222)

---

## Einstieg

| Schritt | Dokument |
|---------|----------|
| 1. Konzeptueller Überblick | [T0_SI_De.pdf](2/pdf/013_T0_SI_De.pdf) — SI-Reform 2019 und ξ |
| 2. Interaktive Erkundung | [T0 Parameter Explorer](https://huggingface.co/spaces/jpascher/T0-FFGFT-Portal) |
| 3. Feldtheorie | [202_FFGFT_Feldtheorie_Gesamt_De.pdf](2/pdf/202_FFGFT_Feldtheorie_Gesamt_De.pdf) |
| 4. Hilbertraum-Brücke | [230_Hilbertraum_Uebersetzung_De.pdf](2/pdf/230_Hilbertraum_Uebersetzung_De.pdf) |
| 5. Alltagssprache | [205_FFGFT_Narrativ_De.pdf](2/pdf/205_FFGFT_Narrativ_De.pdf) |
| 6. Python | `2/python/authentic_t0_quantum.py` |

---

## Aktuelles Release: v1.1.1 (Mai 2026)

11 neue Dokumente in fünf Clustern. Vollständige Details: **[RELEASE_NOTES_v1_1_1_de.md](RELEASE_NOTES_v1_1_1_de.md)**

**IPI Methodologische Analyse**
- [240] KI-Detektoren und Ad-hominem-Argumentation (14/15 S.) — Manipulationsmuster im wissenschaftlichen Diskurs

**FFGFT vs. Externe Rahmenwerke**
- [245] FFGFT ↔ RA 2.1 (José Guevara) — Schicht-für-Schicht-Strukturvergleich
- [246] FFGFT ↔ RSG (Peter Austin) — Konvergenzen und Divergenzen
- [247] Kategorienfehler — Überarbeitete Formulierung

**Schwarzloch-Information**
- [250] Information und schwarze Löcher — Hawking-Paradoxon über Ontologie/Epistemologie-Unterscheidung; Gitterdispersionskorrektur ΔE/E = −(E/E_max)²/24
- [251] FFGFT ↔ Vopson Infodynamik — phänomenologische Konvergenz, keine Identität

**Zahlentheorie & Signalanalyse**
- [252] Phillips sigma-Waisen-Primzahlen und FFGFT — {2,5,11} im 13-glatten Ambient
- [253] Xi-Zahlenraumabhängigkeit — ξ_num vs. ξ_FFGFT: unbewiesene Vermutung, Fakten ausgewiesen

**Duale Ordnungsprinzipien**
- [254] Zwei Ordnungsprinzipien und das Flächenschranken-Theorem — Resonanz und Entropie kausal verbunden; Vopsons zweites Infodynamik-Gesetz geometrisch reproduziert

---

## Vorheriges Release: v1.1.0 (Mai 2026)

Herzstück: **Hilbertraum-Bijektion** (Dok. 230–232). Vollständige Details: **[RELEASE_NOTES_v1_1_0_de.md](RELEASE_NOTES_v1_1_0_de.md)**

Schlüsseldokumente:
- [230] FFGFT ↔ Hilbertraum-QM — konkrete Bijektion auf dem Qubit-Sektor; ΔCHSH ~ 10⁻⁵ testbar
- [231] Hilbertraum-Erweiterungen für volle FFGFT — vier etablierte mathematische Strukturen
- [232] Quantum Graphity als hypothetische FFGFT-Untermenge — Plausibilitätsskizze
- [206] Dreieck-Matrix-Reduktionstheorem — sechs externe Rahmenwerke getestet
- [220–222] Falsifikationstrilogie: Casimir / Rotverschiebung / Lithium

---

## Repository-Struktur

```
T0-Time-Mass-Duality/
├── 2/
│   ├── pdf/          # 250+ Dokumente (DE/EN-Paare)
│   ├── html/         # Interaktive Tools (21 Dateien)
│   └── python/       # Python-Implementierungen
├── ch/               # LaTeX-Kapitelquellen (*_ch.tex)
├── pri-end/          # Gemeinsame LaTeX-Präambeln
├── rsa/              # RSA-Faktorisierungs-Demos
└── sig/              # Signalanalyse-Tools
```

LaTeX-Struktur: Wrapper-Dateien in `wrapper/` referenzieren `../pri-end/T0_preamble_standalone_De/En`. Kapitelinhalte in `ch/` als `NNN_..._De/En_ch.tex`.

---

## Veröffentlichte Bücher (13 Bände, Amazon KDP)

Kindle- und Taschenbuchausgaben auf Deutsch und Englisch — Teil 1–3, FFGFT Narrative Master („Das Kosmische Gehirn"), T0 Anwendungen („Sieben Rätsel der Physik"), Von α=1 zur vollständigen Physik. PDF-Versionen in `2/pdf/` und `2/tex-n/completed/`.

---

## Versionshistorie

| Version | DOI | Inhalt |
|---------|-----|--------|
| v1.1.1 | [20355305](https://doi.org/10.5281/zenodo.20355305) | IPI-Brücken, Schwarzloch-Information, duale Ordnung |
| v1.1.0 | [20117635](https://doi.org/10.5281/zenodo.20117635) | Hilbertraum-Bijektion (Herzstück) |
| v1.0.14 | [20041543](https://doi.org/10.5281/zenodo.20041543) | Dreieck-Matrix-Reduktion, Falsifikationstrilogie |
| v1.0.13 | [20041529](https://doi.org/10.5281/zenodo.20041529) | QM-Brücke, Rekursionsoperator |
| v1.0.12 | [20022166](https://doi.org/10.5281/zenodo.20022166) | Vollständige Feldtheorie |
| v1.0.11 | [18834145](https://doi.org/10.5281/zenodo.18834145) | Quantencomputing-Reihe |

Vollständige Release-Notes als `RELEASE_NOTES_*.md`-Dateien verfügbar.

---

## Lizenz

© 2025–2026 Johann Pascher. Lizenziert unter [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

*Bestätigte Ergebnisse sind im Korpus dokumentiert; offene Vorhersagen bedürfen experimenteller Überprüfung.*
