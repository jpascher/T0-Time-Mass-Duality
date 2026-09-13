"""
pruef_363b_luecken.py
Dok. 363 — Ergänzende Prüfungen (schließt drei Lücken aus pruef_363_hodge_t4z3.py)
Johann Pascher, 13. Sept. 2026

  L1: Ordnungsklassifikation der 8 irreduziblen Kubiken über GF(3)
      (direkt berechnet, nicht aus Dok. 342 übernommen)
  L2: Frobenius x→x³ ist Homomorphismus für ALLE 26×26 = 676 Paare
  L3: GF(3)-Negation e→-e schickt Ordnung-26-Orbits auf Ordnung-13-Orbits
      (also: warum die Sektorpaarung k↔-k Inversion sein muss, nicht Negation)
"""

import sys
from itertools import product

PASS = 0
FAIL = 0

def check(name, cond, info=""):
    global PASS, FAIL
    if cond:
        print(f"  OK  {name}")
        PASS += 1
    else:
        print(f"FAIL  {name}  {info}")
        FAIL += 1

# ============================================================
# Allgemeine GF(27)-Arithmetik mit beliebigem Reduktionspolynom
# ============================================================

def make_gf27(modpoly):
    """
    modpoly: [c0, c1, c2] für x³ + c2·x² + c1·x + c0 (monisch)
    Gibt (mul, pow, one, elements) zurück.
    """
    c0, c1, c2 = modpoly

    def mul(a, b):
        r = [0]*5
        for i in range(3):
            for j in range(3):
                r[i+j] = (r[i+j] + a[i]*b[j]) % 3
        # x³ = -c2·x² - c1·x - c0
        # x⁴ = x·x³
        for deg in (4, 3):
            lead = r[deg]
            if lead == 0:
                continue
            r[deg] = 0
            # x^deg = x^(deg-3) · x³ = x^(deg-3)·(-c2 x² - c1 x - c0)
            s = deg - 3
            r[s+2] = (r[s+2] - lead*c2) % 3
            r[s+1] = (r[s+1] - lead*c1) % 3
            r[s]   = (r[s]   - lead*c0) % 3
        return tuple(r[:3])

    def pw(a, n):
        result = (1, 0, 0)
        base = tuple(a)
        while n > 0:
            if n & 1:
                result = mul(result, base)
            base = mul(base, base)
            n >>= 1
        return result

    elements = [t for t in product(range(3), repeat=3) if t != (0, 0, 0)]
    return mul, pw, (1, 0, 0), elements

def order_of(e, mul, pw, one):
    for n in (1, 2, 13, 26):
        if pw(e, n) == one:
            return n
    return -1

# ============================================================
# L1: Ordnungsklassifikation der 8 irreduziblen Kubiken
# ============================================================
print("\n--- L1: Ordnung der 8 irreduziblen Kubiken (direkt berechnet) ---")

irred = []
for c2 in range(3):
    for c1 in range(3):
        for c0 in range(3):
            # Nullstellentest in GF(3)
            has_root = any((r**3 + c2*r*r + c1*r + c0) % 3 == 0 for r in range(3))
            if not has_root:
                irred.append((c0, c1, c2))

check("Genau 8 irreduzible monische Kubiken", len(irred) == 8, f"got {len(irred)}")

def poly_str(c0, c1, c2):
    s = "x³"
    if c2: s += f" + {c2}x²"
    if c1: s += f" + {c1}x"
    if c0: s += f" + {c0}"
    return s

ord26 = []
ord13 = []
for (c0, c1, c2) in irred:
    mul, pw, one, _ = make_gf27((c0, c1, c2))
    x = (0, 1, 0)
    o = order_of(x, mul, pw, one)
    # Zusätzlich prüfen: das Polynom ist wirklich irreduzibel, d.h. x erzeugt
    # einen Körper mit 27 Elementen (x^26 = 1 muss gelten)
    check(f"  {poly_str(c0,c1,c2):22s} x^26 = 1", pw(x, 26) == one)
    if o == 26:
        ord26.append((c0, c1, c2))
    elif o == 13:
        ord13.append((c0, c1, c2))
    print(f"      → ord(x) = {o}")

check("4 Polynome mit ord(x) = 26 (primitiv)", len(ord26) == 4, f"got {len(ord26)}")
check("4 Polynome mit ord(x) = 13", len(ord13) == 4, f"got {len(ord13)}")
check("Keine anderen Ordnungen", len(ord26) + len(ord13) == 8)

# Die vier Polynome aus Dok. 342/343 (kanonische Tabelle) müssen primitiv sein:
# f1 = x³+2x+1, f2 = x³+2x²+1, f3 = x³+2x²+x+1, f4 = x³+x²+2x+1
canon = {
    "f1": (1, 2, 0),
    "f2": (1, 0, 2),
    "f3": (1, 1, 2),
    "f4": (1, 2, 1),
}
for name, coeffs in canon.items():
    check(f"{name} = {poly_str(*coeffs)} ist primitiv (Ord. 26)", coeffs in ord26)

# ============================================================
# L2: Frobenius-Homomorphismus für alle 676 Paare
# ============================================================
print("\n--- L2: Frobenius x→x³ Homomorphismus, alle 26×26 Paare ---")

mul, pw, one, nz = make_gf27((1, 2, 0))   # f1 als Reduktionspolynom
frob = {e: pw(e, 3) for e in nz}

