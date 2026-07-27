#!/usr/bin/env python3
"""
FFGFT Dok. 310 — Higgs-Formel als zweiter unabhaengiger xi-Zugang
Prueft: xi = m_h^2/(64 pi^3 v^2) trifft xi = 4/30000 aus dem Vakuum-Sektor.
Eingaben: Higgs-Masse, Vakuumwert (gemessen). Keine freien Parameter.
"""
import math

m_h = 125.25   # GeV, Higgs-Masse
v   = 246.22   # GeV, Vakuumerwartungswert
lambda_h = m_h**2 / (2*v**2)

xi_higgs = lambda_h**2 * v**2 / (16*math.pi**3 * m_h**2)
xi_geom  = 4/30000

print("="*60)
print(" HIGGS-ZUGANG zu xi (Vakuum-Sektor)")
print("="*60)
print(f"  m_h      = {m_h} GeV")
print(f"  v        = {v} GeV")
print(f"  lambda_h = m_h^2/(2v^2) = {lambda_h:.6f}")
print()
print(f"  xi = lambda_h^2 v^2/(16 pi^3 m_h^2) = m_h^2/(64 pi^3 v^2)")
print(f"     = {xi_higgs:.6e}")
print(f"  xi (geometrisch, 4/30000)           = {xi_geom:.6e}")
print(f"  Abweichung: {(xi_higgs/xi_geom-1)*100:+.2f}%")
print()
print("  Zwei unabhaengige Sektoren (Higgs vs. Leptonen) liefern")
print("  dasselbe xi auf ~2%. Das ist Querverankerung, kein Fit.")
print()
print(f"  Der Nenner 64 pi^3 = S^2 * (2 S^3) * Kombinatorik")
print(f"  = Sphaeren-Oberflaechen der T^4-Randgeometrie.")
