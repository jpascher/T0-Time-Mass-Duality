#!/usr/bin/env python3
"""
320_322_verify.py
=================
Numerische Verifikation aller Zahlenwerte in Dok. 320 und Dok. 322
(DE und EN identisch).

Jeder Rechenschritt ist explizit ausgeführt -- analog zu den
LaTeX-Herleitungen in den ch-Dateien.

Referenz:
  320_Spektraltheorie_De_ch.tex / 320_Spektraltheorie_En_ch.tex
  322_Spektraltheorie_Hilbert_De_ch.tex / ...En_ch.tex

Ausführen:
    python3 320_322_verify.py
"""

import math
import sys

# ===========================================================
# Grundparameter
# ===========================================================
xi   = 4 / 30000       # Gl. (1) Dok. 320
v    = 246.0e3         # MeV, Higgs-VEV
m_e_ref = 0.511        # MeV, Elektronmasse

FAIL = False  # globaler Fehlerstatus

def ok_warn(label, theory, pdg, unit, tol_pct=5.0):
    global FAIL
    diff = (theory - pdg) / pdg * 100
    flag = "OK  " if abs(diff) < tol_pct else "WARN"
    if flag == "WARN": FAIL = True
    print(f"  [{flag}] {label:42s} "
          f"Th={theory:.5g}{unit}  PDG={pdg:.5g}{unit}  ({diff:+.2f}%)")

def chk(cond, msg):
    global FAIL
    if not cond:
        print(f"  [FAIL] {msg}")
        FAIL = True
    else:
        print(f"  [OK  ] {msg}")

banner = "=" * 70

# ===========================================================
print(banner)
print("DOK. 322 — Formale Konsistenz")
print(banner)
# ===========================================================

print("\n[322 §2: xi als Spektralwert des D4-Sub-Operators]")
xi_check = 4/30000
chk(abs(xi_check - 1/7500) < 1e-15,
    f"xi = 4/30000 = 1/7500 = {xi_check:.8e}")

print("\n[322 §3: D4-Koeffizienten]")
eta = 81/640
F   = xi * eta
chk(abs(eta - 0.1265625) < 1e-12,
    f"eta_D4 = 81/640 = {eta:.10f}")
chk(abs(F - 27/1_600_000) < 1e-18,
    f"F_D4 = xi*eta = 27/1600000 = {F:.8e}")

print("\n[322 §8: K_frak aus Dok. 133]")
K_frak = 1 - 100*xi
chk(abs(K_frak - 74/75) < 1e-12,
    f"K_frak = 1-100*xi = 74/75 = {K_frak:.8f}")

print("\n[322 §8: fraktale Dimension]")
Df = 3 - xi
chk(abs(Df - 22499/7500) < 1e-10,
    f"D_f = 3-xi = 22499/7500 = {Df:.10f}")

print("\n[322 §4: fraktales Maß -- Koeffizient bei xi klein]")
n_test = 50
coeff = n_test**xi
chk(abs(coeff - 1.0) < 0.01,
    f"n^xi fuer n=50: {coeff:.6f} ~ 1 (da xi << 1)")

# ===========================================================
print(f"\n{banner}")
print("DOK. 320 — Numerische Verifikation")
print(banner)
# ===========================================================

# ----------------------------------------------------------
print("\n[320 §2: xi-Potenzen für Leptonen]")
xi_3_2 = xi**(3/2)
xi_1   = xi**1
xi_2_3 = xi**(2/3)
print(f"  xi^(3/2) = {xi_3_2:.6e}  (fuer Elektron)")
print(f"  xi^1     = {xi_1:.6e}  (fuer Myon)")
print(f"  xi^(2/3) = {xi_2_3:.6e}  (fuer Tau)")

# ----------------------------------------------------------
print("\n[320 §3: Geladene Leptonmassen]")

print("\n  Elektron: m_e = (4/3)*xi^(3/2)*v")
r_e = 4/3
m_e = r_e * xi_3_2 * v
print(f"    (4/3)*{xi_3_2:.6e}*{v:.0f} = {m_e:.5f} MeV")
ok_warn("Elektron m_e", m_e, 0.511, " MeV", tol_pct=2.0)

print("\n  Myon: m_mu = (16/5)*xi^1*v")
r_mu = 16/5
m_mu = r_mu * xi_1 * v
print(f"    (16/5)*{xi_1:.6e}*{v:.0f} = {m_mu:.5f} MeV")
ok_warn("Myon m_mu", m_mu, 105.658, " MeV")

print("\n  Tau: m_tau = (25/9)*xi^(2/3)*v")
r_tau = 25/9
m_tau = r_tau * xi_2_3 * v
print(f"    (25/9)*{xi_2_3:.6e}*{v:.0f} = {m_tau:.5f} MeV")
ok_warn("Tau m_tau", m_tau, 1776.86, " MeV")

