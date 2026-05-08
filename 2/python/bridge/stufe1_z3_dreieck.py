#!/usr/bin/env python3
"""
FFGFT — Stufe 1: Das ungestörte Z3-Dreieck

Ziel:
  Symbolisch und numerisch zeigen, dass die Adjazenzmatrix des
  einfachen, gerichteten Z3-Zyklus (drei Knoten, drei Kanten,
  Permutation 0->1->2->0) als Eigenwerte exakt die dritten
  Einheitswurzeln (1, omega, omega^2) hat — und dass damit die
  Z3-Charaktere algebraisch im Dreieck sitzen.

Das ist die Basis-Aussage:
  "Ein Z3-Dreieck IST eine 3x3-Matrix, dessen Spektrum die
   dritten Einheitswurzeln sind."

Wenn das nicht stimmt, kann der Rest des Programms nicht stimmen.
"""

import sympy as sp
import numpy as np

print("=" * 70)
print("FFGFT  —  Stufe 1: Das ungestörte Z3-Dreieck")
print("=" * 70)

# ----------------------------------------------------------------------
# 1.1  Symbolische Adjazenzmatrix des gerichteten Z3-Zyklus
# ----------------------------------------------------------------------
# Knoten 0 -> 1 -> 2 -> 0 (zyklische Permutation)
# A[i,j] = 1, wenn Kante von j nach i fuehrt
A = sp.Matrix([
    [0, 0, 1],
    [1, 0, 0],
    [0, 1, 0],
])

print("\n1.1  Adjazenzmatrix A des gerichteten Z3-Zyklus:")
sp.pprint(A)

# ----------------------------------------------------------------------
# 1.2  Charakteristisches Polynom
# ----------------------------------------------------------------------
lam = sp.symbols('lambda')
char_poly = A.charpoly(lam).as_expr()
char_poly_factored = sp.factor(char_poly, extension=[sp.exp(2*sp.pi*sp.I/3)])

print(f"\n1.2  charakteristisches Polynom:")
print(f"     det(A - lambda I) = {sp.expand(char_poly)}")
print(f"     = {char_poly_factored}")
print(f"     -> Nullstellen sind genau die Loesungen von lambda^3 = 1")
print(f"        also die dritten Einheitswurzeln.")

# ----------------------------------------------------------------------
# 1.3  Eigenwerte symbolisch
# ----------------------------------------------------------------------
eigvals_sym = A.eigenvals()
print(f"\n1.3  Eigenwerte (symbolisch):")
for v, mult in eigvals_sym.items():
    print(f"     {sp.simplify(v)}   (Vielfachheit {mult})")

# Auf Standardform bringen — Match numerisch (symbolisch sind die Formen
# verschieden, aber die Werte gleich)
omega = sp.exp(2 * sp.pi * sp.I / 3)
expected_num = {complex(sp.S.One.evalf()),
                complex(omega.evalf()),
                complex((omega**2).evalf())}
got_num      = {complex(v.evalf()) for v in eigvals_sym}

def close_set(a, b, tol=1e-10):
    return all(any(abs(x - y) < tol for y in b) for x in a) and len(a) == len(b)

match    = close_set(got_num, expected_num)
print(f"\n     Erwartet: 1, omega, omega^2  mit  omega = e^(2 pi i / 3)")
print(f"     Match:    {match}")

# ----------------------------------------------------------------------
# 1.4  Numerische Bestaetigung
# ----------------------------------------------------------------------
A_num = np.array(A.tolist(), dtype=complex)
eigvals_num = np.linalg.eigvals(A_num)
eigvals_num_sorted = sorted(eigvals_num, key=lambda z: (np.angle(z), z.real))

print(f"\n1.4  Eigenwerte (numerisch, sortiert nach Argument):")
for v in eigvals_num_sorted:
    print(f"     {v.real:+.6f} {v.imag:+.6f}j   |z| = {abs(v):.6f}   "
          f"arg = {np.degrees(np.angle(v)):+7.2f} deg")

# ----------------------------------------------------------------------
# 1.5  Z3-Charaktere
# ----------------------------------------------------------------------
print(f"\n1.5  Z3-Charaktere (von omega^k erzeugt):")
for k in range(3):
    chi_k = sp.simplify(omega**k)
    chi_k_num = complex(chi_k.evalf())
    print(f"     chi_{k}: omega^{k} = {chi_k}  ~=  "
          f"{chi_k_num.real:+.4f} {chi_k_num.imag:+.4f}j")

# ----------------------------------------------------------------------
# 1.6  Konsistenz-Tests
# ----------------------------------------------------------------------
print(f"\n1.6  Konsistenz-Tests:")

# Test 1: A^3 = I
A3 = A**3
test1 = (A3 == sp.eye(3))
print(f"     A^3 = I  ?           {test1}")

# Test 2: Spur = 0
trace = sum(eigvals_num)
test2 = abs(trace) < 1e-10
print(f"     Spur(A) = 0 ?        {test2}   (numerisch: {trace.real:+.2e})")

# Test 3: Determinante = 1 (gerichteter Zyklus, Permutation gerader Laenge n=3? Nein, n=3 ist ungerade Permutation: det = (-1)^(n-1) = +1)
det_A = sp.simplify(A.det())
test3 = (det_A == 1)
print(f"     det(A) = +1 ?        {test3}   (symbolisch: {det_A})")

# Test 4: Produkt der Eigenwerte = det
prod_eig = np.prod(eigvals_num)
test4 = abs(prod_eig - 1) < 1e-10
print(f"     prod Eigenwerte = 1? {test4}   (numerisch: {prod_eig.real:+.4f}{prod_eig.imag:+.4f}j)")

# ----------------------------------------------------------------------
# Ergebnis
# ----------------------------------------------------------------------
all_ok = match and test1 and test2 and test3 and test4
print(f"\n{'=' * 70}")
print(f"Stufe 1 — ERGEBNIS:")
print(f"   Z3-Dreieck (Graph) und 3x3-Matrix sind isomorph.")
print(f"   Spektrum = dritte Einheitswurzeln = Z3-Charaktere.")
print(f"   Alle Tests bestanden: {all_ok}")
print(f"{'=' * 70}")
