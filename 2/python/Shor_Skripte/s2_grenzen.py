#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""s2_grenzen.py -- Welche Grenze trifft welche Aufgabe?

Bei grossen Zahlen versagen sowohl die klassische Resonanzsuche als auch
Shors Quantenverfahren. Die Gruende sind aber VERSCHIEDEN, und die
Unterscheidung ist wesentlich -- sonst wird die Weyl-Obstruktion
ueberdehnt.

  AUFGABE A  Eine Periode r EINER konkreten Zahl N finden (Shors Aufgabe)
             -> Ressourcengrenze: Gatterzahl, Fehlerkorrektur
  AUFGABE B  Ein UNENDLICHES arithmetisches Spektrum abbilden
             -> strukturelle Grenze: Weyl-Obstruktion

  TEST A  Weyl-Obstruktion: aequidistantes Register gegen T ln T
  TEST B  Warum sie Shor NICHT trifft
  TEST C  Was Shor tatsaechlich limitiert
  TEST D  Windungszahl: wann schliesst eine Resonanz?

Nur Standardbibliothek.
"""
import math

TWO_PI = 2.0 * math.pi


def N_riemann(T):
    """Riemann-von Mangoldt: arithmetische Zaehldichte."""
    return T / TWO_PI * math.log(T / TWO_PI) - T / TWO_PI + 7.0 / 8.0


def N_register(T):
    """Zaehlfunktion eines aequidistanten Registers: N(T) = T."""
    return T


if __name__ == "__main__":
    print("=" * 74)
    print("S2 -- WELCHE GRENZE TRIFFT WELCHE AUFGABE?")
    print("=" * 74)

    # ---------------------------------------------------- TEST A
    print("\nTEST A: Die Weyl-Obstruktion")
    print("-" * 74)
    print("""   Ein n-Qubit-Register hat 2^n Basiszustaende -- einen kompakten,
   endlichen Zustandsraum mit AEQUIDISTANTEN Niveaus. Seine
   Zaehlfunktion ist N(T) = T. Arithmetische Zaehldichten wachsen
   dagegen wie T ln T.""")
    print(f"\n   {'T':>10} {'Register N(T)=T':>17} {'arithmetisch':>15} "
          f"{'Faktor':>9}")
    for T in (1e3, 1e6, 1e12, 1e30, 1e100):
        na = N_riemann(T)
        print(f"   {T:>10.0e} {T:>17.3e} {na:>15.3e} {na/T:>9.2f}")
    f1, f2 = N_riemann(1e3) / 1e3, N_riemann(1e100) / 1e100
    print(f"\n   Der Faktor waechst wie ln(T)/(2pi) -- unbeschraenkt")
    print(f"   (von {f1:.2f} bei T=10^3 auf {f2:.2f} bei T=10^100).")
    assert f2 > 5 * f1, "Der Faktor sollte deutlich wachsen"
    print("""   => ein Register mit aequidistanten Zustaenden braucht ln(T)-mal
      mehr Zustaende als es hat. Ein kompakter Raum kann die
      arithmetische Dichte nicht vollstaendig tragen.""")

    # ---------------------------------------------------- TEST B
    print("\nTEST B: Warum das Shor NICHT trifft")
    print("-" * 74)
    print("""   Shor sucht EINE Periode r einer KONKRETEN Zahl N -- kein
   unendliches Spektrum. Dafuer genuegt ein endliches Register:""")
    print(f"\n   {'N (Bit)':>9} {'benoetigte Qubits':>19} {'aufloesbare Perioden':>22}")
    for n in (16, 64, 256, 1024, 2048):
        q = 2 * n + 3
        print(f"   {n:>9} {q:>19} {'2^' + str(2*n):>22}")
    print("""
   => die Aufgabe ist endlich und das Register reicht aus. Die
      Weyl-Obstruktion greift hier NICHT -- sie betrifft die
      vollstaendige Abbildung unendlicher Spektren, nicht das
      Auffinden einer einzelnen Periode.

      Diese Unterscheidung ist wesentlich: Wer die Weyl-Grenze
      gegen Shor anfuehrt, ueberdehnt sie.""")

    # ---------------------------------------------------- TEST C
    print("\nTEST C: Was Shor bei grossen N tatsaechlich limitiert")
    print("-" * 74)
    print(f"   {'N (Bit)':>9} {'log. Qubits':>13} {'Gatter ~ n^3':>15} "
          f"{'phys. Qubits (FTQC)':>21}")
    for n in (128, 512, 1024, 2048, 4096):
        q_log = 2 * n + 3
        gatter = n ** 3
        q_phys = q_log * 1000        # grobe Fehlerkorrektur-Abschaetzung
        print(f"   {n:>9} {q_log:>13} {gatter:>15.2e} {q_phys:>21.2e}")
    print("""
   => die Grenze ist die GATTERZAHL der modularen Exponentiation
      (waechst wie n^3) und der Fehlerkorrektur-Overhead (rund 1000
      physikalische je logischem Qubit). Das ist eine
      RESSOURCENGRENZE -- prinzipiell durch bessere Hardware
      ueberwindbar, anders als eine strukturelle Grenze.""")

    print("\n   Zum Vergleich die klassische Resonanzsuche:")
    print(f"   {'N':>12} {'mittlere Ordnung ~ N':>22} {'Praezision ~ 1/N^2':>20}")
    for N in (1e6, 1e12, 1e24, 1e60):
        print(f"   {N:>12.0e} {N:>22.0e} {1/N**2:>20.2e}")
    print("""
   => hier ist die Grenze doppelt: O(N) Schritte UND eine
      Frequenzaufloesung von 1/N^2, die bei RSA-Groessen unterhalb
      jeder Zahlendarstellung liegt.""")

    # ---------------------------------------------------- TEST D
    print("\nTEST D: Windungszahl -- wann schliesst eine Resonanz?")
    print("-" * 74)
    print("""   Fuer geschlossene Trajektorien entscheidet die Windungszahl
   W = log2(r), nicht das Frequenzverhaeltnis r.""")
    faelle = [("reine Quinte 3/2", 1.5), ("temperierte Quinte", 2 ** (7 / 12)),
              ("Oktave 2/1", 2.0), ("reine Terz 5/4", 1.25)]
    print(f"\n   {'Fall':>22} {'Verhaeltnis r':>14} {'W = log2(r)':>13} {'Art':>12}")
    for name, r in faelle:
        W = math.log2(r)
        # rational, wenn W eine kleine Bruchdarstellung exakt trifft
        from fractions import Fraction
        f = Fraction(W).limit_denominator(1000)
        ist_rat = abs(float(f) - W) < 1e-15
        print(f"   {name:>22} {r:>14.9f} {W:>13.9f} "
              f"{'rational' if ist_rat else 'irrational':>12}")

    print("\n   Probe: 12 Quinten aufwaerts, Oktaven herausgerechnet")
    for name, q in (("rein 3/2", 1.5), ("temperiert", 2 ** (7 / 12))):
        x = 1.0
        for _ in range(12):
            x *= q
            while x >= 2:
                x /= 2
        zu = abs(x - 1) < 1e-12
        print(f"     {name:12s}: Endpunkt {x:.12f}  "
              f"{'GESCHLOSSEN' if zu else f'Rest {x-1:+.4e}'}")
    x = 1.0
    for _ in range(12):
        x *= 2 ** (7 / 12)
        while x >= 2:
            x /= 2
    assert abs(x - 1) < 1e-12, "temperiert muesste schliessen"
    print("""
   => reine Verhaeltnisse haben irrationale Windung und schliessen
      nicht; der Rest ist das pythagoreische Komma. Temperierte
      Verhaeltnisse haben rationale Windung (7/12) und schliessen
      exakt. Schliessung ist ein Artefakt der Rationalisierung.""")

    print("\n" + "=" * 74)
    print("ERGEBNIS S2")
    print("=" * 74)
    print("""   Zwei Grenzen, verschiedener Natur:

   [K] STRUKTURELL (Weyl): Ein kompakter Zustandsraum kann ein
       unendliches arithmetisches Spektrum der Dichte T ln T nicht
       vollstaendig tragen. Diese Grenze ist prinzipiell und
       gilt fuer jede Hardware.

   [K] RESSOURCE (Shor): Die Faktorisierung einer konkreten Zahl
       ist eine endliche Aufgabe. Sie scheitert bei grossen N an
       Gatterzahl (n^3) und Fehlerkorrektur-Overhead -- nicht an
       der Weyl-Obstruktion.

   [K] Die klassische Resonanzsuche scheitert doppelt: O(N) Schritte
       und Praezisionsbedarf 1/N^2.

   Beide Ansaetze versagen bei kryptographisch relevanten Groessen,
   aber aus verschiedenen Gruenden. Die Weyl-Obstruktion gegen Shor
   anzufuehren waere eine Ueberdehnung.""")
    print("\nAlle Checks bestanden.")
