# Dok271_274_Skripte — FFGFT spectral discriminator (substrate axis)

Reproducible FFGFT-side testbed for the substrate axis of Dok. 271 (FFGFT↔HLV)
and Dok. 274 (IPI-Feld-Karte). Operationalises the periodic ↔ aperiodic ↔ random
fork: it computes the scale-free spectral fingerprint of a graph Laplacian and
compares a periodic torus (FFGFT's T⁴), a degree-matched random null, and — via the
same pipeline — any externally supplied spectrum (e.g. Krüger's HLV quasicrystal).

## hlv_ffgft_spectral.py
- `torus_laplacian_eigs(D, L)` — exact periodic-torus Laplacian eigenvalues (D = 2,3,4; D=4 = T⁴).
- `erdos_renyi_laplacian_eigs(N, k, rng)` — degree-matched random null.
- `analyze_spectrum(eigs, name)` — scale-free, unfolding-free discriminators:
  consecutive level-spacing ratio ⟨r⟩ (Poisson ≈ 0.386, GOE ≈ 0.531), degeneracy
  fraction, gap richness (Cantor indicator), low eigenvalue ratios. **Drop any
  quasicrystal eigenvalues in here for an apples-to-apples row.**
- `sum_of_squares_ladder(D)` — the FFGFT periodic-arm prediction (|n|² ladder; in D=4
  every integer is hit, Lagrange).
- `recovery_limit_fit()` — leading dispersion exponent (≈2, λ∝|k|²) and residual (≈−1/12).

Run: `python3 hlv_ffgft_spectral.py` (numpy only; seeded 20260609; writes
`ffgft_periodic_spectral_summary.csv`).

Expected separation: periodic → ⟨r⟩≈0 + high degeneracy; random → ⟨r⟩≈0.50; a
genuine quasicrystal → intermediate ⟨r⟩ + high gap richness. If not separable →
clean negative. Falsification before interpretation.

---

# (DE) FFGFT-Spektral-Diskriminator (Substrat-Achse)

Reproduzierbarer FFGFT-Testbed zur Substrat-Achse von Dok. 271/274. Operationalisiert
die Gabel periodisch ↔ aperiodisch ↔ zufällig: skaleninvarianter Spektral-Fingerabdruck
eines Graph-Laplace-Operators; vergleicht periodischen Torus (FFGFTs T⁴), gradangepasstes
Zufalls-Nullmodell und — über dieselbe Pipeline — jedes extern gelieferte Spektrum (z. B.
Krügers HLV-Quasikristall). Schnittstelle: `analyze_spectrum(eigenwerte, name)`.
Diskriminatoren: ⟨r⟩ (Poisson ≈ 0,386 / GOE ≈ 0,531), Entartungsanteil, Lücken-Reichhaltigkeit.
numpy-only, Seed 20260609. Erwartung: periodisch ⟨r⟩≈0/entartet, zufällig ⟨r⟩≈0,50,
Quasikristall intermediär+lückenreich; sonst sauberes Negativ.

## hlv_glattice_reproduction.py
Independent reconstruction of Marcel Krueger's HLV cut-and-project G-lattice
(exact Z^6 icosahedral projection + k-NN rule, rebuilt in NumPy WITHOUT running the
upstream engine), run through the identical analyze_spectrum pipeline vs periodic and
random controls. First result: not periodic (clear), but bulk <r> ~ GOE (not yet
separable from random); aperiodic signature only weak, in gap structure / low-mode
sector. d_s ~ 2.7 (cf. reported 2.49). Needs hlv_ffgft_spectral.py beside it.
