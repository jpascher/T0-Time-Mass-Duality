#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FFGFT T^4 holonomy witness  --  independent comparison carrier for the HICE program
===================================================================================

Purpose
-------
This is the FFGFT-side counterpart to Marcel Krueger's HICE / hybrid-cell holonomy
test, written in his admissibility language so the two can be compared on equal terms.
It computes an accumulated-phase / cycle-flux witness on the FFGFT T^4 torus cycle
structure and runs it through the HICE gate set:

    gauge-null  ->  benign stability  ->  destructive ablation  ->  matched nulls.

Claim-state discipline (deliberately conservative, mirrors Krueger 2026):
    The strongest admissible output is "candidate carrier", NOT validation, NOT a
    physical-spacetime claim, NOT a connection to HLV.  A connection would require an
    explicit map xi <-> delta_H showing both holonomies are images of one structure
    (see accompanying email).  This script only establishes whether the FFGFT side
    even *has* an admissible non-exact loop-holonomy witness to compare.

Object under test (grounded in the corpus)
------------------------------------------
  * Carrier  : periodic 4D lattice graph = discrete T^4.  H_1(T^4) = Z^4 supplies the
               four fundamental cycles (Dok 230: Bell as topological connection;
               Dok 189: integer winding numbers n_i in Z on the (log-)torus).
  * Connection: Peierls phases A_vw on edges; connection Laplacian
               (L s)_v = sum_w W_vw (s_v - exp(i A_vw) s_w)        (cf. Krueger eq. L_HICE)
  * Non-exact holonomy: a constant per-direction phase a_mu is a harmonic (Aharonov-Bohm)
               connection -- a flux through the torus handle that CANNOT be removed by a
               single-valued gauge.  This is the discrete image of FFGFT's
               "irreducible minimum torsion": the torsion-free state is algebraically
               excluded, and xi = 4/30000 is its measure (Dok 172).
  * Witness  : W(flux) = smallest eigenvalue of the connection Laplacian.
               At zero/gradient phase W = 0 (gauge-trivial).  Non-exact flux frustrates
               the constant mode and lifts W > 0  ->  exactly Krueger's "no response at
               gauge-trivial, response only for non-exact holonomy".

