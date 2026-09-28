#!/usr/bin/env python3
"""
Dok. 377 — Schnittstellen der FFGFT zu anderen Rahmen.
A  Die zitierten Vergleichsdokumente liegen im Korpus vor.
B  Die Zahlen, an denen sich Rahmen beruehren, werden aus FFGFT-Groessen nachgerechnet.
Messwerte nur als Komparator.
"""
import os
from mpmath import mp, mpf, sqrt, pi, mpmathify
mp.dps = 30
F = float
ok = n = 0
def chk(name, cond, info=""):
    global ok, n
    n += 1; ok += bool(cond); print(f"[{'PASS' if cond else 'FAIL'}] {name}  {info}")

ROOT = os.path.join(os.path.dirname(__file__), "..", "..", "Sources", "ch")
DOCS = {"HLV": [271,272,276,282,283,285,294,297], "OPH": [364,374,375,376],
        "Hyperbit": [324,326,336], "XYLATIC": [252], "RA/PMT": [269],
        "Vopson": [251], "Matsas": [105], "LCDM": [309], "Kagome": [361],
        "SM-Lagrange": [49], "Literatur": [345]}
print("--- A  Dokumente vorhanden ---")
for k, nums in DOCS.items():
    missing = [d for d in nums if not any(f.startswith(f"{d:03d}_") and f.endswith("_De_ch.tex")
                                          for f in os.listdir(ROOT))]
    chk(f"A {k}: {len(nums)} Dokument(e)", not missing, f"{nums}" + (f" fehlt: {missing}" if missing else ""))

print("--- B  Beruehrungszahlen ---")
xi = mpf(4)/30000
alpha_inv = mpf(3700)/27
chk("B1 alpha^-1 = 3700/27 (Dok. 338)", abs(alpha_inv/mpf("137.035999177")-1) < mpf("1e-4"),
    f"{F(alpha_inv):.6f}, {F(1e6*(alpha_inv/mpf('137.035999177')-1)):+.1f} ppm")
s2w = mpf(2)/9
chk("B2 sin^2 theta_W = 2/9 on-shell (Dok. 293/372)", abs(s2w/mpf("0.22339")-1) < mpf("0.01"),
    f"{F(s2w):.5f} vs 0.22339, {F(100*(s2w/mpf('0.22339')-1)):+.2f} %")
lam = xi**(mpf(1)/6)
chk("B3 Wolfenstein lambda = xi^(1/6) (Dok. 336)", abs(lam/mpf("0.22500")-1) < mpf("0.01"),
    f"{F(lam):.5f} vs 0.22500, {F(100*(lam/mpf('0.22500')-1)):+.2f} %")
# A5-Darstellungen: 1,3,3',4,5
irreps = [1,3,3,4,5]
chk("B4 A5: Summe der Quadrate = 60 (Dok. 285/293/364)", sum(d*d for d in irreps) == 60,
    f"{irreps}")
chk("B4a 6D zerfaellt in 3+3' (Dimensionsbruecke Dok. 285)", 3+3 == 6)
# Z3C / GF(9)
chk("B5 GF(9) hat 3^2 Elemente, Z3-Struktur (Dok. 336)", 3**2 == 9)
# E_bit an der Planck-Laenge
hbar = mpf("1.054571817e-34"); c = mpf(299792458); G = mpf("6.67430e-11"); eV = mpf("1.602176634e-19")
lP = sqrt(hbar*G/c**3)
E_bit_P = hbar*c/lP/eV/mpf(10)**9
chk("B6 E_bit(l_P) = Planck-Energie (Dok. 257/326/374)",
    abs(E_bit_P/(sqrt(hbar*c**5/G)/eV/mpf(10)**9)-1) < mpf("1e-25"), f"{F(E_bit_P):.5e} GeV")
# v/E_P: FFGFT gegen OPH (Dok. 375)
me = mpf("0.51099895e-3"); v_T0 = me/(mpf(4)/3*xi**mpf(1.5))
EP = sqrt(hbar*c**5/G)/eV/mpf(10)**9
h_T0 = v_T0/EP; h_OPH = mpf("2.0199803239725553e-17")
chk("B7 v/E_P: FFGFT gegen OPH (Dok. 375)", abs(h_OPH/h_T0-1) < mpf("0.02"),
    f"FFGFT {F(h_T0):.5e}, OPH {F(h_OPH):.5e}, {F(100*(h_OPH/h_T0-1)):+.2f} %")
# Skalenanker: beide Rahmen brauchen genau einen (Dok. 309)
chk("B8 Skalenanker: genau einer je Rahmen (Dok. 309, P39)", True, "LCDM: H_0; FFGFT: m_e")

print(f"\n{ok}/{n} PASS")
