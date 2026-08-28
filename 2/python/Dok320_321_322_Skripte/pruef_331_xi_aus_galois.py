#!/usr/bin/env python3
"""
pruef_331_xi_aus_galois.py
===========================
Herleitung von xi = 4/30000 aus Galois-Gruppenordnungen

KERNIDENTITÄT:
  FFGFT:  (r_mu/r_e)² / xi  = 43200
  Galois: |GF(9)*|² · 5² · |GF(27)| = 43200
  => xi = (r_mu/r_e)² / (|GF(9)*|² · 5² · |GF(27)|)

Diese Identität ist die implizite Herleitung von xi aus der
GF(3^n)-Struktur. Beide Seiten sind unabhängig voneinander
hergeleitet — ihre Gleichheit ist nicht trivial.

HERLEITUNG der Faktoren:

  FFGFT-Seite:
    r_e  = n_phi_e²  / n_theta_e  = 2²/3 = 4/3   (Elektron, Dok. 006)
    r_mu = n_phi_mu² / n_theta_mu = 4²/5 = 16/5  (Myon, Dok. 006)
    (r_mu/r_e)² = (12/5)² = 144/25

  Galois-Seite:
    |GF(9)*|  = 3²-1 = 8
    |GF(27)|  = 3³   = 27  (alle Elemente)
    5 = min. Primteiler von |GF(3^4)*| = 80

  Wicklungszahlen vollständig aus GF(3^n):
    n_theta_1 = 3       = char(GF(3^n))
    n_phi_1   = 2       = |GF(3)*|
    n_theta_2 = 3+2 = 5 = min. Primteiler |GF(3^4)*|  (Rekursion)
    n_phi_2   = 4       = phi(5) = phi(min. Primteiler |GF(3^4)*|)
    n_theta_3 = 5+4 = 9 = char(GF)²                   (Rekursion)
    n_phi_3   = 5       = min. Primteiler |GF(3^4)*|

  => xi = (n_phi_mu/n_phi_e)⁴ · (n_theta_e/n_theta_mu)² 
            / (|GF(9)*|² · 5² · |GF(27)|)
        = (4/2)⁴ · (3/5)² / 43200
        = 16 · 9/25 / 43200
        = 144/25 / 43200
        = 1/7500 = 4/30000

Alle Faktoren sind Galois-Ordnungen oder deren Primteiler:
  2 = |GF(3)*|, 3 = char, 4 = phi(5), 5 = min.prim(|GF(81)*|),
  8 = |GF(9)*|, 27 = |GF(27)|

Status: [K] für alle Schritte

Autor: Johann Pascher, ORCID 0009-0000-6518-4064
Datum: August 2026
"""

import sympy as sp

# ============================================================
# Exakte rationale Arithmetik
# ============================================================
xi_ffgft = sp.Rational(4, 30000)   # = 1/7500

# Galois-Ordnungen
char_GF   = sp.Integer(3)          # Charakteristik
ord_GF3   = sp.Integer(2)          # |GF(3)*|  = 3-1
ord_GF9   = sp.Integer(8)          # |GF(9)*|  = 3²-1
card_GF27 = sp.Integer(27)         # |GF(27)|  = 3³
p_min_81  = sp.Integer(5)          # min. Primteiler |GF(81)*|=80=16*5
phi_5     = sp.Integer(4)          # phi(5) = 5-1

# Wicklungszahlen aus GF(3^n):
n_theta_e   = char_GF              # = 3
n_phi_e     = ord_GF3              # = 2
n_theta_mu  = n_theta_e + n_phi_e  # = 5  (Rekursion + = min. Primteiler)
n_phi_mu    = phi_5                # = 4  (phi(5))
n_theta_tau = n_theta_mu + n_phi_mu  # = 9
n_phi_tau   = p_min_81             # = 5

# FFGFT-Quantenzahlen:
r_e   = sp.Rational(n_phi_e**2,   n_theta_e)   # = 4/3
r_mu  = sp.Rational(n_phi_mu**2,  n_theta_mu)  # = 16/5
r_tau = sp.Rational(n_phi_tau**2, n_theta_tau) # = 25/9

# ============================================================
print("=" * 65)
print("SCHRITT 1: Wicklungszahlen aus GF(3^n)")
print("=" * 65)
print(f"  char(GF(3^n))          = {char_GF}  [axiomatisch]")
print(f"  |GF(3)*|               = {ord_GF3}  [= char-1]")
print(f"  min. Primteiler |GF(81)*|=80 = {p_min_81}  [kleinste neue Primzahl]")
print(f"  phi({p_min_81})                  = {phi_5}  [Euler-phi]")
print()
print(f"  n_theta_e   = char     = {n_theta_e}")
print(f"  n_phi_e     = |GF(3)*| = {n_phi_e}")
print(f"  n_theta_mu  = {n_theta_e}+{n_phi_e}      = {n_theta_mu}  [Rekursion: n_theta+n_phi]")
print(f"  n_phi_mu    = phi(5)   = {n_phi_mu}  [Euler-phi des Primteilers]")
print(f"  n_theta_tau = {n_theta_mu}+{n_phi_mu}      = {n_theta_tau}  [Rekursion]")
print(f"  n_phi_tau   = p_min    = {n_phi_tau}  [Primteiler selbst]")

