#!/usr/bin/env python3
# ffgft_299_iota_gegenlauf_locked.py
# ---------------------------------------------------------------------------
# FFGFT-side counter-run to Krueger's HLV-FFGFT-IOTA-BRIDGE1.
# Pre-registered, locked BEFORE the run (mirror of the SHA256 sealing
# discipline used on the HLV side). Dok 299, iota-embedding forcing protocol.
#
# WHY THIS RUN IS NOT CIRCULAR
# ----------------------------
# The circularity that has to be avoided is exactly the mirror of the one
# found on the HLV side (measuring a carrier against a reference built from
# the same carrier -> trivial distance 0). Here it is avoided *structurally*,
# not by assertion:
#
#   OBJECT under test  = U3, Marcel's finite hard-reset spiral-time window.
#                        Built independently of the witness; never correlated
#                        against a copy of itself (no `hard = U3.copy()`).
#   INDEPENDENT WITNESS = the BLP back-flow of the FFGFT recursion memory
#                        kernel (Dok 283 / Dok 282, value 5.125). It is a
#                        *derived* property of the T4 connection-Laplacian
#                        spectrum, recomputed here from the corpus constants
#                        (never hard-coded, never taken from U3).
#
# A hard-reset finite window CANNOT reproduce the back-flow by construction
# (monotone dephasing -> back-flow 0). So the witness is (a) independent of
# U3 and (b) unforgeable by U3. That is the whole point: object and witness
# live on different sides. The forbidden design -- testing the FFGFT kernel
# against an FFGFT-derived reference and "finding" it matches -- is never run.
#
# PRE-REGISTERED QUESTION (time sector, iota_dyn)
# -----------------------------------------------
# Does U3 carry the FFGFT recursion's back-flow signature (i.e. exceed the
# generic monotone/Markov nulls on the back-flow observable), or does it sit
# with the nulls at back-flow ~ 0?
#   - U3 sits in the null band   -> iota_dyn ALLOWED, not forced == Dok 297
#     boundary reading confirmed (U3 = degenerate Markov-limit section).
#   - U3 near the FFGFT witness   -> the simple embedding into the Markov
#     limit is FALSIFIED; a richer embedding is required.
#
# Part B adds the geometric-branch discriminant (iota_geo) the way Dok 299
# fixes it and the HLV v0.1 run did NOT: axis angles measured against a FIXED
# icosahedral reference (all 15 pairwise angles arccos(1/sqrt5)=63.435 deg),
# never against axes taken from the carrier itself. A random star then does
# NOT score 0 (unlike the self-referential C3/A5 score).
# ---------------------------------------------------------------------------

import json, hashlib, csv, os
from itertools import product, combinations
import numpy as np
from numpy.linalg import eigvalsh
from scipy.optimize import minimize

SEED = 20260708
rng = np.random.default_rng(SEED)
OUTDIR = os.path.dirname(os.path.abspath(__file__))

# ===========================================================================
# FFGFT memory kernel -- constants FROM THE CORPUS (deterministic), copied
# verbatim from Dok283_Skripte/ffgft_283_memory_harness_shared.py so the
# witness is the proven one, not a re-invention.
# ===========================================================================
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
    wk = np.array([u[0] for u in uniq]); g2 = np.array([u[1] for u in uniq], float)
    return wk, g2

OMEGA_F, G2_F = ffgft_bath()

# coherence observable c(t)=exp(-Gamma(t)); COUP is the single free coupling (fixed truth)
tc   = np.linspace(1e-3, 80.0, 4000)
COUP = 2.4
g    = COUP * np.sqrt(G2_F) / np.sqrt(G2_F.sum())

def backflow(c):
    d = np.diff(c); return float(np.sum(d[d > 0]))

def gamma_from_modes(omega, gg):
    """Dephasing exponent for a discrete oscillator bath (corpus form)."""
    return sum((2*a**2/w**2)*(1 - np.cos(w*tc)) for w, a in zip(omega, gg))

