#!/usr/bin/env python3
# ============================================================================
# Dok 268 / Schritt 17.1 -- Die naive C_ell-Bessel-Projektion ist UNZUREICHEND
#
# Zeigt: C_ell = sum_n N_BE * |j_ell(k_obs * D_A)|^2 reproduziert {3,18,42,78}
# NICHT. Das Spektrum waescht zu einem Quasi-Kontinuum aus, dominiert von den
# niedrigsten Moden. Damit ist die fruehere P30-Aussage ("machbare Rechnung,
# kein prinzipielles Hindernis") zurueckgenommen.
#
# Autor: Johann Pascher / Juni 2026
# ============================================================================
import numpy as np
from scipy.special import spherical_jn
from collections import defaultdict

NMAX2 = 90
R = int(np.sqrt(NMAX2)) + 1
modes = defaultdict(list)
for n1 in range(-R, R+1):
 for n2 in range(-R, R+1):
  for n3 in range(-R, R+1):
   for n4 in range(-R, R+1):
    s = n1*n1+n2*n2+n3*n3+n4*n4
    if 1 <= s <= NMAX2: modes[s].append((n1, n2, n3))

# Skala so dass die (1,1,1)-Mode (k^2=3) bei ell~220 landet
DA_over_L = 220.0/np.sqrt(3)
ells = np.arange(50, 1300, 4)
Cl = np.zeros_like(ells, dtype=float)
for m, lst in modes.items():
    Nbe = 1.0/(np.exp(np.sqrt(m))-1)
    for (n1, n2, n3) in lst:
        k3 = np.sqrt(n1*n1+n2*n2+n3*n3)
        if k3 == 0: continue
        Cl += Nbe*(spherical_jn(ells, k3*DA_over_L)**2)
Cl /= Cl.max()

imax = np.argmax(Cl)
print("=== Naive C_ell-Bessel-Projektion ===")
print(f"  Staerkster Peak bei ell = {ells[imax]} (entspricht |n|^2 ~ {3*(ells[imax]/220)**2:.1f})")
print(f"  Erwartet (falls {{3,18,42,78}} reproduziert): ell ~ 220, 537, 810, 1120")
# Region |n|^2=30 -> ell~696
reg = [(l, c) for l, c in zip(ells, Cl) if 660 <= l <= 730]
print(f"  Region ell=660-730 (|n|^2=30): C_ell ~ {np.mean([c for _, c in reg]):.3f} (schwach, kein Peak)")
print("  -> Ergebnis: Quasi-Kontinuum, dominiert von niedrigen Moden.")
print("     Die naive Bessel-Summe selektiert die Akustikpeaks NICHT.")
print("     Es fehlt eine physikalische Quell-/Fensterfunktion (P30 offen).")
