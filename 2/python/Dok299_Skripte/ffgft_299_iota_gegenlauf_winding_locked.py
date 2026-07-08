#!/usr/bin/env python3
# ffgft_299_iota_gegenlauf_winding_locked.py   (v0.2, supersedes v0.1 time branch)
# ---------------------------------------------------------------------------
# CORRECTION of the v0.1 time branch. v0.1 reduced the spiral-time window to a
# winding-LESS hard-reset kernel and then "found" it carries no back-flow --
# near-tautological, because a kernel with no winding cannot carry a revival by
# construction. That did NOT test Marcel's actual object.
#
# Marcel's object is a SPIRAL-time window: it is defined by a WINDING ANGLE
# theta (the pitch of the archimedean spiral in recursion time). The angle IS
# the structure. This version writes theta explicitly into the kernel and
# sweeps it, so the answer is no longer fixed by construction:
#
#   k_theta(s) = exp(-s/tau) * cos(theta * s),   s = 0..M-1   (finite window)
#
#   theta -> 0 : pure decaying window = Markov / hard-reset limit -> back-flow 0
#   theta > 0  : coherent winding -> spectral weight at omega=theta -> the
#                dephasing can carry (1-cos) revival IF the finite window
#                ("hard reset", width ~1/M) leaves the line sharp enough.
#
# The real, non-tautological question: at Marcel's winding theta*, does the
# coherent winding beat the phase-shuffled null band (same envelope, incoherent
# phase) -> FORCED; or does the hard-reset broadening kill the revival so it
# sits in the band -> ALLOWED (Markov-limit boundary, Dok 297).
#
# NON-CIRCULAR: the winding is IN the object; the nulls share the SAME envelope
# and support (hard reset matched) and differ ONLY in coherent phase, so the
# test isolates the contribution of the ANGLE. No hard=copy; witness (FFGFT
# back-flow 5.125) recomputed from the corpus kernel, independent of theta.
#
# NOTE ON "U3": the OP8/EEG "U3" (a 3rd-order statistical term, confirmed to add
# nothing beyond the Markov limit on real data) is a DIFFERENT object from the
# code's "U3-window". This run concerns the spiral-time WINDOW and its winding.
# ---------------------------------------------------------------------------

import json, hashlib, os
from itertools import product, combinations
import numpy as np
from numpy.linalg import eigvalsh

SEED = 20260708
rng = np.random.default_rng(SEED)
OUTDIR = os.path.dirname(os.path.abspath(__file__))
PHI = (1 + 5**0.5) / 2

# ---- corpus kernel + independent witness (verbatim constants, Dok 283) ----
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
        u = np.exp(1j * amp * (1 + mu)); H[i, j] += -u; H[j, i] += -np.conj(u); deg[i] += 1; deg[j] += 1
    H[np.diag_indices(Nn)] = deg; return H

def ffgft_bath(L=3, amp=0.5 * np.pi, n_modes=6):
    Nn, edges = _build_T4(L)
    lam = eigvalsh(_conn_laplacian(Nn, edges, amp)); lam = lam[lam > 1e-6]
    omega = np.sqrt(lam); uniq = []
    for w in omega:
        if not uniq or abs(w - uniq[-1][0]) > 1e-3: uniq.append([w, 1])
        else: uniq[-1][1] += 1
    uniq = uniq[:n_modes]
    return np.array([u[0] for u in uniq]), np.array([u[1] for u in uniq], float)

OMEGA_F, G2_F = ffgft_bath()
tc   = np.linspace(1e-3, 80.0, 4000)
COUP = 2.4
g    = COUP * np.sqrt(G2_F) / np.sqrt(G2_F.sum())
def backflow(c): d = np.diff(c); return float(np.sum(d[d > 0]))
Gamma_F = sum((2*a**2/w**2)*(1 - np.cos(w*tc)) for w, a in zip(OMEGA_F, g))
BF_WITNESS = backflow(np.exp(-Gamma_F))            # 5.125, derived not set

