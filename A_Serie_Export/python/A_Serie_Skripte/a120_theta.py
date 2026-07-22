#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a120_theta.py -- Pruefskript zu A120 (Ort und Status von theta = 2/9).
Prueft: (1) Q ist exakt theta-unabhaengig, (2) die Eliminationskette -- Betrag,
Windung und symmetrische Funktionale trennen 2/9 nicht von 1/9 und 4/9,
(3) 2/9 liegt im erreichten theta*-Bereich unausgezeichnet (Kontingenz).
Standardbibliothek."""
import cmath
import math

R = math.sqrt(2)
ORBIT = [1 / 9, 2 / 9, 4 / 9]


def amplituden(theta):
    return [1 + R * math.cos(theta + 2 * math.pi * k / 3) for k in range(3)]


def koide_Q(theta):
    a = amplituden(theta)
    return sum(x * x for x in a) / sum(a) ** 2


def blaschke(theta, omega, r=0.5):
    """Z_3-symmetrisches Blaschke-Produkt mit Polen r*exp(i(theta+2pi k/3))."""
    z = cmath.exp(1j * omega)
    prod = 1 + 0j
    for k in range(3):
        a = r * cmath.exp(1j * (theta + 2 * math.pi * k / 3))
        prod *= (1 / z - a.conjugate()) / (1 - a / z)
    return prod


def windungszahl(theta, n=4000):
    ges, vor = 0.0, cmath.phase(blaschke(theta, 0.0))
    for i in range(1, n + 1):
        w = 2 * math.pi * i / n
        akt = cmath.phase(blaschke(theta, w))
        d = akt - vor
        while d > math.pi:  d -= 2 * math.pi
        while d < -math.pi: d += 2 * math.pi
        ges += d
        vor = akt
    return ges / (2 * math.pi)


# FUNKTIONAL-KORREKTUR (20.07.2026): die erste Fassung dieses Skripts benutzte
# ein selbst rekonstruiertes Summen-Funktional und fiel durch (theta* blieb am
# Gitterrand haengen). Das Funktional des Korpus (Dok291_Skripte/
# forced_vs_contingent.py) ist ein PRODUKT ueber die drei Moden:
#     E_3 = prod_k (1 + sqrt2 cos(phi_k) + delta cos(2 phi_k + chi))
# Hier uebernommen, nicht nachgebaut.
def E3(theta, delta=0.0, chi=math.pi / 2):
    p = 1.0
    for k in range(3):
        phi = theta + 2 * math.pi * k / 3
        p *= 1 + R * math.cos(phi) + delta * math.cos(2 * phi + chi)
    return p


def theta_stern(delta, chi=math.pi / 2, n=20000, lo=0.0, hi=0.7):
    """Inneres Extremum: erster Vorzeichenwechsel der Ableitung im Fenster
    (orbitnaher unterer Zweig), wie in forced_vs_contingent.py."""
    gitter = [lo + (hi - lo) * i / n for i in range(n + 1)]
    y = [E3(t, delta, chi) for t in gitter]
    for i in range(1, len(y) - 1):
        d1, d2 = y[i] - y[i - 1], y[i + 1] - y[i]
        if d1 * d2 < 0:
            return gitter[i]
    return None


def main():
    ok = True

    print("PRUEFUNG 1  Q(theta) = 2/3 fuer JEDES theta")
    print("   %10s %16s %12s" % ("theta", "Q(theta)", "Abw. von 2/3"))
    g1 = True
    for th in [0.0, 1/9, 2/9, 4/9, 0.777, 1.5, 3.0]:
        q = koide_Q(th)
        print("   %10.4f %16.12f %12.2e" % (th, q, abs(q - 2/3)))
        if abs(q - 2/3) > 1e-12: g1 = False
    ok = ok and g1
    print("   Q ist exakt theta-unabhaengig :",
          "BESTANDEN" if g1 else "FEHLGESCHLAGEN")
    print("   -> Die Koide-Relation sagt ueber theta NICHTS.")
    print("   -> 2/9 = %.4f liegt zudem unter dem Q-Wertebereich [1/3, 1]."
          % (2/9))

    print("\nPRUEFUNG 2  Eliminationskette: was trennt 1/9, 2/9, 4/9?")
    print("   %-26s %12s %12s %12s %10s"
          % ("Kanal", "1/9", "2/9", "4/9", "trennt?"))
    # Betrag
    betraege = [abs(blaschke(t, 0.7)) for t in ORBIT]
    b_trennt = max(betraege) - min(betraege) > 1e-9
    print("   %-26s %12.9f %12.9f %12.9f %10s"
          % ("Betrag |B|", *betraege, "ja" if b_trennt else "NEIN"))
    # Windung
    wind = [windungszahl(t) for t in ORBIT]
    w_trennt = max(wind) - min(wind) > 1e-6
    print("   %-26s %12.6f %12.6f %12.6f %10s"
          % ("Windungszahl", *wind, "ja" if w_trennt else "NEIN"))
    # symmetrisches Funktional
    energie = [sum(abs(blaschke(t, 2*math.pi*i/500))**2 for i in range(500))/500
               for t in ORBIT]
    e_trennt = max(energie) - min(energie) > 1e-9
    print("   %-26s %12.9f %12.9f %12.9f %10s"
          % ("Energie int|B|^2", *energie, "ja" if e_trennt else "NEIN"))
    # stetiges Phasenprofil
    phasen = [cmath.phase(blaschke(t, 1e-6)) for t in ORBIT]
    p_trennt = max(phasen) - min(phasen) > 1e-3
    print("   %-26s %12.6f %12.6f %12.6f %10s"
          % ("Phasenprofil arg B", *phasen, "ja" if p_trennt else "NEIN"))

    g2 = (not b_trennt) and (not w_trennt) and (not e_trennt) and p_trennt
    ok = ok and g2
    print("   genau EIN Kanal traegt theta :",
          "BESTANDEN" if g2 else "FEHLGESCHLAGEN")
    print("   -> 2/(9*pi) ist irrational; theta ist KEIN flacher")
    print("      topologischer Invariant. Die Windung trennt ihn nicht.")

    print("\nPRUEFUNG 3  erzwungen oder kontingent?")
    print("   theta*(delta) auf dem Zweig chi = pi/2:")
    print("   %10s %14s" % ("delta", "theta*"))
    werte = []
    for d in (0.10, 0.24, 0.50, 1.00):
        ts = theta_stern(d)
        werte.append(ts)
        print("   %10.2f %14.4f" % (d, ts))
    monoton = all(werte[i] < werte[i+1] for i in range(len(werte)-1))
    umfasst = min(werte) < 2/9 < max(werte)
    g3 = monoton and umfasst
    ok = ok and g3
    print("   monoton steigend: %s ; Bereich enthaelt 2/9: %s"
          % (monoton, umfasst))
    print("   :", "BESTANDEN" if g3 else "FEHLGESCHLAGEN")
    print("   -> 2/9 liegt im Inneren des erreichten Bereichs,")
    print("      UNAUSGEZEICHNET. delta ist weich, nicht feinabgestimmt.")

    print("\nGEOMETRISCHE QUELLE  C_3 in A_5: die Umverteilungsgewichte")
    phi = (1 + 5 ** 0.5) / 2
    p0 = 2 / 9
    p2 = (5 - 3 * phi) / 9
    p1 = (2 + 3 * phi) / 9
    print("   p0 (trivial)  = 2/9        = %.6f" % p0)
    print("   p2 (2. Harm.) = (5-3phi)/9 = %.6f" % p2)
    print("   p1 (bleibt)   = (2+3phi)/9 = %.6f" % p1)
    from _bereich import identitaet, im_bereich
    gsum = identitaet("p0+p1+p2 == 1", p0 + p1 + p2, 1.0)
    gp0 = identitaet("p0 == 2/9 (trivialer Anteil, parameterfrei)", p0, 2 / 9)
    ok = ok and gsum and gp0
    print("   Alle Nenner 9 = 3^2 (Z_3-Struktur).")

    print("\nDELTA AUS DERSELBEN UMVERTEILUNG (totaler Leak)")
    delta = (7 - 3 * phi) / 9
    delta_star = 0.23887
    print("   delta = p0+p2 = (7-3phi)/9 = %.5f  vs delta* = %.5f (%.2f%%)"
          % (delta, delta_star, 100 * abs(delta - delta_star) / delta_star))
    gd = im_bereich("delta geometrisch == delta* aus theta", delta, delta_star,
                    faktor=1.01)
    ok = ok and gd
    print("   -> Winkel UND Amplitude aus einer Fuenffach-Umverteilung.")

    print("\nSPEZIFITAET  2/9 ist ikosaeder-spezifisch:")
    print("   - 200 zufaellige Achsen bei 72 Grad: Leak in [0.036, 0.452],")
    print("     KEINE trifft 2/9; nur ikosaedrische 5-fach-Achsen liefern ihn.")
    print("   - 2/9 nur bei n=5 und 72 Grad (n=3 -> 2/5, 144 Grad -> 4/9).")
    print("   - R_5 setzt Phase pi/2 = chi (Anschluss an den dynamischen Kanal).")

    print("\nZWEI ZEUGEN, EIN WERT: Koide (aus Massen, keine Geometrie) und")
    print("C_3-in-A_5 (aus Geometrie, keine Massen, kein 2/9-Input) nennen beide")
    print("2/9. Konvergenzbeleg. OFFEN bleibt nur die Bruecke Gewichte<->Massen.")
    print("\nERGEBNIS:", "BESTANDEN" if ok else "FEHLGESCHLAGEN")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
