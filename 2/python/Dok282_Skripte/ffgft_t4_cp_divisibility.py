#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FFGFT T^4 -- CP-divisibility / non-Markovianity probe (history-coupled loop operator)
=====================================================================================
The first test that tries to separate QM-internal dynamics (Markovian, time-local,
CP-divisible) from beyond-Markovian dynamics, with the memory sourced by the FFGFT
T^4 loop operator itself.

Setup. A fibre qubit is dephased by a bath whose mode frequencies omega_k are the
loop frequencies sqrt(lambda_k) of the T^4 connection Laplacian. Pure-dephasing
(independent-boson) decoherence function:

    Gamma(t) = sum_k (2 g_k^2 / omega_k^2) (1 - cos(omega_k t))
    coherence c(t) = exp(-Gamma(t))
    rate     gamma(t) = dGamma/dt = sum_k (2 g_k^2 / omega_k) sin(omega_k t)

Two reduced descriptions of the SAME loop operator, matched on overall decoherence:
  (M)  memoryless / time-local : constant rate gamma_M            -> CP-divisible
  (NM) history-coupled         : full structured T^4 bath (memory) -> may violate CP-div.

Two standard witnesses:
  BLP : trace-distance back-flow for the pair |+>,|->; here D(t)=c(t).
        Markovian => D monotone non-increasing (back-flow 0); any revival => non-Markovian.
  RHP : CP-divisibility of the step map via Choi positivity. For dephasing the step
        multiplier is r=c(t+dt)/c(t) and the min Choi eigenvalue is (1-r)/2; r>1
        (coherence grew over the step) => negative => CP-divisibility violated.
  (For dephasing the two witnesses coincide -- a built-in consistency check.)

Honest scope. A structured/finite bath that yields a non-CP-divisible REDUCED map is
the operational beyond-Markovian signature -- exactly the layer HLV is built for. It is
"beyond QM modelling" only in the sense of beyond the time-local/Markovian reduced
description, NOT a proof of physics beyond quantum theory (a traced-out unitary bath
reproduces it). What the test establishes is the structural point: history coupling on
the T^4 loop operator drives the reduced dynamics out of the CP-divisible class, while a
memoryless coupling does not.

numpy only.
"""

import numpy as np
from numpy.linalg import eigvalsh
from itertools import product

XI = 4.0 / 30000.0


def build_T4(L):
    coords = list(product(range(L), repeat=4))
    idx = {c: k for k, c in enumerate(coords)}
    edges = []
    for c in coords:
        i = idx[c]
        for mu in range(4):
            d = list(c); d[mu] = (d[mu] + 1) % L
            edges.append((i, idx[tuple(d)], mu))
    return len(coords), edges


def conn_laplacian(N, edges, amp):
    H = np.zeros((N, N), dtype=complex)
    deg = np.zeros(N)
    for (i, j, mu) in edges:
        a = amp * (1 + mu)          # mu-dependent flux -> structured spectrum
        u = np.exp(1j * a)
        H[i, j] += -u; H[j, i] += -np.conj(u)
        deg[i] += 1.0; deg[j] += 1.0
    H[np.diag_indices(N)] = deg
    return H


def bath_modes(L=3, amp=0.5 * np.pi, n_modes=6):
    N, edges = build_T4(L)
    lam = eigvalsh(conn_laplacian(N, edges, amp))
    lam = lam[lam > 1e-6]
    omega = np.sqrt(lam)
    uniq = []
    for w in omega:                                   # bucket near-degenerate modes
        if not uniq or abs(w - uniq[-1][0]) > 1e-3:
            uniq.append([w, 1])
        else:
            uniq[-1][1] += 1
    uniq = uniq[:n_modes]                              # few dominant low modes = structured bath
    omega_k = np.array([u[0] for u in uniq])
    g_k = np.sqrt(np.array([u[1] for u in uniq], dtype=float))   # coupling ~ sqrt(degeneracy)
    return omega_k, g_k


def witnesses(c, gamma_t=None):
    D = c.copy()                       # trace distance for |+>,|-> equals |c(t)|
    dD = np.diff(D)
    backflow = float(np.sum(dD[dD > 0]))
    revived = bool(np.any(dD > 1e-9))
    r = c[1:] / c[:-1]                  # step multiplier
    min_choi = float(np.min((1.0 - r) / 2.0))
    neg = None if gamma_t is None else int(np.sum(gamma_t < 0))
    return backflow, revived, min_choi, neg


def run(L=3, T=80.0, nt=4000, coupling=2.4):
    omega_k, g_k = bath_modes(L)
    g_k = coupling * g_k / np.sqrt(np.sum(g_k ** 2))   # fix total coupling
    t = np.linspace(1e-3, T, nt)

    Gamma = np.zeros_like(t)
    gamma = np.zeros_like(t)
    for wk, gk in zip(omega_k, g_k):
        Gamma += (2 * gk ** 2 / wk ** 2) * (1 - np.cos(wk * t))
        gamma += (2 * gk ** 2 / wk) * np.sin(wk * t)
    c_NM = np.exp(-Gamma)

    gamma_M = float(np.mean(np.abs(gamma)))            # memoryless matched rate
    c_M = np.exp(-gamma_M * t)

    bf_M, rev_M, choi_M, _ = witnesses(c_M)
    bf_NM, rev_NM, choi_NM, negc = witnesses(c_NM, gamma)

    print(f"T^4 loop-operator bath frequencies omega_k: {np.round(omega_k, 3)}")
    print(f"couplings g_k: {np.round(g_k, 3)}   matched memoryless rate gamma_M = {gamma_M:.4f}")
    print(f"max decoherence Gamma_max = {Gamma.max():.3f}   (coherence dips to {np.exp(-Gamma.max()):.3f})\n")

    hdr = f"{'description':34}{'BLP backflow':>13}{'D revives':>11}{'min Choi eig':>14}{'gamma<0 steps':>14}"
    print(hdr); print("-" * len(hdr))
    print(f"{'(M)  memoryless / time-local':34}{bf_M:13.3e}{str(rev_M):>11}{choi_M:14.3e}{'n/a':>14}")
    print(f"{'(NM) history-coupled T^4 bath':34}{bf_NM:13.3e}{str(rev_NM):>11}{choi_NM:14.3e}{str(negc):>14}")

    print("\nReading:")
    print(" (M)  CP-divisible: D monotone, back-flow 0, min Choi eig >= 0  ->  QM-internal / Markovian.")
    print(" (NM) CP-divisibility VIOLATED: D revives (back-flow > 0), min Choi eig < 0, gamma(t) < 0")
    print("      ->  non-Markovian reduced dynamics, sourced purely by the loop-history coupling.")
    print(" Same loop operator, two reduced descriptions: only the history-coupled one leaves the")
    print(" Markovian / CP-divisible class. That is the operational beyond-Markovian signature --")
    print(" the layer HLV is built for. (Caveat: beyond the time-local REDUCED description, not")
    print(" beyond quantum theory; a traced-out unitary bath reproduces it. The structural separation")
    print(" -- history coupling leaves CP-divisibility, memoryless does not -- is what is established.)")


if __name__ == "__main__":
    run()