# ===========================================================================
# spiral-time window with explicit winding angle theta
# ===========================================================================
M, TAU = 12, 6.0                                   # Marcel's finite window (hard reset after M)
s = np.arange(M, dtype=float)
env = np.exp(-s / TAU)                             # envelope (shared with the nulls)

NPAD = 512
omega_grid = np.fft.rfftfreq(NPAD, d=1.0) * 2*np.pi      # winding freq axis, [0, pi]
# precompute the dephasing basis (1 - cos(omega t)) / omega^2 once
with np.errstate(divide='ignore', invalid='ignore'):
    W = (1 - np.cos(np.outer(omega_grid, tc))) / (omega_grid[:, None]**2)
W[0, :] = 0.0                                      # DC carries no dephasing
GSCALE = COUP**2                                   # same coupling scale as the corpus witness

def kernel_backflow(kern):
    """finite memory kernel -> power spectrum -> dephasing Gamma(t) -> back-flow."""
    S = np.abs(np.fft.rfft(kern, n=NPAD))**2
    S = S / (S.sum() + 1e-18)
    Gamma = GSCALE * (S @ W)
    return backflow(np.exp(-Gamma))

def spiral_window(theta):
    return env * np.cos(theta * s)                 # winding IS the structure

# ---- theta sweep: 0 (Markov limit) through the full winding range ----------
thetas = np.linspace(0.0, np.pi, 400)
bf_theta = np.array([kernel_backflow(spiral_window(th)) for th in thetas])

# ---- phase-shuffled null band: SAME envelope, incoherent phase -------------
# (destroys the coherent winding but keeps support/hard reset/energy)
null_bf = []
for _ in range(400):
    signs = rng.choice([-1.0, 1.0], size=M)
    phase = rng.uniform(0, 2*np.pi, size=M)
    kern = env * signs * np.cos(phase)             # incoherent taps, same envelope
    null_bf.append(kernel_backflow(kern))
null_bf = np.array(null_bf)
NULL_Q95 = float(np.quantile(null_bf, 0.95))
NULL_MED = float(np.median(null_bf))

# theta_c: smallest winding where coherent back-flow first exceeds the band
above = np.where(bf_theta > NULL_Q95)[0]
theta_c = float(thetas[above[0]]) if above.size else None

# ---- candidate windings to pin from the native carrier (labelled, not asserted)
anchors = {
    "markov_limit_theta_0":        0.0,
    "per_step_1_over_phi_rad":     1.0/PHI,                     # 0.618 rad
    "golden_angle_rad":            2*np.pi*(1 - 1/PHI),         # 2.3999 rad (137.5 deg)
    "two_pi_over_phi_rad":         2*np.pi/PHI,                 # 3.883 -> wraps; informative
}
anchor_bf = {k: (kernel_backflow(spiral_window(v % np.pi)), float(v))
             for k, v in anchors.items()}

# ===========================================================================
# geometric branch (unchanged, correct): fixed 63.435 deg reference
# ===========================================================================
REF_ANGLE = float(np.degrees(np.arccos(1/np.sqrt(5))))
def six_axes_icosahedral():
    V = np.array([[0,1,PHI],[0,-1,PHI],[1,PHI,0],[-1,PHI,0],[PHI,0,1],[PHI,0,-1]], float)
    return V / np.linalg.norm(V, axis=1, keepdims=True)
def geo_discriminant(axes):
    ang = [np.degrees(np.arccos(np.clip(abs(float(np.dot(axes[i], axes[j]))), 0, 1)))
           for i, j in combinations(range(len(axes)), 2)]
    return float(np.sqrt(np.mean((np.array(ang) - REF_ANGLE)**2)))
d_icosa = geo_discriminant(six_axes_icosahedral())
rand_geo = np.array([geo_discriminant(
    (lambda A: A/np.linalg.norm(A,axis=1,keepdims=True))(rng.normal(size=(6,3))))
    for _ in range(2000)])
