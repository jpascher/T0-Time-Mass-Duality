# BD12-XCORE — FFGFT Mass-Core Declaration (pre-registered)

**Author:** Johann Pascher (FFGFT / T0 mass–time duality)
**For:** the HLV BD12-XCORE interface (Krüger, *Mass-Core Docking for the HLV Recursive Host Carrier*, Zenodo 10.5281/zenodo.20780458)
**Reproducer:** `bd12_xcore_ffgft.py` (numpy-only, seeded)

## Purpose
A candidate external mass-core for BD12-XCORE, stated as a **frozen transformation with no
post-fit freedom**, in matched-null format, so the dock either reproduces the charged-lepton
sector under fixed rules or it fails. It is symmetric: random inputs yield FAIL.

## Frozen inputs (no free parameters)
- `r = √2`  — circulant amplitude (this value, and only this value, forces Koide Q = 2/3)
- `θ = 2/9` — Koide phase
- Z₃ / Foot–Koide spectrum: `μ_k = 1 + √2·cos(2/9 + 2πk/3)`, k = 0,1,2

## Pre-registered bridge rule
- mass ratios: `m_k = μ_k²`
- single scale from the mass-circle (`T̃·m = 1`): `M = 1/T`, fixed by one lepton mass
- **constraints:** the dock must NOT be built on `L_nat` (the carrier Laplacian — the masses are
  not there); and the map is a fixed algebraic transformation (a reformulation of one T⁴ structure),
  adding no new physics — hence it cannot be a post-hoc fit.

## Frozen predictions
| quantity | FFGFT (frozen) | measured | deviation |
|---|---|---|---|
| Koide Q = Σμ²/(Σμ)² | 0.66666667 | 2/3 | exact |
| m_μ/m_e | 206.770 | 206.768 | 0.001 % |
| m_τ/m_e | 3477.47 | 3477.23 | 0.007 % |
| m_τ (Koide + m_e, m_μ) | 1776.969 MeV | 1776.860 | 0.006 % |

## Pass/Fail criterion (matched-null)
- **CANDIDATE** (frozen r=√2, θ=2/9): reproduces {Koide = 2/3, both ratios, τ-prediction}.
- **NULLS** (random r, θ): reproduce the *joint* set in ~0.000 % of cases
  (random r → Koide 0.18 %; random θ → both ratios 0.025 %; random (r,θ) → joint 0.000 %).
- **PASS** iff candidate meets the joint set AND beats the matched nulls. → here: **PASS**.

## Open, falsifiable dock question (for HLV)
Does the HLV carrier admit this frozen transformation under fixed rules and matched nulls?
- **yes** → carrier + core form a combined picture (hybrid, the core supplies the active Z₃
  content that the carrier's 3-slot lacks);
- **no** → a genuine incompatibility result.

This declaration supplies the frozen core; the dock run is performed on the HLV side.
