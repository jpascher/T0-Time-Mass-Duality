# Formula-level analysis

**Paper:** Krüger, Feeney, Wende — *Information-Theoretic Modeling of Neural Coherence via Triadic Spiral-Time Dynamics: A Framework for Neurodynamic Collapse*, Medinformatics 2026 (DOI 10.47852/bonviewMEDIN62029043).

**Purpose.** Test the *explicit mathematical claims* of the paper by computation, not by impression, before any feedback to the authors. Every verdict below is produced by a runnable script (`test_algebra.py`, `test_deltaphi.py`, `test_dynamics.py`, `make_figures.py`). The aim is the falsification-forward standard the authors apply on the HICE/FA-Hub side: separate what *holds* from what is *mislabeled*, *internally inconsistent*, *not derived*, or *not reproducible from the paper*.

---

## Verdict summary

| # | Claim | Section | Status |
|---|-------|---------|--------|
| 0 | Base time-axis: `psi(t)=t+i*phi(t)+j*chi(t)` on physical linear time | 2.1, 2.2.1 | **Foundational** — operator on the post-measurement axis (subsumes 3 & 5) |
| 1 | Triadic time `psi = t + i*phi + j*chi`, "reduced bicomplex/octonionic plane" | 2.1 | **Mislabeled** — it is the quaternions |
| 2 | Octonionic identity operator; non-associativity "explains psychological nonlinearity" | 2.10 | **Math holds, claim overreaches** |
| 3 | `DeltaPhi` instability functional | 2.6 vs 12/15 | **Internally inconsistent (two definitions)** |
| 4 | Critical threshold `DeltaPhi_c ≈ 0.40`, "not a free tuning parameter" | 2.5, 2.6.2 | **Not derived (free parameter)** |
| 5 | Healthy inward spirals / trauma limit cycles | 2.2.3, 2.9 | **Not derived from the specified equations** |
| 6 | `r ≈ 0.96`, `DeltaPhi_c ≈ 0.40` "across subjects" | 3.4 | **Not reproducible from the paper** |
| 7 | Axonal biphoton entanglement coupling `Gamma_axon` | 2.7–2.8 | **Speculative premise stated as established** |

---

## 0 — The base time-axis: *the operator is built on physical (post-measurement) time* (foundational)

This is the most consequential choice in the paper, and the one under which findings 3 and 5 are downstream symptoms. The Spiral-Time operator `psi(t) = t + i*phi(t) + j*chi(t)` takes physical, linear time `t` as its scalar base and writes `phi`, `chi` as functions of that same `t`. The paper is explicit that `t` is physical: U1 is defined as "linear physical time," tracking external chronology (§2.2.1).

- **Unit-independent.** For `t + i*phi + j*chi` to be one algebraic object the three components must be the same kind of quantity. The paper asserts dimensionlessness (§2.1.2) yet calls `t` physical time/chronology (§2.2.1); `phi`, `chi` are internal phase/identity coordinates. Adding a physical time to internal phases in one quaternionic sum is dimensionally incoherent unless all are first reduced to a common dimensionless measure. (Since i, j anticommute the object is quaternionic — `t` is the real part of a quaternion whose cross-term `ij = k` is never tracked; see finding 1.)
- **Deeper (compactification / measurement).** A framework-specific memory lives on the compact internal time-circle S¹ (discrete spectrum, exact recurrence, the coherence-sector back-flow 5.125). Writing `phi(t)`, `chi(t)` as single-valued functions of physical linear `t` flattens S¹ onto ℝ — it performs the projection S¹ → ℝ before any dynamics, and a single-valued function over linear time has no compact periodicity, so the recurrence is not representable on this axis. By the conversion-as-measurement principle (Appendix), committing to physical time is itself the disturbing, information-discarding projection — no apparatus needed. The notation has silently taken that step, hiding the one operation (conversion = measurement) that decides whether a memory claim is framework-specific or generic.
- **Consequence.** The operator is, by construction, post-measurement: whatever memory it carries on physical (EEG) time is generic. Findings 3 and 5 are the same root downstream — a Berry-phase holonomy (Eq 12/15) needs a closed loop / compact cycle, and a limit cycle needs non-gradient closed orbits; neither is supported on a linear physical-time axis, which is why ΔΦ equivocates between a [0,1] index and a holonomy, and why the spirals/limit cycles cannot be produced.
- **Constructive fix.** Define the operator on the compact, dimensionless internal time (cyclic); let physical SI time enter only through an explicit declared conversion — which is precisely what projects out the framework-specific part. Either the operator stays internal/compact (no direct EEG claim) or it is physical/SI (generic memory). `psi(t)=t+i*phi(t)+j*chi(t)` tries to be both. The minimal change is to declare two distinct times and write the conversion between them explicitly as the measurement it is.

