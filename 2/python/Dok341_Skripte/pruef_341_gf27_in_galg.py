#!/usr/bin/env python3
"""
pruef_341_gf27_in_galg.py
==========================
Warum Doug Matzke kein GF(27) in GALG G(3) findet — und wo es in G(6) steckt

Anlass: Doug Matzke, IPI-Mail 1. Sept. 2026:
  "I tried to find a GF(27) in GALG, because 27-1=26 (so really didn't find any)
   gasolve([a,b,c], is_root26): Attempted 6561 with 0 found."
  Er findet GF(9) (Generator (a+ja)^8=1) und GF(81) ((1+a+b+c+a^b)^80=1 in G(3)).

Algebraischer Hintergrund:
  Z3C = GF(3)[i] = GF(9)  (i²=-1, Charakteristik 3).
  G(n) = Cl(n) über GF(9).
  Cl(3) ≅ M_2(GF(9)) ⊕ M_2(GF(9))   (n ungerade: Zentrum 2-dim)
  Cl(6) ≅ M_8(GF(9))

SATZ A (G(3)):
  Eigenwerte einer 2x2-Matrix über GF(9) liegen in GF(9²)=GF(81).
  |GF(81)*| = 80 = 2^4·5.  13 ∤ 80.
  => Kein Element von G(3) hat eine durch 13 teilbare Ordnung.
  => X^26 = 1 mit ord(X)=26 ist in G(3) UNMÖGLICH. Dougs 0/6561 ist kein
     Suchfehler, sondern algebraisch zwingend.
  Dougs Ordnungen {2,4,8,16,40,80} ⊂ Teiler(80) ✓;  3 = unipotent (char 3) ✓.

SATZ B (G(6)):
  In M_8(GF(9)) existieren Elemente der Ordnung 13 und 26:
  Companion-Matrix C_f von f(x)=x³+2x+1 (irreduzibel über GF(3), bleibt
  irreduzibel über GF(9) da ggT(3,2)=1); C_f ⊕ C_f ⊕ (-I_2) hat Ordnung 26.
  Jede 8x8-Matrix ist ein Cl(6)-Element mit Z3C-Blade-Koeffizienten
  => GF(27)-Elemente EXISTIEREN in G(6).

SATZ C (kein Teilkörper):
  GF(27) ist als unitale Unteralgebra in M_n(GF(9)) einbettbar ⟺ 3 | n.
  n=8: 3 ∤ 8  => GF(27) ist in G(6) als ELEMENT-Ordnung präsent, aber
  NICHT als Teilkörper. Das ist exakt die FFGFT-Aussage "GF(9) ⊄ GF(27),
  beide parallel in GF(729)" (pruef_330, Dok. 338).

Konsequenz für die Massenschicht:
  (m_μ/m_e)² = |GF(9)*|²·5²·|GF(27)| braucht GF(27)  (Dok. 338)
  1/α = 3700/27: |GF(27)| kürzt sich heraus — α braucht kein GF(27).
  Doug: "I'm not working on mass" — konsistent: GALG G(3) enthält kein
  GF(27), die Massenschicht ist erst in G(6) über Ordnung-26-Elemente erreichbar.

Autor: Johann Pascher, ORCID 0009-0000-6518-4064
Datum: 1. September 2026
"""
import numpy as np
import sympy as sp
from itertools import combinations
import random

