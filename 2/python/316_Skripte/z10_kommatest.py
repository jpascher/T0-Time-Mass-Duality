#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""z10_kommatest.py -- Ist die fraktale Korrektur ein temperierendes
Instrument?

Ausgangsfrage. Beim Gehoer sitzt die Mittelung im Empfaenger: kritische
Baender, endliche Aufloesung, das Messinstrument wird Teil des
Ergebnisses. In der Mathematik gibt es keinen Empfaenger, dort muss die
Temperierung als Setzung eingefuegt werden. Fuer die Natur ist offen,
ob es einen Empfaenger gibt -- und ob K_frak ihn stellt.

Pruefbare Fassung. Eine Temperierung hinterlaesst einen Rest, und dieser
Rest ist immer ein Komma: ein Verhaeltnis GLATTER Zahlen (nur kleine
Primfaktoren). Der Korpus kennt einen Rest -- die ~7 eV aus P-315-2,
45000-fach ueber dem Messboden. Hat er Kommastruktur?

  TEST A  Groessenvergleich mit bekannten Kommas
  TEST B  Glattheitstest der besten rationalen Naeherungen
  TEST C  Kontrollprobe: erkennt der Test echte Kommas?
  TEST D  Aufloesung statt Temperierung -- der andere Mechanismus

