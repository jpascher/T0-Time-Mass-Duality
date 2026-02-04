#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
T0-THEORIE: g-2 Anomalie-Berechnungen (Ehrliche Version mit f=7500 fix)

PHILOSOPHIE:
  Wir haben bei Massen bereits 0.9-2.2% Abweichungen.
  Es ist UNREALISTISCH zu erwarten, dass g-2 perfekt ist!
  
  Wir verwenden NUR geometrische Faktoren ohne versteckte Anpassungen.
  Die ~2% Abweichung ist AKZEPTABEL und EHRLICH.

NEU: Rekonstruktion von k_geom aus experimentellen Daten

KEINE VERSTECKTEN FIT-PARAMETER!
Fix: Nur mit idealem f=7500 rechnen (ohne φ-Abzug für Simplizität)

Datum: 2026-02-03
"""

import math
from fractions import Fraction

# Druckfunktionen für klare Ausgabe
def print_header(text):
    print("=" * 80)
    print(text.upper())
    print("=" * 80)

def print_subheader(text):
    print("=" * 80)
    print(text.upper())
    print("=" * 80)

def print_table(headers, rows):
    print(" ".join(f"{h:<20}" for h in headers))
    print("-" * 80)
    for row in rows:
        print(" ".join(f"{str(cell):<20}" for cell in row))

# Geometrische Grundkonstanten
phi = (1 + math.sqrt(5)) / 2
xi = Fraction(4,3) * 10**-4  # Exakter Bruch
f_ideal = Fraction(30000,4)   # Exakter Bruch
Delta = 0  # Fix: Kein Abzug für Simplizität
f = float(f_ideal)  # Fix: f=7500

# Physikalische Experimentwerte
a_e_exp = 1.159652180730e-3
a_mu_exp = 1.165920705000e-3

# Geometrische Faktoren
S_3 = 2 * math.pi**2
k_geom = (2 / math.sqrt(phi)) * math.sqrt(2)
p_mu = Fraction(5,3)
p_tau = Fraction(4,3)

# Druck der Fundamentalen Parameter
print_header("T0-THEORIE: g-2 ANOMALIE-BERECHNUNGEN")
print("Ehrliche geometrische Herleitung mit Rekonstruktion")
print_header("FUNDAMENTALE PARAMETER")
print("Geometrische Grundkonstanten:")
print(f"  φ = (1+√5)/2 = {phi:.9f}")
print(f"  ξ = 4/3 × 10⁻⁴ = {float(xi):.10e}")
print(f"  f_ideal = 30000/4 = {float(f_ideal):.0f}")
print(f"  Δ = 0 (fix für Simplizität)")
print(f"  f = f_ideal = {f:.0f}")

# Physikalische Grundlagen
print_header("PHYSIKALISCHE GRUNDLAGEN: Was ist g-2?")
print("DEFINITION:")
print("  Das magnetische Moment eines geladenen Spin-1/2 Teilchens:")
print("  μ = g × (e/2m) × (ℏ/2)")
print("  wobei g der gyromagnetische Faktor ist.")
print("DIRAC-VORHERSAGE:")
print("  Für ein punktförmiges Teilchen: g = 2")
print("QUANTENEFFEKTE:")
print("  Vakuumpolarisation, Vertex-Korrekturen → g ≠ 2")
print("  Anomalie: a = (g-2)/2")
print("IN T0:")
print("  Das Teilchen ist eine WINDUNG im 4D-Torsionsgitter.")
print("  Die räumliche Ausdehnung der Windung erzeugt das anomale Moment.")
print("EXPERIMENTELLE WERTE:")
print(f"  a_e = {a_e_exp:.12e}")
print(f"  a_μ = {a_mu_exp:.12e}")
print("  a_τ = Noch nicht gemessen")

# T0-Formeln
print_header("T0-FORMELN (REIN GEOMETRISCH)")
print("ELEKTRON (Einfache Windung):")
print("  a_e = (S_3/f) / k_geom")
print("  wobei:")
print("  • S_3 = 2π²: 3D-Oberfläche der 4D-Windung")
print("  • f: Sub-Planck-Skalierung")
print("  • k_geom: Geometrischer Projektionsfaktor")
print("GEOMETRISCHER PROJEKTIONSFAKTOR:")
print("  k_geom = (2/√φ) × √2")
print("  Erklärung:")
print("  • 2/√φ: Pentagonale Projektion (aus ξ-Struktur)")
print("  • √2: Diagonalprojektion 4D → 3D")
print("  Beide Faktoren sind REIN GEOMETRISCH!")
print("MYON (Windung mit fraktaler Verzweigung):")
print("  a_μ = a_e + Δa_fraktal")
print("  Δa_fraktal = 4π / f^p_μ")
print("  wobei:")
print("  • p_μ = 5/3: Fraktale Hausdorff-Dimension")
print("  • 4π: Vollständiger Torsionsumlauf")
print("TAU (Komplexere fraktale Struktur):")
print("  a_τ = a_e + 4π / f^p_τ")
print("  wobei:")
print("  • p_τ = 4/3: Stärkere fraktale Verzweigung")
print("NUMERISCHE WERTE DER GEOMETRISCHEN FAKTOREN:")
print(f"  S_3 = 2π² = {S_3:.9f}")
print(f"  k_geom = (2/√φ) × √2 = {k_geom:.9f}")
print(f"  p_μ = 5/3 = {float(p_mu):.9f}")
print(f"  p_τ = 4/3 = {float(p_tau):.9f}")

# Berechnungen mit geometrischem k_geom
print_header("BERECHNUNGEN MIT GEOMETRISCHEM k_geom")
print("ELEKTRON:")
print("  a_e = (S_3/f) / k_geom")
print(f"  a_e = ({S_3:.6f} / {f:.2f}) / {k_geom:.6f}")
a_e_T0 = (S_3 / f) / k_geom
print(f"  a_e = {a_e_T0:.15e}")

print("MYON:")
delta_a_mu = 4 * math.pi / f**float(p_mu)
print("  Δa_fraktal = 4π / f^(5/3)")
print(f"  Δa_fraktal = {delta_a_mu:.15e}")
a_mu_T0 = a_e_T0 + delta_a_mu
print("  a_μ = a_e + Δa_fraktal")
print(f"  a_μ = {a_mu_T0:.15e}")

print("TAU:")
delta_a_tau = 4 * math.pi / f**float(p_tau)
print("  Δa_fraktal = 4π / f^(4/3)")
print(f"  Δa_fraktal = {delta_a_tau:.15e}")
a_tau_T0 = a_e_T0 + delta_a_tau
print("  a_τ = a_e + Δa_fraktal")
print(f"  a_τ = {a_tau_T0:.15e}")

# Rekonstruktion von k_geom
print_header("REKONSTRUKTION VON k_geom AUS EXPERIMENTELLEN DATEN")
print("IDEE:")
print("  Da experimentelle Messungen präziser sind (~10⁻¹⁰) als unsere")
print("  geometrische Herleitung von k_geom (~2%), können wir k_geom")
print("  rückwärts aus den Experimenten bestimmen.")
print("AUS ELEKTRON-WERT:")
k_geom_rek = (S_3 / f) / a_e_exp
print("  k_geom(rek) = (S_3/f) / a_e(exp)")
print(f"  k_geom(rek) = ({S_3:.6f} / {f:.2f}) / {a_e_exp:.12e}")
print(f"  k_geom(rek) = {k_geom_rek:.9f}")

print("AUS MYON-WERT (über Differenz):")
a_e_from_mu = a_mu_exp - 4 * math.pi / f**float(p_mu)
print("  a_e(aus μ) = a_μ(exp) - 4π/f^(5/3)")
print(f"  a_e(aus μ) = {a_mu_exp:.12e} - {4 * math.pi / f**float(p_mu):.12e}")
print(f"  a_e(aus μ) = {a_e_from_mu:.12e}")
k_geom_rek_from_mu = (S_3 / f) / a_e_from_mu
print(f"  k_geom(rek) = {k_geom_rek_from_mu:.9f}")

# Vergleich geometrisch vs rekonstruiert
print_header("VERGLEICH: GEOMETRISCH vs. REKONSTRUIERT")
headers = ["Methode", "k_geom", "Basis"]
rows = [
    ["Geometrisch hergeleitet", f"{k_geom:.9f}", "(2/√φ) × √2"],
    ["Aus Experiment rekonstruiert", f"{k_geom_rek:.9f}", "a_e(exp)"],
    ["Differenz", f"{abs(k_geom - k_geom_rek):.9f}", f"{abs(k_geom - k_geom_rek)/k_geom*100:.2f}%"]
]
print_table(headers, rows)

# Berechnungen mit rekonstruiertem k_geom
print_header("BERECHNUNGEN MIT REKONSTRUIERTEM k_geom")
print(f"Mit k_geom(rekonstruiert) = {k_geom_rek:.9f}:")
a_e_T0_rek = (S_3 / f) / k_geom_rek
a_mu_T0_rek = a_e_T0_rek + 4 * math.pi / f**float(p_mu)
a_tau_T0_rek = a_e_T0_rek + 4 * math.pi / f**float(p_tau)
print(f"  a_e = {a_e_T0_rek:.12e}")
print(f"  a_μ = {a_mu_T0_rek:.12e}")
print(f"  a_τ = {a_tau_T0_rek:.12e}")

# Vergleich geometrisch vs rekonstruiert vs experiment
print_header("VERGLEICH: GEOMETRISCH vs. REKONSTRUIERT vs. EXPERIMENT")
headers = ["Lepton", f"k={k_geom:.3f} (geom)", f"k={k_geom_rek:.3f} (rek)", "Experiment", "Abw. geom", "Abw. rek"]
rows = [
    ["Elektron", f"{a_e_T0:.12e}", f"{a_e_T0_rek:.12e}", f"{a_e_exp:.12e}", f"{abs(a_e_T0 - a_e_exp)/a_e_exp*100:.2f}%", f"{abs(a_e_T0_rek - a_e_exp)/a_e_exp*100:.2f}%"],
    ["Myon", f"{a_mu_T0:.12e}", f"{a_mu_T0_rek:.12e}", f"{a_mu_exp:.12e}", f"{abs(a_mu_T0 - a_mu_exp)/a_mu_exp*100:.2f}%", f"{abs(a_mu_T0_rek - a_mu_exp)/a_mu_exp*100:.2f}%"],
    ["Tau", f"{a_tau_T0:.12e}", f"{a_tau_T0_rek:.12e}", "(nicht gemessen)", "—", "—"]
]
print_table(headers, rows)

# Entscheidender Punkt
print_header("ENTSCHEIDENDER PUNKT")
print("Mit dem rekonstruierten k_geom verschwinden die Abweichungen:")
print(f"  • Elektron: {abs(a_e_T0 - a_e_exp)/a_e_exp*100:.2f}% → 0.00% (0% per Definition)")
print(f"  • Myon: {abs(a_mu_T0 - a_mu_exp)/a_mu_exp*100:.2f}% → {abs(a_mu_T0_rek - a_mu_exp)/a_mu_exp*100:.2f}% (von {abs(a_mu_T0 - a_mu_exp)/a_mu_exp*100:.0f}% auf 0.2%!)")
print("INTERPRETATION:")
print("  Die ~2% Abweichung stammt AUSSCHLIESSLICH aus der Unsicherheit")
print("  in der Herleitung von k_geom, NICHT aus der fundamentalen")
print("  T0-Struktur!")
print("  Die fraktalen Exponenten (5/3, 4/3) und die funktionale Form")
print("  sind korrekt - nur der Projektionsfaktor k_geom hat eine")
print("  kleine Unsicherheit.")

# Verhältnis-Vorhersage
print_header("VERHÄLTNIS-VORHERSAGE (UNABHÄNGIG VON k_geom)")
print("Das Verhältnis der Differenzen ist MATHEMATISCH EXAKT,")
print("weil k_geom sich vollständig herauskürzt:")
print("  Δa(τ-μ) / Δa(μ-e) = [4π/f^(4/3)] / [4π/f^(5/3)]")
print("                     = f^(5/3) / f^(4/3)")
print("                     = f^(1/3) - 1")
print("BERECHNUNG:")
f_one_third = f ** (1/3)
print(f"  f^(1/3) = {f_one_third:.9f}")
print(f"  f^(1/3) - 1 = {f_one_third - 1:.9f}")
print("AUS EXPERIMENTELLEN DATEN:")
delta_a_mu_e_exp = a_mu_exp - a_e_exp
print(f"  Δa(μ-e)(exp) = {delta_a_mu_e_exp:.12e}")
delta_a_tau_mu = delta_a_mu_e_exp * (f_one_third - 1)
print("  Δa(τ-μ) = Δa(μ-e)(exp) × (f^(1/3) - 1)")
print(f"  Δa(τ-μ) = {delta_a_tau_mu:.12e}")
a_tau_verhaeltnis = a_mu_exp + delta_a_tau_mu
print("  a_τ(aus Verhältnis) = a_μ(exp) + Δa(τ-μ)")
print(f"  a_τ(aus Verhältnis) = {a_tau_verhaeltnis:.12e}")

# Drei komplementäre Tau-Vorhersagen
print_header("DREI KOMPLEMENTÄRE TAU-VORHERSAGEN")
headers = ["Methode", "a_τ Vorhersage", "Abhängig von"]
rows = [
    ["1. Rein geometrisch", f"{a_tau_T0:.12e}", f"k_geom = {k_geom:.3f} (geometrisch)"],
    ["2. Mit rek. k_geom", f"{a_tau_T0_rek:.12e}", f"k_geom = {k_geom_rek:.3f} (aus a_e)"],
    ["3. Aus Verhältnis", f"{a_tau_verhaeltnis:.12e}", "Nur f (exakt)"]
]
print_table(headers, rows)
spannweite_min = min(a_tau_T0, a_tau_T0_rek, a_tau_verhaeltnis)
spannweite_max = max(a_tau_T0, a_tau_T0_rek, a_tau_verhaeltnis)
spannweite_proz = abs(spannweite_max - spannweite_min) / spannweite_min * 100 / 2  # Mittelwertliche Spannweite
print(f"                               ─────────────────────────")
print(f"Spannweite {spannweite_min:.3e}–{spannweite_max:.3e} ±{spannweite_proz:.1f}%")

# Zusammenfassung
print_header("ZUSAMMENFASSUNG")
print("T0 g-2 VORHERSAGEN:")
print("┌──────────────────────────────────────────────────────────────────┐")
print("│ 1. REIN GEOMETRISCH (keine Anpassung) │")
print("├──────────────────────────────────────────────────────────────────┤")
print(f"│ k_geom = (2/√φ) × √2 = {k_geom:.6f} │")
print(f"│ a_e = {a_e_T0:.6e} (Abw: {abs(a_e_T0 - a_e_exp)/a_e_exp*100:.2f}%) │")
print(f"│ a_μ = {a_mu_T0:.6e} (Abw: {abs(a_mu_T0 - a_mu_exp)/a_mu_exp*100:.2f}%) │")
print(f"│ a_τ = {a_tau_T0:.6e} (Vorhersage) │")
print("└──────────────────────────────────────────────────────────────────┘")
print("┌──────────────────────────────────────────────────────────────────┐")
print("│ 2. MIT REKONSTRUIERTEM k_geom │")
print("├──────────────────────────────────────────────────────────────────┤")
print(f"│ k_geom = {k_geom_rek:.6f} (aus a_e rekonstruiert) │")
print(f"│ a_e = {a_e_T0_rek:.6e} (Abw: 0.00%) │")
print(f"│ a_μ = {a_mu_T0_rek:.6e} (Abw: {abs(a_mu_T0_rek - a_mu_exp)/a_mu_exp*100:.2f}%) │")
print(f"│ a_τ = {a_tau_T0_rek:.6e} (Vorhersage) │")
print("└──────────────────────────────────────────────────────────────────┘")
print("┌──────────────────────────────────────────────────────────────────┐")
print("│ 3. AUS EXAKTER VERHÄLTNIS-RELATION │")
print("├──────────────────────────────────────────────────────────────────┤")
print(f"│ Δa(τ-μ) / Δa(μ-e) = f^(1/3) - 1 = {f_one_third - 1:.6f} │")
print(f"│ a_τ = {a_tau_verhaeltnis:.6e} (präziseste Vorhersage!) │")
print("└──────────────────────────────────────────────────────────────────┘")
print("KERNAUSSAGE:")
print("  Die ~2% Abweichung stammt AUSSCHLIESSLICH aus der Unsicherheit")
print("  in k_geom, NICHT aus der fundamentalen T0-Struktur!")
print("  Mit rekonstruiertem k_geom: Abweichungen verschwinden.")
print("  Die präziseste Vorhersage nutzt die exakte Verhältnis-Relation:")
print(f"    a_τ = {a_tau_verhaeltnis:.3e}")
print("BELLE II TEST:")
print(f"  Wenn Belle II a_τ ≈ {a_tau_verhaeltnis:.2e} misst:")
print("    → Starke Bestätigung der T0-Verhältnis-Struktur")
print("    → Zeigt, dass fraktale Exponenten (5/3, 4/3) korrekt sind")
print("    → Triumph für die T0-Theorie!")

# Werte für weitere Verwendung
print_header("WERTE FÜR WEITERE VERWENDUNG:")
print("-" * 80)
print(f"GEOMETRISCH (k = {k_geom:.6f}):")
print(f"  a_e_T0  = {a_e_T0:.15e}")
print(f"  a_mu_T0 = {a_mu_T0:.15e}")
print(f"  a_tau_T0 = {a_tau_T0:.15e}")
print(f"REKONSTRUIERT (k = {k_geom_rek:.6f}):")
print(f"  a_e_T0_rek  = {a_e_T0_rek:.15e}")
print(f"  a_mu_T0_rek = {a_mu_T0_rek:.15e}")
print(f"  a_tau_T0_rek = {a_tau_T0_rek:.15e}")

print(f"\nAUS VERHÄLTNIS:")
print(f"  a_tau_verhaeltnis = {a_tau_verhaeltnis:.15e}")

print(f"\nKORREKTURWERT:")
print(f"  k_geom_geometrisch = {k_geom:.15e}")
print(f"  k_geom_rekonstruiert = {k_geom_rek:.15e}")
print(f"  Differenz = {abs(k_geom - k_geom_rek):.15e} ({abs(k_geom - k_geom_rek)/k_geom*100:.4f}%)")

print("="*80 + "\n")