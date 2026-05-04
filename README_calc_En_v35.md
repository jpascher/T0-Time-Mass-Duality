# FFGFT / T0 Time-Mass Duality — Calculation Scripts

**Johann Pascher** · Upper Austria, Austria  
GitHub: [jpascher/T0-Time-Mass-Duality](https://github.com/jpascher/T0-Time-Mass-Duality)  
Zenodo: [10.5281/zenodo.18834145](https://doi.org/10.5281/zenodo.18834145)

---

## Overview

This package contains Python scripts for the numerical validation of
**FFGFT (Fundamental Fractal Geometric Field Theory)**, also known as
**T0 Time-Mass Duality**.

The central concept of the theory: all natural constants and particle masses
follow from a single dimensionless parameter

$$\xi = \frac{4}{3} \times 10^{-4}$$

which in turn is derivable from the Higgs field (Doc. 049, 190).

---

## Core Scripts (Main Directory)

### 1. `calc_De.py` — Main Calculator v3.5

Calculates **9 particle masses** and **47 physical constants**
from only three input values: $\xi$, $\ell_P$, $E_0$.

**Results:**
- Average mass error: **0.84 %**
- Average constant error: **0.0334 %**
- Best single prediction: $R_\text{gas}$ with 0.0000 %

**Corrections included (v3.5):**
- Tau prefactor corrected: $r_\tau = 8/3 \to 25/9$ (Doc. 190, Correction K2)
- $n_0$ (Loschmidt): unit error fixed (L → m³)
- $\Lambda$: no comparison with ΛCDM reference value (different cosmology models)
- $L_0 = \xi \cdot \ell_P$ and $t_0 = L_0/c$ added as output values

**Output:**
```
Calculated constants total: 47
Average mass error:      0.84 %
Average constant error:  0.0334 %
```

**Usage:**
```bash
python calc_De.py
```
Also generates `T0_berechnungsdaten.txt` and `T0_berechnungen.json`.

---

### 2. `calc-h-berechnug.py` — Calibration Check $\hbar$

Derives $\hbar$ from the Higgs field via $\xi$ and checks the internal
consistency of the theory.

**Derivation chain:**
$$\xi_\text{Higgs} = \frac{\lambda_h^2 \, v^2}{16\pi^3 \, m_h^2}
\;\longrightarrow\; L_0 = \xi \cdot \ell_P
\;\longrightarrow\; \hbar \sim \sqrt{\xi} \cdot \ell_P \cdot c$$

**Methodological note:**  
Since $\xi$ is the only free parameter, this calculation is not circular
but a **calibration check**: does $\xi_\text{Higgs}$ (computed from Higgs
parameters) agree with $\xi_\text{T0}$ (geometric target value)?
The $\hbar$ deviation always equals half the $\xi$ deviation
(due to $\sqrt{\xi}$) — this is the intended consistency test.

**Result:**
```
xi_Higgs   = 1.2994e-04  (dev. -2.54 % from T0 target)
hbar dev.  = -1.28 %     (= half xi deviation — consistency OK)
```

---

### 3. `calc-teilchen-untergrenze.py` — Lower Bounds of Particle Masses

Calculates three types of mass lower bounds in FFGFT:

| Type | Formula | Value |
|------|---------|-------|
| Cosmological minimum | $m_\text{min} = \hbar H_0 / c^2$ | $1{.}49 \times 10^{-33}$ eV |
| Lightest massive particle | $m_{\nu_e} = \xi^2 \cdot m_e$ | $9{.}08$ meV |
| xi-scale ladder | $m_n = \xi^n \cdot m_e$ | discrete, $n = 0, 1, 2, 3, \ldots$ |

**Neutrino formula:**
$$m_{\nu_i} = r_i \cdot \xi^2 \cdot m_e$$

| Neutrino | $r_i$ | $m_{\nu_i}$ | PDG limit |
|----------|--------|-------------|-----------|
| $\nu_e$  | $1$    | 9.08 meV    | < 45 meV (KATRIN) |
| $\nu_\mu$| $16/5$ | 29.07 meV   | < 190 keV |
| $\nu_\tau$| $25/9$ | 25.23 meV  | < 18.2 MeV |
| **Sum**  |        | **63.4 meV**| **< 120 meV ✓** |

---

### 4. `calc-resonanz-leiter.py` — Complete Resonance Ladder

Calculates all 12 fermions (leptons + quarks + neutrinos) with
exact fraction arithmetic (`fractions.Fraction`).

**Yukawa formula:**
$$m_i = r_i \cdot \xi^{p_i} \cdot v$$

**Exponent structure** (step size $\Delta p = 1/3$):

| $p$ | Particle |
|-----|---------|
| $-1/3$ | Top |
| $1/2$  | Bottom |
| $2/3$  | Tau, Charm |
| $1$    | Muon, Strange |
| $3/2$  | Electron, Up, Down |
| $\xi^2 \cdot m_e$ | Neutrinos |

---

## Additional Scripts (`2/python/`)

### Gravitational Constant and Field Theory

#### `G_drei_formeln_bedeutung.py`
Compares three different FFGFT derivations of the gravitational constant $G$
and analyses their geometric significance in the torus model.
Reports which formula yields the smallest deviation from CODATA.

#### `c1_geometrisch.py`
Geometric derivation of the coupling constant $C_1$ from the torus topology.
Connects $\xi$, $\ell_P$ and $c$ in the FFGFT fundamental formula.

#### `Yang-Mills.py`
Checks the consistency of the FFGFT field structure with Yang-Mills gauge theory.
Investigates whether the torsion geometry satisfies the Yang-Mills equations.

---

### Cosmology

#### `H0.py`
Derives the Hubble parameter $H_0$ from $\xi$ and the cosmological
torus geometry. Comparison with Planck-CMB and SH0ES measurements.
Addresses the Hubble tension in the FFGFT framework.

#### `t0_cosmic_data_analyzer.py`
Analyses cosmological observation data (CMB, BAO, Type Ia supernovae)
for consistency with the FFGFT torus model.
Comparison: $\Lambda$CDM vs. FFGFT cosmology.
*Requires: `numpy`, `matplotlib`, `pandas`, `scipy`*

#### `t0_cosmic_error_correction.py`
Corrects systematic errors in cosmological data sets
arising from the FFGFT projection principle:
fractal light paths are projected onto straight lines —
this error is quantified and corrected.

#### `t0_cosmic_qubit_simulator.py`
Simulates qubit operations at the cosmological $\xi$ scale level.
Connects quantum information (Doc. 173–176) with the cosmological
torus structure.
*Requires: `ephem`*

#### `max-mass.py`
Calculates the maximum mass/energy possible in FFGFT
before $t_0$ is reached as the lower bound.
Generates `max_masse_pruefung.png`.

---

### Anomalous Magnetic Moment ($g$-$2$)

#### `b18_g2_berechnung.py`
Complete calculation of the anomalous magnetic moment for
electron, muon and tau in the FFGFT framework.
Uses the corrected prefactor $S_3 = 2\pi^2$ (Doc. 190, K3).

#### `b18_vollstaendige_herleitung.py`
Complete analytical derivation of the $g$-$2$ formula from
torus geometry. Shows all intermediate steps from $\xi$ to $a_e$.

---

### Koide Formula and Lepton Masses

#### `kodi.py` / `kodi-test.py`
Main implementation of the Koide relation $Q = 2/3$ in the FFGFT framework.
`kodi-test.py`: automated assertions on all three lepton masses.

#### `koide_korrekt.py`
Verifies the corrected prefactors ($r_\tau = 25/9$, Doc. 190 K2)
against PDG values 2022. Outputs the deviation for each lepton generation.

#### `koide_e0_test.py`
Tests the dependence of the Koide relation on the vacuum expectation value $E_0 = v$.
Sensitivity analysis: how does $Q$ change with small $\xi$ variations?

#### `koide_kfrak_test.py`
Investigates the influence of the fractal correction factor $K_\text{frak}$
on the Koide relation. Connects $g$-$2$ and Koide in one test.
Generates `koide_kfrak_test.png`.

#### `koide_test.py`
Quick test: Koide consistency for current PDG values.
Outputs $Q$, deviation from $2/3$ and significance in $\sigma$.

---

### Fine Structure Constant and $\alpha$ Derivation

#### `t0_alpha_pruefung.py`
Tests both FFGFT methods for deriving $\alpha$:
- Method 1 (geometric): $\alpha = \xi \cdot \varphi^3 \cdot 13$, $\alpha^{-1} \approx 136{.}19$
- Method 2 (T0 quantum numbers): $\alpha^{-1} \approx 141{.}44$

Contains automatic `assert` checks for both methods.
Reference: Doc. 133.

#### `higgs_pruefformel.py`
Tests the Higgs derivation of $\xi$ with the corrected prefactor
$16\pi^3$ (Doc. 190, K1). Compares $\xi_\text{Higgs}$ with $\xi_\text{T0} = 4/30000$.

---

### Quantum Computing and Shor's Algorithm

#### `t0_shor_complete.py`
Complete FFGFT implementation of Shor's algorithm.
Replaces the QFT with $\xi$-resonance search (Doc. 176).
Supports arbitrary $N$, BigInt-exact.
*Note: 0 % success rate is expected and theoretically justified (Doc. 183–184).*

#### `t0_shor_production.py`
Production version of the FFGFT-Shor algorithm.
Optimised for RSA-relevant $N$, with benchmarks against
classical trial division.

#### `bell_73qubit_FIXED.py`
Simulation of Bell states on 73-qubit systems with
FFGFT $\xi$-damping. Corrected version (FIXED) with
improved error handling for large registers.
Generates `bell_73qubit_fixed_analysis.png`.

---

### Geometry and Topology

#### `toroidal_vs_cylindrical_analysis.py`
Compares toroidal geometry (FFGFT) with cylindrical geometry
(Standard Model approximation) for qubit state spaces (Doc. 175).
Generates `toroidal_vs_cylindrical_analysis.png`.

#### `T3-experimet.py`
Numerical experiment on T3 symmetry in the FFGFT torus.
Tests whether the triple torus winding structure reproduces the
Z3 fixed points of Avi Rosenthal's geometry (Doc. 172).
Generates `t3_experiment_pruefung.png`.

---

### Baryon Asymmetry and Matter-Antimatter

#### `baron.py`
Calculates the baryon asymmetry $\eta = n_B/n_\gamma$ in the FFGFT framework.
Comparison with the Planck-CMB value $\eta \approx 6{.}10 \times 10^{-10}$.
Generates `baryon_asymmetrie_pruefung.png`.

---

### Derivations and Relations

#### `t0_herleitung-beziehungen.py`
Documents all derivation relationships between FFGFT quantities:
$\xi \to L_0 \to \ell_P \to \hbar \to \alpha \to m_e \to \ldots$
Contains automatic `assert` checks for the entire chain.

#### `messwert_analyse.py`
Statistical analysis of deviations between FFGFT predictions
and measured values. Calculates mean deviation, standard error
and significance for all 47 constants from `calc_De.py`.

#### `offene-fragen.py`
Lists open numerical questions of FFGFT and tests various
approaches: quark mass prefactors, higher orders in $K_\text{frak}$,
connection to the zeta function (Doc. 176).

---

### Collaboration

#### `avi.py`
Numerical verification of the three predictions from the Avi Rosenthal dialogue
(Doc. 172):
- CP phase: $\delta = 283{.}28°$ (dev. $0{.}18°$ from PDG value)
- $\sin^2\theta_W = 3/13 \approx 0{.}23077$ (dev. $0{.}195\,\%$)
- Baryon asymmetry: $\eta = 6{.}03 \times 10^{-10}$ (dev. $0{.}5\,\%$)

---

## Requirements

```bash
python --version   # Python 3.8 or newer
# Standard library only: math, fractions, datetime, json
```

No external packages required for core scripts.  
Exceptions:
- `t0_cosmic_data_analyzer.py`: requires `numpy`, `matplotlib`, `pandas`, `scipy`
- `t0_cosmic_qubit_simulator.py`: requires `ephem`

```bash
pip install numpy matplotlib pandas scipy ephem
```

---

## Generated Output Files

| Script | Output |
|--------|--------|
| `calc_De.py` | `T0_berechnungsdaten.txt`, `T0_berechnungen.json` |
| `T3-experimet.py` | `t3_experiment_pruefung.png` |
| `bell_73qubit_FIXED.py` | `bell_73qubit_fixed_analysis.png` |
| `baron.py` | `baryon_asymmetrie_pruefung.png` |
| `koide_kfrak_test.py` | `koide_kfrak_test.png` |
| `max-mass.py` | `max_masse_pruefung.png` |
| `toroidal_vs_cylindrical_analysis.py` | `toroidal_vs_cylindrical_analysis.png` |
| `t0_cosmic_data_analyzer.py` | `T0_analyse.png`, `cosmic_qubit_analysis.png` |
| `t0_cosmic_error_correction.py` | `cosmic_analysis_report_*.json` |

---

## Corrections vs. Older Versions

Documented in **Doc. 190** (corrections register):

| No. | Affects | Incorrect | Correct |
|-----|---------|-----------|---------|
| K1 | Doc. 049 | $\xi = \lambda_h^2 v^2 / (64\pi^4 m_h^2)$ | $\xi = \lambda_h^2 v^2 / (16\pi^3 m_h^2)$ |
| K2 | Doc. 116 | $r_\tau = 8/3$ | $r_\tau = 25/9$ |
| K3 | Doc. 018 | $a_e = 4\pi/(f \cdot k)$ | $a_e = 2\pi^2/(f \cdot k)$ |

---

## References

- **Doc. 006** — Particle masses: $r$- and $p$-table  
- **Doc. 018** — Anomalous magnetic moment ($g$-$2$)  
- **Doc. 049** — Lagrangian and Higgs integration  
- **Doc. 133** — Fine structure constant: two derivation methods  
- **Doc. 172** — Dialogue with Avi Rosenthal: CP phase, $\sin^2\theta_W$, baryon asymmetry  
- **Doc. 173–176** — Quantum dots, spin, qubit state spaces, Shor's algorithm  
- **Doc. 182** — Maximum universe scale and $t_0$  
- **Doc. 190** — Corrections register (binding)  

Complete documentation:  
[github.com/jpascher/T0-Time-Mass-Duality](https://github.com/jpascher/T0-Time-Mass-Duality)  
[zenodo.org/records/18834145](https://zenodo.org/records/18834145)
