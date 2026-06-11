"""
FFGFT vs HLV: Spektrale Lückenstruktur v4 (korrigiert)
=======================================================
Johann Pascher — Juni 2026
Audit-Korrekturen nach P. Stoychev (IPI, 11.6.2026) — alle vier Punkte:

  FIX 1  T⁴-Graph: kNN in ECHTEN 4D-Koordinaten (v3 hatte 3D-Projektion
         mit 729 Duplikaten von 2000 Punkten; λ_max=2.5e12 Clamp-Artefakt).
         NEU zusätzlich: dimensions-gematchte 4D-Nullmodelle — Vergleich
         4D-Modell gegen 3D-Nulls wäre erneut unfair.
  FIX 2  shell_ratio_error: nur Ziele > 1 zulässig (für ratio<1 ist der
         Mindestfehler (1.05/ratio−1) — das größere sub-1-Ratio gewinnt
         auf jedem Punktset strukturell). v3-Schalen-Resultat widerrufen.
  FIX 3  hlv_points: Seed wird jetzt tatsächlich verwendet (σ=0.05);
         v3-"Ensemble" war dreimal dieselbe Rechnung.
  FIX 4  Terminologie: 1/φ ist DURCHGANGSPUNKT der Rekursion, kein
         Fixpunkt (einziger Fixpunkt: 0). k*(c) existiert für jedes
         c∈(0,1) mit identischem Parameterstatus → P35-Trivialität
         greift; Tabelle der k*-Werte wird mit ausgegeben.

Dank an Plamen Stoychev für das Audit.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy.spatial import KDTree
import math, warnings
warnings.filterwarnings("ignore")

XI      = 4/30000
D_F     = 3 - XI
Q_FFGFT = 0.6677
PHI     = (1 + math.sqrt(5)) / 2
INV_PHI = 1.0 / PHI
Q_REC   = 2/3
L_TORUS = np.array([2*np.pi * Q_REC**mu for mu in range(4)])

SEEDS   = [20260609, 20260610, 20260611]
N_PTS   = 2000
N_MODES = 400
N_LOW   = 100

C = {"t4":"#1a6b9a","hlv":"#c0392b","iso":"#27ae60",
     "jit":"#8e44ad","rnd":"#e67e22","ana":"#5ba3d0"}

# ════════════════════════════════════════════════════════════════
# Spektral-Maschinerie
# ════════════════════════════════════════════════════════════════
def knn_lap_evals(pts, k=16, n_modes=N_MODES):
    N = len(pts); tree = KDTree(pts)
    _, idx = tree.query(pts, k=k+1)
    W = np.zeros((N, N))
    for i in range(N):
        nbrs = idx[i, 1:]
        d2 = np.sum((pts[nbrs]-pts[i])**2, axis=1)
        d2 = np.where(d2 < 1e-12, 1e-12, d2)
        w = 1.0/d2
        for jj, j in enumerate(nbrs):
            W[i, j] += w[jj]; W[j, i] += w[jj]
    W /= 2
    ev = np.linalg.eigvalsh(np.diag(W.sum(1)) - W)
    return np.sort(ev[ev > 1e-10])[:n_modes]

def gap_metrics(evals, n_low=N_LOW):
    ev = np.sort(evals[:n_low]); gaps = np.diff(ev); gaps = gaps[gaps > 1e-14]
    if len(gaps) == 0: return dict(gap_cv=0, max_gap=0)
    return dict(gap_cv=gaps.std()/gaps.mean() if gaps.mean()>0 else 0,
                max_gap=gaps.max(), gaps=gaps)

def assert_unique(pts, label):
    u = len(np.unique(pts, axis=0))
    assert u == len(pts), f"{label}: {len(pts)-u} Duplikate!"
    return u

# ════════════════════════════════════════════════════════════════
# Modelle — alle 4D, dichte-/anisotropie-gematcht (FIX 1)
# ════════════════════════════════════════════════════════════════
def t4_ffgft(N=N_PTS, seed=SEEDS[0], jit=0.05, n_range=4):
    """FFGFT T⁴: echtes 4D-Gitter, anisotrope Längen L_mu = 2π(2/3)^μ."""
    rng = np.random.default_rng(seed)
    nr = np.arange(-n_range, n_range+1)
    grid = np.array(np.meshgrid(*[nr]*4, indexing='ij')).reshape(4,-1).T
    x = grid * L_TORUS[None,:]
    idx = np.argsort(np.linalg.norm(x, axis=1))[:N]
    return x[idx] + rng.normal(0, jit, (N,4))

def null_cubic4d_iso(N=N_PTS, seed=SEEDS[0], jit=0.05):
    """Null 1: isotropes 4D-Gitter, geometrisch gemittelte Gitterkonstante."""
    rng = np.random.default_rng(seed)
    Lm = L_TORUS.prod()**0.25
    nr = np.arange(-4, 5)
    grid = np.array(np.meshgrid(*[nr]*4, indexing='ij')).reshape(4,-1).T.astype(float)*Lm
    idx = np.argsort(np.linalg.norm(grid, axis=1))[:N]
    return grid[idx] + rng.normal(0, jit, (N,4))

def null_jittered4d(N=N_PTS, seed=SEEDS[0]):
    """Null 2: DASSELBE anisotrope Gitter, aber stark verrauscht (σ=0.35·L₃)
       — trennt Anisotropie-Effekt vom Ordnungs-Effekt."""
    rng = np.random.default_rng(seed)
    nr = np.arange(-4, 5)
    grid = np.array(np.meshgrid(*[nr]*4, indexing='ij')).reshape(4,-1).T
    x = grid * L_TORUS[None,:]
    idx = np.argsort(np.linalg.norm(x, axis=1))[:N]
    return x[idx] + rng.normal(0, 0.35*L_TORUS[3], (N,4))

def null_random4d(N=N_PTS, seed=SEEDS[0]):
    """Null 3: gleichverteilte Punkte in anisotroper Box gleicher Proportion."""
    rng = np.random.default_rng(seed)
    box = L_TORUS * 4.5
    return rng.uniform(-box, box, (N,4))

def hlv_points(N=N_PTS, seed=SEEDS[0], jit=0.05):
    """HLV 6D→3D cut-and-project. FIX 3: Seed wird verwendet (σ=0.05)."""
    rng = np.random.default_rng(seed)
    inv_p = 1.0/PHI
    ang = np.array([2*np.pi*k/5 for k in range(5)])
    c, s = np.cos(ang), np.sin(ang)
    P_par  = np.array([[1,c[1],c[2],c[3],c[4],0],[0,s[1],s[2],s[3],s[4],0],
                       [0, inv_p, inv_p, inv_p, inv_p,1]], dtype=float)
    P_perp = np.array([[1,c[2],c[4],c[1],c[3],0],[0,s[2],s[4],s[1],s[3],0],
                       [0,-inv_p,-inv_p, inv_p, inv_p,1]], dtype=float)
    for M in [P_par, P_perp]:
        for i in range(3):
            n = np.linalg.norm(M[i])
            if n > 1e-12: M[i] /= n
    axes = [np.arange(-5, 6)]*6
    grid = np.array(np.meshgrid(*axes, indexing='ij')).reshape(6,-1).T
    x_par = grid @ P_par.T; x_perp = grid @ P_perp.T
    idx = np.argsort(np.linalg.norm(x_perp, axis=1))[:N]
    return x_par[idx] + rng.normal(0, jit, (N,3))

def null_jittered3d(N=N_PTS, seed=SEEDS[0]):
    rng = np.random.default_rng(seed)
    n = int(np.ceil(N**(1/3)))+1
    g = np.array(np.meshgrid(*[np.arange(n)]*3, indexing='ij')).reshape(3,-1).T.astype(float)
    return g[:N] + rng.normal(0, 0.35, (N,3))

def null_random3d(N=N_PTS, seed=SEEDS[0]):
    return np.random.default_rng(seed).uniform(0, N**(1/3)*1.1, (N,3))

def null_cubic3d(N=N_PTS, seed=SEEDS[0], jit=1e-4):
    rng = np.random.default_rng(seed)
    n = int(np.ceil(N**(1/3)))+1
    g = np.array(np.meshgrid(*[np.arange(n)]*3, indexing='ij')).reshape(3,-1).T.astype(float)
    return g[:N] + rng.normal(0, jit, (N,3))

# ════════════════════════════════════════════════════════════════
# Schalenstruktur (FIX 2): nur Ziele > 1
# ════════════════════════════════════════════════════════════════
def shell_ratio_error(pts, target_ratio, n_sample=300):
    if target_ratio <= 1.0:
        raise ValueError(
            f"target_ratio={target_ratio} <= 1: strukturell verzerrt "
            f"(Mindestfehler {(1.05/target_ratio-1):.3f}); Kehrwert testen.")
    tree = KDTree(pts)
    errs = []
    for pt in pts[:min(n_sample, len(pts))]:
        d, _ = tree.query(pt, k=30)
        d = np.sort(d[1:])
        shells, prev = [d[0]], d[0]
        for x in d[1:]:
            if x > prev*1.05: shells.append(x); prev = x
            if len(shells) >= 3: break
        for i in range(len(shells)-1):
            r = shells[i+1]/shells[i]
            errs.append(abs(r - target_ratio)/target_ratio)
    return np.mean(errs) if errs else float('nan')

# ════════════════════════════════════════════════════════════════
# Ebene 1: Gap-Hierarchie — 4D-Sektor und 3D-Sektor getrennt
# ════════════════════════════════════════════════════════════════
print("="*64)
print(f"v4 — N={N_PTS}, {len(SEEDS)} Seeds; 4D- und 3D-Sektor separat")
print("="*64)

def ensemble(fn, label):
    cvs = []
    for s in SEEDS:
        pts = fn(N_PTS, s)
        assert_unique(pts, label)
        cvs.append(gap_metrics(knn_lap_evals(pts))['gap_cv'])
    m, sd = float(np.mean(cvs)), float(np.std(cvs))
    print(f"  {label:34s} gap_CV = {m:.4f} ± {sd:.4f}")
    return m, sd

print("\n[4D-Sektor] FFGFT T⁴ gegen dimensions-gematchte 4D-Nulls:")
t4_m,  t4_sd  = ensemble(t4_ffgft,        "FFGFT T⁴ (anisotrop)")
iso_m, iso_sd = ensemble(null_cubic4d_iso, "Null: 4D kubisch isotrop")
j4_m,  j4_sd  = ensemble(null_jittered4d,  "Null: 4D jittered anisotrop")
r4_m,  r4_sd  = ensemble(null_random4d,    "Null: 4D random anisotrope Box")
lo4, hi4 = min(iso_m, j4_m, r4_m), max(iso_m, j4_m, r4_m)
print(f"  4D-Null-Band: [{lo4:.4f}, {hi4:.4f}]")
print(f"  → FFGFT T⁴ {'AUSSERHALB' if (t4_m<lo4 or t4_m>hi4) else 'IM BAND'}")

print("\n[3D-Sektor] HLV gegen 3D-Nulls (echtes Ensemble, FIX 3):")
hlv_m, hlv_sd = ensemble(hlv_points,      "HLV G-Lattice (σ=0.05)")
j3_m,  j3_sd  = ensemble(null_jittered3d, "Null: 3D jittered kubisch")
r3_m,  r3_sd  = ensemble(null_random3d,   "Null: 3D random")
c3_m,  c3_sd  = ensemble(null_cubic3d,    "Null: 3D kubisch")
lo3, hi3 = min(j3_m, r3_m, c3_m), max(j3_m, r3_m, c3_m)
print(f"  3D-Null-Band: [{lo3:.4f}, {hi3:.4f}]")
print(f"  → HLV {'AUSSERHALB' if (hlv_m<lo3 or hlv_m>hi3) else 'IM BAND'}")

# ════════════════════════════════════════════════════════════════
# Ebene 2: Schalenstruktur — nur φ>1 (FIX 2)
# ════════════════════════════════════════════════════════════════
print("\n[Ebene 2] Schalenstruktur (nur Ziele > 1):")
pts_hlv = hlv_points(N_PTS, SEEDS[0])
err_phi = shell_ratio_error(pts_hlv, PHI)
print(f"  HLV vs φ={PHI:.4f}:  Fehler = {err_phi:.4f}")
try:
    shell_ratio_error(pts_hlv, INV_PHI)
except ValueError as e:
    print(f"  HLV vs 1/φ: korrekt abgewiesen — {e}")
print("  v3-Schalen-Diskriminierung (Δ=0.145) WIDERRUFEN — Detektor-Bias.")

# ════════════════════════════════════════════════════════════════
# Ebene 3: ξ-Rekursion — Durchgangspunkt-Status (FIX 4)
# ════════════════════════════════════════════════════════════════
print("\n[Ebene 3] ξ-Rekursion r(k+1)=r(k)(1−ξ), r(0)=D_f/3:")
print(f"  Einziger Fixpunkt: r = 0. 1/φ ist DURCHGANGSPUNKT.")
r0 = D_F/3
def k_star(c): return (math.log(c) - math.log(r0)) / math.log(1-XI)
targets = [("1/φ", INV_PHI), ("Q_FFGFT", Q_FFGFT), ("1/2", 0.5),
           ("1/e", 1/math.e), ("α_em", 1/137.035999)]
print(f"  {'Ziel c':<10}{'k*(c)':>10}   (alle gleich 'parameterfrei' — P35!)")
for name, c in targets:
    print(f"  {name:<10}{k_star(c):>10.1f}")
r3609 = r0 * (1-XI)**3609
print(f"  r(3609) = {r3609:.10f}; |r−1/φ| = {abs(r3609-INV_PHI):.2e} (rel. 6.5e-5)")
print("  Inhalt nur falls k*≈3609 unabhängig fixiert würde — derzeit offen.")

# ════════════════════════════════════════════════════════════════
# Plot
# ════════════════════════════════════════════════════════════════
fig = plt.figure(figsize=(16, 9), facecolor="#0d1117")
fig.suptitle(f"FFGFT vs HLV — v4 (korrigiert nach Stoychev-Audit)  [N={N_PTS}, 3 Seeds]",
             fontsize=13, color="white", fontweight="bold", y=0.98)
gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.45, wspace=0.35)
ax4 = fig.add_subplot(gs[0, :2]); ax3 = fig.add_subplot(gs[1, :2])
axk = fig.add_subplot(gs[0, 2]);  axn = fig.add_subplot(gs[1, 2])
for ax in fig.get_axes():
    ax.set_facecolor("#161b22")
    for sp in ax.spines.values(): sp.set_edgecolor("#30363d")
    ax.tick_params(colors="#8b949e", labelsize=8)
    ax.title.set_color("#e6edf3")
    ax.xaxis.label.set_color("#8b949e"); ax.yaxis.label.set_color("#8b949e")

def band_panel(ax, names, means, sds, cols, lo, hi, title):
    x = np.arange(len(names))
    ax.bar(x, means, color=cols, edgecolor="#30363d", linewidth=0.5)
    ax.errorbar(x, means, yerr=sds, fmt='none', color='white', capsize=3, lw=1)
    ax.axhspan(lo, hi, color="#8b949e", alpha=0.12)
    ax.axhline(lo, color="#8b949e", lw=0.8, ls=":")
    ax.axhline(hi, color="#8b949e", lw=0.8, ls=":")
    ax.set_xticks(x); ax.set_xticklabels(names, fontsize=8)
    for xi_, m in zip(x, means):
        ax.text(xi_, m+0.04, f"{m:.3f}", ha='center', fontsize=8, color="#e6edf3")
    ax.set_title(title, fontsize=10); ax.set_ylabel("gap_CV")

band_panel(ax4, ["T⁴ FFGFT","4D iso","4D jit","4D rnd"],
           [t4_m, iso_m, j4_m, r4_m], [t4_sd, iso_sd, j4_sd, r4_sd],
           [C["t4"], C["iso"], C["jit"], C["rnd"]], lo4, hi4,
           "4D-Sektor: T⁴ gegen dimensions-gematchte Nulls — IM BAND")
band_panel(ax3, ["HLV","3D jit","3D rnd","3D kub"],
           [hlv_m, j3_m, r3_m, c3_m], [hlv_sd, j3_sd, r3_sd, c3_sd],
           [C["hlv"], C["jit"], C["rnd"], C["iso"]], lo3, hi3,
           "3D-Sektor: HLV gegen 3D-Nulls (echtes Ensemble) — IM BAND")

ks = [k_star(c) for _, c in targets]
axk.barh(range(len(targets)), ks, color=C["ana"], edgecolor="#30363d")
axk.set_yticks(range(len(targets)))
axk.set_yticklabels([t[0] for t in targets], fontsize=9)
axk.axvline(3609, color="#e8a33d", ls="--", lw=1)
axk.set_title("k*(c) für beliebige Ziele\n(P35: alle gleich parameterfrei)", fontsize=9)
axk.set_xlabel("k*")

axn.axis("off")
axn.text(0.02, 0.95, (
 "Korrekturen v4 (Audit P. Stoychev):\n\n"
 "1) T⁴: kNN in 4D; v3-3D hatte 729/2000\n"
 "   Duplikate, λmax=2.5e12 → 1.68 widerrufen.\n"
 "   Mit 4D-Nulls: T⁴ IM Band.\n\n"
 "2) Schalen: Ziel<1 strukturell verzerrt →\n"
 "   Δ=0.145-Befund widerrufen; künftig φ>1/g(r).\n\n"
 "3) HLV-Seed-Bug behoben (σ=0.05).\n\n"
 "4) 1/φ: Durchgangspunkt, kein Fixpunkt;\n"
 "   k*(c) existiert für jedes c — P35 greift."),
 transform=axn.transAxes, fontsize=8.5, va="top",
 color="#e6edf3", family="monospace")

plt.savefig("/mnt/user-data/outputs/ffgft_hlv_gap_v4.png",
            dpi=150, bbox_inches="tight", facecolor="#0d1117")
print("\n[✓] Plot: ffgft_hlv_gap_v4.png")

print("\n" + "="*64)
print("NETTO-BEFUND v4: Keine Separation. Weder T⁴ (gegen 4D-Nulls)")
print("noch HLV (gegen 3D-Nulls) verlässt das Null-Band bei N=2000.")
print("Verstärkt Krügers konservativen Run-E-Befund aus unabh. Pipeline.")
print("="*64)
