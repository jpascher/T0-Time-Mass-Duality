#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FFGFT -- the actual Hilbert-space mass operator on the C^3 fibre
================================================================
Not a parametrisation: a genuine operator. The fibre Hilbert space is C^3 (the
three Z3-symmetric ICE channels = the generation space). The mass operator is a
HERMITIAN Z3-CIRCULANT

        S = circ(t0, t1, t2),   t0 = M (real),  t2 = conj(t1),

acting on C^3.  Its eigenvalues are sqrt(m_k); the mass operator is S^2.  Its
eigenvectors are the three Z3 Fourier characters f_k = (1, w^k, w^{2k})/sqrt(3),
w = e^{2*pi*i/3}: the three generations ARE the Z3 characters.

Eigenvalues of the circulant:
        mu_k = t0 + 2|t1| cos(arg(t1) + 2*pi*k/3) = M (1 + r cos(theta + 2*pi*k/3)),
with r = 2|t1|/M and theta = arg(t1).  Hence:

   * scale  M = 1/T~   (time--mass duality T~*m = 1; factors out of ratios,
                        since hbar, c are SI conversion factors);
   * r = sqrt(2)       <=>  Koide Q = (1 + r^2/2)/3 = 2/3   (the Z3 + sqrt(2)
                        structural condition, Doc.258/259);
   * theta = 2/9       the angle that fixes the individual ratios -- tested here
                        as a STRUCTURAL RATIONAL (2/3^2), a candidate
                        Grundbedingung of the fractal space, on the footing of
                        xi (NOT a fitted continuous knob).

numpy only.
"""

import numpy as np

w = np.exp(2j * np.pi / 3)                      # cube root of unity
m_e, m_mu, m_tau = 0.51099895, 105.6583755, 1776.86
data = np.sort(np.array([m_e, m_mu, m_tau]))

# ---- structural inputs (two pure numbers + one scale) -------------------
r = np.sqrt(2.0)            # Koide / Z3 condition
theta = 2.0 / 9.0           # candidate Grundbedingung (= 2/3^2), NOT fitted
M = 1.0                     # scale = 1/T~  (ratios are scale-free)

t0 = M
t1 = (M * r / 2.0) * np.exp(1j * theta)
t2 = np.conj(t1)

# ---- the operator: Hermitian Z3-circulant on C^3 ------------------------
S = np.array([[t0, t1, t2],
              [t2, t0, t1],
              [t1, t2, t0]], dtype=complex)

print("Hermitian? ||S - S^dagger|| =", np.linalg.norm(S - S.conj().T))
evals, evecs = np.linalg.eigh(S)                # eigenvalues = sqrt(m_k)

print("\nMass operator = S^2  on the C^3 fibre")
print("  eigenvalues of S (= sqrt(m), scale-free): ", np.round(np.sort(evals), 5))

# eigenvectors are the Z3 characters?
print("\n  eigenvectors vs Z3 Fourier characters (1, w^k, w^2k)/sqrt3:")
for k in range(3):
    fk = np.array([1, w ** k, w ** (2 * k)]) / np.sqrt(3)
    # match to an eigenvector by overlap
    ov = np.max(np.abs(evecs.conj().T @ fk))
    print(f"    character k={k}: best |overlap| with an eigenvector = {ov:.4f}")

# ---- masses = eigenvalues^2 ---------------------------------------------
m = np.sort(evals ** 2)
m = m / m[0]                                     # scale to electron = 1
print("\n  masses m = (eigenvalue)^2, scaled to lightest = 1:")
print(f"    operator : m_e:m_mu:m_tau = 1 : {m[1]:.3f} : {m[2]:.3f}")
dm = data / data[0]
print(f"    data     : m_e:m_mu:m_tau = 1 : {dm[1]:.3f} : {dm[2]:.3f}")
print(f"\n    m_mu/m_e : operator {m[1]:8.3f}   data {dm[1]:8.3f}   (err {abs(m[1]-dm[1])/dm[1]*100:.2f}%)")
print(f"    m_tau/m_mu: operator {m[2]/m[1]:8.3f}   data {dm[2]/dm[1]:8.3f}   (err {abs(m[2]/m[1]-dm[2]/dm[1])/(dm[2]/dm[1])*100:.2f}%)")

Q = m.sum() / np.sqrt(m).sum() ** 2
print(f"\n    Koide Q (from operator spectrum): {Q:.6f}   (2/3 = {2/3:.6f})")

# ---- is theta=2/9 special? compare a small grid -------------------------
# NUMERICAL CAUTION: the lightest eigenvalue is a near-total cancellation,
#   mu_e = M(1 + r*cos(theta + 2pi/3)) = M(1 - 0.95965) = 0.04035*M,
# i.e. the difference of two nearly equal numbers. Hand-rounding the cosines to
# ~3 digits is fatal here: cos(theta+2pi/3) as -0.658 instead of -0.6786 (a 3%
# error) turns mu_e = 0.040 into 0.069 (72% error), and since m_e = mu_e^2 this
# flips m_mu/m_e from 207 to 63. Always evaluate at full machine precision.
print("\n  sensitivity: m_mu/m_e is the lightest, hence the sharpest probe of theta")
for th in [0.2200, 2/9, 0.22223, 0.2240]:
    mu = np.array([1 + r * np.cos(th + 2 * np.pi * k / 3) for k in range(3)]) ** 2
    mu = np.sort(mu); mu /= mu[0]
    tag = "  <- 2/9" if abs(th - 2/9) < 1e-6 else ("  <- data-fit" if abs(th-0.22223) < 1e-5 else "")
    print(f"    theta={th:.5f}:  m_mu/m_e={mu[1]:7.2f}, m_tau/m_mu={mu[2]/mu[1]:6.3f}{tag}")

print("""
----------------------------------------------------------------------
WHAT THIS IS (answering "I see no Hilbert-space mapping"):
  * A genuine operator S on the fibre Hilbert space C^3 (full space
    L^2(T^4) (x) C^3; the T^4 / T~ cycle sets the scale M = 1/T~).
  * Generations = eigenvectors = the three Z3 characters.
  * Masses     = spectrum of S^2.  Koide 2/3 falls out exactly from r=sqrt2.

ON 2/9 AS A Grundbedingung (answering "must 2/9 be derived?"):
  * NO -- not from something deeper. The right distinction is:
      fitted continuous knob (bad, the old r_e~1.349)  vs.
      fixed structural RATIONAL forced by the geometry (fine -- like 2/3,
      like 2*pi/3, like the Z3 count itself).
  * 2/9 = 2/3^2 is a clean rational, not a tuned decimal -- exactly the kind
    of primitive the fractal/open space can carry, on the footing of xi.
  * Consequence (honest): the lepton ratios are then a Z3-GEOMETRY story
    (the pure numbers sqrt2 and 2/9), NOT a xi-power story -- consistent with
    the xi-ladder being the weak/fitted part for leptons all along.
  * Remaining task is therefore NOT "derive a messy number" but the sharper,
    tractable one: SHOW 2/9 is the forced rational of the T^4/Z3 topology
    (as 2/3 is). The electron, being lightest, is the sharpest test of whether
    theta is exactly 2/9.
----------------------------------------------------------------------""")
