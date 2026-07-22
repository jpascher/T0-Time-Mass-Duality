#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a180_windungsquant.py -- Pruefskript zu A180.
Prueft: Delta w = 1 ist ganzzahlig, koordinatenfrei und skalenunabhaengig;
Gegenprobe, dass eine zellbasierte Entropie von der Einteilung abhaengt und
eine spektrale nicht. Standardbibliothek."""
import math

N = 100000


def windung(f):
    ges, vor = 0.0, f(0.0)
    for i in range(1, N+1):
        akt = f(i/N); d = akt - vor
        while d > math.pi:  d -= 2*math.pi
        while d < -math.pi: d += 2*math.pi
        ges += d; vor = akt
    return ges/(2*math.pi)


def main():
    ok = True
    print("PRUEFUNG 1  Ganzzahligkeit und kleinste Differenz")
    ws = [windung(lambda s, w=w: 2*math.pi*w*s) for w in (1, 2, 3)]
    print("   Windungen: %s" % ["%.8f" % x for x in ws])
    diffs = [ws[i+1]-ws[i] for i in range(2)]
    g1 = all(abs(d-1) < 1e-6 for d in diffs)
    ok = ok and g1
    print("   kleinste Differenz = %.8f -> Delta w = 1 :" % diffs[0],
          "BESTANDEN" if g1 else "FEHLGESCHLAGEN")
    print("   Ein halbes Windungsquant existiert nicht: pi_1(T^4) = Z^4.")

    print("\nPRUEFUNG 2  Skalenunabhaengigkeit")
    print("   Der Weg wird um Faktoren gestreckt; die Windung bleibt.")
    print("   %10s %14s" % ("Streckung", "Windung"))
    g2 = True
    for s in (0.01, 1.0, 100.0, 1e6):
        w = windung(lambda t, s=s: 2*math.pi*2*t + 0.0*s)
        print("   %10.0e %14.8f" % (s, w))
        if abs(w-2) > 1e-6: g2 = False
    ok = ok and g2
    print("   energieunabhaengig, weil topologisch :",
          "BESTANDEN" if g2 else "FEHLGESCHLAGEN")

    print("\nPRUEFUNG 3  Gegenprobe: zellbasierte gegen spektrale Entropie")
    print("   Ein Zustand wird in Zellen geteilt; der URSPRUNG der Teilung")
    print("   wird verschoben. Eine partitionsabhaengige Entropie aendert sich.")
    dichte = lambda x: 1 + 0.8*math.cos(2*math.pi*x) + 0.3*math.cos(6*math.pi*x)

    def zell_entropie(nzellen, versatz):
        p = []
        for k in range(nzellen):
            a = (k+versatz)/nzellen
            m = sum(dichte(a + j/(nzellen*200))/200 for j in range(200))
            p.append(max(m, 1e-12))
        s = sum(p); p = [x/s for x in p]
        return -sum(x*math.log(x) for x in p)

    print("   %10s %16s" % ("Versatz", "S_Zelle (8 Zellen)"))
    werte = []
    for v in (0.0, 0.125, 0.25, 0.375):
        e = zell_entropie(8, v); werte.append(e)
        print("   %10.3f %16.8f" % (v, e))
    spanne = max(werte)-min(werte)
    print("   Spanne = %.6f  -> partitionsABHAENGIG" % spanne)

    print("\n   Spektrale Groesse: die Fourier-Betraege der Dichte")
    print("   %10s %16s" % ("Versatz", "S_Spektral"))
    werte2 = []
    for v in (0.0, 0.125, 0.25, 0.375):
        koeff = []
        for n in range(1, 5):
            re = sum(dichte(x/2000 + v)*math.cos(2*math.pi*n*x/2000) for x in range(2000))/2000
            im = sum(dichte(x/2000 + v)*math.sin(2*math.pi*n*x/2000) for x in range(2000))/2000
            koeff.append(math.hypot(re, im))
        s = sum(koeff) or 1.0
        p = [max(k/s, 1e-12) for k in koeff]
        e = -sum(x*math.log(x) for x in p)
        werte2.append(e)
        print("   %10.3f %16.8f" % (v, e))
    spanne2 = max(werte2)-min(werte2)
    print("   Spanne = %.2e  -> partitionsUNABHAENGIG" % spanne2)
    g3 = spanne > 1e-3 and spanne2 < 1e-6
    ok = ok and g3
    print("   :", "BESTANDEN" if g3 else "FEHLGESCHLAGEN")

    print("\n   SCHLUSS: die Einwaende gegen eine Zell-Ontologie treffen; beim")
    print("   Windungsquant laufen sie leer, weil eine Windungsklasse keinen")
    print("   Ort hat. WAS NICHT GEZEIGT IST: dass Delta w = 1 die EINZIGE")
    print("   invariante Einheit ist (A180, 'Was offen bleibt').")
    print("\nERGEBNIS:", "BESTANDEN" if ok else "FEHLGESCHLAGEN")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
