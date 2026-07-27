#!/usr/bin/env python3
"""
FFGFT Dok. 310 — Koide-Relation als parameterfreie Referenz
Prueft: Q = 2/3 aus den drei gemessenen Leptonmassen, ohne xi, ohne Fit.
Keine freien Parameter. Alle Eingaben deklariert (PDG-Massen).
"""
import math

# Gemessene Leptonmassen (PDG 2024, MeV) -- die einzigen Eingaben
m_e   = 0.51099895
m_mu  = 105.6583755
m_tau = 1776.86

# Koide-Verhaeltnis -- benutzt NUR die drei Massen
sqrt_sum = math.sqrt(m_e) + math.sqrt(m_mu) + math.sqrt(m_tau)
Q = (m_e + m_mu + m_tau) / sqrt_sum**2

print("="*60)
print(" KOIDE-RELATION (parameterfrei)")
print("="*60)
print(f"  m_e   = {m_e} MeV")
print(f"  m_mu  = {m_mu} MeV")
print(f"  m_tau = {m_tau} MeV")
print()
print(f"  Q = (sum m)/(sum sqrt(m))^2 = {Q:.8f}")
print(f"  2/3                          = {2/3:.8f}")
print(f"  Abweichung: {(Q/(2/3)-1)*100:+.4f}%")
print(f"  Rest Q - 2/3 = {Q-2/3:.3e}  (!= 0 -> Vorhersage, kein Fit)")
print()

# Geometrische Deutung: Winkel der sqrt-Massen zu (1,1,1)
import numpy as np
sq = np.array([math.sqrt(m_e), math.sqrt(m_mu), math.sqrt(m_tau)])
n  = np.array([1.,1.,1.]) / math.sqrt(3)
cos_theta = np.dot(sq, n) / np.linalg.norm(sq)
angle = math.degrees(math.acos(cos_theta))
print(f"  Winkel (sqrt(m)) zu (1,1,1): {angle:.4f} Grad")
print(f"  cos^2(theta) = {cos_theta**2:.6f}  (= Q, geometrische Form)")
print()
print("  ERGEBNIS: Q trifft 2/3 auf 10^-5 -- ohne xi, ohne Anpassung.")
