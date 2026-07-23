#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dok 190, R61 -- Pruefskript: der Zweitparameter xi_Higgs = 1.038e-5 ist unbelegt;
dieselbe Formel ist das Higgs-Matching von xi selbst (A142 [K]). numpy-frei."""
import math

xi   = 4/30000
v    = 246.22        # GeV (Higgs-VEV)
mh   = 125.25        # GeV
lamh = mh**2 / (2*v**2)

val = lamh**2 * v**2 / (16*math.pi**3 * mh**2)

print("R61 -- xi_Higgs matching check")
print(f"  lambda_h = m_h^2/(2 v^2)          = {lamh:.6f}")
print(f"  lambda_h^2 v^2 / (16 pi^3 m_h^2)  = {val:.6e}")
print(f"  xi = 4/30000                       = {xi:.6e}")
print(f"  deviation from xi                  = {abs(val/xi-1)*100:.2f} %   (A142 [K]: matching of xi itself)")
print(f"  claimed second parameter (Doc 174) = 1.038e-05")
print(f"  ratio formula/claim                = {val/1.038e-5:.2f}   -> claim follows from NO declared input convention")
print()
print("Consequence for the Doc-174 T2 finding (per-stage decades):")
d1 = math.log10(1/xi)
print(f"  single xi: one stage = {d1:.3f} decades; 2 stages = {2*d1:.2f}; 3 stages = {3*d1:.2f}")
print(f"  measured window 9..11 decades matches no integer stage count -> finding doubly void (also post hoc, P35)")
print()
print("Authoritative form (sealed, note v1.1): Gamma ~ xi^(2 DeltaN) * omega")
print(f"  xi^2 = {xi**2:.4e}  (DeltaN=1)   xi^4 = {xi**4:.4e}  (DeltaN=2)")
