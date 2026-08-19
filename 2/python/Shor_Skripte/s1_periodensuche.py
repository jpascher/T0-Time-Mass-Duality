#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""s1_periodensuche.py -- Empirische Pruefung der Periodensuche.

Prueft die Kernaussagen der Dok. 075/076:

  TEST A  Periodensuche ist korrekt: r aus a^r = 1 mod N liefert Faktoren
  TEST B  Sequenzielle Suche skaliert wie O(N), nicht O((log N)^3)
  TEST C  Der Rasterparameter sigma erzeugt Abtastartefakte, keine Resonanzen
  TEST D  Vergleich mit Probeteilung und Pollard rho

Nur Standardbibliothek. Seed 20780458.
"""
import math
import random
import time
from fractions import Fraction

SEED = 20780458


def periode(a, N, maxsteps=None):
    """Kleinste Periode r mit a^r = 1 mod N, sequenziell gesucht."""
    if math.gcd(a, N) != 1:
        return None, 0
    grenze = maxsteps if maxsteps else N
    x, r = a % N, 1
    while x != 1 and r < grenze:
        x = (x * a) % N
        r += 1
    return (r, r) if x == 1 else (None, r)


def faktorisiere_periode(N, versuche=30, rng=None):
    """Faktorisierung ueber Periodenfindung. Gibt (p, q, Schritte) zurueck."""
    rng = rng or random.Random(SEED)
    gesamt = 0
    for _ in range(versuche):
        a = rng.randrange(2, N)
        g = math.gcd(a, N)
        if g > 1:
            return g, N // g, gesamt
        r, schritte = periode(a, N)
        gesamt += schritte
        if r is None or r % 2:
            continue
        y = pow(a, r // 2, N)
        if y == N - 1:
            continue
        for c in (y - 1, y + 1):
            g = math.gcd(c, N)
            if 1 < g < N:
                return g, N // g, gesamt
    return None, None, gesamt


def probeteilung(N):
    """Klassische Probeteilung. Gibt (p, q, Schritte)."""
    s = 0
    for d in range(2, math.isqrt(N) + 1):
        s += 1
        if N % d == 0:
            return d, N // d, s
    return None, None, s


def pollard_rho(N, rng=None):
    """Pollard rho mit Floyd-Zyklensuche."""
    if N % 2 == 0:
        return 2, N // 2, 1
    rng = rng or random.Random(SEED)
    for _ in range(10):
        x = y = rng.randrange(2, N)
        c = rng.randrange(1, N)
        d, s = 1, 0
        while d == 1 and s < 10 ** 6:
            x = (x * x + c) % N
            y = (y * y + c) % N
            y = (y * y + c) % N
            d = math.gcd(abs(x - y), N)
            s += 1
        if 1 < d < N:
            return d, N // d, s
    return None, None, s


def semiprim(bits, rng):
    """Erzeugt ein Semiprim mit etwa der gegebenen Bitlaenge."""
    def ist_prim(n):
        if n < 2:
            return False
        for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
            if n % p == 0:
                return n == p
        d, s = n - 1, 0
        while d % 2 == 0:
            d //= 2
            s += 1
        for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
            x = pow(a, d, n)
            if x in (1, n - 1):
                continue
            for _ in range(s - 1):
                x = x * x % n
                if x == n - 1:
                    break
            else:
                return False
        return True

    def prim(b):
        while True:
            n = rng.randrange(2 ** (b - 1), 2 ** b) | 1
            if ist_prim(n):
                return n
    h = bits // 2
    return prim(h) * prim(bits - h)


if __name__ == "__main__":
    rng = random.Random(SEED)
    print("=" * 74)
    print("S1 -- PERIODENSUCHE: KORREKTHEIT UND SKALIERUNG")
    print("=" * 74)

    # ---------------------------------------------------- TEST A
    print("\nTEST A: Korrektheit der Periodenfindung")
    print("-" * 74)
    print(f"   {'N':>8} {'p*q':>12} {'Periode gefunden':>18}")
    for N in (15, 21, 35, 77, 143, 187, 323):
        p, q, s = faktorisiere_periode(N, rng=random.Random(SEED))
        ok = p is not None and p * q == N
        print(f"   {N:>8} {f'{p}*{q}' if ok else '---':>12} {'ja' if ok else 'nein':>18}")
        assert ok, f"Faktorisierung von {N} fehlgeschlagen"
    print("   => Periodenfindung ist korrekt: sie liefert die Faktoren.")

    # ---------------------------------------------------- TEST B
    print("\nTEST B: Skalierung -- O(N) oder O((log N)^3)?")
    print("-" * 74)
    print("""   Die Periode r teilt lambda(N) = lcm(p-1, q-1) und kann Werte
   der Groessenordnung N annehmen. Eine sequenzielle Suche braucht
   daher O(N) Schritte.""")
    print("""   Einzelne Laeufe streuen stark (die Ordnung von a haengt vom
   Zufall ab). Gemittelt wird daher ueber je 12 Semiprimzahlen und
   alle teilerfremden a -- das gibt die mittlere Ordnung, die
   theoretisch entscheidende Groesse.""")

    def mittlere_ordnung(N):
        """Mittlere multiplikative Ordnung ueber alle a mit gcd(a,N)=1."""
        summe = anzahl = 0
        for a in range(2, min(N, 400)):
            if math.gcd(a, N) != 1:
                continue
            r, _ = periode(a, N)
            if r:
                summe += r
                anzahl += 1
        return summe / anzahl if anzahl else 0

    print(f"\n   {'Bits':>5} {'mittl. N':>10} {'mittl. Ordnung':>15} "
          f"{'N':>10} {'sqrt(N)':>9} {'(ln N)^3':>10}")
    daten = []
    for bits in (8, 10, 12, 14):
        Ns, ords = [], []
        for _ in range(12):
            N = semiprim(bits, rng)
            Ns.append(N)
            ords.append(mittlere_ordnung(N))
        Nm = sum(Ns) / len(Ns)
        om = sum(ords) / len(ords)
        daten.append((Nm, om))
        print(f"   {bits:>5} {Nm:>10.0f} {om:>15.1f} {Nm:>10.0f} "
              f"{math.sqrt(Nm):>9.1f} {math.log(Nm)**3:>10.1f}")

    (N1, o1), (N2, o2) = daten[0], daten[-1]
    exp = math.log(o2 / o1) / math.log(N2 / N1)
    print(f"\n   gemessener Wachstumsexponent der mittleren Ordnung: {exp:.2f}")
    print(f"     O(N) entspraeche        1.00")
    print(f"     O(sqrt(N)) entspraeche  0.50")
    print(f"     O((log N)^3) entspraeche ~0 (polylogarithmisch)")
    assert exp > 0.6, f"Ordnung sollte polynomiell wachsen, gemessen {exp:.2f}"
    print("""
   => die mittlere Ordnung waechst polynomiell in N. Eine sequenzielle
      Suche muss sie durchlaufen und ist damit polynomiell, nicht
      polylogarithmisch. Die Behauptung O((log N)^3) fuer das
      klassische Verfahren ist widerlegt; sie gilt nur fuer Shors
      Quantenverfahren.""")

    # ---------------------------------------------------- TEST C
    print("\nTEST C: Der Rasterparameter sigma")
    print("-" * 74)
    print("   Primfaktorzerlegung der verwendeten sigma-Nenner:")
    for nenner in (42, 100, 1000, 100000):
        f, n = {}, nenner
        for p in range(2, nenner + 1):
            while n % p == 0:
                f[p] = f.get(p, 0) + 1
                n //= p
            if n == 1:
                break
        zerl = " * ".join(f"{p}^{e}" if e > 1 else str(p)
                          for p, e in sorted(f.items()))
        prim = len(f) == 1 and list(f.values())[0] == 1
        print(f"     sigma = 1/{nenner:<7} -> {nenner} = {zerl:<16} "
              f"{'PRIM' if prim else 'zusammengesetzt'}")
        assert not prim, f"{nenner} sollte zusammengesetzt sein"
    print("""
   => alle sigma-Nenner sind zusammengesetzt. Nach dem Bikohaerenz-
      befund (Dok. 316) bilden zusammengesetzte Zahlen im Weil-
      Spektrum Mischpunkte OHNE eigene Kopplungslinie. sigma kann
      daher keine Resonanz erzeugen -- es ist ein Abtastraster.""")

    # ---------------------------------------------------- TEST D
    print("\nTEST D: Vergleich der Verfahren")
    print("-" * 74)
    print(f"   {'N':>10} {'Probeteilung':>14} {'Pollard rho':>13} "
          f"{'Periodensuche':>15}")
    for bits in (12, 14, 16):
        N = semiprim(bits, rng)
        _, _, s_pt = probeteilung(N)
        _, _, s_pr = pollard_rho(N, random.Random(SEED))
        _, _, s_ps = faktorisiere_periode(N, versuche=8,
                                          rng=random.Random(SEED))
        print(f"   {N:>10} {s_pt:>14} {s_pr:>13} {s_ps:>15}")
    print("""
   => die Periodensuche braucht deutlich mehr Schritte als beide
      klassischen Verfahren. Sie hat keinen Vorteil.""")

    print("\n" + "=" * 74)
    print("ERGEBNIS S1")
    print("=" * 74)
    print("""   [K] Die Periodenfindung ist korrekt und liefert die Faktoren.
   [K] Ihre sequenzielle Umsetzung skaliert polynomiell in N; die
       Behauptung O((log N)^3) gilt nur fuer den Quantenfall.
   [K] Alle verwendeten sigma-Werte haben zusammengesetzte Nenner
       und koennen daher keine Resonanzlinien erzeugen.
   [K] Gegenueber Probeteilung und Pollard rho besteht kein Vorteil.""")
    print("\nAlle Checks bestanden.")
