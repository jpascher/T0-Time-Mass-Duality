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
  applied to a coupling.  Honest accuracy: the bare operator value gives
  1/alpha = 138.9 (+1.35%); the corpus value E0 = 7.398 MeV is NOT a tune but
  7.348/sqrt(K_frak) with K_frak = 1 - 100 xi (R72), giving 1/alpha = 137.04.
  The 1.35% gap is the factor K_frak (K_frak * 138.91 = 137.06). The agreement
  with the measured alpha is a property of the anchor E0, not an independent
  prediction (R135).

G in the Hilbert-space picture.
  G enters through the same xi via the T0 fundamental relation xi = 2 sqrt(G m)
  => G = xi^2/(4m).  Caution (R141): xi^2/(4m) has dimension [E^-1], while
  G = l_P^2 has [E^-2]; the SI value is G = xi^2/(4 m_e) * C_conv * K_frak.
  The Hilbert-space mapping supplies the SCALE: m is the
  operator scale M_T = M^2 = 1/T~ of the lepton sector.  The structural origin is
  thus fixed by the operator + xi; only the SI realisation of G (dimensionful,
  via l_P, c, hbar) is the involved step, carried out in calc-o.  This script
  reports the structural/dimensionless content, not the SI number for G.

numpy only.

Aktualisiert am 1.10.2026: "corpus tune E0 = 7.398" / "radiative-correction level"
ersetzt -- 7.398 = 7.348/sqrt(K_frak) ist nicht getunt, die Luecke 1.35 % ist der
Faktor K_frak = 1 - 100 xi (K_frak * 138.91 = 137.06; Pruefung ergaenzt); die
alpha-Uebereinstimmung ist eine Eigenschaft des Ankers E0, keine unabhaengige
Vorhersage; G-Zeile mit Dimensions-/C_conv-Hinweis ([E^-1] vs. [E^-2]) (vgl.
Dok. 282 bzw. Dok. 190, R72/R135/R141).
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
K_frak = 1.0 - 100.0 * xi
E0_corp = E0_op / np.sqrt(K_frak)          # = 7.348/sqrt(K_frak) = 7.398 MeV
inv_alpha_corp = 1.0 / (xi * E0_corp ** 2)
print(f"    (bare operator value; with K_frak = 1-100 xi: E0 = {E0_op:.3f}/sqrt(K_frak)")
print(f"     = {E0_corp:.3f} MeV -> 1/alpha = {inv_alpha_corp:.2f}; K_frak * {1/alpha_op:.2f} = {K_frak/alpha_op:.2f})")
print(f"    gap {100*(1/alpha_op/inv_alpha_corp-1):.2f}% = factor K_frak (100 xi = {100*100*xi:.2f}%), not a tune;")
print(f"    agreement with measured alpha is a property of the anchor E0 (R135)")
# Corpus-level check with the measured lepton masses (Dok. 282 note, R72):
E0_meas = np.sqrt(m_e * m_mu)                        # 7.348 MeV
inv_alpha_bare = 1.0 / (xi * E0_meas ** 2)           # 138.91
print(f"    measured masses: sqrt(m_e m_mu) = {E0_meas:.3f} MeV -> 1/alpha = {inv_alpha_bare:.2f};"
      f" K_frak * {inv_alpha_bare:.2f} = {K_frak*inv_alpha_bare:.2f};"
      f" E0 = {E0_meas/np.sqrt(K_frak):.3f} MeV")
assert abs(E0_meas - 7.348) < 1e-3 and abs(E0_meas / np.sqrt(K_frak) - 7.398) < 1e-3
assert abs(inv_alpha_bare - 138.91) < 0.01 and abs(K_frak * inv_alpha_bare - 137.06) < 0.01
assert abs(1.0 / (xi * 7.398 ** 2) - 137.04) < 0.01   # rounded corpus E0
assert abs(inv_alpha_corp - 137.06) < 0.05            # operator route, same factor

# ---- G: structural content from the same operator scale ----------------------
M_T = M ** 2                               # MeV  (= 1/T~ as an energy)
print("\n  G  (structural, via xi = 2 sqrt(G m), m = operator scale M_T):")
print(f"    G = xi^2 / (4 m),  m = M_T = {M_T:.2f} MeV")
print(f"    G_struct = xi^2/(4 M_T) has dimension [E^-1], G = l_P^2 has [E^-2]:")
print(f"    the SI value is G = xi^2/(4 m_e) * C_conv * K_frak (R141) -- the")
print(f"    conversion C_conv carries the remaining dimension; not repeated here.")

print("""
SUMMARY
  * alpha is computed inside the Hilbert space: a product of two operator
    eigenvalues, scaled by xi. Same operator as the masses, built from the two
    pure numbers (sqrt2, 2/9). 1/alpha = 138.9 (bare) -> 137.04 with K_frak
    (E0 = 7.348/sqrt(K_frak)); the alpha agreement is a property of the anchor
    E0, not an independent prediction (R135).
  * G enters through the same xi; the operator supplies the scale M_T = 1/T~.
    Only the form of G is fixed; xi^2/(4m) is [E^-1] vs. [E^-2] for G, the SI
    value needs C_conv (R141).
  => masses AND couplings are read off ONE Z3 operator -- the recipe of Doc. 282
     extended from the masses to the couplings.
""")
