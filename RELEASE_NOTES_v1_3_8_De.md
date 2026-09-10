# Release Notes — v1.3.8 (10. September 2026)

**DOI:** wird bei Zenodo-Publikation vergeben — ersetzt v1.3.7
Laufende Korrekturen: **[2/pdf/190_T0_Korrekturen_De.pdf](2/pdf/190_T0_Korrekturen_De.pdf)**
Änderungsprotokoll: **[001_FFGFT_Changelog_De.md](001_FFGFT_Changelog_De.md)**

**FFGFT — Fundamentale Fraktale Geometrische Feldtheorie** zeigt: Alle Konstanten des
Standardmodells folgen aus einem einzigen dimensionslosen Parameter **ξ = 4/30000**
auf einem kompakten 4D-Torus T⁴. Die Grundrelation lautet **T̃ · m = 1** — intrinsische
Zeit und Masse sind invers gekoppelt.

**Autor:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Überblick

Diese Version erweitert Dok. 360 um einen vollständigen Atemfrequenz-Scan mit
Polar H10 Brustgurt (7 Aufnahmen, je 5–6 min, kontrollierte Atmung bei 2, 4, 5
und 6 Atemzügen/min), eine korrigierte RMSSD-Analyse mit obligatorischer
Artefakt-Filterung sowie einen ersten vollständigen Journal-Manuskript-Entwurf
(Smart Wearable Technology, SWT). Keine algebraischen Ergebnisse in Dok. 342–360
sind geändert.

---

## Erweiterungen zu Dok. 360 seit v1.3.7

### Polar H10 Selbsttest — Spontanatmungs-Baseline
Aufnahme: `PolarRecording_20260910_125832`, 21,9 min liegend, spontane Atmung,
130 Hz EKG + HR JSONL-Export. Ergebnisse: HF 69,2 bpm, RMSSD 33,6 ms (HR-abgeleitet),
LF-Peak 0,073 Hz, LF/HF → 56/45 (Distanz 0,14 %, k=6). Bestätigt Fantasia-Befund:
LF-Peak-CV >> 1,33 % bei Spontanatmung.

### Polar H10 Atemfrequenz-Scan
Sieben sitzende Aufnahmen mit Metronom-gesteuerter Atmung
(Klick = Wechsel: einatmen ODER ausatmen):

| Bedingung | Metronom | Atem/min | LF Hz | RMSSD ms | Artefakte | LF/HF | Galois p/q | k |
|---|---|---|---|---|---|---|---|---|
| 4/min | 8 bpm | 4,0 | 0,105 | 33,6 | 0 | 4,43 | — | — |
| 6/min | 12 bpm | 6,0 | 0,040 | 36,1 | 0 | 1,12 | 39/35 | 6 |
| 5/min Aufn.1 | 10 bpm | 5,1 | 0,144 | 29,5 | 2 | 4,05 | — | — |
| **5/min Aufn.2** | **10 bpm** | **5,0** | **0,132** | **39,9** | **0** | **2,51** | **88/35** | **6** |
| 2/min Aufn.1 | 4 bpm | 2,0 | 0,071 | 27,7 | 2 | 7,94 | 4 | 1 |
| 2/min Aufn.2 | 4 bpm | 2,0 | 0,075 | 30,5 | 0 | 9,31 | 4 | 1 |

Alle Roh-JSONL-Dateien (EKG + ACC) im Repo unter `2/python/Dok360_Skripte/PolarH10_*.jsonl`.
Analyseskript: `polar_h10_atemfrequenz_scan.py` — reproduziert obige Tabelle
aus Rohdaten mit einem Befehl.

### Artefakt-Korrektur — methodischer Befund

Ein scheinbares RMSSD-Maximum bei 5/min Aufn.1 (67,2 ms roh) wurde auf
2 missed R-Peaks zurückgeführt (|ΔRR|_max = 662 ms), verursacht durch
EKG-Amplitudenmodulation bei langsamer Atmung. Nach Median-±30%-Filterung:
RMSSD 29,5 ms — kein Resonanzeffekt. Diese Korrektur ist als
**methodischer Befund** (M1) in Dok. 360 und im SWT-Manuskript dokumentiert.

Drei methodische Befunde sind jetzt in Dok. 360 dokumentiert:
- **M1:** Artefakt-Filterung (Median ±30 %) ist bei ≤4 Atemzügen/min zwingend.
- **M2:** Subharmonischen-Detektion bei ≤2 Atemzügen/min — Verifikation über vollständiges Amplitudenspektrum erforderlich.
- **M3:** Spontane Atmung macht den Galois-Test strukturell nicht prüfbar.

