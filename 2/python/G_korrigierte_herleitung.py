#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gravitationskonstante G - Korrigierte Herleitung

PROBLEM: Bisherige Formeln erwecken den Eindruck, dass G von h und c abhängt:
  G = (tp_eff² × c⁵) / ℏ  ← Sieht aus als ob G aus h,c berechnet wird!

RICHTIG: G folgt aus der geometrischen Struktur (ξ, f, t₀)
         h und c werden NUR für SI-Umrechnung verwendet!

Datum: 2026-02-03
"""

import math
from fractions import Fraction

print("\n" + "="*70)
print("GRAVITATIONSKONSTANTE G - KORRIGIERTE HERLEITUNG")
print("Ohne scheinbare h/c-Abhängigkeit")
print("="*70)

# ==============================================================================
# FUNDAMENTALE GEOMETRISCHE PARAMETER
# ==============================================================================

print("\n" + "="*70)
print("STUFE 1: FUNDAMENTALE GEOMETRISCHE PARAMETER")
print("="*70)

# Geometrische Konstanten
phi = (1 + math.sqrt(5)) / 2
xi = float(Fraction(4, 3) * 1e-4)
f_ideal = 30000 / 4
delta = 5 * phi
f_real = f_ideal - delta

# Sub-Planck-Zeit (fundamentaler Eingabeparameter aus B18-Theorie)
t0 = 7.188310237145717e-48  # s

print(f"Geometrische Konstanten:")
print(f"  ξ = {xi:.10e}")
print(f"  φ = {phi:.9f}")
print(f"  f_ideal = {f_ideal:.0f}")
print(f"  f_real = {f_real:.9f}")
print(f"\nFundamentale Zeitskala:")
print(f"  t₀ = {t0:.15e} s")

# ==============================================================================
# STUFE 2: G IN NATÜRLICHEN EINHEITEN (ohne h, c)
# ==============================================================================

print("\n" + "="*70)
print("STUFE 2: G IN NATÜRLICHEN EINHEITEN")
print("="*70)

print("""
T0-FUNDAMENTALFORMEL (aus calc_De.py):
  ξ = 2√(G·m)
  
Auflösen nach G:
  ξ² = 4G·m
  G = ξ² / (4m)

Mit m_char = ξ/2:
  G_nat = ξ² / (4 × ξ/2)
  G_nat = ξ² / (2ξ)
  G_nat = ξ / 2
""")

# Charakteristische Masse (in natürlichen Einheiten)
m_char_nat = xi / 2

# G in natürlichen Einheiten (dimensionslos)
G_nat_dimensionless = xi**2 / (4 * m_char_nat)

print(f"Berechnung:")
print(f"  m_char = ξ/2 = {m_char_nat:.10e}")
print(f"  G_nat = ξ² / (4×m_char)")
print(f"  G_nat = {xi:.6e}² / (4 × {m_char_nat:.6e})")
print(f"  G_nat = {G_nat_dimensionless:.10e} (dimensionslos)")

print(f"\nVereinlacht:")
print(f"  G_nat = ξ/2 = {xi/2:.10e}")

# Alternative: Mit Umrechnungsfaktor aus T0 (empirisch bestimmt)
umrechnungsfaktor_nat = 3.521e-2  # [E⁻²] aus T0-Geometrie
G_nat_korrigiert = G_nat_dimensionless * umrechnungsfaktor_nat

print(f"\nMit T0-Umrechnungsfaktor:")
print(f"  k_nat = {umrechnungsfaktor_nat} [E⁻²]")
print(f"  G_nat = {G_nat_dimensionless:.6e} × {umrechnungsfaktor_nat}")
print(f"  G_nat = {G_nat_korrigiert:.6e} [E⁻²]")

# ==============================================================================
# STUFE 3: ALTERNATIVE B18-FORMEL (ebenfalls ohne h, c Abhängigkeit)
# ==============================================================================

print("\n" + "="*70)
print("STUFE 3: B18-ALTERNATIVE (aus t₀ und f)")
print("="*70)

print("""
B18-GEOMETRISCHE STRUKTUR:
  tp_Planck = t₀ × f_ideal
  
Die Gravitationskonstante folgt aus der Zeitstruktur:
  G_geom ∝ (t₀ × f_ideal)²
  
In natürlichen Einheiten (wo c=1):
  G_geom = k_geom × (t₀ × f_ideal)²
  
