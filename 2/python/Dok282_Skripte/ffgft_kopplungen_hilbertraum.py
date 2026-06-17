#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FFGFT -- the couplings alpha and G as Hilbert-space quantities
==============================================================
The recipe of Doc. 282 says: every quantity is an eigenvalue, an eigenvalue
relation, or an eigenbasis overlap on H. This script applies that recipe to the
COUPLINGS, so they are computed via the Hilbert-space mapping -- not as a
separate xi-route formula, but from the SAME Z3 operator that gives the masses.

Construction.
  Build the lepton mass operator from the two pure numbers and the scale:
      S = circ(t0, t1, t2),  t0 = M,  t1 = (M r / 2) e^{i theta},  t2 = conj(t1),
      r = sqrt(2)   (Koide Q = 2/3),
      theta = 2/9   (the structural angle),
      M = mean_j sqrt(m_j)  (the scale 1/T~ of the lepton sector).
  Its eigenvalues are  lambda_j = sqrt(m_j)  (in MeV^{1/2}); squaring gives the
  charged-lepton masses.  M^2 = M_T is the sector mass scale (energy).

alpha as an eigenvalue relation.
  In the xi-route alpha = xi (E0/MeV)^2 with E0 = sqrt(m_e m_mu).  In the
  Hilbert-space picture E0 is NOT a separate input: it is the product of the two
  smaller eigenvalues of S,
      E0 = lambda_e * lambda_mu = sqrt(m_e m_mu),
      alpha = xi (lambda_e lambda_mu / MeV)^2.
  So alpha is literally an eigenvalue relation of the same operator -- the recipe
  applied to a coupling.  Honest accuracy: the operator/geometric value gives
  1/alpha = 138.9 (+1.4%); the corpus uses E0 = 7.398 MeV -> 1/alpha = 137.04,
  i.e. the last ~1% sits in the precise value of E0 (radiative-correction level).

G in the Hilbert-space picture.
  G enters through the same xi via the T0 fundamental relation xi = 2 sqrt(G m)
  => G = xi^2/(4m).  The Hilbert-space mapping supplies the SCALE: m is the
  operator scale M_T = M^2 = 1/T~ of the lepton sector.  The structural origin is
  thus fixed by the operator + xi; only the SI realisation of G (dimensionful,
  via l_P, c, hbar) is the involved step, carried out in calc-o.  This script
  reports the structural/dimensionless content, not the SI number for G.

numpy only.
"""

import numpy as np

# ---- inputs: two pure numbers + the measured lepton scale --------------------
r = np.sqrt(2.0)          # Koide Q = 2/3
theta = 2.0 / 9.0         # structural angle
xi = 4.0 / 30000.0        # fractal primitive of the coupling sector
MeV = 1.0                 # work in MeV; lambda_j in MeV^{1/2}

m_e, m_mu, m_tau = 0.51099895, 105.6583755, 1776.86  # MeV (for the scale only)
M = np.mean(np.sqrt([m_e, m_mu, m_tau]))             # = 1/T~ , in MeV^{1/2}

# ---- build the Z3 operator and read its spectrum -----------------------------
t0 = M
t1 = (M * r / 2.0) * np.exp(1j * theta)
t2 = np.conj(t1)
S = np.array([[t0, t1, t2],
              [t2, t0, t1],
              [t1, t2, t0]], dtype=complex)

lam = np.sort(np.linalg.eigvalsh(S))      # lambda_j = sqrt(m_j), MeV^{1/2}
lam_e, lam_mu, lam_tau = lam              # ascending: e, mu, tau
masses = lam ** 2

print("=" * 70)
print("FFGFT couplings via the Hilbert-space mapping (one Z3 operator)")
print("=" * 70)
print(f"  built from r=sqrt2={r:.4f}, theta=2/9={theta:.5f}, scale M=1/T~={M:.4f} MeV^1/2")
print(f"  eigenvalues lambda_j = sqrt(m_j) [MeV^1/2]: {np.round(lam,5)}")
print(f"  -> masses m_j = lambda_j^2 [MeV]          : {np.round(masses,4)}")
print(f"  sector mass scale M_T = M^2 = {M**2:.2f} MeV")

# ---- alpha as an eigenvalue relation -----------------------------------------
E0_op = lam_e * lam_mu                     # = sqrt(m_e m_mu)
alpha_op = xi * (E0_op / MeV) ** 2
print("\n  ALPHA  (eigenvalue relation on H):")
print(f"    E0 = lambda_e * lambda_mu = sqrt(m_e m_mu) = {E0_op:.4f} MeV")
print(f"    alpha = xi (E0/MeV)^2 = {alpha_op:.6e}  ->  1/alpha = {1/alpha_op:.3f}")
print(f"    (operator/geom value; corpus tune E0=7.398 -> 1/alpha=137.04)")

# ---- G: structural content from the same operator scale ----------------------
M_T = M ** 2                               # MeV  (= 1/T~ as an energy)
print("\n  G  (structural, via xi = 2 sqrt(G m), m = operator scale M_T):")
print(f"    G = xi^2 / (4 m),  m = M_T = {M_T:.2f} MeV")
print(f"    G_struct(dimensionless core) = xi^2/(4 M_T) in natural units;")
print(f"    the SI value of G follows through the (involved) l_P,c,hbar")
print(f"    conversion -- carried out in calc-o, not repeated here.")

print("""
SUMMARY
  * alpha is computed inside the Hilbert space: a product of two operator
    eigenvalues, scaled by xi. Same operator as the masses, built from the two
    pure numbers (sqrt2, 2/9). Accuracy 1/alpha = 138.9 (geom) .. 137.04 (corpus E0).
  * G enters through the same xi; the operator supplies the scale M_T = 1/T~.
    The structural origin is fixed; only the SI conversion of G is the hard part.
  => masses AND couplings are read off ONE Z3 operator -- the recipe of Doc. 282
     extended from the masses to the couplings.
""")