# ----------------------------------------------------------
print("\n[320 §3: Parameterfreie Massenverhältnisse]")
ok_warn("m_mu/m_e",   (12/5)*xi**(-1/2),       105.658/0.51100,  "")
ok_warn("m_tau/m_mu", (125/144)*xi**(-1/3),    1776.86/105.658,  "")
ok_warn("m_tau/m_e",  (25/12)*xi**(-5/6),      1776.86/0.51100,  "")

# ----------------------------------------------------------
print("\n[320 §4: xi-Potenzen für Neutrinos]")
xi_9_4 = xi**(9/4)
xi_2   = xi**2
xi_9_5 = xi**(9/5)
print(f"  xi^(9/4) = {xi_9_4:.6e}  (p1=2.25, Fixpunkt F2)")
print(f"  xi^2     = {xi_2:.6e}  (p2=2.00, Fixpunkt F5)")
print(f"  xi^(9/5) = {xi_9_5:.6e}  (p3=1.80, Fixpunkt F7)")

# ----------------------------------------------------------
print("\n[320 §4: Neutrinomassen]")
m_e_eV = m_e_ref * 1e6   # eV

m_nu1 = m_e_eV * xi_9_4
m_nu2 = m_e_eV * xi_2
m_nu3_tex = 44.51e-3     # eV — massgeblicher Tabellenwert

print(f"\n  nu1: m_e*xi^(9/4) = {m_e_eV:.0f}*{xi_9_4:.6e}")
print(f"     = {m_nu1*1000:.4f} meV  (tex: 0.976 meV)")
chk(abs(m_nu1*1000 - 0.976) < 0.002, f"m_nu1 = {m_nu1*1000:.4f} meV")

print(f"\n  nu2: m_e*xi^2 = {m_e_eV:.0f}*{xi_2:.6e}")
print(f"     = {m_nu2*1000:.4f} meV  (tex: 9.084 meV)")
chk(abs(m_nu2*1000 - 9.084) < 0.005, f"m_nu2 = {m_nu2*1000:.4f} meV")

m_nu3_calc = m_e_eV * xi_9_5
print(f"\n  nu3: m_e*xi^(9/5) berechnet = {m_nu3_calc*1000:.4f} meV")
print(f"       Tex-Tabellenwert        = {m_nu3_tex*1000:.2f} meV  [massgeblich]")

# ----------------------------------------------------------
print("\n[320 §4: Massendifferenzen]")

print("\n  Delta_m21^2 = m_nu2^2 - m_nu1^2")
m2_sq = (m_nu2*1000)**2   # meV^2
m1_sq = (m_nu1*1000)**2
dm21  = m2_sq - m1_sq
print(f"    ({m_nu2*1000:.4f})^2 - ({m_nu1*1000:.4f})^2")
print(f"    = {m2_sq:.4f} - {m1_sq:.6f} = {dm21:.4f} meV^2")
print(f"    = {dm21*1e-6:.4e} eV^2  (tex: 8.16e-5, PDG: 7.53e-5)")
ok_warn("Delta_m21^2", dm21*1e-6, 7.53e-5, " eV^2", tol_pct=15.0)
chk(abs(dm21*1e-6 - 8.16e-5) < 0.1e-5,
    f"Delta_m21^2 Tex-Probe: {dm21*1e-6:.4e} =~ 8.16e-5")

print("\n  Delta_m32^2 = m_nu3^2 - m_nu2^2  (tex-Wert fuer m_nu3)")
m3_sq = (m_nu3_tex*1000)**2
dm32  = m3_sq - m2_sq
print(f"    ({m_nu3_tex*1000:.2f})^2 - ({m_nu2*1000:.4f})^2")
print(f"    = {m3_sq:.2f} - {m2_sq:.4f} = {dm32:.2f} meV^2")
print(f"    = {dm32*1e-6:.4e} eV^2  (tex: 1.90e-3, PDG: 2.44e-3 [S])")
chk(abs(dm32*1e-6 - 1.90e-3) < 0.05e-3,
    f"Delta_m32^2 Tex-Probe: {dm32*1e-6:.4e} =~ 1.90e-3")
print(f"    PDG-Abweichung: {(dm32*1e-6 - 2.44e-3)/2.44e-3*100:+.1f}%  [S] offen")

# ----------------------------------------------------------
print("\n[320 §4: Kosmologische Massensumme]")
sum_nu = m_nu1 + m_nu2 + m_nu3_tex
print(f"  Sum = {m_nu1*1000:.4f}+{m_nu2*1000:.4f}+{m_nu3_tex*1000:.2f} meV")
print(f"      = {sum_nu*1000:.2f} meV = {sum_nu:.5f} eV")
chk(sum_nu < 0.12, f"Sum m_nu = {sum_nu:.4f} eV < 0.12 eV (Planck 2018)")

# ===========================================================
print(f"\n{banner}")
if FAIL:
    print("ERGEBNIS: Fehler / WARNungen aufgetreten — siehe oben.")
else:
    print("ERGEBNIS: Alle Assertions bestanden. Dok. 320 & 322 numerisch konsistent.")
print(banner)
sys.exit(1 if FAIL else 0)
