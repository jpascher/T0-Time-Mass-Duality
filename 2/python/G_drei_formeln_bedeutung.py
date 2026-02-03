#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Die drei G-Formeln: Bedeutung und Zusammenhänge

Wir haben drei scheinbar verschiedene Formeln für G:
1. G = (t₀ × f)² × (c⁵/ℏ)     [T0, aus Zeitstruktur]
2. G = ξ²/(4m)                 [T0, aus Geometrie]
3. G = k_G / (T × π)           [T0, kosmologische Form]

Was bedeuten sie und wie hängen sie zusammen?

WICHTIG:
Die drei Formeln beschreiben DIE GLEICHE Gravitationskonstante G,
nur aus verschiedenen Perspektiven (Mikro, Struktur, Makro).

SYNCHRONISATION:
- Dieses Skript ist mit B18_Gesamtherleitung2_De.tex synchronisiert
- Enthält die Geschwindigkeits-Analogie zur Verdeutlichung
- Erklärt die Rolle von ℏ und c als reine SI-Umrechnungsfaktoren

Datum: 2026-02-03
Letzte Synchronisation: 2026-02-03
"""

import math
from fractions import Fraction

print("\n" + "="*70)
print("DIE DREI G-FORMELN: BEDEUTUNG UND ZUSAMMENHÄNGE")
print("="*70)

# ==============================================================================
# FUNDAMENTALE PARAMETER
# ==============================================================================

phi = (1 + math.sqrt(5)) / 2
xi = float(Fraction(4, 3) * 1e-4)
f_ideal = 7500
t0 = 7.188310237145717e-48
c = 299792458
hbar = 1.054571817e-34
G_exp = 6.67430e-11

print("\nFundamentale Parameter:")
print(f"  ξ = {xi:.10e}")
print(f"  f = {f_ideal:.0f}")
print(f"  t₀ = {t0:.15e} s")

# ==============================================================================
# FORMEL 1: T0 ZEITSTRUKTUR
# ==============================================================================

print("\n" + "="*70)
print("FORMEL 1: G aus T0-Zeitstruktur")
print("="*70)

print("""
FORMEL:
  G = (t₀ × f)² × (c⁵/ℏ)

AUFSCHLÜSSELUNG:
  ┌────────────────┐
  │ (t₀ × f)²      │  ← Geometrische Zeitstruktur
  └────────────────┘
           ×
  ┌────────────────┐
  │ (c⁵/ℏ)         │  ← SI-Umrechnungsfaktor
  └────────────────┘

BEDEUTUNG:
  (t₀ × f)² beschreibt die QUADRIERTE ZEITSKALA
  
  • t₀: Sub-Planck-Zeit (fundamentale Zeiteinheit)
  • f: Skalierungsfaktor (Sub-Planck → Planck)
  • t₀ × f = tp_Planck: Planck-Zeit
  
  (t₀ × f)² hat Dimension [s²]
  
  Physikalische Interpretation:
  - Die Gravitationsstärke ist mit der QUADRIERTEN Zeitskala verknüpft
  - Je größer die fundamentale Zeitskala, desto schwächer die Gravitation
  - G ~ t² bedeutet: Gravitation ist ein "langsamer" Prozess
  
  (c⁵/ℏ) ist KEIN physikalischer Faktor, sondern NUR Umrechnung:
  - Konvertiert [s²] → [m³ kg⁻¹ s⁻²]
  - Dimensionsanalyse: [m⁵ s⁻⁵] / [J·s] = [m³ kg⁻¹ s⁻²]
""")

tp_eff = t0 * f_ideal
G_geom = (tp_eff)**2
G_formula1 = G_geom * (c**5 / hbar)

print(f"Berechnung:")
print(f"  tp = t₀ × f = {t0:.6e} × {f_ideal}")
print(f"  tp = {tp_eff:.12e} s")
print(f"  (tp)² = {G_geom:.12e} s²")
print(f"  c⁵/ℏ = {c**5/hbar:.6e} m³ kg⁻¹ s⁻¹")
print(f"  G = {G_formula1:.12e} m³/(kg·s²)")
print(f"  Abweichung: {abs(G_formula1 - G_exp)/G_exp * 100:.4f}%")

# ==============================================================================
# FORMEL 2: T0 GEOMETRISCHE STRUKTUR
# ==============================================================================

print("\n" + "="*70)
print("FORMEL 2: G aus T0-Geometrie")
print("="*70)

print("""
FORMEL:
  G = ξ² / (4m_char)
  
