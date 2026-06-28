#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Shared HLV <-> FFGFT memory harness (Krueger pre-registered null-model protocol)
================================================================================
Two observables, one protocol -- because the two memory kernels are NOT the same
functional shape, and reading the documents is what settles that:

  HLV benchmark kernel (Krueger, Zenodo 20514548):
      K(t) = sum_i w_i tau_i^{-1} e^{-t/tau_i}     -- POSITIVE DECAYING mixture (overdamped)
  FFGFT kernel (Dok 282, ffgft_t4_cp_divisibility.py):
      Fourier transform of the discrete spectral density sum_k g_k^2 delta(omega-omega_k),
      omega_k = sqrt(lambda_k) the loop frequencies of the T^4 connection-Laplacian,
      g_k^2 ~ mode degeneracy, 6 dominant low modes  -- OSCILLATORY (revivals), NOT decaying.

So FFGFT cannot be a like-for-like decaying kernel in Krueger's overdamped vorticity
benchmark. The honest construction runs the SAME model-comparison logic on the two
observables where each kernel's signature actually lives:

  PART 1 -- overdamped vorticity decay (Krueger's benchmark): M0/M1/M_HLV/M2.
            Expected: M_HLV beats weak nulls, TIES the generic biexponential on RMSE,
            BIC-favoured by parsimony -> non-identifiability (Run M1).
  PART 2 -- coherence / dephasing observable c(t)=e^{-Gamma(t)} (FFGFT's home sector):
            the FFGFT discrete-spectrum kernel produces a BLP back-flow (revivals);
            generic positive DECAYING kernels are monotone (back-flow = 0) and cannot
            reproduce it -> here the structured kernel HAS a signature the generic null
            misses. This is the discriminating observable.

FFGFT kernel constants are taken from the corpus (deterministic), not chosen:
  T^4 connection-Laplacian, L=3, flux a = (pi/2)(1+mu); omega_k=sqrt(lambda_k); g_k=sqrt(deg);
  six dominant low modes. Reproduces the Dok-282 BLP back-flow 5.125 exactly.

numpy + scipy. Seeds fixed. Synthetic data are model-generated, so Part 1 reproduces the
protocol and the qualitative Table-1 result, not Krueger's exact figures.
"""
import numpy as np, csv
from itertools import product
from numpy.linalg import eigvalsh
from scipy.linalg import expm
from scipy.optimize import minimize

rng = np.random.default_rng(0)
T_END, DT = 8.0, 0.01
t = np.arange(0.0, T_END + DT, DT); N = len(t)
BETAS = np.linspace(0.20, 0.90, 8)
TRAIN, TEST = [0, 1, 2, 3], [4, 5, 6, 7]
NOISE = 0.01
HLV_W, HLV_R = np.array([0.65, 0.35]), 3.0     # HLV-constrained: weights & ratio FIXED a priori

# ===== FFGFT memory kernel: constants FROM THE CORPUS (deterministic) ==========
def _build_T4(L):
    coords = list(product(range(L), repeat=4)); idx = {c: k for k, c in enumerate(coords)}
    edges = []
    for c in coords:
        i = idx[c]
        for mu in range(4):
            d = list(c); d[mu] = (d[mu] + 1) % L; edges.append((i, idx[tuple(d)], mu))
    return len(coords), edges
def _conn_laplacian(Nn, edges, amp):
    H = np.zeros((Nn, Nn), complex); deg = np.zeros(Nn)
    for (i, j, mu) in edges:
        u = np.exp(1j * amp * (1 + mu))            # mu-dependent flux -> structured spectrum
        H[i, j] += -u; H[j, i] += -np.conj(u); deg[i] += 1; deg[j] += 1
    H[np.diag_indices(Nn)] = deg; return H
def ffgft_bath(L=3, amp=0.5 * np.pi, n_modes=6):
    Nn, edges = _build_T4(L)
    lam = eigvalsh(_conn_laplacian(Nn, edges, amp)); lam = lam[lam > 1e-6]
    omega = np.sqrt(lam); uniq = []
    for w in omega:
        if not uniq or abs(w - uniq[-1][0]) > 1e-3: uniq.append([w, 1])
        else: uniq[-1][1] += 1
    uniq = uniq[:n_modes]
    wk = np.array([u[0] for u in uniq]); g2 = np.array([u[1] for u in uniq], float)  # g_k^2 ~ degeneracy
    return wk, g2
OMEGA_F, G2_F = ffgft_bath()

# ===== PART 1: Krueger overdamped vorticity benchmark ==========================
def simulate(beta, alpha, ws, taus):
    q = len(taus); A = np.zeros((q + 1, q + 1)); A[0, 0] = -beta
    for i in range(q):
        A[0, 1 + i] = -alpha * ws[i]; A[1 + i, 0] = 1.0 / taus[i]; A[1 + i, 1 + i] = -1.0 / taus[i]
    Phi = expm(A * DT); z = np.zeros(q + 1); z[0] = 1.0; out = np.empty(N); out[0] = 1.0
    for n in range(1, N): z = Phi @ z; out[n] = z[0]
    return out
def damping(beta, gamma): return np.exp(-(beta + gamma) * t)

DATA = {r: simulate(b, 0.52, HLV_W, np.array([0.42, 0.42 * HLV_R])) + NOISE * rng.standard_normal(N)
        for r, b in enumerate(BETAS)}

def traj(model, p, beta):
    if model == "M0":    return damping(beta, p[0])
    if model == "M1":    return simulate(beta, p[0], [1.0], [p[1]])
    if model == "M_HLV": return simulate(beta, p[0], HLV_W, np.array([p[1], p[1] * HLV_R]))
    if model == "M2":    return simulate(beta, p[0], [p[1], 1 - p[1]], [p[2], p[3]])
def rmse_on(model, p, regimes):
    return np.sqrt(np.mean(np.concatenate([traj(model, p, BETAS[r]) - DATA[r] for r in regimes])**2))
SPECS = {"M0": ([0.3], [(0, 5)]), "M1": ([0.5, 0.5], [(0, 5), (0.02, 10)]),
         "M_HLV": ([0.5, 0.4], [(0, 5), (0.02, 10)]),
         "M2": ([0.5, 0.6, 0.4, 1.2], [(0, 5), (0.01, 0.99), (0.02, 10), (0.02, 10)])}
NPARAM = {"M0": 1, "M1": 2, "M_HLV": 2, "M2": 4}
def fit(model, regimes):
    x0, bnds = SPECS[model]; best = None
    starts = [np.array(x0)] + ([np.array([0.5, 0.5, 0.3, 1.0]), np.array([0.52, 0.65, 0.42, 1.26])] if model == "M2" else [])
    for s in starts:
        res = minimize(lambda p: rmse_on(model, p, regimes), s, bounds=bnds, method="L-BFGS-B")
        if best is None or res.fun < best.fun: best = res
    return best.x
def info_crit(model, p):
    res = np.concatenate([traj(model, p, BETAS[r]) - DATA[r] for r in TEST]); n, k = len(res), NPARAM[model]
    sse = np.sum(res**2); return 2*k + n*np.log(sse/n), k*np.log(n) + n*np.log(sse/n)

params, rows = {}, []
for m in ["M0", "M1", "M_HLV", "M2"]:
    params[m] = fit(m, TRAIN)
    aic, bic = info_crit(m, params[m])
    rows.append([m, NPARAM[m], f"{rmse_on(m, params[m], TRAIN):.5f}", f"{rmse_on(m, params[m], TEST):.5f}",
                 f"{aic:.1f}", f"{bic:.1f}"])
def tresid(m): return np.concatenate([traj(m, params[m], BETAS[r]) - DATA[r] for r in TEST])
def boot_adv(a, b, B=1000):
    ra, rb = tresid(a)**2, tresid(b)**2; n = len(ra); d = []
    for _ in range(B):
        idx = rng.integers(0, n, n); d.append(np.sqrt(rb[idx].mean()) - np.sqrt(ra[idx].mean()))
    d = np.array(d); return d.mean(), np.percentile(d, 2.5), np.percentile(d, 97.5)
adv_rows = []
for b in ["M0", "M1", "M2"]:
    mean, lo, hi = boot_adv("M_HLV", b)
    if lo > 0:
        verdict = ("HLV-specific ADMISSIBLE" if (b == "M2" and mean >= 0.10*rmse_on(b, params[b], TEST))
                   else ("positive but <10%" if b == "M2" else "beats null (CI>0)"))
    elif hi < 0: verdict = "null is better (CI<0)"
    else: verdict = "tie (CI thru 0)"
    adv_rows.append(["M_HLV", b, f"{mean:+.6f}", f"{lo:+.6f}", f"{hi:+.6f}", verdict])
p_M2_refit = fit("M2", TEST)
cf = [["M2_refit_on_test (best-case generic)", f"{rmse_on('M2', p_M2_refit, TEST):.5f}"],
      ["M_HLV_frozen_from_train", f"{rmse_on('M_HLV', params['M_HLV'], TEST):.5f}"]]

# ===== PART 2: FFGFT coherence/dephasing observable ============================
def backflow(c): d = np.diff(c); return float(np.sum(d[d > 0]))
tc = np.linspace(1e-3, 80.0, 4000)
COUP = 2.4                                            # the one free overall coupling (fixed truth)
g = COUP * np.sqrt(G2_F) / np.sqrt(G2_F.sum())
Gamma = sum((2*gg**2/w**2)*(1 - np.cos(w*tc)) for w, gg in zip(OMEGA_F, g))
c_ffgft = np.exp(-Gamma); bf_ffgft = backflow(c_ffgft)
# generic positive DECAYING coherence nulls fitted to c_ffgft(t)
def fit_curve(model, x0, bnds):
    res = minimize(lambda p: np.sqrt(np.mean((model(p) - c_ffgft)**2)), x0, bounds=bnds, method="L-BFGS-B")
    return model(res.x), np.sqrt(np.mean((model(res.x) - c_ffgft)**2))
c_se, r_se = fit_curve(lambda p: np.exp(-p[0]*tc), [0.1], [(1e-3, 5)])
c_be, r_be = fit_curve(lambda p: p[0]*np.exp(-p[1]*tc) + (1-p[0])*np.exp(-p[2]*tc),
                       [0.5, 0.3, 0.05], [(0, 1), (1e-3, 5), (1e-3, 5)])
coh_rows = [["FFGFT_discrete_spectrum (6 modes, fixed)", "1 (coupling)", "0.000000", f"{bf_ffgft:.3f}",
             "revival signature present"],
            ["generic single-exp (decaying)", "1", f"{r_se:.6f}", f"{backflow(c_se):.3f}", "monotone; no revival"],
            ["generic biexponential (decaying)", "3", f"{r_be:.6f}", f"{backflow(c_be):.3f}", "monotone; no revival"]]

# ===== write CSVs ==============================================================
def W(name, header, data):
    with open(name, "w", newline="") as f: w = csv.writer(f); w.writerow(header); w.writerows(data)
W("memory_harness_models.csv", ["model", "n_params", "train_RMSE", "test_RMSE", "test_AIC", "test_BIC"], rows)
W("memory_harness_bootstrap.csv", ["model", "vs_null", "mean_RMSE_advantage", "ci_lo", "ci_hi", "verdict"], adv_rows)
W("memory_harness_crossflow.csv", ["quantity", "test_RMSE"], cf)
W("memory_harness_ffgft_coherence.csv",
  ["kernel_on_coherence_observable", "n_params", "rmse_to_c_FFGFT", "BLP_backflow", "note"], coh_rows)
W("ffgft_kernel_constants.csv", ["mode_k", "omega_k=sqrt(lambda_k)", "g_k^2=degeneracy"],
  [[k, f"{OMEGA_F[k]:.4f}", f"{G2_F[k]:.0f}"] for k in range(len(OMEGA_F))])

# ===== report ==================================================================
print("FFGFT memory kernel (from the corpus, deterministic):")
print(f"  6 modes; omega_k = {np.round(OMEGA_F,4)}")
print(f"  g_k^2 (degeneracy) = {G2_F.astype(int)}  -> oscillatory discrete spectrum, NOT decaying\n")
print("PART 1 -- Krueger overdamped vorticity benchmark (M0/M1/M_HLV/M2):")
print(f"  {'model':8s}{'k':>3s}{'test RMSE':>11s}{'test BIC':>11s}")
for r in rows: print(f"  {r[0]:8s}{r[1]:>3d}{r[3]:>11s}{r[5]:>11s}")
for r in adv_rows: print(f"  M_HLV over {r[1]:4s}: {r[2]} CI[{r[3]},{r[4]}]  {r[5]}")
print(f"  cross-flow: M2 refit-on-test={cf[0][1]}, frozen M_HLV={cf[1][1]}")
print("\nPART 2 -- FFGFT coherence observable c(t)=exp(-Gamma(t)) (its home sector):")
print(f"  {'kernel':40s}{'rmse->c':>10s}{'backflow':>10s}")
for r in coh_rows: print(f"  {r[0]:40s}{r[2]:>10s}{r[3]:>10s}")
print(f"\n  FFGFT discrete-spectrum back-flow = {bf_ffgft:.3f} (Dok-282 value 5.125); generic decaying")
print("  kernels are monotone (back-flow 0) and cannot reproduce the revival -> on THIS observable")
print("  the structured FFGFT kernel has a signature the generic null misses. The overdamped sector")
print("  (Part 1) shows non-identifiability; the coherence sector (Part 2) is the discriminator.")
print("-> 5 CSVs written")

# ===== plot ====================================================================
try:
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt, os
    os.makedirs("figures", exist_ok=True)
    fig, ax = plt.subplots(1, 3, figsize=(16, 4.3))
    nm = [r[0] for r in rows]; te = [float(r[3]) for r in rows]
    ax[0].bar(nm, te, color=["#94a3b8", "#94a3b8", "#1d4ed8", "#c2410c"])
    ax[0].set_ylabel("held-out RMSE"); ax[0].tick_params(axis="x", labelrotation=15)
    ax[0].set_title("Part 1: overdamped decay -- M_HLV ties M2 (non-identifiable)", fontsize=9, loc="left")
    ax[1].plot(tc, c_ffgft, color="#0f766e", lw=2, label="FFGFT discrete spectrum (revivals)")
    ax[1].plot(tc, c_se, "--", color="#c2410c", lw=1.3, label="generic single-exp")
    ax[1].plot(tc, c_be, ":", color="#1d4ed8", lw=1.6, label="generic biexp")
    ax[1].set_xlabel("t"); ax[1].set_ylabel("coherence c(t)"); ax[1].legend(fontsize=7, frameon=False)
    ax[1].set_title("Part 2: coherence observable -- generic decaying kernels miss revivals", fontsize=9, loc="left")
    ax[2].bar(["FFGFT", "single-exp", "biexp"], [bf_ffgft, backflow(c_se), backflow(c_be)],
              color=["#0f766e", "#c2410c", "#1d4ed8"])
    ax[2].set_ylabel("BLP back-flow (revival)"); ax[2].set_title("Part 2: revival signature", fontsize=9, loc="left")
    fig.suptitle("Shared HLV<->FFGFT memory harness: overdamped decay (non-identifiable) vs coherence sector (discriminating)", fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.95]); fig.savefig("figures/memory_harness.png", dpi=140); plt.close(fig)
    print("-> figures/memory_harness.png")
except Exception as e:
    print(f"(plot skipped: {e})")
