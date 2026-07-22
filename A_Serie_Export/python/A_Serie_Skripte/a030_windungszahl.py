#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a030_windungszahl.py -- Pruefskript zu A030.
Behauptung: Windungszahlen sind ganzzahlig, koordinatenfrei und stabil unter
stetiger Verformung; auf einfach zusammenhaengenden Flaechen existieren sie nicht.
Standardbibliothek."""
import math

N = 200000


def windung(theta_von_s, m=1.0):
    """Windungszahl = Gesamtphasenzuwachs / 2pi, numerisch integriert."""
    ges = 0.0
    vor = theta_von_s(0.0)
    for i in range(1, N + 1):
        s = i / N
        akt = theta_von_s(s)
        d = akt - vor
        while d > math.pi:  d -= 2 * math.pi
        while d < -math.pi: d += 2 * math.pi
        ges += d
        vor = akt
    return ges / (2 * math.pi)


def main():
    ok = True
    print("PRUEFUNG 1  Ganzzahligkeit auf T^2")
    for w1, w2 in [(1, 0), (3, -2), (5, 7)]:
        a = windung(lambda s, w=w1: 2 * math.pi * w * s)
        b = windung(lambda s, w=w2: 2 * math.pi * w * s)
        gut = abs(a - w1) < 1e-6 and abs(b - w2) < 1e-6
        ok = ok and gut
        print("   Soll (%2d,%2d)  Ist (%8.5f,%8.5f)  %s"
              % (w1, w2, a, b, "ok" if gut else "FEHLER"))

    print("\nPRUEFUNG 2  Koordinatenfreiheit (Umparametrisierung s -> s^3)")
    g = windung(lambda s: 2 * math.pi * 3 * s)
    h = windung(lambda s: 2 * math.pi * 3 * (s ** 3))
    gut = abs(g - h) < 1e-6
    ok = ok and gut
    print("   linear %.6f   kubisch %.6f   Differenz %.2e   %s"
          % (g, h, abs(g - h), "ok" if gut else "FEHLER"))

    print("\nPRUEFUNG 3  Stabilitaet unter stetiger Verformung")
    print("   Weg wird mit einer glatten Stoerung amplitude*sin(2pi s) verbeult")
    for amp in [0.0, 0.5, 1.5, 3.0]:
        v = windung(lambda s, a=amp: 2 * math.pi * 2 * s + a * math.sin(2 * math.pi * s))
        gut = abs(v - 2) < 1e-6
        ok = ok and gut
        print("   Amplitude %.1f  Windung %.6f  %s" % (amp, v, "ok" if gut else "FEHLER"))

    print("\nPRUEFUNG 4  einfach zusammenhaengender Fall")
    print("   Auf S^n (n>=2) ist pi_1 = 0: jeder geschlossene Weg ist")
    print("   zusammenziehbar, die Windungszahl ist identisch 0 und traegt")
    print("   keine Information. Das ist eine topologische Tatsache, kein")
    print("   numerisches Ergebnis -- sie wird hier nicht simuliert, sondern")
    print("   als Grund der Torus-Wahl benannt (A030).")

    print("\nERGEBNIS:", "BESTANDEN" if ok else "FEHLGESCHLAGEN")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