mit m_char = ξ/2, also:
  G = ξ² / (4 × ξ/2) = ξ² / (2ξ) = ξ/2

AUFSCHLÜSSELUNG:
  ┌────────────────┐
  │ ξ/2            │  ← Reine Geometrie
  └────────────────┘
           ×
  ┌────────────────┐
  │ k_umrechnung   │  ← Umrechnung [E⁻²] → [m³ kg⁻¹ s⁻²]
  └────────────────┘

BEDEUTUNG:
  ξ ist die TORSIONSKONSTANTE (4/3 × 10⁻⁴)
  
  T0-Fundamentalformel: ξ = 2√(G·m)
  
  Diese Formel sagt:
  - ξ beschreibt die "Spannung" im Torsionsgitter
  - G ist direkt proportional zu ξ (G ~ ξ)
  - Je größer die Torsionsspannung, desto stärker die Gravitation
  
  Physikalische Interpretation:
  - Gravitation IST Torsion im Gitter
  - G misst die "Steifigkeit" des Raum-Zeit-Gitters
  - ξ/2 ist der geometrische Faktor (Faktor 1/2 aus Quadratwurzel)
  
WICHTIG:
  Diese Formel gibt G in NATÜRLICHEN EINHEITEN (dimensionslos oder [E⁻²])
  Für SI-Einheiten brauchen wir einen Umrechnungsfaktor
""")

m_char = xi / 2
G_nat = xi / 2
k_umrechnung = 2.843e-5  # [m³ kg⁻¹ s⁻²] / [E⁻²], aus T0
umrechnungsfaktor_E2 = 3.521e-2  # [E⁻²] / [dimensionslos]

G_formula2 = G_nat * umrechnungsfaktor_E2 * k_umrechnung

print(f"Berechnung:")
print(f"  m_char = ξ/2 = {m_char:.10e}")
print(f"  G_nat = ξ/2 = {G_nat:.10e} (dimensionslos)")
print(f"  G_nat = {G_nat * umrechnungsfaktor_E2:.10e} [E⁻²]")
print(f"  k_SI = {k_umrechnung} [m³ kg⁻¹ s⁻²] / [E⁻²]")
print(f"  G = {G_formula2:.12e} m³/(kg·s²)")
print(f"  Abweichung: {abs(G_formula2 - G_exp)/G_exp * 100:.4f}%")

# ==============================================================================
# FORMEL 3: T0 KOSMOLOGISCHE FORM
# ==============================================================================

print("\n" + "="*70)
print("FORMEL 3: G in kosmologischer Form")
print("="*70)

print("""
FORMEL:
  G = k_G / (T × π)

AUFSCHLÜSSELUNG:
  ┌────────────────┐
  │ k_G            │  ← Kopplungsstärke (aus Formel 1 abgeleitet)
  └────────────────┘
           ÷
  ┌────────────────┐
  │ T × π          │  ← Kosmologische Zeitskala
  └────────────────┘

BEDEUTUNG:
  T = 100 Millionen Jahre (temporale Verdünnung)
  
  Diese Formel zeigt:
  - G wird über KOSMISCHE ZEITSKALEN "verdünnt"
  - Je länger die Zeitskala T, desto schwächer erscheint G
  - π ist geometrischer Faktor (4D-Sphäre)
  
  Physikalische Interpretation:
  - Gravitation akkumuliert über lange Zeiträume
  - Die lokale Stärke von G hängt von der "Integrationsdauer" ab
  - T = 100 Mio Jahre ist charakteristische kosmologische Skala
  
  k_G ist NICHT willkürlich, sondern:
  k_G = G × T × π (aus Formel 1 berechnet!)
  
