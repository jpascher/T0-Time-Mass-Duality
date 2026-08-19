#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""z11_alphorn.py -- Die Naturtonreihe als physikalischer Beleg.

Das Alphorn hat keine Ventile und keine Grifflöcher; es spielt die
Naturtonreihe n*f0 unverstellt. Damit ist es der physikalische Fall
derselben Struktur, die Dok. 316 arithmetisch untersucht:

  TEIL A  PRIMZAHLEN ALS GENERATOREN. Unter den Naturtoenen fuehren
          genau die Primzahl-Ordnungen neue Klangqualitaeten ein;
          zusammengesetzte Ordnungen sind Kombinationen bereits
          vorhandener. Das ist die Euler-Produkt-Struktur, hoerbar.
  TEIL B  DAEMPFUNG ALS TENNEY-ANALOGON. Hohe Ordnungen tragen wenig
          Amplitude -- die akustische Entsprechung der
          Gewichtungsfrage aus z7.
  TEIL C  WINDUNGSZAHL, NICHT FREQUENZVERHAELTNIS. Fuer die
          Torus-Topologie zaehlt der Logarithmus des Verhaeltnisses,
          nicht das Verhaeltnis. Wer beides verwechselt, kehrt die
          Aussage um: rein gestimmt schliesst NICHT, temperiert
          schliesst.
  TEIL D  CENT-BUCHHALTUNG. Theoretische Abweichung und
          instrumentenbedingte Verschiebung sind getrennt zu fuehren;
          Addition beider ergibt die Nettoabweichung.

