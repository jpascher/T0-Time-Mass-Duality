#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dok 290 -- "Buchhaltung" heisst notwendig, nicht entbehrlich.

Der dimensionslose Zaehlwert (log2 M, Entropie ln2) ist primaer und in jedem
Einheitensystem gleich. SI trennt Temperatur (K), Energie (J), Zeit (s) in
eigene Einheiten; sobald thermodynamisch GERECHNET wird -- und das geschieht in
SI --, ist kB die unverzichtbare Umrechnung K->J (wie hbar, c fuer E0=hbar*c/L).
In natuerlichen Einheiten (kB=hbar=c=1) sind die Kosten reine Zahlen; SI fuehrt
die Einheitenwaende ein, und kB, hbar, c sind deren Moertel: ontologisch
sekundaer, operativ unverzichtbar.

numpy-only, seed 20780458.
"""
import numpy as np
np.random.seed(20780458)

hbar = 1.054571817e-34
c    = 2.99792458e8
kB   = 1.380649e-23
ln2  = np.log(2)

print("DIMENSIONSLOS (primaer, in jedem Einheitensystem gleich):")
print(f"  1 Bit -> Information log2(2) = 1 Bit ; Entropie ln2 = {ln2:.6f} (nat)")
print()
print("NATUERLICHE EINHEITEN (kB=hbar=c=1) -- Kosten sind reine Zahlen:")
print("  Landauer-Loeschkosten = T*ln2   (T als Energie)")
print("  Flip-Zeit             = 1/E0    (E0 als Energie)")
print()
print("SI-EINHEITEN -- getrennte Einheiten K, J, s -> Buchhaltung NOTWENDIG:")
T = 300; L = 1e-9; E0 = hbar*c/L
print(f"  Loeschwaerme Q = kB*T*ln2 = {kB*T*ln2:.3e} J    (kB: Bruecke K->J)")
print(f"  Entropie     S = kB*ln2   = {kB*ln2:.3e} J/K")
print(f"  Flip-Zeit    T~ = hbar/E0 = {hbar/E0:.3e} s     (hbar,c: E0=hbar*c/L)")
print()
print("Probe: ohne kB stuende Q in 'K' statt J -- in SI sinnlos. Die dimensionslose")
print(f"Zahl ln2={ln2:.4f} ist in beiden Systemen identisch; nur die Einheiten-Bruecke")
print("kB,hbar,c kommt hinzu.")
print()
print("Befund: 'Buchhaltung' = notwendige SI-Umrechnung, NICHT entbehrlich. Primaer")
print("        bleibt der dimensionslose Zaehlwert; kB,hbar,c sind ontologisch sekundaer,")
print("        aber sobald (thermodynamisch) in SI gerechnet wird, unverzichtbar.")
