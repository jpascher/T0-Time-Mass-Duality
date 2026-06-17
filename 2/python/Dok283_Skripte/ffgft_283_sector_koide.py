#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Doc 283, Sec. 9 -- which charge sector realises which symmetry order?
=====================================================================
The fork is 3-fold (FFGFT, r=sqrt2, Koide Q=2/3) vs 5-fold (HLV protected,
r=2/sqrt5, Koide Q=7/15). Sec. 9 claims: only the charged leptons sit at the
3-fold point; the hadrons are near-degenerate (Q ~ 1/3); NO sector realises the
5-fold point 7/15; the neutrinos cannot reach 2/3; and reaching 7/15 in a light
hadron triplet would need a heavy/light mass ratio ~12, which no real multiplet
shows. This script computes Q and r for each sector and writes sector_koide.csv.

Koide:  Q = (m1+m2+m3) / (sqrt m1 + sqrt m2 + sqrt m3)^2     (dimensionless, in [1/3,1])
Circulant map (Doc 206/282):  Q = 1/3 + r^2/6   =>   r = sqrt(6Q - 2)
  r = sqrt2   <-> Q = 2/3   (3-fold, FFGFT)
  r = 2/sqrt5 <-> Q = 7/15  (5-fold, HLV protected)
  r = 0       <-> Q = 1/3   (degenerate)

Masses in MeV (PDG-level); neutrinos in eV (units cancel in Q). numpy only.
"""
import numpy as np, csv

def koide_Q(m):
    m = np.asarray(m, float); return m.sum() / (np.sqrt(m).sum())**2
def r_of_Q(Q): return np.sqrt(max(0.0, 6*Q - 2))
def nearest(r):
    pts = {"3-fold (sqrt2)": np.sqrt(2), "5-fold (2/sqrt5)": 2/np.sqrt(5), "degenerate (0)": 0.0}
    return min(pts, key=lambda k: abs(r - pts[k]))

SECTORS = {
    "charged_leptons":   [0.51099895, 105.6583755, 1776.86],
    "up_quarks_uct":     [2.16, 1270.0, 172690.0],
    "down_quarks_dsb":   [4.67, 93.4, 4180.0],
    "vector_mesons_rho_omega_phi": [775.26, 782.66, 1019.461],
    "baryon_p_n_lambda": [938.272, 939.565, 1115.683],
    "neutrinos_NO_m1=0_eV": [0.0, 8.678e-3, 4.953e-2],   # normal ordering, lightest=0
}

rows = []
for name, m in SECTORS.items():
    Q = koide_Q(m); r = r_of_Q(Q)
    rows.append([name, *[f"{x:g}" for x in m], f"{Q:.5f}", f"{r:.5f}", nearest(r)])

with open("sector_koide.csv", "w", newline="") as f:
    wr = csv.writer(f)
    wr.writerow(["sector", "m1", "m2", "m3", "koide_Q", "r=sqrt(6Q-2)", "nearest_symmetry_point"])
    wr.writerows(rows)

print("Koide Q and circulant r per charge sector  (3-fold Q=2/3, 5-fold Q=7/15, degenerate Q=1/3)\n")
print(f"{'sector':32s}{'Q':>9s}{'r':>9s}   nearest")
for row in rows:
    print(f"{row[0]:32s}{float(row[4]):9.4f}{float(row[5]):9.4f}   {row[6]}")

# what heavy mass would the light vector-meson triplet need to reach 5-fold 7/15?
a, b = np.sqrt(775.26), np.sqrt(782.66); S2, P = a*a + b*b, a + b
Qt = 7/15
A = 1 - Qt; B = -2*Qt*P; C = S2 - Qt*P*P          # A c^2 + B c + C = 0,  c = sqrt(m3)
c = max(np.roots([A, B, C]))
m3_needed = c*c
print(f"\nFor rho/omega/phi to reach 5-fold Q=7/15, the heaviest would need "
      f"m3 ~ {m3_needed/1000:.1f} GeV (ratio {m3_needed/775.26:.1f}); the real phi is 1.02 GeV "
      f"(ratio {1019.461/775.26:.2f}).")
print("\nVERDICT: only the charged leptons sit at the 3-fold point (Q=2/3, r=sqrt2);")
print("hadrons are near-degenerate (Q~1/3); the up/down quarks miss sqrt2 either way;")
print("neutrinos top out at Q~0.584 < 2/3; and NO sector lands at the 5-fold point 7/15.")
print("The 5-fold / phi branch is geometrically real but physically unrealised.")
print("-> sector_koide.csv")
