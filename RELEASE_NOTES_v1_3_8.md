# Release Notes — v1.3.8 (4 September 2026)

**DOI:** to be assigned on Zenodo publication — supersedes v1.3.7
Running corrections: **[2/pdf/190_T0_Korrekturen_En.pdf](2/pdf/190_T0_Korrekturen_En.pdf)**

**Author:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Overview

This release adds Docs. 344–348: the Furey/GALG convergence (344), the
literature comparison (345), and the new algebraic results on charge
quantisation (346), Gell-Mann–Nishijima (347), and generation structure /
coupling matrix / CKM complexity (348).

---

## New documents

### Doc. 344 — Furey fermions in GALG and FFGFT (DE+EN)
Su[0] = Vss[0]: neutrino = vacuum of Clifford-Fock space [B]. Sector pairing
k↦−k has no fixed points → all neutrinos Dirac [B/S]. nEXO decides.

### Doc. 345 — FFGFT in literature comparison (DE+EN)
Froggatt-Nielsen: same hierarchy principle but FFGFT forces exponents from
Galois group orders [K]. After Docs. 346/347: at charge content equal with
Furey/Dixon. All 14 references verified 4 September 2026.

### Doc. 346 — Charge quantisation from GF(27)* (DE+EN)
Two Galois properties classify all SM fermions [B]:
QR mod 13 ↔ electric neutrality; N mod 3 ↔ colour charge.
Q ∈ {0,±1/3,±2/3,±1} from Legendre symbol [B].
Check script: pruef_346_ladungsquantisierung.py.

### Doc. 347 — Gell-Mann–Nishijima from Galois (DE+EN)
Q = I₃ + Y/2 algebraically derived [B]: Y from Legendre symbol (Doc. 346),
I₃ from jE7 projector (Doc. 344). All four fermion charges exact.
Theorem E [S] of Doc. 346 closed.

### Doc. 348 — Generation structure and coupling matrix from GF(27) (DE+EN)
Root orbits of f₁–f₄ are genuine Frobenius orbits; 3 elements = 3 generations [B].
f₃×f₄ = permutation matrix [B]; Gen.2↔Gen.3 swap forced.
f₁×f₃: entries 1/√2 [B], consistent with large PMNS angles.
CKM complexity: δ_CP ≈ 68° not derivable from GF(27)*; usable as phase anchor.
Check script: pruef_348_ckm.py.

---

## Register entries (Doc. 190)

R106–R110 cover Docs. 342–345 and the Galois results.
New entries to be added: R111 (Docs. 346–348, charge quantisation and
Gell-Mann–Nishijima from Galois).

---

## What has not changed

ξ, T̃·m=1, all derivation chains from v1.3.7 unchanged.