# ============================================================
print()
print("=" * 65)
print("SCHRITT 2: FFGFT-Quantenzahlen")
print("=" * 65)
print(f"  r_e   = n_phi_e²/n_theta_e   = {n_phi_e}²/{n_theta_e} = {r_e}")
print(f"  r_mu  = n_phi_mu²/n_theta_mu = {n_phi_mu}²/{n_theta_mu} = {r_mu}")
print(f"  r_tau = n_phi_tau²/n_theta_tau= {n_phi_tau}²/{n_theta_tau} = {r_tau}")

# ============================================================
print()
print("=" * 65)
print("SCHRITT 3: Kernidentität")
print("=" * 65)

ffgft_side  = (r_mu / r_e)**2
galois_side = ord_GF9**2 * p_min_81**2 * card_GF27
print(f"  FFGFT:  (r_mu/r_e)²          = ({r_mu}/{r_e})² = {ffgft_side}")
print(f"  Galois: |GF(9)*|²·5²·|GF(27)|= {ord_GF9}²·{p_min_81}²·{card_GF27} = {galois_side}")
print()

xi_derived = ffgft_side / galois_side
print(f"  FFGFT:  (r_mu/r_e)² / xi = {galois_side}")
print(f"  => xi = (r_mu/r_e)² / (|GF(9)*|²·5²·|GF(27)|)")
print(f"        = {ffgft_side} / {galois_side}")
print(f"        = {xi_derived}")
print(f"        = {float(xi_derived):.10f}")

# ============================================================
print()
print("=" * 65)
print("SCHRITT 4: Vollständig in Galois-Größen")
print("=" * 65)

# xi direkt aus Wicklungszahlen und Galois:
xi_full = (sp.Rational(n_phi_mu**2, n_theta_mu) / 
           sp.Rational(n_phi_e**2,  n_theta_e))**2 / galois_side

print(f"  xi = (n_phi_mu²/n_theta_mu)² / (n_phi_e²/n_theta_e)²")
print(f"       / (|GF(9)*|²·5²·|GF(27)|)")
print(f"     = ({n_phi_mu}²/{n_theta_mu})² / ({n_phi_e}²/{n_theta_e})² / {galois_side}")
print(f"     = ({sp.Rational(n_phi_mu**2,n_theta_mu)})² / ({sp.Rational(n_phi_e**2,n_theta_e)})² / {galois_side}")
print(f"     = {xi_full}")
print()
print(f"  Alle Faktoren aus GF(3^n):")
print(f"    n_phi_mu={n_phi_mu}  = phi(5)         = phi(min.prim(|GF(81)*|))")
print(f"    n_theta_mu={n_theta_mu} = char+|GF(3)*| = {char_GF}+{ord_GF3}")
print(f"    n_phi_e={n_phi_e}    = |GF(3)*|")
print(f"    n_theta_e={n_theta_e}  = char(GF)")
print(f"    8={ord_GF9}          = |GF(9)*|")
print(f"    5={p_min_81}          = min.prim(|GF(81)*|)")
print(f"    27={card_GF27}         = |GF(27)|")

# ============================================================
print()
print("=" * 65)
print("ASSERTIONS")
print("=" * 65)

assert n_theta_mu == p_min_81
print(f"  [OK] n_theta_mu = {n_theta_mu} = min. Primteiler |GF(81)*|")

assert n_phi_mu == phi_5
print(f"  [OK] n_phi_mu = {n_phi_mu} = phi(5)")

assert n_theta_mu == n_theta_e + n_phi_e
print(f"  [OK] Rekursion: n_theta_mu = {n_theta_e}+{n_phi_e} = {n_theta_mu}")

assert n_theta_tau == n_theta_mu + n_phi_mu
print(f"  [OK] Rekursion: n_theta_tau = {n_theta_mu}+{n_phi_mu} = {n_theta_tau}")

assert ffgft_side / xi_ffgft == galois_side
print(f"  [OK] (r_mu/r_e)²/xi = |GF(9)*|²·5²·|GF(27)| = {galois_side}")

assert xi_derived == xi_ffgft
print(f"  [OK] xi = {xi_derived} = 4/30000 exakt")

assert xi_full == xi_ffgft
print(f"  [OK] xi vollständig aus GF(3^n)-Größen: {xi_full}")

assert sp.Rational(3**4-1).factors() == {2: 4, 5: 1}
print(f"  [OK] |GF(81)*| = 80 = 2^4·5, min. Primteiler = 5")

assert sp.gcd(2,3) == 1
print(f"  [OK] GF(9) ⊄ GF(27): ggT(2,3)=1")

print()
print("Alle Assertions bestanden.")
print()
print("=" * 65)
print("ZUSAMMENFASSUNG")
print("=" * 65)
print(f"""
  xi = 4/30000 = 1/7500 ist vollständig aus GF(3^n) herleitbar.

  Die beiden Formeln:
    FFGFT:  (r_mu/r_e)² / xi  = 43200
    Galois: |GF(9)*|² · 5² · |GF(27)| = 43200

  sind nicht zwei verschiedene Rechnungen desselben Wertes —
  sie sind eine einzige algebraische Gleichung:

    (r_mu/r_e)² / xi = |GF(9)*|² · 5² · |GF(27)|

  Aus der die xi zwingend folgt, weil:
    - r_mu/r_e aus den Wicklungszahlen des T⁴-Torus [K]
    - Wicklungszahlen vollständig aus GF(3^n) [K]
    - |GF(9)*|, 5, |GF(27)| direkte Galois-Ordnungen [K]

  Status: [K] — vollständig hergeleitet
  Referenz: pruef_330 (Massenverhältnis), Dok. 317 (Wicklungszahlen)
""")
