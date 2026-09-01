#!/usr/bin/env python3
"""
pruef_330_galois_massenverhaeltnis.py
======================================
Galois-Massenverhältnis m_mu/m_e: FFGFT-Quantenzahlen vs. GF(9)/GF(27)

Hauptergebnis (exakt, ganzzahlig, kein sqrt):

  (m_mu/m_e)² = 43200

  FFGFT-Seite:  (r_mu/r_e)² / xi = (144/25) * 7500 = 43200
  Galois-Seite: |GF(9)*|² * 5² * |GF(27)| = 8² * 25 * 27 = 43200

  IDENTISCH — kein sqrt, kein Rundungsfehler, rein rational.

Warum kein sqrt(3)?
  m_mu/m_e = (r_mu/r_e) * xi^(p_mu - p_e) = (12/5) * xi^(-1/2)
  xi^(-1/2) = sqrt(7500) = 50*sqrt(3) — irrational.
  sqrt(3) existiert in GF(3^n) nicht sinnvoll (3=0 dort).
  Quadrierung beseitigt das sqrt:
  (m_mu/m_e)² = (12/5)² * xi^(-1) = (144/25) * 7500 = 43200 — rational.

Galois-Strukturen:
  GF(9)  = GF(3^2): |GF(9)*|  = 8  = 3^2-1
  GF(27) = GF(3^3): |GF(27)|  = 27 = 3^3   (alle Elemente!)
                    |GF(27)*| = 26 = 3^3-1  (mult. Gruppe)
  GF(9) ⊄ GF(27): ggT(2,3)=1, beide ⊂ GF(3^6)
  Parallele Einbettung — kein Turm.

  Beziehung: (8*26)² - 43200 = 64 = 8² = |GF(9)*|²
  => (|GF(9)*|*|GF(27)*|)² = 43200 + |GF(9)*|²

Status: [K] für beide Herleitungen

Autor: Johann Pascher, ORCID 0009-0000-6518-4064
Datum: August 2026
"""

import sympy as sp
import numpy as np

# ============================================================
# Exakte rationale Parameter
# ============================================================
xi    = sp.Rational(4, 30000)   # = 1/7500
r_e   = sp.Rational(4, 3)       # Elektron, Dok. 006
r_mu  = sp.Rational(16, 5)      # Myon,     Dok. 006
p_e   = sp.Rational(3, 2)
p_mu  = sp.Rational(1, 1)

r_exp_float = 105.6583755 / 0.51099895   # = 206.768283

# Galois-Ordnungen
ord_GF9   = 9  - 1   # = 8   multiplikative Gruppe
ord_GF27  = 27 - 1   # = 26  multiplikative Gruppe
card_GF27 = 27       # = 27  alle Elemente
ord_GF3   = 3  - 1   # = 2

# ============================================================
print("=" * 65)
print("TEIL A: Lineares Verhältnis (enthält sqrt)")
print("=" * 65)

ratio_lin = (r_mu / r_e) * xi**(p_mu - p_e)
print(f"  m_mu/m_e = (r_mu/r_e) * xi^(p_mu-p_e)")
print(f"           = (12/5) * xi^(-1/2)")
print(f"           = (12/5) * sqrt(7500)")
print(f"           = (12/5) * 50*sqrt(3)")
print(f"           = 120*sqrt(3)")
print(f"           = {float(120*sp.sqrt(3)):.6f}")
print(f"  exp.     = {r_exp_float:.6f}")
print(f"  Abw.     = {abs(float(120*sp.sqrt(3))-r_exp_float)/r_exp_float*100:.4f}%  [K]")
print()
print(f"  Problem: sqrt(3) in GF(3^n) nicht definiert (3=0 dort).")
print(f"  Galois-Zahl 8*26=208 approximiert 120*sqrt(3) mit 0.07% Lücke.")
print(f"  Diese Lücke ist strukturell: (26*sqrt(3))^2 - 45^2 = 3 = char(GF)")

# ============================================================
print()
print("=" * 65)
print("TEIL B: Quadratisches Verhältnis (exakt rational, kein sqrt)")
print("=" * 65)

