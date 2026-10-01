#!/usr/bin/env python3
"""
T0-Model Casimir-CMB Verification Script (English Version)
==========================================================

This script recomputes the relationships between the Casimir effect and
cosmic microwave background radiation (CMB) in the T0-Model.

Author: Based on T0-Theory Documentation
Date: 2025-01-19
Filename: CMB_En.py
Updated on 1 Oct 2026: Casimir energy density π²ℏc/(720 d⁴) instead of π²ℏc/(240 d⁴)
  (240 is the Casimir pressure); ratio π²/(720ξ) ≈ 102.8 instead of 308.4; the former
  "experimental ratio" is the same formula with L_ξ taken from ρ_CMB (identity, not a
  measured value); accuracy figures removed; T_CMB/E_ξ = (16/9)ξ² marked as a
  unit-dependent agreement; checks (assert) for the identity and for 102.8 added
  (cf. Doc. 025/061, A260 and Doc. 190, R136, R137).

Classification: the Casimir-CMB connection is a scale statement [S], not evidence (R136).
The T_CMB relation agrees only in the energy unit eV; open (R137, R70).
Marker: [S] = scale statement/hypothesis, not to be counted as evidence.

T0-Theory: Time-Mass Duality Framework
Available at: https://github.com/jpascher/T0-Time-Mass-Duality
All T0 source documents and theory available on GitHub
"""

import math
import logging
from datetime import datetime
from typing import Dict, Tuple

# Casimir ENERGY DENSITY between ideal plates: π²ℏc/(720 d⁴).
# (π²ℏc/(240 d⁴) is the Casimir PRESSURE, not the energy density.)
CASIMIR_DENOMINATOR = 720

# === LOGGING CONFIGURATION ===
def setup_logging():
  """Configures logging for console and file output."""
  # Create log file
  log_filename = "t0_casimir_cmb_verification_En.log"

  # Configure logger
  logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(message)s',
    handlers=[
      logging.FileHandler(log_filename, encoding='utf-8'),
      logging.StreamHandler()
    ]
  )

  logger = logging.getLogger(__name__)
  logger.info("=" * 80)
  logger.info("T0-MODEL CASIMIR-CMB VERIFICATION SCRIPT")
  logger.info("=" * 80)
  logger.info(f"Log file: {log_filename}")
  logger.info("=" * 80)

  return logger

# === PHYSICAL CONSTANTS ===
class PhysicalConstants:
  """Collection of all physical constants with sources."""

  def __init__(self):
    # Fundamental constants (CODATA 2018)
    self.hbar = 1.054571817e-34 # J·s [CODATA]
    self.c = 2.99792458e8    # m/s [CODATA]
    self.k_B = 1.380649e-23   # J/K [CODATA]

    # Derived constants
    self.hbar_c = self.hbar * self.c # J·m

    # T0-Model parameters (from project documentation)
    self.xi = 4/3 * 1e-4 # dimensionless [T0-Doc]

    # CMB data (Planck 2018)
    self.rho_CMB_SI = 4.17e-14   # J/m³ [Planck]
    self.T_CMB_K = 2.7255     # K [Planck]

    # Mathematical constants
    self.pi = math.pi
    self.pi_squared = self.pi ** 2

  def log_constants(self, logger):
    """Logs all constants with sources."""
    logger.info("PHYSICAL CONSTANTS:")
    logger.info(f"ℏ = {self.hbar:.3e} J·s [CODATA 2018]")
    logger.info(f"c = {self.c:.3e} m/s [CODATA 2018]")
    logger.info(f"k_B = {self.k_B:.3e} J/K [CODATA 2018]")
    logger.info(f"ℏc = {self.hbar_c:.3e} J·m [calculated]")
    logger.info("")
    logger.info("T0-MODEL PARAMETERS:")
    logger.info(f"ξ = 4/3 × 10⁻⁴ = {self.xi:.6e} [T0-Doc]")
    logger.info("")
    logger.info("CMB DATA:")
    logger.info(f"ρ_CMB = {self.rho_CMB_SI:.2e} J/m³ [Planck 2018]")
    logger.info(f"T_CMB = {self.T_CMB_K} K [Planck 2018]")
    logger.info("")