geo_ok = d_icosa < 1.0 and float(np.quantile(rand_geo, 0.05)) > 5.0

# ===========================================================================
# non-circularity self-checks
# ===========================================================================
assert BF_WITNESS > 4.5, "witness must be the derived FFGFT back-flow (~5.125)"
assert bf_theta[0] < NULL_Q95 + 1e-9, "theta=0 (no winding) must sit in the Markov band"
assert geo_discriminant(six_axes_icosahedral()) < 1.0

# ---- verdict is now CONDITIONAL on the winding, not fixed by construction ---
result = {
    "protocol": "FFGFT-IOTA-GEGENLAUF-2-WINDING", "version": "v0.2-locked", "seed": SEED,
    "supersedes": "v0.1 time branch (winding-less reduction; near-tautological)",
    "claim_boundary": "finite-proxy diagnostic; no subset proof, no physics/mass/QFT/GR claim",
    "witness_backflow_FFGFT": BF_WITNESS,
    "time_branch_winding": {
        "window_M": M, "window_tau": TAU,
        "phase_shuffled_null_median": NULL_MED,
        "phase_shuffled_null_q95": NULL_Q95,
        "theta_sweep_backflow_min": float(bf_theta.min()),
        "theta_sweep_backflow_max": float(bf_theta.max()),
        "theta_at_backflow_max": float(thetas[int(bf_theta.argmax())]),
        "theta_c_first_exceeds_band_rad": theta_c,
        "backflow_at_candidate_windings": {k: {"backflow": bf, "theta_rad": th,
                                               "above_band": bool(bf > NULL_Q95)}
                                           for k, (bf, th) in anchor_bf.items()},
        "reading": ("theta=0 sits in the band (Markov limit, sanity). Whether the "
                    "spiral WINDOW forces back-flow depends on the actual winding "
                    "theta* of the native carrier: allowed if theta* < theta_c, "
                    "forced if theta* >= theta_c. theta* must be pinned from HLV.")
    },
    "geo_branch": {"reference_angle_deg": REF_ANGLE,
                   "icosahedral_discriminant_deg": d_icosa,
                   "random_star_median_deg": float(np.median(rand_geo)),
                   "valid": bool(geo_ok)},
}
with open(os.path.join(OUTDIR, "ffgft_299_gegenlauf_winding_result.json"), "w") as f:
    json.dump(result, f, indent=2)
with open(os.path.abspath(__file__), "rb") as f:
    sha = hashlib.sha256(f.read()).hexdigest()
with open(os.path.join(OUTDIR, "ffgft_299_gegenlauf_winding_LOCK.json"), "w") as f:
    json.dump({"script": os.path.basename(__file__), "sha256": sha, "seed": SEED}, f, indent=2)

print("FFGFT-IOTA-GEGENLAUF-2  (winding-parametrized, locked, seed=%d)" % SEED)
print("-"*66)
print("independent witness   : FFGFT back-flow = %.3f" % BF_WITNESS)
print("window (M, tau)       : (%d, %.1f)   winding theta swept 0..pi" % (M, TAU))
print("phase-shuffled null   : median %.3f   q95 %.3f" % (NULL_MED, NULL_Q95))
print("theta-sweep back-flow : min %.3f   max %.3f  at theta=%.3f rad"
      % (bf_theta.min(), bf_theta.max(), thetas[int(bf_theta.argmax())]))
print("theta_c (first > band): %s" % ("%.3f rad" % theta_c if theta_c else "never (stays in band)"))
print("\ncandidate windings (to be pinned from the native carrier):")
for k, (bf, th) in anchor_bf.items():
    print("  %-26s theta=%.3f rad  back-flow=%.3f  %s"
          % (k, th, bf, "ABOVE band" if bf > NULL_Q95 else "in band"))
print("\ngeo branch: icosa %.3f deg vs random median %.3f deg -> valid=%s"
      % (d_icosa, np.median(rand_geo), geo_ok))
print("script SHA256:", sha)
