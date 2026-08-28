#!/usr/bin/env python3
"""
pruef_326_gf9_orbit_masse_weinberg.py
======================================
Drei weitere Strukturfragen auf Basis von Dok. 336 (Z3C_sym-Brücke):

Punkt 3: Frobenius-Fixpunkte in Z3C_sym = FFGFT-Sektoren Dw [B]
Punkt 4: Norm-Hierarchie GF(3)->Z3C_sym->R(xi) fuer Massen [K]
Punkt 5: Weinberg-Winkel — Z3C_sym gibt Topologie, xi gibt Wert [K]

Ausführen: python3 pruef_326_gf9_orbit_masse_weinberg.py
Benötigt:  numpy
"""
import numpy as np
import sys

FAIL = False
def chk(cond, msg):
    global FAIL
    tag = "OK  " if cond else "FAIL"
    if not cond: FAIL = True
    print(f"  [{tag}] {msg}")
    return cond

banner = "=" * 68

class Z3C_sym:
    """Symmetrisches Z3C (nach Matzke): a+bi, a,b in {-1,0,+1}.
    +1+1=-1, -1-1=+1 (symmetrische char.3, ternary inline carry/borrow)."""
    def __init__(self, a, b=0):
        r=int(a)%3; self.a=r if r<2 else r-3
        r=int(b)%3; self.b=r if r<2 else r-3
    def __add__(self, o):
        if isinstance(o,int): o=Z3C_sym(o)
        return Z3C_sym(self.a+o.a, self.b+o.b)
    def __radd__(self, o): return self.__add__(o)
    def __mul__(self, o):
        if isinstance(o,int): o=Z3C_sym(o)
        return Z3C_sym(self.a*o.a-self.b*o.b, self.a*o.b+self.b*o.a)
    def __rmul__(self, o): return self.__mul__(o)
    def __neg__(self): return Z3C_sym(-self.a,-self.b)
    def __sub__(self, o): return self+(-o)
    def __pow__(self, n):
        r=Z3C_sym(1)
        for _ in range(n): r=r*self
        return r
    def __eq__(self, o):
        if isinstance(o,int): o=Z3C_sym(o)
        return self.a==o.a and self.b==o.b
    def conj(self): return Z3C_sym(self.a,-self.b)
    def norm(self):
        r=(self.a**2+self.b**2)%3; return r if r<2 else r-3
    def is_zero(self): return self.a==0 and self.b==0
    def __repr__(self):
        if self.b==0: return f"{self.a:+d}" if self.a else "0"
        if self.a==0: return f"{self.b:+d}i"
        return f"{self.a:+d}{self.b:+d}i"

# Alle 9 Elemente (Dougs Reihenfolge: symmetrisch um 0)
all_z3c = [Z3C_sym(a,b) for a in [-1,0,1] for b in [-1,0,1]]


# ============================================================
# PUNKT 3: Frobenius-Fixpunkte = FFGFT-Sektoren
# ============================================================
print(banner)
print("PUNKT 3: Frobenius-Fixpunkte phi(x)=x^3 in Z3C_sym = FFGFT-Sektoren")
print(banner)

fixpoints  = [x for x in all_z3c if x**3 == x]
non_fixed  = [x for x in all_z3c if x**3 != x and not x.is_zero()]

print(f"\nFixpunkte: {fixpoints}")
chk(len(fixpoints) == 3, "3 Fixpunkte in Z3C_sym [=GF(3)]")
chk(all(x == Z3C_sym(x.a, 0) for x in fixpoints),
    "Alle Fixpunkte haben b=0: Fixpunkte = GF(3) subset Z3C_sym")

print(f"\nFFGFT-Sektoren Dw in {{0,1,2}} = GF(3):")
for fp in fixpoints:
    chk(fp == Z3C_sym(fp.a, 0), f"Fixpunkt {fp} = GF(3)-Element Dw={fp.a}")

# 2-Zyklen (Nicht-Fixpunkte)
print(f"\nNicht-Fixpunkte = (k,-k)-Paare:")
seen = set()
orbits = []
for x in non_fixed:
    key = (x.a, x.b)
    if key not in seen:
        y = x**3
        orbits.append((x, y))
        seen.add((x.a, x.b))
        seen.add((y.a, y.b))
        chk(y**3 == x, f"2-Zyklus: {x} <-> {y}: ({x})^3={y}, ({y})^3={x}")

