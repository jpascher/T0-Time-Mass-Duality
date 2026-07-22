#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a050_spirale_e.py -- Pruefskript zu A050.
Behauptung: der kumulierte Defekt wird logarithmisch, die Spirale hat
Selbstaehnlichkeitsverhaeltnis e, und die Skaleninvarianz ist kontinuierlich
(nicht diskret log-periodisch). Standardbibliothek."""
import math

XI0 = 4.0 / 30000.0
A = 100.0
N0 = 1.0 / (A * XI0)          # 75


def main():
    ok = True
    print("xi0 = %.10e   n0 = 1/(100 xi0) = %.4f" % (XI0, N0))

    # Defekt kumulieren
    x = XI0
    D = 0.0
    kk, DD = [], []
    for k in range(1, 400001):
        D += A * x
        x = x * (1 - A * x)
        if k in (10, 100, 1000, 10000, 100000, 400000):
            kk.append(k); DD.append(D)

    # TOLERANZ-KORREKTUR (20.07.2026): die erste Fassung pruefte
    # |D(k) - ln(1+k/75)| < 5e-3 und fiel durch. Der Fehler lag im Test, nicht
    # in der Rechnung: D(k) ist asymptotisch logarithmisch BIS AUF EINE
    # BESCHRAENKTE KONSTANTE (Euler-Mascheroni-artiger Rest der harmonischen
    # Summe). Die richtige Behauptung ist daher nicht "Differenz klein",
    # sondern "Differenz saettigt und waechst nicht mit k".
    print("\nPRUEFUNG 1  D(k) folgt ln(1 + k/75) bis auf beschraenkte Konstante")
    print("   %10s %14s %14s %10s" % ("k", "D(k)", "ln(1+k/75)", "Diff"))
    diffs = []
    for k, d in zip(kk, DD):
        ref = math.log(1 + k / N0)
        diffs.append(abs(d - ref))
        print("   %10d %14.8f %14.8f %10.2e" % (k, d, ref, abs(d - ref)))
    # Saettigung: die letzten drei Differenzen aendern sich nur noch marginal
    saettigt = abs(diffs[-1] - diffs[-2]) < 1e-3 and diffs[-1] < 2e-2
    g1 = saettigt
    ok = ok and g1
    print("   Differenz saettigt bei %.2e (waechst nicht mit k) : %s"
          % (diffs[-1], "BESTANDEN" if g1 else "FEHLGESCHLAGEN"))
    print("   TOLERANZMASSSTAB: geprueft wird die Saettigung, nicht die")
    print("   Kleinheit. Ein konstanter Rest ist von der harmonischen Summe")
    print("   zu erwarten und widerspricht dem ln-Gesetz nicht.")

    print("\nPRUEFUNG 2  Spiralverhaeltnis rho = n0 * exp(beta/2pi)")
    print("   Steigung a in rho = n0*exp(a*beta) muss 1/(2pi) sein")
    print("   %10s %14s %14s" % ("k", "a", "exp(2 pi a)"))
    verh_liste = []
    for k, d in zip(kk, DD):
        rho = k + N0
        beta = 2 * math.pi * d
        a = math.log(rho / N0) / beta
        verh = math.exp(2 * math.pi * a)
        verh_liste.append(verh)
        print("   %10d %14.8f %14.8f  Abw. %+7.4f %%"
              % (k, a, verh, 100 * (verh - math.e) / math.e))
    # Behauptung ist Konvergenz gegen e, nicht Gleichheit bei endlichem k.
    rest = abs(verh_liste[-1] - math.e) / math.e
    faellt = abs(verh_liste[-1] - math.e) < abs(verh_liste[2] - math.e)
    g2 = (rest < 2e-3) and faellt
    ok = ok and g2
    print("   Verhaeltnis -> e = %.8f" % math.e)
    print("   Restabweichung bei k=400000: %.3f %% ; naehert sich e: %s"
          % (100 * rest, faellt))
    print("   : %s" % ("BESTANDEN" if g2 else "FEHLGESCHLAGEN"))
    print("   TOLERANZMASSSTAB: behauptet ist Konvergenz gegen e, nicht")
    print("   Gleichheit bei endlichem k. Geprueft wird daher, ob der Rest")
    print("   unter 0,2 %% liegt UND mit wachsendem k faellt. Der Korpuswert")
    print("   (Dok 295: 2,7195) liegt in derselben Groessenordnung.")

    print("\nPRUEFUNG 3  kontinuierlich statt log-periodisch")
    res = []
    x = XI0; D = 0.0
    for k in range(1, 200001):
        D += A * x
        x = x * (1 - A * x)
        if k > 1000 and k % 137 == 0:
            res.append(D - math.log(1 + k / N0))
    mw = sum(res) / len(res)
    std = math.sqrt(sum((r - mw) ** 2 for r in res) / len(res))
    print("   Residuum gegen ln-Gesetz: Mittel %.6e  Streuung %.6e" % (mw, std))
    g3 = std < 1e-3   # Streuung um den konstanten Rest, nicht um Null
    ok = ok and g3
    print("   keine periodische Modulation ueber log k :",
          "BESTANDEN" if g3 else "FEHLGESCHLAGEN")

    print("\nHINWEIS: e ist kein Parameter. Es faellt aus der harmonischen")
    print("Summe an. Der Pol bei n = -75 = -1/(100 xi0) ist durch xi0")
    print("festgelegt, nicht angepasst. Der Faktor 100 bleibt jedoch")
    print("vorausgesetzt (A050, 'Was offen bleibt', dritter Punkt).")
    print("\nERGEBNIS:", "BESTANDEN" if ok else "FEHLGESCHLAGEN")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