# --- the independent witness: FFGFT discrete-spectrum back-flow (5.125) ---
Gamma_F  = gamma_from_modes(OMEGA_F, g)
c_ffgft  = np.exp(-Gamma_F)
BF_WITNESS = backflow(c_ffgft)          # derived, NOT hard-coded

# ===========================================================================
# PART A -- time branch (iota_dyn)
# OBJECT under test: U3 = Marcel's finite hard-reset spiral-time window,
# built independently of the witness.
# ===========================================================================
def u3_hard_reset_window(M=12, tau=6.0, T=75):
    """Finite exponential window, hard reset after M steps (Marcel's U3)."""
    k = np.arange(T, dtype=float)
    w = np.zeros(T); w[:M] = np.exp(-k[:M]/tau)
    return w / (w.sum() + 1e-12)

def coherence_from_window(window):
    """
    Map a finite time-window memory kernel to the same coherence observable.
    A bounded (hard-reset) kernel gives a bounded, saturating Gamma -> monotone
    c(t) -> back-flow 0. This is U3 evaluated on FFGFT's home observable; no
    term compares U3 to a copy of itself.
    """
    # window -> spectral content via its (real) power spectrum, mapped onto tc
    W = np.abs(np.fft.rfft(window))**2
    freqs = np.fft.rfftfreq(len(window), d=1.0)
    freqs = freqs[1:]; W = W[1:]                      # drop DC
    if W.sum() <= 0:
        return np.ones_like(tc)
    Wn = W / W.sum()
    # bounded, non-oscillatory dephasing: sum of (1-cos) is present but the
    # amplitudes decay so fast (hard reset) that Gamma saturates monotonically
    scale = COUP**2 * 0.5
    Gamma = sum(scale * a * (1 - np.cos(2*np.pi*f*tc)) for f, a in zip(freqs, Wn))
    return np.exp(-Gamma)

U3 = u3_hard_reset_window()
c_u3 = coherence_from_window(U3)
BF_U3 = backflow(c_u3)

# --- time-axis null family (Dok 299 iota_dyn), matched to c_ffgft ----------
def fit_curve(model, x0, bnds):
    res = minimize(lambda p: np.sqrt(np.mean((model(p) - c_ffgft)**2)),
                   x0, bounds=bnds, method="L-BFGS-B")
    return model(res.x), float(np.sqrt(np.mean((model(res.x) - c_ffgft)**2)))

nulls = {}
# memory-free Markov (single exponential decay)
c_se, r_se = fit_curve(lambda p: np.exp(-p[0]*tc), [0.1], [(1e-3, 5)])
nulls["memory_free_markov"] = backflow(c_se)
# biexponential decaying
c_be, r_be = fit_curve(lambda p: p[0]*np.exp(-p[1]*tc) + (1-p[0])*np.exp(-p[2]*tc),
                       [0.5, 0.3, 0.05], [(0, 1), (1e-3, 5), (1e-3, 5)])
nulls["biexponential_decay"] = backflow(c_be)
# generic bounded window (random finite hard-reset windows, same support as U3)
gbw = []
for _ in range(200):
    M = int(rng.integers(6, 20)); tau = float(rng.uniform(2, 12))
    w = np.zeros(75); kk = np.arange(M); w[:M] = np.exp(-kk/tau) * rng.uniform(0.5, 1.5, size=M)
    w = np.clip(w, 0, None); w /= (w.sum()+1e-12)
    gbw.append(backflow(coherence_from_window(w)))
nulls["generic_bounded_window_median"] = float(np.median(gbw))
# frequency-shuffled bath: same degeneracies g^2, random frequencies (destroys
# the coherent revival structure) -> establishes the back-flow band
freq_shuffled = []
for _ in range(200):
    w_rand = np.sort(rng.uniform(OMEGA_F.min(), OMEGA_F.max(), size=len(OMEGA_F)))
    freq_shuffled.append(backflow(np.exp(-gamma_from_modes(w_rand, g))))
