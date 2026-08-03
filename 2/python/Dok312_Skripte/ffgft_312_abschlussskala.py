#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FFGFT Dok. 312 — Die Abschlussskala
Verifikation der Lambda*-Kette (bedingt auf P20: Exponent 10).

Alle Aussagen [K|P20]: reproduzierbar aus xi, lambda_e_bar und
Naturkonstanten (CODATA/SI). Keine Fits. kappa wird berechnet,
aber NICHT geschlossen (offen, Kap. 5B).
"""

from math import pi, log10

# ---------------------------------------------------------------
# Eingaben
# ---------------------------------------------------------------
XI       = 4 / 30000                  # [SETZUNG, P33]
C        = 2.99792458e8               # m/s (exakt, SI)
LAM_E    = 3.8615926796e-13           # m, red. Compton-WL Elektron (Kammerton)
L_P      = 1.616255e-35               # m, Planck-Laenge
MPC      = 3.0856775814913673e22      # m
LAM_OBS  = 1.1056e-52                 # 1/m^2, Planck 2018 (Lambda_obs)
A0_RAR   = 1.2e-10                    # m/s^2, empirische MOND/RAR-Skala

N_EXP    = 10                         # [SETZUNG, P20] — nicht hergeleitet

# ---------------------------------------------------------------
# Kette [K|P20]
# ---------------------------------------------------------------
H0 = (pi / 2) * C * XI**N_EXP / LAM_E            # 1/s
H0_kmsmpc = H0 * MPC / 1000
R_H = C / H0                                      # m
LAM_STAR = 1 / R_H**2                             # 1/m^2

print("=== Dok. 312 — Abschlussskala: Verifikation ===")
print(f"H0            = {H0:.6e} 1/s  = {H0_kmsmpc:.2f} km/s/Mpc")
print(f"R_H           = {R_H:.6e} m")
print(f"Lambda*       = 1/R_H^2 = {LAM_STAR:.6e} 1/m^2   [K|P20]")

# Identitaetstest: Lambda* == (pi/2)^2 xi^20 / lam_e^2
lhs = LAM_STAR
rhs = (pi / 2)**2 * XI**(2 * N_EXP) / LAM_E**2
assert abs(lhs - rhs) / lhs < 1e-12, "Kettenidentitaet verletzt"
print(f"Identitaet    Lambda* = (pi/2)^2 xi^20 / lam_e^2 : OK "
      f"(rel. Abw. {abs(lhs-rhs)/lhs:.1e})")

# ---------------------------------------------------------------
# Dimensionslose Form
# ---------------------------------------------------------------
diml = LAM_STAR * LAM_E**2
print(f"\nLambda* lam_e^2 = {diml:.6e}  (= (pi/2)^2 xi^20)   [K|P20]")

# ---------------------------------------------------------------
# Strukturzerlegung des 10^122-Problems
# ---------------------------------------------------------------
lam_lp2 = LAM_STAR * L_P**2
dex_xi   = 2 * N_EXP * log10(XI)
dex_comp = 2 * log10(L_P / LAM_E)
dex_geo  = 2 * log10(pi / 2)
print(f"\nLambda* l_P^2  = {lam_lp2:.4e}  = 10^{log10(lam_lp2):.2f}")
print(f"  Zerlegung [dex]:  xi^20 -> {dex_xi:+.2f}   "
      f"(l_P/lam_e)^2 -> {dex_comp:+.2f}   (pi/2)^2 -> {dex_geo:+.2f}")
print(f"  Summe             {dex_xi + dex_comp + dex_geo:+.2f}   [K|P20]")

# ---------------------------------------------------------------
# kappa — berechnet, NICHT geschlossen
# ---------------------------------------------------------------
kappa = LAM_OBS * R_H**2
print(f"\nkappa = Lambda_obs * R_H^2 = {kappa:.3f}   [OFFEN — kein Fit]")
print(f"  (Vergleich LCDM: 3*Omega_L ~ {3*0.6889:.3f} bei H0_Planck)")

# ---------------------------------------------------------------
# Querverankerung a0 (Dok. 308)
# ---------------------------------------------------------------
print(f"\nc*H0          = {C*H0:.3e} m/s^2")
print(f"c*H0/(2 pi)   = {C*H0/(2*pi):.3e} m/s^2   vs. a0_RAR = {A0_RAR:.1e}")
print(f"Verhaeltnis   = {(C*H0/(2*pi))/A0_RAR:.3f}")

# ---------------------------------------------------------------
# Lokaler Sektor: Hierarchie-Check
# ---------------------------------------------------------------
# Kruemmungsskala am Sonnenrand ~ GM/(c^2 r^3) ~ 1e-27 1/m^2 (Groessenordnung)
K_sun = 1e-27
print(f"\nLokale Kruemmung (Sonnenrand, GO) ~ {K_sun:.0e} 1/m^2")
print(f"Lambda*/K_sun ~ {LAM_STAR/K_sun:.1e}  -> lokal vernachlaessigbar [K]")