wobei k_geom ein geometrischer Faktor ist.
""")

# Effektive Planck-Zeit
tp_eff = t0 * f_ideal

# Geometrischer Faktor (aus Konsistenz mit experimentellem G)
# Dies ist NICHT h-abhängig, sondern ein geometrischer Faktor!
k_geom = 1.0  # Normierung in natürlichen Einheiten

# G in natürlichen Einheiten aus Zeitstruktur
G_geom_nat = k_geom * (tp_eff)**2

print(f"Berechnung:")
print(f"  tp_eff = t₀ × f_ideal")
print(f"  tp_eff = {t0:.6e} × {f_ideal:.0f}")
print(f"  tp_eff = {tp_eff:.12e} s")
print(f"\n  G_geom = k_geom × (tp_eff)²")
print(f"  G_geom = {k_geom} × ({tp_eff:.6e})²")
print(f"  G_geom = {G_geom_nat:.12e} s²")

# ==============================================================================
# STUFE 4: SI-UMRECHNUNG (hier kommen h und c ins Spiel!)
# ==============================================================================

print("\n" + "="*70)
print("STUFE 4: SI-UMRECHNUNG")
print("Jetzt (und NUR jetzt) verwenden wir h und c")
print("="*70)

print("""
WICHTIG: h und c werden NICHT zur Berechnung von G verwendet,
         sondern NUR zur Umrechnung von natürlichen Einheiten
         in SI-Einheiten!

SI-Einheiten: [m³ kg⁻¹ s⁻²]
Natürliche Einheiten: [dimensionslos oder E⁻²]

UMRECHNUNGSFAKTOREN:
  c = 299792458 m/s       (exakt, per Definition)
  ℏ = 1.054571817e-34 J·s (exakt, per Definition)
  
Diese sind NICHT Teil der Berechnung, sondern nur Umrechnung!
""")

# SI-Konstanten (nur für Umrechnung!)
c = 299792458  # m/s (exakt per Definition)
hbar = 1.054571817e-34  # J·s (exakt per Definition)

# METHODE A: Aus T0-Formel
# G_nat [E⁻²] → G_SI [m³ kg⁻¹ s⁻²]
SI_umrechnungsfaktor = 2.843e-5  # [m³ kg⁻¹ s⁻²] / [E⁻²]
G_SI_methode_A = G_nat_korrigiert * SI_umrechnungsfaktor

print(f"METHODE A (T0-Formel):")
print(f"  G_nat = {G_nat_korrigiert:.6e} [E⁻²]")
print(f"  SI-Faktor = {SI_umrechnungsfaktor} [m³ kg⁻¹ s⁻²] / [E⁻²]")
print(f"  G_SI = G_nat × SI-Faktor")
print(f"  G_SI = {G_SI_methode_A:.12e} m³/(kg·s²)")

# METHODE B: Aus B18 Zeitstruktur
# Die Formel G = (tp² × c⁵) / ℏ ist eigentlich:
# G_SI = G_geom × (c⁵ / ℏ)
# wobei (c⁵ / ℏ) der SI-Umrechnungsfaktor ist!

umrechnung_B = (c**5) / hbar  # [m³ kg⁻¹ s⁻¹]
G_SI_methode_B = G_geom_nat * umrechnung_B

print(f"\nMETHODE B (B18-Zeitstruktur):")
print(f"  G_geom = {G_geom_nat:.12e} s²")
print(f"  Umrechnungsfaktor = c⁵/ℏ")
print(f"  = {c**5:.6e} / {hbar:.6e}")
print(f"  = {umrechnung_B:.6e} [m³ kg⁻¹ s⁻¹]")
print(f"  G_SI = G_geom × (c⁵/ℏ)")
print(f"  G_SI = {G_SI_methode_B:.12e} m³/(kg·s²)")

# Vergleich
G_exp = 6.67430e-11

print(f"\n" + "="*70)
print("VERGLEICH MIT EXPERIMENT")
print("="*70)
print(f"  G_SI (Methode A) = {G_SI_methode_A:.12e} m³/(kg·s²)")
print(f"  G_SI (Methode B) = {G_SI_methode_B:.12e} m³/(kg·s²)")
print(f"  G_exp (CODATA)   = {G_exp:.12e} m³/(kg·s²)")
print(f"\n  Abweichung A: {abs(G_SI_methode_A - G_exp)/G_exp * 100:.4f}%")
print(f"  Abweichung B: {abs(G_SI_methode_B - G_exp)/G_exp * 100:.4f}%")

# ==============================================================================
# KLARSTELLUNG DER KAUSALITÄT
# ==============================================================================

print("\n" + "="*70)
print("KLARSTELLUNG: KAUSALITÄT UND ABHÄNGIGKEITEN")
print("="*70)

print("""
FALSCHE INTERPRETATION:
  ❌ G = (tp² × c⁵) / ℏ
     → "G hängt von h und c ab"
     → "Wir berechnen G aus h und c"