# ============================================================
# GF(9) = GF(3)[i] Arithmetik: Matrizen als (re, im) int-Arrays mod 3
# ============================================================
class M9:
    """8x8 (oder nxn) Matrix über GF(9), re/im ∈ {0,1,2}"""
    def __init__(self, re, im=None):
        self.re = np.array(re, dtype=np.int64) % 3
        self.im = np.zeros_like(self.re) if im is None else np.array(im, dtype=np.int64) % 3
    @staticmethod
    def eye(n): return M9(np.eye(n, dtype=np.int64))
    @staticmethod
    def zeros(n): return M9(np.zeros((n,n), dtype=np.int64))
    def __matmul__(self, o):
        re = self.re @ o.re - self.im @ o.im
        im = self.re @ o.im + self.im @ o.re
        return M9(re, im)
    def __add__(self, o): return M9(self.re + o.re, self.im + o.im)
    def __sub__(self, o): return M9(self.re - o.re, self.im - o.im)
    def __neg__(self): return M9(-self.re, -self.im)
    def scal(self, a, b=0):  # Multiplikation mit Skalar a+bi
        return M9(a*self.re - b*self.im, a*self.im + b*self.re)
    def __eq__(self, o): return np.array_equal(self.re, o.re) and np.array_equal(self.im, o.im)
    def kron(self, o):
        re = np.kron(self.re, o.re) - np.kron(self.im, o.im)
        im = np.kron(self.re, o.im) + np.kron(self.im, o.re)
        return M9(re, im)
    def trace(self):
        return (int(np.trace(self.re)) % 3, int(np.trace(self.im)) % 3)
    def is_zero(self): return not self.re.any() and not self.im.any()

def mpow(X, k):
    n = X.re.shape[0]
    R = M9.eye(n); B = X
    while k:
        if k & 1: R = R @ B
        B = B @ B; k >>= 1
    return R

# ============================================================
# Pauli-Matrizen über GF(9) und Cl(6)-Erzeuger (8x8)
# ============================================================
I2 = M9.eye(2)
sx = M9([[0,1],[1,0]])
sy = M9([[0,0],[0,0]], [[0,2],[1,0]])   # [[0,-i],[i,0]], -1 ≡ 2
sz = M9([[1,0],[0,2]])                  # diag(1,-1)

e = [
    sx.kron(I2).kron(I2),
    sy.kron(I2).kron(I2),
    sz.kron(sx).kron(I2),
    sz.kron(sy).kron(I2),
    sz.kron(sz).kron(sx),
    sz.kron(sz).kron(sy),
]
I8 = M9.eye(8)

print("=" * 66)
print("SCHRITT 0: Cl(6) über GF(9) — Erzeuger e1..e6 (8x8)")
print("=" * 66)
for i in range(6):
    assert mpow(e[i], 2) == I8, f"e{i+1}² ≠ 1"
for i in range(6):
    for j in range(i+1, 6):
        assert (e[i]@e[j] + e[j]@e[i]).is_zero(), f"e{i+1},e{j+1} antikommutieren nicht"
print("  [OK] e_i² = +1 (Hyperbit-Signatur), e_i e_j = -e_j e_i  — Cl(6,0) über GF(9)")

# Blade-Basis (64 Blades)
blades = {}
for r in range(7):
    for S in combinations(range(6), r):
        B = I8
        for s in S: B = B @ e[s]
        blades[S] = B
assert len(blades) == 64
# B_S² = ±1 -> B_S^{-1} = ±B_S
blade_inv = {}
for S, B in blades.items():
    B2 = B @ B
    if B2 == I8: blade_inv[S] = B
    elif B2 == -I8: blade_inv[S] = -B
    else: raise RuntimeError("Blade quadriert nicht zu ±1")
print("  [OK] 64 Blades, alle B_S² = ±1")

def blade_coeffs(X):
    """X = Σ c_S B_S ; c_S = tr(X B_S^{-1})/8, 1/8 = 1/2 = 2 in GF(3)"""
    out = {}
    for S in blades:
        tr_re, tr_im = (X @ blade_inv[S]).trace()
        c = ((2*tr_re) % 3, (2*tr_im) % 3)
        if c != (0,0): out[S] = c
    return out

def fmt_c(c):
    re, im = c
    s = {0:"", 1:"+1", 2:"-1"}[re]
    t = {0:"", 1:"+i", 2:"-i"}[im]
    return (s + t) if (s or t) else "0"

def fmt_blade(S):
    return "1" if not S else "^".join(f"e{s+1}" for s in S)