Nur Standardbibliothek.
"""
import math
from fractions import Fraction

CENT = 1200.0 / math.log(2.0)


def prim(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


def cent(v):
    """Verhaeltnis -> Cent."""
    return CENT * math.log(v)


def oktavreduziert(n):
    """Naturton n auf die Oktave [1,2) reduziert."""
    x = float(n)
    while x >= 2:
        x /= 2
    return x


if __name__ == "__main__":
    print("=" * 74)
    print("Z11 -- DIE NATURTONREIHE ALS PHYSIKALISCHER BELEG")
    print("=" * 74)

    # ---------------------------------------------------- TEIL A
    print("\nTEIL A: Primzahlen als Generatoren der Naturtonreihe")
    print("-" * 74)
    print(f"   {'n':>3} {'okt.red.':>10} {'Cent':>8}  Rolle")
    gesehen = set()
    for n in range(1, 18):
        r = oktavreduziert(n)
        if n == 1:
            rolle = "Grundton"
        elif prim(n):
            rolle = f"PRIMZAHL -- neue Achse"
            gesehen.add(n)
        else:
            # Zerlegung in bereits vorhandene Faktoren
            f, m = [], n
            for p in range(2, n + 1):
                while m % p == 0:
                    f.append(p)
                    m //= p
            rolle = "= " + "*".join(map(str, f)) + " -- Kombination"
        print(f"   {n:>3} {r:10.5f} {cent(r):8.1f}  {rolle}")
    print(f"""
   Die Primzahlen bis 17 sind {sorted(gesehen)}. Nur sie fuehren
   Klangqualitaeten ein, die nicht aus tieferen Ordnungen
   zusammensetzbar sind: 4 = 2*2 ist Oktave der Oktave, 6 = 2*3
   Oktave der Quinte, 9 = 3*3 Quinte der Quinte. Das ist die
   Euler-Produkt-Struktur -- jede Primzahl steht fuer sich, die
   zusammengesetzten sind Produkte.""")
    assert sorted(gesehen) == [2, 3, 5, 7, 11, 13, 17], "Primzahlliste falsch"

    # ---------------------------------------------------- TEIL B
    print("\nTEIL B: Amplitudenabfall als akustisches Tenney-Analogon")
    print("-" * 74)
    print("""   Hohe Naturtoene sind schwerer anzublasen und tragen weniger
   Amplitude. Formal entspricht das der Gewichtung aus z7: die
   Tenney-Hoehe gewichtet ein Verhaeltnis n/d mit 1/(n*d).""")
    print(f"\n   {'n':>3} {'1/n (idealisiert)':>18} {'Tenney 1/n':>12}")
    for n in (1, 2, 3, 5, 7, 11, 13, 17):
        print(f"   {n:>3} {1.0/n:18.5f} {1.0/n:12.5f}")
    print("""   Beide Skalen fallen wie 1/n. Der physikalische Grund
   (abnehmende bewegte Luftmasse) und der zahlentheoretische
   (zunehmende harmonische Distanz) fuehren auf dieselbe Form.""")

    # ---------------------------------------------------- TEIL C
    print("\nTEIL C: Windungszahl statt Frequenzverhaeltnis")
    print("-" * 74)
    print("""   Fuer Bahnen auf dem Torus zaehlt die WINDUNGSZAHL -- der
   Bruchteil des Zyklus, also der Logarithmus zur Oktavbasis --,
   nicht das Frequenzverhaeltnis selbst. Die Verwechslung kehrt die
   Aussage um.""")
    q_rein = 1.5
    q_temp = 2 ** (7 / 12)
    print(f"\n   {'Quinte':>14} {'Verhaeltnis':>14} {'Art':>12} "
          f"{'Windungszahl':>14} {'Art':>12}")
    print(f"   {'rein 3/2':>14} {q_rein:14.10f} {'rational':>12} "
          f"{math.log2(q_rein):14.10f} {'IRRATIONAL':>12}")
    print(f"   {'temperiert':>14} {q_temp:14.10f} {'irrational':>12} "
          f"{math.log2(q_temp):14.10f} {'RATIONAL 7/12':>12}")
    assert abs(math.log2(q_temp) - 7 / 12) < 1e-15, "7/12 erwartet"

    print("\n   Probe: 12 Quinten aufwaerts, Oktaven herausgerechnet")
    for name, q in (("rein 3/2", q_rein), ("temperiert", q_temp)):
        x = 1.0
        for _ in range(12):
            x *= q
            while x >= 2:
                x /= 2
        zu = abs(x - 1) < 1e-12
        print(f"     {name:12s}: Endpunkt {x:.12f}   "
              f"{'GESCHLOSSEN' if zu else f'Rest {x-1:+.4e}'}")
    komma = Fraction(3, 2) ** 12 / Fraction(2) ** 7
    print(f"     Rest der reinen Quinten = {komma} = "
          f"{cent(float(komma)):.2f} Cent (pythagoreisches Komma)")
    x = 1.0
    for _ in range(12):
        x *= q_temp
        while x >= 2:
            x /= 2
    assert abs(x - 1) < 1e-12, "temperiert muesste schliessen"

    print("""
   Richtig ist also:
     reine Naturtoene   -> irrationale Windung -> dichte, offene Bahn
     temperierte Toene  -> rationale Windung   -> geschlossene Bahn
   Der geschlossene Quintenzirkel ist ein Artefakt der Temperierung;
   rein gestimmt ist er eine Spirale.""")

    # ---------------------------------------------------- TEIL D
    print("\nTEIL D: Cent-Buchhaltung -- Theorie und Instrument getrennt")
    print("-" * 74)
    print("""   Die theoretische Abweichung eines Naturtons von der
   temperierten Skala und die instrumentenbedingte Verschiebung sind
   zwei verschiedene Groessen. Nur ihre Summe ist die
   Nettoabweichung; wer sie gleichsetzt, zaehlt eine davon nicht.""")
    faelle = [
        (4, 4 / 4, 1200 * 0, 0.0, "Oktave, stabil"),
        (7, 7 / 4, 1000.0, -12.5, "Trichter zieht abwaerts"),
        (11, 11 / 8, 600.0, +20.0, "Konus, Ansatz"),
    ]
    print(f"\n   {'n':>3} {'Verhaeltnis':>12} {'theor. Abw.':>12} "
          f"{'Instrument':>11} {'Netto':>9}  Bemerkung")
    for n, verh, ref, instr, bem in faelle:
        theo = cent(verh) - ref if ref else 0.0
        print(f"   {n:>3} {verh:12.5f} {theo:12.1f} {instr:11.1f} "
              f"{theo+instr:9.1f}  {bem}")
    t7 = cent(7 / 4) - 1000.0
    assert abs(t7 - (-31.17)) < 0.1, "7. Naturton: -31.2 Cent erwartet"
    t11 = cent(11 / 8) - 600.0
    assert abs(t11 - (-48.68)) < 0.1, "11. Naturton: -48.7 Cent erwartet"
    print(f"""
   Der 7. Naturton weicht theoretisch bereits {t7:.1f} Cent von der
   temperierten Septime ab; kommen {faelle[1][3]:.1f} Cent vom Trichter hinzu,
   ist die Nettoabweichung {t7+faelle[1][3]:.1f} Cent -- nicht {t7:.1f}.
   Ebenso beim 11.: theoretisch {t11:.1f} Cent gegen den Tritonus,
   mit {faelle[2][3]:+.1f} Cent Instrumenteneinfluss netto {t11+faelle[2][3]:.1f}.""")

    print("\n" + "=" * 74)
    print("ERGEBNIS Z11")
    print("=" * 74)
    print("""   [K] Die Naturtonreihe belegt die Generator-Struktur physikalisch:
   Primzahl-Ordnungen fuehren neue Qualitaeten ein, zusammengesetzte
   sind Kombinationen. Das ist dieselbe Struktur, die der
   Bikohaerenztest im Weil-Spektrum misst -- dort Kopplung nur bei
   Primzahlpotenzen, hier neue Klangqualitaet nur bei Primzahlen.

   [K] Der Amplitudenabfall ~1/n entspricht formal der Tenney-Hoehe.
   Physikalischer und zahlentheoretischer Grund fuehren auf dieselbe
   Gewichtung.

   [K] Fuer die Torus-Topologie zaehlt die Windungszahl, nicht das
   Frequenzverhaeltnis. Rein gestimmt ist die Windung irrational und
   die Bahn offen; temperiert ist sie rational (7/12) und die Bahn
   geschlossen. Die umgekehrte Zuordnung ist ein haeufiger Fehler.""")
    print("\nAlle Checks bestanden.")
