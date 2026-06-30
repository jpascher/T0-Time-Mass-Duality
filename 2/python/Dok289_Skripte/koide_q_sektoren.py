#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dok 289 -- Hebel: wo die vier Fermion-Sektoren in der (Q, r)-Koordinate liegen.

Jedes 3er-Triplett bekommt zwei Zahlen:
    Q = sum(m) / (sum sqrt(m))^2          (Koide-Skalar = Betrags-/Magnitude-Koordinate)
    r = sqrt(6Q - 2)                       (Umkehrung von  Q = 1/3 + r^2/6)
Nur die geladenen Leptonen sitzen bei Q = 2/3 (r = sqrt(2)).

WICHTIG: Quarkmassen sind MS-bar und LAUFEN (skalen-/schemaabhaengig); die
Quark-Q-Werte sind daher nur Illustration an einer Skala, kein Invariant.
Neutrinos: nur Delta m^2 gemessen, absolute Skala und Ordnung offen -> kein
Triplett bildbar.

numpy-only, seed 20780458. Werte PDG-nah (MeV).
"""
import numpy as np
np.random.seed(20780458)

sectors = {
    "geladene Leptonen (e,mu,tau)": [0.5110, 105.66, 1776.86],   # gut bestimmt
    "up-Quarks   (u,c,t)":          [2.2, 1270.0, 172500.0],     # MS-bar, laufen!
    "down-Quarks (d,s,b)":          [4.7, 95.0, 4180.0],         # MS-bar, laufen!
}

def Q_of(ms):
    ms = np.array(ms, float); s = np.sqrt(ms)
    return ms.sum() / s.sum()**2

print(f"{'Sektor':32s}  {'Q':8s} {'r=sqrt(6Q-2)':14s} Lage")
for name, ms in sectors.items():
    q = Q_of(ms); r = np.sqrt(6*q - 2)
    lage = "SPEZIELL: r=sqrt(2)" if abs(q-2/3) < 5e-3 else "nicht speziell"
    print(f"{name:32s}  {q:.4f}  {r:.4f}         {lage}")

print()
print(f"Referenz Leptonen exakt: Q = 2/3 = {2/3:.6f},  r = sqrt(2) = {np.sqrt(2):.6f}")
print(f"Dictionary: Q = 1/3 + r^2/6  ->  r=sqrt(2) gibt Q=2/3 exakt: {1/3 + 2/6:.6f}")
print()
print("Neutrinos: Delta m^2_21 = 7.5e-5 eV^2, Delta m^2_31 = 2.5e-3 eV^2 (gemessen).")
print("           absolute Massen + Ordnung unbekannt  ->  Q NICHT bildbar.")
print()
print("Befund: nur die geladenen Leptonen sitzen am speziellen Punkt r=sqrt(2);")
print("        die Quark-r sind nicht erkennbar besonders und skalenabhaengig.")