# ============================================================
# Ordnungsbestimmung in GL_8(GF(9))
# ============================================================
# Exponent: lcm(9^k-1, k=1..8) * 9  (unipotenter Anteil: 3^2 ≥ 8)
N_exp = 1
for k in range(1, 9): N_exp = sp.ilcm(N_exp, 9**k - 1)
N_exp *= 9
N_fac = sp.factorint(N_exp)

def order(X):
    if not (mpow(X, N_exp) == I8): return None   # nicht invertierbar
    n = N_exp
    for p in N_fac:
        while n % p == 0 and mpow(X, n // p) == I8:
            n //= p
    return n

# ============================================================
print()
print("=" * 66)
print("SATZ A: G(3) ≅ M_2(GF(9))⊕M_2(GF(9)) — Ordnungen teilen 80·3")
print("=" * 66)
print(f"  Eigenwerte 2x2 über GF(9) ∈ GF(81);  |GF(81)*| = {9**2-1} = {sp.factorint(80)}")
print(f"  13 | 80 ?  {80 % 13 == 0}   → Ordnung 26 in G(3) unmöglich")
print(f"  Dougs gefundene Ordnungen {{2,4,8,16,40,80}} ⊂ Teiler(80) = {sp.divisors(80)}")
print(f"  Ordnung 3 = unipotent (Charakteristik 3) ✓")
print(f"  => Dougs 'Attempted 6561 with 0 found' ist algebraisch zwingend [B]")
assert 80 % 13 != 0

# Numerische Bestätigung in Cl(3) ⊂ Cl(6): span{1,e1,e2,e3, e1e2, ...}
print()
print("  Numerische Probe: 3000 Zufallselemente aus Cl(3)=span{Blades in e1,e2,e3}")
cl3_blades = [S for S in blades if all(s < 3 for s in S)]
rng = random.Random(3)
ords3 = {}
for _ in range(3000):
    X = M9.zeros(8)
    for S in cl3_blades:
        a, b = rng.randrange(3), rng.randrange(3)
        if a or b: X = X + blades[S].scal(a, b)
    o = order(X)
    if o: ords3[o] = ords3.get(o, 0) + 1
print(f"  gefundene Ordnungen in Cl(3): {sorted(ords3)}")
assert all(o % 13 != 0 for o in ords3), "13 in Cl(3)?!"
print(f"  [OK] keine Ordnung durch 13 teilbar — GF(27) fehlt in G(3) [B]")

# ============================================================
print()
print("=" * 66)
print("SATZ B: In G(6) ≅ M_8(GF(9)) existieren Elemente der Ordnung 13 und 26")
print("=" * 66)
x = sp.symbols('x')
f = sp.Poly(x**3 + 2*x + 1, x, modulus=3)   # = x³ - x + 1
print(f"  f(x) = x³+2x+1 (≡ x³-x+1) über GF(3): Nullstellen? ", end="")
roots = [v for v in range(3) if (v**3 + 2*v + 1) % 3 == 0]
print(f"{roots} → irreduzibel (Grad 3, keine Nullstelle)")
print(f"  ggT(3,2)=1 → f bleibt irreduzibel über GF(9); Wurzeln ∈ GF(27)\\GF(3)")

# Companion-Matrix von x³+2x+1: x³ = -2x - 1 = x + 2 (mod 3)
C = np.zeros((3,3), dtype=np.int64)
C[1,0] = 1; C[2,1] = 1
C[0,2] = 2; C[1,2] = 1; C[2,2] = 0      # letzte Spalte = Koeffizienten von x³ = 2 + 1·x + 0·x²
Cf = M9(C)
# Ordnung von C_f in GL_3(GF(3)) — hier über 3x3 direkt
def order_small(X, nexp, nfac):
    I = M9.eye(X.re.shape[0])
    n = nexp
    for p in nfac:
        while n % p == 0 and mpow(X, n//p) == I: n //= p
    return n
ord_Cf = order_small(Cf, 26, sp.factorint(26))
print(f"  Companion-Matrix C_f: Ordnung = {ord_Cf}   (26 = |GF(27)*| → f primitiv)")
assert ord_Cf in (13, 26)

# 8x8 Element: C_f ⊕ C_f ⊕ (-I_2)
X26 = M9.zeros(8)
X26.re[0:3,0:3] = Cf.re; X26.re[3:6,3:6] = Cf.re
X26.re[6,6] = 2; X26.re[7,7] = 2
o = order(X26)
print(f"  X = C_f ⊕ C_f ⊕ (-I₂) ∈ M_8(GF(9)):  Ordnung = {o}")
assert o == 26
assert mpow(X26, 26) == I8 and not (mpow(X26, 13) == I8) and not (mpow(X26, 2) == I8)
print(f"  [OK] X^26 = 1, X^13 ≠ 1, X^2 ≠ 1  → Ordnung exakt 26 [B]")

coeffs = blade_coeffs(X26)
print(f"\n  Blade-Zerlegung von X in GALG-Notation ({len(coeffs)} Blades ≠ 0):")
# Rückprobe
Xr = M9.zeros(8)
for S, c in coeffs.items(): Xr = Xr + blades[S].scal(c[0], c[1])
assert Xr == X26, "Blade-Rekonstruktion fehlgeschlagen"
line = "  X = "
for S, c in sorted(coeffs.items(), key=lambda t: (len(t[0]), t[0])):
    line += f"({fmt_c(c)})*{fmt_blade(S)} "
print(line)
print(f"  [OK] Rekonstruktion aus Blades exakt — X ist ein G(6)-Element mit Z3C-Koeffizienten")

# Grad-Verteilung
grades = {}
for S in coeffs: grades[len(S)] = grades.get(len(S), 0) + 1
print(f"  Grade der beteiligten Blades: {dict(sorted(grades.items()))}")

# ============================================================
print()
print("=" * 66)
print("SATZ B': Wie häufig sind Ordnung-13-Elemente in G(6)?")
print("=" * 66)
# Test 13 | ord(X)  ⟺  X^(N/13) ≠ 1  (für invertierbare X)
N13 = N_exp // 13
def has13(X):
    if not (mpow(X, N_exp) == I8): return None
    return not (mpow(X, N13) == I8)

rng = random.Random(7)
for supp in (2, 3, 4, 6, 10):
    hits = tot = 0
    for _ in range(600):
        X = M9.zeros(8)
        for S in rng.sample(list(blades), supp):
            a, b = rng.randrange(3), rng.randrange(3)
            if not (a or b): a = 1
            X = X + blades[S].scal(a, b)
        h = has13(X)
        if h is None: continue
        tot += 1; hits += h
    print(f"  Support {supp:2d} Blades: 13 | ord(X) bei {hits:3d}/{tot:3d} invertierbaren Elementen ({100*hits/max(tot,1):5.1f} %)")

print("  => Ordnung-13-Elemente sind in G(6) häufig — Dougs Suche in G(3) (span{a,b,c})")
print("     konnte sie prinzipiell nicht finden; zudem braucht es ≥5 Blades.")

# ------------------------------------------------------------
# Konkretes Minimalbeispiel für Doug (GALG-Notation), Ordnung exakt 26
# ------------------------------------------------------------
print()
print("  Konkretes 5-Blade-Element mit Ordnung EXAKT 26 (direkt in GALG nachprüfbar):")
X5_terms = [
    ((0,1),       (2,2)),   # (-1-i)*e1^e2
    ((0,1,2,5),   (1,1)),   # (+1+i)*e1^e2^e3^e6
    ((0,1,4,5),   (1,2)),   # (+1-i)*e1^e2^e5^e6
    ((0,3,4,5),   (1,1)),   # (+1+i)*e1^e4^e5^e6
    ((0,1,2,3,5), (2,0)),   # (-1)  *e1^e2^e3^e4^e6
]
X5 = M9.zeros(8)
for S, c in X5_terms: X5 = X5 + blades[S].scal(c[0], c[1])
print("    X = " + " ".join(f"({fmt_c(c)})*{fmt_blade(S)}" for S, c in X5_terms))
o5 = order(X5)
print(f"    ord(X) = {o5};  X^26 = 1: {mpow(X5,26)==I8},  X^13 = 1: {mpow(X5,13)==I8},  X^2 = 1: {mpow(X5,2)==I8}")
assert o5 == 26
print("    [OK] Ordnung exakt 26 — GF(27)*-Struktur mit nur 5 Blades in G(6)")
print("    GALG-Check für Doug:  X = -(1+1j)*(e1^e2) + (1+1j)*(e1^e2^e3^e6) + (1-1j)*(e1^e2^e5^e6)")
print("                              + (1+1j)*(e1^e4^e5^e6) - (e1^e2^e3^e4^e6);   X**26 == 1, X**13 != 1")

# ============================================================
print()
print("=" * 66)
print("SATZ C: GF(27) als TEILKÖRPER in M_n(GF(9)) ⟺ 3 | n")
print("=" * 66)
print("  Unitale Einbettung GF(27) ↪ M_n(GF(9)) macht GF(9)^n zu einem")
print("  GF(27)⊗GF(9) = GF(729)-Vektorraum  → [GF(729):GF(9)] = 3 teilt n.")
for n in (2, 8, 3, 6, 9):
    print(f"    n={n}: 3|n = {n % 3 == 0}  →  {'Teilkörper möglich' if n%3==0 else 'kein Teilkörper'}")
print("  G(3) → n=2: nein.   G(6) → n=8: nein.")
print("  Aber ELEMENTE der Ordnung 26 existieren in G(6) (Satz B):")
print("  GF(9)[X] ≅ GF(729) ⊕ GF(9)  (nicht ein Körper, X hat Eigenwerte in GF(27) und -1∈GF(3))")
print("  => GF(27) ist in G(6) als Ordnungsstruktur präsent, nicht als Teilkörper.")
print("  => Exakt FFGFT: GF(9) ⊄ GF(27), beide parallel in GF(3^6)=GF(729)  [Dok. 338, pruef_330]")

# Charpoly von X26 über GF(3) zur Illustration
print()
print("  Charakteristisches Polynom von X über GF(3):")
print("    χ(x) = (x³+2x+1)² · (x+1)²   — zwei GF(27)-Faktoren, ein GF(3)-Faktor")

# ============================================================
print()
print("=" * 66)
print("KONSEQUENZ für FFGFT ↔ GALG")
print("=" * 66)
print("""  (m_μ/m_e)² = |GF(9)*|² · 5² · |GF(27)| = 43200     braucht GF(27)  [Dok. 338]
  1/α = 3700/27:  |GF(27)| kürzt sich heraus            braucht KEIN GF(27)

  GALG G(3): enthält GF(9), GF(81) — kein GF(27)  (Satz A, Dougs Befund bestätigt)
  GALG G(6): enthält Ordnung-26-Elemente — GF(27) erreichbar (Satz B), kein Teilkörper (Satz C)

  => α ist auf der G(3)/GF(9)-Ebene formulierbar; die Leptonen-Massenschicht braucht
     G(6) mit Ordnung-26-Elementen. Dougs "not working on mass" und sein Suchergebnis
     sind beide konsistent mit dieser Trennung.
""")

print("=" * 66)
print("ASSERTIONS")
print("=" * 66)
assert 80 % 13 != 0;                       print("  [OK] 13 ∤ |GF(81)*|  → G(3) ohne GF(27)")
assert all(o % 13 != 0 for o in ords3);    print("  [OK] Cl(3)-Stichprobe: keine Ordnung ≡ 0 mod 13")
assert order(X26) == 26;                   print("  [OK] Ordnung-26-Element in G(6) konstruiert")
assert Xr == X26;                          print("  [OK] Blade-Zerlegung mit Z3C-Koeffizienten exakt")
assert 8 % 3 != 0;                         print("  [OK] 3 ∤ 8 → kein GF(27)-Teilkörper in G(6)")
assert (9**3 - 1) % 13 == 0;               print("  [OK] 13 | |GF(729)*| → GF(27) ⊂ GF(729) = GF(9)·GF(27)")
print("\nAlle Assertions bestanden.")
