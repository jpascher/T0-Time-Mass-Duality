#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FFGFT T^4 -- dynamical U3(t) memory test (Krueger v2, Sec. 13.5 / 17)
=====================================================================

The static context/content witness gave a NEGATIVE channel-swap: U1,U2,U3 are
Z3-symmetric, so no axis is distinguished. Krueger's Sec. 13.5 says the fix is a
genuinely time-indexed memory channel

    U3(v, t) <- { Omega(C_f ; t - tau) : tau > 0 },

i.e. U3 carries forward the *history* of loop holonomy, while U1/U2 see only the
instantaneous content. The decisive question: does a real, magnitude-matched
memory law break the channel symmetry (-> U3 genuinely distinct), or does it
not (-> U3-uniqueness fails even dynamically)?

Crucial fairness rule (Krueger Sec. 13.3 channel-swap; Sec. 13.4 warning that a
naive integral just changes magnitude or smooths toward the exact/gradient part):
we compare U3(memory-integrated) against U1/U2(snapshot) at the SAME L2 phase
magnitude. Any witness difference must then come from the *pattern* (coherence
structure of the accumulated holonomy), not from magnitude.

Honest stance: one memory law is a probe, not a proof. We run an exponential
history kernel over a time-varying content (the active flux handle rotates in
time, so the snapshot sees one handle while the memory integral sees a history-
shaped spread), scan the memory time, and report what happens.

numpy only.
"""

import numpy as np
from numpy.linalg import eigvalsh
from itertools import product

XI = 4.0 / 30000.0


def build_T4(L):
    coords = list(product(range(L), repeat=4))
    idx = {c: k for k, c in enumerate(coords)}
    N = len(coords)
    edges = []
    for c in coords:
        i = idx[c]
        for mu in range(4):
            d = list(c); d[mu] = (d[mu] + 1) % L
            edges.append((i, idx[tuple(d)], mu))
    return N, edges, L


def scalar_laplacian(N, edges, phase):
    H = np.zeros((N, N), dtype=complex)
    deg = np.zeros(N)
    for k, (i, j, _m) in enumerate(edges):
        u = np.exp(1j * phase[k])
        H[i, j] += -u; H[j, i] += -np.conj(u)
        deg[i] += 1.0; deg[j] += 1.0
    H[np.diag_indices(N)] = deg
    return H


def handle_flux(edges, L, mu, amp):
    """Uniform non-exact flux of amplitude `amp` on handle mu only."""
    return np.array([amp / L if m == mu else 0.0 for (_i, _j, m) in edges])


def match_norm(phase, target_norm):
    """Rescale a phase vector to a fixed L2 norm (magnitude match)."""
    n = np.linalg.norm(phase)
    return phase * (target_norm / n) if n > 1e-15 else phase


def witness(N, edges, phase):
    """Low-mode lift = smallest eigenvalue of the single-axis connection Laplacian."""
    return float(eigvalsh(scalar_laplacian(N, edges, phase))[0])


def run(L=4, T=8, amp=0.5 * np.pi):
    N, edges, L = build_T4(L)
    print(f"Carrier: T^4, L={L}, N={N}, {len(edges)} edges/axis;  time steps T={T}\n")

    # --- time-varying content: active flux handle rotates over the 4 handles ---
    handles = [t % 4 for t in range(T)]                      # mu(t)
    snapshots = [handle_flux(edges, L, mu, amp) for mu in handles]

    # U1, U2 : NO memory -> they see only the final instantaneous content
    snap = snapshots[-1]                                      # flux on handle mu(T-1)
    target = np.linalg.norm(snap)                            # common magnitude

    print(" tau_mem |  W(U1/U2 snapshot) |  W(U3 memory) | spread/chance | U3 distinct?")
    print("-" * 74)
    for tau_mem in [0.5, 1.0, 2.0, 4.0, 1e9]:                # 1e9 ~ flat (full history)
        # U3 : exponential history kernel over the rotating content (memory)
        kern = np.array([np.exp(-(T - 1 - t) / tau_mem) for t in range(T)])
        u3 = sum(k * s for k, s in zip(kern, snapshots))
        u3 = match_norm(u3, target)                          # FAIR: same L2 magnitude

        W12 = witness(N, edges, snap)
        W3 = witness(N, edges, u3)
        spread = abs(W3 - W12)
        # chance band: spread from re-seeding the no-memory snapshot phase signs
        chance = np.std([witness(N, edges, match_norm(
            snap * np.random.default_rng(s).choice([-1, 1], size=len(edges)), target))
            for s in range(4)])
        distinct = spread > 3 * max(chance, 1e-12)
        tm = "inf" if tau_mem > 1e8 else f"{tau_mem:.1f}"
        print(f" {tm:>6}  |  {W12:14.5e}  | {W3:12.5e} |  {spread/max(chance,1e-12):6.2f}x      |  {distinct}")

    print("\nReading:")
    print(" - If 'U3 distinct?' is True for some tau_mem, a magnitude-matched memory")
    print("   law DOES break the Z3 channel symmetry -> U3-uniqueness can emerge")
    print("   dynamically, and is worth carrying to the channel-swap falsifier proper.")
    print(" - If it stays False, memory only rescales/reshapes within the witness'")
    print("   blind spot: U3-uniqueness fails even dynamically for THIS witness, and")
    print("   the limit is confirmed to be the witness class, not the memory law.")
    print("   (Per Krueger 13.4, the next move would then be a memory law that")
    print("    *generates* non-exact curvature, plus a coherence-resolving observable.)")


if __name__ == "__main__":
    run()