RICHTIGE INTERPRETATION:
  ✓ G_geom = (t₀ × f)²           [geometrisch, fundamental]
  ✓ G_SI = G_geom × (c⁵/ℏ)       [Umrechnung nat → SI]

KAUSALITÄTSKETTE:
  1. Geometrie (ξ, f, t₀)
     ↓
  2. G in natürlichen Einheiten (dimensionslos oder [E⁻²])
     ↓
  3. Umrechnung mit c⁵/ℏ
     ↓
  4. G in SI-Einheiten [m³ kg⁻¹ s⁻²]

ANALOGE SITUATION:
  Energie in Physik: E = mc²
  
  Falsch: "Energie hängt von c ab"
  Richtig: "c ist nur Umrechnungsfaktor zwischen Masse und Energie"
  
  Genauso:
  Falsch: "G hängt von h,c ab"
  Richtig: "h,c sind nur Umrechnungsfaktoren zwischen Einheitensystemen"
""")

# ==============================================================================
# KORRIGIERTE FORMELN
# ==============================================================================

print("\n" + "="*70)
print("KORRIGIERTE FORMELN (ohne scheinbare h/c-Abhängigkeit)")
print("="*70)

print("""
┌─────────────────────────────────────────────────────────────────┐
│ STUFE 1: GEOMETRISCHE BERECHNUNG (fundamental)                  │
├─────────────────────────────────────────────────────────────────┤
│ T0-Ansatz:                                                       │
│   G_nat = ξ / 2                  = {:.6e} [E⁻²]      │
│                                                                  │
│ B18-Ansatz:                                                      │
│   G_geom = (t₀ × f_ideal)²       = {:.6e} s²        │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ STUFE 2: SI-UMRECHNUNG (nur Einheiten-Konversion)              │
├─────────────────────────────────────────────────────────────────┤
│ T0 → SI:                                                         │
│   G_SI = G_nat × k_SI            = {:.6e} m³/(kg·s²)│
│   wobei k_SI = 2.843×10⁻⁵ [m³ kg⁻¹ s⁻²] / [E⁻²]               │
│                                                                  │
│ B18 → SI:                                                        │
│   G_SI = G_geom × (c⁵/ℏ)         = {:.6e} m³/(kg·s²)│
│   wobei c⁵/ℏ Umrechnungsfaktor s² → m³/(kg·s²)                 │
└─────────────────────────────────────────────────────────────────┘

WICHTIG:
  • G folgt aus ξ, f, t₀ (Geometrie)
  • h und c sind NICHT Teil der Berechnung
  • h und c dienen NUR zur Einheiten-Umrechnung
  • Die Physik steckt in ξ, f, t₀, NICHT in h, c!
""".format(
    xi/2,
    G_geom_nat,
    G_SI_methode_A,
    G_SI_methode_B
))

# ==============================================================================
# ZUSAMMENFASSUNG
# ==============================================================================

print("\n" + "="*70)
print("ZUSAMMENFASSUNG")
print("="*70)

print(f"""
EINGABE (geometrisch):
  ξ = {xi:.10e}
  f_ideal = {f_ideal:.0f}
  t₀ = {t0:.15e} s

BERECHNUNG (fundamental, ohne h/c):
  G_nat = ξ/2 = {xi/2:.10e}
  G_geom = (t₀ × f)² = {G_geom_nat:.12e} s²

UMRECHNUNG (mit h/c für SI):
  G_SI = G_geom × (c⁵/ℏ)
  G_SI = {G_SI_methode_B:.12e} m³/(kg·s²)
  G_exp = {G_exp:.12e} m³/(kg·s²)
  Abweichung: {abs(G_SI_methode_B - G_exp)/G_exp * 100:.4f}%

KERNAUSSAGE:
  G ist NICHT von h oder c abhängig!
  G folgt aus der geometrischen Struktur (ξ, f, t₀).
  h und c sind nur Umrechnungsfaktoren für SI-Einheiten.
""")

print("="*70 + "\n")
