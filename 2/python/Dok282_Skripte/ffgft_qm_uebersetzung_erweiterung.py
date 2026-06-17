#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FFGFT -- what the mass/time extension changes in the QM translation
===================================================================
The standalone QM-translation doc (Doc. 230/231/232) maps the QM OPERATIONS onto
the T^4 Hilbert space: gauge freedom = unitary equivalence, entanglement = holonomy
around cycles, Bell correlations = topological connections. We found that this
translation does NOT contain mass and time. Doc. 282 adds them: mass = the Z3
operator S on the C^3 fibre (Level 2), time = the process / CP-divisibility
structure of the loop operator (Level 1).

Question (Pascher): the QM translation is slightly incomplete -- extending it must
have some influence on the results. This script computes what actually changes,
separately for the two missing pieces.

  Part A -- MASS (the C^3 fibre). The mass operator acts on a SEPARATE tensor
            factor. We compute a genuine QM observable (CHSH/Bell, the very thing
            the bridge translates) on the base qubits, with and without the C^3
            mass fibre attached. If they agree, the mass extension does not touch
            the QM results -- it only enlarges the space and supplies the masses.

  Part B -- TIME (process / non-Markovianity). The QM bridge treats the reduced
            dynamics as time-local (unitary / Markovian). The extended translation
            carries the loop history. We compute the SAME fibre-qubit coherence
            c(t) under the time-local (Markovian) and the history-coupled
            (non-Markovian) description and report the difference.

numpy only.
"""

import numpy as np
from numpy.linalg import eigvalsh

XI = 4.0 / 30000.0
np.set_printoptions(precision=4, suppress=True)


# ============================================================================
# Part A -- MASS extension: does the C^3 fibre change a QM correlation?
# ============================================================================
def chsh_value(rho, A0, A1, B0, B1):
    """CHSH = <A0 B0> + <A0 B1> + <A1 B0> - <A1 B1> for a 2-qubit state rho."""
    def corr(A, B):
        return np.real(np.trace(rho @ np.kron(A, B)))
    return corr(A0, B0) + corr(A0, B1) + corr(A1, B0) - corr(A1, B1)


# Tsirelson-optimal CHSH on a Bell state (this is the "QM operation" the bridge maps)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
A0, A1 = sz, sx
B0 = (sz + sx) / np.sqrt(2)
B1 = (sz - sx) / np.sqrt(2)

bell = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
rho_base = np.outer(bell, bell.conj())                    # 2 qubits, base only
S_base = chsh_value(rho_base, A0, A1, B0, B1)

# Now attach the C^3 mass fibre: build the Z3 mass operator S_mass and put the
# fibre in one of its eigenstates (a generation). The full state is rho_base (x) rho_fibre.
r, theta, M = np.sqrt(2.0), 2.0 / 9.0, 1.0
t1 = (M * r / 2.0) * np.exp(1j * theta)
S_mass = np.array([[M, t1, np.conj(t1)],
                   [np.conj(t1), M, t1],
                   [t1, np.conj(t1), M]], dtype=complex)
_, evecs = np.linalg.eigh(S_mass)
fibre = evecs[:, 1]                                        # the muon generation, say
rho_fibre = np.outer(fibre, fibre.conj())
rho_full = np.kron(rho_base, rho_fibre)                    # lives on (C^2 x C^2) x C^3

# CHSH on the base qubits, evaluated in the ENLARGED space (operators (x) I_3 on fibre)
I3 = np.eye(3)
def corr_full(A, B):
    op = np.kron(np.kron(A, B), I3)
    return np.real(np.trace(rho_full @ op))
S_full = (corr_full(A0, B0) + corr_full(A0, B1)
          + corr_full(A1, B0) - corr_full(A1, B1))

print("=" * 72)
print("Part A -- MASS extension (C^3 fibre): effect on a QM correlation (CHSH)")
print("=" * 72)
print(f"  CHSH on base qubits,           QM-only translation : {S_base:.12f}")
print(f"  CHSH on base qubits, with C^3 mass fibre attached   : {S_full:.12f}")
print(f"  |difference| = {abs(S_full - S_base):.2e}   (Tsirelson 2*sqrt2 = {2*np.sqrt(2):.6f})")
print("  => the mass operator lives on a separate tensor factor; the QM result is")
print("     UNCHANGED. Mass enlarges the space and supplies masses, nothing else.")


# ============================================================================
# Part B -- TIME extension: time-local (Markovian) vs history-coupled (non-Markov)
# ============================================================================
# Bath = T^4 loop frequencies (connection-Laplacian); pure-dephasing of a qubit.
rng = np.random.default_rng(0)
omega = np.array([1.239, 1.808, 2.130, 2.236, 2.504, 2.595])   # loop freqs sqrt(lambda_k)
g = np.array([0.610, 0.862, 0.964, 1.056, 1.363, 0.862])       # couplings
t = np.linspace(0, 12, 4000)

# Non-Markovian (extended translation): full structured bath, carries history
Gamma_NM = np.array([np.sum(2 * g**2 / omega**2 * (1 - np.cos(omega * tt))) for tt in t])
c_NM = np.exp(-Gamma_NM)

# Markovian (QM-only translation): memoryless, matched on overall decoherence
gamma_M = Gamma_NM[-1] / t[-1]                            # matched: Gamma_M(t_end)=Gamma_NM(t_end)
Gamma_M = gamma_M * t
c_M = np.exp(-Gamma_M)

# BLP back-flow (sum of coherence revivals) and CP-divisibility (step multiplier)
def backflow(c):
    dc = np.diff(c)
    return float(np.sum(dc[dc > 0]))
def min_choi_eig(c):
    r = c[1:] / np.clip(c[:-1], 1e-300, None)        # step multiplier
    return float(np.min((1 - r) / 2))                # min Choi eigenvalue of the step map

print("\n" + "=" * 72)
print("Part B -- TIME extension: same loop operator, two reduced descriptions")
print("=" * 72)
print(f"  max |c_NM(t) - c_M(t)| over the run         : {np.max(np.abs(c_NM - c_M)):.4f}")
print(f"  coherence back-flow   QM-only (Markov)      : {backflow(c_M):.3e}  (0 => no revival)")
print(f"  coherence back-flow   extended (non-Markov) : {backflow(c_NM):.3e}  (>0 => revivals)")
print(f"  min Choi eig          QM-only (Markov)      : {min_choi_eig(c_M):+.4f}  (>=0 => CP-divisible)")
print(f"  min Choi eig          extended (non-Markov) : {min_choi_eig(c_NM):+.4f}  (<0 => CP-div. VIOLATED)")
print("  => the TIME extension genuinely changes the DYNAMICAL result: the QM-only")
print("     (time-local) description is CP-divisible and shows no revival; the")
print("     extended (history-coupled) one leaves the Markovian class.")

print("""
SUMMARY -- what the extension changes
  * MASS  (C^3 fibre)      : nothing for the QM operations. It is a tensor factor;
                             static QM observables (gauge, entanglement, CHSH) are
                             identical. The translation was already complete AS a
                             translation of QM operations -- it merely did not COVER
                             mass.
  * TIME  (process)        : changes time-dependent observables. The QM-only bridge
                             is time-local/Markovian; the extended one is non-Markovian
                             (coherence revivals, CP-divisibility violated). Single-time
                             observables are unaffected; sequential/dynamical ones are.
  Net: the QM translation is "slightly incomplete" only in scope (no mass, time-local).
  Extending it leaves every static QM result intact and adds exactly one new effect --
  non-Markovian memory in the dynamics -- which is itself still within quantum theory
  (a traced-out unitary bath reproduces it).
""")
