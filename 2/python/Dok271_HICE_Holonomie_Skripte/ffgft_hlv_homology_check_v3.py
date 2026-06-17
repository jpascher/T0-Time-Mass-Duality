#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ffgft_hlv_homology_check_v3.py
==============================

Falsification prototype for the HLV vortex/boundary-mode claim-state, v3.
Self-contained (numpy + scipy).  gudhi and matplotlib are OPTIONAL: present ->
extra rigour / a figure; absent -> graceful fallback.  Keeping the hard core
dependency-free is deliberate, so any IPI reader can reproduce the result
without a build step.

What it does
------------
CHECK 1  ensemble total persistence of H_1 over a kNN filtration, HLV vs
         matched controls, with a two-sample permutation test.
CHECK 1b k-sensitivity sweep (the kNN complex depends on k, so we test
         whether separation survives several k).
CHECK 1c the decisive comparison: the whole normalised b1(eps) CURVE SHAPE,
         compared by an energy-distance permutation test.  This is what the
         winding argument needs -- not a single scalar.
CHECK 2  deformation null test HLV -> control (persistence vs drift).  If
         gudhi is present this ALSO tracks the longest-lived H_1 cycle
         (Rips persistence), which is far less circular than total
         persistence because a genuine protected cycle is a single long bar,
         not a count that is forced to 0 at the endpoint.
CHECK 3  N-scaling of the effect size: does HLV's separation from the
         CRYSTALLINE controls stabilise (structural) or vanish (finite-size
         artefact) as N grows?
--falsify  a PRE-REGISTERED consistency check (not Popperian falsification):
         at fixed N, k, p, require HLV to separate from every crystalline
         control (FCC, cubic, BCC).  PASS/WEAKENED is printed.

Honest scope: finite point-cloud diagnostic; nothing validates HLV as
physical microstructure.  H_1 is cell-shape-independent WITHIN a fixed
complex, but still depends on k and the metric -- hence the k-sweep and the
curve-shape comparison rather than a single "tessellation-free" number.

Usage
-----
    python3 ffgft_hlv_homology_check_v3.py
    python3 ffgft_hlv_homology_check_v3.py --N 280 --seeds 5 --png fig.png
    python3 ffgft_hlv_homology_check_v3.py --falsify --falsify-N 400
    python3 ffgft_hlv_homology_check_v3.py --nscaling 200,400,800
