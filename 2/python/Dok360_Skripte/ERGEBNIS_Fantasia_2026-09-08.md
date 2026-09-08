# Fantasia-Galois-Analyse — Ergebnisse (8. September 2026)

## Datensatz
PhysioNet Fantasia Database v1.0.0, Gold et al. 2002
5 jung (f1y01-05, 21-34 J.) + 5 alt (f2o01-05, 68-85 J.)
Je ~120 min Ruhe, 250 Hz EKG, spontane Atmung, CC-BY 4.0

## Ergebnistabelle

| Rec    | Gr   | n_RR | LF Hz  | CV%   | Stab  | LF/HF | p/q   | k | 5lim | Arnold |
|--------|------|------|--------|-------|-------|-------|-------|---|------|--------|
| f1y01  | jung | 8707 | 0.1090 | 11.45 | NEIN  | 0.438 | 7/16  | 6 | NEIN | 0.087  |
| f1y02  | jung | 6919 | 0.0846 | 33.03 | NEIN  | 0.867 | 13/15 | 4 | NEIN | 0.071  |
| f1y03  | jung | 7641 | 0.1001 | 13.69 | NEIN  | 4.219 | 4     | 1 | JA   | 0.400  |
| f1y04  | jung | 5232 | 0.0777 | 30.94 | NEIN  | 1.060 | 35/33 | 6 | NEIN | 0.029  |
| f1y05  | jung | 6943 | 0.0680 | 16.50 | NEIN  | 2.993 | 3     | 1 | JA   | 0.500  |
| f2o01  | alt  | 7045 | 0.0667 | 25.57 | NEIN  | 1.494 | 3/2   | 1 | JA   | 0.400  |
| f2o02  | alt  | 6327 | 0.0515 | 14.40 | NEIN  | 0.864 | 45/52 | 4 | NEIN | 0.021  |
| f2o03  | alt  | 6478 | 0.0547 | 22.02 | NEIN  | 0.841 | 21/25 | 6 | NEIN | 0.043  |
| f2o04  | alt  | 6849 | 0.0648 | 32.21 | NEIN  | 0.719 | 28/39 | 6 | NEIN | 0.030  |
| f2o05  | alt  | 8334 | 0.0493 | 11.40 | NEIN  | 1.873 | 15/8  | 4 | JA   | 0.087  |

## Hauptbefunde

1. **LF-Peak-Stabilität: 0/10** — CV 11–33%, alle >> 1.33% (FFGFT-Grenze).
   Der LF-Peak wandert mit der spontanen Atemfrequenz.

2. **5-Limit LF/HF: 4/10 (40%)** — nicht signifikant. Zufallserwartung
   bei gleichverteilten Verhältnissen ~30–40% (weites Kriterium).

3. **Gruppenunterschied jung/alt: keiner** — alle p > 0.4, n.s.
   (n=5 pro Gruppe zu klein; und Spontanatmung verrauscht das Signal).

4. **Galois-Stabilität (Arnold-Zungenbreite):** Streut stark (0.02–0.50),
   kein Gruppenunterschied (p=0.40).

## Warum der Test scheitert — strukturelle Gründe

1. **HF = Atmung.** Die HF-Bandleistung folgt der spontanen Atemfrequenz
   (0.15–0.4 Hz). LF/HF ist damit das Verhältnis zweier unabhängiger
   Regelkreise, deren Frequenzen sich unabhängig ändern.

2. **LF wandert.** Der LF-Peak liegt physiologisch bei ~0.04–0.15 Hz
   und ist nicht auf einen festen Wert stabilisiert. CV 11–33% ist
   ca. 10–25x größer als die FFGFT-Grenze.

3. **Galois-Raster zu fein.** Bei einem LF/HF zwischen 0.4 und 4.5
   landen ~40% der Werte zufällig im 5-Limit-Raster. Das Kriterium
   ist nicht diskriminativ.

## Konsequenz

Das Galois-Signal ist bei spontaner Atmung nicht prüfbar.
Der saubere Test erfordert:

- **Kontrollierte Atmung 6/min** (0.1 Hz): LF = HF → Ratio = 1:1.
  Frage: rastet das System ein (Arnold-Zunge breit) oder nicht?
- **Sensor**: Polar H10 (Brustgurt, 1 ms RR-Auflösung).
- **Protokoll**: 5 min Eingewöhnung, 5–10 min bei 6/min Metronom.
- **Referenz**: Lehrer & Gevirtz 2014, Appl. Psychophysiol. Biofeedback.

## Literatur
- Gold et al. (2002). Phantasia database. PhysioNet.
- Task Force ESC/NASPE (1996). Eur. Heart J. 17, 354–381.
- Lehrer & Gevirtz (2014). Front. Psychol. 5:756.