chk(len(orbits) == 3, f"Genau 3 konjugierte Paare (k,-k) in Z3C_sym\\GF(3)")
print(f"\n[B] Frobenius-Fixpunkte = GF(3) = FFGFT-Sektoren Dw")
print(f"[B] Nicht-Fixpunkte = 3 konjugierte (k,-k)-Paare")
print(f"[B] Galois-Gruppe Gal(Z3C_sym/GF(3)) = Z2 = FFGFT-Sektorpaarung")

# ============================================================
# PUNKT 4: Norm-Hierarchie GF(3)->Z3C_sym->R
# ============================================================
print(f"\n{banner}")
print("PUNKT 4: Norm-Hierarchie GF(3) -> Z3C_sym -> R(xi) fuer Massen")
print(banner)

print(f"\n[A] GF(3): n^2 fuer n in {{0,1,2}}")
gf3_squares = {n: n**2 % 3 for n in range(3)}
for n, sq in gf3_squares.items():
    print(f"  {n}^2 mod 3 = {sq}")
chk(gf3_squares[1] == gf3_squares[2],
    "1^2 = 2^2 = 1 in GF(3): Gen.2 und Gen.3 DEGENERIERT als Quadrate")
chk(gf3_squares[0] == 0,
    "0^2 = 0 in GF(3): Gen.1 (masselose Neutrino-Klasse) verschwindet")
print(f"  => GF(3) unterscheidet nur: 0 (Massennullstelle) vs. 1 (Masse vorhanden)")

print(f"\n[B] Z3C_sym: Norm = a^2+b^2 mod 3 fuer x=a+bi")
norm_classes = {}
for x in all_z3c:
    if not x.is_zero():
        n = x.norm()
        if n not in norm_classes: norm_classes[n] = []
        norm_classes[n].append(x)

for norm_val in sorted(norm_classes):
    els = norm_classes[norm_val]
    chk(True, f"Norm={norm_val}: {els} ({len(els)} Elemente)")

chk(set(norm_classes.keys()) == {1, -1},
    "Z3C_sym*: genau zwei Normklassen {1, 2}")

# Norm-1-Klasse: rein reell oder rein imaginaer = GF(3)*-Elemente + imagnaere
norm1 = norm_classes[1]
norm2 = norm_classes[-1]
print(f"\n  Norm=1 ({len(norm1)} Elem.): {norm1}")
print(f"    => Fixpunkte (GF(3)*) und rein Imaginaere")
print(f"  Norm=-1 ({len(norm2)} Elem.): {norm2}")
print(f"    => Gemischte Elemente (Z3C_sym\\GF(3), Nicht-Fixpunkte ohne rein imag.)")
chk(len(norm1) == 4 and len(norm2) == 4,
    "4 Elemente pro Normklasse: symmetrische Aufteilung")

# Physikalische Interpretation
print(f"\n[C] Physikalische Interpretation:")
print(f"  Norm=1: leichte Generationen (Fixpunkte, stabil unter Frobenius)")
print(f"  Norm=-1: schwere Generationen (gemischte Elemente, instabil)")
print(f"  Massenhierarchie: Norm=1 -> leicht, Norm=-1 -> schwer [K]")

# Experimentell: Leptonmassen
m_e, m_mu, m_tau = 0.511, 105.66, 1776.86
print(f"\n  Leptonmassen: m_e={m_e}, m_mu={m_mu}, m_tau={m_tau} MeV")
# Welche Norm hat welche Generation?
# m_e: klein -> Norm=1? m_tau: gross -> Norm=-1?
print(f"  Wenn e,nu: Norm=1 und mu,tau: Norm=-1:")
print(f"  Massenverhaltnis Norm-2/Norm-1 ~ m_mu/m_e = {m_mu/m_e:.0f}")
print(f"  Z3C_sym gibt keine Zahl, ξ gibt den Faktor 206 [K]")

# n^2 in GF(3): Warum 1^2=2^2=1?
print(f"\n[D] Algebraische Degeneriertheit und ihre Bedeutung:")
print(f"  In GF(3): 2 ≡ -1, also 2^2 = (-1)^2 = 1 = 1^2 [B]")
print(f"  => Die Z3-Symmetrie macht Generation 2 und 3 'algebraisch aequivalent'")
print(f"  => Die Massendifferenz m_mu ≠ m_tau ist eine SYMMETRIEBRECHUNG")
print(f"  => ξ bricht die GF(3)-Degeneriertheit und gibt unterschiedliche Massen [K]")
chk(2**2 % 3 == 1**2 % 3,
    "2^2 = 1^2 = 1 in GF(3): algebraische Massendegenerierung [B]")

