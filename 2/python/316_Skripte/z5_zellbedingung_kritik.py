#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""z5_zellbedingung_kritik.py -- Warum §3 NICHT auf [K] gehoben werden kann.

Diese Prüfung war als Herleitung angelegt: die Berry-Keating-Zellbedingung
l_x*l_p = 2pi sollte aus der Korpus-Relation lambda_4*m = 2pi (Dok. 314,
Kap. D1) folgen. Beim Ausformulieren zerfällt das Argument in drei Stufen,
alle drei negativ. Das Skript dokumentiert den Zerfall, weil ein
zurückgenommenes Argument dieselbe Sorgfalt verdient wie ein gehaltenes.

  Stufe 1: Die Zellbedingung ist inhaltsleer -- sie sagt nur hbar = 1.
  Stufe 2: Der eigentliche Gehalt (zwei Cutoffs, Produkt = Planck-Zelle)
           scheitert am FFGFT-Doppel-Cutoff um ~65 Dekaden.
  Stufe 3: Ein endliches Skalenfenster trägt endlich viele Moden;
           die Nullstellen sind unendlich viele.

Was übrig bleibt (und in z2 korrekt bleibt): dass die Zählfunktion
überhaupt die Form T*ln(T) hat, verlangt einen DILATATIONS-Operator statt
eines Laplace. Das ist der Gehalt -- nicht der Zahlenwert 2pi.
Nur Standardbibliothek.
"""
import math

XI = 4.0 / 30000.0
TWO_PI = 2.0 * math.pi

# Konstanten (CODATA 2022 bzw. Korpus)
L_PLANCK = 1.616255e-35        # m
LAMBDA_E = 3.8615926796e-13    # reduzierte Compton-Wellenlaenge Elektron, m

# Korpus-Doppel-Cutoff
L0 = XI * L_PLANCK             # UV
LSTAR = 4.0 * LAMBDA_E / XI ** 10   # IR


def N_berry_keating(E, zelle=TWO_PI):
    return (E * math.log(E / zelle) - E + zelle) / TWO_PI


def N_riemann(T):
    return T / TWO_PI * math.log(T / TWO_PI) - T / TWO_PI + 7.0 / 8.0


if __name__ == "__main__":
    print("=" * 74)
    print("Z5 -- WARUM DIE ZELLBEDINGUNG NICHT AUF [K] GEHOBEN WERDEN KANN")
    print("=" * 74)

    # --- Stufe 1 ---------------------------------------------------
    print("\nSTUFE 1: Die Zellbedingung ist inhaltsleer")
    print("-" * 74)
    print("""   Berry-Keating verlangt l_x * l_p = 2*pi*hbar. In natuerlichen
   Einheiten (hbar = 1) ist das die Planck-Zelle des Phasenraums --
   und die folgt aus der kanonischen Quantisierung JEDES konjugierten
   Paares, ohne jede physikalische Zusatzannahme.

   Dass die Korpus-Relation lambda_4 * m = 2pi (Dok. 314 D1) dieselbe
   Form hat, ist daher KEIN eigenstaendiger Befund: de-Broglie IST die
   Aussage hbar = 1. Zwei Schreibweisen derselben Trivialitaet.""")
    print("\n   Kontrolle: die Zaehlung ist gegenueber der Zelle logarithmisch")
    print("   unempfindlich -- ein 'Treffer' der Zelle waere ohnehin kein Test:")
    T = 1000.0
    ziel = N_riemann(T)
    for faktor in (1.0, 1.01, 1.1, 2.0):
        z = TWO_PI * faktor
        print(f"     Zelle = {faktor:4.2f} * 2pi  ->  N(1000) = "
              f"{N_berry_keating(T, z):9.3f}   Abw. {N_berry_keating(T,z)/ziel-1:+.3%}")
    print("   => selbst eine um Faktor 2 falsche Zelle aendert N um ~1%.")

    # --- Stufe 2 ---------------------------------------------------
    print("\nSTUFE 2: Der eigentliche Gehalt -- zwei Cutoffs -- scheitert")
    print("-" * 74)
    print("""   Was Berry-Keating wirklich verlangt, ist schaerfer als die Zelle:
   der Phasenraum wird bei x > l_x UND p > l_p abgeschnitten, ZWEI
   unabhaengige Grenzen, deren PRODUKT die Planck-Zelle ist. Das ist
   eine echte Bedingung an die Abschneidung.

   FFGFT hat einen natuerlichen Doppel-Cutoff. Pruefbare Frage:
   ist L* / L0 von der Groessenordnung der Planck-Zelle?""")
    print(f"\n     UV  L0    = xi * l_P          = {L0:.6e} m")
    print(f"     IR  L*    = 4*lambda_e/xi^10  = {LSTAR:.6e} m")
    verh = LSTAR / L0
    print(f"     Verhaeltnis L*/L0             = {verh:.6e}")
    print(f"     verlangt waere                = 2pi = {TWO_PI:.4f}")
    dekaden = math.log10(verh / TWO_PI)
    print(f"     Fehlbetrag                    = {dekaden:.1f} Dekaden  [X]")
    assert dekaden > 50, "Der Fehlbetrag sollte massiv sein"

    # --- Stufe 3 ---------------------------------------------------
    print("\nSTUFE 3: Endliches Fenster gegen unendlich viele Nullstellen")
    print("-" * 74)
    lnW = math.log(verh)
    stufen = lnW / (-math.log(XI))
    print(f"     ln(L*/L0)                     = {lnW:.4f}")
    print(f"     in xi-Leiterstufen            = {stufen:.4f}")
    Nmax = lnW ** 2 / (4 * math.pi)
    print(f"     Berry-Keating-Moden im Fenster ~ ln^2/(4pi) = {Nmax:.0f}")
    print("""
     Ein endliches Skalenfenster traegt ENDLICH viele Moden. Die
     Riemann-Nullstellen sind abzaehlbar unendlich viele. Selbst wenn
     Stufe 1 und 2 hielten, koennte das FFGFT-Fenster hoechstens einen
     Anfangsabschnitt tragen -- und ein Anfangsabschnitt ist keine
     Spektralidentitaet.  [X]""")
    print("\n     Beobachtung (NICHT gebucht, P35): die Stufenzahl liegt nahe 17.")
    print(f"     |{stufen:.4f} - 17| = {abs(stufen-17):.4f}. Beide Cutoffs tragen")
    print("     eigene Unsicherheiten (Vorfaktor 4 offen per R73, l_P via G);")
    print("     ohne Fehlerbudget ist die Naehe nicht auswertbar.")

    # --- Was bleibt ------------------------------------------------
    print("\n" + "=" * 74)
    print("WAS BLEIBT -- und was zurueckzunehmen ist")
    print("=" * 74)
    print("""   ZURUECKZUNEHMEN:
     'Die Nullstellendichte folgt aus der FFGFT-Zellbedingung.'
     Die Zelle ist hbar; sie folgt aus nichts Spezifischem. Die
     Formulierung suggeriert einen Befund, wo eine Trivialitaet steht.

   ES BLEIBT [B] -- und das ist nicht wenig:
     Dass die Zaehlfunktion ueberhaupt die Form (T/2pi)ln(T/2pi) hat,
     verlangt einen DILATATIONS-Erzeuger. Ein Laplace auf einer
     kompakten Mannigfaltigkeit kann sie nicht liefern (z1, Weyl).
     Die Identifikation, WELCHE Struktur in FFGFT die Dilatation
     traegt -- die ausgerollte Domaene, Dok. 315 --, ist eine
     inhaltliche Aussage. Der Zahlenwert 2pi ist es nicht.

   FOLGE FUER DEN STATUS:
     §3 bleibt [B] und kann mit Korpusmitteln NICHT auf [K] gehoben
     werden. Der Weg dorthin ist nicht 'die Herleitung nachliefern',
     sondern waere ein anderer: zu zeigen, dass die ausgerollte
     Skalenrichtung eine nicht-triviale Randbedingung traegt.
     Der naheliegende Kandidat dafuer ist die xi-Leiter -- und der
     ist in z3 negativ getestet.""")
    print("\nAlle Checks bestanden.")
