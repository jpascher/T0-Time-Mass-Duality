#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
audit_a_serie.py -- Adversariales Selbst-Audit der FFGFT A-Serie

Legt an die eigenen Dokumente denselben Massstab an, der in der
IPI-Korrespondenz an fremde Manuskripte angelegt wird. Die sechs Pruefungen
entsprechen den Befundarten, die dort tatsaechlich Treffer erzeugt haben:

  A1  Entwurfskommentar im kanonischen Text
      (Vorbild: vier Passagen Draft-Kommentar in Constitutional Physics)
  A2  Doppelte Abschnittsnummern / zusammengefuehrte Entwuerfe
      (Vorbild: Volume III mit zwei Abschnitten "2")
  A3  Selbstausnahme -- das Dokument verletzt eine Regel, die es selbst aufstellt
      (Vorbild: CDM 10.4.11 in Kap. 13-21 befolgt, in Kap. 22 nicht)
  A4  Begriffsinflation -- ein Leitbegriff verliert durch Haeufigkeit
      seine Unterscheidungskraft
      (Vorbild: "constitutional" 5151x in 55671 Woertern)
  A5  Ableitungsanspruch, wo tatsaechlich gesetzt wird
      (Vorbild: 22.1 -- Rolle per Argument, Besetzung per Stipulation)
  A6  Fehlendes Residuum -- Dokument benennt nicht, was es offen laesst
      (Vorbild: CDM 10.4.11 als Anforderung an jede abgeschlossene Recovery)

