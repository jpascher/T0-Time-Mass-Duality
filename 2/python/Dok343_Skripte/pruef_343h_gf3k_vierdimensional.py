#!/usr/bin/env python3
"""
pruef_343h_gf3k_vierdimensional.py
Offener Rest zu Dok. 343 / R130: Hat die GF(3^k)-Lesart (Dok. 342: Primzahl p tritt bei der
Eintrittstiefe k = ord_p(3) auf) eine Entsprechung in der echten spektralen Zeta-Funktion
des Korpus-Orbifolds T4/Z3 (fixpunktfreie Z3 auf D4, Dok. 314/330)?

Vorgehen:
  1. Bahnzahlen je Schale direkt auszählen: a(m) = #Z3-Bahnen der D4-Vektoren mit |k|^2 = 2m.
  2. Gegen die Formel a(m) = 8 * sigma_odd(m) prüfen (Thetareihe von D4 / 3).
  3. Multiplikativität und lokale Euler-Faktoren je Primzahl bestimmen.
  4. Prüfen, ob die lokalen Faktoren von ord_p(3) abhängen (GF(3^k)-Signatur) oder ob p = 3
     eine Sonderrolle hat.
Ergebnis wird so ausgegeben, wie es fällt; jede Prüfung kann fehlschlagen.
"""
import itertools
from math import gcd
import numpy as np

ok = n_t = 0


def check(name, cond, info=""):
    global ok, n_t
    n_t += 1
    ok += bool(cond)
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}" + (f"  ({info})" if info else ""))


# fixpunktfreie Z3 auf D4: Linksmultiplikation mit der Hurwitz-Einheit (-1+i+j+k)/2
a0, a1, a2, a3 = -0.5, 0.5, 0.5, 0.5
Hq = np.array([[a0, -a1, -a2, -a3], [a1, a0, -a3, a2], [a2, a3, a0, -a1], [a3, -a2, a1, a0]])
check("Z3 fixpunktfrei, Spur -2, |det(1-A)| = 9 (Korpus-Klasse Dok. 314)",
      abs(np.trace(Hq) + 2) < 1e-12 and round(abs(np.linalg.det(np.eye(4) - Hq))) == 9)

M = 26
R = int(np.ceil(np.sqrt(2 * M))) + 1
shells = {m: [] for m in range(1, M + 1)}
for c in itertools.product(range(-R, R + 1), repeat=4):
    if sum(c) % 2:
        continue
    n2 = sum(x * x for x in c)
    if n2 == 0 or n2 > 2 * M:
        continue
    shells[n2 // 2].append(np.array(c, float))


def orbits(vs):
    seen, cnt = set(), 0
    for v in vs:
        k = tuple(np.round(v, 6))
        if k in seen:
            continue
        seen |= {k, tuple(np.round(Hq @ v, 6)), tuple(np.round(Hq @ Hq @ v, 6))}
        cnt += 1
    return cnt


def sigma_odd(m):
    return sum(d for d in range(1, m + 1) if m % d == 0 and d % 2)


def n_order(g, p):
    k, x = 1, g % p
    while x != 1:
        x, k = x * g % p, k + 1
    return k


a = {m: orbits(shells[m]) for m in shells}
print("\n  m :", " ".join(f"{m:>4}" for m in range(1, 13)))
print("  a :", " ".join(f"{a[m]:>4}" for m in range(1, 13)))
check(f"a(m) = 8 * sigma_odd(m) für m = 1..{M} (direkte Bahnzählung)", all(a[m] == 8 * sigma_odd(m) for m in a))
check("jede Schale zerfällt restlos in Dreierbahnen (|Schale| = 3 a(m))",
      all(len(shells[m]) == 3 * a[m] for m in a))
check("a(m)/8 multiplikativ für teilerfremde m, n",
      all(a[m * n] * 8 == a[m] * a[n] for m in range(1, M + 1) for n in range(1, M + 1)
          if m * n <= M and gcd(m, n) == 1))

print("\n  Lokale Faktoren je ungerader Primzahl (b(p^j) = a(p^j)/8):")
print(f"  {'p':>3} {'ord_p(3)':>9} {'b(p)':>6} {'1+p':>6} {'b(p^2)':>7} {'1+p+p^2':>8}")
uniform = True
for p in (3, 5, 7, 11, 13):
    ordp = "-" if p == 3 else n_order(3, p)
    bp = a[p] // 8
    bp2 = a[p * p] // 8 if p * p <= M else None
    uniform &= (bp == 1 + p) and (bp2 is None or bp2 == 1 + p + p * p)
    print(f"  {p:>3} {str(ordp):>9} {bp:>6} {1+p:>6} {str(bp2) if bp2 else '-':>7} {1+p+p*p:>8}")
check("lokale Faktoren b(p^j) = 1+p+...+p^j für alle ungeraden p, unabhängig von ord_p(3)", uniform)
check("p = 3 ohne Sonderrolle (b(3) = 4, b(9) = 13 wie jede ungerade Primzahl)", a[3] == 32 and a[9] == 104)
check("p = 2 trivial: b(2^j) = 1", all(a[2 ** j] == 8 for j in range(1, 5)))

print("\n" + "=" * 72)
print(f"ERGEBNIS: {ok}/{n_t} Prüfungen bestanden")
print("=" * 72)
print("""
  Die Bahnzahlen des Korpus-Orbifolds sind a(m) = 8 sigma_odd(m); ihre Euler-Faktoren
  1/((1-p^-s)(1-p^(1-s))) haben für jede ungerade Primzahl dieselbe Form.
  Eine Ordnung der Primzahlen nach ord_p(3) (GF(3^k)-Eintrittstiefe) tritt in der
  spektralen Zeta-Funktion von T4/Z3 nicht auf, und p = 3 spielt dort keine Sonderrolle.
  Die GF(3^k)-Struktur aus Dok. 342 ist damit eine Aussage über die Arithmetik mod 3,
  nicht über das Laplace-Spektrum des Orbifolds.
""")
assert ok == n_t
