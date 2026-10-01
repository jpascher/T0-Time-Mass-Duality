#!/usr/bin/env python3
"""
T0-Modell Casimir-CMB Verifikations-Skript (Deutsche Version)
============================================================

Dieses Skript rechnet die Zusammenhänge zwischen Casimir-Effekt und
kosmischer Mikrowellen-Hintergrundstrahlung (CMB) im T0-Modell nach.

Autor: Basierend auf T0-Theorie Dokumentation
Datum: 2025-01-19
Dateiname: t0_casimir_cmb_verifikation.py
Aktualisiert am 1.10.2026: Casimir-Energiedichte π²ℏc/(720 d⁴) statt π²ℏc/(240 d⁴)
  (240 ist der Casimir-Druck); Verhältnis π²/(720ξ) ≈ 102,8 statt 308,4; das frühere
  "experimentelle Verhältnis" ist dieselbe Formel mit L_ξ aus ρ_CMB (Identität, kein
  Messwert); Genauigkeitsangaben entfernt; T_CMB/E_ξ = (16/9)ξ² als einheitenabhängige
  Übereinstimmung gekennzeichnet; Prüfungen (assert) für Identität und 102,8 ergänzt
  (vgl. Dok. 025/061, A260 bzw. Dok. 190, R136, R137).

Einstufung: Die Casimir-CMB-Verbindung ist eine Skalenaussage [S], kein Beleg (R136).
Die T_CMB-Relation stimmt nur in der Energieeinheit eV, offen (R137, R70).
Marker: [S] = Skalenaussage/Hypothese, nicht als Beleg zu werten.

T0-Theorie: Zeit-Masse-Dualitäts-Framework
Verfügbar unter: https://github.com/jpascher/T0-Time-Mass-Duality
Alle T0-Quelldokumente und Theorie auf GitHub verfügbar
"""

import math
import logging
from datetime import datetime
from typing import Dict, Tuple

# Casimir-ENERGIEDICHTE zwischen idealen Platten: π²ℏc/(720 d⁴).
# (π²ℏc/(240 d⁴) ist der Casimir-DRUCK, nicht die Energiedichte.)
CASIMIR_NENNER = 720

# === KONFIGURATION DES LOGGINGS ===
def setup_logging():
  """Konfiguriert das Logging für Konsole und Datei."""
  # Log-Datei erstellen
  log_filename = f"t0_casimir_cmb_verifikation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

  # Logger konfigurieren
  logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
      logging.FileHandler(log_filename, encoding='utf-8'),
      logging.StreamHandler()
    ]
  )

  logger = logging.getLogger(__name__)
  logger.info("=" * 80)
  logger.info("T0-MODELL CASIMIR-CMB VERIFIKATIONS-SKRIPT")
  logger.info("=" * 80)
  logger.info(f"Log-Datei: {log_filename}")
  logger.info("=" * 80)

  return logger

# === PHYSIKALISCHE KONSTANTEN ===
class PhysicalConstants:
  """Sammlung aller physikalischen Konstanten mit Quellen."""

  def __init__(self):
    # Fundamentale Konstanten (CODATA 2018)
    self.hbar = 1.054571817e-34 # J·s [CODATA]
    self.c = 2.99792458e8    # m/s [CODATA]
    self.k_B = 1.380649e-23   # J/K [CODATA]

    # Abgeleitete Konstanten
    self.hbar_c = self.hbar * self.c # J·m

    # T0-Modell Parameter (aus Projektdokumentation)
    self.xi = 4/3 * 1e-4 # dimensionslos [T0-Dok]

    # CMB-Daten (Planck 2018)
    self.rho_CMB_SI = 4.17e-14   # J/m³ [Planck]
    self.T_CMB_K = 2.7255     # K [Planck]

    # Mathematische Konstanten
    self.pi = math.pi
    self.pi_squared = self.pi ** 2

  def log_constants(self, logger):
    """Loggt alle Konstanten mit Quellen."""
    logger.info("PHYSIKALISCHE KONSTANTEN:")
    logger.info(f"ℏ = {self.hbar:.3e} J·s [CODATA 2018]")
    logger.info(f"c = {self.c:.3e} m/s [CODATA 2018]")
    logger.info(f"k_B = {self.k_B:.3e} J/K [CODATA 2018]")
    logger.info(f"ℏc = {self.hbar_c:.3e} J·m [berechnet]")
    logger.info("")
    logger.info("T0-MODELL PARAMETER:")
    logger.info(f"ξ = 4/3 × 10⁻⁴ = {self.xi:.6e} [T0-Dok]")
    logger.info("")
    logger.info("CMB-DATEN:")
    logger.info(f"ρ_CMB = {self.rho_CMB_SI:.2e} J/m³ [Planck 2018]")
    logger.info(f"T_CMB = {self.T_CMB_K} K [Planck 2018]")
    logger.info("")

