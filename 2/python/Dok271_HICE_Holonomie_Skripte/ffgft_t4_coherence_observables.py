#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FFGFT T^4 -- coherence-resolving observables (#7)
=================================================

#1 showed: a magnitude-matched dynamical U3(t) memory does NOT separate from a
no-memory snapshot under the witness lambda_low. The open question (and exactly
Marcel's HICE-MEM0 question, mail 08:33): can ANY observable on the static
carrier resolve what lambda_low cannot -- i.e. distinguish two phase patterns
of equal magnitude by their coherence STRUCTURE rather than their size?

We take the same fair probe as #1 (snapshot single-handle flux vs memory-spread
flux, L2-magnitude-matched) and the coherent-vs-random probe, and run THREE
observables beyond lambda_low:

  (O1) lambda_low                : baseline (known blind spot)
  (O2) IPR of the lowest mode    : localization of the frustrated state
  (O3) low-band spectral spread  : variance of the lowest-k eigenvalues
  (O4) loop-holonomy dispersion  : std of Omega(C) over a family of closed loops

If any of O2-O4 separates patterns that O1 cannot, that observable is the
coherence-resolving upgrade the dynamical U3(t) test needs. If none do, the
limit is fundamental to this carrier family and U3-uniqueness needs a different
structure entirely.

numpy only.
"""

import numpy as np
from numpy.linalg import eigh
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
    return len(coords), edges, idx, L


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
    return np.array([amp / L if m == mu else 0.0 for (_i, _j, m) in edges])


def match_norm(phase, target):
    n = np.linalg.norm(phase)
    return phase * (target / n) if n > 1e-15 else phase


# ---- observables ---------------------------------------------------------
def observables(N, edges, phase, idx, L):
    w, v = eigh(scalar_laplacian(N, edges, phase))
    lam_low = float(w[0])
    psi = np.abs(v[:, 0]) ** 2
    ipr = float(np.sum(psi ** 2) / (np.sum(psi) ** 2))          # localization
    band = float(np.var(w[:8]))                                  # low-band spread
    # loop-holonomy dispersion over all elementary plaquettes (mu<nu faces)
    pos = {i: c for c, i in idx.items()}
    fluxes = []
    emap = {(i, m): p for p, (i, _j, m) in enumerate(edges)}
    for i in range(N):
        c = pos[i]
        for mu in range(4):
            for nu in range(mu + 1, 4):
                a = list(c); a[mu] = (a[mu] + 1) % L; im = idx_of(idx, a)
                b = list(c); b[nu] = (b[nu] + 1) % L
                # plaquette edges: +mu(i), +nu(i+mu), -mu(i+nu), -nu(i)
                e1 = phase[emap[(i, mu)]]
                e2 = phase[emap[(im, nu)]]
                e3 = phase[emap[(idx_of(idx, b), mu)]]
                e4 = phase[emap[(i, nu)]]
                fluxes.append(e1 + e2 - e3 - e4)
    loop_disp = float(np.std(fluxes))
    return lam_low, ipr, band, loop_disp


def idx_of(idx, coord_list):
    return idx[tuple(coord_list)]


def run(L=4, T=8, amp=0.5 * np.pi):
    N, edges, idx, L = build_T4(L)
    print(f"Carrier: T^4, L={L}, N={N}.  Probe: magnitude-matched pattern pairs.\n")

    # Probe A: coherent single-handle vs matched-magnitude random
    snap = handle_flux(edges, L, 0, amp)
    tgt = np.linalg.norm(snap)
    rng = np.random.default_rng(0)
    rand = match_norm(rng.uniform(-1, 1, len(edges)), tgt)

    # Probe B: snapshot vs memory-spread (the #1 pattern)
    handles = [t % 4 for t in range(T)]
    snaps = [handle_flux(edges, L, mu, amp) for mu in handles]
    mem = match_norm(sum(np.exp(-(T - 1 - t) / 4.0) * s for t, s in enumerate(snaps)), tgt)

    labels = ["coherent(1-handle)", "random(matched)", "snapshot", "memory-spread"]
    pats = [snap, rand, snaps[-1], mem]
    names = ["lambda_low", "IPR(loc)", "low-band var", "loop-holo std"]
    rows = [observables(N, edges, p, idx, L) for p in pats]

    print(f"{'pattern':20} " + " ".join(f"{n:>14}" for n in names))
    print("-" * 84)
    for lab, r in zip(labels, rows):
        print(f"{lab:20} " + " ".join(f"{x:14.5e}" for x in r))

    # discrimination: relative gap between the two pairs, per observable
    def gap(a, b):
        return [abs(a[k] - b[k]) / max(abs(a[k]), abs(b[k]), 1e-15) for k in range(4)]

    gAB = gap(rows[0], rows[1])   # coherent vs random
    gSM = gap(rows[2], rows[3])   # snapshot vs memory
    print("\nrelative separation (|a-b|/max):")
    print(f"{'coherent vs random':20} " + " ".join(f"{x:14.2%}" for x in gAB))
    print(f"{'snapshot vs memory':20} " + " ".join(f"{x:14.2%}" for x in gSM))

    print("\nReading: lambda_low (col 1) is the known blind spot. Any column where")
    print("'snapshot vs memory' shows a large separation is an observable that")
    print("resolves coherence structure where lambda_low cannot -> candidate")
    print("upgrade for the HICE-MEM0 channel-swap test. If all columns stay small")
    print("for snapshot-vs-memory, the static carrier cannot host U3-uniqueness.")


if __name__ == "__main__":
    run()
