#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FFGFT-side contribution to the joint HLV <-> FFGFT spectral test
================================================================

Purpose
-------
Marcel Krueger's HLV testbed produces a graph Laplacian on an aperiodic
(cut-and-project / quasicrystalline) graph. The agreed sharp question is
*aperiodic-vs-periodic*, not discrete-vs-random. This script supplies the
FFGFT side of the comparison:

  (1) the PERIODIC arm  -- combinatorial graph-Laplacian spectra of the
      D-dimensional periodic torus lattice (D = 2, 3, 4; D = 4 is FFGFT's
      native T^4 substrate), with exact analytic eigenvalues;
  (2) a RANDOM null      -- degree-matched Erdos-Renyi control;
  (3) SCALE-FREE discriminators that need no absolute scale and no spectral
      unfolding: the consecutive level-spacing ratio <r>, the degeneracy
      fraction, a gap-richness measure, and low eigenvalue ratios;
  (4) the FFGFT periodic-arm PREDICTION: the continuum torus mode spectrum
      is integer-structured, |n|^2 = sum of D squares -> a rational/harmonic
      ratio ladder with NO Cantor-type gap hierarchy;
  (5) the RECOVERY-LIMIT check: the lattice dispersion lambda(k) ~ |k|^2
      with the leading residual reported (not only shown qualitatively).

The single function `analyze_spectrum(eigenvalues, name)` computes the SAME
scale-free metrics for any eigenvalue array, so Marcel can drop the HLV
quasicrystal Laplacian eigenvalues straight in for an apples-to-apples row:

    >>> analyze_spectrum(my_quasicrystal_eigs, "HLV quasicrystal")

Conservative framing: this is falsification-before-interpretation. If the
quasicrystal is NOT separable from the periodic and random controls on these
statistics, that is a clean negative and should be reported as one.

