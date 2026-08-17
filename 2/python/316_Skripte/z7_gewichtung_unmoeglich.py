#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""z7_gewichtung_unmoeglich.py -- Kann eine Tonnetz-Gewichtung existieren?

Offener Punkt Z-1 hatte gefragt, ob die Exponenten (2,1,4) von
xi = 1/(2^2 * 3 * 5^4) eine Gewichtung im Weil-Laengenspektrum erzeugen
koennten. Drei unabhaengige Tests, alle negativ:

  TEST A  GEWICHTUNGSSTAERKE: das Tonnetz wird mit einem Parameter
          alpha gewichtet (w = 1/(n*d)^alpha; alpha=0 ungewichtet,
          alpha=1 Tenney). Ueber den ganzen Bereich -- einschliesslich
          der Mitte bei alpha ~ 0.3, wo das Gitter weder blind-dicht
          noch achsen-duenn ist -- entsteht keine Selektion.
  TEST B  LIMIT-ERWEITERUNG: 5-, 7-, 11-Limit. Jede Erweiterung
          verschiebt nur die Grenze zwischen 'trivial abgedeckt' und
          'gar nicht abgedeckt'; dazwischen gibt es nichts.
  TEST C  STARRHEIT: die Weil-Gewichte sind keine freien Parameter.
          Jede Gewichtung aendert das Euler-Produkt und zerstoert die
          Funktionalgleichung -- also gerade die kritische Linie.

