#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""z3_randbedingung_test.py -- Der entscheidende Test, negativ.

Nach Z2 fehlt dem Dilatationsoperator H = xp die Randbedingung, die aus
seinem kontinuierlichen Spektrum ein diskretes macht. Der natuerliche
FFGFT-Kandidat: die xi-Leiter erzeugt eine diskrete Untergruppe
Gamma_xi = {xi^n} < R+*, der Quotient R+*/Gamma_xi ist ein KREIS vom
Umfang L = ln(1/xi) = 8,9227. Zulaessige Dilatationsfrequenzen waeren
dann Vielfache von 2pi/L.

Dieses Skript testet das -- mit drei Disziplinen, die bei Naehe-Argumenten
noetig sind (P35):
  (1) Nullverteilung ueber zufaellige Perioden im GLEICHEN Bereich,
  (2) Artefaktkontrolle: Perioden groesser als der Datenbereich
      erzeugen automatisch kleine Scores,
  (3) Out-of-Sample-Pruefung an Nullstellen, die nicht im Fit waren,
      plus Look-elsewhere-Korrektur.

Ergebnis: negativ. Und das ist strukturell erwartbar -- die
Nullstellen sind GUE-verteilt (Niveau-Abstossung), ein Kreis
liefert ein aequidistantes Gitter.
Nur Standardbibliothek. Seed = Korpus-Seed 20780458.
"""
import math
import random
import statistics

SEED = 20780458
XI = 4.0 / 30000.0
TWO_PI = 2.0 * math.pi

# In-Sample: Nullstellen 1-30
ZEROS_IN = [
    14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178,
    40.918719, 43.327073, 48.005151, 49.773832, 52.970321, 56.446248,
    59.347044, 60.831779, 65.112544, 67.079811, 69.546402, 72.067158,
    75.704691, 77.144840, 79.337375, 82.910381, 84.735493, 87.425275,
    88.809111, 92.491899, 94.651344, 95.870634, 98.831194, 101.317851,
]
# Out-of-Sample: Nullstellen 31-50
ZEROS_OUT = [
    103.725538, 105.446623, 107.168611, 111.029536, 111.874659, 114.320221,
    116.226680, 118.790783, 121.370125, 122.946829, 124.256819, 127.516684,
    129.578704, 131.087688, 133.497737, 134.756510, 138.116042, 139.736209,
    141.123707, 143.111846,
]


def score(zeros, periode):
    """Mittlerer Abstand von rho/periode zur naechsten ganzen Zahl.
    0 = perfekte Kommensurabilitaet, 0.25 = Zufall."""
    return statistics.mean(abs(z / periode - round(z / periode)) for z in zeros)


def nullverteilung(zeros, lo, hi, n=20000, seed=SEED):
    rng = random.Random(seed)
    return [score(zeros, rng.uniform(lo, hi)) for _ in range(n)]


if __name__ == "__main__":
    print("=" * 74)
    print("Z3 -- LIEFERT DIE XI-LEITER DIE FEHLENDE RANDBEDINGUNG?")
    print("=" * 74)
    L = -math.log(XI)
    print(f"\n   xi = {XI:.6e}")
    print(f"   L = ln(1/xi) = {L:.6f}   (Umfang des Dilatationskreises)")
    print(f"   Grundfrequenz 2pi/L = {TWO_PI/L:.6f}")

    # --- Check 1: Artefaktkontrolle ZUERST -------------------------
    print("\nCheck 1: Artefaktkontrolle -- grosse Perioden taeuschen Signale vor")
    print(f"   groesste In-Sample-Nullstelle: {max(ZEROS_IN):.2f}")
    print(f"   {'Periode':>10} {'Score':>8}  Bemerkung")
    for P in (5.0, 50.0, 200.0, 468.09, 1000.0):
        s = score(ZEROS_IN, P)
        bem = "" if P < 2 * max(ZEROS_IN) else "<- Artefakt: alle rho/P runden auf 0"
        print(f"   {P:10.2f} {s:8.4f}  {bem}")
    assert score(ZEROS_IN, 1000.0) < 0.10, "Artefakt sollte auftreten"
    print("   => Perioden > ~2*max(rho) sind auszuschliessen. Die")
    print("      Nullverteilung MUSS denselben Bereich abdecken wie die")
    print("      Kandidaten, sonst entstehen Scheinsignale.")

    # --- Check 2: Kandidaten im zulaessigen Bereich ----------------
    print("\nCheck 2: xi-abgeleitete Kandidaten (Bereich 0.5 - 12)")
    kandidaten = {
        "2pi/ln(1/xi)": TWO_PI / L,
        "2pi/ln(75)": TWO_PI / math.log(75.0),
        "ln(1/xi)": L,
        "2pi": TWO_PI,
        "2pi/ln(50/2pi) (mittl. Abstand)": TWO_PI / math.log(50.0 / TWO_PI),
    }
    null_in = nullverteilung(ZEROS_IN, 0.5, 12.0)
    print(f"   Nullverteilung: Mittel {statistics.mean(null_in):.4f}, "
          f"Std {statistics.stdev(null_in):.4f}, Min {min(null_in):.4f}")
    print(f"\n   {'Kandidat':>32} {'Periode':>10} {'Score':>8} {'p-Wert':>9}")
    pwerte = {}
    for name, P in kandidaten.items():
        s = score(ZEROS_IN, P)
        pv = sum(1 for x in null_in if x <= s) / len(null_in)
        pwerte[name] = (P, s, pv)
        print(f"   {name:>32} {P:10.4f} {s:8.4f} {pv:9.4f}")

    # --- Check 3: Out-of-Sample fuer den besten Kandidaten ---------
    best = min(pwerte, key=lambda k: pwerte[k][2])
    P_best, s_in, pv_in = pwerte[best]
    print(f"\nCheck 3: Out-of-Sample-Pruefung des besten Kandidaten")
    print(f"   Kandidat: {best}, Periode {P_best:.4f}")
    print(f"   In-Sample  (rho 1-30):  Score {s_in:.4f}, p = {pv_in:.4f}")
    s_out = score(ZEROS_OUT, P_best)
    null_out = nullverteilung(ZEROS_OUT, 0.5, 12.0, seed=SEED + 1)
    pv_out = sum(1 for x in null_out if x <= s_out) / len(null_out)
    print(f"   Out-of-Sample (rho 31-50): Score {s_out:.4f}, p = {pv_out:.4f}")
    pv_korr = min(1.0, pv_out * len(kandidaten))
    print(f"   Look-elsewhere ({len(kandidaten)} Kandidaten): p_korr = {pv_korr:.3f}")
    ueberlebt = pv_korr < 0.05
    print(f"   => {'SIGNAL ueberlebt' if ueberlebt else 'Signal ueberlebt NICHT'}")
    assert not ueberlebt, "Unerwartet: Signal ueberlebt -- neu pruefen"

    # --- Check 4: warum das strukturell erwartbar war --------------
    print("\nCheck 4: GUE-Kontrolle (Montgomery-Odlyzko) -- normierte Abstaende")
    alle = ZEROS_IN + ZEROS_OUT
    sp = []
    for i in range(len(alle) - 1):
        dichte = math.log(alle[i] / TWO_PI) / TWO_PI
        sp.append((alle[i + 1] - alle[i]) * dichte)
    anteil_klein = sum(1 for s in sp if s < 0.3) / len(sp)
    print(f"   mittlerer normierter Abstand: {statistics.mean(sp):.4f} (soll ~1)")
    print(f"   Anteil Abstaende < 0.3:       {anteil_klein:.3f}")
    print(f"     GUE (Niveau-Abstossung):    ~0.04")
    print(f"     Poisson / gitterartig:      ~0.26")
    assert anteil_klein < 0.15, "Niveau-Abstossung sollte sichtbar sein"
    print("   => klare Niveau-Abstossung: GUE-artig, NICHT gitterartig.")
    print("      Eine Kreis-Kompaktifizierung erzeugt ein aequidistantes")
    print("      Gitter -- sie kann GUE prinzipiell nicht liefern.")

    print("\n" + "=" * 74)
    print("ERGEBNIS Z3  [X]")
    print("=" * 74)
    print("""Die xi-Leiter liefert die fehlende Randbedingung NICHT.
Kein xi-abgeleiteter Periodenkandidat ueberlebt die
Out-of-Sample-Pruefung mit Look-elsewhere-Korrektur.

Das ist kein Zufallsbefund, sondern strukturell erwartbar: eine
Ein-Perioden-Kompaktifizierung erzeugt aequidistante Spektren, die
Nullstellen zeigen aber GUE-Statistik mit Niveau-Abstossung. Die
fehlende Randbedingung traegt die Arithmetik (Primzahlen), nicht die
Geometrie.""")
    print("\nAlle Checks bestanden.")
