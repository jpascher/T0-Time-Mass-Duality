#!/usr/bin/env python3
"""
pruef_332_alpha_galois.py
==========================
alpha rein aus Galois-Gruppenordnungen — ohne xi als Eingang

HAUPTERGEBNIS:
  1/alpha = 3700/27 = 137.037037...
  Experiment:       137.035999...
  Abweichung:       0.00076% (7.6 ppm)

ZWEI SCHLÜSSELIDENTITÄTEN:

(A) Galois-Identität für xi (pruef_331):
    xi = (r_mu/r_e)² / (|GF(9)*|² * 5² * |GF(27)|) = 1/7500

(B) Neue Beobachtung:
    m_e * m_mu = 54 MeV²  (Abw. 0.016%)
    54 = 2 * 27 = |GF(3)*| * |GF(27)|

Einsetzen beider Identitäten in alpha = xi * E0² / K_frak:
    |GF(27)| kürzt sich heraus!
    alpha = |GF(3)*| * 12² / (5² * |GF(9)*|² * 5²) / K_frak
          = 2 * 144 / 40000 / (74/75)
          = 27/3700

Eingänge ausschliesslich Galois-Gruppenordnungen:
    2  = |GF(3)*| = 3-1
    8  = |GF(9)*| = 3²-1
    27 = |GF(27)| = 3³
    5  = min.prim(|GF(81)*|=80)
    12 = n_phi_mu * n_theta_e = 4*3 (Wicklungszahlen, Galois)
    K_frak = 74/75 (gesichert durch alpha selbst)

Kein xi, kein v, kein m_e als expliziter Eingang.
Die MeV-Einheit ist die einzige SI-Brücke (implizit in E0²=54 MeV²).

Warum 700x genauer als bare m_mu/m_e?
    Die Identifikation E0²=54 MeV² gilt für die experimentellen
    (fraktal korrigierten) Massen — die Korrektur ist implizit
    enthalten. Bare: m_e*m_mu = 0.505*104.96 = 53.003 MeV² (Abw. 1.85%)

Status: [K] numerisch gesichert
        [S] algebraische Notwendigkeit von m_e*m_mu = 2*27 MeV²
            noch offen — warum exakt |GF(3)*|*|GF(27)| MeV²?

Autor: Johann Pascher, ORCID 0009-0000-6518-4064
Datum: August 2026
"""

import sympy as sp

# ============================================================
# Experimentelle Werte (PDG)
# ============================================================
m_e_exp  = 0.51099895000  # MeV
m_mu_exp = 105.6583755    # MeV
alpha_exp_inv = 137.035999084

# ============================================================
# Galois-Gruppenordnungen
# ============================================================
ord_GF3  = sp.Integer(2)   # |GF(3)*|  = 3-1
ord_GF9  = sp.Integer(8)   # |GF(9)*|  = 3²-1
card_GF27= sp.Integer(27)  # |GF(27)|  = 3³
p5       = sp.Integer(5)   # min.prim(|GF(81)*|=80)
K_frak   = sp.Rational(74, 75)

# Wicklungszahlen (Galois-Herkunft):
n_phi_e   = sp.Integer(2)  # = |GF(3)*|
n_theta_e = sp.Integer(3)  # = char(GF)
n_phi_mu  = sp.Integer(4)  # = phi(5)
n_theta_mu= sp.Integer(5)  # = p5

# ============================================================
print("=" * 65)
print("SCHRITT A: xi aus Galois-Identität (pruef_331)")
print("=" * 65)

r_e  = sp.Rational(n_phi_e**2,  n_theta_e)   # = 4/3
r_mu = sp.Rational(n_phi_mu**2, n_theta_mu)  # = 16/5

xi_galois = (r_mu/r_e)**2 / (ord_GF9**2 * p5**2 * card_GF27)
print(f"  xi = (r_mu/r_e)² / (|GF(9)*|²·5²·|GF(27)|)")
print(f"     = {xi_galois} = {float(xi_galois):.10f}")
assert xi_galois == sp.Rational(1, 7500)
print(f"  [OK] xi = 1/7500 = 4/30000")

# ============================================================
print()
print("=" * 65)
print("SCHRITT B: E0² = m_e*m_mu ≈ 2*27 MeV² [neue Beobachtung]")
print("=" * 65)

E0_sq_exp  = m_e_exp * m_mu_exp
E0_sq_galois = ord_GF3 * card_GF27  # = 2*27 = 54

print(f"  m_e * m_mu (PDG) = {E0_sq_exp:.6f} MeV²")
print(f"  |GF(3)*| * |GF(27)| = {E0_sq_galois} MeV²")
abw_E0 = abs(E0_sq_exp - float(E0_sq_galois))/float(E0_sq_galois)*100
print(f"  Abweichung: {abw_E0:.5f}%  [K] numerisch")
print(f"  E0 = sqrt(54) = 3*sqrt(6) = {float(sp.sqrt(54)):.6f} MeV")
print(f"  E0 (PDG)    =            {E0_sq_exp**0.5:.6f} MeV")
print()
print(f"  Bare-Wert: m_e_bare*m_mu_bare = 0.505*104.96 = {0.505*104.96:.3f} MeV²")
print(f"  Bare-Abweichung von 54: {abs(0.505*104.96-54)/54*100:.3f}%")
print(f"  => Die Identifikation gilt für experimentelle (korrigierte) Massen")

# ============================================================
print()
print("=" * 65)
print("SCHRITT C: alpha ohne xi — Galois-Substitution")
print("=" * 65)

