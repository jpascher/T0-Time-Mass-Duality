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

Ausführen / run:

    python3 z1_weyl_obstruktion.py
    python3 z2_zellbedingung.py
    python3 z3_randbedingung_test.py
    python3 z4_epstein_casimir.py
    python3 z5_zellbedingung_kritik.py

Eingaben / inputs: ξ = 4/30000 exakt; ℓ_P = 1,616255e-35 m,
λ̄_e = 3,8615926796e-13 m (CODATA 2022); Nullstellen (erste 50) aus der Literatur.
