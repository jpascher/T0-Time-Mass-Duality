#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analyse: E₀ (charakteristische Energie)
Idealisierter Wert vs. Fraktal korrigierter Wert

Ziel: Verstehen woher E₀ = 7.398 MeV in calc_De.py kommt
und wie es mit B18-Parametern zusammenhängt.

Datum: 2026-02-03
"""

import math
from fractions import Fraction

print("\n" + "="*70)
print("ANALYSE: CHARAKTERISTISCHE ENERGIE E₀")
print("Idealisiert vs. Fraktal korrigiert")
print("="*70)

# ==============================================================================
# FUNDAMENTALE PARAMETER
# ==============================================================================

print("\n" + "="*70)
print("FUNDAMENTALE PARAMETER (identisch in beiden Theorien)")
print("="*70)

# Goldener Schnitt
phi = (1 + math.sqrt(5)) / 2

# Torsionskonstante
xi = float(Fraction(4, 3) * 1e-4)

# Sub-Planck-Faktoren
f_ideal = 30000 / 4  # = 7500
delta = 5 * phi
f_real = f_ideal - delta  # = 7491.91

# Gitter-Einheit
gitter_einheit = f_ideal * xi  # = 1.0

print(f"φ (goldener Schnitt) = {phi:.9f}")
print(f"ξ (Torsionskonstante) = {xi:.10e}")
print(f"f_ideal = {f_ideal:.0f}")
print(f"Δ (Symmetriebrechung) = 5φ = {delta:.9f}")
print(f"f_real = f_ideal - Δ = {f_real:.9f}")
print(f"Gitter-Einheit = f_ideal × ξ = {gitter_einheit:.10f}")

# ==============================================================================
# METHODE 1: IDEALISIERTE ENERGIE E₀_ideal
# ==============================================================================

print("\n" + "="*70)
print("METHODE 1: IDEALISIERTE ENERGIE E₀_ideal")
print("="*70)

print("""
AUSGANGSPUNKT: Feinstrukturkonstante aus Energiebasis

T0-Formel: α = ξ × (E₀/1MeV)²

Für die ideale (perfekte) Struktur würden wir erwarten:
α_ideal sollte mit der idealisierten Geometrie konsistent sein.

ZWEI ANSÄTZE:

A) Von α ausgehen:
   α_exp = 7.2973525693×10⁻³ (experimentell)
   E₀² = α_exp / ξ
   E₀_ideal = √(α_exp / ξ)

B) Von 1/ξ ausgehen (dimensionale Konsistenz):
   E₀_ideal ∝ 1/√ξ
""")

# Ansatz A: Aus experimentellem α
alpha_exp = 7.2973525693e-3
E0_ideal_A = math.sqrt(alpha_exp / xi)

print(f"ANSATZ A (aus experimentellem α):")
print(f"  α_exp = {alpha_exp:.10e}")
print(f"  E₀_ideal = √(α_exp / ξ)")
print(f"  E₀_ideal = √({alpha_exp:.6e} / {xi:.6e})")
print(f"  E₀_ideal = {E0_ideal_A:.6f} (dimensionslos)")

# Ansatz B: Aus ξ
E0_ideal_B = 1 / math.sqrt(xi)

print(f"\nANSATZ B (aus 1/√ξ):")
print(f"  E₀_ideal = 1 / √ξ")
print(f"  E₀_ideal = 1 / √{xi:.6e}")
print(f"  E₀_ideal = {E0_ideal_B:.6f} (dimensionslos)")

# Vergleich
print(f"\nVERGLEICH:")
print(f"  Ansatz A: E₀ = {E0_ideal_A:.6f}")
print(f"  Ansatz B: E₀ = {E0_ideal_B:.6f}")
print(f"  Verhältnis: {E0_ideal_A / E0_ideal_B:.6f}")

# ==============================================================================
# METHODE 2: FRAKTAL KORRIGIERTE ENERGIE E₀_korrigiert
# ==============================================================================

print("\n" + "="*70)
print("METHODE 2: FRAKTAL KORRIGIERTE ENERGIE E₀_korrigiert")
print("="*70)

print("""
FRAKTAL-KORREKTUR analog zu f_real = f_ideal - Δ

Die pentagonale Symmetriebrechung (5φ) beeinflusst auch E₀:

OPTION 1: Direkte Subtraktion
  E₀_korr = E₀_ideal - φ

OPTION 2: Multiplikative Korrektur
  E₀_korr = E₀_ideal × (f_real / f_ideal)

OPTION 3: Aus korrigiertem α berechnen
  α_korr (aus B18) = 1 / (π⁴ × √2)
  E₀_korr = √(α_korr / ξ)

OPTION 4: Wurzel-Korrektur (symmetrisch zu f)
  E₀_korr = E₀_ideal - √(5φ)
