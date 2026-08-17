#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""z6_tonnetz_weil.py -- xi als Tonnetz-Punkt und das Weil-Laengenspektrum.

Der Zugang dieses Skripts fragt nicht nach xi als kleinem Parameter,
sondern nach seiner HARMONISCHEN STRUKTUR:

    xi = 4/30000 = 1/7500 = 1/(2^2 * 3 * 5^4)

xi ist damit ein Punkt im Eulerschen Tonnetz mit den Koordinaten
(a2, a3, a5) = (-2, -1, -4) -- dieselbe Gitterstruktur wie im
Kontrollfall der Musikspirale, Primzahlen 2, 3, 5 als Achsen.

Die zustaendige Anschlussstelle ist dann nicht der Laplace-Operator,
sondern die Weilsche explizite Formel:

    sum_rho h(gamma) = (archimedischer Term)
                       - 2 sum_{p,k} (ln p)/p^{k/2} * hhat(k ln p)

Das duale Laengenspektrum der Nullstellen ist L = { k ln p }, also
Vielfache von Logarithmen EINZELNER Primzahlen. Ob xi dort auftaucht,
ist direkt pruefbar: die Fouriertransformierte der Nullstellendichte
muss bei den Laengen Peaks zeigen.

Ergebnis: die Methode funktioniert (Primzahl-Peaks erscheinen), aber
ln(1/xi) ist keine Laenge -- und der Grund ist strukturell, nicht
numerisch: 7500 ist zusammengesetzt.
Nur Standardbibliothek. Seed 20780458.
"""
import math
import random

SEED = 20780458
XI = 4.0 / 30000.0

# Erste 100 Riemann-Nullstellen (Imaginaerteile, Literatur)
ZEROS = [
    14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178,
    40.918719, 43.327073, 48.005151, 49.773832, 52.970321, 56.446248,
    59.347044, 60.831779, 65.112544, 67.079811, 69.546402, 72.067158,
    75.704691, 77.144840, 79.337375, 82.910381, 84.735493, 87.425275,
    88.809111, 92.491899, 94.651344, 95.870634, 98.831194, 101.317851,
    103.725538, 105.446623, 107.168611, 111.029536, 111.874659, 114.320221,
    116.226680, 118.790783, 121.370125, 122.946829, 124.256819, 127.516684,
    129.578704, 131.087688, 133.497737, 134.756510, 138.116042, 139.736209,
    141.123707, 143.111846, 146.000982, 147.422765, 150.053520, 150.925257,
    153.024694, 156.112909, 157.597592, 158.849988, 161.188964, 163.030710,
    165.537069, 167.184440, 169.094515, 169.911976, 173.411537, 174.754191,
    176.441434, 178.377407, 179.916484, 182.207078, 184.874468, 185.598784,
    187.228922, 189.416159, 192.026656, 193.079726, 195.265397, 196.876482,
    198.015309, 201.264752, 202.493594, 204.189672, 205.394697, 207.906259,
    209.576509, 211.690862, 213.347920, 214.547045, 216.169539, 219.067596,
    220.714918, 221.430705, 224.007000, 224.983325, 227.421444, 229.337413,
    231.250189, 231.987235, 233.693404, 236.524230,
]


def F(u, zeros=ZEROS):
    """Betrag der Fouriersumme der Nullstellen bei Laenge u, normiert."""
    re = sum(math.cos(g * u) for g in zeros)
    im = sum(math.sin(g * u) for g in zeros)
    return math.hypot(re, im) / len(zeros)


def weil_laengen(primes=(2, 3, 5, 7, 11, 13, 17, 19), kmax=6):
    """Das duale Laengenspektrum { k ln p } der Weil-Formel."""
    out = []
    for p in primes:
        for k in range(1, kmax + 1):
            out.append((k * math.log(p), p, k))
    return sorted(out)


if __name__ == "__main__":
    print("=" * 74)
    print("Z6 -- XI ALS TONNETZ-PUNKT UND DAS WEIL-LAENGENSPEKTRUM")
    print("=" * 74)

    # --- Check 1: xi im Tonnetz ------------------------------------
    print("\nCheck 1: die Tonnetz-Koordinaten von xi")
    n = round(1 / XI)
    print(f"   1/xi = {n}")
    rest, exps = n, {}
    for p in (2, 3, 5):
        while rest % p == 0:
            rest //= p
            exps[p] = exps.get(p, 0) + 1
    print(f"   Primfaktorzerlegung: {n} = " +
          " * ".join(f"{p}^{e}" for p, e in sorted(exps.items())))
    assert rest == 1, "1/xi enthaelt Primfaktoren jenseits von 5"
    print(f"   => xi liegt im 5-Limit-Tonnetz, Koordinaten "
          f"(a2,a3,a5) = ({-exps[2]}, {-exps[3]}, {-exps[5]})")
    L_xi = -math.log(XI)
    summe = sum(e * math.log(p) for p, e in exps.items())
    print(f"   ln(1/xi) = {L_xi:.6f}")
    print(f"   2ln2 + ln3 + 4ln5 = {summe:.6f}")
    assert abs(L_xi - summe) < 1e-12, "Log-Zerlegung inkonsistent"

    # --- Check 2: das Laengenspektrum ------------------------------
    print("\nCheck 2: das duale Laengenspektrum der Weil-Formel")
    L = weil_laengen()
    print("   erste Laengen k*ln(p):")
    for u, p, k in L[:10]:
        print(f"     {u:8.5f} = {k}*ln{p}")

    # --- Check 3: Fourier-Peaks bei Primlogarithmen ----------------
    print("\nCheck 3: Fourier-Nachweis der Laengen (100 Nullstellen)")
    rng = random.Random(SEED)
    bg = sorted(F(rng.uniform(0.4, 4.0)) for _ in range(3000))
    median, p95, p99 = bg[len(bg) // 2], bg[int(0.95 * len(bg))], bg[int(0.99 * len(bg))]
    print(f"   Hintergrund (3000 zufaellige u in [0.4,4]):")
    print(f"     Median {median:.4f}, 95%-Schwelle {p95:.4f}, "
          f"99%-Schwelle {p99:.4f}")
    print(f"\n   {'u':>9} {'F(u)':>8}  Zuordnung")
    treffer = 0
    for u, p, k in L:
        if u > 2.7:
            continue
        f = F(u)
        marke = ""
        if f > p99:
            marke, treffer = "  <== Peak (99%)", treffer + 1
        elif f > p95:
            marke, treffer = "  <== Peak (95%)", treffer + 1
        print(f"   {u:9.5f} {f:8.4f}  {k}*ln{p}{marke}")
    print(f"\n   Peaks ueber der 95%-Schwelle: {treffer}")
    assert treffer >= 4, "Die Methode sollte Primzahl-Peaks zeigen"
    print("   => die Methode funktioniert: die Primzahlen sind sichtbar.")

    # --- Check 4: Gueltigkeitsbereich der Messung ------------------
    print("\nCheck 4: Artefaktkontrolle -- kleine u sind nicht auswertbar")
    print("""   Fuer u -> 0 laufen alle Phasen gamma_n*u zusammen, F(u) -> 1
   unabhaengig von jeder Struktur. Die Messung ist erst auswertbar,
   wenn u die Phasen ueber den vollen Kreis streut, also
   u >> 2pi/(gamma_max - gamma_min).""")
    u_min = 2 * math.pi / (max(ZEROS) - min(ZEROS))
    print(f"   Aufloesungsgrenze u_min = 2pi/(gamma_max-gamma_min) = {u_min:.5f}")
    print(f"   {'u':>9} {'F(u)':>8}  Bemerkung")
    for u in (0.005, 0.0134, 0.05, 0.28, 1.0):
        f = F(u)
        bem = "unterhalb der Aufloesung -- Artefakt" if u < u_min else "auswertbar"
        print(f"   {u:9.5f} {f:8.4f}  {bem}")
    assert F(0.005) > 0.9, "Artefakt bei kleinem u sollte auftreten"
    print("   => Kandidaten mit u < u_min sind auszuschliessen. Insbesondere")
    print(f"      ln(75/74) = {-math.log(74.0/75.0):.5f} liegt darunter und")
    print("      ist mit 100 Nullstellen nicht messbar (keine Aussage).")

    # --- Check 5: die xi-Groessen im gueltigen Bereich -------------
    print("\nCheck 5: xi-abgeleitete Laengen im auswertbaren Bereich")
    kandidaten = [
        (L_xi, "ln(1/xi) = 2ln2+ln3+4ln5"),
        (L_xi / 2, "ln(1/xi)/2"),
        (math.log(75.0), "ln75 = ln3+2ln5"),
        (math.log(7500.0) / 4, "ln(7500)/4"),
        (2 * math.pi / L_xi, "2pi/ln(1/xi)"),
    ]
    print(f"   {'u':>9} {'F(u)':>8}  Groesse")
    ueber = 0
    for u, name in kandidaten:
        assert u > u_min, f"{name} liegt unter der Aufloesungsgrenze"
        f = F(u)
        marke = "  <== Peak" if f > p95 else ""
        if f > p95:
            ueber += 1
        print(f"   {u:9.5f} {f:8.4f}  {name}{marke}")
    assert ueber == 0, "Unerwartet: eine xi-Groesse ueber der Schwelle"
    print("   => keine einzige xi-Groesse erreicht die Schwelle.")

    # --- Check 6: der strukturelle Grund ---------------------------
    print("\nCheck 6: der Grund -- Kombination gegen Faktorisierung")
    print("""   Das Euler-Produkt zeta(s) = prod_p 1/(1-p^{-s}) logarithmiert zu
   einer SUMME ueber Primzahlpotenzen: jede Primzahl steht fuer sich,
   ohne Mischterme. Das Laengenspektrum enthaelt daher nur k*ln(p) --
   Logarithmen EINZELNER Primzahlen.

   Das Tonnetz lebt vom Gegenteil: ein Intervall ist 2^a 3^b 5^c mit
   mehreren nichtnullen Exponenten; gerade die Mischung erzeugt die
   Kommas. xi ist ein solcher Mischpunkt (a2,a3,a5) = (-2,-1,-4).""")
    print(f"\n   ln(1/xi) als Summe von Laengen:")
    print(f"     2*ln2 = {2*math.log(2):.5f}   (Laenge im Spektrum)")
    print(f"     1*ln3 = {math.log(3):.5f}   (Laenge im Spektrum)")
    print(f"     4*ln5 = {4*math.log(5):.5f}   (Laenge im Spektrum)")
    print(f"     Summe = {L_xi:.5f}   (KEINE Laenge im Spektrum)")
    naechste = min(weil_laengen(kmax=12), key=lambda t: abs(t[0] - L_xi))
    print(f"   naechste echte Laenge: {naechste[0]:.5f} = "
          f"{naechste[2]}*ln{naechste[1]}, Abstand {abs(naechste[0]-L_xi):.5f}")

    print("\n" + "=" * 74)
    print("ERGEBNIS Z6  [X]")
    print("=" * 74)
    print("""Tonnetz und Euler-Produkt teilen die Primzahlachsen, nutzen sie
aber entgegengesetzt: das Tonnetz kombiniert, das Euler-Produkt
faktorisiert. xi ist ein Kombinationspunkt -- musikalisch bedeutsam,
arithmetisch unsichtbar.

Der Ausschluss ist damit strukturell und nicht groessenordnungsbedingt:
er gilt unveraendert, wenn xi von Ordnung 1 waere. Was zaehlt, ist
nicht der Wert von xi, sondern dass 1/xi zusammengesetzt ist.""")
    print("\nAlle Checks bestanden.")