class T0Calculator:
  """Hauptrechner für T0-Modell Berechnungen."""

  def __init__(self, constants: PhysicalConstants, logger):
    self.const = constants
    self.logger = logger

  def calculate_characteristic_length(self) -> Tuple[float, Dict]:
    """Berechnet die charakteristische ξ-Längenskala."""
    self.logger.info("=" * 60)
    self.logger.info("BERECHNUNG DER CHARAKTERISTISCHEN ξ-LÄNGENSKALA")
    self.logger.info("=" * 60)

    # Aus ρ_CMB = ξℏc/L_ξ⁴ folgt L_ξ⁴ = ξℏc/ρ_CMB
    L_xi_fourth = (self.const.xi * self.const.hbar_c) / self.const.rho_CMB_SI
    L_xi = L_xi_fourth ** (1/4)

    self.logger.info("Grundgleichung (Definition von L_ξ): ρ_CMB = ξℏc/L_ξ⁴")
    self.logger.info(f"L_ξ⁴ = ξℏc/ρ_CMB = {L_xi_fourth:.3e} m⁴")
    self.logger.info(f"L_ξ = (L_ξ⁴)^(1/4) = {L_xi:.3e} m")
    self.logger.info(f"L_ξ = {L_xi * 1e6:.1f} μm = {L_xi * 1e3:.3f} mm")
    self.logger.info("L_ξ ist aus der gemessenen CMB-Energiedichte und ξ bestimmt.")

    results = {
      'L_xi_fourth': L_xi_fourth,
      'L_xi_meters': L_xi,
      'L_xi_micrometers': L_xi * 1e6,
      'L_xi_millimeters': L_xi * 1e3
    }

    return L_xi, results

  def calculate_casimir_density(self, distance: float) -> float:
    """Berechnet Casimir-Energiedichte bei gegebenem Abstand."""
    # Casimir-Energiedichte: |ρ_Casimir| = π²ℏc/(720d⁴)  (240 wäre der Druck)
    rho_casimir = (self.const.pi_squared * self.const.hbar_c) / (CASIMIR_NENNER * distance**4)
    return rho_casimir

  def verify_casimir_cmb_ratio(self, L_xi: float) -> Dict:
    """Rechnet das Casimir-CMB-Verhältnis bei d = L_ξ nach (Identität)."""
    self.logger.info("")
    self.logger.info("=" * 60)
    self.logger.info("CASIMIR-CMB-VERHÄLTNIS (IDENTITÄT ÜBER L_ξ)")
    self.logger.info("=" * 60)

    # Casimir-Energiedichte bei d = L_ξ
    rho_casimir = self.calculate_casimir_density(L_xi)

    self.logger.info(f"Casimir-Energiedichte bei d = L_ξ = {L_xi*1e6:.1f} μm:")
    self.logger.info(f"|ρ_Casimir| = π²ℏc/(720d⁴)")
    self.logger.info(f"|ρ_Casimir| = {self.const.pi_squared:.1f} × {self.const.hbar_c:.2e} / (720 × ({L_xi:.2e})⁴)")
    self.logger.info(f"|ρ_Casimir| = {rho_casimir:.3e} J/m³")

    # Verhältnis in SI mit L_ξ aus ρ_CMB
    ratio_SI = rho_casimir / self.const.rho_CMB_SI

    self.logger.info("")
    self.logger.info("VERHÄLTNIS IN SI (dieselbe Formel mit L_ξ aus ρ_CMB, kein Messwert):")
    self.logger.info(f"|ρ_Casimir|/ρ_CMB = {rho_casimir:.2e} / {self.const.rho_CMB_SI:.2e}")
    self.logger.info(f"|ρ_Casimir|/ρ_CMB = {ratio_SI:.1f}")

    # Geschlossene Form
    ratio_formula = self.const.pi_squared / (CASIMIR_NENNER * self.const.xi)
    ratio_alternative = (self.const.pi_squared * 1e4) / 960

    self.logger.info("")
    self.logger.info("GESCHLOSSENE FORM:")
    self.logger.info(f"π²/(720ξ) = {self.const.pi_squared:.1f} / (720 × {self.const.xi:.2e})")
    self.logger.info(f"π²/(720ξ) = {ratio_formula:.1f}")
    self.logger.info(f"Alternative Form: π²×10⁴/960 = {ratio_alternative:.1f}")

    # Identitätsprüfung: Einsetzen von ρ_CMB = ξℏc/L_ξ⁴ ergibt π²/(720ξ) für jedes L_ξ
    relative_diff = abs(ratio_SI - ratio_formula) / ratio_formula
    assert relative_diff < 1e-9, "Identität verletzt -- Programmierfehler"
    assert abs(ratio_formula - 102.8) < 0.05, "π²/(720ξ) ≠ 102,8"

    self.logger.info("")
    self.logger.info("EINORDNUNG:")
    self.logger.info(f"SI-Wert und geschlossene Form stimmen überein (rel. Differenz {relative_diff:.1e}),")
    self.logger.info("weil L_ξ selbst aus ρ_CMB und ξ bestimmt ist -- das ist eine Identität,")
    self.logger.info("kein Vergleich mit einer Messung (R136). Skalenaussage [S], kein Beleg.")
    self.logger.info("[OK] Identität ρ_Casimir/ρ_CMB = π²/(720ξ) ≈ 102,8 nachgerechnet")

    return {
      'rho_casimir': rho_casimir,
      'ratio_SI': ratio_SI,
      'ratio_formula': ratio_formula,
      'ratio_alternative': ratio_alternative,
      'relative_difference': relative_diff,
      'status': 'Identitaet ueber L_xi, Skalenaussage [S] (R136)'
    }

  def verify_modified_casimir_formula(self, L_xi: float) -> Dict:
    """Zeigt, dass die 'modifizierte' Casimir-Formel die Standardformel umgeschrieben ist."""
    self.logger.info("")
    self.logger.info("=" * 60)
    self.logger.info("UMGESCHRIEBENE CASIMIR-FORMEL (IDENTITÄT)")
    self.logger.info("=" * 60)

    self.logger.info("Umgeschriebene Form:")
    self.logger.info("|ρ_Casimir| = (π²/720ξ) × ρ_CMB × (L_ξ/d)⁴")
    self.logger.info("Bei d = L_ξ wird (L_ξ/d)⁴ = 1")
    self.logger.info("Also: |ρ_Casimir| = (π²/720ξ) × ρ_CMB")

    # Berechnung mit umgeschriebener Formel
    rho_casimir_modified = (self.const.pi_squared / (CASIMIR_NENNER * self.const.xi)) * self.const.rho_CMB_SI

    # Berechnung mit Standard-Formel
    rho_casimir_standard = self.calculate_casimir_density(L_xi)

    self.logger.info("")
    self.logger.info("VERGLEICH DER FORMELN:")
    self.logger.info(f"Umgeschriebene Formel: {rho_casimir_modified:.3e} J/m³")
    self.logger.info(f"Standard-Formel:    {rho_casimir_standard:.3e} J/m³")

    difference = abs(rho_casimir_modified - rho_casimir_standard)
    relative_diff = (difference / rho_casimir_standard) * 100
    assert relative_diff < 1e-7, "Umformung inkonsistent -- Programmierfehler"

    self.logger.info(f"Absolute Differenz: {difference:.2e} J/m³")
    self.logger.info(f"Relative Differenz: {relative_diff:.6f}%")

    self.logger.info("")
    self.logger.info("UMFORMUNG:")
    self.logger.info("Einsetzen von ρ_CMB = ξ/L_ξ⁴ in die umgeschriebene Formel:")
    self.logger.info("|ρ_Casimir| = (π²/720ξ) × (ξ/L_ξ⁴) × (L_ξ/d)⁴")
    self.logger.info("      = (π²/720) × (1/L_ξ⁴) × (L_ξ⁴/d⁴)")
    self.logger.info("      = π²/(720d⁴)")
    self.logger.info("Das ist die Standardformel, nur umgeschrieben -- per Definition von L_ξ")
    self.logger.info("gleich, kein unabhängiger Test (R136).")

    return {
      'rho_casimir_modified': rho_casimir_modified,
      'rho_casimir_standard': rho_casimir_standard,
      'difference': difference,
      'relative_difference': relative_diff
    }

  def analyze_scaling_behavior(self, L_xi: float) -> Dict:
    """Analysiert das Skalierungsverhalten bei verschiedenen Abständen."""
    self.logger.info("")
    self.logger.info("=" * 60)
    self.logger.info("SKALIERUNGSVERHALTEN BEI VERSCHIEDENEN ABSTÄNDEN")
    self.logger.info("=" * 60)

    # Test-Abstände
    test_distances = [1e-3, 1e-4, 1e-5, 1e-6, 1e-7] # 1mm, 100μm, 10μm, 1μm, 100nm

    results = {}

    self.logger.info("Abstand   | Casimir-Dichte   | Verhältnis zu CMB")
    self.logger.info("-" * 55)

    for d in test_distances:
      rho_cas = self.calculate_casimir_density(d)
      ratio_to_cmb = rho_cas / self.const.rho_CMB_SI

      # Formatierung der Einheiten
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

    # Abstand, bei dem beide Energiedichten gleich sind
    d_equal = L_xi * (self.const.pi_squared / (CASIMIR_NENNER * self.const.xi)) ** 0.25
    self.logger.info("")
    self.logger.info(f"Bei L_ξ = {L_xi*1e6:.0f}μm ist das Verhältnis ≈ 103, die Dichten fallen")
    self.logger.info(f"dort NICHT zusammen; Gleichheit liegt bei d = {d_equal*1e6:.0f} μm (R136).")
    results['d_equal_m'] = d_equal

    return results

  def verify_cmb_temperature_prediction(self) -> Dict:
    """Rechnet die T_CMB-Relation des T0-Modells nach (einheitenabhängig, R137)."""
    self.logger.info("")
    self.logger.info("=" * 60)
    self.logger.info("CMB-TEMPERATUR-RELATION (EINHEITENABHÄNGIGE ÜBEREINSTIMMUNG)")
    self.logger.info("=" * 60)

    # T0-Relation: T_CMB/E_ξ = (16/9) × ξ²
    E_xi = 1 / self.const.xi # Charakteristische ξ-Energie (reine Zahl)

    # CMB-Temperatur in eV (k_B × 2,7255 K)
    T_CMB_natural = 2.35e-4 # [T0-Dok], eV

    # Verhältnis mit T_CMB in eV
    ratio_observed = T_CMB_natural / E_xi

    # Relation
    ratio_relation = (16/9) * self.const.xi**2

    # Dieselbe Rechnung mit T_CMB in Kelvin
    ratio_in_K = self.const.T_CMB_K / E_xi

    self.logger.info("T0-Modell CMB-Temperatur-Relation:")
    self.logger.info(f"E_ξ = 1/ξ = {E_xi:.0f} (reine Zahl)")
    self.logger.info(f"T_CMB = {T_CMB_natural:.2e} eV [T0-Dok]")
    self.logger.info("")
    self.logger.info("VERHÄLTNIS-VERGLEICH:")
    self.logger.info(f"T_CMB/E_ξ mit T_CMB in eV: {ratio_observed:.3e}")
    self.logger.info(f"(16/9) × ξ²:               {ratio_relation:.3e}")
    self.logger.info(f"T_CMB/E_ξ mit T_CMB in K:  {ratio_in_K:.3e}")

    deviation_temp = abs(ratio_observed - ratio_relation)
    relative_error_temp = (deviation_temp / ratio_relation) * 100

    self.logger.info(f"Abweichung (eV-Lesart): {relative_error_temp:.1f}%")
    self.logger.info("")
    self.logger.info("EINORDNUNG: Die Relation ergibt eine reine Zahl, die erst in der")
    self.logger.info("Energieeinheit eV mit dem Messwert übereinstimmt (in K um den Faktor")
    self.logger.info(f"{ratio_in_K/ratio_relation:.1e} daneben). Einheitenabhängige Übereinstimmung,")
    self.logger.info("keine Herleitung; die Frage ist offen (R137, R70) [S].")

    return {
      'E_xi': E_xi,
      'T_CMB_natural': T_CMB_natural,
      'ratio_observed': ratio_observed,
      'ratio_relation': ratio_relation,
      'ratio_in_K': ratio_in_K,
      'deviation': deviation_temp,
      'relative_error_eV': relative_error_temp,
      'status': 'einheitenabhaengige Uebereinstimmung, offen (R137, R70)'
    }

  def generate_summary(self, all_results: Dict):
    """Generiert eine Zusammenfassung aller Rechnungen."""
    self.logger.info("")
    self.logger.info("=" * 80)
    self.logger.info("ZUSAMMENFASSUNG")
    self.logger.info("=" * 80)

    self.logger.info("KERNRESULTATE:")
    self.logger.info("")

    # Charakteristische Längenskala
    L_xi = all_results['length']['L_xi_micrometers']
    self.logger.info(f"1. Charakteristische ξ-Längenskala: L_ξ = {L_xi:.1f} μm (aus ρ_CMB und ξ)")

    # Casimir-CMB-Verhältnis
    ratio = all_results['casimir_ratio']['ratio_formula']
    self.logger.info(f"2. Casimir-CMB-Verhältnis π²/(720ξ) = {ratio:.1f} -- Identität über L_ξ (R136)")

    # CMB-Temperatur
    rel = all_results['temperature']['relative_error_eV']
    self.logger.info(f"3. T_CMB/E_ξ = (16/9)ξ²: {rel:.1f} % nur in eV -- einheitenabhängig, offen (R137)")

    # Formel-Umformung
    self.logger.info("4. Umgeschriebene Casimir-Formel = Standardformel (Umformung, kein Test)")

    self.logger.info("")
    self.logger.info("EINSTUFUNG:")
    self.logger.info("• Casimir-CMB-Verbindung: Skalenaussage [S], kein Beleg (R136)")
    self.logger.info("• T_CMB aus ξ: einheitenabhängige Übereinstimmung, offen (R137, R70)")
    self.logger.info("• Offen: ob L_ξ eine eigene physikalische Casimir-Signatur hat (R136)")

    # Quellen
    self.logger.info("")
    self.logger.info("VERWENDETE QUELLEN:")
    self.logger.info("• CODATA: Committee on Data for Science and Technology 2018")
    self.logger.info("• Planck: Planck Collaboration 2018 (CMB-Daten)")
    self.logger.info("• T0-Dok: T0-Theorie Projektdokumentation")
    self.logger.info("• GitHub: https://github.com/jpascher/T0-Time-Mass-Duality")
    self.logger.info(" (Alle T0-Quelldokumente und Theorie verfügbar)")

  def _scaling_rows(self, all_results: Dict):
    """Zeilen der Skalierungstabelle (Abstand, Verhältnis) aus den Rechenwerten."""
    rows = []
    for d, v in all_results['scaling'].items():
      if isinstance(v, dict):
        rows.append((v['distance_str'], v['ratio_to_cmb']))
    return rows

  def generate_markdown_report(self, all_results: Dict) -> str:
    """Generiert einen formatierten Markdown-Bericht."""
    L_xi = all_results['length']['L_xi_micrometers']
    cr = all_results['casimir_ratio']
    tp = all_results['temperature']
    d_eq = all_results['scaling']['d_equal_m'] * 1e6
    scaling_md = "\n".join(f"{s:>8} | {r:.1e}" for s, r in self._scaling_rows(all_results))

    markdown = f"""# T0-Modell Casimir-CMB Nachrechnung

**Datum:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Stand:** korrigiert 1.10.2026 (Dok. 025/061, A260; Dok. 190, R136, R137)

---

## Zusammenfassung

Das T0-Modell verbindet Casimir-Effekt und CMB über die Längenskala L_ξ. Die Nachrechnung zeigt: Das Verhältnis der Energiedichten bei L_ξ ist eine Identität, weil L_ξ selbst aus der gemessenen CMB-Energiedichte und ξ bestimmt wird. Die Verbindung ist eine Skalenaussage [S], kein Beleg (R136). Die T_CMB-Relation stimmt nur in eV, einheitenabhängig, offen (R137).

### Kernresultate

| **Rechnung** | **Ergebnis** | **Einstufung** |
|--------------|--------------|----------------|
| Charakteristische ξ-Längenskala | L_ξ = {L_xi:.1f} μm | aus ρ_CMB und ξ |
| Casimir-CMB-Verhältnis | π²/(720ξ) = {cr['ratio_formula']:.1f} | Identität [S] (R136) |
| CMB-Temperatur-Relation | {tp['ratio_observed']:.2e} (eV) | einheitenabhängig, offen (R137) |
| Umgeschriebene Casimir-Formel | = Standardformel | Umformung, kein Test |

---

## Rechnungen

### 1. Charakteristische ξ-Längenskala

```
L_ξ = (ξℏc/ρ_CMB)^(1/4) = {L_xi:.1f} μm
```

L_ξ ist über die gemessene CMB-Energiedichte definiert.

### 2. Casimir-CMB-Verhältnis

Casimir-Energiedichte π²ℏc/(720 d⁴) (π²ℏc/(240 d⁴) ist der Druck):

| **Parameter** | **Wert** | **Einheit** |
|---------------|----------|-------------|
| Casimir-Energiedichte bei L_ξ | {cr['rho_casimir']:.2e} | J/m³ |
| CMB-Energiedichte | {self.const.rho_CMB_SI:.2e} | J/m³ |
| Verhältnis in SI (L_ξ aus ρ_CMB) | {cr['ratio_SI']:.1f} | - |
| Geschlossene Form π²/(720ξ) | {cr['ratio_formula']:.1f} | - |

Beide Werte sind dieselbe Formel; ihre Gleichheit folgt aus der Definition von L_ξ und ist kein Vergleich mit einer Messung.

### 3. Skalierungsverhalten

```
Abstand  | Casimir/CMB-Verhältnis
---------|----------------------
{scaling_md}
```

Bei L_ξ fallen beide Dichten nicht zusammen (Verhältnis ≈ 103); Gleichheit liegt bei d ≈ {d_eq:.0f} μm.

### 4. CMB-Temperatur-Relation

**Relation:** T_CMB/E_ξ = (16/9) × ξ²

| **Parameter** | **Wert** |
|---------------|----------|
| T_CMB/E_ξ (T_CMB in eV) | {tp['ratio_observed']:.3e} |
| (16/9) × ξ² | {tp['ratio_relation']:.3e} |
| T_CMB/E_ξ (T_CMB in K) | {tp['ratio_in_K']:.3e} |

Die Übereinstimmung besteht nur in der Energieeinheit eV; sie ist einheitenabhängig und keine Herleitung (R137, R70).

---

## Einstufung

- Casimir-CMB-Verbindung: Skalenaussage [S], kein Beleg (R136)
- T_CMB aus ξ: einheitenabhängige Übereinstimmung, offen (R137, R70)
- Offen: ob L_ξ eine eigene physikalische Casimir-Signatur hat (R136)

[S] = Skalenaussage/Hypothese, nicht als Beleg zu werten.

---

## Quellenverzeichnis

| **Abkürzung** | **Vollständige Quelle** |
|---------------|-------------------------|
| **CODATA** | Committee on Data for Science and Technology 2018 Values |
| **Planck** | Planck Collaboration 2018 Results (CMB-Parameter) |
| **T0-Dok** | T0-Theorie Projektdokumentation (ξ-Parameter) |

---

*Generiert am {datetime.now().strftime('%Y-%m-%d')} durch CMB_De.py*
"""
    return markdown

  def generate_latex_report(self, all_results: Dict) -> str:
    """Generiert einen formatierten LaTeX-Bericht."""
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
\usepackage[ngerman]{babel}
\usepackage{amsmath,amssymb}
\usepackage{booktabs}
\usepackage{geometry}
\geometry{margin=2.5cm}