### Befundzusammenfassung (Dok. 360, endgültig)

1. **Kein RMSSD-Resonanzeffekt** nach Artefakt-Korrektur (27–40 ms bei allen Bedingungen).
2. **LF-Peak folgt der Atemfrequenz** (0,040–0,144 Hz) — keine stabile Ruheposition, kein LF = Atemfrequenz-Zusammenfall.
3. **Galois-Raster getroffen bei 5/min Aufn.2** (88/35, 0,02 %) und **6/min** (39/35, 0,06 %), beide k=6.
4. **Drei Negativ-Validierungen** (BIDMC-01, Fantasia, Polar H10 spontan) bestätigen strukturellen Befund [B].

---

## SWT-Journal-Manuskript (neu)

Erster vollständiger Entwurf:
**„Galois-Informed HRV Preprocessing: Algebraic Constraints for Wearable
Frequency Analysis"**
Zieljournal: *Smart Wearable Technology* (SWT, Bon View Publishing,
APC-frei bis 31. Dezember 2026, Annahmequote 31 %).

Dateien:
- `SWT_Galois_HRV_v2.docx` — Manuskript (~4.660 Wörter, 10 Seiten, Times New Roman 12pt A4)
- `SWT_CoverLetter.docx` — Anschreiben

Wesentliche Beiträge im Manuskript über Dok. 360 hinaus:
- **§4.5 Fundamentale Grenzen des Galois-Tests:** drei Grenzen formal definiert —
  EKG-Amplitudenmodulationsgrenze (≤4 Atemzüge/min), Auflösungsboden als Systemgrenze
  (1,33 %, keine Messgenauigkeit), Spontanatmung als epistemologische Grenze
  (mit Verweis auf Eckberg 1997, Karemaker 2017).
- **§4.6 Vorwissen und algebraische Constraints in der Spektralschätzung:**
  Galois-Zulässigkeit als algebraisch notwendiger Prior (härter als Bayes);
  Lattice-constrained Periodogramm als Implementierungsziel;
  Verbindung zu AR, MUSIC, ESPRIT, harmonischer Spektralanalyse.
- Datenverfügbarkeitserklärung, Fördernachweis, Interessenkonflikt-Erklärung,
  KI-Assistenz-Erklärung (COPE-konform), Autorenbiografie.

Status: einreichungsbereit ausstehend Zenodo-DOI für v1.3.7.

---

## Register
R106–R119 unverändert aus v1.3.7. Keine neuen Registereinträge.

---

## Aktualisierte Brücken seit v1.3.7

| Brücke | v1.3.7 | v1.3.8 |
|--------|--------|--------|
| Galois-informierte HRV: Resonanzfrequenz-Protokoll | [S] ausstehend | [S] getestet (n=1, negativ); Anwendbarkeitsenvelope definiert |
| SWT-Manuskript | — | erster vollständiger Entwurf bereit |

## Verbleibende offene Brücken (unverändert aus v1.3.7)

| Brücke | Status |
|--------|--------|
| CKM/PMNS-Winkelwerte (numerisch) | [S] (Dok. 348 Satz D); GF(3⁶)=GF(729) Kandidat |
| HRV-Galois-Test: positives Ergebnis | [S] erfordert kontrollierte Atmung ≥13 min, n≥5 |
| Generations-Zuordnung (Reihenfolge) | [S] (Dok. 346) |
| m_Pl und α_em(M_Z) aus ξ | [S] |
| Quark-/Hadron-Sektor | offen (Dok. 318, R76) |
| CMB-Peaks {1,6,14,26}; \|n\|²=30 | offen (P29/P31) |
| Δm²₃₂ Mischungsterm F₅–F₇ | [S] |

## Einstiegspunkt für neue Leser
Dok. 205 „FFGFT in einfacher Sprache" (DE+EN, 13–14 Seiten) bleibt der empfohlene
Einstieg. Das SWT-Manuskript (`SWT_Galois_HRV_v2.docx`) ist der empfohlene
Einstiegspunkt für die HRV-Anwendung der FFGFT.

## Was unverändert bleibt
ξ, T̃·m=1 und alle algebraischen Ergebnisse aus v1.3.7 sind unverändert.
Alle Herleitungsketten aus v1.3.6 sind unverändert.