nulls["frequency_shuffled_bath_median"] = float(np.median(freq_shuffled))
null_band_hi = float(np.quantile(np.array(gbw + freq_shuffled), 0.95))
gbw_q95 = float(np.quantile(np.array(gbw), 0.95))   # what a GENERIC finite window can reach

# empirical p: fraction of nulls with back-flow >= U3 back-flow
all_null_bf = np.array(gbw + freq_shuffled)
p_emp = float((np.sum(all_null_bf >= BF_U3) + 1) / (len(all_null_bf) + 1))

# ===========================================================================
# PART B -- geometric branch (iota_geo): FIXED icosahedral reference
# (the fix the HLV v0.1 run was missing). Angles measured against a fixed
# 63.435 deg reference, NEVER against axes taken from the carrier.
# ===========================================================================
PHI = (1 + 5**0.5) / 2
REF_ANGLE = float(np.degrees(np.arccos(1/np.sqrt(5))))   # 63.4349...

def six_axes_icosahedral():
    V = np.array([[0,1,PHI],[0,-1,PHI],[1,PHI,0],[-1,PHI,0],[PHI,0,1],[PHI,0,-1]], float)
    return V / np.linalg.norm(V, axis=1, keepdims=True)

def pairwise_angles(axes):
    ang = []
    for i, j in combinations(range(len(axes)), 2):
        c = abs(float(np.dot(axes[i], axes[j])))        # undirected axes -> abs
        ang.append(np.degrees(np.arccos(np.clip(c, 0, 1))))
    return np.array(ang)

def geo_discriminant(axes):
    """RMS deviation of the 15 pairwise axis angles from the FIXED reference."""
    return float(np.sqrt(np.mean((pairwise_angles(axes) - REF_ANGLE)**2)))

d_icosa = geo_discriminant(six_axes_icosahedral())       # exact carrier -> ~0
rand_d = []
for _ in range(2000):
    A = rng.normal(size=(6, 3)); A /= np.linalg.norm(A, axis=1, keepdims=True)
    rand_d.append(geo_discriminant(A))
rand_d = np.array(rand_d)
geo_null_median = float(np.median(rand_d))
geo_null_p05    = float(np.quantile(rand_d, 0.05))

# ===========================================================================
# PRE-REGISTERED VERDICT (locked before the run)
# ===========================================================================
GATES = {
    "time_forced_if_BF_U3_exceeds_generic_window_band": gbw_q95,   # U3 must do more than a generic finite window
    "time_forced_strong_if_BF_U3_at_least_half_witness": 0.5 * BF_WITNESS,
    "geo_carrier_forces_if_discriminant_below": 1.0,     # exact icosa ~0 (deg)
    "geo_generic_must_exceed": 5.0,                       # random stars land well above (deg)
}
if BF_U3 > GATES["time_forced_if_BF_U3_exceeds_generic_window_band"]:
    time_verdict = "IOTA_DYN_FORCED__U3_exceeds_generic_finite_window__297_boundary_FALSIFIED"
elif BF_U3 <= GATES["time_forced_if_BF_U3_exceeds_generic_window_band"] and p_emp > 0.20:
    time_verdict = "IOTA_DYN_ALLOWED_NOT_FORCED__U3_indistinguishable_from_generic_window__297_CONFIRMED"
else:
    time_verdict = "IOTA_DYN_INCONCLUSIVE"

geo_discriminates = (d_icosa < GATES["geo_carrier_forces_if_discriminant_below"]
                     and geo_null_p05 > GATES["geo_generic_must_exceed"])
geo_verdict = ("GEO_DISCRIMINANT_VALID__fixed_reference_separates_icosa_from_generic"
               if geo_discriminates else "GEO_DISCRIMINANT_DEGENERATE")