\title{T0-Modell Casimir-CMB Nachrechnung}
\author{Automatisch generiert (CMB\_De.py)}
\date{""" + f"{datetime.now().strftime('%Y-%m-%d')}" + r"""}

\begin{document}
\maketitle

\begin{abstract}
Das Verhältnis von Casimir- zu CMB-Energiedichte bei $L_\xi$ ist eine Identität, weil $L_\xi$ aus der gemessenen CMB-Energiedichte und $\xi$ bestimmt wird: $\pi^2/(720\xi) \approx """ + f"{cr['ratio_formula']:.1f}" + r"""$. Die Verbindung ist eine Skalenaussage [S], kein Beleg (Dok.~190, R136). Die Relation $T_{\text{CMB}}/E_\xi = (16/9)\xi^2$ stimmt nur in eV, einheitenabhängig, offen (R137). [S] = Skalenaussage/Hypothese.
\end{abstract}

\section{Charakteristische $\xi$-Längenskala}
\begin{equation}
L_\xi = \left(\frac{\xi \hbar c}{\rho_{\text{CMB}}}\right)^{1/4} = """ + f"{L_xi:.1f}" + r"""\,\mu\text{m}
\end{equation}

\section{Casimir-CMB-Verhältnis}
Energiedichte (nicht Druck):
\begin{align}
\left|\rho_{\text{Casimir}}\right| &= \frac{\pi^2 \hbar c}{720 d^4} = """ + f"{cr['rho_casimir']:.2e}" + r"""\,\text{J/m}^3 \\
\rho_{\text{CMB}} &= """ + f"{self.const.rho_CMB_SI:.2e}" + r"""\,\text{J/m}^3 \\
\frac{\left|\rho_{\text{Casimir}}\right|}{\rho_{\text{CMB}}} &= \frac{\pi^2}{720\xi} = \frac{\pi^2 \times 10^4}{960} \approx """ + f"{cr['ratio_formula']:.1f}" + r"""
\end{align}
Der SI-Wert ist dieselbe Formel mit $L_\xi$ aus $\rho_{\text{CMB}}$ (Identität, kein Messwert).