# Wohldefiniert: Bild liegt in GF(27)*
check("Frobenius-Bild ⊂ GF(27)*", all(v in nz for v in frob.values()))

# Multiplikativ
bad_mul = [(a, b) for a in nz for b in nz if mul(frob[a], frob[b]) != frob[mul(a, b)]]
check("Frob(a·b) = Frob(a)·Frob(b) für alle 676 Paare", len(bad_mul) == 0,
      f"{len(bad_mul)} Verstöße")

# Additiv (Frobenius ist Ringautomorphismus, also auch additiv)
def add(a, b):
    return tuple((a[i] + b[i]) % 3 for i in range(3))
zero = (0, 0, 0)
all27 = [zero] + nz
frob_full = {e: pw(e, 3) if e != zero else zero for e in all27}
bad_add = [(a, b) for a in all27 for b in all27
           if frob_full[add(a, b)] != add(frob_full[a], frob_full[b])]
check("Frob(a+b) = Frob(a)+Frob(b) für alle 729 Paare", len(bad_add) == 0,
      f"{len(bad_add)} Verstöße")

# Ordnung des Frobenius = 3 (Gal(GF(27)/GF(3)) ≅ Z₃)
frob3 = {e: frob[frob[frob[e]]] for e in nz}
check("Frob³ = id (Galoisgruppe Z₃)", all(frob3[e] == e for e in nz))
check("Frob ≠ id", any(frob[e] != e for e in nz))
frob2 = {e: frob[frob[e]] for e in nz}
check("Frob² ≠ id", any(frob2[e] != e for e in nz))

# ============================================================
# L3: Negation vs. Inversion auf den Orbits
# ============================================================
print("\n--- L3: GF(3)-Negation schickt Ord.-26 → Ord.-13, Inversion nicht ---")

def orbit(e):
    o = []
    x = e
    while x not in o:
        o.append(x)
        x = frob[x]
    return tuple(sorted(o))

orbits = sorted({orbit(e) for e in nz})
check("10 Frobenius-Orbits (2 Fixpunkte + 8 Dreier)", len(orbits) == 10)

orb26 = [o for o in orbits if len(o) == 3 and order_of(o[0], mul, pw, one) == 26]
orb13 = [o for o in orbits if len(o) == 3 and order_of(o[0], mul, pw, one) == 13]
check("4 Orbits der Ordnung 26", len(orb26) == 4)
check("4 Orbits der Ordnung 13", len(orb13) == 4)

# Ordnung ist orbit-invariant
check("Ordnung ist innerhalb jedes Orbits konstant",
      all(len({order_of(e, mul, pw, one) for e in o}) == 1 for o in orbits))

neg_one = (2, 0, 0)
def neg(e): return mul(e, neg_one)
def inv(e): return pw(e, 25)

# Negation: Ord.-26-Orbit → Ord.-13-Orbit
neg_images = [tuple(sorted(neg(e) for e in o)) for o in orb26]
check("Negation bildet jeden Ord.-26-Orbit auf einen Ord.-13-Orbit ab",
      all(img in orb13 for img in neg_images))
check("Negation bildet Ord.-13-Orbits zurück auf Ord.-26-Orbits",
      all(tuple(sorted(neg(e) for e in o)) in orb26 for o in orb13))

# Inversion: Ord.-26-Orbit → Ord.-26-Orbit (anderer)
inv_images = [tuple(sorted(inv(e) for e in o)) for o in orb26]
check("Inversion bildet jeden Ord.-26-Orbit auf einen Ord.-26-Orbit ab",
      all(img in orb26 for img in inv_images))
check("Inversion hat auf Ord.-26-Orbits keinen Fixorbit",
      all(img != o for img, o in zip(inv_images, orb26)))
check("Inversion ist Involution auf den Orbits",
      all(tuple(sorted(inv(e) for e in img)) == o for img, o in zip(inv_images, orb26)))

# Konsequenz: Negation ∘ Inversion = Multiplikation mit -1 auf Inversem,
# beide Operationen sind verschieden
check("Negation ≠ Inversion als Abbildung auf GF(27)*",
      any(neg(e) != inv(e) for e in nz))

# Genau die Paarung f1↔f2, f3↔f4 (Dok. 343 Satz D) via Inversion
# Diskreter Logarithmus zur Basis x
x = (0, 1, 0)
dlog = {}
g = one
for k in range(26):
    dlog[g] = k
    g = mul(g, x)
orb_k = [frozenset(dlog[e] for e in o) for o in orb26]
expected = {frozenset({1, 3, 9}), frozenset({17, 23, 25}),
            frozenset({5, 15, 19}), frozenset({7, 11, 21})}
check("Ord.-26-Orbits = {1,3,9},{17,23,25},{5,15,19},{7,11,21}", set(orb_k) == expected)
pairs = {frozenset({frozenset(dlog[e] for e in o),
                    frozenset(dlog[inv(e)] for e in o)}) for o in orb26}
check("Inversion: f1↔f2 und f3↔f4",
      pairs == {frozenset({frozenset({1,3,9}), frozenset({17,23,25})}),
                frozenset({frozenset({5,15,19}), frozenset({7,11,21})})})

# ============================================================
print(f"\n{'='*50}")
print(f"Ergebnis: {PASS} OK, {FAIL} FAIL")
sys.exit(FAIL)