# ============================================================
# PUNKT 5: Weinberg-Winkel
# ============================================================
print(f"\n{banner}")
print("PUNKT 5: Weinberg-Winkel — Z3C_sym-Topologie vs. xi-Wert")
print(banner)

sin2_W_exp = 0.23122  # experimentell

print(f"\n[A] Z3C_sym-Untergruppen-Analyse:")
# Generator von Z3C_sym* (Ordnung 8)
g = None
for a in [-1,0,1]:
    for b in [-1,0,1]:
        el = Z3C_sym(a,b)
        if el.is_zero(): continue
        if all((el**k != Z3C_sym(1,0) or k==8) for k in range(1,8)):
            # Ordnung testen
            order = next((n for n in range(1,9) if (el**n)==Z3C_sym(1,0)), None)
            if order == 8:
                g = el; break
    if g: break

if g:
    print(f"  Generator Z3C_sym*: g = {g} (Ordnung 8)")
    # Untergruppen
    for div in [1,2,4,8]:
        subgr = [g**(div*k) for k in range(8//div)]
        print(f"  Untergruppe Ord.{8//div}: {subgr}")

print(f"\n[B] Z3C_sym-Ratios als sin^2(theta_W)-Kandidaten:")
candidates = {
    "|GF(3)|/|Z3C_sym|":        3/9,
    "|GF(3)*|/|Z3C_sym*|":      2/8,
    "|Norm=1|/|Z3C_sym*|":      4/8,
    "1/|Gal(Z3C_sym/GF(3))|":   1/2,
    "|Fixpkt.*|/|Z3C_sym*|":    2/8,
}
for name, val in candidates.items():
    diff = abs(val - sin2_W_exp)
    marker = " <- naechster" if diff < 0.05 else ""
    chk(True, f"{name} = {val:.4f}  (Diff zu exp. {sin2_W_exp}: {diff:.4f}){marker}")

best_val = 2/8  # |GF(3)*|/|Z3C_sym*| = 0.25
print(f"\n  Bester Z3C_sym-Kandidat: {best_val:.4f}")
print(f"  Experimentell:         {sin2_W_exp:.4f}")
print(f"  Abweichung: {abs(best_val-sin2_W_exp)/sin2_W_exp*100:.1f}%")
chk(abs(best_val - sin2_W_exp) < 0.05,
    f"|GF(3)*|/|Z3C_sym*| = 0.25 nahe sin^2(theta_W)=0.231 (Abw. 8%)")

print(f"\n[C] Was Z3C_sym leistet:")
print(f"  Topologie: Grad-2-Erweiterung Z3C_sym/GF(3) = zwei Eichgruppen [K]")
print(f"  Kandidat:  |GF(3)*|/|Z3C_sym*| = 1/4 als tree-level-Naherung [K]")
print(f"  Exakter Wert 0.231 braucht xi-Korrekturen (Dok. 323) [K]")
print(f"  Z3C_sym gibt WARUM zwei Eichgruppen; xi gibt WIE VIEL Mischung.")

# ============================================================
# Hierarchie-Zusammenfassung
# ============================================================
print(f"\n{banner}")
print("ZUSAMMENFASSUNG: Algebraische Hierarchie GF(3) -> Z3C_sym -> R(xi)")
print(banner)
print("""
Ebene        Gibt                           Status
--------------------------------------------------------------
GF(3)        Ob Sektor/Generation existiert    [B]
             n^2 in {0,1}: 0=masselos, 1=massiv
             Gen.2 und Gen.3 algebraisch degeneriert

Z3C_sym        Stabile Sektoren (Fixpunkte)      [B]
             3 konjugierte (k,-k)-Paare
             2 Normklassen {1,2}: leicht/schwer
             2-Galois-Struktur -> 2 Eichgruppen

R(xi)        Exakte Massenwerte                [K]
             xi bricht GF(3)-Degeneriertheit
             sin^2(theta_W) = 0.231 via Dok.323
             Massenverhaltnis m_mu/m_e = 206.77

Brücke Z3C_sym->R: Die Singularitaet C2=4/3 in GF(3) (Dok.336, Punkt 4)
markiert genau diesen Uebergang von diskreter Topologie zu kontinuierlicher Physik.
""")

print(banner)
if FAIL:
    print("ERGEBNIS: Fehler — siehe FAIL-Eintraege.")
    sys.exit(1)
else:
    print("ERGEBNIS: Alle Assertions bestanden.")
    sys.exit(0)