class T0Calculator:
  """Main calculator for T0-Model computations."""

  def __init__(self, constants: PhysicalConstants, logger):
    self.const = constants
    self.logger = logger

  def calculate_characteristic_length(self) -> Tuple[float, Dict]:
    """Calculates the characteristic ξ length scale."""
    self.logger.info("=" * 60)
    self.logger.info("CALCULATION OF THE CHARACTERISTIC ξ LENGTH SCALE")
    self.logger.info("=" * 60)

    # From ρ_CMB = ξℏc/L_ξ⁴ follows L_ξ⁴ = ξℏc/ρ_CMB
    L_xi_fourth = (self.const.xi * self.const.hbar_c) / self.const.rho_CMB_SI
    L_xi = L_xi_fourth ** (1/4)

    self.logger.info("Basic equation (definition of L_ξ): ρ_CMB = ξℏc/L_ξ⁴")
    self.logger.info(f"L_ξ⁴ = ξℏc/ρ_CMB = {L_xi_fourth:.3e} m⁴")
    self.logger.info(f"L_ξ = (L_ξ⁴)^(1/4) = {L_xi:.3e} m")
    self.logger.info(f"L_ξ = {L_xi * 1e6:.1f} μm = {L_xi * 1e3:.3f} mm")
    self.logger.info("L_ξ is fixed by the measured CMB energy density and ξ.")

    results = {
      'L_xi_fourth': L_xi_fourth,
      'L_xi_meters': L_xi,
      'L_xi_micrometers': L_xi * 1e6,
      'L_xi_millimeters': L_xi * 1e3
    }

    return L_xi, results

  def calculate_casimir_density(self, distance: float) -> float:
    """Calculates the Casimir energy density at a given distance."""
    # Casimir energy density: |ρ_Casimir| = π²ℏc/(720d⁴)  (240 would be the pressure)
    rho_casimir = (self.const.pi_squared * self.const.hbar_c) / (CASIMIR_DENOMINATOR * distance**4)
    return rho_casimir

  def verify_casimir_cmb_ratio(self, L_xi: float) -> Dict:
    """Recomputes the Casimir-CMB ratio at d = L_ξ (identity)."""
    self.logger.info("")
    self.logger.info("=" * 60)
    self.logger.info("CASIMIR-CMB RATIO (IDENTITY VIA L_ξ)")
    self.logger.info("=" * 60)

    # Casimir energy density at d = L_ξ
    rho_casimir = self.calculate_casimir_density(L_xi)

    self.logger.info(f"Casimir energy density at d = L_ξ = {L_xi*1e6:.1f} μm:")
    self.logger.info(f"|ρ_Casimir| = π²ℏc/(720d⁴)")
    self.logger.info(f"|ρ_Casimir| = {self.const.pi_squared:.1f} × {self.const.hbar_c:.2e} / (720 × ({L_xi:.2e})⁴)")
    self.logger.info(f"|ρ_Casimir| = {rho_casimir:.3e} J/m³")

    # Ratio in SI with L_ξ from ρ_CMB
    ratio_SI = rho_casimir / self.const.rho_CMB_SI

    self.logger.info("")
    self.logger.info("RATIO IN SI (same formula with L_ξ from ρ_CMB, not a measured value):")
    self.logger.info(f"|ρ_Casimir|/ρ_CMB = {rho_casimir:.2e} / {self.const.rho_CMB_SI:.2e}")
    self.logger.info(f"|ρ_Casimir|/ρ_CMB = {ratio_SI:.1f}")

    # Closed form
    ratio_formula = self.const.pi_squared / (CASIMIR_DENOMINATOR * self.const.xi)
    ratio_alternative = (self.const.pi_squared * 1e4) / 960

    self.logger.info("")
    self.logger.info("CLOSED FORM:")
    self.logger.info(f"π²/(720ξ) = {self.const.pi_squared:.1f} / (720 × {self.const.xi:.2e})")
    self.logger.info(f"π²/(720ξ) = {ratio_formula:.1f}")
    self.logger.info(f"Alternative form: π²×10⁴/960 = {ratio_alternative:.1f}")

    # Identity check: inserting ρ_CMB = ξℏc/L_ξ⁴ gives π²/(720ξ) for every L_ξ
    relative_diff = abs(ratio_SI - ratio_formula) / ratio_formula
    assert relative_diff < 1e-9, "Identity violated -- programming error"
    assert abs(ratio_formula - 102.8) < 0.05, "π²/(720ξ) ≠ 102.8"

    self.logger.info("")
    self.logger.info("CLASSIFICATION:")
    self.logger.info(f"SI value and closed form agree (rel. difference {relative_diff:.1e}),")
    self.logger.info("because L_ξ itself is fixed by ρ_CMB and ξ -- this is an identity,")
    self.logger.info("not a comparison with a measurement (R136). Scale statement [S], not evidence.")
    self.logger.info("[OK] Identity ρ_Casimir/ρ_CMB = π²/(720ξ) ≈ 102.8 recomputed")

    return {
      'rho_casimir': rho_casimir,
      'ratio_SI': ratio_SI,
      'ratio_formula': ratio_formula,
      'ratio_alternative': ratio_alternative,
      'relative_difference': relative_diff,
      'status': 'identity via L_xi, scale statement [S] (R136)'
    }

  def verify_modified_casimir_formula(self, L_xi: float) -> Dict:
    """Shows that the 'modified' Casimir formula is the standard formula rewritten."""
    self.logger.info("")
    self.logger.info("=" * 60)
    self.logger.info("REWRITTEN CASIMIR FORMULA (IDENTITY)")
    self.logger.info("=" * 60)

    self.logger.info("Rewritten form:")
    self.logger.info("|ρ_Casimir| = (π²/720ξ) × ρ_CMB × (L_ξ/d)⁴")
    self.logger.info("At d = L_ξ, (L_ξ/d)⁴ = 1")
    self.logger.info("Thus: |ρ_Casimir| = (π²/720ξ) × ρ_CMB")

    # Calculation with rewritten formula
    rho_casimir_modified = (self.const.pi_squared / (CASIMIR_DENOMINATOR * self.const.xi)) * self.const.rho_CMB_SI

    # Calculation with standard formula
    rho_casimir_standard = self.calculate_casimir_density(L_xi)

    self.logger.info("")
    self.logger.info("FORMULA COMPARISON:")
    self.logger.info(f"Rewritten formula: {rho_casimir_modified:.3e} J/m³")
    self.logger.info(f"Standard formula:  {rho_casimir_standard:.3e} J/m³")

    difference = abs(rho_casimir_modified - rho_casimir_standard)
    relative_diff = (difference / rho_casimir_standard) * 100
    assert relative_diff < 1e-7, "Rewriting inconsistent -- programming error"

    self.logger.info(f"Absolute difference: {difference:.2e} J/m³")
    self.logger.info(f"Relative difference: {relative_diff:.6f}%")

    self.logger.info("")
    self.logger.info("REWRITING:")
    self.logger.info("Inserting ρ_CMB = ξ/L_ξ⁴ into the rewritten formula:")
    self.logger.info("|ρ_Casimir| = (π²/720ξ) × (ξ/L_ξ⁴) × (L_ξ/d)⁴")
    self.logger.info("      = (π²/720) × (1/L_ξ⁴) × (L_ξ⁴/d⁴)")
    self.logger.info("      = π²/(720d⁴)")
    self.logger.info("This is the standard formula, merely rewritten -- equal by the definition")
    self.logger.info("of L_ξ, not an independent test (R136).")

    return {
      'rho_casimir_modified': rho_casimir_modified,
      'rho_casimir_standard': rho_casimir_standard,
      'difference': difference,
      'relative_difference': relative_diff
    }

  def analyze_scaling_behavior(self, L_xi: float) -> Dict:
    """Analyzes the scaling behavior at different distances."""
    self.logger.info("")
    self.logger.info("=" * 60)
    self.logger.info("SCALING BEHAVIOR AT DIFFERENT DISTANCES")
    self.logger.info("=" * 60)

    # Test distances
    test_distances = [1e-3, 1e-4, 1e-5, 1e-6, 1e-7] # 1mm, 100μm, 10μm, 1μm, 100nm

    results = {}

    self.logger.info("Distance  | Casimir density  | Ratio to CMB")
    self.logger.info("-" * 55)

    for d in test_distances:
      rho_cas = self.calculate_casimir_density(d)
      ratio_to_cmb = rho_cas / self.const.rho_CMB_SI

      # Unit formatting
      if d >= 1e-6:
        d_str = f"{d*1e6:.0f}μm"
      else:
        d_str = f"{d*1e9:.0f}nm"

      self.logger.info(f"{d_str:8} | {rho_cas:.1e} J/m³ | {ratio_to_cmb:.1e}")

      results[d] = {
        'distance_str': d_str,
        'rho_casimir': rho_cas,
        'ratio_to_cmb': ratio_to_cmb
      }

    # Distance at which both energy densities are equal
    d_equal = L_xi * (self.const.pi_squared / (CASIMIR_DENOMINATOR * self.const.xi)) ** 0.25
    self.logger.info("")
    self.logger.info(f"At L_ξ = {L_xi*1e6:.0f}μm the ratio is ≈ 103; the densities do NOT")
    self.logger.info(f"coincide there; equality lies at d = {d_equal*1e6:.0f} μm (R136).")
    results['d_equal_m'] = d_equal

    return results

  def verify_cmb_temperature_prediction(self) -> Dict:
    """Recomputes the T0 T_CMB relation (unit-dependent, R137)."""
    self.logger.info("")
    self.logger.info("=" * 60)
    self.logger.info("CMB TEMPERATURE RELATION (UNIT-DEPENDENT AGREEMENT)")
    self.logger.info("=" * 60)

    # T0 relation: T_CMB/E_ξ = (16/9) × ξ²
    E_xi = 1 / self.const.xi # characteristic ξ energy (pure number)

    # CMB temperature in eV (k_B × 2.7255 K)
    T_CMB_natural = 2.35e-4 # [T0-Doc], eV

    # Ratio with T_CMB in eV
    ratio_observed = T_CMB_natural / E_xi

    # Relation
    ratio_relation = (16/9) * self.const.xi**2

    # Same calculation with T_CMB in kelvin
    ratio_in_K = self.const.T_CMB_K / E_xi

    self.logger.info("T0-Model CMB temperature relation:")
    self.logger.info(f"E_ξ = 1/ξ = {E_xi:.0f} (pure number)")
    self.logger.info(f"T_CMB = {T_CMB_natural:.2e} eV [T0-Doc]")
    self.logger.info("")
    self.logger.info("RATIO COMPARISON:")
    self.logger.info(f"T_CMB/E_ξ with T_CMB in eV: {ratio_observed:.3e}")
    self.logger.info(f"(16/9) × ξ²:                {ratio_relation:.3e}")
    self.logger.info(f"T_CMB/E_ξ with T_CMB in K:  {ratio_in_K:.3e}")

    deviation_temp = abs(ratio_observed - ratio_relation)
    relative_error_temp = (deviation_temp / ratio_relation) * 100

    self.logger.info(f"Deviation (eV reading): {relative_error_temp:.1f}%")
    self.logger.info("")
    self.logger.info("CLASSIFICATION: the relation yields a pure number that matches the")
    self.logger.info("measured value only in the energy unit eV (in K it is off by a factor")
    self.logger.info(f"{ratio_in_K/ratio_relation:.1e}). Unit-dependent agreement, not a derivation;")
    self.logger.info("the question is open (R137, R70) [S].")

    return {
      'E_xi': E_xi,
      'T_CMB_natural': T_CMB_natural,
      'ratio_observed': ratio_observed,
      'ratio_relation': ratio_relation,
      'ratio_in_K': ratio_in_K,
      'deviation': deviation_temp,
      'relative_error_eV': relative_error_temp,
      'status': 'unit-dependent agreement, open (R137, R70)'
    }

  def generate_summary(self, all_results: Dict):
    """Generates a summary of all calculations."""
    self.logger.info("")
    self.logger.info("=" * 80)
    self.logger.info("SUMMARY")
    self.logger.info("=" * 80)

    self.logger.info("CORE RESULTS:")
    self.logger.info("")

    # Characteristic length scale
    L_xi = all_results['length']['L_xi_micrometers']
    self.logger.info(f"1. Characteristic ξ length scale: L_ξ = {L_xi:.1f} μm (from ρ_CMB and ξ)")

    # Casimir-CMB ratio
    ratio = all_results['casimir_ratio']['ratio_formula']
    self.logger.info(f"2. Casimir-CMB ratio π²/(720ξ) = {ratio:.1f} -- identity via L_ξ (R136)")

    # CMB temperature
    rel = all_results['temperature']['relative_error_eV']
    self.logger.info(f"3. T_CMB/E_ξ = (16/9)ξ²: {rel:.1f} % only in eV -- unit-dependent, open (R137)")

    # Formula rewriting
    self.logger.info("4. Rewritten Casimir formula = standard formula (rewriting, not a test)")

    self.logger.info("")
    self.logger.info("CLASSIFICATION:")
    self.logger.info("• Casimir-CMB connection: scale statement [S], not evidence (R136)")
    self.logger.info("• T_CMB from ξ: unit-dependent agreement, open (R137, R70)")
    self.logger.info("• Open: whether L_ξ has its own physical Casimir signature (R136)")

    # Sources
    self.logger.info("")
    self.logger.info("SOURCES USED:")
    self.logger.info("• CODATA: Committee on Data for Science and Technology 2018")
    self.logger.info("• Planck: Planck Collaboration 2018 (CMB data)")
    self.logger.info("• T0-Doc: T0-Theory project documentation")
    self.logger.info("• GitHub: https://github.com/jpascher/T0-Time-Mass-Duality")
    self.logger.info(" (All T0 source documents and theory available)")

  def _scaling_rows(self, all_results: Dict):
    """Rows of the scaling table (distance, ratio) from the computed values."""
    rows = []
    for d, v in all_results['scaling'].items():
      if isinstance(v, dict):
        rows.append((v['distance_str'], v['ratio_to_cmb']))
    return rows

  def generate_markdown_report(self, all_results: Dict) -> str:
    """Generates a formatted Markdown report."""
    L_xi = all_results['length']['L_xi_micrometers']
    cr = all_results['casimir_ratio']
    tp = all_results['temperature']
    d_eq = all_results['scaling']['d_equal_m'] * 1e6
    scaling_md = "\n".join(f"{s:>8} | {r:.1e}" for s, r in self._scaling_rows(all_results))

    markdown = f"""# T0-Model Casimir-CMB Recalculation

**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Status:** corrected 1 Oct 2026 (Doc. 025/061, A260; Doc. 190, R136, R137)

---

## Summary

The T0-Model connects the Casimir effect and the CMB through the length scale L_ξ. The recalculation shows: the ratio of the energy densities at L_ξ is an identity, because L_ξ itself is fixed by the measured CMB energy density and ξ. The connection is a scale statement [S], not evidence (R136). The T_CMB relation agrees only in eV; unit-dependent, open (R137).

### Core results

| **Calculation** | **Result** | **Classification** |
|-----------------|------------|--------------------|
| Characteristic ξ length scale | L_ξ = {L_xi:.1f} μm | from ρ_CMB and ξ |
| Casimir-CMB ratio | π²/(720ξ) = {cr['ratio_formula']:.1f} | identity [S] (R136) |
| CMB temperature relation | {tp['ratio_observed']:.2e} (eV) | unit-dependent, open (R137) |
| Rewritten Casimir formula | = standard formula | rewriting, not a test |

---

## Calculations

### 1. Characteristic ξ length scale

```
L_ξ = (ξℏc/ρ_CMB)^(1/4) = {L_xi:.1f} μm
```

L_ξ is defined through the measured CMB energy density.

### 2. Casimir-CMB ratio

Casimir energy density π²ℏc/(720 d⁴) (π²ℏc/(240 d⁴) is the pressure):

| **Parameter** | **Value** | **Unit** |
|---------------|-----------|----------|
| Casimir energy density at L_ξ | {cr['rho_casimir']:.2e} | J/m³ |
| CMB energy density | {self.const.rho_CMB_SI:.2e} | J/m³ |
| Ratio in SI (L_ξ from ρ_CMB) | {cr['ratio_SI']:.1f} | - |
| Closed form π²/(720ξ) | {cr['ratio_formula']:.1f} | - |

Both values are the same formula; their equality follows from the definition of L_ξ and is not a comparison with a measurement.

### 3. Scaling behavior

```
Distance | Casimir/CMB ratio
---------|------------------
{scaling_md}
```

At L_ξ the two densities do not coincide (ratio ≈ 103); equality lies at d ≈ {d_eq:.0f} μm.

### 4. CMB temperature relation

**Relation:** T_CMB/E_ξ = (16/9) × ξ²

| **Parameter** | **Value** |
|---------------|-----------|
| T_CMB/E_ξ (T_CMB in eV) | {tp['ratio_observed']:.3e} |
| (16/9) × ξ² | {tp['ratio_relation']:.3e} |
| T_CMB/E_ξ (T_CMB in K) | {tp['ratio_in_K']:.3e} |

The agreement holds only in the energy unit eV; it is unit-dependent and not a derivation (R137, R70).

---

## Classification

- Casimir-CMB connection: scale statement [S], not evidence (R136)
- T_CMB from ξ: unit-dependent agreement, open (R137, R70)
- Open: whether L_ξ has its own physical Casimir signature (R136)

[S] = scale statement/hypothesis, not to be counted as evidence.

---

## References

| **Abbreviation** | **Full source** |
|------------------|-----------------|
| **CODATA** | Committee on Data for Science and Technology 2018 Values |
| **Planck** | Planck Collaboration 2018 Results (CMB parameters) |
| **T0-Doc** | T0-Theory project documentation (ξ parameter) |

---

*Generated on {datetime.now().strftime('%Y-%m-%d')} by CMB_En.py*
"""
    return markdown

  def generate_latex_report(self, all_results: Dict) -> str:
    """Generates a formatted LaTeX report."""
    L_xi = all_results['length']['L_xi_micrometers']
    cr = all_results['casimir_ratio']
    tp = all_results['temperature']
    d_eq = all_results['scaling']['d_equal_m'] * 1e6
    def _tex_num(x):
      m, e = f"{x:.1e}".split('e')
      return f"${m} \\times 10^{{{int(e)}}}$"
    scaling_tex = "\n".join(
      s.replace('μm', r'\,$\mu$m').replace('nm', r'\,nm') + " & " + _tex_num(r) + r" \\"
      for s, r in self._scaling_rows(all_results))

    latex = r"""
\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[english]{babel}
\usepackage{amsmath,amssymb}
\usepackage{booktabs}
\usepackage{geometry}
\geometry{margin=2.5cm}

\title{T0-Model Casimir-CMB Recalculation}
\author{Automatically generated (CMB\_En.py)}
\date{""" + f"{datetime.now().strftime('%Y-%m-%d')}" + r"""}

\begin{document}
\maketitle

\begin{abstract}
The ratio of Casimir to CMB energy density at $L_\xi$ is an identity, because $L_\xi$ is fixed by the measured CMB energy density and $\xi$: $\pi^2/(720\xi) \approx """ + f"{cr['ratio_formula']:.1f}" + r"""$. The connection is a scale statement [S], not evidence (Doc.~190, R136). The relation $T_{\text{CMB}}/E_\xi = (16/9)\xi^2$ agrees only in eV; unit-dependent, open (R137). [S] = scale statement/hypothesis.
\end{abstract}

\section{Characteristic $\xi$ length scale}
\begin{equation}
L_\xi = \left(\frac{\xi \hbar c}{\rho_{\text{CMB}}}\right)^{1/4} = """ + f"{L_xi:.1f}" + r"""\,\mu\text{m}
\end{equation}

\section{Casimir-CMB ratio}
Energy density (not pressure):
\begin{align}
\left|\rho_{\text{Casimir}}\right| &= \frac{\pi^2 \hbar c}{720 d^4} = """ + f"{cr['rho_casimir']:.2e}" + r"""\,\text{J/m}^3 \\
\rho_{\text{CMB}} &= """ + f"{self.const.rho_CMB_SI:.2e}" + r"""\,\text{J/m}^3 \\
\frac{\left|\rho_{\text{Casimir}}\right|}{\rho_{\text{CMB}}} &= \frac{\pi^2}{720\xi} = \frac{\pi^2 \times 10^4}{960} \approx """ + f"{cr['ratio_formula']:.1f}" + r"""
\end{align}
The SI value is the same formula with $L_\xi$ taken from $\rho_{\text{CMB}}$ (identity, not a measured value).

\section{Scaling behavior}
\begin{table}[h]
\centering
\begin{tabular}{cc}
\toprule
\textbf{Distance} & \textbf{Casimir/CMB ratio} \\
\midrule
""" + scaling_tex + r"""
\bottomrule
\end{tabular}
\end{table}
At $L_\xi$ the two densities do not coincide; equality at $d \approx """ + f"{d_eq:.0f}" + r"""\,\mu$m.

\section{CMB temperature relation}
\begin{table}[h]
\centering
\begin{tabular}{cc}
\toprule
\textbf{Quantity} & \textbf{Value} \\
\midrule
$T_{\text{CMB}}/E_\xi$ ($T$ in eV) & $""" + f"{tp['ratio_observed']:.3e}" + r"""$ \\
$(16/9)\xi^2$ & $""" + f"{tp['ratio_relation']:.3e}" + r"""$ \\
$T_{\text{CMB}}/E_\xi$ ($T$ in K) & $""" + f"{tp['ratio_in_K']:.3e}" + r"""$ \\
\bottomrule
\end{tabular}
\end{table}
Unit-dependent agreement, not a derivation; open (R137, R70).

\section{Classification}
\begin{itemize}
\item Casimir-CMB connection: scale statement [S], not evidence (R136)
\item $T_{\text{CMB}}$ from $\xi$: unit-dependent, open (R137, R70)
\item Open: own physical Casimir signature of $L_\xi$ (R136)
\end{itemize}

\section{References}
\begin{itemize}
\item \textbf{CODATA:} Committee on Data for Science and Technology 2018 Values
\item \textbf{Planck:} Planck Collaboration 2018 Results (CMB parameters)
\item \textbf{T0-Doc:} T0-Theory project documentation ($\xi$ parameter)
\item \textbf{GitHub:} \texttt{https://github.com/jpascher/T0-Time-Mass-Duality}
\end{itemize}

\end{document}
"""
    return latex

