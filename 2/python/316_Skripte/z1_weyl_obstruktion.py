#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""z1_weyl_obstruktion.py -- Die Obstruktion auf Satzebene.

Frage: Kann das Laplace-Spektrum irgendeiner kompakten Riemannschen
Mannigfaltigkeit die Riemann-Nullstellen sein?

Antwort: nein, und zwar aus der ABZAEHLUNG, nicht aus der Anschauung.

  Weyl-Gesetz (jede kompakte Mannigfaltigkeit, jede Dimension d,
  jede Kruemmung; Kruemmung/Rand/Orbifold-Punkte aendern nur
  niedrigere Ordnungen):
      N(lambda) ~ C_d * Vol * lambda^{d/2}          -- reine Potenz

  Riemann-von Mangoldt (bewiesen):
      N(T) = (T/2pi) ln(T/2pi) - T/2pi + 7/8 + O(1/T)

  T*ln(T) ist keine Potenz T^{d/2}. Der lokale Exponent
  d ln N / d ln T = 1 + 1/ln(T/2pi) ist nicht konstant.

Damit sind ALLE Ansaetze erledigt, die eine kompakte Mannigfaltigkeit
suchen -- einschliesslich Kruemmungsdeformationen von T^4/Z3.
Nur Standardbibliothek.
"""
import math

TWO_PI = 2.0 * math.pi


def N_riemann(T):
    """Riemann-von-Mangoldt-Zaehlfunktion der Nullstellen bis Hoehe T."""
    return T / TWO_PI * math.log(T / TWO_PI) - T / TWO_PI + 7.0 / 8.0


def lokaler_exponent(T, rel=1e-6):
    """d ln N / d ln T -- entspricht d/2 im Weyl-Gesetz."""
    h = T * rel
    return ((math.log(N_riemann(T + h)) - math.log(N_riemann(T - h)))
            / (math.log(T + h) - math.log(T - h)))


def weyl_N(lam, d, C=1.0):
    """Weyl-Leitterm einer kompakten d-Mannigfaltigkeit."""
    return C * lam ** (d / 2.0)


ZEROS_30 = [
    14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178,
    40.918719, 43.327073, 48.005151, 49.773832, 52.970321, 56.446248,
    59.347044, 60.831779, 65.112544, 67.079811, 69.546402, 72.067158,
    75.704691, 77.144840, 79.337375, 82.910381, 84.735493, 87.425275,
    88.809111, 92.491899, 94.651344, 95.870634, 98.831194, 101.317851,
]

if __name__ == "__main__":
    print("=" * 74)
    print("Z1 -- WEYL-OBSTRUKTION")
    print("=" * 74)

    # --- Check 1: Formel gegen echte Nullstellen -------------------
    print("\nCheck 1: Riemann-von Mangoldt gegen echte Nullstellenzahl")
    for T in (15.0, 25.0, 35.0, 50.0, 80.0, 102.0):
        echt = sum(1 for z in ZEROS_30 if z < T)
        print(f"   T={T:6.1f}   N_formel={N_riemann(T):8.3f}   echt={echt:3d}")
    assert abs(N_riemann(102.0) - 30) < 1.0, "Zaehlformel inkonsistent"

    # --- Check 2: lokaler Exponent ist nicht konstant --------------
    print("\nCheck 2: lokaler Exponent d/2 = dlnN/dlnT (Weyl verlangt konstant)")
    exponenten = []
    for T in (1e3, 1e4, 1e5, 1e6, 1e8, 1e12, 1e20):
        e = lokaler_exponent(T)
        exponenten.append(e)
        print(f"   T={T:8.0e}   d/2 = {e:.6f}   (d = {2*e:.4f})")
    spanne = max(exponenten) - min(exponenten)
    print(f"\n   Spanne ueber 17 Dekaden: {spanne:.4f}")
    assert spanne > 0.05, "Exponent waere doch konstant -- Widerspruch"
    print("   => nicht konstant. Keine feste Dimension d existiert.")

    # --- Check 3: bester Potenzfit scheitert -----------------------
    print("\nCheck 3: bester Potenzfit N ~ C*T^(d/2) im Fenster T in [1e3,1e6]")
    Ts = [10 ** e for e in (3.0, 4.0, 5.0, 6.0)]
    # Fit ueber Endpunkte
    d_half = ((math.log(N_riemann(Ts[-1])) - math.log(N_riemann(Ts[0])))
              / (math.log(Ts[-1]) - math.log(Ts[0])))
    C = N_riemann(Ts[0]) / Ts[0] ** d_half
    print(f"   gefittet: d/2 = {d_half:.4f}, C = {C:.4f}")
    print(f"   {'T':>10} {'N_Riemann':>13} {'Potenzfit':>13} {'rel. Fehler':>12}")
    maxfehler = 0.0
    for T in (1e3, 1e35 if False else 3e3, 1e4, 3e4, 1e5, 3e5, 1e6):
        nr, nf = N_riemann(T), C * T ** d_half
        fehler = abs(nf / nr - 1.0)
        maxfehler = max(maxfehler, fehler)
        print(f"   {T:10.1e} {nr:13.4e} {nf:13.4e} {fehler:12.2%}")
    print(f"\n   groesster relativer Fehler im Fenster: {maxfehler:.2%}")
    print("   => selbst der beste Potenzfit weicht systematisch ab.")

    # --- Check 4: Weyl-Vergleich fuer d = 1..6 ---------------------
    print("\nCheck 4: Weyl-Potenzen gegen Riemann-Wachstum (Verhaeltnis "
          "N(1e6)/N(1e3))")
    r_riemann = N_riemann(1e6) / N_riemann(1e3)
    print(f"   Riemann:            {r_riemann:12.2f}")
    for d in range(1, 7):
        r = weyl_N(1e6, d) / weyl_N(1e3, d)
        marke = "  <-- am naechsten" if abs(math.log(r / r_riemann)) < 0.5 else ""
        print(f"   Weyl d={d}:          {r:12.2f}{marke}")
    print("   => keine ganzzahlige Dimension trifft; das ln(T) fehlt allen.")

    print("\n" + "=" * 74)
    print("ERGEBNIS Z1  [X]")
    print("=" * 74)
    print("""Es gibt keine kompakte Riemannsche Mannigfaltigkeit -- gleich
welcher Dimension, Kruemmung, Topologie oder Orbifold-Struktur --,
deren Laplace-Spektrum die Riemann-Nullstellen sind.

Folge fuer FFGFT: der gesamte Zweig 'T^4/Z3 geeignet deformieren'
ist damit erledigt, nicht nur der flache Fall. Das zusaetzliche
ln(T) ist die Signatur eines SKALENFREIHEITSGRADES -- einer
Dilatationsrichtung mit logarithmisch wachsendem Volumen.
Das ist kein Laplace auf einer Mannigfaltigkeit; das ist die
ausgerollte Domaene (Dok. 315).""")
    print("\nAlle Checks bestanden.")
