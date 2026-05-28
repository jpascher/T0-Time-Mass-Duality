# K2-Korrekturbericht — r_τ = 8/3 → 25/9 (vollständige Einarbeitung)

**Datum:** 27. Mai 2026
**Anlass:** Dok. 190 K2-Nachtrag (26. Mai) meldete verbliebene 8/3-Reste in 016/046/116.
Vollprüfung ergab zusätzlich übersehene Reste in **046 DE** (abgeleitete Werte).
**Soll-Stand (Dok. 190):** r_τ = 25/9 · m_τ = 1783,4 MeV · Abw. +0,37 % · ξ_ντ = 400/81·10⁻⁸ · E_ντ = 18,0 meV · ν_τ-Zeilen 25/9.

---

## Durchgeführte Korrekturen

### 046 DE — `046_Teilchenmassen_De_ch.tex` (war als „erledigt" geführt, hatte aber Reste)
| Stelle | Vorher | Nachher |
|---|---|---|
| Ergebnistabelle ν_τ (Verträglichkeit) | 18.8 meV | 18.0 meV |
| Methodenäquivalenz, Tau-Zeile | r_i = 2.768 | 2.778 (= 25/9) |
| Methodenäquivalenz, ν_τ-Zeile | 18.8 ×10⁻⁶ / 2.768 | 18.0 ×10⁻⁶ / 2.778 |
| Falsifikations-/Massentabelle m_{ν_τ} | 18.8 meV | 18.0 meV |

(Haupt-Rechnung war bereits korrekt: ξ_ντ = 400/81, E = 18,0 meV; nur die nachgelagerten Tabellen waren nicht nachgezogen.)

### 016 EN — `016_T0_Vollstaendige_Berchnungen_En_ch.tex` (DE war korrekt)
| Stelle | Vorher | Nachher |
|---|---|---|
| Massentabelle, Tau-Zeile | 8/3 · 1712.1 · 3.64 | 25/9 · 1783.4 · 0.37 |
| r-Parameter-Liste | …, 8/3, … | …, 25/9, … |

### 046 EN — `046_Teilchenmassen_En_ch.tex` (DE war korrekt)
| Stelle | Vorher | Nachher |
|---|---|---|
| ν_τ-Parameterzeile (erste Tabelle) | 8/3 & 8/3 | 25/9 & 25/9 |
| ξ_ντ-Rechnung | 8/3 → 128/27 | 25/9 → 400/81 |
| E_ντ (3 Stellen) | 18.8 meV | 18.0 meV |
| Methodenäquivalenz, Tau + ν_τ | 2.768 | 2.778 |
| ν_τ-Zeile (zweite Tabelle) | 8/3 & 8/3 | 25/9 & 25/9 |

### 116 EN — `116_T0_koide-formel-3_En_ch.tex` (DE war korrekt)
| Stelle | Vorher | Nachher |
|---|---|---|
| Leptonparameter-Tabelle, Tau-Zeile | r = 8/3 | 25/9 |

---

## Richtungsentscheidung Tau-Neutrino

Das frühere Changelog hielt fest „ν_τ bleibt 8/3 — eigenständiger Wert, kein r_τ".
Dok. 190 (26. Mai) und die bereits korrigierte **046-DE-Rechnung** (ξ_ντ = 400/81)
setzen ν_τ jedoch auf 25/9. **Maßgeblich ist Dok. 190** (jüngster Stand); die EN-Datei
wurde entsprechend auf 25/9 / 400/81 / 18,0 meV gebracht. Diese Richtungsänderung
gegenüber dem alten Changelog ist hiermit dokumentiert.

---

## Verifikation
- Korpusweite Restsuche (8/3, 128/27, 1712, 18.8, 2.768, 3.64) in allen vier Dateien: **0 Treffer**.
- Spaltenzahl (`&`) der geänderten Tabellenzeilen identisch mit Nachbarzeilen — keine zerbrochenen Tabellen.
- Keine fehlerhaften `\&`-Escapes eingeführt.

## Offen / Hinweise
- **EN-Build der Voll-PDFs** steht noch aus (benötigt LuaLaTeX + Voll-Präambel; in dieser Umgebung nicht abschließend baubar). Empfehlung: 016/046/116 EN nach Übernahme neu kompilieren.
- **Datum/Version:** Diese EN-Korrekturen liegen nach dem v1.1.1-Release (23. Mai, DOI 20355305, „nichts geändert"). Das Zenodo-Archiv v1.1.1 ist in diesen Werten **nicht** deckungsgleich mit dem korrigierten Repo-Stand.
- **Dok. 190** sollte im K2-Statusabschnitt ergänzt werden: betroffen war auch **046 DE** (abgeleitete 18,8-Werte), und die EN-Seite (016/046/116) wurde erst am 27. Mai nachgezogen.
- **Changelog** K2-Eintrag entsprechend erweitern (Dok 016 + EN-Nachzug + ν_τ-Richtungsentscheidung).
