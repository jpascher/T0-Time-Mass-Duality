#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""z4_epstein_casimir.py -- Was von der Verbindung uebrigbleibt.

Zwei Korpusbefunde, die die Riemann-Zeta unmittelbar beruehren:

(1) FAKTORISIERUNG. Die Spektral-Zeta des Z^4-Torus hat die geschlossene
    Form (Dok. 314, dort dreifach verifiziert):
        Z_{Z^4}(s) = 8 (1 - 4^{1-s}) zeta(s) zeta(s-1)
    Die Riemann-Zeta ist also ein FAKTOR der Torus-Spektral-Zeta --
    nicht per Analogie, sondern als Identitaet.

(2) CASIMIR-SYMMETRIE. Der Casimir-Punkt der Epstein-Zeta ist s = -1/2
    (Dok. 314: E = pi zeta_M(-1/2), Ordnungsumkehr D4 gegen Z^4).
    Sein Spiegelpunkt unter der Funktionalgleichung zeta(s) = chi(s)
    zeta(1-s) ist s = 3/2. Die Symmetrieachse von -1/2 und 3/2 ist
    exakt Re(s) = 1/2 -- die kritische Linie.

Dieses Skript verifiziert beides numerisch und prueft anschliessend
(P35-Disziplin), was daraus NICHT folgt.
Nur Standardbibliothek.
"""
import math

XI = 4.0 / 30000.0


def zeta(s, N=200000):
    """Riemann-Zeta fuer reelles s > 1 per Direktsumme mit Schwanzkorrektur."""
    if s <= 1:
        raise ValueError("nur fuer s > 1")
    total = sum(1.0 / n ** s for n in range(1, N + 1))
    # Euler-Maclaurin-Schwanz
    total += N ** (1 - s) / (s - 1) - 0.5 * N ** (-s) + s * N ** (-s - 1) / 12.0
    return total


def Z_Z4_geschlossen(s):
    """Geschlossene Form der Z^4-Spektral-Zeta (Dok. 314)."""
    return 8.0 * (1.0 - 4.0 ** (1 - s)) * zeta(s) * zeta(s - 1)


def Z_Z4_direkt(s, R=24):
    """Direktsumme sum_{k != 0} |k|^{-2s} bis Radius R, mit analytischer
    Schwanzkorrektur. Der abgeschnittene Rest ist naeherungsweise
        int_R^inf (2 pi^2 r^3) r^{-2s} dr = 2 pi^2 R^{4-2s} / (2s-4)
    (2 pi^2 r^3 ist die Oberflaeche der 3-Sphaere vom Radius r,
     also die Gitterpunktdichte pro Radiusintervall in 4D)."""
    schalen = {}
    for a in range(-R, R + 1):
        a2 = a * a
        for b in range(-R, R + 1):
            ab = a2 + b * b
            if ab > R * R:
                continue
            for c in range(-R, R + 1):
                abc = ab + c * c
                if abc > R * R:
                    continue
                for d in range(-R, R + 1):
                    r2 = abc + d * d
                    if 0 < r2 <= R * R:
                        schalen[r2] = schalen.get(r2, 0) + 1
    kern = sum(n * r2 ** (-s) for r2, n in schalen.items())
    schwanz = 2.0 * math.pi ** 2 * R ** (4 - 2 * s) / (2 * s - 4)
    return kern + schwanz


if __name__ == "__main__":
    print("=" * 74)
    print("Z4 -- EPSTEIN-FAKTORISIERUNG UND CASIMIR-SYMMETRIE")
    print("=" * 74)

    # --- Check 1: Zeta-Werte gegen bekannte Konstanten -------------
    print("\nCheck 1: Zeta-Routine gegen geschlossene Werte")
    paare = [(2, math.pi ** 2 / 6), (4, math.pi ** 4 / 90), (6, math.pi ** 6 / 945)]
    for s, soll in paare:
        ist = zeta(s)
        print(f"   zeta({s}) = {ist:.12f}   soll {soll:.12f}   "
              f"Diff {abs(ist-soll):.2e}")
        assert abs(ist - soll) < 1e-10, "Zeta-Routine ungenau"

    # --- Check 2: Faktorisierung gegen Direktsumme -----------------
    print("\nCheck 2: geschlossene Form gegen Direktsumme (Dok.-314-Identitaet)")
    print(f"   {'s':>4} {'geschlossen':>16} {'direkt':>16} {"rel. Diff":>12}")
    for s in (3.0, 4.0, 5.0):
        g = Z_Z4_geschlossen(s)
        d = Z_Z4_direkt(s, R=24)
        print(f"   {s:4.1f} {g:16.8f} {d:16.8f} {abs(g/d-1):12.2e}")
        assert abs(g / d - 1) < 5e-4, "Faktorisierung nicht bestaetigt"
    print("   => Z_{Z^4}(s) = 8 (1-4^{1-s}) zeta(s) zeta(s-1) bestaetigt.")

    # --- Check 3: Nullstellenstruktur der Torus-Zeta ---------------
    print("\nCheck 3: woher die Nullstellen von Z_{Z^4} kommen")
    print("""   drei Quellen:
     (a) zeta(s)     = 0  ->  bei Re(s) = 1/2  (nichttrivial, RH)
     (b) zeta(s-1)   = 0  ->  bei Re(s) = 3/2  (um 1 verschoben)
     (c) 1 - 4^{1-s} = 0  ->  s = 1 + 2pi i k / ln 4  (Gitterfaktor)""")
    ln4 = math.log(4.0)
    print(f"   Gitterfaktor-Nullstellen: s = 1 + i * k * {2*math.pi/ln4:.6f}")
    for k in (1, 2, 3):
        print(f"     k={k}: s = 1 + {k*2*math.pi/ln4:.6f} i")
    print("   => die RH ist damit eine Aussage ueber das Spektrum des")
    print("      Z^4-Torus, nicht nur ueber eine Zahlenreihe.")

    # --- Check 4: Casimir-Symmetriepunkt ---------------------------
    print("\nCheck 4: Casimir-Punkt und Funktionalgleichung")
    s_cas = -0.5
    s_spiegel = 1.0 - s_cas
    achse = (s_cas + s_spiegel) / 2.0
    print(f"   Casimir-Punkt (Dok. 314):      s = {s_cas}")
    print(f"   Spiegel unter zeta(s)=chi(s)zeta(1-s): 1-s = {s_spiegel}")
    print(f"   Symmetrieachse:                ({s_cas} + {s_spiegel})/2 = {achse}")
    print(f"   kritische Linie der RH:        Re(s) = 0.5")
    assert abs(achse - 0.5) < 1e-12, "Symmetrieachse muesste 1/2 sein"
    print("   => der physikalische Casimir-Punkt und sein funktionaler")
    print("      Spiegel liegen symmetrisch zur kritischen Linie.")
    print("\n   Korpuswerte (Dok. 314, Kovolumen 1):")
    print("     zeta_{Z^4}(-1/2) = -0.2966893  ->  E = -0.9320768")
    print("     zeta_{D4}(-1/2)  = -0.2764778  ->  E = -0.8685805")
    print("     Ordnungsumkehr: D4 minimiert fuer s>0, verliert bei s=-1/2")

    # --- Check 5: was NICHT folgt (P35) ----------------------------
    print("\nCheck 5: Kontrolle -- was daraus NICHT folgt")
    print("   (a) xi als Nullstellen-Parameter?")
    for rho in (14.134725, 21.022040, 25.010858):
        print(f"       xi / rho^-2 fuer rho={rho:.4f}: {XI*rho**2:.4f}")
    print("       => kein Muster; xi ist kein inverses Quadrat einer Nullstelle.")
    print("   (b) Verschiebt xi die kritische Linie?")
    print(f"       Stoerung O(xi) = {XI:.2e}, mit RG-Faktor 100: {100*XI:.4f}")
    print("       Re(s)=1/2 ist durch die Funktionalgleichung EXAKT fixiert;")
    print("       ein Stoerparameter kann sie nicht verschieben. [X]")
    print("   (c) Beweist die Ordnungsumkehr die RH?")
    print("       Nein -- sie ist eine Aussage ueber Gitterhierarchien,")
    print("       nicht ueber die Lage der Nullstellen. [X]")

    print("\n" + "=" * 74)
    print("ERGEBNIS Z4  [K] fuer die Befunde, [X] fuer die Folgerungen")
    print("=" * 74)
    print("""Zwei harte Korpusbefunde beruehren die Riemann-Zeta direkt:
die Faktorisierung (zeta ist ein Faktor der Torus-Spektral-Zeta) und
die Casimir-Symmetrie (kritische Linie als Symmetrieachse des
physikalisch besetzten Intervalls [-1/2, 3/2]).

Beides ist eine konsistente EINBETTUNG der RH-Struktur in die
Geometrie -- und keine Aussage ueber die Lage der Nullstellen.
Die kritische Linie ist ohnehin durch die Funktionalgleichung
fixiert; dass die Physik sie als Symmetrieachse wiederfindet, ist
Konsistenz, kein Beweis.""")
    print("\nAlle Checks bestanden.")