Aufruf:  python3 audit_a_serie.py [SOURCES_DIR]
Exit 0 = kein Befund, Exit 1 = mindestens ein Befund.
Reine Standardbibliothek.
"""

import os
import re
import sys
from collections import Counter

# ------------------------------------------------------------------ A1

# PRAEZISIONS-KORREKTUR (Altbestand-Scan 20.07.2026):
# Die erste Fassung fuehrte "Platzhalter" und "wollen wir" als Trigger und
# erzeugte damit 6 von 6 Fehlalarmen auf 231 Altdokumenten -- "dimensionaler
# Platzhalter" ist dort Fachbegriff, "wollen wir" normale Fachprosa. Beide
# entfernt. Uebrig bleiben nur Muster, die den Leser oder den Assistenten
# direkt adressieren oder als Arbeitsmarke gesetzt sind.
ENTWURFSSPUREN = [
    r"\bTODO\b", r"\bFIXME\b", r"\bXXX\b",
    r"\bhier fehlt noch\b", r"\bnoch einzufuegen\b", r"\bnoch einzufügen\b",
    r"\bder naechste Abschnitt sollte\b", r"\bder nächste Abschnitt sollte\b",
    r"\bdu hast gefragt\b", r"\bwie du gewuenscht\b", r"\bwie gewünscht hast\b",
    r"\bich denke, hier\b", r"\bsoll ich\b", r"\blass uns\b",
    r"\bdas fuegen wir\b", r"\bwie besprochen\b",
    r"\bhier beginnt die\b.{0,40}\bBeschleunigung\b",
]

# ------------------------------------------------------------------ A4

# Leitbegriffe, deren Inflation die Unterscheidungskraft kostet.
LEITBEGRIFFE = ["fraktal", "geometrisch", "Struktur", "Serie", "Schicht",
                "Setzung", "Toleranz", "Projektion"]
INFLATIONSSCHWELLE = 0.010   # Anteil an allen Woertern; Vorbild lag bei 0,0925

# ------------------------------------------------------------------ A5

ABLEITUNGSVERBEN = [
    r"folgt aus", r"ergibt sich aus", r"ist hergeleitet", r"wird hergeleitet",
    r"leitet sich ab", r"zwingt", r"erzwing", r"beweist",
]
SETZUNGSVERBEN = [
    r"wird gesetzt", r"deklarier", r"stipulier", r"per Definition",
    r"wir waehlen", r"wird gewaehlt", r"Konvention", r"Setzung",
]

# ------------------------------------------------------------------ A6

RESIDUUM_MARKER = [
    r"\\section\{Was offen bleibt\}",
    r"\\section\{Offen\}",
    r"\\section\{Residuum\}",
]

SCHICHT_RE = r"\[(K|B|S|SETZUNG)\]"


class Befund:
    def __init__(self):
        self.eintraege = []

    def add(self, doc, code, schwere, text):
        self.eintraege.append((doc, code, schwere, text))

    def hat_fehler(self):
        return any(s == "BEFUND" for _, _, s, _ in self.eintraege)


def klartext(tex):
    """LaTeX grob zu Text: Kommentare, Befehle, Mathe entfernen."""
    t = re.sub(r"(?<!\\)%.*", "", tex)
    t = re.sub(r"\$[^$]*\$", " ", t)
    t = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?(\{[^}]*\})?", " ", t)
    t = re.sub(r"[{}\\]", " ", t)
    return t


# ------------------------------------------------------------------ Pruefungen

def a1_entwurfsspuren(doc, tex, b):
    treffer = 0
    for nr, z in enumerate(tex.splitlines(), 1):
        z = re.sub(r"(?<!\\)%.*", "", z)
        for pat in ENTWURFSSPUREN:
            if re.search(pat, z, re.IGNORECASE):
                b.add(doc, "A1", "BEFUND",
                      "Zeile %d Entwurfskommentar: %s" % (nr, z.strip()[:70]))
                treffer += 1
    if not treffer:
        b.add(doc, "A1", "OK", "kein Entwurfskommentar im kanonischen Text")


def a2_doppelnummern(doc, tex, b):
    titel = re.findall(r"\\section\{(.+?)\}", tex)
    # texorpdfstring-Huellen entfernen
    titel = [re.sub(r"\\texorpdfstring", "", t).strip() for t in titel]
    dubl = [t for t, n in Counter(titel).items() if n > 1]
    for t in dubl:
        b.add(doc, "A2", "BEFUND", "Abschnittstitel doppelt: %s" % t[:60])
    if not dubl:
        b.add(doc, "A2", "OK", "%d Abschnitte, keine Dubletten" % len(titel))


def a3_selbstausnahme(doc, tex, b):
    """Regeln, die das Dokument aufstellt, gegen sein eigenes Verhalten."""
    # Breit gefasst: jede Formulierung, die Markierung pro Aussage verlangt.
    # (Die erste Fassung dieses Detektors verfehlte den realen Fall in A010,
    #  weil sie nur "Schichtmarkierung" und nicht "Schichtstatus" kannte.)
    fordert_schicht = bool(re.search(
        r"(Schicht\w*|Markierung|Marke)[^.]{0,120}pro Aussage"
        r"|pro Aussage[^.]{0,120}(Schicht\w*|Markierung|Marke)", tex, re.S))
    if fordert_schicht:
        # Wie oft wird tatsaechlich markiert -- ausserhalb der Definitionsliste?
        ohne_defliste = re.sub(r"\\begin\{description\}.*?\\end\{description\}",
                               " ", tex, flags=re.S)
        marken = len(re.findall(SCHICHT_RE, ohne_defliste))
        if marken == 0:
            b.add(doc, "A3", "BEFUND",
                  "fordert Schichtmarkierung pro Aussage, markiert selbst "
                  "keine einzige eigene Aussage (nur Definitionsliste)")
        else:
            b.add(doc, "A3", "OK",
                  "fordert Schichtmarkierung und verwendet sie %dx im Fliesstext"
                  % marken)

    fordert_skript = bool(re.search(
        r"[Pp]r[uü]fskript.{0,120}(jede|jeder)", tex, re.S))
    if fordert_skript:
        rechnerisch = len(re.findall(r"\$.*?=.*?\$", tex))
        if rechnerisch > 3:
            b.add(doc, "A3", "HINWEIS",
                  "fordert Pruefskript je rechnerischer Aussage; Dokument "
                  "enthaelt %d Gleichungen -- Skriptzuordnung pruefen"
                  % rechnerisch)
        else:
            b.add(doc, "A3", "OK",
                  "fordert Pruefskript, enthaelt selbst keine rechnerische "
                  "Aussage (%d Gleichungen)" % rechnerisch)


def a4_begriffsinflation(doc, tex, b):
    txt = klartext(tex).lower()
    woerter = re.findall(r"[a-zaeoeuess\u00e4\u00f6\u00fc\u00df]+", txt)
    n = len(woerter)
    if n < 50:
        return
    auffaellig = False
    for begriff in LEITBEGRIFFE:
        c = sum(1 for w in woerter if begriff.lower() in w)
        anteil = c / n
        if anteil > INFLATIONSSCHWELLE:
            b.add(doc, "A4", "HINWEIS",
                  "'%s' %dx in %d Woertern (%.2f%%) -- Unterscheidungskraft "
                  "pruefen" % (begriff, c, n, 100 * anteil))
            auffaellig = True
    if not auffaellig:
        b.add(doc, "A4", "OK", "keine Begriffsinflation (%d Woerter)" % n)


def a5_anspruchsebene(doc, tex, b):
    """Saetze, die Ableitung behaupten und Setzung beschreiben."""
    saetze = re.split(r"(?<=[.!?])\s+", klartext(tex))
    treffer = 0
    for s in saetze:
        hat_abl = any(re.search(p, s, re.IGNORECASE) for p in ABLEITUNGSVERBEN)
        hat_set = any(re.search(p, s, re.IGNORECASE) for p in SETZUNGSVERBEN)
        if hat_abl and hat_set:
            b.add(doc, "A5", "HINWEIS",
                  "Ableitungs- und Setzungssprache im selben Satz: %s"
                  % s.strip()[:80])
            treffer += 1
    if not treffer:
        b.add(doc, "A5", "OK", "keine vermischte Anspruchsebene")


def a6_residuum(doc, tex, b):
    if any(re.search(p, tex) for p in RESIDUUM_MARKER):
        b.add(doc, "A6", "OK", "Residuum benannt")
    else:
        b.add(doc, "A6", "BEFUND",
              "kein Abschnitt, der benennt was das Dokument offen laesst")


# ------------------------------------------------------------------ Hauptlauf

def main():
    hier = os.path.dirname(os.path.abspath(__file__))
    basis = sys.argv[1] if len(sys.argv) > 1 else os.path.abspath(
        os.path.join(hier, "..", ".."))
    ch_dir = os.path.join(basis, "Sources", "ch")

    dateien = sorted(f for f in os.listdir(ch_dir)
                     if re.match(r"A\d{3}_.*_De_ch\.tex$", f))
    if not dateien:
        print("Keine A-Serien-Dokumente gefunden.")
        return 1

    b = Befund()
    for f in dateien:
        doc = f.split("_")[0]
        with open(os.path.join(ch_dir, f), encoding="utf-8") as fh:
            tex = fh.read()
        a1_entwurfsspuren(doc, tex, b)
        a2_doppelnummern(doc, tex, b)
        a3_selbstausnahme(doc, tex, b)
        a4_begriffsinflation(doc, tex, b)
        a5_anspruchsebene(doc, tex, b)
        a6_residuum(doc, tex, b)

    print("=" * 74)
    print("FFGFT A-Serie -- adversariales Selbst-Audit")
    print("Massstab: derselbe wie bei externen Manuskripten")
    print("=" * 74)

    for schwere in ("BEFUND", "HINWEIS", "OK"):
        teil = [e for e in b.eintraege if e[2] == schwere]
        if not teil:
            continue
        print("\n[%s]  %d" % (schwere, len(teil)))
        for doc, code, _, text in teil:
            print("   %-5s %-3s %s" % (doc, code, text))

    if b.hat_fehler():
        print("\nERGEBNIS: BEFUNDE VORHANDEN -- vor Freigabe beheben")
        return 1
    print("\nERGEBNIS: keine Befunde")
    return 0


if __name__ == "__main__":
    sys.exit(main())
