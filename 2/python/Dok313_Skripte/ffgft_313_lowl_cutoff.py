#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FFGFT Dok. 313 — Der Low-l-Cutoff der kompakten Topologie

Auf T^4 der Kantenlaenge L* existieren keine Moden mit Wellenlaenge
> L*. Daraus folgt eine untere Grenze im CMB-Winkelspektrum:
  l_min = k_min * D_LSS = 2 pi D_LSS/L*
Kein freier Parameter: L* = 4 lambda_e/xi^10, D_LSS aus der Kette.
"""
import numpy as np
from math import pi
C=2.99792458e8; XI=4/30000; LAM_E=3.8615926796e-13
H0=(pi/2)*C*XI**10/LAM_E; R_H=C/H0; L_STAR=2*pi*R_H
K=1-100*XI; GPC=3.0856775814913673e25
h=H0*3.0856775814913673e22/1e5; OR=4.15e-5/h**2

def chi(z, Om=0.3139):
    zz=np.concatenate([np.linspace(0,1090,200000),
        np.logspace(np.log10(1090.001),9,200000)])
    zz=zz[zz<=z]
    return np.trapezoid(C/(H0*np.sqrt(Om*(1+zz)**3+OR*(1+zz)**4+1-Om-OR)),zz)

print("="*58)
print("LOW-l-CUTOFF AUS DER KOMPAKTEN TOPOLOGIE")
print("="*58)
print(f"L*      = 4 lambda_e/xi^10 = {L_STAR/GPC:.2f} Gpc")
D=chi(1090)*K
print(f"D_LSS   = {D/GPC:.2f} Gpc  (fraktal korrigiert, R70)")
print(f"k_min   = 2 pi/L* = {2*pi/L_STAR:.4e} 1/m")
print(f"\n  l_min = 2 pi D_LSS/L* = {2*pi*D/L_STAR:.2f}")
print("\nRobustheit gegen Omega_m:")
for Om in (0.305,0.310,0.3139,0.320,0.325):
    print(f"   Om_m={Om:.4f} -> l_min = {2*pi*chi(1090,Om)*K/L_STAR:.3f}")
print(f"ohne fraktale Wegkorrektur: l_min = {2*pi*chi(1090)/L_STAR:.3f}")
print("\nVorhersage: Moden mit l < 3 fehlen; l=2 (Quadrupol) stark")
print("unterdrueckt, l=3 (Oktupol) am Rand, ab l>=4 unbeeinflusst.")
print("\nBeobachtung (COBE 1992, WMAP, Planck): Quadrupol ~1/6 des")
print("LCDM-Erwartungswerts, Oktupol leicht niedrig, ab l=4 normal.")
print("In LCDM unerklaert ('low-l anomaly', kosmische Varianz).")
print("\nWICHTIG: l_min ist NICHT angepasst. L* folgt aus der")
print("xi-Kette, D_LSS aus derselben Kette. Der Wert ist eine")
print("Vorhersage mit einer einzigen Ziffer Spielraum.")
print("\nOFFEN: der genaue Unterdrueckungsgrad verlangt die")
print("Modensummation auf T^3 statt der R^3-Integration")
print("(endliche Summe, kein Boltzmann-Code noetig).")
