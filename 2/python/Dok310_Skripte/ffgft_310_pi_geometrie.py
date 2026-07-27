#!/usr/bin/env python3
"""
FFGFT Dok. 310 — pi-Faktoren sind Sphaeren-Geometrie, keine Schleifen
Prueft: 16 pi^3 = S^2 * 2 S^3 (T^4-Randgeometrie); mu_0-4pi kuerzt sich in alpha.
Alle Eingaben CODATA. Keine freien Parameter.
"""
import math

print("="*60)
print(" pi-FAKTOREN ALS SPHAEREN-OBERFLAECHEN")
print("="*60)
S1 = 2*math.pi       # Kreis
S2 = 4*math.pi       # 2-Kugel
S3 = 2*math.pi**2    # 3-Sphaere (Rand des 4-Volumens)
print(f"  S^1 = 2 pi   = {S1:.4f}")
print(f"  S^2 = 4 pi   = {S2:.4f}")
print(f"  S^3 = 2 pi^2 = {S3:.4f}")
print()
lhs = 16*math.pi**3
rhs = S2 * (2*S3)
print(f"  16 pi^3            = {lhs:.4f}")
print(f"  S^2 * 2 S^3        = {rhs:.4f}")
print(f"  gleich? {abs(lhs-rhs) < 1e-9}")
print()
# 64 pi^4 war eine Sphaere zu viel
print(f"  64 pi^4 / 16 pi^3 = {64*math.pi**4/(16*math.pi**3):.4f} = 4 pi = S^2")
print("  -> 64 pi^4 zaehlte genau EINE 2-Sphaere zu viel.")
print()

print("="*60)
print(" mu_0: Geometrie (4 pi) x Einheit (10^-7); kuerzt sich in alpha")
print("="*60)
e    = 1.602176634e-19
c    = 2.99792458e8
hbar = 1.054571817e-34
mu_0 = 4*math.pi*1e-7
alpha_full   = e**2 * mu_0 * c / (4*math.pi*hbar)
alpha_reduced = e**2 * 1e-7 * c / hbar    # nach Kuerzung des 4 pi
print(f"  mu_0 = 4 pi x 10^-7 = {mu_0:.6e}")
print(f"  alpha = e^2 mu_0 c/(4 pi hbar)      = 1/{1/alpha_full:.4f}")
print(f"  nach 4pi-Kuerzung: e^2 10^-7 c/hbar = 1/{1/alpha_reduced:.4f}")
print(f"  identisch? {abs(alpha_full-alpha_reduced) < 1e-12}")
print()
print("  Das 4 pi (Geometrie) kuerzt sich exakt gegen das 4 pi")
print("  im alpha-Nenner. Uebrig: reine Einheitenzaehlung.")

print()
print("="*60)
print(" mu_0, epsilon_0 folgen aus alpha, e, c (Dok 013)")
print("="*60)
alpha = 7.2973525693e-3
h = 2*math.pi*hbar
eps_0 = e**2/(2*alpha*h*c)
mu_0d = 2*alpha*h/(e**2*c)
print(f"  epsilon_0 = e^2/(2 alpha h c) = {eps_0:.6e} F/m")
print(f"  mu_0      = 2 alpha h/(e^2 c) = {mu_0d:.6e} N/A^2")
print(f"  eps_0 mu_0 c^2 = {eps_0*mu_0d*c**2:.6f}  (= 1)")
print("  -> beide sind KEINE unabhaengigen Konstanten.")
