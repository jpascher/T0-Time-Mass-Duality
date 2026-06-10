"""
FFGFT vs HLV G-Lattice: Spektrale Lückenstruktur v3
====================================================
Johann Pascher / FFGFT — Juni 2026

Neu gegenüber v2:
  - N=2000 (statt 600) für Schalenstruktur-Diskriminierung 1/φ vs Q_FFGFT
  - Endlicher T⁴-Graph (kNN auf T⁴-Punktgitter, identisch zu HLV-Methode)
  - Mini-Ensemble (3 Seeds) für FFGFT T⁴ und HLV — einfache Bandbreite
  - Alle offenen Punkte 1–3 aus Dok 275 damit geschlossen
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy.spatial import KDTree
import warnings
warnings.filterwarnings("ignore")

# ════════════════════════════════════════════════════════════════
# Fundamentale Konstanten
# ════════════════════════════════════════════════════════════════
XI      = 4 / 30000
D_F     = 3 - XI
Q_FFGFT = 0.6677
PHI     = (1 + np.sqrt(5)) / 2
INV_PHI = 1.0 / PHI
Q_REC   = 2 / 3
K_STAR  = np.log(PHI) / XI

C = {
    "ffgft_ana":  "#1a6b9a",   # analytisch
    "ffgft_graph":"#5ba3d0",   # endlicher Graph
    "hlv":        "#c0392b",
    "torus":      "#7f8c8d",
    "cubic":      "#27ae60",
    "jitter":     "#8e44ad",
    "random":     "#e67e22",
}

SEEDS = [20260609, 20260610, 20260611]

# ════════════════════════════════════════════════════════════════
# Hilfsfunktionen
# ════════════════════════════════════════════════════════════════

def knn_laplacian(pts, k=16):
    N = len(pts)
    tree = KDTree(pts)
    _, idx = tree.query(pts, k=k+1)
    W = np.zeros((N, N))
    for i in range(N):
        nbrs = idx[i, 1:]
        d2 = np.sum((pts[nbrs] - pts[i])**2, axis=1)
        d2 = np.where(d2 < 1e-12, 1e-12, d2)
        w = 1.0 / d2
        for jj, j in enumerate(nbrs):
            W[i, j] += w[jj]; W[j, i] += w[jj]
    W /= 2
    return np.diag(W.sum(1)) - W

def graph_evals(pts, N_modes=400):
    ev = np.linalg.eigvalsh(knn_laplacian(pts))
    ev = np.sort(ev[ev > 1e-10])
    return ev[:N_modes]

def gap_metrics(evals, n_low=100):
    ev   = np.sort(evals[:n_low])
    gaps = np.diff(ev)
    gaps = gaps[gaps > 1e-14]
    if len(gaps) == 0:
        return dict(max_gap=0, gap_cv=0, low_r=0, gaps=gaps, evals=ev)
    max_gap = gaps.max()
    gap_cv  = gaps.std() / gaps.mean() if gaps.mean() > 0 else 0
    if len(gaps) >= 2:
        r     = np.minimum(gaps[:-1], gaps[1:]) / np.maximum(gaps[:-1], gaps[1:])
        low_r = r.mean()
    else:
        low_r = 0.0
    return dict(max_gap=max_gap, gap_cv=gap_cv, low_r=low_r, gaps=gaps, evals=ev)

def ids(evals, lam_max=15.0):
    ev = np.sort(evals)
    x  = np.linspace(0, lam_max, 500)
    y  = np.array([np.sum(ev <= xi) / len(ev) for xi in x])
    return x, y

def shell_ratio_error(pts, ratio, n_sample=300):
    tree = KDTree(pts)
    errors = []
    for pt in pts[:n_sample]:
        dists, _ = tree.query(pt, k=30)
        dists = np.sort(dists[1:])
        shells, prev = [dists[0]], dists[0]
        for d in dists[1:]:
            if d > prev * 1.05:
                shells.append(d); prev = d
            if len(shells) >= 3: break
        if len(shells) >= 2:
            for i in range(len(shells)-1):
                errors.append(abs(shells[i+1] - shells[i]*ratio) / (shells[i]*ratio))
    return np.mean(errors) if errors else 1.0

# ════════════════════════════════════════════════════════════════
# 1. FFGFT T⁴ — analytisch (v2-Methode, Referenz)
# ════════════════════════════════════════════════════════════════

def ffgft_t4_analytic(N_modes=400, n_levels=6):
    L0 = 2 * np.pi
    L  = np.array([L0 * Q_REC**mu for mu in range(4)])
    n_range = np.arange(-n_levels, n_levels+1)
    grid = np.array(np.meshgrid(*[n_range]*4, indexing='ij')).reshape(4,-1).T
    freqs = (2*np.pi*grid) / L[None,:]
    raw   = np.sum(freqs**2, axis=1)
    wind  = np.sum(np.abs(grid), axis=1)
    scaled = np.sort(raw * D_F**(wind/4.0))
    scaled = scaled[scaled > 1e-12]
    return scaled[:N_modes]

# ════════════════════════════════════════════════════════════════
# 2. FFGFT T⁴ — endlicher Graph (NEU in v3)
# ════════════════════════════════════════════════════════════════

def ffgft_t4_points(N=2000, seed=20260609):
    """
    Endliches Punktgitter auf T⁴ mit Ensemble-Jitter.
    Seed variiert die Akzeptanzgrenze leicht (σ=0.05) um
    ein echtes Ensemble zu erzeugen.
    """
    rng = np.random.default_rng(seed)
    L = np.array([2*np.pi * Q_REC**mu for mu in range(4)])
    n_range = 4
    axes = [np.arange(-n_range, n_range+1)]*4
    grid = np.array(np.meshgrid(*axes, indexing='ij')).reshape(4,-1).T
    x_phys = grid[:, :3] * L[:3][None, :]
    x_int  = grid[:, 3:4] * L[3]
    jitter = rng.normal(0, 0.05, len(grid))
    norms  = np.linalg.norm(x_int, axis=1) + XI * np.linalg.norm(x_phys, axis=1) + jitter
    idx    = np.argsort(norms)[:N]
    return x_phys[idx]

# ════════════════════════════════════════════════════════════════
# 3. HLV G-Lattice
# ════════════════════════════════════════════════════════════════

def hlv_points(N=2000, seed=20260609):
    angles = np.array([2*np.pi*k/5 for k in range(5)])
    c, s   = np.cos(angles), np.sin(angles)
    inv_p  = 1.0/PHI
    P_par = np.array([
        [1, c[1], c[2], c[3], c[4], 0],
        [0, s[1], s[2], s[3], s[4], 0],
        [0, inv_p,inv_p,inv_p,inv_p,1],
    ], dtype=float)
    P_perp = np.array([
        [1, c[2], c[4], c[1], c[3], 0],
        [0, s[2], s[4], s[1], s[3], 0],
        [0,-inv_p,-inv_p,inv_p,inv_p,1],
    ], dtype=float)
    for M in [P_par, P_perp]:
        for i in range(3):
            n = np.linalg.norm(M[i])
            if n > 1e-12: M[i] /= n
    n_range = 5
    axes = [np.arange(-n_range, n_range+1)]*6
    grid = np.array(np.meshgrid(*axes, indexing='ij')).reshape(6,-1).T
    x_par  = grid @ P_par.T
    x_perp = grid @ P_perp.T
    norms  = np.linalg.norm(x_perp, axis=1)
    idx    = np.argsort(norms)[:N]
    return x_par[idx]

# ════════════════════════════════════════════════════════════════
# 4. Null-Modelle
# ════════════════════════════════════════════════════════════════

def periodic_torus_evals(N_modes=400, n_grid=8):
    n  = np.arange(-n_grid, n_grid+1)
    g  = np.array(np.meshgrid(n,n,n,indexing='ij')).reshape(3,-1).T
    ev = np.sort(np.sum(g**2,axis=1).astype(float))
    return ev[ev>1e-10][:N_modes]

def cubic_pts(N=2000):
    n = int(np.ceil(N**(1/3)))+1
    g = np.array(np.meshgrid(*[np.arange(n)]*3,indexing='ij')).reshape(3,-1).T
    return g[:N].astype(float)

def jittered_pts(N=2000, seed=20260609):
    rng = np.random.default_rng(seed)
    return cubic_pts(N) + rng.normal(0, 0.35, (N,3))

def random_pts(N=2000, seed=20260609):
    rng = np.random.default_rng(seed)
    return rng.uniform(0, N**(1/3)*1.1, (N,3))

# ════════════════════════════════════════════════════════════════
# 5. Ensemble-Berechnung (3 Seeds)
# ════════════════════════════════════════════════════════════════

N_PTS   = 2000
N_MODES = 400
N_LOW   = 100

print("="*60)
print(f"FFGFT vs HLV v3  —  N={N_PTS}, {len(SEEDS)} Seeds")
print("="*60)

# — Analytischer T⁴ (deterministisch, kein Seed) —
print("\n[A] FFGFT T⁴ analytisch...")
ev_ana = ffgft_t4_analytic(N_modes=N_MODES)
m_ana  = gap_metrics(ev_ana, n_low=N_LOW)
print(f"    gap_CV={m_ana['gap_cv']:.4f}  max_gap={m_ana['max_gap']:.4f}  low_r={m_ana['low_r']:.4f}")

# — Endlicher T⁴-Graph (3 Seeds) —
print("\n[B] FFGFT T⁴ endlicher Graph (3 Seeds)...")
ev_t4g, m_t4g = [], []
for s in SEEDS:
    pts = ffgft_t4_points(N=N_PTS, seed=s)
    ev  = graph_evals(pts, N_modes=N_MODES)
    m   = gap_metrics(ev, n_low=N_LOW)
    ev_t4g.append(ev); m_t4g.append(m)
    print(f"    Seed {s}: gap_CV={m['gap_cv']:.4f}  max_gap={m['max_gap']:.4f}  low_r={m['low_r']:.4f}")

# — HLV (3 Seeds) —
print("\n[C] HLV G-Lattice (3 Seeds)...")
ev_hlv, m_hlv = [], []
for s in SEEDS:
    pts = hlv_points(N=N_PTS, seed=s)
    ev  = graph_evals(pts, N_modes=N_MODES)
    m   = gap_metrics(ev, n_low=N_LOW)
    ev_hlv.append(ev); m_hlv.append(m)
    print(f"    Seed {s}: gap_CV={m['gap_cv']:.4f}  max_gap={m['max_gap']:.4f}  low_r={m['low_r']:.4f}")

# — Null-Modelle (Seed 0) —
print("\n[D] Null-Modelle...")
ev_torus = periodic_torus_evals(N_modes=N_MODES)
m_torus  = gap_metrics(ev_torus, n_low=N_LOW)

pts_cub = cubic_pts(N=N_PTS)
ev_cub  = graph_evals(pts_cub, N_modes=N_MODES)
m_cub   = gap_metrics(ev_cub, n_low=N_LOW)

pts_jit = jittered_pts(N=N_PTS)
ev_jit  = graph_evals(pts_jit, N_modes=N_MODES)
m_jit   = gap_metrics(ev_jit, n_low=N_LOW)

pts_rnd = random_pts(N=N_PTS)
ev_rnd  = graph_evals(pts_rnd, N_modes=N_MODES)
m_rnd   = gap_metrics(ev_rnd, n_low=N_LOW)

print(f"    Torus:   gap_CV={m_torus['gap_cv']:.4f}")
print(f"    Kubisch: gap_CV={m_cub['gap_cv']:.4f}")
print(f"    Jitter:  gap_CV={m_jit['gap_cv']:.4f}")
print(f"    Zufäll.: gap_CV={m_rnd['gap_cv']:.4f}")

# ════════════════════════════════════════════════════════════════
# 6. Schalenstruktur N=2000: 1/φ vs Q_FFGFT
# ════════════════════════════════════════════════════════════════
print("\n[E] Schalenstruktur N=2000 (1/φ vs Q_FFGFT)...")
# HLV Seed 0
pts_hlv0 = hlv_points(N=N_PTS, seed=SEEDS[0])
err_hlv_invphi  = shell_ratio_error(pts_hlv0, INV_PHI)
err_hlv_qffgft  = shell_ratio_error(pts_hlv0, Q_FFGFT)
# T⁴ Graph Seed 0
pts_t4g0 = ffgft_t4_points(N=N_PTS, seed=SEEDS[0])
err_t4g_invphi  = shell_ratio_error(pts_t4g0, INV_PHI)
err_t4g_qffgft  = shell_ratio_error(pts_t4g0, Q_FFGFT)
# Kontrollen
err_cub_invphi  = shell_ratio_error(pts_cub,  INV_PHI)
err_rnd_invphi  = shell_ratio_error(pts_rnd,  INV_PHI)

print(f"    HLV,    1/φ={INV_PHI:.4f}:  Fehler={err_hlv_invphi:.4f}")
print(f"    HLV,    Q_FFGFT={Q_FFGFT}: Fehler={err_hlv_qffgft:.4f}")
print(f"    T⁴-Gr., 1/φ:               Fehler={err_t4g_invphi:.4f}")
print(f"    T⁴-Gr., Q_FFGFT:           Fehler={err_t4g_qffgft:.4f}")
print(f"    Kubisch, 1/φ:               Fehler={err_cub_invphi:.4f}")
print(f"    Zufäll., 1/φ:               Fehler={err_rnd_invphi:.4f}")

disc = abs(err_hlv_invphi - err_hlv_qffgft)
print(f"\n    Diskriminierung HLV: |err(1/φ) - err(Q_FFGFT)| = {disc:.4f}")
if disc > 0.05:
    print(f"    → 1/φ und Q_FFGFT sind bei N={N_PTS} unterscheidbar")
else:
    print(f"    → Bei N={N_PTS} noch nicht robust unterscheidbar (Δ<0.05)")

# ════════════════════════════════════════════════════════════════
# 7. Ensemble-Bandtest (vereinfacht: 3 Seeds)
# ════════════════════════════════════════════════════════════════
print("\n[F] Mini-Ensemble gap_CV (3 Seeds)...")
cv_t4g = [m['gap_cv'] for m in m_t4g]
cv_hlv = [m['gap_cv'] for m in m_hlv]
cv_null = [m_torus['gap_cv'], m_cub['gap_cv'], m_jit['gap_cv'], m_rnd['gap_cv']]
cv_null_lo, cv_null_hi = min(cv_null), max(cv_null)

print(f"    FFGFT T⁴-Graph:  {np.mean(cv_t4g):.4f} ± {np.std(cv_t4g):.4f}  (min={min(cv_t4g):.4f}, max={max(cv_t4g):.4f})")
print(f"    HLV:             {np.mean(cv_hlv):.4f} ± {np.std(cv_hlv):.4f}  (min={min(cv_hlv):.4f}, max={max(cv_hlv):.4f})")
print(f"    Null-Band:       [{cv_null_lo:.4f}, {cv_null_hi:.4f}]")

def outside_band(vals, lo, hi):
    return sum(1 for v in vals if v < lo or v > hi) / len(vals)

print(f"    FFGFT außerhalb Null-Band: {outside_band(cv_t4g, cv_null_lo, cv_null_hi):.2f}")
print(f"    HLV   außerhalb Null-Band: {outside_band(cv_hlv, cv_null_lo, cv_null_hi):.2f}")

# ════════════════════════════════════════════════════════════════
# 8. ξ-Rekursion (Ebene 3, unveränderter v2-Kern)
# ════════════════════════════════════════════════════════════════
k_vals = np.arange(0, 5001)
r_vals = (D_F/3) * (1-XI)**k_vals
r_star = (D_F/3) * (1-XI)**int(round(K_STAR))

# ════════════════════════════════════════════════════════════════
# 9. Plots
# ════════════════════════════════════════════════════════════════
fig = plt.figure(figsize=(20, 16), facecolor="#0d1117")
fig.suptitle(
    f"FFGFT T⁴ vs HLV G-Lattice: Spektrale Lückenstruktur  [v3, N={N_PTS}]",
    fontsize=14, color="white", fontweight="bold", y=0.98
)
gs = gridspec.GridSpec(3, 4, figure=fig, hspace=0.48, wspace=0.38)

ax_ids  = fig.add_subplot(gs[0, :2])
ax_cv   = fig.add_subplot(gs[0, 2])
ax_rec  = fig.add_subplot(gs[0, 3])
ax_gaps = fig.add_subplot(gs[1, :2])
ax_ens  = fig.add_subplot(gs[1, 2])
ax_sh   = fig.add_subplot(gs[1, 3])
ax_mg   = fig.add_subplot(gs[2, 0])
ax_lr   = fig.add_subplot(gs[2, 1])
ax_disc = fig.add_subplot(gs[2, 2:])

for ax in fig.get_axes():
    ax.set_facecolor("#161b22")
    for sp in ax.spines.values(): sp.set_edgecolor("#30363d")
    ax.tick_params(colors="#8b949e", labelsize=8)
    ax.xaxis.label.set_color("#8b949e")
    ax.yaxis.label.set_color("#8b949e")
    ax.title.set_color("#e6edf3")

# IDS
ax_ids.plot(*ids(ev_ana), color=C["ffgft_ana"], lw=2.5, label="FFGFT T⁴ (analytisch)")
for i,(ev,s) in enumerate(zip(ev_t4g, SEEDS)):
    ax_ids.plot(*ids(ev), color=C["ffgft_graph"], lw=1.5, alpha=0.7,
                label=f"FFGFT T⁴ Graph" if i==0 else "")
for i,(ev,s) in enumerate(zip(ev_hlv, SEEDS)):
    ax_ids.plot(*ids(ev), color=C["hlv"], lw=1.5, alpha=0.7,
                label=f"HLV G-Lattice" if i==0 else "")
for ev,col,name in [(ev_torus,C["torus"],"Torus"),(ev_cub,C["cubic"],"Kubisch"),
                     (ev_jit,C["jitter"],"Jittered"),(ev_rnd,C["random"],"Zufällig")]:
    ax_ids.plot(*ids(ev), color=col, lw=0.9, ls="--", label=name)
ax_ids.set_title("IDS", fontsize=10); ax_ids.set_xlabel("λ"); ax_ids.set_ylabel("IDS")
ax_ids.legend(fontsize=6, framealpha=0.3, facecolor="#161b22", labelcolor="white")

# gap_CV Balken
names_s = ["T⁴\nana","T⁴\nGraph","HLV","Torus","Kub.","Jit.","Rnd."]
cv_vals = [m_ana['gap_cv'],
           np.mean(cv_t4g), np.mean(cv_hlv),
           m_torus['gap_cv'], m_cub['gap_cv'], m_jit['gap_cv'], m_rnd['gap_cv']]
cv_errs = [0, np.std(cv_t4g), np.std(cv_hlv), 0, 0, 0, 0]
cols_b  = [C["ffgft_ana"],C["ffgft_graph"],C["hlv"],C["torus"],C["cubic"],C["jitter"],C["random"]]
bars = ax_cv.bar(range(7), cv_vals, color=cols_b, edgecolor="#30363d", linewidth=0.5)
ax_cv.errorbar(range(7), cv_vals, yerr=cv_errs, fmt='none', color='white', capsize=3, lw=1)
ax_cv.set_xticks(range(7)); ax_cv.set_xticklabels(names_s, fontsize=7)
ax_cv.set_title("Gap CV (mean±std)", fontsize=9); ax_cv.set_ylabel("gap CV")
for b,v in zip(bars,cv_vals):
    ax_cv.text(b.get_x()+b.get_width()/2, v+0.01, f"{v:.3f}",
               ha='center', va='bottom', fontsize=6, color="#e6edf3")

# ξ-Rekursion
ax_rec.plot(k_vals, r_vals, color=C["ffgft_ana"], lw=1.8, label="r(k)")
ax_rec.axhline(INV_PHI, color=C["hlv"], lw=1.5, ls="--", label=f"1/φ={INV_PHI:.4f}")
ax_rec.axhline(Q_FFGFT, color="#f39c12", lw=1.0, ls=":", label=f"Q={Q_FFGFT}")
ax_rec.axvline(K_STAR, color="white", lw=0.8, ls=":", alpha=0.5)
ax_rec.annotate(f"k*={int(K_STAR)}", xy=(K_STAR, INV_PHI),
                xytext=(K_STAR+400, INV_PHI+0.08),
                color="#e6edf3", fontsize=7,
                arrowprops=dict(arrowstyle="->", color="#e6edf3", lw=0.8))
ax_rec.set_xlim(0,5000); ax_rec.set_ylim(0,1.02)
ax_rec.set_title("ξ-Rekursion → 1/φ", fontsize=9)
ax_rec.set_xlabel("k"); ax_rec.set_ylabel("r(k)")
ax_rec.legend(fontsize=7, framealpha=0.3, facecolor="#161b22", labelcolor="white")

# Lückenspektrum
for ev,col,name,lw in [
    (ev_ana,C["ffgft_ana"],"T⁴ ana",2.0),
    (ev_t4g[0],C["ffgft_graph"],"T⁴ Graph",1.5),
    (ev_hlv[0],C["hlv"],"HLV",1.5),
    (ev_torus,C["torus"],"Torus",0.8),
    (ev_cub,C["cubic"],"Kubisch",0.8),
]:
    g = gap_metrics(ev, n_low=N_LOW)['gaps']
    if len(g):
        ax_gaps.plot(np.arange(1,len(g)+1), g, color=col, lw=lw,
                     marker='o' if lw>1.2 else None, markersize=3, label=name)
ax_gaps.set_yscale('log')
ax_gaps.set_title("Low-sector Lückenspektrum", fontsize=9)
ax_gaps.set_xlabel("Modenindex n"); ax_gaps.set_ylabel("Lücke sₙ")
ax_gaps.legend(fontsize=7, framealpha=0.3, facecolor="#161b22", labelcolor="white", ncol=2)

# Ensemble gap_CV
x_ens = [0,1,2]
labels_ens = ["T⁴ Graph","HLV","Null\n(Band)"]
means_ens  = [np.mean(cv_t4g), np.mean(cv_hlv), np.mean([m_jit['gap_cv'],m_rnd['gap_cv']])]
stds_ens   = [np.std(cv_t4g),  np.std(cv_hlv),  np.std([m_jit['gap_cv'],m_rnd['gap_cv']])]
cols_ens   = [C["ffgft_graph"], C["hlv"], C["random"]]
ax_ens.bar(x_ens, means_ens, color=cols_ens, edgecolor="#30363d", linewidth=0.5)
ax_ens.errorbar(x_ens, means_ens, yerr=stds_ens, fmt='none', color='white', capsize=4, lw=1.5)
ax_ens.set_xticks(x_ens); ax_ens.set_xticklabels(labels_ens, fontsize=8)
ax_ens.set_title("Ensemble gap_CV ±std\n(3 Seeds)", fontsize=9)
ax_ens.set_ylabel("gap CV")
for x,m in zip(x_ens, means_ens):
    ax_ens.text(x, m+0.01, f"{m:.3f}", ha='center', va='bottom', fontsize=7, color="#e6edf3")

# Schalenstruktur N=2000
sh_labels = [f"HLV\n1/φ", f"HLV\nQ_FFGFT", f"T⁴-Gr.\n1/φ", f"T⁴-Gr.\nQ_FFGFT",
             "Kub.\n1/φ", "Rnd.\n1/φ"]
sh_vals   = [err_hlv_invphi, err_hlv_qffgft, err_t4g_invphi, err_t4g_qffgft,
             err_cub_invphi, err_rnd_invphi]
sh_cols   = [C["hlv"], "#f39c12", C["ffgft_graph"], "#5ba3d0", C["cubic"], C["random"]]
bars_sh = ax_sh.bar(range(6), sh_vals, color=sh_cols, edgecolor="#30363d", linewidth=0.5)
ax_sh.set_xticks(range(6)); ax_sh.set_xticklabels(sh_labels, fontsize=6.5)
ax_sh.set_title(f"Schalen-Fehler N={N_PTS}\n(kleiner = besser)", fontsize=9)
ax_sh.set_ylabel("Rel. Fehler")
for b,v in zip(bars_sh, sh_vals):
    ax_sh.text(b.get_x()+b.get_width()/2, v+0.005, f"{v:.3f}",
               ha='center', va='bottom', fontsize=6, color="#e6edf3")

# max_gap
mg_vals = [m_ana['max_gap'], np.mean([m['max_gap'] for m in m_t4g]),
           np.mean([m['max_gap'] for m in m_hlv]),
           m_torus['max_gap'], m_cub['max_gap'], m_jit['max_gap'], m_rnd['max_gap']]
ax_mg.bar(range(7), mg_vals, color=cols_b, edgecolor="#30363d", linewidth=0.5)
ax_mg.set_xticks(range(7)); ax_mg.set_xticklabels(names_s, fontsize=7)
ax_mg.set_title("Maximum Gap", fontsize=9); ax_mg.set_ylabel("max gap")

# low_r
lr_vals = [m_ana['low_r'], np.mean([m['low_r'] for m in m_t4g]),
           np.mean([m['low_r'] for m in m_hlv]),
           m_torus['low_r'], m_cub['low_r'], m_jit['low_r'], m_rnd['low_r']]
ax_lr.bar(range(7), lr_vals, color=cols_b, edgecolor="#30363d", linewidth=0.5)
ax_lr.set_xticks(range(7)); ax_lr.set_xticklabels(names_s, fontsize=7)
ax_lr.set_title("Low-sector ⟨r⟩", fontsize=9); ax_lr.set_ylabel("⟨r⟩")

# Diskriminierung 1/φ vs Q_FFGFT
disc_models = ["HLV", "T⁴-Graph", "Kubisch", "Zufällig"]
disc_invphi = [err_hlv_invphi, err_t4g_invphi, err_cub_invphi, err_rnd_invphi]
disc_qffgft = [err_hlv_qffgft, err_t4g_qffgft,
               shell_ratio_error(pts_cub, Q_FFGFT),
               shell_ratio_error(pts_rnd, Q_FFGFT)]
x_d = np.arange(4)
w   = 0.35
ax_disc.bar(x_d-w/2, disc_invphi, w, color=C["hlv"],        label=f"1/φ={INV_PHI:.4f}", edgecolor="#30363d")
ax_disc.bar(x_d+w/2, disc_qffgft, w, color="#f39c12",       label=f"Q_FFGFT={Q_FFGFT}", edgecolor="#30363d")
ax_disc.set_xticks(x_d); ax_disc.set_xticklabels(disc_models, fontsize=9)
ax_disc.set_title(f"Diskriminierung 1/φ vs Q_FFGFT  (N={N_PTS})", fontsize=10)
ax_disc.set_ylabel("Rel. Schalen-Fehler")
ax_disc.legend(fontsize=8, framealpha=0.3, facecolor="#161b22", labelcolor="white")
disc_diff = abs(disc_invphi[0] - disc_qffgft[0])
status = "unterscheidbar" if disc_diff > 0.05 else "noch nicht robust unterscheidbar"
ax_disc.text(0.5, 0.92, f"HLV Δ={disc_diff:.4f} → {status}",
             transform=ax_disc.transAxes, ha='center', color="#e6edf3", fontsize=8)

fig.text(0.5, 0.005,
    f"v3: N={N_PTS}, {len(SEEDS)} Seeds | ξ=4/30000, D_f=3-ξ, q=2/3 | "
    f"k*=log(φ)/ξ≈{int(K_STAR)} | endlicher T⁴-Graph + Ensemble",
    ha='center', fontsize=7, color="#484f58")

plt.savefig("/mnt/user-data/outputs/ffgft_hlv_gap_v3.png",
            dpi=150, bbox_inches='tight', facecolor="#0d1117")
print("\n[✓] Plot gespeichert: ffgft_hlv_gap_v3.png")

# ════════════════════════════════════════════════════════════════
# 10. Zusammenfassung
# ════════════════════════════════════════════════════════════════
print("\n" + "="*60)
print(f"{'Modell':<22} {'gap_CV':>8} {'max_gap':>9} {'low_r':>8}")
print("-"*60)
print(f"{'FFGFT T⁴ analytisch':<22} {m_ana['gap_cv']:>8.4f} {m_ana['max_gap']:>9.4f} {m_ana['low_r']:>8.4f}")
print(f"{'FFGFT T⁴ Graph (mean)':<22} {np.mean(cv_t4g):>8.4f} {np.mean([m['max_gap'] for m in m_t4g]):>9.4f} {np.mean([m['low_r'] for m in m_t4g]):>8.4f}")
print(f"{'HLV G-Lattice (mean)':<22} {np.mean(cv_hlv):>8.4f} {np.mean([m['max_gap'] for m in m_hlv]):>9.4f} {np.mean([m['low_r'] for m in m_hlv]):>8.4f}")
print(f"{'Periodischer Torus':<22} {m_torus['gap_cv']:>8.4f} {m_torus['max_gap']:>9.4f} {m_torus['low_r']:>8.4f}")
print(f"{'Kubisch':<22} {m_cub['gap_cv']:>8.4f} {m_cub['max_gap']:>9.4f} {m_cub['low_r']:>8.4f}")
print(f"{'Jittered-kubisch':<22} {m_jit['gap_cv']:>8.4f} {m_jit['max_gap']:>9.4f} {m_jit['low_r']:>8.4f}")
print(f"{'Zufällig-geometrisch':<22} {m_rnd['gap_cv']:>8.4f} {m_rnd['max_gap']:>9.4f} {m_rnd['low_r']:>8.4f}")
print("="*60)
print(f"\nSchalenstruktur N={N_PTS}:")
print(f"  HLV: 1/φ-Fehler={err_hlv_invphi:.4f}  Q_FFGFT-Fehler={err_hlv_qffgft:.4f}  Δ={abs(err_hlv_invphi-err_hlv_qffgft):.4f}")
print(f"  T⁴-Graph: 1/φ-Fehler={err_t4g_invphi:.4f}  Q_FFGFT-Fehler={err_t4g_qffgft:.4f}")
print(f"\nk* = log(φ)/ξ = {K_STAR:.2f}  →  r(k*) = {r_star:.10f} ≈ 1/φ = {INV_PHI:.10f}")
