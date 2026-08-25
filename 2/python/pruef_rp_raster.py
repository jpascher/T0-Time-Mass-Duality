#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prüfskript: Regelstruktur des (r,p)-Rasters der Yukawa-Massenformel
m = r · ξ^p · v,   ξ = 4/30000,  v = 246 GeV

Quellen der Koeffizienten: Dok. 005/006/046, calc_De.py v3.5
(Tau-Korrektur r = 25/9), HTML-Tabelle complete_particle_spectrum.html.

Geprüfte Kandidatenregeln (Status: empirisch, [S]):
  R1  Generation 1 ist p-uniform: p(e) = p(u) = p(d) = 3/2
  R2  Geladene Leptonen: p geometrisch, Faktor 2/3  (3/2 → 1 → 2/3)
  R3  Down-Typ: p arithmetisch, Schritt −1/2        (3/2 → 1 → 1/2)
  R4  Up-Typ: erfüllt weder R2- noch R3-Form (Negativbefund)
  R5  r-Werte sind {2,3,5}-glatt (5-Limit / Tonnetz) —
      mit genau zwei Ausnahmen: s (Faktor 13), t (Faktor 7)
  R6  Extrapolations-Check: eine 4. Generation nach R2 läge bei
      p = 4/9, also m ≈ r · 4.66 GeV — experimentell ausgeschlossen
      für r = O(1) (LEP: m_L4 > 100.8 GeV). Konsequenz: R2 muss bei
      n = 3 abbrechen; Abbruchgrund ist nicht Teil dieses Skripts.

Alle Prüfungen sind reine Konsistenzchecks der Koeffiziententabelle.
Es wird nichts aus ξ abgeleitet.
"""

from fractions import Fraction as F

XI = F(4, 30000)
V  = 246.0  # GeV (Higgs-VEV, Layer-2-Anker)

# Teilchen: (r, p, m_exp [GeV])  — m_exp wie in der HTML-Tabelle (PDG, MS̄ außer Top)
PARTS = {
    'e':   (F(4, 3),   F(3, 2),  0.000511),
    'mu':  (F(16, 5),  F(1),     0.10566),
    'tau': (F(25, 9),  F(2, 3),  1.7769),
    'u':   (F(6),      F(3, 2),  0.00227),
    'c':   (F(2),      F(2, 3),  1.270),
    't':   (F(1, 28),  F(-1, 3), 172.76),
    'd':   (F(25, 2),  F(3, 2),  0.00472),
    's':   (F(26, 9),  F(1),     0.0934),
    'b':   (F(3, 2),   F(1, 2),  4.180),
}

FAMILIES = {
    'geladene Leptonen': ['e', 'mu', 'tau'],
    'Up-Typ-Quarks':     ['u', 'c', 't'],
    'Down-Typ-Quarks':   ['d', 's', 'b'],
}

def mass(r, p):
    return float(r) * (float(XI) ** float(p)) * V

def factorize(n):
    n = int(n); f = {}; d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f

def primes_of(r):
    return set(factorize(r.numerator)) | set(factorize(r.denominator))

results = []
def check(name, ok, detail):
    results.append((name, ok, detail))
    print(f"[{'OK' if ok else '!!'}] {name}: {detail}")

print("=" * 72)
print("Massenreproduktion (Kontext, keine Prüfung):")
for n, (r, p, mexp) in PARTS.items():
    m = mass(r, p)
    dev = 100 * abs(m - mexp) / mexp
    print(f"  {n:3s}  r={str(r):6s} p={str(p):5s}  m_T0={m:12.6g}  "
          f"m_exp={mexp:10.5g}  Abw={dev:5.2f}%")
print("=" * 72)

# R1: Generation 1 p-uniform
p1 = {PARTS[x][1] for x in ('e', 'u', 'd')}
check("R1  Gen-1 p-uniform (p=3/2)", p1 == {F(3, 2)},
      f"p(e,u,d) = {sorted(str(q) for q in p1)}")

# R2: Leptonen geometrisch, Faktor 2/3
pl = [PARTS[x][1] for x in FAMILIES['geladene Leptonen']]
ratios = [pl[i + 1] / pl[i] for i in range(2)]
check("R2  Leptonen p geometrisch (Faktor 2/3)",
      all(q == F(2, 3) for q in ratios),
      f"p = {[str(q) for q in pl]}, Quotienten = {[str(q) for q in ratios]}")

# R3: Down-Typ arithmetisch, Schritt −1/2
pd = [PARTS[x][1] for x in FAMILIES['Down-Typ-Quarks']]
diffs = [pd[i + 1] - pd[i] for i in range(2)]
check("R3  Down-Typ p arithmetisch (Schritt -1/2)",
      all(d == F(-1, 2) for d in diffs),
      f"p = {[str(q) for q in pd]}, Differenzen = {[str(d) for d in diffs]}")

# R4: Up-Typ erfüllt weder geometrische noch arithmetische Form (Negativbefund)
pu = [PARTS[x][1] for x in FAMILIES['Up-Typ-Quarks']]
u_ratios = [pu[i + 1] / pu[i] for i in range(2)]
u_diffs  = [pu[i + 1] - pu[i] for i in range(2)]
is_geo   = u_ratios[0] == u_ratios[1]
is_arith = u_diffs[0] == u_diffs[1]
check("R4  Up-Typ: weder geometrisch noch arithmetisch (Negativbefund)",
      not is_geo and not is_arith,
      f"p = {[str(q) for q in pu]}, Quotienten = {[str(q) for q in u_ratios]}, "
      f"Differenzen = {[str(d) for d in u_diffs]}")

# R5: 5-Limit-Struktur der r-Werte, Ausnahmen s und t
LIMIT = {2, 3, 5}
smooth, anomalies = [], []
for n, (r, p, _) in PARTS.items():
    pr = primes_of(r)
    (smooth if pr <= LIMIT else anomalies).append((n, r, sorted(pr - LIMIT)))
check("R5  r-Werte {2,3,5}-glatt außer s (13) und t (7)",
      sorted(n for n, _, _ in anomalies) == ['s', 't'],
      f"glatt: {[n for n, _, _ in smooth]}; "
      f"Anomalien: {[(n, str(r), extra) for n, r, extra in anomalies]}")

# R6: Extrapolation 4. Generation nach R2 → experimentell ausgeschlossen
p4 = pl[-1] * F(2, 3)          # = 4/9
m4_scale = mass(F(1), p4)      # r = 1 als Skalenreferenz
LEP_BOUND = 100.8              # GeV, PDG-Untergrenze für ein 4. geladenes Lepton
r_needed = LEP_BOUND / m4_scale
check("R6  4. Lepton-Generation nach R2 ausgeschlossen fuer r=O(1)",
      m4_scale < LEP_BOUND,
      f"p4 = {p4}, xi^p4·v = {m4_scale:.3f} GeV; LEP-Grenze {LEP_BOUND} GeV "
      f"erfordert r > {r_needed:.1f} — kein 5-Limit-Bruch dieser Groesse in der "
      f"Tabelle; R2 muss bei n=3 abbrechen")

print("=" * 72)
ok = sum(1 for _, s, _ in results if s)
print(f"Ergebnis: {ok}/{len(results)} Pruefungen bestanden")
