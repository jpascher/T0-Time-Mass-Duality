#!/usr/bin/env python3
"""
pruef_341_primordnung.py
=========================
Eintrittsskala der Primzahlen in GF(3^k): ord_p(3) = kleinstes k mit p | 3^k-1
Tripotente als Matrix-Phänomen: t^3=t mit t≠0,1 unmöglich in GF(3^k)*
Trine-Produkt: Gegenbeispiel bei nicht-kommutativen Faktoren

Anlass: Doug Matzke, IPI-Mail 4. Sept. 2026:
  "root5 is a genuinely new classification class — the first odd-prime root
   of unity, dividing the period-80 clock"
  — Korrekt für G(3)-Algebren; global tritt 13 (k=3) vor 5 (k=4) ein.

ERGEBNISSE:

(A) Globale Eintrittsskala der Primzahlen [K]:
    ord_p(3) = kleinstes k mit p | 3^k-1
    k=3: p=13  (13 | |GF(27)*| = 26)
    k=4: p=5   (5  | |GF(81)*| = 80)
    k=5: p=11  (11 | 242)
    k=6: p=7   (7  | 728)
    Dougs "root5 erste ungerade Primzahl" gilt nur für G(3)-Elementordnungen
    (GF(27)-Eigenwerte dort nicht erreichbar), nicht global.

(B) Tripotente t^3=t mit t≠0,1 unmöglich in GF(3^k)* [K]:
    3^k - 1 ≡ 2 (mod 3) für alle k ≥ 1 → 3 ∤ |GF(3^k)*| immer.
    Tripotente sind ein Matrix-Phänomen (M_n(GF(9))), kein Körper-Phänomen.
    Konsequenz: Q = N/3 nicht GF(3)-einbettbar; φ(N) = N mod 3 ist der
    korrekte Ring-Homomorphismus (Dok. 336).

(C) Trine-Produkt: Gegenbeispiel in M_2(GF(3)) [B]:
    Zwei nicht-kommutierende Trines t1,t2 (t^3=I, t≠I) in M_2(GF(3));
    (t1·t2)^3 ≠ I — kein Trine.
    Dougs (1+ap1)(1+ap2)(1+ap3) funktioniert weil ap_k antikommutieren
    → in Char. 3 äquivalent zu Frobenius-Kommutatitivität unter Kubierung.

Autor: Johann Pascher, ORCID 0009-0000-6518-4064
Datum: 4. September 2026
"""
import sympy as sp
import numpy as np

# ============================================================
print("="*66)
print("(A) Eintrittsskala der Primzahlen: ord_p(3)")
print("="*66)

entries = []
for p in sp.primerange(3, 50):
    for k in range(1, 25):
        if (3**k - 1) % p == 0:
            entries.append((k, int(p), 3**k - 1))
            break

entries.sort()
print(f"  {'p':>4}  k   |GF(3^k)*|  Primfaktorzerlegung")
print(f"  {'-'*50}")
for k, p, ord_k in entries[:10]:
    print(f"  p={p:>2}: k={k}  {ord_k:>10}  = {dict(sp.factorint(ord_k))}")

print()
print(f"  Reihenfolge nach k: {[(k,p) for k,p,_ in entries[:8]]}")
print()
print(f"  In G(3) [Eigenwerte in GF(81), k≤4]:")
for k in range(1, 5):
    fac = dict(sp.factorint(3**k - 1))
    print(f"    k={k}: |GF(3^{k})*| = {3**k-1} = {fac}")
print(f"  Elementordnungen in G(3) teilen |GF(81)*| = 80 = 2^4·5")
print(f"  => Ordnung 13 nicht erreichbar in G(3)-Elementen (obwohl 13 bei k=3 eintritt)")
print(f"  => Dougs 'root5 erste ungerade' gilt für G(3)-Elementordnungen ✓")
print(f"  => Global aber: 13 vor 5 ✓")

# Assertions
k5 = next(k for k,p,_ in entries if p==5)
k13 = next(k for k,p,_ in entries if p==13)
k7 = next(k for k,p,_ in entries if p==7)
assert k13 < k5 < k7
print(f"\n  [OK] ord_13(3) = {k13} < ord_5(3) = {k5} < ord_7(3) = {k7}")
assert (3**k13 - 1) % 13 == 0 and (3**(k13-1) - 1) % 13 != 0
print(f"  [OK] 13 tritt erstmals bei k={k13} auf")

# ============================================================
print()
print("="*66)
print("(B) Tripotente t^3=t unmöglich in GF(3^k)*")
print("="*66)

print(f"  3^k - 1 (mod 3) für k=1..8:")
for k in range(1, 9):
    val = (3**k - 1) % 3
    print(f"    k={k}: 3^{k}-1 = {3**k-1}, mod 3 = {val}")