def main():
  """Main function of the script."""

  # Logging setup
  logger = setup_logging()

  try:
    # Initialize constants
    constants = PhysicalConstants()
    constants.log_constants(logger)

    # Initialize calculator
    calc = T0Calculator(constants, logger)

    # Perform all calculations
    all_results = {}

    # 1. Characteristic length scale
    L_xi, length_results = calc.calculate_characteristic_length()
    all_results['length'] = length_results

    # 2. Casimir-CMB ratio (identity)
    casimir_results = calc.verify_casimir_cmb_ratio(L_xi)
    all_results['casimir_ratio'] = casimir_results

    # 3. Rewritten Casimir formula
    formula_results = calc.verify_modified_casimir_formula(L_xi)
    all_results['modified_formula'] = formula_results

    # 4. Scaling behavior
    scaling_results = calc.analyze_scaling_behavior(L_xi)
    all_results['scaling'] = scaling_results

    # 5. CMB temperature relation
    temp_results = calc.verify_cmb_temperature_prediction()
    all_results['temperature'] = temp_results

    # 6. Summary
    calc.generate_summary(all_results)

    # 7. Generate reports
    logger.info("")
    logger.info("=" * 60)
    logger.info("GENERATING REPORTS")
    logger.info("=" * 60)

    # Markdown report
    markdown_report = calc.generate_markdown_report(all_results)
    markdown_filename = "t0_casimir_cmb_report_En.md"
    with open(markdown_filename, 'w', encoding='utf-8') as f:
      f.write(markdown_report)
    logger.info(f"✓ Markdown report created: {markdown_filename}")

    # LaTeX report
    latex_report = calc.generate_latex_report(all_results)
    latex_filename = "t0_casimir_cmb_report_En.tex"
    with open(latex_filename, 'w', encoding='utf-8') as f:
      f.write(latex_report)
    logger.info(f"✓ LaTeX report created: {latex_filename}")

    # JSON export for further processing
    import json
    json_filename = "t0_casimir_cmb_data_En.json"
    with open(json_filename, 'w', encoding='utf-8') as f:
      json.dump(all_results, f, indent=2, ensure_ascii=False, default=str)
    logger.info(f"✓ JSON data exported: {json_filename}")

    logger.info("")
    logger.info("=" * 80)
    logger.info("RECALCULATION COMPLETED -- all checks passed")
    logger.info("=" * 80)
    logger.info("Generated files:")
    logger.info(f"• Log file: {logging.getLogger().handlers[0].baseFilename}")
    logger.info(f"• Markdown report: {markdown_filename}")
    logger.info(f"• LaTeX report: {latex_filename}")
    logger.info(f"• JSON data: {json_filename}")
    logger.info("")
    logger.info("T0-Theory: Time-Mass Duality Framework")
    logger.info("GitHub: https://github.com/jpascher/T0-Time-Mass-Duality")
    logger.info("All T0 source documents and theory available")

    return all_results

  except Exception as e:
    logger.error(f"Error during verification: {e}")
    raise

if __name__ == "__main__":
  results = main()
  print("\nScript executed successfully. See log file for details.")
