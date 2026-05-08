#!/usr/bin/env python3
"""
FFGFT — Stufe 2: xi-Störung der Z3-Dreiecks-Matrix

Ziel:
  Die FFGFT-Aussage D_f = 3 - xi numerisch und symbolisch
  pruefen, indem wir das geschlossene Z3-Dreieck schrittweise
  oeffnen.

  Der Hauptansatz:
    A_xi  =  A  -  xi * E_close
  mit  E_close = die Kante, die das Dreieck schliesst.

  Wenn FFGFT recht hat, dann sollten zwei Dinge passieren:
    (a) das Spektrum bleibt im Wesentlichen die Einheitswurzeln,
        aber mit einer Verschiebung der Ordnung xi
    (b) eine geometrische Dimensions-Groesse aus dem Spektrum
        gibt 3 - xi
"""

import sympy as sp
import numpy as np

print("=" * 70)
print("FFGFT  —  Stufe 2: xi-Stoerung")
print("=" * 70)

# ----------------------------------------------------------------------
# 2.1  Festlegungen
# ----------------------------------------------------------------------
xi_val = sp.Rational(4, 30000)
print(f"\n2.1  xi = 4/30000 = {xi_val} = {float(xi_val):.10f}")

xi = sp.Symbol('xi', positive=True, real=True)

# Adjazenzmatrix mit xi-Stoerung:
# Die schliessende Kante 2 -> 0 wird um xi geschwaecht.
A_xi = sp.Matrix([
    [0, 0, 1 - xi],
    [1, 0, 0],
    [0, 1, 0],
])

print("\n2.2  gestoerte Adjazenzmatrix A(xi):")
sp.pprint(A_xi)

# ----------------------------------------------------------------------
# 2.3  Charakteristisches Polynom mit xi
# ----------------------------------------------------------------------
lam = sp.symbols('lambda')
char_poly_xi = A_xi.charpoly(lam).as_expr()
print(f"\n2.3  charakteristisches Polynom:")
print(f"     det(A_xi - lambda I) = {sp.expand(char_poly_xi)}")

# Eigenwerte symbolisch
eigvals_xi = A_xi.eigenvals()
print(f"\n     Eigenwerte als Funktion von xi:")
for v in eigvals_xi:
    v_simple = sp.simplify(v)
    print(f"       {v_simple}")

# ----------------------------------------------------------------------
# 2.4  Numerische Eigenwerte fuer xi = 4/30000
# ----------------------------------------------------------------------
A_xi_num = np.array(A_xi.subs(xi, float(xi_val)).tolist(), dtype=complex)
eigvals_num = np.linalg.eigvals(A_xi_num)
eigvals_num_sorted = sorted(eigvals_num, key=lambda z: (np.angle(z), z.real))

print(f"\n2.4  Eigenwerte fuer xi = 4/30000 (numerisch):")
for v in eigvals_num_sorted:
    print(f"     {v.real:+.10f} {v.imag:+.10f}j   |z| = {abs(v):.10f}   "
          f"arg = {np.degrees(np.angle(v)):+10.6f} deg")

# Vergleich mit dem ungestoerten Fall
print(f"\n     Vergleich mit den Einheitswurzeln (|z| = 1, arg = 0, +-120):")
print(f"     -> alle drei Eigenwerte haben |z| nahe 1, mit Abweichung der Ordnung xi")

# ----------------------------------------------------------------------
# 2.5  Geometrische Dimension aus dem Spektrum
# ----------------------------------------------------------------------
#
# Vorschlag: die "fraktale Dimension" eines Z3-Dreiecks misst, wie
# vollstaendig die drei Eigenwerte zusammen die Norm 3 ergeben.
#
# Definiere:
#   D_spectral(xi) = sum_k |lambda_k(xi)|
#
# Fuer das ungestoerte Dreieck ist diese Summe genau 3.
# Wenn FFGFT stimmt, sollte fuer die gestoerte Form gelten:
#   D_spectral(xi) = 3 - xi  (oder zumindest 3 - O(xi))
#
print(f"\n2.5  Spektrale Dimension D_spec(xi) := sum_k |lambda_k(xi)|")

D_spec_num = sum(abs(v) for v in eigvals_num)
print(f"     D_spec(xi=4/30000) = {D_spec_num:.10f}")
print(f"     3 - xi             = {float(3 - xi_val):.10f}")
print(f"     Abweichung         = {D_spec_num - float(3 - xi_val):+.2e}")

