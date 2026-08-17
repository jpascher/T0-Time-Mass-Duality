#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""z9_limit_einschluss.py -- Schliesst das 5-Limit die hoeheren ein?

Fuenf Lesarten von 'einschliessen', alle gerechnet:

  (1) EXAKT           nein, per Primfaktorzerlegung
  (2) DICHT           ja, beliebig genau -- der Naeherungsfehler an ln7
                      ist genau das Ragisma 4375/4374
  (3) AUFLOESUNG      ja, bei der Peakbreite dieser Messung
                      ununterscheidbar
  (4) GEWICHTET       nein, Tenney-Gewicht des Naeherungspunkts
                      3.7e-7 gegen 1/7
  (5) TEMPERIERT      ja, aber per Setzung (ragismische Temperatur)

Das Muster ist dasselbe wie ueberall in Dok. 316: Einschliessung
entsteht durch Rationalisierung oder durch begrenzte Aufloesung,
nie durch Struktur.
Nur Standardbibliothek. Nullstellen aus z8.
"""
import math
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from z8_bikohaerenz import nullstellen, F_bloecke  # noqa: E402

L2, L3, L5 = math.log(2.0), math.log(3.0), math.log(5.0)


def beste_naeherung(ziel, N):
    """Bester 5-Limit-Punkt a*ln2+b*ln3+c*ln5 mit |Exponenten| <= N."""
    best = (float("inf"), None)
    for a in range(-N, N + 1):
        va = a * L2
        for b in range(-N, N + 1):
            vab = va + b * L3
            c = round((ziel - vab) / L5)
            if abs(c) <= N:
                d = abs(vab + c * L5 - ziel)
                if d < best[0]:
                    best = (d, (a, b, c))
    return best


def tenney(e):
    return 1.0 / (2 ** abs(e[0]) * 3 ** abs(e[1]) * 5 ** abs(e[2]))


if __name__ == "__main__":
    print("=" * 74)
    print("Z9 -- SCHLIESST DAS 5-LIMIT DIE HOEHEREN EIN?")
    print("=" * 74)

    # ---------------------------------------------------- (1)
    print("\n(1) EXAKTE ENTHALTUNG: nein, beweisbar")
    print("-" * 74)
    print("""    ln7 = a ln2 + b ln3 + c ln5 mit rationalen a,b,c hiesse
    durchmultipliziert 7^q = 2^A 3^B 5^C -- Widerspruch zur
    Eindeutigkeit der Primfaktorzerlegung. Gilt fuer jede Primzahl
    oberhalb des Limits, also fuer unendlich viele.""")

    # ---------------------------------------------------- (2)
    print("\n(2) DICHTE APPROXIMATION: ja, beliebig genau")
    print("-" * 74)
    print("""    ln2, ln3, ln5 sind ueber Q linear unabhaengig, also liegt
    {a ln2 + b ln3 + c ln5} dicht in R.""")
    u7 = math.log(7.0)
    print(f"\n    Beste Naeherungen an ln7 = {u7:.8f}:")
    print(f"    {'N':>3} {'Fehler':>11} {'Cent':>8} {'Exponenten':>14} "
          f"{'Tenney':>11}")
    for N in (2, 4, 6, 8, 12):
        d, e = beste_naeherung(u7, N)
        print(f"    {N:>3} {d:11.2e} {d*1200/L2:8.3f} {str(e):>14} "
              f"{tenney(e):11.2e}")
    d8, e8 = beste_naeherung(u7, 8)
    ragisma = math.log(4375.0 / 4374.0)
    print(f"\n    Der Fehler der besten Naeherung {e8} ist {d8:.6e}.")
    print(f"    ln(4375/4374) = {ragisma:.6e}  -- das RAGISMA.")
    assert abs(d8 - ragisma) < 1e-12, "Naeherungsfehler sollte das Ragisma sein"
    d2, e2 = beste_naeherung(u7, 6)
    archytas = math.log(64.0 / 63.0)
    grob = 6 * L2 - 2 * L3
    print(f"    Die grobe Naeherung (6,-2,0) = ln(64/9) hat den Fehler")
    print(f"    ln(64/63) = {archytas:.6f} -- das ARCHYTAS-KOMMA "
          f"({archytas*1200/L2:.1f} Cent).")
    assert abs(abs(grob - u7) - archytas) < 1e-12, "Archytas-Komma erwartet"
    print("""
    Beide Kommas sind aus dem Euler-Kontrollfall bekannt: das Ragisma
    als bester 7-Limit-Beinaheschluss, das Archytas-Komma als
    septimales Gegenstueck zum syntonischen. Sie treten hier in
    anderer Rolle wieder auf -- als Fehler der 5-Limit-Naeherung an
    die 7-Achse. Das ist dieselbe Groesse aus der Gegenrichtung
    gelesen.""")

    # ---------------------------------------------------- (3)
    print("\n(3) BEI ENDLICHER AUFLOESUNG: ja, ununterscheidbar")
    print("-" * 74)
    zs = nullstellen()
    breite = 2 * math.pi / (max(zs) - min(zs))
    appr = e8[0] * L2 + e8[1] * L3 + e8[2] * L5
    print(f"    Peakbreite 2pi/(Hoehenspanne) = {breite:.5f}")
    print(f"    ln7                    = {u7:.8f}")
    print(f"    Naeherung {str(e8):>12}   = {appr:.8f}")
    print(f"    Abstand = {abs(u7-appr):.2e} = {abs(u7-appr)/breite:.2f} "
          f"Peakbreiten")
    assert abs(u7 - appr) < breite, "Naeherung sollte unter der Peakbreite liegen"

    NB = 24
    F = F_bloecke(zs, NB)

    def leistung(u):
        v = F(u)
        return sum(abs(x) ** 2 for x in v) / len(v) / (len(zs) / NB)

    print(f"\n    Messung:")
    L_exakt, L_appr = leistung(u7), leistung(appr)
    L_grob, L_kontr = leistung(grob), leistung(u7 + 0.05)
    for u, name, L in ((u7, "ln7 exakt", L_exakt),
                       (appr, f"Naeherung {e8}", L_appr),
                       (grob, "grob (6,-2,0) = ln(64/9)", L_grob),
                       (u7 + 0.05, "Kontrolle ln7 + 0.05", L_kontr)):
        print(f"      {name:28s} u={u:.6f}  Leistung {L:7.3f}")
    assert abs(L_exakt - L_appr) / L_exakt < 0.01, \
        "Naeherung sollte ununterscheidbar sein"
    assert L_grob < 0.8 * L_exakt, "grobe Naeherung sollte abfallen"
    assert L_kontr < 0.1 * L_exakt, "Kontrollpunkt sollte im Rauschen liegen"
    print("""
    Die feine Naeherung ist von ln7 nicht zu unterscheiden, die grobe
    faellt ab, der Kontrollpunkt liegt im Rauschen. Bei dieser
    Aufloesung enthaelt das 5-Limit ln7 also effektiv -- eine Aussage
    ueber das Messverfahren, nicht ueber die Arithmetik.""")

    # ---------------------------------------------------- (4)
    print("\n(4) AMPLITUDENGEWICHTET: nein, und deutlich")
    print("-" * 74)
    w = tenney(e8)
    print(f"    Tenney-Gewicht der Naeherung {e8}: {w:.2e}")
    print(f"    Tenney-Gewicht von ln7 als eigener Achse:   {1/7:.4f}")
    print(f"    Verhaeltnis: {(1/7)/w:.3e}")
    assert (1 / 7) / w > 1e5, "Gewichtsunterschied sollte gross sein"
    print("""    Im amplitudengewichteten Bild traegt der Naeherungspunkt
    nichts. Das 5-Limit enthaelt ln7 nur als unhoerbar leise
    Kombination -- was zugleich erklaert, warum die Naeherung so
    genau sein kann: sie braucht grosse Exponenten, und grosse
    Exponenten bedeuten kleines Gewicht.""")

    # ---------------------------------------------------- (5)
    print("\n(5) DURCH TEMPERIERUNG: ja, aber per Setzung")
    print("-" * 74)
    print(f"""    Erklaert man das Ragisma 4375/4374 zu 1, so IST
    7 = 2 * 3^7 / 5^4 im temperierten System (ragismische Temperatur).
    Ebenso macht die Wegtemperierung des Archytas-Kommas 64/63 die
    Naeherung 64/9 exakt.""")

    print("\n" + "=" * 74)
    print("ERGEBNIS Z9")
    print("=" * 74)
    print("""    Das 5-Limit schliesst die hoeheren Limits nicht ein --
    ausser man laesst Naeherung, begrenzte Aufloesung oder
    Temperierung als Einschliessung gelten.

    Das Muster ist dasselbe wie ueberall in diesem Dokument:
    Einschliessung entsteht durch Rationalisierung (Temperierung)
    oder durch Unschaerfe (Aufloesung), nie durch Struktur. Ebenso
    schliesst die Euler-Spirale nur durch Temperierung, und ebenso
    sitzt Kopplung im Weil-Spektrum nur bei exakten
    Primzahlpotenzen.

    Fuer xi folgt nichts Neues, aber eine Bestaetigung: dass xi ein
    reiner 5-Limit-Punkt ist, laesst sich durch keine Erweiterung
    heilen -- und die Naeherungen, die eine Erweiterung ersetzen
    koennten, tragen kein Gewicht.""")
    print("\nAlle Checks bestanden.")