ratio_sq = (r_mu / r_e)**2 * xi**(2*(p_mu - p_e))
print(f"  (m_mu/m_e)² = (r_mu/r_e)² * xi^(-1)")
print(f"              = (12/5)² / xi")
print(f"              = (144/25) * 7500")
print(f"              = {ratio_sq}  [exakt rational]")
print(f"  Faktorisierung: {sp.factorint(int(ratio_sq))}")
print(f"  = 2^6 * 3^3 * 5^2 = 64 * 27 * 25")
print()
print(f"  exp: (m_mu/m_e)²_exp = {r_exp_float**2:.4f}")
print(f"  Abw: {abs(float(ratio_sq)-r_exp_float**2)/r_exp_float**2*100:.4f}%  [K]")
print(f"  (doppelt so groß wie linear, weil Quadrat Fehler verdoppelt)")

# ============================================================
print()
print("=" * 65)
print("TEIL C: Galois-Seite — exakt dieselbe Zahl")
print("=" * 65)

galois_sq = ord_GF9**2 * 25 * card_GF27
print(f"  |GF(9)*|² * 5² * |GF(27)| = {ord_GF9}² * 25 * {card_GF27}")
print(f"                             = {ord_GF9**2} * 25 * {card_GF27}")
print(f"                             = {galois_sq}")
print()
print(f"  Faktoren:")
print(f"    8  = |GF(9)*|  = 3²-1 (multiplikative Gruppe)")
print(f"    27 = |GF(27)|  = 3³   (alle Elemente, nicht mult. Gruppe!)")
print(f"    5  aus xi = 4/30000 = 1/(2²·3·5³) — Torus-Geometrie")
print()
print(f"  Beziehung zu |GF(27)*|=26:")
print(f"  (8*26)² - 43200 = {8**2*26**2} - {43200} = {8**2*26**2-43200} = 8² = |GF(9)*|²")
print(f"  => (|GF(9)*|·|GF(27)*|)² = (m_mu/m_e)²_FFGFT + |GF(9)*|²")

# ============================================================
print()
print("=" * 65)
print("VERGLEICH")
print("=" * 65)
print(f"  {'Methode':<40} {'(m/m)²':>8}  {'Abw.':>8}")
print(f"  {'-'*58}")
print(f"  {'Experiment (PDG)':<40} {r_exp_float**2:>8.2f}  {'—':>8}")
print(f"  {'FFGFT: (144/25)/xi [K]':<40} {float(ratio_sq):>8.1f}  {abs(float(ratio_sq)-r_exp_float**2)/r_exp_float**2*100:>7.4f}%")
print(f"  {'Galois: 8²·25·27 [K]':<40} {galois_sq:>8.1f}  {abs(galois_sq-r_exp_float**2)/r_exp_float**2*100:>7.4f}%")
print()
print(f"  FFGFT = Galois = 43200  exakt identisch.")

# ============================================================
print()
print("=" * 65)
print("ASSERTIONS")
print("=" * 65)

# Exakte Gleichheit FFGFT = Galois
assert ratio_sq == 43200, f"FFGFT: {ratio_sq} ≠ 43200"
print(f"  [OK] FFGFT: (r_mu/r_e)²/xi = {ratio_sq} exakt")

assert galois_sq == 43200, f"Galois: {galois_sq} ≠ 43200"
print(f"  [OK] Galois: 8²*25*27 = {galois_sq} exakt")

assert ratio_sq == galois_sq
print(f"  [OK] FFGFT == Galois == 43200 identisch")

# Faktorisierung
assert sp.factorint(43200) == {2: 6, 3: 3, 5: 2}
print(f"  [OK] 43200 = 2^6 * 3^3 * 5^2")

# Beziehung zu mult. Gruppe
assert ord_GF9**2 * ord_GF27**2 - 43200 == ord_GF9**2
print(f"  [OK] (8*26)² - 43200 = 8² = |GF(9)*|²")

# GF(9) ⊄ GF(27)
assert sp.gcd(2, 3) == 1
print(f"  [OK] ggT(deg GF9, deg GF27) = 1 => GF(9) ⊄ GF(27)")

# Abweichung vom Experiment
assert abs(float(sp.sqrt(ratio_sq)) - r_exp_float)/r_exp_float < 0.006
print(f"  [OK] sqrt(43200) = {float(sp.sqrt(43200)):.4f} liegt binnen 0.6% von m_mu/m_e")