Reproducible: fixed seed. Dependencies: numpy (+ stdlib). No network needed.
Author: Johann Pascher (FFGFT / T0).  Date: 2026-06-09.
"""

import itertools
import numpy as np
from numpy.linalg import eigvalsh

SEED = 20260609
RNG = np.random.default_rng(SEED)


# --------------------------------------------------------------------------
# (1) Periodic torus graph-Laplacian: exact analytic eigenvalues
# --------------------------------------------------------------------------
def torus_laplacian_eigs(D, L):
    """Combinatorial graph-Laplacian eigenvalues of the D-dimensional
    periodic nearest-neighbour lattice with L sites per dimension.

    Exact formula:  lambda(m) = 2 * sum_{i=1..D} (1 - cos(2*pi*m_i / L)),
    with m_i in {0,...,L-1}.  Returns the full sorted multiset (L**D values).
    """
    one_minus_cos = 1.0 - np.cos(2.0 * np.pi * np.arange(L) / L)   # length L
    vals = np.zeros(1)
    for _ in range(D):
        vals = (vals[:, None] + 2.0 * one_minus_cos[None, :]).ravel()
    return np.sort(vals)


def sum_of_squares_ladder(D, nmax=8):
    """Continuum torus mode-squared values |n|^2 = sum of D squares
    (the FFGFT periodic-arm prediction). Returns sorted distinct positive
    values up to nmax^2, and their ratios to the first."""
    rng = range(-nmax, nmax + 1)
    vals = set()
    for combo in itertools.product(rng, repeat=D):
        s = sum(c * c for c in combo)
        if 0 < s <= nmax * nmax:
            vals.add(s)
    v = np.array(sorted(vals), dtype=float)
    return v


# --------------------------------------------------------------------------
# (2) Random null: degree-matched Erdos-Renyi control
# --------------------------------------------------------------------------
def erdos_renyi_laplacian_eigs(N, mean_degree, rng):
    """Laplacian eigenvalues of an Erdos-Renyi G(N, p) graph with
    p = mean_degree / (N - 1)  (so the expected degree matches the lattice)."""
    p = mean_degree / (N - 1)
    U = rng.random((N, N))
    A = (U < p).astype(float)
    A = np.triu(A, 1)
    A = A + A.T                       # symmetric, zero diagonal
    deg = A.sum(axis=1)
    Lap = np.diag(deg) - A
    return np.sort(eigvalsh(Lap))


# --------------------------------------------------------------------------
# (3) Scale-free discriminators  -- the shared analysis pipeline
# --------------------------------------------------------------------------
def analyze_spectrum(eigs, name, n_ratios=8, big_gap_factor=3.0):
    """Compute scale-free, unfolding-free spectral discriminators.

    Returns a dict; also safe to print via `print_row`. Works on ANY
    eigenvalue array (periodic, random, or HLV quasicrystal).

    Metrics
    -------
    degeneracy_fraction : fraction of consecutive gaps that are ~0 (relative
                          to spectral width). High for periodic/integrable
                          spectra, ~0 for random and (generically) quasicrystal.
    mean_r_raw          : <r> = <min(s_n,s_{n+1})/max(s_n,s_{n+1})> over all
                          consecutive gaps (degenerate gaps -> r = 0).
                          Reference values: Poisson ~ 0.386, GOE ~ 0.531.
    mean_r_distinct     : the same, but on DISTINCT eigenvalues only (isolates
                          level repulsion from degeneracy).
    gap_richness        : fraction of gaps exceeding big_gap_factor * mean gap
                          (a hierarchy of large gaps -> quasicrystalline,
                          Cantor-like; few -> band edges; ~0 -> random).
    low_ratios          : lambda_k / lambda_1 for the first n_ratios distinct
                          nonzero eigenvalues (the scale-free ratio spectrum).
    """
    e = np.sort(np.asarray(eigs, dtype=float))
    e = e[e > -1e-12]                              # drop tiny negatives (numerical)
    width = e[-1] - e[0] if e[-1] > e[0] else 1.0
    tol = 1e-9 * width

    # --- consecutive level-spacing ratio on the full spectrum ---
    s = np.diff(e)
    deg_frac = float(np.mean(s <= tol)) if len(s) else 0.0
    r_raw = _mean_r(s, tol)

    # --- distinct levels only ---
    distinct = _collapse(e, tol)
    s_d = np.diff(distinct)
    r_distinct = _mean_r(s_d, 0.0)

    # --- gap richness ---
    mean_gap = s_d.mean() if len(s_d) else 0.0
    gap_rich = float(np.mean(s_d > big_gap_factor * mean_gap)) if len(s_d) else 0.0
    max_gap_ratio = float(s_d.max() / mean_gap) if len(s_d) and mean_gap > 0 else 0.0

    # --- scale-free low eigenvalue ratios ---
    nz = distinct[distinct > tol]
    low = nz[:n_ratios]
    low_ratios = (low / low[0]).tolist() if len(low) else []

    return dict(name=name, N=len(e), n_distinct=len(distinct),
                degeneracy_fraction=deg_frac, mean_r_raw=r_raw,
                mean_r_distinct=r_distinct, gap_richness=gap_rich,
                max_gap_ratio=max_gap_ratio, low_ratios=low_ratios)


def _mean_r(spacings, tol):
    if len(spacings) < 2:
        return float("nan")
    s = spacings
    a, b = s[:-1], s[1:]
    mx = np.maximum(a, b)
    r = np.where(mx > tol, np.minimum(a, b) / np.where(mx > tol, mx, 1.0), 0.0)
    return float(np.mean(r))


def _collapse(e, tol):
    out = [e[0]]
    for x in e[1:]:
        if x - out[-1] > tol:
            out.append(x)
    return np.array(out)


def print_row(d):
    lr = ", ".join(f"{x:.3f}" for x in d["low_ratios"][:6])
    print(f"  {d['name']:<22s} N={d['N']:<5d} distinct={d['n_distinct']:<5d}"
          f" deg.frac={d['degeneracy_fraction']:.3f}"
          f"  <r>_raw={d['mean_r_raw']:.3f}  <r>_distinct={d['mean_r_distinct']:.3f}"
          f"  gap_rich={d['gap_richness']:.3f}  maxgap/mean={d['max_gap_ratio']:.1f}")
    print(f"      scale-free low ratios (lam_k/lam_1): [{lr}]")


# --------------------------------------------------------------------------
# (5) Recovery-limit check for the periodic lattice
# --------------------------------------------------------------------------
def recovery_limit_fit(L=512):
    """Lattice dispersion along one axis: lambda(k) = 2(1 - cos k).
    Fit small-k behaviour to  lambda = a*k^2 + b*k^4  and report the leading
    exponent and residual. Continuum wave dispersion omega = sqrt(lambda) ~ |k|.
    """
    m = np.arange(1, L // 8)                 # small-k window
    k = 2.0 * np.pi * m / L
    lam = 2.0 * (1.0 - np.cos(k))
    # fit lambda/k^2 = a + b*k^2  (linear in k^2)
    x = k ** 2
    y = lam / x
    b, a = np.polyfit(x, y, 1)               # y = b*x + a
    # leading exponent of lambda(k): slope of log(lambda) vs log(k) at small k
    p = np.polyfit(np.log(k[:10]), np.log(lam[:10]), 1)[0]
    return dict(leading_exponent=p, a=a, b=b)


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------
def main():
    print("=" * 78)
    print("FFGFT periodic-arm spectral testbed  (seed = %d)" % SEED)
    print("Scale-free references:  Poisson <r> ~ 0.386   GOE <r> ~ 0.531")
    print("=" * 78)

    configs = [(2, 24), (3, 8), (4, 5)]      # (D, L);  D=4 is FFGFT's T^4
    rows = []
    for D, L in configs:
        N = L ** D
        deg = 2 * D
        eigs_p = torus_laplacian_eigs(D, L)
        dp = analyze_spectrum(eigs_p, f"periodic T^{D} (L={L})")
        eigs_r = erdos_renyi_laplacian_eigs(N, deg, RNG)
        dr = analyze_spectrum(eigs_r, f"random ER (N={N},<k>={deg})")
        print(f"\n--- D={D}  (N={N}, degree={deg}) ---")
        print_row(dp)
        print_row(dr)
        rows.extend([dp, dr])

    print("\n" + "=" * 78)
    print("FFGFT prediction -- continuum torus mode ladder |n|^2 = sum of D squares")
    print("(scale-free ratios lam_k/lam_1; note: D=4 hits EVERY integer, Lagrange)")
    print("-" * 78)
    for D in (2, 3, 4):
        v = sum_of_squares_ladder(D, nmax=6)
        ratios = v[:10] / v[0]
        print(f"  D={D}:  |n|^2 = [{', '.join(f'{int(x)}' for x in v[:10])}]"
              f"   ratios = [{', '.join(f'{x:.3f}' for x in ratios)}]")

    print("\n" + "=" * 78)
    print("Recovery-limit check (periodic lattice, dispersion along one axis)")
    print("-" * 78)
    rl = recovery_limit_fit()
    print(f"  leading exponent of lambda(k) at small k : {rl['leading_exponent']:.4f}"
          f"   (expected 2.000  ->  diffusive lambda ~ |k|^2)")
    print(f"  lambda/k^2 = a + b*k^2 :  a = {rl['a']:.5f} (expect 1),"
          f"  b = {rl['b']:.5f} (expect -1/12 = -0.08333)")
    print(f"  => leading residual is O(k^2) relative, sign-definite (negative);")
    print(f"     wave dispersion omega = sqrt(lambda) ~ |k| is recovered.")

    # CSV
    try:
        import csv
        with open("ffgft_periodic_spectral_summary.csv", "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["name", "N", "n_distinct", "degeneracy_fraction",
                        "mean_r_raw", "mean_r_distinct", "gap_richness",
                        "max_gap_ratio", "low_ratios"])
            for d in rows:
                w.writerow([d["name"], d["N"], d["n_distinct"],
                            f"{d['degeneracy_fraction']:.5f}",
                            f"{d['mean_r_raw']:.5f}", f"{d['mean_r_distinct']:.5f}",
                            f"{d['gap_richness']:.5f}", f"{d['max_gap_ratio']:.4f}",
                            ";".join(f"{x:.5f}" for x in d["low_ratios"])])
        print("\n[wrote ffgft_periodic_spectral_summary.csv]")
    except Exception as exc:                  # pragma: no cover
        print("CSV not written:", exc)

    print("\n" + "=" * 78)
    print("TO COMPARE THE HLV QUASICRYSTAL: pass its Laplacian eigenvalues through")
    print("the identical pipeline, e.g.")
    print("    d = analyze_spectrum(quasicrystal_eigs, 'HLV quasicrystal'); print_row(d)")
    print("Expected if genuinely aperiodic: low degeneracy, intermediate <r>")
    print("(between Poisson 0.386 and GOE 0.531), and HIGH gap_richness")
    print("(Cantor-like hierarchy) -- distinguishable from BOTH controls.")
    print("If not distinguishable: report the negative. Falsification before interpretation.")
    print("=" * 78)


if __name__ == "__main__":
    main()
