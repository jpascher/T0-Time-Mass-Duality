# HRV-5-Limit-Test an BIDMC-01 — warum er gescheitert ist (8. Sept. 2026)

## Daten
- BIDMC PPG and Respiration Dataset v1.0.0, Record 01 (88 J., m, MICU, 8 min, 125 Hz)
  Pimentel et al. 2017, PhysioNet, CC-BY 4.0
  https://physionet.org/content/bidmc/1.0.0/
  Dateien: bidmc01.dat, bidmc01.hea (beiliegend)
- rr01.csv: 728 RR-Intervalle (ms) aus Kanal II, erzeugt mit 01_rpeaks_bidmc01.py

## Kette
1. 01_rpeaks_bidmc01.py  — R-Zacken (Bandpass 5–20 Hz, find_peaks) → rr01.csv
2. 02_welch_5limit.py    — Welch-Spektrum, Peaks pro Band, 5-Limit-Test, Nullmodell
3. 03_lombscargle_dfa.py — Lomb-Scargle (kein Resampling), Atemreferenz, DFA
   Ergebnisse: ergebnis_02_welch.txt, ergebnis_03_lombscargle_dfa.txt

## Vorab festgelegtes Kriterium
Verhältnis f_j/f_i wird als 5-limit gewertet, wenn der nächste Bruch mit Nenner ≤ 12
nur Primfaktoren {2,3,5} hat UND die Abweichung ≤ 15 Cent beträgt.

## Ergebnis
| Verhältnis | Welch  | Lomb-Scargle | nächster 5-Limit-Bruch | Abweichung |
|-----------|--------|--------------|------------------------|-----------|
| HF/LF     | 2.545  | 2.449        | 5/2 = 2.500            | +31 / −36 Cent |
| LF/VLF    | 24.4   | 11.2         | —                      | VLF nicht auflösbar |
0 von 3 Verhältnissen erfüllen das Kriterium (beide Methoden).

## Warum es scheitert — vier Gründe
1. **Konvention ≠ Messung.** Die 100 % 5-limit vom Vortag stammten aus den Task-Force-
   Bandgrenzen 0.04/0.15/0.40 Hz. Das sind gewählte runde Dezimalzahlen; 100 = 2²·5²,
   also ist jede zweistellige Dezimalzahl fast automatisch 5-limit. Physiologie steckt
   da nicht drin. Gemessene Peaks (0.134, 0.328 Hz) sind es nicht.
2. **Gitterartefakt.** Das erste Welch-Skript (nperseg=256, Δf=0.0078 Hz) legte alle
   Peaks auf ein Gitter ganzzahliger Vielfacher; Verhältnisse waren zwangsläufig kleine
   Brüche. Mit Zero-Padding + parabolischer Interpolation verschwindet das.
3. **HF ist die Atmung.** HF-Peak 0.328 Hz = gemessene Atemfrequenz 0.336 Hz (RESP-Kanal).
   HF/LF ist also Atemfrequenz/Barorezeptorfrequenz — zwei unabhängige Regelkreise.
   Ein festes rationales Verhältnis wäre biologisch nicht zu erwarten; atmet der Patient
   langsamer, wandert HF.
4. **Messunsicherheit > Effekt.** Welch vs. Lomb-Scargle differieren um ±2 % in der
   Peakposition (2.545 vs. 2.449). Die 5/2-Hypothese (±15 Cent ≈ ±0.9 %) und die
   FFGFT-Grenze 100ξ = 1.33 % (Dok. 359 Satz B) liegen beide unter dieser Streuung
   und sind damit nicht prüfbar.

## Nebenbefund DFA
α1 = 0.50, α2 = 0.45 → praktisch weißes Rauschen; gesund wäre ≈ 1.0.
ICU-Patient, 88 J.: fraktale Regulation weitgehend verloren. Für Resonanz-/Fraktalfragen
ist dieses Kollektiv ungeeignet; nötig wären spontan atmende Gesunde (z. B. PhysioNet
nsrdb, WildPPG).

## Einschränkung
Ein Record. Das widerlegt nichts endgültig — es zeigt, dass die These an dieser Stelle
keine Stütze hat und dass die Bandgrenzen als Beleg nicht taugen.
