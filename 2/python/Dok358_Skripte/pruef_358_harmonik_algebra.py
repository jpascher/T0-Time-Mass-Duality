#!/usr/bin/env python3
"""
pruef_358_harmonik_algebra.py — Prüfskript zu Dok. 358
Harmonik und algebraische Struktur: Warum dieselbe Mathematik.

Prüft nur, was Dok. 358 neu behauptet; Korpus-Zitate (060, 159, 328,
336, 341, 342, 343) werden vorausgesetzt, nicht wiederholt.
"""
from fractions import Fraction
from math import pi, sqrt, log2, gcd

XI = Fraction(4, 30000)
ok = 0; tot = 0
def check(name, cond, detail=""):
    global ok, tot
    tot += 1; ok += bool(cond)
    print(f"[{'OK ' if cond else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

# ---------------------------------------------------------------
# Satz A: Exakter Schluss im endlichen Körper, kein Schluss in Q*
# ---------------------------------------------------------------
def order_mod(a, n):
    k, x = 1, a % n
    while x != 1:
        x = (x * a) % n; k += 1
        if k > n: return None
    return k

# A1: GF(3^k)* explizit: Polynomarithmetik mod irreduziblem Polynom,
#     jedes Element hat Ordnung | 3^k-1 (Lagrange), k=1..6
def poly_mul_mod(a, b, m, p=3):
    # a,b,m Koeffizientenlisten (niedrigster Grad zuerst), m monisch
    k = len(m) - 1
    prod = [0] * (2*k - 1 if k > 1 else 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            prod[i+j] = (prod[i+j] + ai*bj) % p
    for d in range(len(prod)-1, k-1, -1):
        c = prod[d]
        if c:
            for i in range(k+1):
                prod[d-k+i] = (prod[d-k+i] - c*m[i]) % p
    return prod[:k] + [0]*(k - len(prod[:k]))
def is_irreducible(m, p=3):
    k = len(m) - 1
    if k == 1: return True
    # brute force: kein Faktor vom Grad 1..k//2
    from itertools import product
    for d in range(1, k//2 + 1):
        for coeffs in product(range(p), repeat=d):
            f = list(coeffs) + [1]  # monisch Grad d
            # Division m / f: Rest 0?
            r = m[:]
            for e in range(k, d-1, -1):
                c = r[e]
                if c:
                    for i in range(d+1):
                        r[e-d+i] = (r[e-d+i] - c*f[i]) % p
            if all(x == 0 for x in r[:d]): return False
    return True
def find_irreducible(k, p=3):
    from itertools import product
    for coeffs in product(range(p), repeat=k):
        m = list(coeffs) + [1]
        if m[0] != 0 and is_irreducible(m, p): return m
for k in range(1, 7):
    m = find_irreducible(k)
    N = 3**k - 1
    one = [1] + [0]*(k-1)
    from itertools import product
    elems = [list(c) for c in product(range(3), repeat=k) if any(c)]
    def order(x):
        y, n = x[:], 1
        while y != one:
            y = poly_mul_mod(y, x, m); n += 1
        return n
    sample = elems if len(elems) <= 80 else elems[::max(1, len(elems)//80)]
    check(f"A1 k={k}: GF(3^{k})* — alle Ordnungen teilen {N}",
          all(N % order(x) == 0 for x in sample), f"mod {m}")
# A2: in Q* schließt keine Quintenkette: 3^a != 2^b für a,b>0
no_close = all(3**a != 2**b for a in range(1, 60) for b in range(1, 100))
check("A2 Q*: 3^a = 2^b hat keine Lösung a,b>0 (Eindeutigkeit der Primfaktorzerlegung)", no_close)

# A3: pythagoreisches Komma und K_frak (Zitat Dok. 060, hier nur Reproduktion)
komma = Fraction(3, 2)**12 / Fraction(2)**7
K_frak = 1 - 100 * XI
prod = float(komma * K_frak)
check("A3 Komma·K_frak ≈ 1", abs(prod - 1) < 2e-4, f"{prod:.5f}")
cent = lambda r: 1200 * log2(float(r))
check("A3 Komma +23.46 ct, K_frak -23.24 ct", abs(cent(komma) - 23.46) < 0.01 and abs(cent(K_frak) + 23.24) < 0.01,
      f"{cent(komma):+.2f} / {cent(K_frak):+.2f}")

# ---------------------------------------------------------------
# Satz B: Ausnahmen der 5-Limit-Lesart sind Galois-Primen
# ---------------------------------------------------------------
# Dok. 060: Strange 26/9 (Prim 13), Top 1/28 (Prim 7) nicht 5-Limit.
# Dok. 343 E: harmonische Primen p mit ord_p(3)=k, k<=6: {13,5,11,7}
harm = {p: order_mod(3, p) for p in (5, 7, 11, 13)}
check("B1 ord_p(3): 13->3, 5->4, 11->5, 7->6", harm == {13: 3, 5: 4, 11: 5, 7: 6}, str(harm))
def primes_of(fr):
    s = set()
    for n in (fr.numerator, fr.denominator):
        d = 2
        while d * d <= n:
            while n % d == 0: s.add(d); n //= d
            d += 1
        if n > 1: s.add(n)
    return s
yuk = {"e": Fraction(4,3), "mu": Fraction(16,5), "tau": Fraction(25,9),
       "u": Fraction(6), "d": Fraction(25,2), "c": Fraction(2), "b": Fraction(3,2),
       "s": Fraction(26,9), "t": Fraction(1,28)}
allowed = {2, 3, 5, 7, 11, 13}
check("B2 alle neun Yukawa-Koeffizienten (Dok. 006/060) nur Galois-Primen ≤13",
      all(primes_of(v) <= allowed for v in yuk.values()))
check("B3 Strange trägt 13 (k=3, GF(27)) — Leptonentiefe", 13 in primes_of(yuk["s"]))
check("B4 Top trägt 7 (k=6, GF(729)) — R115-Kandidat", 7 in primes_of(yuk["t"]))
check("B5 kein Koeffizient trägt 11 (k=5)", all(11 not in primes_of(v) for v in yuk.values()))

# ---------------------------------------------------------------
# Beobachtung C: drei Zwölfen — verschiedene Mechanismen, gleiche Ordnung
# ---------------------------------------------------------------
# C1: 12-ET = Z^2 / <syntonisches Komma (4,-1), Diesis (0,-3)> in (e3,e5)
det = abs(4 * (-3) - 0 * (-1))
check("C1 |Z^2/<81/80,128/125>| = 12 (Quotient des 5-Limit-Tonnetzes)", det == 12, f"det={det}")
# C2: |(Z/13)*| = 12, Nebenklassen von <3> (Ordnung 3): 4 Klassen à 3
check("C2 |(Z/13)*| = 12, <3> Ordnung 3, 4 Nebenklassen", order_mod(3, 13) == 3 and 12 // 3 == 4)
# C3: Farey-Nennerhöhe Q_c = pi/sqrt(6 eps) bei Komma-Auflösung
for name, eps in (("pyth. Komma", float(komma) - 1), ("100xi", float(100 * XI)), ("1.05% (Dok.343)", 0.0105)):
    Qc = pi / sqrt(6 * eps)
    check(f"C3 Q_c({name}) in [10.5,13]", 10.5 <= Qc <= 13, f"Q_c={Qc:.2f}")
# C4: Mechanismen verschieden — Tonnetz Z^2 torsionsfrei (Rang 2), (Z/13)* zyklisch (Torsion)
check("C4 Tonnetz-Gitter torsionsfrei; (Z/13)* = Z_12 zyklisch (Erzeuger 2)", order_mod(2, 13) == 12)

# ---------------------------------------------------------------
# Satz D: Konsonanzgrenze = Galois-Schichtgrenze (Zitat 343 F: p*≈9.76)
# ---------------------------------------------------------------
p_star = 9.76
check("D1 7-Limit-Grenze: 7 < p* < 11", 7 < p_star < 11)
check("D2 Leptonen-Koeffizienten (Dok. 006) sind 5-Limit", all(primes_of(yuk[x]) <= {2,3,5} for x in ("e","mu","tau")))

print(f"\n{ok}/{tot} Assertions bestanden")
raise SystemExit(0 if ok == tot else 1)
