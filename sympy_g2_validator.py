#!/usr/bin/env python3
# sympy_g2_validator.py: SymPy-Validator für g-2-Formeln (aus T0_g2-erweiterung-4_De.tex)
# Überprüft Parameter & Abweichungen zu PDG 2024

import argparse
import sympy as sp

# PDG-Referenzen (CODATA 2025)
pdg_a_p = sp.Rational(1792847, 1000000)  # 1.792847
pdg_m_p = sp.Rational(938, 1000)  # 0.938 GeV

# T0-Formeln
xi = sp.Rational(4, 30000)
D_f = 3 - xi
K_frak = 1 - 100 * xi
E_0 = 1 / xi
m_T = sp.Rational(522, 100)
alpha_s = sp.Rational(118, 1000)
N_c = 3
p = sp.Rational(-2, 3)
F_dual = 1 / (1 + (xi * E_0 / m_T)**p)
K_QCD = K_frak * sp.exp(-xi * N_c)

def validate_g2(m=sp.Rational(912, 1000), scale=1000):  # ML-Masse 0.912
    a_t0 = (alpha_s * K_QCD**2 * m**2 / (48 * sp.pi**2 * m_T**2)) * N_c * F_dual * scale
    sigma = float((a_t0 - pdg_a_p).evalf() / sp.Rational(43, 1000000))  # Unsicherheit 43e-6
    return float(a_t0.evalf()), abs(sigma)

def full_validation():
    print(f"ξ: {xi.evalf(10)}")
    print(f"D_f: {D_f.evalf(10)}")
    print(f"K_frak: {K_frak.evalf(6)}")
    print(f"K_QCD: {K_QCD.evalf(6)}")
    print(f"F_dual: {F_dual.evalf(6)}")
    a_p, sig = validate_g2()
    print(f"a_p (T0): {a_p:.3f}, σ zu PDG: ~{sig:.1f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SymPy G2 Validator")
    parser.add_argument("--full", action="store_true", help="Vollständige Validierung")
    args = parser.parse_args()
    
    if args.full:
        full_validation()
    else:
        print("SymPy Validator: Führe --full für Checks aus.")