""")

# Option 1: Direkte Subtraktion
E0_korr_1 = E0_ideal_A - phi
print(f"OPTION 1 (Direkte Subtraktion):")
print(f"  E₀_korr = E₀_ideal - φ")
print(f"  E₀_korr = {E0_ideal_A:.6f} - {phi:.6f}")
print(f"  E₀_korr = {E0_korr_1:.6f}")

# Option 2: Multiplikative Korrektur
E0_korr_2 = E0_ideal_A * (f_real / f_ideal)
print(f"\nOPTION 2 (Multiplikative Korrektur):")
print(f"  E₀_korr = E₀_ideal × (f_real / f_ideal)")
print(f"  E₀_korr = {E0_ideal_A:.6f} × ({f_real:.2f} / {f_ideal:.0f})")
print(f"  E₀_korr = {E0_ideal_A:.6f} × {f_real/f_ideal:.9f}")
print(f"  E₀_korr = {E0_korr_2:.6f}")

# Option 3: Aus B18-α
alpha_b18 = 1 / (math.pi**4 * math.sqrt(2))
E0_korr_3 = math.sqrt(alpha_b18 / xi)
print(f"\nOPTION 3 (Aus B18-α):")
print(f"  α_B18 = 1 / (π⁴ × √2) = {alpha_b18:.10e}")
print(f"  E₀_korr = √(α_B18 / ξ)")
print(f"  E₀_korr = {E0_korr_3:.6f}")

# Option 4: Wurzel-Korrektur
E0_korr_4 = E0_ideal_A - math.sqrt(delta)
print(f"\nOPTION 4 (Wurzel-Korrektur):")
print(f"  E₀_korr = E₀_ideal - √(5φ)")
print(f"  E₀_korr = {E0_ideal_A:.6f} - √{delta:.6f}")
print(f"  E₀_korr = {E0_ideal_A:.6f} - {math.sqrt(delta):.6f}")
print(f"  E₀_korr = {E0_korr_4:.6f}")

# ==============================================================================
# VERGLEICH MIT calc_De.py WERT
# ==============================================================================

print("\n" + "="*70)
print("VERGLEICH MIT calc_De.py")
print("="*70)

E0_calc = 7.398  # MeV aus calc_De.py

print(f"\nE₀ aus calc_De.py = {E0_calc} MeV (empirisch, fraktal korrigiert)")
print(f"\n{'Methode':<35} {'Wert':<15} {'Abweichung':<15}")
print("-"*65)
print(f"{'E₀_ideal (Ansatz A)':<35} {E0_ideal_A:<15.6f} {abs(E0_ideal_A - E0_calc):<15.6f}")
print(f"{'E₀_ideal (Ansatz B)':<35} {E0_ideal_B:<15.6f} {abs(E0_ideal_B - E0_calc):<15.6f}")
print(f"{'E₀_korr (Option 1: -φ)':<35} {E0_korr_1:<15.6f} {abs(E0_korr_1 - E0_calc):<15.6f}")
print(f"{'E₀_korr (Option 2: ×f_real/f)':<35} {E0_korr_2:<15.6f} {abs(E0_korr_2 - E0_calc):<15.6f}")
print(f"{'E₀_korr (Option 3: B18-α)':<35} {E0_korr_3:<15.6f} {abs(E0_korr_3 - E0_calc):<15.6f}")
print(f"{'E₀_korr (Option 4: -√(5φ))':<35} {E0_korr_4:<15.6f} {abs(E0_korr_4 - E0_calc):<15.6f}")

# Finde beste Übereinstimmung
optionen = {
    'Option 1 (-φ)': E0_korr_1,
    'Option 2 (×f_real/f)': E0_korr_2,
    'Option 3 (B18-α)': E0_korr_3,
    'Option 4 (-√(5φ))': E0_korr_4
}

beste_option = min(optionen.items(), key=lambda x: abs(x[1] - E0_calc))

print(f"\n{'='*65}")
print(f"BESTE ÜBEREINSTIMMUNG: {beste_option[0]}")
print(f"  E₀ = {beste_option[1]:.6f}")
print(f"  calc_De.py: {E0_calc}")
print(f"  Abweichung: {abs(beste_option[1] - E0_calc):.6f}")
print(f"  Relative Abweichung: {abs(beste_option[1] - E0_calc)/E0_calc * 100:.2f}%")

# ==============================================================================
# ALTERNATIVE: UMGEKEHRTE RECHNUNG
# ==============================================================================

print("\n" + "="*70)
print("UMGEKEHRTE RECHNUNG: E₀ aus B18-Parametern direkt")
print("="*70)

print("""
Aus der B18-Feinstrukturkonstante:
  α⁻¹_B18 = (f_ideal × ξ) × π⁴ × √2

Wenn wir E₀ so definieren, dass α = ξ × E₀²:
  E₀² = α / ξ = 1 / (ξ × α⁻¹)
  E₀² = 1 / (ξ × (f_ideal × ξ) × π⁴ × √2)
  E₀² = 1 / (ξ² × f_ideal × π⁴ × √2)
  E₀ = 1 / (ξ × √(f_ideal × π⁴ × √2))