# ===========================================================================
# non-circularity self-checks (fail loudly if the design is violated)
# ===========================================================================
assert BF_WITNESS > 4.5, "witness must be the derived FFGFT back-flow (~5.125)"
# witness recomputed from the kernel, not read from U3:
assert not np.allclose(c_u3, c_ffgft), "U3 must not equal the FFGFT coherence by construction"
# geometric discriminant must reject a random star (unlike a self-referential score):
assert geo_null_median > REF_ANGLE * 0.05, "fixed-reference geo discriminant must not score random stars ~0"

result = {
    "protocol": "FFGFT-IOTA-GEGENLAUF-1",
    "version": "v0.1-locked",
    "seed": SEED,
    "claim_boundary": "finite-proxy time/geometry diagnostic only; no subset proof, no physics/mass/QFT/GR claim",
    "non_circular_by": "object (U3, external) and witness (FFGFT-derived back-flow) on different sides; "
                       "no self-correlation term; witness recomputed from corpus kernel; "
                       "geometric angles vs a FIXED reference, not axes from the carrier",
    "witness_backflow_FFGFT": BF_WITNESS,
    "ffgft_kernel_omega": [round(float(x), 4) for x in OMEGA_F],
    "ffgft_kernel_g2": [int(x) for x in G2_F],
    "time_branch": {
        "U3_backflow": BF_U3,
        "nulls": nulls,
        "null_band_hi_q95": null_band_hi,
        "generic_window_band_q95": gbw_q95,
        "empirical_p_null_ge_U3": p_emp,
        "gates": {k: GATES[k] for k in ("time_forced_if_BF_U3_exceeds_generic_window_band",
                                        "time_forced_strong_if_BF_U3_at_least_half_witness")},
        "verdict": time_verdict,
    },
    "geo_branch": {
        "reference_angle_deg": REF_ANGLE,
        "icosahedral_carrier_discriminant_deg": d_icosa,
        "random_star_discriminant_median_deg": geo_null_median,
        "random_star_discriminant_p05_deg": geo_null_p05,
        "verdict": geo_verdict,
    },
}

with open(os.path.join(OUTDIR, "ffgft_299_gegenlauf_result.json"), "w") as f:
    json.dump(result, f, indent=2)

# self-hash for the pre-registration lock (mirror of the HLV-side SHA256 seal)
with open(os.path.abspath(__file__), "rb") as f:
    script_sha = hashlib.sha256(f.read()).hexdigest()
with open(os.path.join(OUTDIR, "ffgft_299_gegenlauf_LOCK.json"), "w") as f:
    json.dump({"script": os.path.basename(__file__), "sha256": script_sha, "seed": SEED,
               "witness_backflow_FFGFT": BF_WITNESS}, f, indent=2)

print("FFGFT-IOTA-GEGENLAUF-1  (locked, seed=%d)" % SEED)
print("-"*66)
print("independent witness  : FFGFT back-flow = %.3f  (Dok-282 value 5.125)" % BF_WITNESS)
print("kernel omega_k       :", np.round(OMEGA_F, 4))
print("kernel g_k^2 (deg)   :", G2_F.astype(int))
print()
print("TIME BRANCH (iota_dyn)  -- object = U3 hard-reset window (external)")
print("  U3 back-flow        : %.4f" % BF_U3)
for k, v in nulls.items():
    print("  null %-28s: %.4f" % (k, v))
print("  null band hi (q95)  : %.4f" % null_band_hi)
print("  empirical p(null>=U3): %.3f" % p_emp)
print("  VERDICT             :", time_verdict)
print()
print("GEO BRANCH (iota_geo)  -- fixed 63.435 deg reference (not self-star)")
print("  icosahedral carrier : %.4f deg   (exact -> ~0)" % d_icosa)
print("  random star median  : %.4f deg" % geo_null_median)
print("  random star p05     : %.4f deg" % geo_null_p05)
print("  VERDICT             :", geo_verdict)
print()
print("script SHA256        :", script_sha)