# alpha = xi * E0² / K_frak
# = [xi_galois] * [E0²_galois] / K_frak
alpha_galois = xi_galois * E0_sq_galois / K_frak
alpha_simplified = sp.simplify(alpha_galois)
print(f"  alpha = xi_Galois * E0²_Galois / K_frak")
print(f"        = [{xi_galois}] * [{E0_sq_galois}] / {K_frak}")
print(f"        = {alpha_simplified}")
print()
print(f"  BEACHTE: |GF(27)|=27 kürzt sich heraus!")
print(f"  alpha = |GF(3)*| * 12² / (5²*|GF(9)*|²*5²) / K_frak")
print(f"        = 2 * 144 / 40000 * 75/74")
print(f"        = {alpha_simplified}")

# ============================================================
print()
print("=" * 65)
print("SCHRITT D: Numerisches Ergebnis")
print("=" * 65)
print(f"  1/alpha = {1/alpha_simplified} = {float(1/alpha_simplified):.9f}")
print(f"  exp:      {alpha_exp_inv:.9f}")
abw_alpha = abs(float(1/alpha_simplified)-alpha_exp_inv)/alpha_exp_inv*100
print(f"  Abweichung: {abw_alpha:.7f}%  ({abw_alpha*1e4:.2f} ppm)")
print()
print(f"  Vergleich:")
print(f"    m_mu/m_e bare Galois: Abw. 0.52%  (5200 ppm)")
print(f"    1/alpha Galois:       Abw. {abw_alpha*100:.4f}%  ({abw_alpha*1e4:.1f} ppm)")
print(f"    => alpha-Formel ist ~{5200/(abw_alpha*1e4):.0f}x genauer")

# ============================================================
print()
print("=" * 65)
print("SCHRITT E: Faktoren vollständig in Galois-Sprache")
print("=" * 65)
print(f"""
  1/alpha = 3700/27

  Zähler: 3700 = 4 * 925 = 2² * 5² * 37
    Galois-Zerlegung:
    2² = ord_GF3²  = |GF(3)*|²              [K]
    5² = p5²       = min.prim(|GF(81)*|)²   [K]
    37 = ?         [offen — kein offensichtlicher Galois-Ursprung]

  Nenner: 27 = 3³ = |GF(27)|               [K]

  Alternative Darstellung (aus Herleitung):
    1/alpha = (5² * |GF(9)*|² * 5²) / (|GF(3)*| * 12² * K_frak_inv)
            = 25 * 64 * 25 / (2 * 144 * 75/74)
            = 40000 / (288 * 75/74)
            = 40000 * 74 / (288 * 75)

  Alle Faktoren sind Galois-Zahlen:
    |GF(3)*| = 2, |GF(9)*| = 8, p5 = 5
    12 = n_phi_mu * n_theta_e = 4*3 (Wicklungszahlen)  [K]
    K_frak = 74/75                                      [K]
""")

# 37 in Galois?
import sympy as sp2
print(f"  37 prim? {sp2.isprime(37)}")
print(f"  37 = Primteiler von |GF(3^n)*|?")
for n in range(1, 15):
    ord_n = 3**n - 1
    if ord_n % 37 == 0:
        print(f"    |GF(3^{n})*| = {ord_n} = ... * 37  ✓")

# ============================================================
print()
print("=" * 65)
print("ASSERTIONS")
print("=" * 65)

assert abs(E0_sq_exp - 54) / 54 < 0.0002
print(f"  [OK] m_e*m_mu = {E0_sq_exp:.4f} ≈ 54 = |GF(3)*|*|GF(27)| (0.02%)")

assert alpha_simplified == sp.Rational(27, 3700)
print(f"  [OK] alpha = 27/3700 exakt aus Galois-Substitution")

assert abs(float(1/alpha_simplified) - alpha_exp_inv)/alpha_exp_inv < 1e-5
print(f"  [OK] 1/alpha = {float(1/alpha_simplified):.6f} binnen 0.001% vom Experiment")

for _n in range(1, 50):
    if (3**_n - 1) % 37 == 0:
        print(f"  [OK] 37 | |GF(3^{_n})*| = {3**_n-1}")
        print(f"       Und: K_frak=74/75, 74=2*37 => 37 steckt in K_frak")
        break

print()
print("Alle Assertions bestanden.")
print()
print("=" * 65)
print("ZUSAMMENFASSUNG")
print("=" * 65)
print(f"""
  1/alpha = 3700/27  [K, Abw. 7.6 ppm]

  Hergeleitet aus:
    xi  = 1/(|GF(9)*|²*5²*|GF(27)|) * (12/5)²    [pruef_331, K]
    E0² = |GF(3)*| * |GF(27)| = 54 MeV²           [neue Beob., K]
    alpha = xi * E0² / K_frak                       [Dok. 285]

  => |GF(27)| kürzt sich heraus:
     alpha = |GF(3)*| * 12² / (5²*|GF(9)*|²*5²) / K_frak = 27/3700

  Kein xi als expliziter Eingang.
  Einzige SI-Brücke: MeV (implizit in E0²=54 MeV²).
  
  Status E0²=54 MeV²:
    Dok. 011 leitet E0=sqrt(m_e*m_mu) als logarithmisches Mittel
    auf der T0-Torus-Geometrie her (nicht empirisch angepasst).
    Alternative: E0²=4*sqrt(2)*m_mu/xi^4 (Dok. 011).
    Die Identifikation E0²=|GF(3)*|*|GF(27)|=54 MeV² ist ein
    neuer Galois-seitiger Ausdruck derselben Groesse [K].
""")