This file is self-contained (numpy + scipy).  It is a concept/benchmark script, not a
simulation of physical spacetime.
"""

import numpy as np
from numpy.linalg import eigvalsh
from itertools import product

XI = 4.0 / 30000.0          # FFGFT fundamental constant (irreducible minimum torsion)
RNG = np.random.default_rng(0)


# ----------------------------------------------------------------------------------
# 1. Carrier: discrete T^4
# ----------------------------------------------------------------------------------
def build_T4(L):
    """Periodic 4D lattice graph (discrete T^4) with L sites per dimension.

    Returns
    -------
    N      : number of nodes (= L**4)
    edges  : list of (i, j, mu) for the +mu nearest-neighbour edge from i to j
    L      : echoed side length
    """
    coords = list(product(range(L), repeat=4))
    index = {c: k for k, c in enumerate(coords)}
    N = len(coords)
    edges = []
    for c in coords:
        i = index[c]
        for mu in range(4):
            d = list(c)
            d[mu] = (d[mu] + 1) % L          # periodic boundary -> nontrivial cycles
            j = index[tuple(d)]
            edges.append((i, j, mu))
    return N, edges, L


# ----------------------------------------------------------------------------------
# 2. Connection Laplacian and the holonomy witness
# ----------------------------------------------------------------------------------
def connection_laplacian(N, edges, edge_phase):
    """Hermitian connection Laplacian; edge_phase[k] = A_vw on edge k = (i,j,mu)."""
    H = np.zeros((N, N), dtype=complex)
    deg = np.zeros(N)
    for k, (i, j, _mu) in enumerate(edges):
        u = np.exp(1j * edge_phase[k])
        H[i, j] += -u
        H[j, i] += -np.conj(u)
        deg[i] += 1.0
        deg[j] += 1.0
    H[np.diag_indices(N)] = deg
    return H


def uniform_flux_phase(edges, L, flux_per_loop):
    """Coherent non-exact connection: constant phase per direction.

    A fundamental loop in direction mu has length L, so its holonomy is
    Omega_mu = L * a_mu.  We set a_mu = flux_per_loop[mu] / L so that the loop
    holonomy equals flux_per_loop[mu] exactly.  This is harmonic (non-gradient):
    it cannot be gauged away.
    """
    a = np.array([flux_per_loop[mu] / L for (_i, _j, mu) in edges])
    return a


def gradient_phase(N, edges, theta):
    """Exact (gradient) connection A_vw = theta_w - theta_v.  Must be gauge-removable."""
    return np.array([theta[j] - theta[i] for (i, j, _mu) in edges])


def loop_holonomy(edges, edge_phase, L, mu):
    """Accumulated phase Omega(C) around one fundamental cycle in direction mu."""
    # straight path 0 -> e_mu -> 2 e_mu -> ... -> wraps to 0
    total = 0.0
    for k, (_i, _j, m) in enumerate(edges):
        if m == mu and (_i // (L ** mu)) % L != L - 1:  # not strictly needed; sum all +mu
            pass
    # simpler & exact for the uniform model: sum a_mu over the L edges of one line
    a_mu = [edge_phase[k] for k, (_i, _j, m) in enumerate(edges) if m == mu]
    return (np.mean(a_mu) * L) if a_mu else 0.0


def witness(N, edges, edge_phase):
    """W = smallest eigenvalue of the connection Laplacian (ground-state frustration)."""
    H = connection_laplacian(N, edges, edge_phase)
    return float(eigvalsh(H)[0])


# ----------------------------------------------------------------------------------
# 3. Null models / ablations (Krueger's mandatory set, adapted to T^4)
# ----------------------------------------------------------------------------------
def randomized_holonomy(edges, magnitude, rng):
    """Holonomy-randomization null: random edge phases, magnitude-matched."""
    return rng.uniform(-magnitude, magnitude, size=len(edges))


def degree_matched_rewire(N, edges, rng):
    """Degree-preserving rewiring (double-edge swaps): tests graph-residual reducibility."""
    e = [(i, j) for (i, j, _m) in edges]
    m = len(e)
    for _ in range(5 * m):
        a, b = rng.integers(0, m, size=2)
        (i1, j1), (i2, j2) = e[a], e[b]
        if len({i1, j1, i2, j2}) < 4:
            continue
        e[a], e[b] = (i1, j2), (i2, j1)
    return [(i, j, 0) for (i, j) in e]


# ----------------------------------------------------------------------------------
# 4. Gate runner
# ----------------------------------------------------------------------------------
def run(L=5, scan=None, n_seeds=4):
    if scan is None:
        scan = [0.0, 0.25 * np.pi, 0.5 * np.pi, np.pi, 2.0 * np.pi]
    N, edges, L = build_T4(L)
    print(f"Carrier: discrete T^4, L={L}, nodes N={N}, edges={len(edges)}, "
          f"degree={2*len(edges)//N}")
    print(f"FFGFT anchor: xi = {XI:.6e}  (irreducible minimum torsion, Dok 172)\n")

    W0 = witness(N, edges, np.zeros(len(edges)))
    print(f"[baseline]  W(no phase)            = {W0:.3e}   (expect ~0, constant mode)")

    # --- Gate 1: gauge-null (exact gradient must be isospectral -> W unchanged) -----
    theta = RNG.uniform(0, 2 * np.pi, size=N)
    Wg = witness(N, edges, gradient_phase(N, edges, theta))
    gauge_ok = abs(Wg - W0) < 1e-9
    print(f"[gate 1]    W(exact gradient phase) = {Wg:.3e}   gauge-null pass = {gauge_ok}")
    print(f"            (Krueger Prop.1 / FFGFT torsion-free-excluded: removable part -> 0)\n")

    # --- Corridor scan: coherent non-exact flux vs magnitude-matched randomization --
    print(" flux/loop  |  W_coherent  |  Omega_mu(check) |  W_random(mean+/-sd)  |  ratio")
    print("-" * 78)
    corridor = []
    for f in scan:
        flux = [f, 0.0, 0.0, 0.0]           # flux through ONE torus handle (mu=0)
        a = uniform_flux_phase(edges, L, flux)
        Wc = witness(N, edges, a)
        Om = loop_holonomy(edges, a, L, mu=0)
        mag = np.max(np.abs(a)) if np.max(np.abs(a)) > 0 else 1e-9
        Wr = [witness(N, edges, randomized_holonomy(edges, mag, np.random.default_rng(s)))
              for s in range(n_seeds)]
        Wr_m, Wr_s = float(np.mean(Wr)), float(np.std(Wr))
        ratio = Wc / Wr_m if Wr_m > 1e-12 else float('inf')
        corridor.append((f, Wc, Wr_m, Wr_s))
        print(f"  {f:7.4f}  |  {Wc:9.4e} |   {Om:7.4f}      |  {Wr_m:8.3e}+/-{Wr_s:.1e} |  {ratio:5.2f}")

    # --- Gate at the FFGFT anchor flux = xi -----------------------------------------
    a_xi = uniform_flux_phase(edges, L, [XI, 0, 0, 0])
    W_xi = witness(N, edges, a_xi)
    print(f"\n[anchor]    W(flux/loop = xi)       = {W_xi:.3e}   "
          f"(FFGFT non-removable baseline; >0 and != gradient)")

    # --- Gate 3: destructive ablation (randomize holonomy -> coherent response lost) -
    f_probe = 0.5 * np.pi
    a = uniform_flux_phase(edges, L, [f_probe, 0, 0, 0])
    Wc = witness(N, edges, a)
    mag = np.max(np.abs(a))
    Wr = np.mean([witness(N, edges, randomized_holonomy(edges, mag, np.random.default_rng(s)))
                  for s in range(n_seeds)])
    destructive_ok = abs(Wc - Wr) / max(Wc, 1e-12) > 0.10
    print(f"[gate 3]    coherent {Wc:.3e} vs randomized {Wr:.3e}  -> "
          f"distinguishable = {destructive_ok}")

    # --- Gate 4: matched null (degree-preserving rewire kills the T^4 cycle structure)
    rew = degree_matched_rewire(N, edges, np.random.default_rng(1))
    a_rew = uniform_flux_phase(rew, L, [f_probe, 0, 0, 0])
    W_rew = witness(N, rew, a_rew)
    residual_ok = abs(Wc - W_rew) / max(Wc, 1e-12) > 0.10
    print(f"[gate 4]    T^4 {Wc:.3e} vs degree-matched-rewire {W_rew:.3e}  -> "
          f"not-a-graph-residual = {residual_ok}")

    # --- Gate 2: benign stability (small jitter must stay near, NOT separable) -------
    base = witness(N, edges, uniform_flux_phase(edges, L, [f_probe, 0, 0, 0]))
    jit = [witness(N, edges, uniform_flux_phase(edges, L,
            [f_probe * (1 + 0.02 * RNG.standard_normal()), 0, 0, 0]))
           for _ in range(n_seeds)]
    rel = np.max(np.abs(np.array(jit) - base)) / max(base, 1e-12)
    benign_ok = rel < 0.10
    print(f"[gate 2]    benign jitter rel. change = {rel:.3e}  -> stable = {benign_ok}")

    # --- Verdict (Krueger claim-state ledger) ---------------------------------------
    gates = {"gauge_null": gauge_ok, "benign_stable": benign_ok,
             "destructive_sensitive": destructive_ok, "not_graph_residual": residual_ok}
    print("\n" + "=" * 78)
    print("CLAIM-STATE (HICE ledger):")
    for k, v in gates.items():
        print(f"   {k:24s}: {'PASS' if v else 'FAIL'}")
    if all(gates.values()):
        print("\n   -> candidate_T4_holonomy_carrier  (admissible comparison object;")
        print("      NOT established, NOT a physical claim, NOT yet a connection to HLV)")
    else:
        print("\n   -> T4_holonomy_witness_precondition_not_satisfied")
    print("=" * 78)
    print("Next, for an actual HLV connection: seek an explicit map xi <-> delta_H")
    print("such that this T^4 cycle holonomy and HLV's H_1(G_d) holonomy are images")
    print("of one structure, with a divergence point against a matched null.")
    return gates


if __name__ == "__main__":
    run()
