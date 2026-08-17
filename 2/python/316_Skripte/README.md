# Dok. 316 — Prüfskripte / verification scripts

Reine Standardbibliothek, Sollwerte als Assertions, Seed 20780458.
Standard library only, target values as assertions, seed 20780458.

| Skript | Inhalt / content | Status |
|---|---|---|
| `z1_weyl_obstruktion.py` | Weyl-Gesetz gegen Riemann-von Mangoldt; lokaler Exponent, Potenzfit | [X] Ausschluss auf Satzebene |
| `z2_zellbedingung.py` | Berry-Keating-Zählung, Äquivalenz zur Riemann-Form, Gegenprobe Weyl | [B] Strukturaussage |
| `z3_randbedingung_test.py` | ξ-Leiter als Randbedingung; Artefaktkontrolle, Nullverteilung, Out-of-Sample, GUE | [X] Test negativ |
| `z4_epstein_casimir.py` | Faktorisierung gegen Direktsumme; Casimir-Symmetriepunkt | [K] verifiziert |
| `z5_zellbedingung_kritik.py` | Zerfall des Zellarguments in drei Stufen | [X] Rücknahme |
| `z6_tonnetz_weil.py` | ξ als Tonnetz-Punkt; Fourier-Nachweis des Weil-Längenspektrums, Auflösungsgrenze | [X] Summe, keine Länge |
| `z10_kommatest.py` | Hat der P-315-2-Rest Kommastruktur? Glattheitstest mit Kontrollprobe | [X] kein Komma |
| `z9_limit_einschluss.py` | Fünf Lesarten der Limit-Einschließung; Ragisma und Archytas-Komma als Näherungsfehler | [X] nur genähert/temperiert |
| `z8_bikohaerenz.py` | Nullstellen per Riemann-Siegel (2469 bis t=3000), Bikohärenz mit Phasenrandomisierung, Positiv-/Negativkontrollen | [K] Mischterme gemessen, Z-4 geschlossen |
| `z7_gewichtung_unmoeglich.py` | Gewichtungsstärke α, Limit-Erweiterung (5-/7-/11-Limit), Permutationstests, Starrheit der Weil-Gewichte | [X] Z-1 entschieden |

Ausführen / run:

    for f in z1_weyl_obstruktion z2_zellbedingung z3_randbedingung_test \
             z4_epstein_casimir z5_zellbedingung_kritik z6_tonnetz_weil \
             z7_gewichtung_unmoeglich z8_bikohaerenz \
             z9_limit_einschluss z10_kommatest; do
        python3 $f.py
    done

Eingaben / inputs: ξ = 4/30000 exakt; ℓ_P = 1,616255e-35 m,
λ̄_e = 3,8615926796e-13 m (CODATA 2022); Nullstellen (erste 100) aus der Literatur; z8 berechnet 2469 selbst.
