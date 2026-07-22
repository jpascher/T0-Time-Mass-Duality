#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""_bereich.py -- gemeinsame Prueflogik der A-Serie.

Die Theorie berechnet nichts (A220). Es gibt genau zwei Arten von Pruefung:

  identitaet(name, wert, soll)  -- rechnet eine DEFINITION nach. Kann nur an
      einem Programmierfehler scheitern; Bestehen ist kein Verdienst.

  im_bereich(name, wert, ziel, faktor) -- BEREICHSKONTROLLE: liegt der Wert in
      der richtigen Groessenordnung des Ziels (Standard: innerhalb Faktor 3)?

  vorhersage(name, wert, gemessen, sigma) -- VORHERSAGE: ein aus der Struktur
      vorhergesagter, MESSBARER Wert, verglichen mit der Messung in Einheiten
      der Messunsicherheit. Das ist der Fall der Leptonmassen: die Struktur
      (sqrt2, 2/9) sagt m_tau aus m_e, m_mu voraus. Anders als Identitaet und
      Bereich ist dies eine echte, scharfe, falsifizierbare Vorhersage.

Identitaet und Bereich behaupten kein exaktes Ergebnis. Die Vorhersage schon --
aber nur im Rahmen der Messunsicherheit, nicht auf beliebige Stellen.
"""


def identitaet(name, wert, soll, eps=1e-9):
    ok = abs(wert - soll) <= eps * (1 + abs(soll))
    marke = "IDENTITAET (per Definition, keine Rechnung)" if ok \
        else "FEHLER IN DER ALGEBRA"
    print("   %-40s %s" % (name, marke))
    return ok


def im_bereich(name, wert, ziel, faktor=3.0):
    if ziel == 0:
        ok = abs(wert) < faktor
    else:
        q = abs(wert / ziel)
        ok = (1.0 / faktor) <= q <= faktor
    marke = "im richtigen Bereich" if ok else "AUSSERHALB des Bereichs"
    print("   %-40s %s" % (name, marke))
    return ok


def vorhersage(name, wert, gemessen, sigma):
    """Echte Vorhersage: Struktur sagt einen messbaren Wert voraus.
    Bestanden, wenn die Vorhersage innerhalb weniger sigma der Messung liegt."""
    n = abs(wert - gemessen) / sigma if sigma else float("inf")
    ok = n < 3.0
    marke = ("VORHERSAGE bestaetigt (%.2f sigma)" % n) if ok         else ("VORHERSAGE verfehlt (%.2f sigma)" % n)
    print("   %-40s %s" % (name, marke))
    return ok