Nur Standardbibliothek.
"""
import math
from fractions import Fraction

REST = 1.36e-5          # P-315-2, relativer Rest auf K/m_e-Ebene
XI = 4.0 / 30000.0

KOMMAS = {
    "pythagoreisch 531441/524288": Fraction(531441, 524288),
    "syntonisch 81/80": Fraction(81, 80),
    "Schisma 32805/32768": Fraction(32805, 32768),
    "Breedsma 2401/2400": Fraction(2401, 2400),
    "Ragisma 4375/4374": Fraction(4375, 4374),
    "Landscape 250047/250000": Fraction(250047, 250000),
}


def glatt(n, limit):
    """Ist n ein Produkt nur aus Primzahlen <= limit?"""
    for p in (2, 3, 5, 7, 11, 13):
        if p > limit:
            break
        while n % p == 0:
            n //= p
    return n == 1


def glattheitsurteil(f, ziel, tol=0.05):
    """Prueft Glattheit -- aber nur, wenn die Naeherung den Zielwert
    ueberhaupt trifft. Ohne diese Bedingung meldet der Test die
    triviale Naeherung 1/1 als 'glatt'."""
    if abs(float(f) - ziel) / abs(ziel - 1.0) > tol:
        return None            # Naeherung zu grob, keine Aussage
    for lim, name in ((5, "5-Limit"), (7, "7-Limit"), (13, "13-Limit")):
        if glatt(f.numerator, lim) and glatt(f.denominator, lim):
            return name
    return ""


if __name__ == "__main__":
    print("=" * 74)
    print("Z10 -- IST DIE FRAKTALE KORREKTUR EIN TEMPERIERENDES INSTRUMENT?")
    print("=" * 74)
    ziel = 1.0 + REST
    print(f"\n   Rest aus P-315-2: {REST:.3e}   ->   Verhaeltnis {ziel:.10f}")

    # ---------------------------------------------------- TEST A
    print("\nTEST A: Groessenvergleich mit bekannten Kommas")
    print("-" * 74)
    print(f"   {'Komma':>28} {'relativ':>12} {'Vielfaches des Rests':>22}")
    for n, v in sorted(KOMMAS.items(), key=lambda x: -x[1]):
        rel = float(v) - 1
        print(f"   {n:>28} {rel:12.3e} {rel/REST:22.1f}")
    print("""   => der Rest liegt um Faktor 14 bis 1000 unter allen bekannten
      Kommas. Das schliesst nichts aus -- Kommas gibt es in jeder
      Groesse --, macht aber eine Zuordnung nicht von selbst plausibel.""")

    # ---------------------------------------------------- TEST B
    print("\nTEST B: hat 1 + Rest die Struktur eines Kommas?")
    print("-" * 74)
    print("""   Jedes Komma ist ein Verhaeltnis glatter Zahlen -- Produkte
   kleiner Primzahlen. Geprueft werden die besten rationalen
   Naeherungen an 1 + Rest.""")
    print(f"\n   {'Nenner <=':>12} {'Naeherung':>22} {'Trefferguete':>13}  Urteil")
    treffer = []
    for maxden in (10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7, 10 ** 8):
        f = Fraction(ziel).limit_denominator(maxden)
        guete = abs(float(f) - ziel) / REST
        urteil = glattheitsurteil(f, ziel)
        if urteil is None:
            txt = "zu grob, keine Aussage"
        elif urteil:
            txt = f"<== {urteil}-glatt"
            treffer.append((f, urteil))
        else:
            txt = "nicht glatt"
        print(f"   {maxden:>12} {str(f):>22} {guete:12.1%}  {txt}")
    assert not treffer, "Unerwartet: der Rest zeigt Kommastruktur"
    print("""
   => KEINE der brauchbaren Naeherungen ist glatt. Der Rest hat keine
      Kommastruktur.

   Anmerkung zur Testfuehrung: ohne die Trefferguete-Bedingung meldet
   der Glattheitstest die triviale Naeherung 1/1 als '5-Limit-glatt'
   -- bei 100% Restfehler. Diese Bedingung ist notwendig, nicht
   kosmetisch.""")

    # ---------------------------------------------------- TEST C
    print("\nTEST C: Kontrollprobe -- erkennt der Test echte Kommas?")
    print("-" * 74)
    erkannt = 0
    for name, v in KOMMAS.items():
        f = Fraction(float(v)).limit_denominator(10 ** 6)
        u = glattheitsurteil(f, float(v))
        ok = bool(u)
        erkannt += ok
        print(f"   {name:>28}  ->  {f.numerator}/{f.denominator}"
              f"   {u if u else 'nicht glatt'}")
    assert erkannt >= 5, "Der Test muesste echte Kommas erkennen"
    print(f"   => {erkannt} von {len(KOMMAS)} erkannt: der Test hat Trennschaerfe.")

    # ---------------------------------------------------- TEST D
    print("\nTEST D: der andere Mechanismus -- Aufloesung statt Temperierung")
    print("-" * 74)
    print("""   Eine Temperierung veraendert die Werte und hinterlaesst ein
   Komma. Eine Aufloesungsgrenze veraendert nichts und hinterlaesst
   nichts -- sie macht Unterschiede nur unsichtbar. Beide Mechanismen
   machen Unterscheidungen verschwinden, aber nur der erste erzeugt
   Reste.""")
    lP = 1.616255e-35
    lam_e = 3.8615926796e-13
    L0, Lstar = XI * lP, 4 * lam_e / XI ** 10
    print(f"\n   FFGFT-Doppel-Cutoff: L0 = {L0:.3e} m, L* = {Lstar:.3e} m")
    print(f"   Skalenfenster ln(L*/L0) = {math.log(Lstar/L0):.2f}")
    print(f"   Peakbreite der Nullstellenmessung (z9): 0.0021")
    ragisma = math.log(4375.0 / 4374.0)
    print(f"   Ragisma als Laenge:                     {ragisma:.6f}")
    print(f"   => {ragisma/0.0021:.2f} Peakbreiten: unsichtbar, aber vorhanden.")
    print("""
   Genau dies ist der Fall 'Instrument wird Teil des Ergebnisses'
   ohne Temperierung: Die Struktur bleibt exakt, nur die Messung
   trennt nicht mehr. Kein Komma entsteht, weil nichts veraendert
   wurde.""")

    # ---------------------------------------------------- FAZIT
    print("\n" + "=" * 74)
    print("ERGEBNIS Z10")
    print("=" * 74)
    print("""   [X] Die fraktale Korrektur ist nicht das temperierende
   Instrument. Waere K_frak eine Temperierung, muesste sie einen
   kommaartigen Rest hinterlassen; der vorhandene Rest hat diese
   Struktur nicht (Test B, bei erwiesener Trennschaerfe in Test C).
   Das praezisiert P-315-2: die ~7 eV sind eher Polmassen-Effekt oder
   echter Korrekturterm als Abfall einer Rationalisierung.

   [B] K_frak sitzt gleichwohl dort, wo ein Instrument saesse:
   Dok. 314 D2 fuehrt sie als Eigenschaft der DURCHQUERUNG, die ueber
   die Brueckenkonstanten hereinkommt, nicht ueber den lokalen
   Operator. Sie aehnelt einem Messeffekt im Ort, nicht im Charakter
   -- sie ist exakt, nicht mittelnd.

   [B] Der eigentliche Kandidat fuer das Instrument ist der
   Doppel-Cutoff. Er erzeugt eine Aufloesungsgrenze, und genau dort
   wird das Verfahren Teil des Ergebnisses (Test D) -- ohne Komma,
   weil nichts veraendert wird.

   Damit die Dreiteilung: Das Gehoer mittelt AKTIV und erzeugt
   Kommas. Die Mathematik hat keinen Empfaenger, dort muss temperiert
   werden -- durch Setzung. Die Natur, sofern FFGFT recht hat,
   schneidet PASSIV ab: Unterscheidungen verschwinden ohne
   Rationalisierung, und die fraktale Korrektur ist daran nicht
   beteiligt.""")
    print("\nAlle Checks bestanden.")
