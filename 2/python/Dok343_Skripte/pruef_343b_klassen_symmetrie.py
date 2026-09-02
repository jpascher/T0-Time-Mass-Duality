"""
pruef_343b_klassen_symmetrie.py
Offene Brücke D' aus Dok. 342/343 D: Sind die 4 primitiven Klassen f1..f4
in GF(27)* unter den FFGFT-Symmetrien verschieden?

Symmetrien auf GF(27)*:
  Frobenius  F: x -> x^3        (Z3-Rotation des Orbifolds, Dok. 336)
  Inversion  I: x -> x^{-1}     (Sektorpaarung k <-> -k, Dok. 336)
  Negation   N: x -> -x = x^13·x (Fixpunkt -1 in GF(27)*, Dok. 339)
Die Klassen sind Frobenius-Orbits; wir prüfen, wie I und N die Orbits permutieren.
Zusätzlich: Orbit-Struktur der Ordnung-13-Klassen g1..g4 und Zuordnung
der Frobenius-Konjugationsklassen zu den Charakteren von Gal(GF(27)/GF(3)).
"""
from itertools import product

# GF(27) = GF(3)[x]/(x^3 + 2x + 1)   [= f1, primitiv]
MOD = (1, 2, 0)  # x^3 = -(2x + 1) = x + 2  mod 3  -> x^3 = 1*x^1... wir rechnen generisch
# Elemente als Tripel (a0,a1,a2) = a0 + a1 x + a2 x^2

def add(a, b): return tuple((u+v) % 3 for u, v in zip(a, b))
def mul(a, b):
    # Produkt, dann reduzieren mit x^3 = x + 2  (aus x^3+2x+1=0 -> x^3 = -2x-1 = x+2)
    c = [0]*5
    for i in range(3):
        for j in range(3):
            c[i+j] = (c[i+j] + a[i]*b[j]) % 3
    # x^4 = x*x^3 = x^2 + 2x
    c[2] = (c[2] + c[4]) % 3; c[1] = (c[1] + 2*c[4]) % 3; c[4] = 0
    # x^3 = x + 2
    c[1] = (c[1] + c[3]) % 3; c[0] = (c[0] + 2*c[3]) % 3; c[3] = 0
    return (c[0], c[1], c[2])
ONE = (1, 0, 0)
def pw(a, n):
    r = ONE
    for _ in range(n): r = mul(r, a)
    return r
def order(a):
    r, k = a, 1
    while r != ONE:
        r = mul(r, a); k += 1
    return k
def inv(a): return pw(a, 25)          # a^26 = 1
def neg(a): return tuple((-u) % 3 for u in a)
def frob(a): return pw(a, 3)

# Minimalpolynom eines Elements: prod (X - a^{3^i})
def minpoly(a):
    roots = [a, frob(a), frob(frob(a))]
    # Koeffizienten von (X-r1)(X-r2)(X-r3) über GF(27), sollten in GF(3) liegen
    # e1 = sum, e2 = sum pairs, e3 = product
    e1 = add(add(roots[0], roots[1]), roots[2])
    e2 = add(add(mul(roots[0], roots[1]), mul(roots[0], roots[2])), mul(roots[1], roots[2]))
    e3 = mul(mul(roots[0], roots[1]), roots[2])
    for e in (e1, e2, e3): assert e[1] == 0 and e[2] == 0, "Koeffizient nicht in GF(3)"
    # X^3 - e1 X^2 + e2 X - e3
    return (( -e3[0]) % 3, e2[0] % 3, (-e1[0]) % 3)   # (c0, c1, c2) für X^3 + c2 X^2 + c1 X + c0

def pname(c):
    c0, c1, c2 = c
    s = "x³"
    if c2: s += f"+{c2}x²"
    if c1: s += f"+{c1}x"
    s += f"+{c0}"
    return s

x = (0, 1, 0)
assert order(x) == 26, "x sollte primitiv sein"
print("GF(27) = GF(3)[x]/(x³+2x+1),  x primitiv, ord(x) = 26\n")

# Alle Elemente nach Ordnung
elems = [e for e in product(range(3), repeat=3) if e != (0, 0, 0)]
by_order = {}
for e in elems: by_order.setdefault(order(e), []).append(e)
print("Elementzahl nach Ordnung:", {k: len(v) for k, v in sorted(by_order.items())})

print("\n" + "="*66)
print("A) Frobenius-Klassen der primitiven Elemente (Ordnung 26)")
print("="*66)
seen, classes = set(), []
for e in by_order[26]:
    if e in seen: continue
    orb = [e, frob(e), frob(frob(e))]
    seen |= set(orb); classes.append(orb)
labels = {}
for i, orb in enumerate(classes):
    mp = minpoly(orb[0]); labels[tuple(sorted(orb))] = f"f{i+1}"
    # als Potenzen von x
    exps = sorted(k for k in range(26) if pw(x, k) in orb)
    print(f"  f{i+1} = {pname(mp):18s}  Orbit = x^{exps}")

