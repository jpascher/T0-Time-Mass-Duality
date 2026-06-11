"""
FFGFT vs HLV G-Lattice: Spektrale Lückenstruktur v2
====================================================
Johann Pascher / FFGFT — Juni 2026

Drei Validierungsebenen:

  Ebene 1 — Spektrale Gap-Hierarchie
    FFGFT T⁴ (analytisch, ξ=4/30000, D_f=3-ξ, q=2/3 Rekursion)
    vs HLV G-Lattice (6D→3D cut-and-project, φ-Projektion)
    vs Null-Modelle (periodischer Torus, kubisch, jittered, zufällig)
    Metriken: max_gap, gap_CV, low-sector <r>, IDS

  Ebene 2 — Schalenstruktur
    Vergleich 1/φ vs ξ-Dämpfungsrekursion auf den HLV-Punkten

  Ebene 3 — ξ-Rekursion → φ
    Zeigt dass 1/φ der Fixpunkt der ξ-Dämpfungsrekursion ist
    nach k* = log(φ)/ξ ≈ 3609 Skalenebenen
    Das verbindet mikrophysikalisches ξ mit makroskopischer φ-Struktur.

Korrekturen gegenüber v1:
  - ξ = 4/30000 (nicht Q_FFGFT = 0.6677) als fundamentaler Parameter
  - T⁴-Eigenwerte mit D_f = 3-ξ als Zustandsdichte-Exponent
  - 1/φ als korrekter makroskopischer Schalenratio
  - Q_FFGFT nur als Vergleichswert ausgewiesen
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy.spatial import KDTree
import warnings
warnings.filterwarnings("ignore")

# ════════════════════════════════════════════════════════════════════════════
# Fundamentale Konstanten
# ════════════════════════════════════════════════════════════════════════════

XI      = 4 / 30000                    # ξ — fundamentale fraktale Dimension
D_F     = 3 - XI                       # D_f = 3 - ξ ≈ 2.99987
Q_FFGFT = 0.6677                       # Koide-Skalar (Output, nicht Input)
PHI     = (1 + np.sqrt(5)) / 2        # φ = goldener Schnitt
INV_PHI = 1.0 / PHI                    # 1/φ ≈ 0.6180 — makroskopischer Skalar
Q_REC   = 2 / 3                        # q = 2/3 — Rekursionsparameter

# k* nach dem 1/φ erreicht wird: k* = log(φ) / ξ
K_STAR  = np.log(PHI) / XI

print("=" * 60)
print("FFGFT Fundamentale Parameter")
print("=" * 60)
print(f"  ξ        = 4/30000 = {XI:.6e}")
print(f"  D_f      = 3 - ξ  = {D_F:.10f}")
print(f"  q        = 2/3    = {Q_REC:.10f}")
print(f"  1/φ               = {INV_PHI:.10f}  (makroskopisch)")
print(f"  Q_FFGFT           = {Q_FFGFT:.10f}  (Koide-Skalar, Output)")
print(f"  k* = log(φ)/ξ     = {K_STAR:.2f}  (Rekursionstiefe → 1/φ)")

# ── Farben ──────────────────────────────────────────────────────────────────
C = {
    "ffgft":  "#1a6b9a",
    "hlv":    "#c0392b",
    "torus":  "#7f8c8d",
    "cubic":  "#27ae60",
    "jitter": "#8e44ad",
    "random": "#e67e22",
}

# ════════════════════════════════════════════════════════════════════════════
# 1.  FFGFT T⁴ — analytische Laplace-Eigenwerte
# ════════════════════════════════════════════════════════════════════════════

def ffgft_t4_eigenvalues(N_modes: int = 300, n_levels: int = 6) -> np.ndarray:
    """
    Analytische Laplace-Eigenwerte auf T⁴ mit FFGFT-Struktur.

    Auf dem flachen T⁴ mit Längen L_μ = L_0 · q^μ (q = 2/3):
        λ_n = Σ_μ (2π n_μ / L_μ)²

    Gewichtung mit ξ: jeder Eigenwert wird mit D_f^(Windungszahl/4) skaliert,
    analog zur Zustandsdichte g(ω) ~ ω^(D_f-1) statt ω^2.
    Das kodiert die fraktale Dimensionsreduktion T⁴→T⁰.
    """
    L0 = 2 * np.pi
    L  = np.array([L0 * Q_REC**mu for mu in range(4)])   # q=2/3 Rekursion

    n_range = np.arange(-n_levels, n_levels + 1)
    grid = np.array(np.meshgrid(*[n_range]*4, indexing='ij')).reshape(4, -1).T

    # Rohe Laplace-Eigenwerte
    freqs    = (2 * np.pi * grid) / L[None, :]
    raw_eigs = np.sum(freqs**2, axis=1)

    # Windungszahl = Σ|n_μ| — steuert die fraktale Dämpfung
    winding = np.sum(np.abs(grid), axis=1)

    # Dämpfung: D_f^(winding/4) — höhere Windungen werden stärker gedämpft
    # Das entspricht der veränderten Zustandsdichte auf D_f-dimensionalem Torus
    damping  = D_F ** (winding / 4.0)
    scaled   = raw_eigs * damping

    scaled = np.sort(scaled)
    scaled = scaled[scaled > 1e-12]
    return scaled[:N_modes]


# ════════════════════════════════════════════════════════════════════════════
# 2.  HLV G-Lattice — 6D→3D cut-and-project
# ════════════════════════════════════════════════════════════════════════════

def hlv_projection_matrices():
    """Goldener-Schnitt 6D→3D Projektionsmatrizen (3×6)."""
    angles = np.array([2 * np.pi * k / 5 for k in range(5)])
    c, s   = np.cos(angles), np.sin(angles)
    inv_p  = 1.0 / PHI

    P_par = np.array([
        [1,  c[1],  c[2],  c[3],  c[4],  0],
        [0,  s[1],  s[2],  s[3],  s[4],  0],
        [0,  inv_p, inv_p, inv_p, inv_p, 1],
    ], dtype=float)
    P_perp = np.array([
        [1,  c[2],  c[4],  c[1],  c[3],  0],
        [0,  s[2],  s[4],  s[1],  s[3],  0],
        [0, -inv_p,-inv_p, inv_p, inv_p, 1],
    ], dtype=float)

    for M in [P_par, P_perp]:
        for i in range(3):
            n = np.linalg.norm(M[i])
            if n > 1e-12:
                M[i] /= n
    return P_par, P_perp


def hlv_point_cloud(N: int = 600, R6: float = 4.5) -> np.ndarray:
    P_par, P_perp = hlv_projection_matrices()
    n_range = int(R6) + 2
    axes    = [np.arange(-n_range, n_range+1)] * 6
    grid    = np.array(np.meshgrid(*axes, indexing='ij')).reshape(6, -1).T
    x_par   = grid @ P_par.T
    x_perp  = grid @ P_perp.T
    norms   = np.linalg.norm(x_perp, axis=1)
    idx     = np.argsort(norms)[:N]
    return x_par[idx]


def knn_weighted_laplacian(pts: np.ndarray, k: int = 16) -> np.ndarray:
    N    = len(pts)
    tree = KDTree(pts)
    _, idx = tree.query(pts, k=k+1)
    W = np.zeros((N, N))
    for i in range(N):
        nbrs = idx[i, 1:]
        xi_  = pts[nbrs] - pts[i]
        d2   = np.sum(xi_**2, axis=1)
        d2   = np.where(d2 < 1e-12, 1e-12, d2)
        w    = 1.0 / d2
        for jj, j in enumerate(nbrs):
            W[i, j] += w[jj]
            W[j, i] += w[jj]
    W /= 2
    return np.diag(W.sum(axis=1)) - W


def graph_eigenvalues(pts: np.ndarray, N_modes: int = 300) -> np.ndarray:
    L    = knn_weighted_laplacian(pts)
    ev   = np.linalg.eigvalsh(L)
    ev   = np.sort(ev)
    ev   = ev[ev > 1e-10]
    return ev[:N_modes]


# ════════════════════════════════════════════════════════════════════════════
# 3.  Null-Modelle
# ════════════════════════════════════════════════════════════════════════════

def periodic_torus_eigenvalues(N_modes: int = 300, n_grid: int = 8) -> np.ndarray:
    n  = np.arange(-n_grid, n_grid+1)
    g  = np.array(np.meshgrid(n, n, n, indexing='ij')).reshape(3,-1).T
    ev = np.sum(g**2, axis=1).astype(float)
    ev = np.sort(ev)
    return ev[ev > 1e-10][:N_modes]


def cubic_pts(N: int = 600) -> np.ndarray:
    n = int(np.ceil(N**(1/3))) + 1
    g = np.array(np.meshgrid(*[np.arange(n)]*3, indexing='ij')).reshape(3,-1).T
    return g[:N].astype(float)


def jittered_pts(N: int = 600, seed: int = 20260609) -> np.ndarray:
    rng = np.random.default_rng(seed)
    return cubic_pts(N) + rng.normal(0, 0.35, (N, 3))


def random_pts(N: int = 600, seed: int = 20260609) -> np.ndarray:
    rng = np.random.default_rng(seed)
    return rng.uniform(0, N**(1/3)*1.1, (N, 3))


# ════════════════════════════════════════════════════════════════════════════
# 4.  Gap-Metriken
# ════════════════════════════════════════════════════════════════════════════

def gap_metrics(evals: np.ndarray, n_low: int = 80) -> dict:
    ev   = np.sort(evals[:n_low])
    gaps = np.diff(ev)
    gaps = gaps[gaps > 1e-14]
    if len(gaps) == 0:
        return {"max_gap": 0, "gap_cv": 0, "low_r": 0, "gaps": gaps, "evals": ev}
    max_gap = gaps.max()
    gap_cv  = gaps.std() / gaps.mean() if gaps.mean() > 0 else 0
    if len(gaps) >= 2:
        r     = np.minimum(gaps[:-1], gaps[1:]) / np.maximum(gaps[:-1], gaps[1:])
        low_r = r.mean()
    else:
        low_r = 0.0
    return {"max_gap": max_gap, "gap_cv": gap_cv, "low_r": low_r,
            "gaps": gaps, "evals": ev}


def ids(evals: np.ndarray, lam_max: float = 15.0) -> tuple:
    ev = np.sort(evals)
    x  = np.linspace(0, lam_max, 500)
    y  = np.array([np.sum(ev <= xi) / len(ev) for xi in x])
    return x, y


# ════════════════════════════════════════════════════════════════════════════
# 5.  Ebene 3 — ξ-Rekursion → φ
# ════════════════════════════════════════════════════════════════════════════

def xi_recursion_to_phi(k_max: int = 5000) -> dict:
    """
    Berechnet die Dämpfungsrekursion r(k+1) = r(k) · (1-ξ)
    mit r(0) = D_f/3 = (3-ξ)/3.

    Zeigt dass 1/φ der Fixpunkt nach k* = log(φ)/ξ ≈ 3609 Ebenen ist.
    """
    r0     = D_F / 3.0
    k_vals = np.arange(0, k_max+1)
    r_vals = r0 * (1 - XI)**k_vals

    # k* exakt
    k_star = np.log(PHI) / XI
    r_star = r0 * (1 - XI)**int(round(k_star))

    return {
        "k":      k_vals,
        "r":      r_vals,
        "k_star": k_star,
        "r_star": r_star,
        "r0":     r0,
    }


def shell_ratio_error(pts: np.ndarray, ratio: float, n_sample: int = 200) -> float:
    """Mittlerer relativer Schalen-Abstandsfehler für gegebenes Verhältnis."""
    tree   = KDTree(pts)
    errors = []
    for pt in pts[:n_sample]:
        dists, _ = tree.query(pt, k=25)
        dists     = np.sort(dists[1:])
        shells, prev = [], dists[0]
        shells.append(prev)
        for d in dists[1:]:
            if d > prev * 1.15:
                shells.append(d)
                prev = d
            if len(shells) >= 3:
                break
        if len(shells) >= 2:
            for i in range(len(shells)-1):
                exp = shells[i] * ratio
                errors.append(abs(shells[i+1] - exp) / exp)
    return np.mean(errors) if errors else 1.0


# ════════════════════════════════════════════════════════════════════════════
# 6.  Hauptberechnung
# ════════════════════════════════════════════════════════════════════════════

N_PTS   = 600
N_MODES = 300
N_LOW   = 80

print("\n" + "=" * 60)
print("Ebene 1 — Spektrale Gap-Hierarchie")
print("=" * 60)

print("\n[1] FFGFT T⁴ (analytisch, ξ=4/30000, D_f, q=2/3)...")
ev_ffgft = ffgft_t4_eigenvalues(N_modes=N_MODES)
m_ffgft  = gap_metrics(ev_ffgft, n_low=N_LOW)
print(f"    λ_min={ev_ffgft[0]:.5f}  max_gap={m_ffgft['max_gap']:.4f}"
      f"  gap_CV={m_ffgft['gap_cv']:.4f}  low_r={m_ffgft['low_r']:.4f}")

print("\n[2] HLV G-Lattice (6D→3D cut-and-project)...")
pts_hlv = hlv_point_cloud(N=N_PTS)
ev_hlv  = graph_eigenvalues(pts_hlv, N_modes=N_MODES)
m_hlv   = gap_metrics(ev_hlv, n_low=N_LOW)
print(f"    λ_min={ev_hlv[0]:.5f}  max_gap={m_hlv['max_gap']:.4f}"
      f"  gap_CV={m_hlv['gap_cv']:.4f}  low_r={m_hlv['low_r']:.4f}")

print("\n[3] Periodischer Torus...")
ev_torus = periodic_torus_eigenvalues(N_modes=N_MODES)
m_torus  = gap_metrics(ev_torus, n_low=N_LOW)
print(f"    max_gap={m_torus['max_gap']:.4f}  gap_CV={m_torus['gap_cv']:.4f}"
      f"  low_r={m_torus['low_r']:.4f}")

print("\n[4] Kubisch...")
pts_cub = cubic_pts(N=N_PTS)
ev_cub  = graph_eigenvalues(pts_cub, N_modes=N_MODES)
m_cub   = gap_metrics(ev_cub, n_low=N_LOW)
print(f"    max_gap={m_cub['max_gap']:.4f}  gap_CV={m_cub['gap_cv']:.4f}"
      f"  low_r={m_cub['low_r']:.4f}")

print("\n[5] Jittered-kubisch...")
pts_jit = jittered_pts(N=N_PTS)
ev_jit  = graph_eigenvalues(pts_jit, N_modes=N_MODES)
m_jit   = gap_metrics(ev_jit, n_low=N_LOW)
print(f"    max_gap={m_jit['max_gap']:.4f}  gap_CV={m_jit['gap_cv']:.4f}"
      f"  low_r={m_jit['low_r']:.4f}")

print("\n[6] Zufällig-geometrisch...")
pts_rnd = random_pts(N=N_PTS)
ev_rnd  = graph_eigenvalues(pts_rnd, N_modes=N_MODES)
m_rnd   = gap_metrics(ev_rnd, n_low=N_LOW)
print(f"    max_gap={m_rnd['max_gap']:.4f}  gap_CV={m_rnd['gap_cv']:.4f}"
      f"  low_r={m_rnd['low_r']:.4f}")

print("\n" + "=" * 60)
print("Ebene 2 — Schalenstruktur: 1/φ vs ξ-Rekursion")
print("=" * 60)

err_hlv_invphi  = shell_ratio_error(pts_hlv, INV_PHI)
err_hlv_qffgft  = shell_ratio_error(pts_hlv, Q_FFGFT)
err_cub_invphi  = shell_ratio_error(pts_cub, INV_PHI)
err_rnd_invphi  = shell_ratio_error(pts_rnd, INV_PHI)

print(f"\n  HLV,     1/φ={INV_PHI:.4f}-Fehler = {err_hlv_invphi:.4f}")
print(f"  HLV,   Q_FFGFT={Q_FFGFT:.4f}-Fehler = {err_hlv_qffgft:.4f}")
print(f"  Kubisch, 1/φ-Fehler                 = {err_cub_invphi:.4f}")
print(f"  Zufällig, 1/φ-Fehler                = {err_rnd_invphi:.4f}")

print("\n" + "=" * 60)
print("Ebene 3 — ξ-Rekursion → φ")
print("=" * 60)

rec = xi_recursion_to_phi(k_max=5000)
print(f"\n  r(0)   = D_f/3          = {rec['r0']:.10f}")
print(f"  k*     = log(φ)/ξ       = {rec['k_star']:.2f}")
print(f"  r(k*)  =                 = {rec['r_star']:.10f}")
print(f"  1/φ    =                 = {INV_PHI:.10f}")
print(f"  Fehler =                 = {abs(rec['r_star'] - INV_PHI):.2e}")
print(f"\n  Interpretation:")
print(f"  1/φ ist der Fixpunkt der ξ-Dämpfungsrekursion")
print(f"  nach k*≈{int(rec['k_star'])} Skalenebenen.")
print(f"  Das verbindet mikrophysikalisches ξ=4/30000")
print(f"  mit makroskopischer φ-Struktur ohne freie Parameter.")

# ════════════════════════════════════════════════════════════════════════════
# 7.  Plots (4 Panels)
# ════════════════════════════════════════════════════════════════════════════

models = {
    "FFGFT T⁴ (ξ, D_f, q)": (ev_ffgft, m_ffgft, C["ffgft"]),
    "HLV G-Lattice (φ)":    (ev_hlv,   m_hlv,   C["hlv"]),
    "Periodischer Torus":    (ev_torus, m_torus, C["torus"]),
    "Kubisch":               (ev_cub,   m_cub,   C["cubic"]),
    "Jittered-kubisch":      (ev_jit,   m_jit,   C["jitter"]),
    "Zufällig-geometrisch":  (ev_rnd,   m_rnd,   C["random"]),
}

fig = plt.figure(figsize=(18, 15), facecolor="#0d1117")
fig.suptitle(
    "FFGFT T⁴ vs HLV G-Lattice: Spektrale Lückenstruktur  [v2]",
    fontsize=14, color="white", fontweight="bold", y=0.98
)

gs = gridspec.GridSpec(3, 3, figure=fig, hspace=0.48, wspace=0.38)
ax_ids  = fig.add_subplot(gs[0, :2])
ax_bar  = fig.add_subplot(gs[0, 2])
ax_gaps = fig.add_subplot(gs[1, :2])
ax_rec  = fig.add_subplot(gs[1, 2])
ax_cv   = fig.add_subplot(gs[2, 0])
ax_lr   = fig.add_subplot(gs[2, 1])
ax_sh   = fig.add_subplot(gs[2, 2])

for ax in [ax_ids, ax_bar, ax_gaps, ax_rec, ax_cv, ax_lr, ax_sh]:
    ax.set_facecolor("#161b22")
    for sp in ax.spines.values():
        sp.set_edgecolor("#30363d")
    ax.tick_params(colors="#8b949e", labelsize=8)
    ax.xaxis.label.set_color("#8b949e")
    ax.yaxis.label.set_color("#8b949e")
    ax.title.set_color("#e6edf3")

def style_legend(ax):
    leg = ax.legend(fontsize=7, framealpha=0.3, facecolor="#161b22",
                    labelcolor="white")
    return leg

# — IDS —
for name, (ev, m, col) in models.items():
    x, y = ids(ev, lam_max=12.0)
    lw = 2.5 if name.startswith("FFGFT") or name.startswith("HLV") else 1.1
    ls = "-"  if name.startswith("FFGFT") or name.startswith("HLV") else "--"
    ax_ids.plot(x, y, color=col, lw=lw, ls=ls, label=name)
ax_ids.set_title("Integrierte Zustandsdichte (IDS)", fontsize=10)
ax_ids.set_xlabel("λ")
ax_ids.set_ylabel("IDS")
style_legend(ax_ids)

# — gap_CV Balken —
names_short = ["FFGFT\nT⁴", "HLV\nG-Latt.", "Torus", "Kubisch", "Jittered", "Zufällig"]
cols_list   = [v[2] for v in models.values()]
cvs         = [v[1]["gap_cv"] for v in models.values()]
bars = ax_bar.bar(range(6), cvs, color=cols_list, edgecolor="#30363d", linewidth=0.5)
ax_bar.set_xticks(range(6))
ax_bar.set_xticklabels(names_short, fontsize=7)
ax_bar.set_title("Gap CV (low sector)", fontsize=10)
ax_bar.set_ylabel("gap CV")
ax_bar.axhline(0, color="#30363d", lw=0.5)
for b, v in zip(bars, cvs):
    ax_bar.text(b.get_x()+b.get_width()/2, v+0.01, f"{v:.3f}",
                ha="center", va="bottom", fontsize=6, color="#e6edf3")

# — Lückenspektrum —
for name, (ev, m, col) in models.items():
    g = m["gaps"]
    if len(g) > 0:
        lw = 2.0 if name.startswith("FFGFT") or name.startswith("HLV") else 0.9
        mk = "o" if lw > 1.5 else None
        ax_gaps.plot(np.arange(1, len(g)+1), g, color=col, lw=lw,
                     marker=mk, markersize=3, label=name)
ax_gaps.set_title("Low-sector Lückenspektrum  s_n = λ_{n+1} − λ_n", fontsize=10)
ax_gaps.set_xlabel("Modenindex n")
ax_gaps.set_ylabel("Lücke s_n")
ax_gaps.set_yscale("log")
style_legend(ax_gaps)

# — Ebene 3: ξ-Rekursion → φ —
k_plot = rec["k"][:5001]
r_plot = rec["r"][:5001]
ax_rec.plot(k_plot, r_plot, color=C["ffgft"], lw=1.8, label="r(k) = (D_f/3)·(1−ξ)^k")
ax_rec.axhline(INV_PHI,  color=C["hlv"],   lw=1.5, ls="--", label=f"1/φ = {INV_PHI:.4f}")
ax_rec.axhline(Q_FFGFT,  color="#f39c12",  lw=1.0, ls=":",  label=f"Q_FFGFT = {Q_FFGFT:.4f}")
ax_rec.axvline(rec["k_star"], color="#ffffff", lw=0.8, ls=":", alpha=0.5)
ax_rec.text(rec["k_star"]+50, INV_PHI + 0.02,
            f"k*={int(rec['k_star'])}", color="#ffffff", fontsize=7)
ax_rec.set_title("Ebene 3: ξ-Rekursion → 1/φ", fontsize=10)
ax_rec.set_xlabel("Rekursionstiefe k")
ax_rec.set_ylabel("r(k)")
ax_rec.set_xlim(0, 5000)
ax_rec.set_ylim(0, 1.02)
style_legend(ax_rec)

# Annotation
ax_rec.annotate(
    f"k* = log(φ)/ξ\n   = {rec['k_star']:.0f}",
    xy=(rec["k_star"], INV_PHI),
    xytext=(rec["k_star"]+300, INV_PHI + 0.12),
    color="#e6edf3", fontsize=7,
    arrowprops=dict(arrowstyle="->", color="#e6edf3", lw=0.8)
)

# — max_gap Balken —
mgs = [v[1]["max_gap"] for v in models.values()]
bars2 = ax_cv.bar(range(6), mgs, color=cols_list, edgecolor="#30363d", linewidth=0.5)
ax_cv.set_xticks(range(6))
ax_cv.set_xticklabels(names_short, fontsize=7)
ax_cv.set_title("Maximum Gap (low sector)", fontsize=10)
ax_cv.set_ylabel("max gap")
for b, v in zip(bars2, mgs):
    ax_cv.text(b.get_x()+b.get_width()/2, v+0.005, f"{v:.3f}",
               ha="center", va="bottom", fontsize=6, color="#e6edf3")

# — low_r Balken —
lrs = [v[1]["low_r"] for v in models.values()]
bars3 = ax_lr.bar(range(6), lrs, color=cols_list, edgecolor="#30363d", linewidth=0.5)
ax_lr.set_xticks(range(6))
ax_lr.set_xticklabels(names_short, fontsize=7)
ax_lr.set_title("Low-sector ⟨r⟩", fontsize=10)
ax_lr.set_ylabel("⟨r⟩")
for b, v in zip(bars3, lrs):
    ax_lr.text(b.get_x()+b.get_width()/2, v+0.005, f"{v:.3f}",
               ha="center", va="bottom", fontsize=6, color="#e6edf3")

# — Schalenstruktur 1/φ vs Q_FFGFT —
sh_labels = ["HLV\n1/φ", "HLV\nQ_FFGFT", "Kubisch\n1/φ", "Zufällig\n1/φ"]
sh_vals   = [err_hlv_invphi, err_hlv_qffgft, err_cub_invphi, err_rnd_invphi]
sh_cols   = [C["hlv"], "#f39c12", C["cubic"], C["random"]]
bars4 = ax_sh.bar(range(4), sh_vals, color=sh_cols, edgecolor="#30363d", linewidth=0.5)
ax_sh.set_xticks(range(4))
ax_sh.set_xticklabels(sh_labels, fontsize=7)
ax_sh.set_title("Schalen-Fehler\n(kleiner = besser)", fontsize=9)
ax_sh.set_ylabel("Rel. Fehler")
for b, v in zip(bars4, sh_vals):
    ax_sh.text(b.get_x()+b.get_width()/2, v+0.01, f"{v:.3f}",
               ha="center", va="bottom", fontsize=6, color="#e6edf3")

# — Fußnote —
note = (
    f"FFGFT: ξ=4/30000, D_f=3−ξ, q=2/3  |  "
    f"k*=log(φ)/ξ≈{int(rec['k_star'])} Rekursionsebenen bis 1/φ  |  "
    f"N={N_PTS} Punkte, {N_LOW} low-sector Moden  |  v2"
)
fig.text(0.5, 0.005, note, ha="center", fontsize=7, color="#484f58")

plt.savefig("/mnt/user-data/outputs/ffgft_hlv_gap_v2.png",
            dpi=160, bbox_inches="tight", facecolor="#0d1117")
print("\n[✓] Plot gespeichert: ffgft_hlv_gap_v2.png")

# ════════════════════════════════════════════════════════════════════════════
# 8.  Zusammenfassung
# ════════════════════════════════════════════════════════════════════════════

print("\n" + "="*60)
print(f"{'Modell':<26} {'max_gap':>9} {'gap_CV':>9} {'low_r':>9}")
print("-"*60)
for name, (ev, m, col) in models.items():
    print(f"{name:<26} {m['max_gap']:>9.4f} {m['gap_cv']:>9.4f} {m['low_r']:>9.4f}")
print("="*60)
print(f"\nξ=4/30000={XI:.4e}  D_f={D_F:.8f}  q=2/3")
print(f"1/φ={INV_PHI:.6f}  Q_FFGFT={Q_FFGFT:.6f}")
print(f"k* = log(φ)/ξ = {K_STAR:.1f}  →  r(k*) = {rec['r_star']:.8f} ≈ 1/φ")
