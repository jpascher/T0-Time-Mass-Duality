# Polar H10 Selbsttest — Johann Pascher, 10. September 2026

## Aufnahme
- Gerät: Polar H10 (EKG-Brustgurt, Firmware 4.2.0)
- App: Polar Sensor Recording (Android), JSONL-Export
- Datei: PolarRecording_20260910_125832
- Dauer: 21,9 min, spontane Atmung, liegend
- n_RR: 1517 RR-Intervalle

## Physiologische Kennwerte

| Kennwert | Wert | Einordnung |
|----------|------|------------|
| HF | 69,2 bpm (RR̄ = 867 ms) | Normal Ruhe |
| RMSSD | 36,3 ms | Gut für 75 J. (Fantasia alt: 20–35 ms) |
| SDNN | 53,8 ms | Normal |
| Atemfrequenz | 12,6/min (0,210 Hz) | Spontan, leicht erhöht |
| LF-Peak | 0,073 Hz | Unter Norm (~0,10 Hz) |
| HF-Peak | 0,210 Hz | = Atemfrequenz ✓ |

## Galois-Analyse

| Kennwert | Wert |
|----------|------|
| LF-Leistung | 951,75 ms² |
| HF-Leistung | 765,88 ms² |
| LF/HF (roh) | 1,2427 |
| Galois p/q | 56/45 = 1,2444 |
| Distanz | 0,14% — **im Raster ✓** |
| Orbit-Tiefe k | 6 (Primzahl 7, GF(729)) |
| 5-Limit | Nein (Prim 7) |
| Arnold-Stabilität | 0,020 (niedrig) |
| LF-CV | 10,55% >> 1,33% (instabil) |

## Befund

Bestätigt die Fantasia-Negativ-Validierung aus demselben strukturellen Grund:
bei spontaner Atmung ist HF = Atemfrequenz (hier 12,6/min = 0,21 Hz, variabel).
LF/HF ist das Verhältnis zweier unabhängiger Regelkreise — kein festes Galois-Verhältnis.

**LF-CV 10,55%** liegt im Bereich der Fantasia-Probanden (11–33%) und bestätigt:
der Galois-Test bei Spontanatmung ist strukturell nicht prüfbar.

**Positiver Befund:** RMSSD 36,3 ms ist für 75 J. sehr gut (Fantasia „alt": 20–35 ms).
Die Datenqualität des Polar H10 ist einwandfrei — klinische EKG-Qualität.

**LF-Peak bei 0,073 Hz** (unter Norm 0,10 Hz): mögliche parasympathische Dominanz
in Ruhe oder individuelle Barorezeptor-Resonanzfrequenz. Das ist ein Hinweis:
das individuelle Resonanzfrequenz-Protokoll (Lehrer & Gevirtz 2014) würde
die individuelle Resonanzfrequenz ermitteln — sie liegt nicht zwingend bei 6/min.

## Vergleich

| | Johann | Fantasia jung | Fantasia alt |
|---|---|---|---|
| RMSSD ms | 36,3 | 35–60 | 20–35 |
| LF-CV % | 10,55 | 11–33 | 11–33 |
| RR̄ ms | 867 | ~820 | ~900 |
| LF-Peak Hz | 0,073 | 0,07–0,11 | 0,05–0,08 |

## Nächster Schritt

Individuelle Resonanzfrequenz ermitteln: schrittweise Atemfrequenzen testen
(4, 5, 6, 7, 8/min) und LF-Peak-Stabilität messen. Die Frequenz mit maximalem
LF-Peak und minimalem CV ist die individuelle Resonanzfrequenz — bei Johann
möglicherweise eher 4–5/min (0,067–0,083 Hz) als 6/min (0,100 Hz).
