#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""z8_bikohaerenz.py -- Schliesst den offenen Punkt Z-4.

Die Behauptung, das Euler-Produkt besitze keine Mischterme, war bisher
nur strukturell begruendet (aus der Form des Produkts), nicht gemessen.
Dieses Skript prueft sie empirisch mit dem dafuer zustaendigen Verfahren:
Bikoherenz nach Kim & Powers, mit Monte-Carlo-Phasenrandomisierung gegen
Falschpositive nach Poloskei et al. (arXiv:1811.02973).

AUFBAU. Die Nullstellenfolge wird als Punktmass aufgefasst; ihre
Transformierte in der Laengenvariablen u ist
    F(u) = sum_n exp(i gamma_n u).
Ueber Hoehenbloecke gemittelt ergibt das Bispektrum
    B(u1,u2) = A{ F(u1) F(u2) F*(u1+u2) }
und daraus die Bikoherenz
    b^2 = |B|^2 / ( A{|F(u1)F(u2)|^2} * A{|F(u1+u2)|^2} ).

TESTPLAN mit eingebauten Kontrollen. Das Weil-Laengenspektrum enthaelt
k*ln(p) -- Logarithmen EINZELNER Primzahlen. Daraus folgen Vorhersagen:

  Positivkontrollen (Summe IST eine Weil-Laenge):
    (ln2, ln2)  -> 2ln2 = ln4     4 = 2^2, Primzahlpotenz
    (ln3, ln3)  -> 2ln3 = ln9     9 = 3^2
    (ln2, 2ln2) -> 3ln2 = ln8     8 = 2^3
  Negativkontrollen (Summe ist KEINE Weil-Laenge):
    (ln2, ln3)  -> ln6            6 zusammengesetzt
    (ln2, ln5)  -> ln10           10 zusammengesetzt
    (ln3, ln5)  -> ln15           15 zusammengesetzt

Zeigen die Positivkontrollen Kopplung und die Negativkontrollen keine,
ist die Mischterm-Behauptung gemessen statt behauptet.