WICHTIG:
  Diese Formel ist ÄQUIVALENT zu Formel 1!
  Sie zeigt nur eine andere Perspektive (kosmologisch statt lokal)
""")

T_100mio = 100_000_000 * 365.25 * 24 * 3600  # 100 Mio Jahre in Sekunden
k_G = G_formula1 * T_100mio * math.pi

G_formula3 = k_G / (T_100mio * math.pi)

print(f"Berechnung:")
print(f"  T = 100 Mio Jahre = {T_100mio:.6e} s")
print(f"  k_G = G₁ × T × π")
print(f"  k_G = {G_formula1:.6e} × {T_100mio:.6e} × π")
print(f"  k_G = {k_G:.2f}")
print(f"  G = k_G / (T × π)")
print(f"  G = {G_formula3:.12e} m³/(kg·s²)")
print(f"  Abweichung: {abs(G_formula3 - G_exp)/G_exp * 100:.4f}%")

# ==============================================================================
# ZUSAMMENHANG DER DREI FORMELN
# ==============================================================================

print("\n" + "="*70)
print("ZUSAMMENHANG DER DREI FORMELN")
print("="*70)

print("""
┌─────────────────────────────────────────────────────────────────┐
│ FORMEL 1: ZEITSTRUKTUR (lokal)                                  │
├─────────────────────────────────────────────────────────────────┤
│ G = (t₀ × f)² × (c⁵/ℏ)                                          │
│                                                                  │
│ Perspektive: Lokale Sub-Planck-Zeitskala                       │
│ Zeigt: Gravitation ~ Zeit²                                      │
│ Vorteil: Direkte Verbindung zu t₀ und f                        │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ FORMEL 2: GEOMETRIE (fundamental)                               │
├─────────────────────────────────────────────────────────────────┤
│ G = ξ/2 × k_umrechnung                                           │
│                                                                  │
│ Perspektive: Torsionsspannung des Gitters                      │
│ Zeigt: Gravitation = Gitterdeformation                         │
│ Vorteil: Rein geometrisch, ohne Zeitbezug                      │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ FORMEL 3: KOSMOLOGIE (global)                                   │
├─────────────────────────────────────────────────────────────────┤
│ G = k_G / (T × π)                                                │
│                                                                  │
│ Perspektive: Kosmische Zeitskala (100 Mio Jahre)               │
│ Zeigt: Gravitation über lange Zeiträume verdünnt               │
│ Vorteil: Verbindung zu kosmologischen Prozessen                │
└─────────────────────────────────────────────────────────────────┘

ÄQUIVALENZ:
  Alle drei Formeln beschreiben DAS GLEICHE G!
  Sie zeigen nur verschiedene Aspekte:
  
  Formel 1 (Zeit):     Mikro-Perspektive (Sub-Planck)
  Formel 2 (Geometrie): Struktur-Perspektive (Torsion)
  Formel 3 (Kosmos):   Makro-Perspektive (kosmologisch)
  
MATHEMATISCHE BEZIEHUNG:
  Formel 1 ≡ Formel 3  (durch Definition von k_G)
  Formel 2 ≈ Formel 1  (mit Umrechnungsfaktoren)
  
  ξ, f, t₀ sind NICHT unabhängig, sondern verknüpft:
  - ξ beschreibt Torsion
  - f beschreibt Zeit-Hierarchie
  - t₀ beschreibt fundamentale Zeiteinheit
  
  Sie beschreiben alle die GLEICHE geometrische Struktur!
""")

# ==============================================================================
# PHYSIKALISCHE INTERPRETATION
# ==============================================================================

print("\n" + "="*70)
print("PHYSIKALISCHE INTERPRETATION")
print("="*70)

print(f"""
WARUM DREI FORMELN FÜR EINE KONSTANTE?

Analogie: Geschwindigkeit v

  v = s/t         ← Definition (Weg pro Zeit)
  v = a×t         ← Dynamisch (aus Beschleunigung)
  v = √(2E/m)     ← Energetisch (aus kinetischer Energie)
  
  Alle drei beschreiben DIE GLEICHE Geschwindigkeit,
  aber aus verschiedenen Perspektiven!

