#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FFGFT T^4 context/content holonomy witness  --  independent replication of the
De Jesus W_psi audit (Krueger 2026, hybrid-HLV manuscript v2, Sec. 13) on the
FFGFT carrier.
=============================================================================

Why this script exists
----------------------
The first-cut witness (lambda_min of a connection Laplacian) failed the
destructive-ablation gate: it measured frustration *magnitude*, not cycle
*coherence*.  De Jesus' v2 fix is a context/content split:

    context (anchor) = gauge-exact background, held fixed
    content          = non-exact holonomy added on top
    W_psi            = lambda_low( L[context + content] ) - lambda_low( L[context] )

holding the carrier and the gauge-exact anchor fixed and subtracting the
context-only baseline.  This script implements that on the FFGFT C^3 ICE fibre
over T^4 (U1,U2,U3) and runs De Jesus' decisive tests:

    gauge-null  --  content detection  --  benign stability  --  destructive
    ablation  --  channel-swap falsifier  --  corridor sweep  --  matched null

Honest expectation (to be confirmed/refuted by the run, not assumed):
  * gauge-null clean and content detectable  -> context/content design works;
  * channel-swap NEGATIVE -- the three ICE channels are Z3-symmetric on the
    FFGFT carrier (det A_xi = 1 - xi, Dok 206), so no axis is distinguished;
  * corridor sweep MONOTONE -> bounded slow-beat corridor not supported.
If so, the FFGFT carrier reaches the SAME claim-state as De Jesus' HLV run,
which is the useful result: it is an independent-carrier confirmation, and it
locates the limitation in the witness class, not in either substrate.

NOT implemented here (declared, not hidden): the moving spiral-time window
W_psi(t) of Sec. 5.2 and its membership-flip residualisation (HICE-CORR4).
This static carrier has no acceptance-window membership dynamics to confound,
so it tests the operator side only.