def cls_of(e):
    for orb in classes:
        if e in orb: return labels[tuple(sorted(orb))]
    return None

print("\n" + "="*66)
print("B) Wirkung von Inversion I (x→x⁻¹, Sektorpaarung k↔−k) und Negation N")
print("="*66)
for i, orb in enumerate(classes):
    e = orb[0]
    print(f"  f{i+1}:  I → {cls_of(inv(e))},   N → Ordnung {order(neg(e))} (verlässt die f-Klassen: −1 = x¹³)")

# Orbits unter der Gruppe <I, N> (Klein'sche Vierergruppe)
def group_orbit(cl):
    e = [o for o in classes if labels[tuple(sorted(o))] == cl][0][0]
    return sorted({cls_of(e), cls_of(inv(e))})   # N verlässt die Ordnung 26 (s.u.)
orbits = []
for cl in ["f1", "f2", "f3", "f4"]:
    o = group_orbit(cl)
    if o not in orbits: orbits.append(o)
print("\n  Orbits der 4 Klassen unter <I, N>:", orbits)
print(f"  → {len(orbits)} unterscheidbare Klassen, wenn die Sektorpaarung k↔−k Symmetrie ist [B].")

print("\n" + "="*66)
print("C) Dasselbe für die Ordnung-13-Klassen g1..g4")
print("="*66)
seen13, classes13 = set(), []
for e in by_order[13]:
    if e in seen13: continue
    orb = [e, frob(e), frob(frob(e))]
    seen13 |= set(orb); classes13.append(orb)
lab13 = {tuple(sorted(o)): f"g{i+1}" for i, o in enumerate(classes13)}
def cls13(e):
    for o in classes13:
        if e in o: return lab13[tuple(sorted(o))]
    return None
for i, orb in enumerate(classes13):
    e = orb[0]; mp = minpoly(e)
    print(f"  g{i+1} = {pname(mp):18s}  I → {cls13(inv(e))}   N → {cls_of(neg(e))} (Ordnung {order(neg(e))})")
print("  Negation bildet Ordnung 13 auf Ordnung 26 ab (−1 hat Ordnung 2): g-Klassen ↔ f-Klassen gepaart.")

print("\n" + "="*66)
print("D) Zuordnung zu den Charakteren von Gal(GF(27)/GF(3)) ≅ Z3  [Präzisierung Dok. 343 D]")
print("="*66)
print("  Gal = <F>, F: x→x³. Charaktere χ_j(F) = ω^j, j=0,1,2. Alle 4 Klassen sind")
print("  reguläre F-Orbits (Länge 3): F wirkt auf jedem Orbit als Zyklus, der Charakter")
print("  ist nicht von der Klasse abhängig — die Klassenunterscheidung liegt NICHT im")
print("  Galois-Charakter, sondern im diskreten Logarithmus mod 26 (Orbit x^k, k mod 26).")
print("  Die Klassen f1..f4 entsprechen den 4 Nebenklassen von <3> in (Z/26)* ≅ Z12:")
mults = sorted(k for k in range(1, 26) if __import__('math').gcd(k, 26) == 1)
sub = {1, 3, 9}
cosets = []
for k in mults:
    c = tuple(sorted({(k*s) % 26 for s in sub}))
    if c not in cosets: cosets.append(c)
for c in cosets: print("   ", c, "→", cls_of(pw(x, c[0])))
print("  (Z/26)*/<3> ≅ Z4: die vier Klassen bilden eine zyklische Gruppe der Ordnung 4;")
print("  I (k→−k) ist das Element der Ordnung 2 darin. Bestätigt B.")

print("\n" + "="*66)
print("E) Dirichlet L(s,χ₁) mod 3 — exakte Werte als Referenz (kein Fit)")
print("="*66)
import math
N = 200000
L1 = {s: sum(((1 if n % 3 == 1 else -1) / n**s) for n in range(1, N) if n % 3) for s in (1, 2, 3)}
print(f"  L(1,χ₁) = {L1[1]:.6f}   exakt π/(3√3) = {math.pi/(3*math.sqrt(3)):.6f}")
print(f"  L(2,χ₁) = {L1[2]:.6f}   (kein geschlossener Ausdruck mit π² bekannt)")
print(f"  L(3,χ₁) = {L1[3]:.6f}   exakt 4π³/(81√3) = {4*math.pi**3/(81*math.sqrt(3)):.6f}")
print("  Sektorasymmetrie Σ_{n≡1}−Σ_{n≡2} ist bei ungeradem s ein π-Ausdruck (Dok. 159:")
print("  π-Potenzen = Periodizitätssignatur); bei geradem s nicht. Deutung: offen [S].")

print("\nAlle Assertions bestanden.")