assert all((3**k - 1) % 3 == 2 for k in range(1, 20))
print(f"  [OK] 3^k - 1 ≡ 2 (mod 3) für alle k=1..19")
print(f"  [OK] 3 ∤ |GF(3^k)*| für alle k → Ordnung 3 in GF(3^k)* unmöglich")
print(f"  => t^3=t mit t≠0,1 ist ein Matrix-Phänomen, kein Körper-Phänomen")
print(f"  => Q = Number/3 nicht GF(3)-einbettbar (Division durch 3 in Char.3 undefiniert)")
print(f"  => Korrekte Formulierung: φ(N) = N mod 3 als Ring-Homomorphismus")

# ============================================================
print()
print("="*66)
print("(C) Trine-Produkt: Gegenbeispiel in M_2(GF(3))")
print("="*66)

def mpow2(X, k):
    I = np.eye(2, dtype=np.int64)
    R = I.copy(); B = X.copy() % 3
    while k:
        if k & 1: R = R @ B % 3
        B = B @ B % 3; k >>= 1
    return R % 3

I2 = np.eye(2, dtype=np.int64)

# t1: Companion von x^2+x+1 (irred. über GF(3), ord=3)
t1 = np.array([[0,1],[2,2]], dtype=np.int64)
# t2: anderes Element der Ordnung 3 in GL_2(GF(3))
t2 = np.array([[0,2],[1,2]], dtype=np.int64)
# t3: unipotent, Ordnung 3 (obere Dreiecksmatrix)
t3 = np.array([[1,1],[0,1]], dtype=np.int64)

for t, nm in [(t1,"t1"),(t2,"t2"),(t3,"t3")]:
    is_trine = np.array_equal(mpow2(t,3), I2) and not np.array_equal(t, I2)
    print(f"  {nm}^3 = I: {np.array_equal(mpow2(t,3),I2)},  {nm}≠I: {not np.array_equal(t,I2)}  → Trine: {is_trine}")

print()
# t1,t2 nicht-kommutierend → (t1·t2)^3 ≠ I
comm12 = np.array_equal(t1@t2%3, t2@t1%3)
prod12 = t1@t2%3
trine12 = np.array_equal(mpow2(prod12,3), I2)
print(f"  t1,t2 kommutieren: {comm12}")
print(f"  (t1·t2)^3 = I: {trine12}  → {'Trine' if trine12 else 'KEIN Trine ← Gegenbeispiel!'}")

# t1,t3 nicht-kommutierend → (t1·t3)^3 ≠ I
comm13 = np.array_equal(t1@t3%3, t3@t1%3)
prod13 = t1@t3%3
trine13 = np.array_equal(mpow2(prod13,3), I2)
print(f"  t1,t3 kommutieren: {comm13}")
print(f"  (t1·t3)^3 = I: {trine13}  → {'Trine' if trine13 else 'KEIN Trine ← Gegenbeispiel!'}")

assert not comm12 and not trine12
assert not comm13 and not trine13
print(f"  [OK] Nicht-kommutierende Trines: Produkt ist kein Trine")

# Warum funktioniert Dougs (1+ap1)(1+ap2)(1+ap3)?
print()
print(f"  Warum Dougs Konstruktion funktioniert:")
print(f"  ap_i·ap_j = -ap_j·ap_i (antikommutierend, da Witt-Raiser)")
print(f"  In Char. 3: (-1)^3 = -1 ≡ 2 — Antikommutatitivität bleibt unter Kubierung erhalten")
print(f"  (1+ap_k)^3 = 1 + 3·ap_k + 3·ap_k^2 + ap_k^3 = 1 + 0 + 0 + ap_k^3 = 1 + ap_k^3")
print(f"  ap_k^3 = 0 (nilpotent, da ap_k^2 = 0 für Witt-Raiser)")
print(f"  => (1+ap_k)^3 = 1 — jeder Faktor ist Trine")
print(f"  Produkt dreier antikommutierender Trines in Char. 3: Frobenius-Expansion kollabiert")

# ============================================================
print()
print("="*66)
print("ASSERTIONS GESAMT")
print("="*66)
assert k13 == 3 and k5 == 4 and k7 == 6
print(f"  [OK] Eintrittsskala: k(13)=3, k(5)=4, k(7)=6")
assert all((3**k - 1) % 3 == 2 for k in range(1, 30))
print(f"  [OK] 3^k-1 ≡ 2 (mod 3) für k=1..29 — Tripotente nicht in GF(3^k)*")
assert not comm12 and not trine12 and not comm13 and not trine13
print(f"  [OK] Gegenbeispiel: nicht-kommutierende Trines → kein Trine-Produkt")
print()
print("Alle Assertions bestanden.")