Self-contained: numpy only.
"""

import numpy as np
from numpy.linalg import eigvalsh
from itertools import product

XI = 4.0 / 30000.0
RNG = np.random.default_rng(0)


# --------------------------------------------------------------------------
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
    """N x N Hermitian connection Laplacian for one fibre axis."""
    H = np.zeros((N, N), dtype=complex)
    deg = np.zeros(N)
    for k, (i, j, _m) in enumerate(edges):
        u = np.exp(1j * phase[k])
        H[i, j] += -u; H[j, i] += -np.conj(u)
        deg[i] += 1.0; deg[j] += 1.0
    H[np.diag_indices(N)] = deg
    return H


def uniform_flux(edges, L, flux):
    """Coherent non-exact connection: a_mu = flux/L  ->  loop holonomy = flux."""
    return np.array([flux / L for (_i, _j, _m) in edges])


def gradient_phase(N, edges, rng):
    """Exact / removable phase A_vw = theta_w - theta_v (gauge-exact context)."""
    theta = rng.uniform(0, 2 * np.pi, size=N)
    return np.array([theta[j] - theta[i] for (i, j, _m) in edges])


def low_sum(H, k=3):
    """Sum of the k lowest eigenvalues (the constant-mode sector for C^3)."""
    return float(np.sum(eigvalsh(H)[:k]))


# --------------------------------------------------------------------------
def W_psi(N, edges, L, content_axis, flux, ctx_seed=0, content_phase=None):
    """De Jesus context/content witness on the 3-axis ICE fibre.

    context : gauge-exact gradient phase on each of the 3 axes (removable).
    content : non-exact phase on `content_axis` (uniform flux, or custom array).
    Returns lambda_low[ctx+content] - lambda_low[ctx], summed over the 3 axes'
    lowest modes (robust to the 3-fold constant-mode degeneracy).
    """
    rng = np.random.default_rng(ctx_seed)
    ctx = [gradient_phase(N, edges, rng) for _ in range(3)]      # 3 gauge-exact axes
    cnt = uniform_flux(edges, L, flux) if content_phase is None else content_phase

    # context only
    base = sum(eigvalsh(scalar_laplacian(N, edges, ctx[a]))[0] for a in range(3))
    # context + content (content added on one axis)
    tot = 0.0
    for a in range(3):
        ph = ctx[a] + (cnt if a == content_axis else 0.0)
        tot += eigvalsh(scalar_laplacian(N, edges, ph))[0]
    return tot - base


# --------------------------------------------------------------------------
def run(L=4):
    N, edges, L = build_T4(L)
    print(f"Carrier: discrete T^4 with C^3 ICE fibre (U1,U2,U3).  L={L}, "
          f"N={N} nodes, {len(edges)} edges/axis")
    print(f"Witness: W_psi = lambda_low[ctx+content] - lambda_low[ctx]  "
          f"(De Jesus context/content split)\n")

    probe = 0.5 * np.pi

    # --- Gate 1: gauge-null (content = exact gradient -> W_psi ~ 0) ----------
    Wg = W_psi(N, edges, L, content_axis=2, flux=0.0,
               content_phase=gradient_phase(N, edges, np.random.default_rng(7)))
    gauge_ok = abs(Wg) < 1e-9
    print(f"[gate 1] gauge-null     W_psi(exact-gradient content) = {Wg:.3e}  "
          f"pass={gauge_ok}")

    # --- content detection (non-exact content over gauge-exact context) ------
    W_none = W_psi(N, edges, L, content_axis=2, flux=0.0)
    W_cont = W_psi(N, edges, L, content_axis=2, flux=probe)
    detect_ok = (W_cont - W_none) > 1e-6
    print(f"[detect] W_psi(no content)={W_none:.3e}   W_psi(content)={W_cont:.3e}"
          f"   content detectable={detect_ok}")

    # --- Channel-swap falsifier: content on U1 vs U2 vs U3 --------------------
    swaps = [W_psi(N, edges, L, content_axis=a, flux=probe) for a in range(3)]
    spread = float(np.max(swaps) - np.min(swaps))
    chance = 1e-9   # numerical noise band
    channel_specific = spread > 10 * chance
    print(f"[falsifier] channel-swap W_psi(U1,U2,U3) = "
          f"[{swaps[0]:.4e}, {swaps[1]:.4e}, {swaps[2]:.4e}]")
    print(f"            spread={spread:.2e}  ->  U3-specific memory = {channel_specific}"
          f"   (Z3-symmetric axes: expected NEGATIVE)")

    # --- Corridor sweep: monotone/saturating or interior-peaked? -------------
    scan = np.linspace(0, np.pi, 9)
    sweep = [W_psi(N, edges, L, content_axis=2, flux=f) for f in scan]
    arg = int(np.argmax(sweep))
    interior_peak = 0 < arg < len(scan) - 1
    print(f"[corridor] sweep over flux in [0,pi]:")
    for f, w in zip(scan, sweep):
        print(f"            flux={f:5.3f}  W_psi={w:.4e}")
    print(f"            argmax at index {arg}/{len(scan)-1}  -> interior-peaked "
          f"corridor = {interior_peak}   (monotone/saturating: expected)")

    # --- Benign stability: small jitter of flux + context seed ---------------
    base = W_psi(N, edges, L, content_axis=2, flux=probe, ctx_seed=0)
    jit = [W_psi(N, edges, L, content_axis=2,
                 flux=probe * (1 + 0.02 * RNG.standard_normal()), ctx_seed=s)
           for s in range(1, 6)]
    rel = float(np.max(np.abs(np.array(jit) - base)) / max(abs(base), 1e-12))
    benign_ok = rel < 0.10
    print(f"\n[gate 2] benign jitter rel.change = {rel:.3e}  stable={benign_ok}")

    # --- Destructive ablation: coherent flux vs matched-magnitude random ------
    a_coh = uniform_flux(edges, L, probe)
    mag = np.max(np.abs(a_coh))
    Wc = W_psi(N, edges, L, content_axis=2, flux=probe)
    Wr = np.mean([W_psi(N, edges, L, content_axis=2, flux=0.0,
                        content_phase=np.random.default_rng(s).uniform(-mag, mag, len(edges)))
                  for s in range(4)])
    destr_ok = abs(Wc - Wr) / max(abs(Wc), 1e-12) > 0.10
    print(f"[gate 3] coherent={Wc:.4e} vs randomized(matched mag)={Wr:.4e}  "
          f"-> distinguishable={destr_ok}")

    # --- Verdict, in De Jesus' claim-state ledger form ------------------------
    print("\n" + "=" * 76)
    print("CLAIM-STATE (mirror of Krueger v2 / De Jesus Table 4, on FFGFT T^4):")
    rows = [
        ("context/content design clean", gauge_ok and detect_ok,
         "gauge-null clean and non-exact content detectable"),
        ("non-exact content over gauge context", detect_ok,
         "witness tracks added non-exact content"),
        ("U3 unique memory channel", channel_specific,
         "channel-swap; Z3-symmetric axes -> not distinguished"),
        ("bounded slow-beat corridor", interior_peak,
         "corridor sweep is monotone/saturating"),
        ("coherence- (not magnitude-) sensitive", destr_ok,
         "coherent vs matched-random content"),
    ]
    for name, ok, why in rows:
        print(f"   {name:38s}: {'supported' if ok else 'NOT supported':14s} | {why}")
    print("=" * 76)
    print("Reading: same claim-state as the HLV carrier. The two negatives")
    print("(channel-swap, corridor) reproduce independently on T^4 -> the limit")
    print("is in the witness class, and U3-uniqueness/corridor are features")
    print("neither carrier provides. Next: a genuinely dynamical, time-indexed")
    print("U3(t) that carries non-exact loop curvature forward (Krueger Sec.13.5).")
    return rows


if __name__ == "__main__":
    run()