## 1 — Triadic time algebra: *mislabeled* (`test_algebra.py`, Test A)

The stated relations `i^2 = j^2 = -1`, `ij = -ji` are exactly the imaginary quaternions: setting `k := ij` gives `k^2 = -1` and `{1,i,j,k}` closes into **H**, which is **associative** and **non-commutative**. A *bicomplex* plane requires the two imaginary units to **commute** (`ij = ji`); here `ij = -ji`, so the algebra is **not** bicomplex. A three-term operator `t + i*phi + j*chi` lives entirely inside a quaternion sub-algebra; **octonions are not required** for it. The "reduced bicomplex/octonionic" label is therefore incorrect — the correct name is quaternionic.

## 2 — Octonionic structure: *math holds, interpretation overreaches* (Test B)

Octonion non-associativity is **real**: the associator `(e1 e2)e4 - e1(e2 e4) = 2·e7 ≠ 0` (computed via Cayley–Dickson), while associators on a quaternionic triple vanish. That part is correct mathematics. The further step — that this non-associativity "directly matches empirical psychology" and is "the first physics-based explanation for psychological nonlinearity" — is an **interpretive analogy**, not a derivation: no psychological quantity is computed from, constrained by, or tested against the algebra. The eight basis directions are assigned meanings ("trans-generational memory echoes," "intuition," …) by stipulation.

## 3 — `DeltaPhi`: *two incompatible definitions under one symbol* (`test_deltaphi.py`, Tests C, D)

- **Definition 1 (§2.6):** `DeltaPhi = a|dS| + b|dI| + g|dC|`, convex weights, each component in [0,1] ⇒ a **unitless weighted-L1 index in [0,1]**. It is linear in each component (constant slope = weight), so it has **no curvature and no intrinsic bifurcation**; the level set `DeltaPhi = c` is a flat polytope facet for every `c`.
- **Definition 2 (Eq 12, 15):** `DeltaPhi = ∮ (∇×A_HLV)·da ≈ Im ∮ <psi|∇θ|psi> dθ` — a **Berry-phase holonomy**, i.e. an **angle in radians** that ranges over `0 … 2π` and has no reason to lie in [0,1] or near 0.40 (a loop with `|gamma| = 0.40 rad` is a tiny ~29° cone; see `fig_deltaphi.png`).

A normalized deviation index and a radian holonomy are **different mathematical objects**. Calling both "`DeltaPhi`" and assigning both the same critical value 0.40 is an **equivocation**: the symbol is overloaded with two definitions that cannot be the same quantity.

## 4 — The 0.40 threshold: *not derived* (Tests C, E)

§2.5 states the value is "not imposed as a free tuning parameter" and that "the operator structure enforces the existence of a bounded instability surface." But:

- the L1 functional has **no intrinsic critical point** (it is linear) — the only structural statement available is the trivial bound `0 ≤ DeltaPhi ≤ 1` and the symmetric reference `DeltaPhi = d` (so `1/3` at `d = 1/3`);
- §2.6.2 itself attributes the `0.40` vs `0.333` gap to "dataset-specific weighting asymmetry, signal heterogeneity, and normalization window effects" — i.e. a **fitted/observed** number;
- at equal deviation `d = 0.40`, **every** convex weight set returns 0.40.

So 0.40 is an empirical/contour value, not a structurally enforced bifurcation, contradicting §2.5.

## 5 — Spirals and trauma limit cycles: *not derived from the specified equations* (`test_dynamics.py`, Test F; `fig_dynamics.png`)

The only dynamical mechanism given with **explicit potentials** (§2.4) is the gradient-flow part of the master equation, `dPsi/dt = -∇V_DLHR(Psi) (+ …)`. For any gradient flow,

```
dV/dt = ∇V · dPsi/dt = -|∇V|^2 ≤ 0,
```

so `V` is a strict Lyapunov function and the system **cannot have periodic orbits, limit cycles, or sustained spirals** — it relaxes to fixed points (theorem). Numerically: across 40 trajectories `V(t)` is monotonically decreasing (0 violations) and 0 closed orbits are found. Therefore the central phenomenology — "healthy cognition → stable inward spirals," "trauma loops → limit cycles around fixed χ basins" — does **not** follow from the specified dynamics. It would require the advection terms `lambda_phi ∂_phi`, `lambda_chi ∂_chi` or `W_oct`, which are never given concretely. As written, the dynamical picture is **asserted, not derived**.