""")

# Mit f_ideal
E0_aus_f_ideal = 1 / (xi * math.sqrt(f_ideal * math.pi**4 * math.sqrt(2)))
print(f"Mit f_ideal = {f_ideal:.0f}:")
print(f"  E₀ = 1 / (ξ × √(f_ideal × π⁴ × √2))")
print(f"  E₀ = {E0_aus_f_ideal:.6f}")

# Mit f_real (fraktal korrigiert)
E0_aus_f_real = 1 / (xi * math.sqrt(f_real * math.pi**4 * math.sqrt(2)))
print(f"\nMit f_real = {f_real:.2f}:")
print(f"  E₀ = 1 / (ξ × √(f_real × π⁴ × √2))")
print(f"  E₀ = {E0_aus_f_real:.6f}")

print(f"\nVergleich mit calc_De.py:")
print(f"  E₀ (aus f_ideal) = {E0_aus_f_ideal:.6f}")
print(f"  E₀ (aus f_real)  = {E0_aus_f_real:.6f}")
print(f"  E₀ (calc_De.py)  = {E0_calc}")
print(f"  Beste Übereinstimmung: {'f_real' if abs(E0_aus_f_real - E0_calc) < abs(E0_aus_f_ideal - E0_calc) else 'f_ideal'}")

# ==============================================================================
# FAZIT UND FORMEL
# ==============================================================================

print("\n" + "="*70)
print("FAZIT: HERLEITUNG VON E₀")
print("="*70)

print(f"""
ERGEBNIS:

1. IDEALISIERTE ENERGIE:
   E₀_ideal = √(α_exp / ξ) = {E0_ideal_A:.6f}
   
   Oder dimensionslos:
   E₀_ideal = 1/√ξ = {E0_ideal_B:.6f}

2. FRAKTAL KORRIGIERTE ENERGIE:
   BESTE FORMEL: {beste_option[0]}
   E₀_korrigiert = {beste_option[1]:.6f}
   
   Alternativ aus B18:
   E₀ = 1 / (ξ × √(f_real × π⁴ × √2)) = {E0_aus_f_real:.6f}

3. EMPIRISCHER WERT (calc_De.py):
   E₀_empirisch = {E0_calc} MeV

BEZIEHUNG:
   E₀_ideal → E₀_korrigiert durch pentagonale Symmetriebrechung
   Analog zu: f_ideal → f_real = f_ideal - 5φ

INTERPRETATION:
   E₀ ist die charakteristische Energieskala, die aus der
   geometrischen Struktur des Torsionskristalls emergiert.
   
   Die Korrektur durch 5φ reflektiert die gleiche
   pentagonale Symmetriebrechung wie bei f.

VERWENDUNG IN B18:
   Man kann E₀ als alternative Parametrisierung verwenden:
   
   α = ξ × E₀²  (T0-Stil, energiebasiert)
   
   statt:
   
   α⁻¹ = (f_ideal × ξ) × π⁴ × √2  (B18-Stil, zeitbasiert)
   
   Beide sind äquivalent, wenn:
   E₀ = 1 / (ξ × √(f_ideal × π⁴ × √2))
""")

# ==============================================================================
# ZUSAMMENFASSUNG DER FORMELN
# ==============================================================================

print("\n" + "="*70)
print("ZUSAMMENFASSUNG: E₀ FORMELN")
print("="*70)

print(f"""
┌─────────────────────────────────────────────────────────────────┐
│ IDEALISIERT (perfekte Symmetrie):                               │
├─────────────────────────────────────────────────────────────────┤
│ E₀_ideal = √(α_exp / ξ)           = {E0_ideal_A:.6f}         │
│ E₀_ideal = 1 / √ξ                  = {E0_ideal_B:.6f}         │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ FRAKTAL KORRIGIERT (mit Symmetriebrechung):                     │
├─────────────────────────────────────────────────────────────────┤
│ E₀_korr = 1/(ξ×√(f_real×π⁴×√2))   = {E0_aus_f_real:.6f}      │
│ E₀_korr = E₀_ideal × (f_real/f)   = {E0_korr_2:.6f}           │
│ E₀_korr = E₀_ideal - φ             = {E0_korr_1:.6f}           │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ EMPIRISCH (aus calc_De.py):                                     │
├─────────────────────────────────────────────────────────────────┤
│ E₀_empirisch = {E0_calc} MeV                                    │
└─────────────────────────────────────────────────────────────────┘

NUMERISCHE WERTE:
  ξ = {xi:.10e}
  φ = {phi:.9f}
  f_ideal = {f_ideal:.0f}
  f_real = {f_real:.9f}
  π⁴ × √2 = {math.pi**4 * math.sqrt(2):.6f}
""")

print("="*70 + "\n")