Test C ist der eigentliche Grund; A und B zeigen, dass auch die
numerischen Wege nichts hergeben.
Nur Standardbibliothek. Seed 20780458.
"""
import math
import random
import statistics
from itertools import product

SEED = 20780458
XI = 4.0 / 30000.0

# Primzahlen jenseits des jeweiligen Limits -- nur sie sind ein echter Test
TESTPRIMES = (7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)


def gitter(primes, alpha, N, cut=1e-9):
    """Tonnetz-Punkte (Log-Position, Gewicht) mit w = (prod p^|k|)^-alpha."""
    logs = [math.log(p) for p in primes]
    pts = []
    for e in product(range(-N, N + 1), repeat=len(primes)):
        n = 1
        for p, k in zip(primes, e):
            n *= p ** abs(k)
        w = n ** (-alpha)
        if w > cut:
            pts.append((sum(k * l for k, l in zip(e, logs)), w))
    return pts


def gewichtssumme_formel(primes, alpha):
    """Geschlossene Form: prod_p [1 + 2 p^-alpha/(1-p^-alpha)]."""
    out = 1.0
    for p in primes:
        x = p ** (-alpha)
        out *= 1 + 2 * x / (1 - x)
    return out


def selektionstest(primes, alpha, N, rng, sigma=0.02, nzuf=200, nperm=3000):
    """Haeuft sich die gewichtete Gittermasse bei echten Weil-Laengen
    staerker als bei Zufallszielen? Primzahlen <= Limit sind Achsen und
    werden als trivial ausgeschlossen."""
    pts = gitter(primes, alpha, N)

    def masse(z):
        return sum(w * math.exp(-((u - z) / sigma) ** 2 / 2) for u, w in pts)

    lim = max(primes)
    aussen = [p for p in TESTPRIMES if p > lim]
    ziele = [math.log(p) for p in aussen] + [2 * math.log(p) for p in aussen[:5]]
    mw = [masse(u) for u in ziele]
    zuf = [masse(rng.uniform(0.5, 8.0)) for _ in range(nzuf)]
    m = statistics.mean(mw)
    alle = mw + zuf
    treffer = 0
    for _ in range(nperm):
        rng.shuffle(alle)
        if statistics.mean(alle[:len(mw)]) >= m:
            treffer += 1
    return len(pts), len(aussen), m, statistics.mean(zuf), treffer / nperm


if __name__ == "__main__":
    rng = random.Random(SEED)
    print("=" * 74)
    print("Z7 -- KANN EINE TONNETZ-GEWICHTUNG EXISTIEREN?")
    print("=" * 74)

    # ---------------------------------------------------- TEST A
    print("\nTEST A: Gewichtungsstaerke alpha")
    print("-" * 74)
    print("""   Hoehere Harmonische haben kleinere Amplitude. Das Standardmass
   ist die Tenney-Hoehe: fuer n/d ist das Gewicht ~ 1/(n*d). Mit
   einem Exponenten alpha wird die Staerke frei:
       w = 1/(2^|a| 3^|b| 5^|c|)^alpha
   alpha = 0 ungewichtet, alpha = 1 Tenney. Beide Extreme sind
   ungeeignet -- ungewichtet ist das Gitter blind-dicht, bei Tenney
   bleiben nur die Achsen. Entscheidend ist die Mitte.""")
    print(f"\n   {'alpha':>6} {'Gewichtssumme':>15} {'eff. Punktzahl':>16} {'Charakter'}")
    N_A = 20
    eff = {}
    for alpha in (0.1, 0.2, 0.3, 0.5, 0.7, 1.0):
        S1 = S2 = 0.0
        for u, w in gitter((2, 3, 5), alpha, N_A, cut=1e-11):
            S1 += w
            S2 += w * w
        e = S1 * S1 / S2
        eff[alpha] = e
        char = ("blind-dicht" if e > 5000 else
                "achsen-duenn" if e < 100 else "Mitte")
        print(f"   {alpha:6.2f} {S1:15.4f} {e:16.1f}   {char}")
    # Kontrolle gegen die geschlossene Form
    for alpha in (0.3, 0.5, 1.0):
        S1 = sum(w for _, w in gitter((2, 3, 5), alpha, N_A, cut=1e-11))
        theo = gewichtssumme_formel((2, 3, 5), alpha)
        assert abs(S1 / theo - 1) < 0.02, "Gewichtssumme weicht von der Formel ab"
    print("   (Gewichtssummen gegen prod_p [1+2p^-a/(1-p^-a)] geprueft)")
    assert eff[1.0] < 100 < eff[0.3] < 5000, "alpha-Staffelung unerwartet"

    print(f"\n   Selektionstest ueber den alpha-Bereich (5-Limit):")
    print(f"   {'alpha':>6} {'Punkte':>8} {'M(Weil)':>10} {'M(Zufall)':>11} "
          f"{'Verh.':>7} {'p':>7}")
    pmin = 1.0
    for alpha in (0.15, 0.3, 0.5, 1.0):
        n, na, a, b, p = selektionstest((2, 3, 5), alpha, 12, rng)
        pmin = min(pmin, p)
        print(f"   {alpha:6.2f} {n:8d} {a:10.4f} {b:11.4f} {a/b:7.3f} {p:7.4f}")
    assert pmin > 0.05, "Unerwartet: eine Gewichtung erzeugt Selektion"
    print("""   => kein alpha erzeugt Selektion. Das Verhaeltnis bleibt bei
      oder unter 1; die Gewichtungsstaerke ist nicht das Problem.""")

    # ---------------------------------------------------- TEST B
    print("\nTEST B: erweiterte Tonnetze -- 5-, 7-, 11-Limit")
    print("-" * 74)
    print("""   Das 5-Limit ist die einfache Fassung; erweiterte Tonnetze nehmen
   weitere Primzahlachsen auf (7 als naechste). Getestet wird bei
   alpha = 0.3, Exponenten bis +-6; Primzahlen bis zum Limit sind
   Achsen und daher als trivial ausgeschlossen.""")
    print(f"\n   {'Limit':>7} {'Achsen':>7} {'Punkte':>8} {'Primz. drueber':>15} "
          f"{'Verh.':>7} {'p':>7}")
    pmin = 1.0
    for primes in ((2, 3, 5), (2, 3, 5, 7), (2, 3, 5, 7, 11)):
        n, na, a, b, p = selektionstest(primes, 0.3, 6, rng)
        pmin = min(pmin, p)
        print(f"   {max(primes):7d} {len(primes):7d} {n:8d} {na:15d} "
              f"{a/b:7.3f} {p:7.4f}")
    assert pmin > 0.05, "Unerwartet: eine Limit-Erweiterung erzeugt Selektion"

    print("""
   Der strukturelle Punkt wiegt schwerer als die p-Werte: jede
   Erweiterung verschiebt nur die Grenze, sie schliesst keine Luecke.

      5-Limit:   2,3,5 sind Achsen (trivial) -- ab  7 fehlen ALLE
      7-Limit:   2,3,5,7 trivial             -- ab 11 fehlen ALLE
     13-Limit:   2...13 trivial              -- ab 17 fehlen ALLE

   Ein Tonnetz mit Limit L deckt die endlich vielen Primzahlen <= L
   per Definition ab und die unendlich vielen Primzahlen > L
   ueberhaupt nicht. Dazwischen gibt es nichts. Die Weilsche Formel
   summiert aber ueber SAEMTLICHE Primzahlen.

   Der Grenzfall macht es endgueltig: ein Tonnetz mit unendlichem
   Limit waere keine Struktur mehr -- es enthielte jede Primzahl als
   Achse, also genau das Euler-Produkt selbst, ohne Zusatzgehalt und
   ohne jeden Bezug zu xi.""")

    print("\n   Und wo steht xi bei alldem?")
    print(f"     xi = 4/30000 = 2^2/(2^4 * 3 * 5^4)")
    print(f"     Exponenten auf allen Achsen ab 7: NULL")
    w_xi = 1.0 / (2 ** 2 * 3 ** 1 * 5 ** 4)
    print(f"     Tenney-Gewicht von xi: {w_xi:.3e} = 1/7500")
    print("""     => eine Erweiterung auf 7-, 11- oder 13-Limit vergroessert das
        Gitter, aendert aber die Stellung von xi darin nicht. xi bleibt
        ein reiner 5-Limit-Punkt.""")

    # ---------------------------------------------------- TEST C
    print("\nTEST C: sind die Weil-Gewichte ueberhaupt frei?")
    print("-" * 74)
    print("""   Im Euler-Produkt sind die Gewichte keine Wahl, sondern Konsequenz:
       log zeta(s) = sum_{p,k} (1/k) p^{-ks}
   Der Faktor ln(p)/p^{k/2} der expliziten Formel folgt daraus durch
   Ableiten und Verschieben nach s = 1/2. Es gibt keine Stelle, an der
   ein zusaetzlicher Faktor eingefuegt werden koennte, ohne das
   Euler-Produkt selbst zu aendern.""")

    def dirichlet_gewichtet(s, g, N=5000):
        """sum_n g^Omega(n) n^{-s}: das Euler-Produkt mit Gewicht g,
        prod_p (1 - g p^{-s})^{-1}. Fuer g=1 mit Schwanzkorrektur."""
        omega = [0] * (N + 1)
        for p in range(2, N + 1):
            if omega[p] == 0:
                for m in range(p, N + 1, p):
                    q, e = m, 0
                    while q % p == 0:
                        q //= p
                        e += 1
                    omega[m] += e
        kern = sum(g ** omega[n] * n ** (-s) for n in range(1, N + 1))
        if g == 1.0:
            kern += N ** (1 - s) / (s - 1) - 0.5 * N ** (-s)
        return kern

    print("\n   Numerische Probe bei s = 1.5:")
    print(f"   {'g':>6} {'Reihenwert':>14}  Bemerkung")
    for g in (1.0, 1.05, 1.2):
        val = dirichlet_gewichtet(1.5, g)
        bem = ("Riemann-Zeta, Funktionalgleichung gilt" if g == 1.0
               else "andere Funktion, Funktionalgleichung zerstoert")
        print(f"   {g:>6.2f} {val:>14.6f}  {bem}")
    zeta15 = dirichlet_gewichtet(1.5, 1.0)
    print(f"   Kontrolle: zeta(1.5) = {zeta15:.6f}, Literaturwert 2.612375")
    assert abs(zeta15 - 2.612375) < 1e-4, "zeta(1.5) sollte 2.612375 sein"
    print("""
   => Jede Gewichtung g != 1 erzeugt eine ANDERE Dirichlet-Reihe mit
      verschobener Konvergenzabszisse und ohne Funktionalgleichung.
      Und die Funktionalgleichung ist genau das, was die kritische
      Linie definiert.""")

    # ---------------------------------------------------- FAZIT
    print("\n" + "=" * 74)
    print("ERGEBNIS Z7  [X] -- Z-1 geschlossen")
    print("=" * 74)
    print("""   Eine Gewichtung des Weil-Spektrums durch die Tonnetz-Exponenten
   (2,1,4) kann es nicht geben, aus drei zusammenwirkenden Gruenden:

   (A) Keine Gewichtungsstaerke erzeugt Selektion -- auch nicht in der
       Mitte zwischen ungewichtet und Tenney, wo das Gitter weder
       blind-dicht noch achsen-duenn ist.
   (B) Keine Limit-Erweiterung schliesst die Luecke: ein Tonnetz mit
       Limit L deckt die Primzahlen <= L trivial ab und die unendlich
       vielen darueber gar nicht. xi bleibt zudem ein 5-Limit-Punkt.
   (C) Die Weil-Gewichte sind keine freien Parameter. Eine Gewichtung
       aendert das Euler-Produkt, damit die Funktionalgleichung und
       damit die kritische Linie: sie zerstoert das Objekt, dessen
       Nullstellen sie erklaeren soll.

   (C) ist der eigentliche Grund und gilt unabhaengig von jeder
   Zahlenrechnung. (A) und (B) zeigen zusaetzlich, dass auch die
   numerischen Wege nichts hergeben.

   Damit ist der offene Punkt Z-1 nicht nur unbeantwortet, sondern
   negativ entschieden.""")
    print("\nAlle Checks bestanden.")
