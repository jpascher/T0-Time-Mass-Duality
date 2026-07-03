#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
delta als golden gedaempfte zweite Harmonische -- der Betrags-Sektor, so weit die
Struktur traegt. Rein FFGFT-seitig.

Befunde:
  1. delta* (theta*=2/9 bei chi=pi/2) = 0.2389 < 1 -> DAEMPFUNGS-Regime (phi^-n, Zerfall).
  2. Exponent 3 = D: einzelne dekompaktifizierte 3'-Rekursion gaebe 1/phi^1 (159% daneben);
     erst D=3 Dimensionen (volles kompaktes T^4) geben 1/phi^3.
  3. xi-Daempfungs-Rekursion r(k+1)=r(k)(1-xi), r(0)=D_f/3 (Dok 275): passiert 1/phi bei
     3609, 1/phi^3 bei 3x3609; delta* ~89 Schritte davor (Ueberschuss +1.187%, von oben).
  4. Ueberschuss ist NICHT K_frak: Dok 133 (D_eff/3)^(D_eff/2) gibt Faktor ~100 (1.333%),
     delta braucht ~89*xi (1.187%). 89-Schritt-Offset OFFEN (Dok 275 fixiert Tiefe nicht).

numpy-only, seed 20780458.
"""
import numpy as np
np.random.seed(20780458)
xi=4/30000; phi=(1+np.sqrt(5))/2; dstar=0.238870980080; g3=1/phi**3

print("1) Daempfung, nicht Verstaerkung")
print(f"   delta* = {dstar:.6f} < 1  -> phi^-n (Zerfall).  1/phi^3 = {g3:.6f}")
print(f"   delta* liegt {100*(dstar-g3)/g3:+.3f}% UEBER dem Attraktor -> Naeherung von oben.")
print()
print("2) Exponent = D (volles kompaktes T^4, nicht dekompaktifiziert)")
for n,lab in [(1,'1 (einzelne 3prime, dekompakt.)'),(3,'3 (D=3, volles T^4)'),(4,'4')]:
    v=1/phi**n; print(f"   1/phi^{n} [{lab:30s}] = {v:.4f}  Abw {100*abs(dstar-v)/dstar:5.1f}%")
print("   -> nur n=3 passt; einzelne Rekursion (n=1) 159% daneben.")
print()
print("3) xi-Daempfungs-Rekursion (Dok 275)")
Df=3-xi; r0=Df/3
depth=lambda c:(np.log(r0)-np.log(c))/(-np.log(1-xi))
print(f"   r(k+1)=r(k)(1-xi), r(0)=D_f/3={r0:.6f}")
print(f"   1/phi   bei Tiefe {depth(1/phi):.1f}  (~3609 = ln phi/xi)")
print(f"   1/phi^3 bei Tiefe {depth(g3):.1f}  (~3x3609)")
print(f"   delta*  bei Tiefe {depth(dstar):.1f}  -> {depth(g3)-depth(dstar):.0f} Schritte VOR 1/phi^3")
print()
print("4) NICHT K_frak (Dok 133)")
Kf=lambda D:(D/3)**(D/2); f133=(1-Kf(2.973))/xi
print(f"   Dok 133 (D_eff/3)^(D_eff/2), D_eff=2.973 -> Faktor {f133:.1f} (~100), = {100*(1-Kf(2.973)):.3f}%")
print(f"   delta braucht {(dstar/g3-1)/xi:.1f}*xi = {100*(dstar/g3-1):.3f}%  -> WENIGER, nicht K_frak.")
print()
print("Bilanz: Form (phi^-3), Exponent (=D), Richtung (Daempfung von oben) fest.")
print("        89-Schritt-Ueberschuss OFFEN -- nicht K_frak, Tiefe in Dok 275 nicht fixiert.")
print("        -> nicht gebucht.")