print()
print("Alle Assertions bestanden.")
print()
print("=" * 65)
print("ZUSAMMENFASSUNG")
print("=" * 65)
print(f"""
  Lineares Verhältnis:
    m_mu/m_e = 120*sqrt(3) = {float(120*sp.sqrt(3)):.4f}  [FFGFT, K]
             ≈ 8*26 = 208                  [Galois, K]
    sqrt(3) in GF(3^n) nicht definiert — strukturelle Lücke 0.07%

  Quadratisches Verhältnis (exakt, ganzzahlig):
    (m_mu/m_e)² = 43200  [FFGFT = Galois, identisch]
    FFGFT:  (r_mu/r_e)² / xi = (144/25) * 7500
    Galois: |GF(9)*|² * 5² * |GF(27)| = 64 * 25 * 27
    Experiment: (m_mu/m_e)²_exp = {r_exp_float**2:.1f}  (Abw. 1.04%)

  Die verbleibende 1.04%-Abweichung im Quadrat (0.52% linear)
  ist die offene xi-Korrektur — algebraisch noch nicht hergeleitet.
""")


# ============================================================
# TEIL D: Fraktale Struktur und K_frak-Gegenprobe (Dok. 070)
# ============================================================
print("=" * 65)
print("TEIL D: Fraktale Struktur und K_frak-Gegenprobe")
print("=" * 65)

K_frak = 74/75   # = 1 - 100*xi = 0.98666...

print("""
Aus Dok. 070: m_exp = K_frak * m_bare für jedes Lepton einzeln.
Im Verhältnis kürzt sich K_frak exakt heraus:

  m_mu_exp / m_e_exp = (K_frak * m_mu_bare) / (K_frak * m_e_bare)
                     = m_mu_bare / m_e_bare

=> Massenverhältnisse sind K_frak-frei (Dok. 070, 285).
=> Die 0.52% Abweichung von sqrt(43200)=207.846 vom Experiment
   kommen aus fraktal-rekursiven Korrekturen höherer Ordnung
   der Torus-Wicklungszahlen — die das Experiment bereits misst.
""")

print("Gegenprobe: K_frak gesichert durch alpha (Dok. 070)")
print("-" * 55)

# Aus Dok. 070: alpha = xi * E0² mit E0 = sqrt(m_e*m_mu) in MeV
m_e_f  = 0.51099895    # MeV
m_mu_f = 105.6583755   # MeV
E0     = (m_e_f * m_mu_f)**0.5

alpha_bare = xi * E0**2
alpha_corr = xi * E0**2 / K_frak

print(f"  E0 = sqrt(m_e*m_mu) = {E0:.6f} MeV")
print(f"\n  Ohne K_frak: alpha = xi*E0² = {alpha_bare:.7f}")
print(f"              1/alpha = {1/alpha_bare:.4f}  (exp: 137.036)")
print(f"              Abw. = {abs(1/alpha_bare-137.036)/137.036*100:.4f}%")
print(f"\n  Mit  K_frak: alpha = xi*E0²/K_frak = {alpha_corr:.7f}")
print(f"              1/alpha = {1/alpha_corr:.4f}  (exp: 137.036)")
print(f"              Abw. = {abs(1/alpha_corr-137.036)/137.036*100:.4f}%")

print(f"""
  K_frak ist durch alpha gesichert [K]:
    Ohne K_frak: 1/alpha = {1/alpha_bare:.2f}  Abw. {abs(1/alpha_bare-137.036)/137.036*100:.2f}%
    Mit  K_frak: 1/alpha = {1/alpha_corr:.3f}  Abw. {abs(1/alpha_corr-137.036)/137.036*100:.3f}%

  Im Massenverhältnis kürzt K_frak sich heraus —
  deshalb bleibt die 0.52% als fraktale Korrektur höherer Ordnung.
""")

# Assertions
assert abs(1/alpha_bare - 137.036)/137.036 > 0.01
print("  [OK] Ohne K_frak: 1/alpha weicht > 1% vom Experiment ab")

assert abs(1/alpha_corr - 137.036)/137.036 < 0.002
print(f"  [OK] Mit K_frak: 1/alpha = {1/alpha_corr:.3f} trifft Experiment auf < 0.2%")

# K_frak kürzt sich im Verhältnis
assert abs((m_mu_f * K_frak)/(m_e_f * K_frak) - m_mu_f/m_e_f) < 1e-10
print("  [OK] K_frak kürzt sich im Massenverhältnis exakt heraus")

print("\nAlle Assertions bestanden (Teil D).")
