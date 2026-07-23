#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dok 190, R61 -- Pruefskript (v2): xi_Higgs = 1.038e-5 war datengetriebene
Wertauswahl; der gedruckte Wert passt nicht zur gedruckten Formel (Faktor 4 pi).
Ohne Abhaengigkeiten."""
import math

xi   = 4/30000
v    = 246.22        # GeV
mh   = 125.25        # GeV
lamh = mh**2 / (2*v**2)

f16 = lamh**2 * v**2 / (16*math.pi**3 * mh**2)   # gedruckte Formel (Dok 175)
f64 = lamh**2 * v**2 / (64*math.pi**4 * mh**2)   # entspricht dem gedruckten Wert

print("R61 -- xi_Higgs check (v2)")
print(f"  lambda_h = m_h^2/(2 v^2)              = {lamh:.6f}")
print(f"  printed formula, 16 pi^3              = {f16:.4e}   (~ xi = {xi:.4e}; A142 [K], dev {abs(f16/xi-1)*100:.1f}%)")
print(f"  same expression with 64 pi^4          = {f64:.4e}   (matches printed 1.038e-5 to {abs(f64/1.038e-5-1)*100:.2f}%)")
print(f"  ratio = {f16/f64:.4f} = 4*pi          -> extra factor nowhere derived")
print()
print("Selection check (Doc 174 table logic):")
for name, val in (("xi_par ", xi), ("xi_Higgs", 1.038e-5)):
    d = math.log10(1/val)
    print(f"  {name}: 1 stage = {d:.3f} decades; 2 stages = {2*d:.2f}  (measured window 9..11)")
print("  -> the fitting value was selected AFTER comparison with the window: post-hoc, P35, no evidence")
print()
print("Authoritative form (sealed, note v1.1): Gamma ~ xi^(2 DeltaN) * omega")
print(f"  xi^2 = {xi**2:.4e} (DeltaN=1)   xi^4 = {xi**4:.4e} (DeltaN=2)")
print("Open point (recorded, not closed): no integer stage count hits the 9..11 window with the single xi")