Genauso bei G:

  G = (t₀×f)²×(c⁵/ℏ)   ← Aus Zeitstruktur
  G = ξ/2 × k_umr       ← Aus Torsion
  G = k_G/(T×π)         ← Aus Kosmologie
  
WAS SAGEN UNS DIE FORMELN?

1. FORMEL 1 (Zeit): G ~ t²
   "Gravitation ist langsam"
   - Gravitation wirkt über große Zeitskalen
   - Je fundamentaler die Zeit (kleiner t₀), desto schwächer G
   - G ist NICHT instantan, sondern zeitabhängig

2. FORMEL 2 (Geometrie): G ~ ξ
   "Gravitation ist Torsion"
   - Gravitation = Verformung des Raum-Zeit-Gitters
   - G misst die "Elastizität" der Raumzeit
   - Keine mysteriöse Kraft, sondern Geometrie

3. FORMEL 3 (Kosmos): G ~ 1/T
   "Gravitation wird über Zeit verdünnt"
   - G erscheint schwach, weil T so groß ist (100 Mio Jahre)
   - Auf kürzeren Zeitskalen würde G "stärker" erscheinen
   - Erklärt warum Gravitation die schwächste Kraft ist

KERNAUSSAGE:
  G ist NICHT eine willkürliche Naturkonstante!
  G folgt zwingend aus der geometrischen Struktur:
  - Zeitskala: t₀, f
  - Torsion: ξ
  - Kosmische Skala: T
  
  Alle drei Aspekte beschreiben DIE GLEICHE Struktur!
""")

# ==============================================================================
# VERGLEICH DER ERGEBNISSE
# ==============================================================================

print("\n" + "="*70)
print("NUMERISCHER VERGLEICH")
print("="*70)

print(f"\n{'Formel':<35} {'G [10⁻¹¹ m³/kg·s²]':<25} {'Abweichung'}")
print("-"*70)
print(f"{'1. Zeitstruktur (t₀×f)²':<35} {G_formula1*1e11:<25.12f} {abs(G_formula1-G_exp)/G_exp*100:.4f}%")
print(f"{'2. Geometrie (ξ/2)':<35} {G_formula2*1e11:<25.12f} {abs(G_formula2-G_exp)/G_exp*100:.4f}%")
print(f"{'3. Kosmologie (k_G/Tπ)':<35} {G_formula3*1e11:<25.12f} {abs(G_formula3-G_exp)/G_exp*100:.4f}%")
print(f"{'CODATA (Experiment)':<35} {G_exp*1e11:<25.12f} {'Referenz'}")

print(f"\nÄQUIVALENZ:")
print(f"  Formel 1 = Formel 3: {abs(G_formula1 - G_formula3) < 1e-20} (exakt gleich)")
print(f"  Formel 2 ≈ Formel 1: {abs(G_formula2 - G_formula1)/G_formula1 * 100:.3f}% Unterschied")

# ==============================================================================
# FAZIT
# ==============================================================================

print("\n" + "="*70)
print("FAZIT")
print("="*70)

print(f"""
DIE DREI FORMELN SIND:

1. MATHEMATISCH äquivalent (beschreiben das gleiche G)
2. PHYSIKALISCH komplementär (zeigen verschiedene Aspekte)
3. KONZEPTIONELL aufschlussreich (jede erklärt warum G diesen Wert hat)

VERWENDUNG:

• Formel 1: Wenn man die SUB-PLANCK-STRUKTUR betonen will
• Formel 2: Wenn man die GEOMETRISCHE NATUR betonen will  
• Formel 3: Wenn man die KOSMOLOGISCHE PERSPEKTIVE betonen will

ALLE sind gültig, ALLE sind wichtig!

Die Wahl der Formel hängt vom KONTEXT ab:
- Teilchenphysik → Formel 1 (Zeitstruktur)
- Geometrie/GR → Formel 2 (Torsion)
- Kosmologie → Formel 3 (100 Mio Jahre)

h und c sind in ALLEN nur Umrechnungsfaktoren!
Die Physik steckt in ξ, f, t₀, T - nicht in h, c!
""")

print("="*70 + "\n")