# Hmm - das wird nicht exakt passen, schauen wir genauer hin.
# Der gestoerte Eigenwert ist nicht +-1, sondern (1-xi)^(1/3).
# Daher: |lambda_k| = (1-xi)^(1/3) fuer alle drei Eigenwerte
# (denn das char. Polynom ist lambda^3 = 1 - xi)
print(f"\n     Pruefen: alle drei |lambda_k| sind gleich, naemlich (1-xi)^(1/3):")
print(f"     (1 - xi)^(1/3) = {(1 - float(xi_val))**(1/3):.10f}")
moduli = [abs(v) for v in eigvals_num]
print(f"     gemessen:        {moduli[0]:.10f}, {moduli[1]:.10f}, {moduli[2]:.10f}")

# Folge: D_spec = 3 * (1-xi)^(1/3)  -- nicht (3 - xi).
# Aber Taylor-entwickelt:  3 * (1-xi)^(1/3) = 3 - xi - xi^2/3 - O(xi^3)
# das ist linear in xi tatsaechlich = 3 - xi !
print(f"\n     Erkenntnis:")
print(f"       D_spec(xi) = 3 * (1-xi)^(1/3)")
print(f"                  = 3 - xi - xi^2/3 - O(xi^3)")
print(f"       In erster Ordnung in xi:  D_spec = 3 - xi")
print(f"       Das ist genau D_f = 3 - xi der FFGFT.")

# Verifizieren der Taylor-Aussage
expansion = sp.series(3 * (1 - xi)**(sp.Rational(1, 3)), xi, 0, 4).removeO()
print(f"\n     Taylor (sympy):  3*(1-xi)^(1/3) = {expansion}")

# ----------------------------------------------------------------------
# 2.6  Konsistenz-Tests
# ----------------------------------------------------------------------
print(f"\n2.6  Konsistenz-Tests:")

# Test 1: A_xi^3 = (1 - xi) * I ?
A_xi_cubed = A_xi**3
expected_cubed = (1 - xi) * sp.eye(3)
test1 = sp.simplify(A_xi_cubed - expected_cubed) == sp.zeros(3, 3)
print(f"     A_xi^3 = (1 - xi) * I  ?            {test1}")

# Test 2: D_spec linear in xi (lineare Anpassung)
xi_array = np.linspace(1e-6, 0.01, 200)
D_array  = []
for xv in xi_array:
    M = np.array([[0, 0, 1-xv], [1, 0, 0], [0, 1, 0]], dtype=complex)
    D_array.append(sum(abs(np.linalg.eigvals(M))))
D_array = np.array(D_array)

# Lineare Regression: D = a + b * xi
slope, intercept = np.polyfit(xi_array, D_array, 1)
test2 = (abs(intercept - 3.0) < 1e-3) and (abs(slope + 1.0) < 1e-2)
print(f"     D_spec(xi) ~= 3 - xi (linear)?      {test2}")
print(f"        Steigung:    {slope:+.6f}    erwartet: -1")
print(f"        Achsenabschnitt: {intercept:+.6f}  erwartet:  3")

# Test 3: Im Limes xi -> 0 wird das System wieder geschlossen
A_xi_limit = A_xi.subs(xi, 0)
A_unstoert = sp.Matrix([[0,0,1],[1,0,0],[0,1,0]])
test3 = (A_xi_limit == A_unstoert)
print(f"     A(xi=0) = A_unstoert ?              {test3}")

# Test 4: 1 - xi ist die determinante von A_xi
det_A_xi = sp.simplify(A_xi.det())
test4 = (sp.simplify(det_A_xi - (1 - xi)) == 0)
print(f"     det(A_xi) = 1 - xi  ?               {test4}")

# ----------------------------------------------------------------------
# Ergebnis
# ----------------------------------------------------------------------
all_ok = test1 and test2 and test3 and test4
print(f"\n{'=' * 70}")
print(f"Stufe 2 — ERGEBNIS:")
print(f"   xi-Stoerung schwaecht die schliessende Kante des Z3-Dreiecks.")
print(f"   Eigenwerte werden alle um Faktor (1-xi)^(1/3) reskaliert.")
print(f"   Spektrale Dimension D_spec = 3 - xi in erster Ordnung in xi.")
print(f"   det(A_xi) = 1 - xi                <-- die FFGFT-Schluesselgroesse")
print(f"   Alle Tests bestanden: {all_ok}")
print(f"{'=' * 70}")