"""

import argparse
import itertools
import math
import sys

import numpy as np
from scipy.spatial import cKDTree

try:
    import gudhi as _gudhi
    HAVE_GUDHI = True
except Exception:
    HAVE_GUDHI = False

PHI = (1.0 + math.sqrt(5.0)) / 2.0
SIGMA = -1.0 / PHI
EPS_MULTS = (1.1, 1.35, 1.6, 1.85, 2.1, 2.35)


# --------------------------------------------------------------------------- #
#  Point clouds   (each: fn(n_points, seed) -> (n,3))
# --------------------------------------------------------------------------- #
def _icosahedral_projectors(tau):
    P = np.array([
        [1.0, -1.0,  0.0,  0.0,  tau,  tau],
        [tau,  tau,  1.0, -1.0,  0.0,  0.0],
        [0.0,  0.0,  tau,  tau,  1.0, -1.0],
    ])
    return P / np.linalg.norm(P, axis=0, keepdims=True)


_Z6_CACHE = {}


def _z6(box):
    if box not in _Z6_CACHE:
        g = np.arange(-box, box + 1)
        M = np.stack(np.meshgrid(*([g] * 6), indexing="ij"), axis=-1)
        _Z6_CACHE[box] = M.reshape(-1, 6).astype(float)
    return _Z6_CACHE[box]


def cut_and_project_cloud(n_points, seed=0, box=4, tau_par=PHI, tau_perp=SIGMA):
    rng = np.random.default_rng(seed)
    Ppar = _icosahedral_projectors(tau_par)
    Pperp = _icosahedral_projectors(tau_perp)
    ints = _z6(box)
    shift = rng.uniform(-0.5, 0.5, size=6)
    xperp = (ints + shift) @ Pperp.T
    order = np.argsort(np.linalg.norm(xperp, axis=1))[:n_points]
    pts = ints[order] @ Ppar.T
    return _recentre(pts + 1e-6 * rng.standard_normal(pts.shape))


def fcc_cloud(n_points, seed=0):
    m = int(math.ceil((n_points * 4) ** (1.0 / 3.0))) + 2
    base = np.array([[0, 0, 0], [0.5, 0.5, 0], [0.5, 0, 0.5], [0, 0.5, 0.5]])
    cells = np.array(list(itertools.product(range(m), repeat=3)), dtype=float)
    return _take_interior((cells[:, None, :] + base[None, :, :]).reshape(-1, 3),
                          n_points)


def bcc_cloud(n_points, seed=0):
    m = int(math.ceil((n_points * 2) ** (1.0 / 3.0))) + 2
    base = np.array([[0, 0, 0], [0.5, 0.5, 0.5]])
    cells = np.array(list(itertools.product(range(m), repeat=3)), dtype=float)
    return _take_interior((cells[:, None, :] + base[None, :, :]).reshape(-1, 3),
                          n_points)


def cubic_cloud(n_points, seed=0):
    m = int(math.ceil(n_points ** (1.0 / 3.0))) + 2
    pts = np.array(list(itertools.product(range(m), repeat=3)), dtype=float)
    return _take_interior(pts, n_points)


def jittered_cubic_cloud(n_points, seed=0, sigma=0.18):
    rng = np.random.default_rng(seed)
    return _recentre(cubic_cloud(n_points, seed)
                     + sigma * rng.standard_normal((n_points, 3)))


def random_cloud(n_points, seed=0):
    rng = np.random.default_rng(seed)
    span = n_points ** (1.0 / 3.0)
    return _recentre(rng.uniform(0, span, size=(n_points, 3)))


def generic_qc_cloud(n_points, seed=0):
    t = math.sqrt(2.0)
    return cut_and_project_cloud(n_points, seed=seed, tau_par=t, tau_perp=-1.0 / t)


def poisson_disc_cloud(n_points, seed=0):
    rng = np.random.default_rng(seed)
    span = (n_points ** (1.0 / 3.0)) * 1.15
    r = span / (n_points ** (1.0 / 3.0)) * 0.85
    cell = r / math.sqrt(3.0)
    gdim = int(math.ceil(span / cell))
    grid = -np.ones((gdim, gdim, gdim), dtype=int)
    samples, active = [], []

    def gi(p):
        return tuple(np.clip((p / cell).astype(int), 0, gdim - 1))

    def fits(p):
        if np.any(p < 0) or np.any(p >= span):
            return False
        g = gi(p)
        for a in range(max(0, g[0] - 2), min(gdim, g[0] + 3)):
            for b in range(max(0, g[1] - 2), min(gdim, g[1] + 3)):
                for c in range(max(0, g[2] - 2), min(gdim, g[2] + 3)):
                    s = grid[a, b, c]
                    if s >= 0 and np.linalg.norm(samples[s] - p) < r:
                        return False
        return True

    p0 = rng.uniform(0, span, size=3)
    samples.append(p0)
    active.append(0)
    grid[gi(p0)] = 0
    while active and len(samples) < n_points * 3:
        ai = int(rng.integers(len(active)))
        base = samples[active[ai]]
        placed = False
        for _ in range(30):
            d = rng.standard_normal(3)
            d /= np.linalg.norm(d)
            p = base + r * (1.0 + rng.random()) * d
            if fits(p):
                samples.append(p)
                grid[gi(p)] = len(samples) - 1
                active.append(len(samples) - 1)
                placed = True
                break
        if not placed:
            active.pop(ai)
    pts = np.array(samples)
    if len(pts) < n_points:
        pts = np.vstack([pts, rng.uniform(0, span, size=(n_points - len(pts), 3))])
    return _take_interior(pts, n_points)


def _recentre(pts):
    return pts - pts.mean(axis=0, keepdims=True)


def _take_interior(pts, n_points):
    pts = _recentre(pts)
    keep = np.argsort(np.linalg.norm(pts, axis=1))[:n_points]
    return _recentre(pts[keep])


GENERATORS = {
    "HLV (golden cut-project)": cut_and_project_cloud,
    "FCC (rhombic-dodeca)": fcc_cloud,
    "cubic": cubic_cloud,
    "BCC": bcc_cloud,
    "jittered cubic": jittered_cubic_cloud,
    "uniform random": random_cloud,
    "Poisson-disc (blue noise)": poisson_disc_cloud,
    "generic cut-project (sqrt2)": generic_qc_cloud,
}
CONTROLS = [n for n in GENERATORS if not n.startswith("HLV")]
CRYSTALLINE = ["FCC (rhombic-dodeca)", "cubic", "BCC"]

PALETTE = {
    "HLV (golden cut-project)": "#c0392b",
    "FCC (rhombic-dodeca)": "#2e86de",
    "cubic": "#1b1464",
    "BCC": "#16a085",
    "jittered cubic": "#e67e22",
    "uniform random": "#7f8c8d",
    "Poisson-disc (blue noise)": "#27ae60",
    "generic cut-project (sqrt2)": "#8e44ad",
}


# --------------------------------------------------------------------------- #
#  Filtration -> GF(2) homology -> Betti curve
# --------------------------------------------------------------------------- #
def knn_candidate_edges(points, k):
    n = len(points)
    tree = cKDTree(points)
    dist, idx = tree.query(points, k=k + 1)
    d0 = float(np.median(dist[:, 1]))
    seen = {}
    for i in range(n):
        for col in range(1, k + 1):
            j = int(idx[i, col])
            if j == i:
                continue
            a, b = (i, j) if i < j else (j, i)
            seen[(a, b)] = float(dist[i, col])
    return [(a, b, L) for (a, b), L in seen.items()], d0


def gf2_rank(columns):
    piv, rank = {}, 0
    for c in columns:
        while c:
            hb = c.bit_length() - 1
            p = piv.get(hb)
            if p is None:
                piv[hb] = c
                rank += 1
                break
            c ^= p
    return rank


def _components(n, edge_pairs):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for (i, j) in edge_pairs:
        ri, rj = find(i), find(j)
        if ri != rj:
            parent[ri] = rj
    return len({find(x) for x in range(n)})


def betti_at(n, edges, eps):
    adj, elist, eidx, tris = {}, [], {}, []
    for (i, j, L) in edges:
        if L <= eps:
            eidx[(i, j)] = len(elist)
            elist.append((i, j))
            adj.setdefault(i, set()).add(j)
            adj.setdefault(j, set()).add(i)
    for (i, j) in elist:
        for c in (adj.get(i, set()) & adj.get(j, set())):
            if c > j:
                tris.append((i, j, c))
    rank_d1 = n - _components(n, elist)
    d2 = [(1 << eidx[(i, j)]) | (1 << eidx[(i, c)]) | (1 << eidx[(j, c)])
          for (i, j, c) in tris]
    return (len(elist) - rank_d1) - gf2_rank(d2)


def betti_curve(points, k):
    edges, d0 = knn_candidate_edges(points, k)
    n = len(points)
    ys = np.array([betti_at(n, edges, m * d0) for m in EPS_MULTS], dtype=float)
    xs = np.array(EPS_MULTS)
    total = float(np.trapezoid(ys, xs)) if hasattr(np, "trapezoid") \
        else float(np.trapz(ys, xs))
    return ys, total


def shape_of(ys):
    return ys / (ys.sum() + 1e-9)


# --------------------------------------------------------------------------- #
#  Statistics
# --------------------------------------------------------------------------- #
def permutation_test(a, b, n_perm=4000, seed=0):
    rng = np.random.default_rng(seed)
    a, b = np.asarray(a, float), np.asarray(b, float)
    obs = a.mean() - b.mean()
    pooled = np.concatenate([a, b])
    na = len(a)
    diffs = np.empty(n_perm)
    for i in range(n_perm):
        rng.shuffle(pooled)
        diffs[i] = pooled[:na].mean() - pooled[na:].mean()
    z = obs / (diffs.std() + 1e-12)
    p = (np.sum(np.abs(diffs) >= abs(obs)) + 1) / (n_perm + 1)
    return obs, z, p


def _energy_distance(A, B):
    def md(X, Y):
        return np.mean([np.sum(np.abs(x - y)) for x in X for y in Y])
    return 2 * md(A, B) - md(A, A) - md(B, B)


def energy_perm_test(A, B, n_perm=2000, seed=0):
    rng = np.random.default_rng(seed)
    A, B = np.asarray(A, float), np.asarray(B, float)
    obs = _energy_distance(A, B)
    pool = np.vstack([A, B])
    na, idx = len(A), np.arange(len(A) + len(B))
    null = np.empty(n_perm)
    for i in range(n_perm):
        rng.shuffle(idx)
        null[i] = _energy_distance(pool[idx[:na]], pool[idx[na:]])
    p = (np.sum(null >= obs) + 1) / (n_perm + 1)
    z = (obs - null.mean()) / (null.std() + 1e-12)
    return obs, z, p


# --------------------------------------------------------------------------- #
#  gudhi: longest-lived H_1 cycle  (optional, less circular than totPers)
# --------------------------------------------------------------------------- #
def rips_max_h1_lifetime(points, max_edge):
    if not HAVE_GUDHI:
        return None
    rc = _gudhi.RipsComplex(points=points, max_edge_length=max_edge)
    st = rc.create_simplex_tree(max_dimension=2)
    st.compute_persistence()
    lifes = [d - b for (dim, (b, d)) in st.persistence()
             if dim == 1 and d != float("inf")]
    return float(max(lifes)) if lifes else 0.0


# --------------------------------------------------------------------------- #
#  Deformation null test
# --------------------------------------------------------------------------- #
def deformation_curve(cloud_hlv, cloud_target, k, steps=11, use_gudhi=False):
    n = min(len(cloud_hlv), len(cloud_target))
    a, b = cloud_hlv[:n], cloud_target[:n]
    _, d0 = knn_candidate_edges(a, k)
    max_edge = 2.0 * d0
    ts = np.linspace(0.0, 1.0, steps)
    out = []
    for t in ts:
        x = _recentre((1.0 - t) * a + t * b)
        _, total = betti_curve(x, k)
        ml = rips_max_h1_lifetime(x, max_edge) if use_gudhi else None
        out.append((float(t), total, ml))
    return out


def classify_persistence(curve, target_b1_zero=False):
    ts = np.array([c[0] for c in curve])
    val = np.array([c[1] for c in curve], float)
    frac = val / max(val[0], 1e-9)
    plateau_t = 0.0
    for t, f in zip(ts, frac):
        if f >= 0.75:
            plateau_t = t
        else:
            break
    collapsed = frac[-1] < 0.5
    if plateau_t >= 0.2 and collapsed and not target_b1_zero:
        return "PERSISTENCE", "candidate", plateau_t, float(frac[-1])
    if plateau_t < 0.12 and collapsed and not target_b1_zero:
        return "DRIFT", "rejected", plateau_t, float(frac[-1])
    return "NO ROBUST PLATEAU", "underdetermined", plateau_t, float(frac[-1])


# --------------------------------------------------------------------------- #
#  N-scaling of the effect size (HLV vs pooled crystalline shape)
# --------------------------------------------------------------------------- #
def nscaling(ladder, k, seeds):
    """Stable effect size: L1 distance between MEAN normalised Betti curves.

    (energy distance on ~4 samples is too noisy for a scaling trend; the
    mean-curve L1 distance is a smooth, interpretable separation measure.)
    """
    rows = []
    for N in ladder:
        hlv = np.mean([shape_of(betti_curve(cut_and_project_cloud(N, seed=s), k)[0])
                       for s in seeds], axis=0)
        cryst = []
        for name in CRYSTALLINE:
            cryst += [shape_of(betti_curve(GENERATORS[name](N, seed=s), k)[0])
                      for s in seeds]
        cryst = np.mean(cryst, axis=0)
        rnd = np.mean([shape_of(betti_curve(random_cloud(N, seed=s), k)[0])
                       for s in seeds], axis=0)
        e_cryst = float(np.sum(np.abs(hlv - cryst)))
        e_rand = float(np.sum(np.abs(hlv - rnd)))
        rows.append((N, e_cryst, e_rand))
    return rows


# --------------------------------------------------------------------------- #
#  Pre-registered consistency check (NOT Popperian falsification)
# --------------------------------------------------------------------------- #
def falsification_check(N, k, p_thresh, seeds):
    hlv = np.array([shape_of(betti_curve(cut_and_project_cloud(N, seed=s), k)[0])
                    for s in seeds])
    results, passed = [], True
    for name in CRYSTALLINE:
        cs = np.array([shape_of(betti_curve(GENERATORS[name](N, seed=s), k)[0])
                       for s in seeds])
        _, z, p = energy_perm_test(hlv, cs, seed=1234)
        ok = p < p_thresh
        passed = passed and ok
        results.append((name, z, p, ok))
    return passed, results


# --------------------------------------------------------------------------- #
#  Figure
# --------------------------------------------------------------------------- #
def make_figure(path, shapes_mean, energy_rows, deform, nscale_rows, meta):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as exc:
        print(f" (figure skipped: {exc})")
        return False

    plt.rcParams.update({
        "font.size": 9, "axes.titlesize": 10, "axes.titleweight": "bold",
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.grid": True, "grid.alpha": 0.25, "figure.dpi": 130,
    })
    fig, ax = plt.subplots(2, 2, figsize=(11.5, 7.6), constrained_layout=True)
    fig.suptitle("FFGFT / HLV homology check  v3   "
                 f"(N={meta['N']}, k={meta['k']}, {meta['seeds']} seeds"
                 f"{', gudhi' if meta['gudhi'] else ''})",
                 fontsize=12, fontweight="bold")

    # Panel A: mean normalised Betti curves
    a = ax[0, 0]
    xs = np.array(EPS_MULTS)
    for name, ys in shapes_mean.items():
        is_hlv = name.startswith("HLV")
        a.plot(xs, ys, marker="o", ms=3.5,
               lw=2.6 if is_hlv else 1.3,
               color=PALETTE[name], alpha=1.0 if is_hlv else 0.75,
               zorder=5 if is_hlv else 2, label=name)
    a.set_title("A · Normalised Betti curve  b1(eps)  — shape, not magnitude")
    a.set_xlabel("eps / d0"), a.set_ylabel("normalised b1")
    a.legend(fontsize=6.5, ncol=1, loc="upper right", framealpha=0.9)

    # Panel B: CHECK 1c energy distances
    b = ax[0, 1]
    names = [r[0] for r in energy_rows]
    dists = [r[1] for r in energy_rows]
    ps = [r[3] for r in energy_rows]
    order = np.argsort(dists)
    names = [names[i] for i in order]
    dists = [dists[i] for i in order]
    ps = [ps[i] for i in order]
    ypos = np.arange(len(names))
    b.barh(ypos, dists, color=[PALETTE[n] for n in names], alpha=0.85)
    for y, d, p in zip(ypos, dists, ps):
        b.text(d, y, f"  p={p:.3f}{'*' if p < 0.05 else ''}",
               va="center", fontsize=7)
    b.set_yticks(ypos)
    b.set_yticklabels(names, fontsize=7)
    b.set_title("B · Curve-shape separation: energy distance HLV vs control")
    b.set_xlabel("energy distance  (larger = more distinct from HLV)")

    # Panel C: deformation null test
    c = ax[1, 0]
    for target, curve in deform.items():
        ts = [p[0] for p in curve]
        tp = np.array([p[1] for p in curve])
        tp = tp / max(tp[0], 1e-9)
        col = PALETTE.get(target, "#555")
        c.plot(ts, tp, marker="o", ms=3.5, lw=2.0, color=col,
               label=f"totPers  HLV->{target.split(' (')[0]}")
        mls = [p[2] for p in curve]
        if all(m is not None for m in mls):
            mls = np.array(mls)
            mls = mls / max(mls[0], 1e-9)
            c.plot(ts, mls, marker="s", ms=3, lw=1.6, ls="--", color=col,
                   alpha=0.7,
                   label=f"max H1 life  HLV->{target.split(' (')[0]}")
    c.axhspan(0.75, 1.02, color="#f1c40f", alpha=0.12)
    c.text(0.02, 0.97, "plateau band", fontsize=6.5, color="#b7950b", va="top")
    c.set_title("C · Deformation null test  (persistence vs drift)")
    c.set_xlabel("deformation t   (0 = HLV, 1 = control)")
    c.set_ylabel("value / value(t=0)")
    c.legend(fontsize=6.5, loc="upper right")

    # Panel D: N-scaling effect size
    d = ax[1, 1]
    Ns = [r[0] for r in nscale_rows]
    ec = [r[1] for r in nscale_rows]
    er = [r[2] for r in nscale_rows]
    d.plot(Ns, ec, marker="o", lw=2.2, color="#c0392b",
           label="HLV vs crystalline (FCC/cubic/BCC)")
    d.plot(Ns, er, marker="s", lw=1.8, color="#7f8c8d",
           label="HLV vs uniform random")
    d.set_title("D · N-scaling of effect size  (stabilise = structural)")
    d.set_xlabel("N points / cloud"), d.set_ylabel("mean-shape L1 distance")
    d.set_xscale("log")
    d.legend(fontsize=7, loc="best")

    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    return True


# --------------------------------------------------------------------------- #
#  Main
# --------------------------------------------------------------------------- #
def main(argv=None):
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--N", type=int, default=260)
    ap.add_argument("--seeds", type=int, default=5)
    ap.add_argument("--klist", type=str, default="10,14,18")
    ap.add_argument("--seed0", type=int, default=20260613)
    ap.add_argument("--steps", type=int, default=11)
    ap.add_argument("--nscaling", type=str, default="200,400,800")
    ap.add_argument("--falsify", action="store_true")
    ap.add_argument("--falsify-N", type=int, default=400)
    ap.add_argument("--falsify-p", type=float, default=0.01)
    ap.add_argument("--csv", type=str, default="")
    ap.add_argument("--png", type=str, default="ffgft_hlv_v3.png")
    ap.add_argument("--no-plot", action="store_true")
    args = ap.parse_args(argv)

    klist = [int(x) for x in args.klist.split(",")]
    seeds = [args.seed0 + s for s in range(args.seeds)]
    k_main = klist[len(klist) // 2]

    print("=" * 78)
    print(" FFGFT / HLV  homology check  v3")
    print("=" * 78)
    print(f" N={args.N}/cloud  seeds={args.seeds}  k_list={klist}  k_main={k_main}"
          f"  gudhi={'yes' if HAVE_GUDHI else 'no'}")
    print(" H_1 is cell-shape-independent WITHIN a fixed complex; it still")
    print(" depends on k and the metric -> hence k-sweep + curve-shape test.")
    print(" Finite diagnostic only; no physical-spacetime claim.")
    print()

    clouds = {name: [GENERATORS[name](args.N, seed=s) for s in seeds]
              for name in GENERATORS}
    curves_main = {name: [betti_curve(c, k_main) for c in clouds[name]]
                   for name in GENERATORS}
    tp_by_k = {k_main: {name: np.array([t for (_, t) in curves_main[name]])
                        for name in GENERATORS}}
    for k in klist:
        if k != k_main:
            tp_by_k[k] = {name: np.array([betti_curve(c, k)[1]
                                          for c in clouds[name]])
                          for name in GENERATORS}
    csv_rows = [("section", "cloud", "k", "metric", "value")]

    # CHECK 1
    print("-" * 78)
    print(f" CHECK 1 : ensemble total persistence @ k={k_main}")
    print("-" * 78)
    tp = tp_by_k[k_main]
    hlv = tp["HLV (golden cut-project)"]
    print(f" {'cloud':<30} {'meanTP':>8} {'std':>6}   vs HLV: z      p")
    print(f" {'HLV (golden cut-project)':<30} {hlv.mean():>8.2f} {hlv.std():>6.2f}"
          f"   (reference)")
    sep1 = []
    for name in CONTROLS:
        v = tp[name]
        _, z, p = permutation_test(hlv, v, seed=args.seed0)
        ok = (hlv.mean() > v.mean()) and (p < 0.05)
        sep1.append(ok)
        print(f" {name:<30} {v.mean():>8.2f} {v.std():>6.2f}   z={z:>6.2f}"
              f"  p={p:.4f}{'  *' if ok else ''}")
        csv_rows.append(("check1", name, k_main, "meanTP", f"{v.mean():.4f}"))
    print(f"\n CHECK 1 claim-state: "
          f"{'candidate' if all(sep1) else 'underdetermined'}  "
          f"(scalar totPers is a coarse, k-sensitive measure -- see 1c)")
    print()

    # CHECK 1b
    print("-" * 78)
    print(" CHECK 1b: k-sensitivity")
    print("-" * 78)
    print(f" {'k':>4} | HLV meanTP | control band [min,max] | above band?")
    ksurv = []
    for k in klist:
        h = tp_by_k[k]["HLV (golden cut-project)"].mean()
        cm = [tp_by_k[k][n].mean() for n in CONTROLS]
        above = h > max(cm)
        ksurv.append(above)
        print(f" {k:>4} | {h:>10.2f} | [{min(cm):>6.2f},{max(cm):>6.2f}]"
              f"       | {'YES' if above else 'no'}")
    print(f"\n k-robustness (scalar): {sum(ksurv)}/{len(klist)}"
          f" -> {'robust' if all(ksurv) else 'k-sensitive (use shape, 1c)'}")
    print()

    # CHECK 1c
    print("-" * 78)
    print(" CHECK 1c: Betti-curve SHAPE vs controls (energy permutation test)")
    print("-" * 78)
    shapes = {name: np.array([shape_of(ys) for (ys, _) in curves_main[name]])
              for name in GENERATORS}
    hlv_shapes = shapes["HLV (golden cut-project)"]
    print(f" {'cloud':<30} {'energyDist':>10} {'z':>6} {'p':>8}")
    energy_rows, sep1c = [], []
    for name in CONTROLS:
        obs, z, p = energy_perm_test(hlv_shapes, shapes[name], seed=args.seed0)
        ok = p < 0.05
        sep1c.append(ok)
        energy_rows.append((name, obs, z, ok and p or p))
        print(f" {name:<30} {obs:>10.4f} {z:>6.2f} {p:>8.4f}{'  *' if ok else ''}")
        csv_rows.append(("check1c", name, k_main, "energy", f"{obs:.4f}"))
    n_sep = sum(sep1c)
    cryst_sep = all(p_ok for nm, _, _, p_ok in energy_rows if nm in CRYSTALLINE)
    print(f"\n CHECK 1c claim-state: "
          + ("candidate (separates from ALL controls)" if n_sep == len(CONTROLS)
             else f"partial candidate ({n_sep}/{len(CONTROLS)} controls)"))
    print(f"   crystalline controls (FCC/cubic/BCC) separated: "
          f"{'YES' if cryst_sep else 'no'}")
    print("   honest reading: sharp vs crystalline, weaker vs disordered/QC ->")
    print("   signal = 'quasiperiodic cut-project shape', not specifically golden.")
    shapes_mean = {name: shapes[name].mean(axis=0) for name in GENERATORS}
    print()

    # CHECK 2
    print("-" * 78)
    print(f" CHECK 2 : deformation null test @ k={k_main}"
          f"{'  (+ gudhi max-H1-lifetime)' if HAVE_GUDHI else ''}")
    print("-" * 78)
    deform = {}
    for target in ["uniform random", "Poisson-disc (blue noise)"]:
        m = min(len(seeds), 3)
        accT = None
        accL = None
        for s in range(m):
            cur = deformation_curve(clouds["HLV (golden cut-project)"][s],
                                    clouds[target][s], k_main, steps=args.steps,
                                    use_gudhi=HAVE_GUDHI)
            T = np.array([c[1] for c in cur])
            accT = T if accT is None else accT + T
            if HAVE_GUDHI:
                L = np.array([c[2] for c in cur])
                accL = L if accL is None else accL + L
        accT /= m
        ts = np.linspace(0, 1, args.steps)
        if HAVE_GUDHI:
            accL /= m
            curve = list(zip(ts.tolist(), accT.tolist(), accL.tolist()))
        else:
            curve = list(zip(ts.tolist(), accT.tolist(), [None] * len(ts)))
        deform[target] = curve
        verdict, state, plat, endf = classify_persistence(curve)
        print(f"\n  HLV -> {target}   (avg {m} pairings)")
        base = max(accT[0], 1e-9)
        for c in curve:
            t, val = c[0], c[1]
            extra = f"   maxH1life={c[2]:.3f}" if c[2] is not None else ""
            print(f"   t={t:>4.2f}  totPers={val:>7.2f}  "
                  f"{'#' * int(round(30 * val / base))}{extra}")
        print(f"   plateau up to t={plat:.2f}, end frac={endf:.2f}"
              f"  -> {verdict} ({state})")
    print()

    # CHECK 3: N-scaling
    print("-" * 78)
    print(" CHECK 3 : N-scaling of effect size (stabilise=structural, vanish=artefact)")
    print("-" * 78)
    ladder = [int(x) for x in args.nscaling.split(",")]
    big = [N for N in ladder if N > 1000]
    if big:
        print(f" note: N>{1000} ({big}) is slow -- run those offline.")
    ns_seeds = seeds[:min(len(seeds), 4)]
    nscale_rows = nscaling(ladder, k_main, ns_seeds)
    print(f" {'N':>6} | {'HLV vs crystalline':>18} | {'HLV vs random':>14}")
    for (N, ec, er) in nscale_rows:
        print(f" {N:>6} | {ec:>18.4f} | {er:>14.4f}")
        csv_rows.append(("nscaling", "HLV_vs_crystalline", k_main, f"N={N}",
                         f"{ec:.4f}"))
    trend = ("grows" if nscale_rows[-1][1] > nscale_rows[0][1] * 1.15
             else "vanishes" if nscale_rows[-1][1] < nscale_rows[0][1] * 0.85
             else "stable")
    print(f"\n crystalline-separation effect size: {trend} with N"
          f"  -> {'structural candidate' if trend in ('grows', 'stable') else 'finite-size artefact'}")
    print()

    # optional pre-registered consistency check
    if args.falsify:
        print("-" * 78)
        print(" PRE-REGISTERED CONSISTENCY CHECK  (NOT Popperian falsification)")
        print("-" * 78)
        print(f" pre-set: N={args.falsify_N}, k={k_main}, p<{args.falsify_p},"
              f" crystalline controls {CRYSTALLINE}")
        passed, res = falsification_check(args.falsify_N, k_main, args.falsify_p,
                                          seeds)
        for (name, z, p, ok) in res:
            print(f"   HLV vs {name:<24} z={z:>6.2f} p={p:.4f}"
                  f"  {'pass' if ok else 'FAIL'}")
        print(f"\n RESULT: {'PASS (consistent with a distinct-topology claim)' if passed else 'WEAKENED (claim not supported at this pre-set)'}")
        print(" Interpretation: a consistency check. A negative result weakens")
        print(" the claim but does not logically falsify it in the Popperian sense.")
        print()

    # figure
    if not args.no_plot:
        meta = {"N": args.N, "k": k_main, "seeds": args.seeds, "gudhi": HAVE_GUDHI}
        if make_figure(args.png, shapes_mean, energy_rows, deform, nscale_rows, meta):
            print(f" Figure written: {args.png}")

    if args.csv:
        with open(args.csv, "w") as fh:
            for r in csv_rows:
                fh.write(",".join(str(x) for x in r) + "\n")
        print(f" CSV written: {args.csv}")

    print("=" * 78)
    print(" Done. Verdicts are CANDIDATE at best; require larger N, more seeds,")
    print(" and independent reproduction before any promotion.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