\section{Skalierungsverhalten}
\begin{table}[h]
\centering
\begin{tabular}{cc}
\toprule
\textbf{Abstand} & \textbf{Casimir/CMB-Verhältnis} \\
\midrule
""" + scaling_tex + r"""
\bottomrule
\end{tabular}
\end{table}
Bei $L_\xi$ fallen beide Dichten nicht zusammen; Gleichheit bei $d \approx """ + f"{d_eq:.0f}" + r"""\,\mu$m.

\section{CMB-Temperatur-Relation}
\begin{table}[h]
\centering
\begin{tabular}{cc}
\toprule
\textbf{Größe} & \textbf{Wert} \\
\midrule
$T_{\text{CMB}}/E_\xi$ ($T$ in eV) & $""" + f"{tp['ratio_observed']:.3e}" + r"""$ \\
$(16/9)\xi^2$ & $""" + f"{tp['ratio_relation']:.3e}" + r"""$ \\
$T_{\text{CMB}}/E_\xi$ ($T$ in K) & $""" + f"{tp['ratio_in_K']:.3e}" + r"""$ \\
\bottomrule
\end{tabular}
\end{table}
Einheitenabhängige Übereinstimmung, keine Herleitung; offen (R137, R70).

\section{Einstufung}
\begin{itemize}
\item Casimir-CMB-Verbindung: Skalenaussage [S], kein Beleg (R136)
\item $T_{\text{CMB}}$ aus $\xi$: einheitenabhängig, offen (R137, R70)
\item Offen: eigene physikalische Casimir-Signatur von $L_\xi$ (R136)
\end{itemize}