*(Side observation: `V2(M) = a2 M^2 + b2 M^3 + c2 EM` contains a cubic `M^3` term, so `V → -∞` as `M → -∞`: the "energy landscape" has no global minimum and is unbounded below.)*

## 6 — `r ≈ 0.96`, `DeltaPhi_c ≈ 0.40` "across subjects": *not reproducible from the paper*

These are empirical EEG claims (§3.4). The paper provides no data table from which to recompute them; reproduction requires the external dataset (Zenodo 10.5281/zenodo.17990696) and the validation notebook (github.com/nwycomp/NeuroDynamics-Collapse-Validation-). A formula-level check cannot confirm or refute them; a fair test would need the dataset plus a pre-registered protocol with the nulls the authors themselves use on the HICE side (time-shuffle, present-state-matched, phase-randomized).

## 7 — Axonal biphoton entanglement: *speculative premise stated as established*

`Gamma_axon = g e^{i phi} E12 + g' e^{j chi} E23` (§2.8) is built on "experimental findings" of biphoton entanglement and long-range coherence in myelinated axons, presented as settled "university-level research." Entanglement in warm, wet, myelinated axons is **not** established physics. This is not a formula error, but it is a **load-bearing empirical premise asserted as fact**, and it should be flagged as hypothesis.

---

## Defensible core (fair note)

Stripped of the superstructure, there is a sound, modest object: `DeltaPhi = |omega(t) - omega_memory(t)|` — the deviation of instantaneous phase velocity from a short-term phase-memory baseline — is an **interpretable, lightweight time-series instability feature**. As a signal-analysis operator (the framing of the companion respiratory paper) it is legitimate. The problems are confined to the HLV/octonion/consciousness superstructure, the `DeltaPhi` redefinition, and the un-derived threshold and dynamics.

## Appendix — decompactification reading (J. Pascher, **conjecture**)

Offered as a constructive bridge, explicitly conjectural. Temporal recursion does carry memory, and it maps onto FFGFT's own structure (recursion operator R; memory kernel as the Fourier transform of the connection-Laplacian spectral density).

FFGFT's memory has **two faces**. On the *overdamped/relaxation* observable the kernel is a positive multi-exponential and a generic biexponential reproduces it (residual ~1e-3) — non-identifiable, Stufe-0. On the *coherence* observable `c(t) = exp(-Gamma(t))` — its home sector — the discrete spectrum produces a genuine revival: **back-flow 5.125**, which generic decaying kernels cannot reproduce (back-flow 0). So the memory is discriminating, but only on the coherence sector and only when **both** a discrete spectrum **and** preserved coherence (small Gamma) hold.

FFGFT is fundamentally **compact** (T⁴, discrete spectrum), and in that dimensionless representation the system always has memory: the discrete spectrum carries the exact recurrence behind the 5.125. What removes it is not a second physical accident but a **single principle — every conversion to SI units is itself a measurement.** A bare units rescaling (by `ħ, c`) is invertible and loses nothing; the disturbing step is committing the compact periodic internal time-circle `S¹` to physical non-periodic time `ℝ` over a finite window. That commitment is a **non-invertible, information-discarding map**: it keeps the local short-time behaviour and discards the global recurrence, exactly as a measurement selects a basis and drops the coherences. It is already present at the **mathematical** conversion (no apparatus needed); a **physical** measurement is the same projection with decoherence added on top — the strong-coupling end of the same operation, not a separate mechanism. This is the structural, representational sense of measurement FFGFT already takes: projection onto a read-out, not ontological collapse.

So a temporal-recursion memory effect in cellular/EEG data is **expected but generic**. The reading supports the modest core (recursion carries memory) and bounds the claim hard: a geometry-specific compact memory signature cannot appear in any SI-carrying result, because writing the result in SI has **already performed the disturbing projection**. SI-time EEG — the observable the paper's clinical sections use — is therefore post-measurement by construction, exactly the regime where FFGFT's own harness shows the memory to be generic, not a fingerprint. This is also why the base-time-axis choice (§0) is decisive: the operator is written on that post-measurement axis from the start.

---

### Reproducibility
- `test_algebra.py` — quaternion closure + bicomplex refutation (A); octonion associator (B)
- `test_deltaphi.py` — L1 bound/linearity (C); Berry-phase range (D); 0.40 as free knob (E)
- `test_dynamics.py` — gradient-flow Lyapunov / no-limit-cycle test (F)
- `test_compactification.py` — read-out as a non-invertible projection: compact back-flow 11.5 vs windowed 0.000, lines unresolved (G)
- `make_figures.py` — `fig_dynamics.png`, `fig_deltaphi.png`