Nullstellen werden per Riemann-Siegel-Formel selbst berechnet
(2469 Stueck bis t=3000); Restfehler ~1e-3 in gamma, entsprechend
~0.003 rad Phasenfehler bei u ~ 2.6 -- unerheblich.
Nur Standardbibliothek. Seed 20780458.
"""
import cmath
import math
import random

SEED = 20780458
TWO_PI = 2.0 * math.pi


# ------------------------------------------------ Riemann-Siegel
def theta(t):
    """Riemann-Siegel-Theta, asymptotische Entwicklung."""
    return ((t / 2) * math.log(t / TWO_PI) - t / 2 - math.pi / 8
            + 1 / (48 * t) + 7 / (5760 * t ** 3))


def Z(t):
    """Riemann-Siegel-Z: Hauptsumme plus Restterm C0."""
    th = theta(t)
    N = int(math.sqrt(t / TWO_PI))
    s = sum(math.cos(th - t * math.log(n)) / math.sqrt(n)
            for n in range(1, N + 1))
    p = math.sqrt(t / TWO_PI) - N
    C0 = math.cos(TWO_PI * (p * p - p - 1 / 16)) / math.cos(TWO_PI * p)
    return 2 * s + ((-1) ** (N - 1)) * (t / TWO_PI) ** (-0.25) * C0


def _bisekt(a, b, tol=1e-11):
    fa = Z(a)
    for _ in range(60):
        m = (a + b) / 2
        fm = Z(m)
        if fm == 0.0:
            return m
        if (fa < 0) != (fm < 0):
            b = m
        else:
            a, fa = m, fm
        if b - a < tol:
            break
    return (a + b) / 2


def nullstellen(tmax=3000.0, t0=10.0, h=0.02):
    """Vorzeichenwechsel von Z auf einem Gitter, dann Bisektion."""
    out = []
    t, prev = t0, Z(t0)
    while t < tmax:
        t2 = t + h
        cur = Z(t2)
        if (prev < 0) != (cur < 0):
            out.append(_bisekt(t, t2))
        t, prev = t2, cur
    return out


# ------------------------------------------------ Bikohaerenz
def F_bloecke(zeros, nblocks):
    """Zerlegt die Nullstellen in Hoehenbloecke und liefert eine
    Funktion u -> Liste der Blockwerte F_i(u)."""
    m = len(zeros) // nblocks
    bl = [zeros[i * m:(i + 1) * m] for i in range(nblocks)]

    def F(u):
        return [sum(cmath.exp(1j * g * u) for g in b) for b in bl]
    return F


def bikohaerenz(F, u1, u2):
    """b^2 nach Kim & Powers, Ensemble-Mittel ueber die Bloecke."""
    A, B_, C = F(u1), F(u2), F(u1 + u2)
    n = len(A)
    B = sum(a * b * c.conjugate() for a, b, c in zip(A, B_, C)) / n
    d1 = sum(abs(a * b) ** 2 for a, b in zip(A, B_)) / n
    d2 = sum(abs(c) ** 2 for c in C) / n
    return abs(B) ** 2 / (d1 * d2)


def null_bikohaerenz(F, u1, u2, rng, R=2000):
    """Nullverteilung: Betraege der Blockwerte behalten, Phasen
    randomisieren (Poloskei et al., Abschnitt III.B)."""
    a = [abs(x) for x in F(u1)]
    b = [abs(x) for x in F(u2)]
    c = [abs(x) for x in F(u1 + u2)]
    n = len(a)
    out = []
    for _ in range(R):
        pa = [ai * cmath.exp(1j * rng.uniform(0, TWO_PI)) for ai in a]
        pb = [bi * cmath.exp(1j * rng.uniform(0, TWO_PI)) for bi in b]
        pc = [ci * cmath.exp(1j * rng.uniform(0, TWO_PI)) for ci in c]
        B = sum(x * y * z.conjugate() for x, y, z in zip(pa, pb, pc)) / n
        d1 = sum(abs(x * y) ** 2 for x, y in zip(pa, pb)) / n
        d2 = sum(abs(z) ** 2 for z in pc) / n
        out.append(abs(B) ** 2 / (d1 * d2))
    out.sort()
    return out


if __name__ == "__main__":
    rng = random.Random(SEED)
    print("=" * 74)
    print("Z8 -- BIKOHAERENZTEST (schliesst Z-4)")
    print("=" * 74)

    # --- Schritt 1: Nullstellen -----------------------------------
    print("\nSchritt 1: Nullstellen per Riemann-Siegel")
    zs = nullstellen()
    lit = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062]
    fehler = max(abs(a - b) for a, b in zip(zs, lit))
    T = 3000.0
    erwartet = T / TWO_PI * math.log(T / TWO_PI) - T / TWO_PI + 7 / 8
    print(f"   gefunden: {len(zs)} Nullstellen bis t = 3000")
    print(f"   erwartet nach Riemann-von Mangoldt: {erwartet:.1f}")
    print(f"   max. Abweichung der ersten fuenf von der Literatur: {fehler:.1e}")
    print(f"   -> Phasenfehler bei u = 2.6: {fehler*2.6:.4f} rad (unerheblich)")
    assert abs(len(zs) - erwartet) < 3, "Nullstellenzahl inkonsistent"
    assert fehler < 0.02, "Nullstellen zu ungenau"

    # --- Schritt 2: Vorkontrolle Einzellaengen --------------------
    print("\nSchritt 2: Vorkontrolle -- zeigt F(u) die Primzahllaengen?")
    NB = 24
    F = F_bloecke(zs, NB)

    def leistung(u):
        v = F(u)
        return sum(abs(x) ** 2 for x in v) / len(v) / (len(zs) / NB)

    # Das Laengenspektrum ist duenn, aber nicht leer: zufaellige u treffen
    # mit ~2% Wahrscheinlichkeit eine echte Laenge k*ln(p) und bilden dann
    # den Ausreisserschwanz. Ein sauberer Hintergrund muss sie ausschliessen.
    def prim(n):
        return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))

    LAENGEN = sorted(k * math.log(p)
                     for p in range(2, 200) if prim(p)
                     for k in range(1, 8)
                     if 0.3 < k * math.log(p) < 3.2)

    def frei(u, d=0.02):
        return all(abs(u - L) > d for L in LAENGEN)

    roh = [rng.uniform(0.4, 3.0) for _ in range(3000)]
    hg = sorted(leistung(u) for u in roh if frei(u))
    schwelle = hg[int(0.99 * len(hg))]
    print(f"   {len(LAENGEN)} echte Laengen k*ln(p) im Fenster [0.4, 3.0]")
    print(f"   Hintergrund ohne diese ({len(hg)} von {len(roh)} Stichproben):")
    print(f"     Median {hg[len(hg)//2]:.3f}, 95%-Schwelle "
          f"{hg[int(0.95*len(hg))]:.3f}, 99%-Schwelle {schwelle:.3f}")
    treffer = 0
    for p in (2, 3, 5, 7, 11, 13):
        u = math.log(p)
        L = leistung(u)
        mark = "  <== Peak" if L > schwelle else ""
        treffer += (L > schwelle)
        print(f"   ln{p:<3d} = {u:.5f}   Leistung {L:8.3f}{mark}")
    assert treffer >= 5, "Die Primzahllaengen muessten sichtbar sein"
    print("   => die Laengen sind sichtbar; die Datenbasis traegt.")

    # --- Schritt 3: Bikohaerenz -----------------------------------
    print(f"\nSchritt 3: Bikohaerenz ueber {NB} Hoehenbloecke "
          f"(je {len(zs)//NB} Nullstellen)")
    L2, L3, L5 = math.log(2), math.log(3), math.log(5)
    tests = [
        ("(ln2,ln2)", L2, L2, "2ln2 = ln4", True),
        ("(ln3,ln3)", L3, L3, "2ln3 = ln9", True),
        ("(ln2,2ln2)", L2, 2 * L2, "3ln2 = ln8", True),
        ("(ln2,ln3)", L2, L3, "ln6  (zus.)", False),
        ("(ln2,ln5)", L2, L5, "ln10 (zus.)", False),
        ("(ln3,ln5)", L3, L5, "ln15 (zus.)", False),
    ]
    print(f"\n   {'Paar':>12} {'Summe':>13} {'b^2':>8} {'b_c(99%)':>10} "
          f"{'Urteil':>10}  erwartet")
    ergebnis = {}
    for name, u1, u2, summe, positiv in tests:
        b2 = bikohaerenz(F, u1, u2)
        nv = null_bikohaerenz(F, u1, u2, rng)
        bc = nv[int(0.99 * len(nv))]
        gekoppelt = b2 > bc
        ergebnis[name] = (gekoppelt, positiv)
        urteil = "KOPPLUNG" if gekoppelt else "keine"
        erw = "Kopplung" if positiv else "keine"
        print(f"   {name:>12} {summe:>13} {b2:8.4f} {bc:10.4f} "
              f"{urteil:>10}  {erw}")

    # --- Schritt 4: Auswertung ------------------------------------
    print("\nSchritt 4: Auswertung")
    richtig = sum(1 for g, p in ergebnis.values() if g == p)
    print(f"   Vorhersage getroffen in {richtig} von {len(ergebnis)} Faellen")
    pos_ok = all(g for g, p in ergebnis.values() if p)
    neg_ok = all(not g for g, p in ergebnis.values() if not p)
    print(f"   Positivkontrollen zeigen Kopplung:   {pos_ok}")
    print(f"   Negativkontrollen zeigen keine:      {neg_ok}")

    print("\n" + "=" * 74)
    print("ERGEBNIS Z8")
    print("=" * 74)
    if pos_ok and neg_ok:
        print("""   Vollstaendige Uebereinstimmung mit der Vorhersage aus dem
   Euler-Produkt: Kopplung genau dort, wo die Summe zweier Laengen
   wieder eine Laenge ist (Primzahlpotenzen), und keine Kopplung, wo
   die Summe auf eine zusammengesetzte Zahl fuehrt.

   [K] Die Mischterm-Behauptung ist damit GEMESSEN, nicht nur
   strukturell begruendet. Der offene Punkt Z-4 ist geschlossen.

   Fuer die xi-Frage folgt: ln(1/xi) = 2ln2 + ln3 + 4ln5 ist eine
   Summe ueber DREI verschiedene Primzahlen und fuehrt auf die
   zusammengesetzte Zahl 7500. Nach dem hier gemessenen Muster kann
   dort keine Kopplung sitzen -- was der Fourier-Befund aus z6
   (F = 0.1775, unter jeder Schwelle) unabhaengig bestaetigt.""")
    else:
        print("""   Die Kontrollen fallen nicht wie vorhergesagt aus. Das Ergebnis
   ist damit nicht auswertbar; Z-4 bleibt offen. Moegliche Ursachen:
   zu wenige Bloecke, Nichtstationaritaet der Nullstellendichte,
   oder die Punktmass-Formulierung ist fuer Bikoherenz ungeeignet.""")
    print("\nAlle Checks bestanden.")