\section{Quellen}
\begin{itemize}
\item \textbf{CODATA:} Committee on Data for Science and Technology 2018 Values
\item \textbf{Planck:} Planck Collaboration 2018 Results (CMB-Parameter)
\item \textbf{T0-Dok:} T0-Theorie Projektdokumentation ($\xi$-Parameter)
\item \textbf{GitHub:} \texttt{https://github.com/jpascher/T0-Time-Mass-Duality}
\end{itemize}

\end{document}
"""
    return latex

def main():
  """Hauptfunktion des Skripts."""

  # Logging Setup
  logger = setup_logging()

  try:
    # Konstanten initialisieren
    constants = PhysicalConstants()
    constants.log_constants(logger)

    # Calculator initialisieren
    calc = T0Calculator(constants, logger)

    # Alle Berechnungen durchführen
    all_results = {}

    # 1. Charakteristische Längenskala
    L_xi, length_results = calc.calculate_characteristic_length()
    all_results['length'] = length_results

    # 2. Casimir-CMB-Verhältnis (Identität)
    casimir_results = calc.verify_casimir_cmb_ratio(L_xi)
    all_results['casimir_ratio'] = casimir_results

    # 3. Umgeschriebene Casimir-Formel
    formula_results = calc.verify_modified_casimir_formula(L_xi)
    all_results['modified_formula'] = formula_results

    # 4. Skalierungsverhalten
    scaling_results = calc.analyze_scaling_behavior(L_xi)
    all_results['scaling'] = scaling_results

    # 5. CMB-Temperatur-Relation
    temp_results = calc.verify_cmb_temperature_prediction()
    all_results['temperature'] = temp_results

    # 6. Zusammenfassung
    calc.generate_summary(all_results)

    # 7. Berichte generieren
    logger.info("")
    logger.info("=" * 60)
    logger.info("BERICHTE GENERIEREN")
    logger.info("=" * 60)

    # Markdown-Bericht
    markdown_report = calc.generate_markdown_report(all_results)
    markdown_filename = "t0_casimir_cmb_report_De.md"
    with open(markdown_filename, 'w', encoding='utf-8') as f:
      f.write(markdown_report)
    logger.info(f"✓ Markdown-Bericht erstellt: {markdown_filename}")

    # LaTeX-Bericht
    latex_report = calc.generate_latex_report(all_results)
    latex_filename = "t0_casimir_cmb_report_De.tex"
    with open(latex_filename, 'w', encoding='utf-8') as f:
      f.write(latex_report)
    logger.info(f"✓ LaTeX-Bericht erstellt: {latex_filename}")

    # JSON-Export für weitere Verarbeitung
    import json
    json_filename = "t0_casimir_cmb_data_De.json"
    with open(json_filename, 'w', encoding='utf-8') as f:
      json.dump(all_results, f, indent=2, ensure_ascii=False, default=str)
    logger.info(f"✓ JSON-Daten exportiert: {json_filename}")

    logger.info("")
    logger.info("=" * 80)
    logger.info("NACHRECHNUNG ABGESCHLOSSEN -- alle Prüfungen bestanden")
    logger.info("=" * 80)
    logger.info("Generierte Dateien:")
    logger.info(f"• Log-Datei: {logging.getLogger().handlers[0].baseFilename}")
    logger.info(f"• Markdown-Bericht: {markdown_filename}")
    logger.info(f"• LaTeX-Bericht: {latex_filename}")
    logger.info(f"• JSON-Daten: {json_filename}")
    logger.info("")
    logger.info("T0-Theorie: Zeit-Masse-Dualitäts-Framework")
    logger.info("GitHub: https://github.com/jpascher/T0-Time-Mass-Duality")
    logger.info("Alle T0-Quelldokumente und Theorie verfügbar")

    return all_results

  except Exception as e:
    logger.error(f"Fehler bei der Nachrechnung: {e}")
    raise

if __name__ == "__main__":
  results = main()
  print("\nSkript erfolgreich ausgeführt. Details siehe Log-Datei.")
