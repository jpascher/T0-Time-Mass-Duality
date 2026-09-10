# Atemfrequenz-Scan — Johann Pascher, 10. September 2026
## Endversion nach Artefakt-Korrektur

## Protokoll
Polar H10 EKG-Brustgurt, 130 Hz, JSONL-Export (ECG + ACC), sitzend.
Metronom: Klick = Wechsel (einatmen ODER ausatmen).
4 bpm → 2/min; 8 bpm → 4/min; 10 bpm → 5/min; 12 bpm → 6/min.
R-Peaks aus ECG (Pan-Tompkins), Artefakt-Filterung: Median ±30%.
Atemfrequenz aus R-Amplituden-Modulation.

## Endgültige Ergebnistabelle (bereinigt)

| Bedingung | Atem/min | LF Hz | RMSSD ms | Artefakte |
|-----------|---------|-------|----------|-----------|
| Spontan (liegend) | 12.6 | 0.073 | 33.6 | 0 |
| 4/min | 4.0 | 0.105 | 33.6 | 0 |
| 2/min Aufn.1 | 2.0 | 0.071 | 27.7 | 2 missed beats |
| 2/min Aufn.2 | 2.0 | 0.075 | 30.5 | 0 |
| 5/min Aufn.1 | 5.1 | 0.144 | 29.5 | 2 missed beats |
| **5/min Aufn.2** | **5.0** | **0.132** | **39.9** | **0** |
| 6/min | 6.0 | 0.040 | 36.1 | 0 |

## Galois-Analyse (bereinigt)

| Bedingung | LF/HF | Galois p/q | Distanz | k |
|-----------|-------|-----------|---------|---|
| Spontan | 1.24 | 56/45 | 0.14% ✓ | 6 |
| 4/min | 4.43 | — | >10% | — |
| 2/min A1 | 8.14 | 4 | 103% | 1 |
| 2/min A2 | 9.31 | 4 | 133% | 1 |
| 5/min A2 (sauber) | 2.51 | 88/35 | 0.02% ✓ | 6 |
| 6/min | 1.12 | 39/35 | 0.06% ✓ | 6 |

## Hauptbefunde (endgültig)

### 1. Kein RMSSD-Resonanzeffekt nachweisbar
Nach Artefakt-Bereinigung: RMSSD 27–40 ms bei allen Bedingungen —
kein signifikanter Unterschied zwischen den Atemfrequenzen.
Das frühere RMSSD-Maximum bei 5/min (67.2 ms) war ein
R-Peak-Detektionsartefakt (2 missed beats, |ΔRR|max=662 ms).

### 2. LF-Peak wandert mit Atemfrequenz
LF-Peak verschiebt sich systematisch:
- 2/min: 0.071–0.075 Hz ≈ Spontan-Wert (0.073 Hz)
- 4/min: 0.105 Hz (aufwärts)
- 5/min: 0.132–0.144 Hz (weiter aufwärts)
- 6/min: 0.040 Hz (abwärts, anders als erwartet)

Das zeigt Kopplung des Barorezeptorkreises an die Atmung,
aber keine stabile Resonanz im klassischen Sinne (n=1).

### 3. Galois-Raster bei 5/min und 6/min getroffen
LF/HF = 88/35 (Distanz 0.02%) bei 5/min und 39/35 (Distanz 0.06%)
bei 6/min — beide k=6 (GF(729), R115). Bei Spontanatmung: 56/45
(Distanz 0.14%). Die Galois-Projektion ist reproduzierbar, aber
die Distanz allein ist kein Stabilitätskriterium.

### 4. Kein LF=Atem-Zusammenfall
LF-Peak und Atemfrequenz blieben bei allen Bedingungen getrennt.
Der Galois-Resonanztest wurde nicht erfüllt.
Bestätigt BIDMC und Fantasia.

## Methodische Lehren

1. **Artefakt-Filterung ist zwingend** bei kurzen Aufnahmen und
   kontrollierter Atmung: missed beats durch Amplitudenmodulation
   des EKG treiben RMSSD artifiziell hoch.
2. **Subharmonischen-Problem** bei ≤2/min: RSA-Detektor kann
   halbe Frequenz detektieren — Verifikation durch Spektrum nötig.
3. **n=1, kurze Aufnahmen**: Keine statistischen Schlüsse möglich.
   Alle Befunde explorativ.

## Empfehlung
- Längere Aufnahmen (≥15 min) pro Bedingung
- Mehrere Probanden (n>5)
- Robuste R-Peak-Detektion mit ektopischen Schlägen-Filterung

## Literatur
- Lehrer & Gevirtz (2014). Front. Psychol. 5:756.
- Task Force ESC/NASPE (1996). Eur. Heart J. 17, 354–381.
- Pan & Tompkins (1985). IEEE Trans. Biomed. Eng. 32(3):230–236.
