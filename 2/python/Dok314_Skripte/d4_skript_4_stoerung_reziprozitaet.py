#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dok. 314 — Skript 4
Stoerungstheorie 1. Ordnung auf der 24er-Schale (Multiplettstruktur
nach Symmetrieklasse der Stoerung) und Reziprozitaet T*m auf dem
Massenkreis (modenweise exakt; Jensen-Ungleichung im Gemisch).
Abhaengigkeiten: numpy, mpmath. Deterministische Seeds.
Stand: 5. August 2026
"""
import itertools, collections
import numpy as np
from mpmath import mp, mpf, exp

mp.dps = 20

# ================================================================
# Teil A — Multiplettstruktur der ersten Schale unter Stoerung
# ================================================================
# H0 = 2*I auf den 24 Moden; Stoerer V(x) = Sum_g c_g e^{i g.x}:
#   <k|V|k'> = c_{k-k'};  Hermitezitaet c_{-g} = conj(c_g).
# Symmetrieklassen via Orbit-Mittelung der Koeffizienten.

A2 = np.array([[-1, 1, 1, 1], [-1, -1, -1, 1],
               [-1, 1, -1, -1], [-1, -1, 1, -1]])   # 2A (Trialitaet)

def actA(v):
    r = A2 @ np.array(v); assert np.all(r % 2 == 0)
    return tuple(int(x) for x in r // 2)

S1 = [v for v in itertools.product([-1, 0, 1], repeat=4)
      if sum(x * x for x in v) == 2 and sum(v) % 2 == 0]
assert len(S1) == 24
G = [g for g in itertools.product(range(-2, 3), repeat=4)
     if g != (0, 0, 0, 0) and sum(g) % 2 == 0
     and sum(x * x for x in g) <= 8]

def orbit(g, use_A, use_inv):
    out = {g}; changed = True
    while changed:
        changed = False
        for h in list(out):
            for n in ([actA(h)] if use_A else []) + \
                     ([tuple(-x for x in h)] if use_inv else []):
                if n not in out:
                    out.add(n); changed = True
    return frozenset(out)

def build_V(use_A, use_inv, seed, norm_only=False):
    r = np.random.default_rng(seed)
    c = {}
    if norm_only:                      # voll Aut(D4)-invariant
        f = {n: r.normal() for n in (2, 4, 6, 8)}
        for g in G:
            c[g] = f[sum(x * x for x in g)]
    else:
        seen = set()
        for g in G:
            if g in seen:
                continue
            orb = orbit(g, use_A, use_inv)
            neg = frozenset(tuple(-x for x in h) for h in orb)
            val = (r.normal() if neg == orb
                   else r.normal() + 1j * r.normal())
            for h in orb:
                c[h] = val
            for h in neg:
                c[h] = np.conj(val)
            seen |= set(orb) | set(neg)
    V = np.zeros((24, 24), dtype=complex)
    for i, k in enumerate(S1):
        for j, kp in enumerate(S1):
            if i != j:
                V[i, j] = c.get(tuple(np.array(k) - np.array(kp)), 0)
    return (V + V.conj().T) / 2

def multipletts(V):
    ev = np.linalg.eigvalsh(V)
    cl = []
    for e in ev:
        if cl and abs(e - cl[-1][-1]) < 1e-8:
            cl[-1].append(e)
        else:
            cl.append([e])
    return tuple(sorted(collections.Counter(len(x) for x in cl).items()))

FAELLE = [
    ("Aut(D4) (c normabhaengig)", dict(use_A=False, use_inv=False,
                                       norm_only=True),
     ((1, 1), (2, 1), (4, 1), (8, 1), (9, 1))),
    ("Z3 und -1",  dict(use_A=True,  use_inv=True),  ((1, 8), (2, 8))),
    ("nur Z3",     dict(use_A=True,  use_inv=False), ((1, 8), (2, 8))),
    ("nur -1",     dict(use_A=False, use_inv=True),  ((1, 24),)),
    ("nichts",     dict(use_A=False, use_inv=False), ((1, 24),)),
]
print("Stoerung respektiert           Multipletts (Entartung: Anzahl)")
for name, kw, erwartet in FAELLE:
    res = {multipletts(build_V(seed=s, **kw)) for s in (7, 11, 42)}
    assert res == {erwartet}, (name, res)
    print(f"  {name:<28} {dict(erwartet)}   [3 Seeds identisch]")
print("Satz bestaetigt: Multiplettgroessen = Irrep-Dimensionen der")
print("respektierten Symmetrie, NICHT Orbitgroessen. 24=9+8+4+2+1 im")
print("Aut-Fall; Z3-Dubletts = antiunitaere chi1/chi2-Paarung.\n")

# ================================================================
# Teil B — Reziprozitaet auf dem Massenkreis
# ================================================================
# Modenweise: T_k * m_k = (2 pi R4/k)(k/R4) = 2 pi exakt (identisch).
# Gemisch: <T><m>/(2 pi) = <k><1/k> >= 1 (Jensen),
#          Gleichheit <=> genau eine Schale besetzt.

def produkt(p):
    Z = sum(p.values())
    return (sum(w * k for k, w in p.items()) / Z) * \
           (sum(w / mpf(k) for k, w in p.items()) / Z)

assert abs(produkt({1: mpf(1)}) - 1) < mpf('1e-18')
assert abs(produkt({3: mpf(1)}) - 1) < mpf('1e-18')
assert abs(produkt({1: mpf(1), 2: mpf(1)}) - mpf('1.125')) < mpf('1e-15')
g50 = produkt({k: mpf(1) for k in range(1, 51)})
assert abs(g50 - mpf('2.2945947225')) < mpf('1e-9')
print(f"scharfe Schale: <k><1/k> = 1 exakt;  k=1,2: 1.125;  "
      f"k=1..50 gleich: {float(g50):.10f}")
for Tth in (mpf('0.1'), mpf('1'), mpf('10')):
    p = {k: exp(-k / Tth) for k in range(1, 201)}
    print(f"thermisch T={float(Tth):>4}: <k><1/k> = "
          f"{float(produkt(p)):.7f}")
import random
random.seed(1)
worst = min(float(produkt({k: mpf(random.random()) + mpf('1e-6')
                           for k in range(1, 8)})) for _ in range(2000))
assert worst >= 1.0
print(f"2000 Zufallsverteilungen: Minimum {worst:.6f}  (Jensen >= 1)")
print("Alle Kontrollen bestanden.")
