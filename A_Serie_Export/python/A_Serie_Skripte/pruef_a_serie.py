#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pruef_a_serie.py -- Strukturpruefung der FFGFT A-Serie

Prueft fuer jedes A-Dokument:
  1. Dateipaar vorhanden (ch/ + wr_standalone_A4/) und korrekt verdrahtet
  2. Nummernschema AxxX, Zehnerschritt, keine Doppelvergabe
  3. Pflichtabschnitte vorhanden (Disclaimer, Ersetzt)
  4. Kosmologie-Ausschluss eingehalten (Sperrliste)
  5. Prognose-Disziplin: nur die deklarierten Grundprognosen
  6. Schichtmarkierung [K]/[B]/[S]/[SETZUNG] wird verwendet

Aufruf:  python3 pruef_a_serie.py [SOURCES_DIR]
         Default SOURCES_DIR = ../..  (relativ zum Skriptordner)

Exit 0 = alles gruen, Exit 1 = mindestens ein FEHLER.
Reine Standardbibliothek, keine Abhaengigkeiten.
"""

import os
import re
import sys

# ---------------------------------------------------------------- Konfiguration

# Kosmologie-Sperrliste. Stehende Vorgabe: die A-Serie enthaelt keinen
# kosmologischen Sektor. Treffer sind FEHLER, nicht Warnungen.
KOSMOLOGIE_SPERRE = [
    r"\bH_?0\b", r"\bHubble", r"\bR_?H\b", r"Rotverschiebung", r"\bCMB\b",
    r"Urknall", r"Dunkle[rn]? (Materie|Energie)", r"Dunkelsektor",
    r"kosmologisch", r"Kosmologie", r"LambdaCDM", r"\\LCDM",
    r"Expansion des Universums", r"Hubble-Spannung", r"Sandage",
]

# Erlaubte Ausnahmen: eine Sperr-Nennung ist zulaessig, wenn sie in derselben
# Zeile ausdruecklich als ausgeschlossen markiert ist.
AUSNAHME_MARKER = [
    "nicht Teil der A-Serie", "ausserhalb der A-Serie", "außerhalb der A-Serie",
    "kein kosmologischer Sektor", "ausgeschlossen", "Ausschluss",
    "Ausschlusses", "nicht uebernommen", "nicht übernommen",
    "AUSNAHME_KOSMOLOGIE", "Kosmologie-Sektor", "kosmologischen Sektor",
    "diesen Sektor nicht", "enthaelt diesen Sektor nicht",
]

# Prognose-Disziplin: nur diese Groessen duerfen als Vorhersage auftreten.
GRUNDPROGNOSEN = [
    "m_tau", "m_\\tau", "\\tau", "Tau-Masse", "Tauonmasse",
    "Leptonmasse", "Massenverh", "Koide", "Massenverhaeltnis",
    "CHSH", "D_f", "\\Dfrak", "L_0", "\\Lzero",
]
# Verneinungen: Saetze, die eine Prognose ausdruecklich ABLEHNEN, duerfen die
# Triggerwoerter enthalten. (Eingefuehrt 20.07.2026 nach drei Fehlalarmen in
# A060/A090, wo genau das der Fall war.)
PROGNOSE_NEGATION = [
    "keine Vorhersage", "keine Prognose", "nicht als Prognose",
    "nicht als Vorhersage", "Prognosegrößen", "Prognosegroessen",
    "keine Prognosen", "Strukturaussage, keine",
]

PROGNOSE_TRIGGER = [
    r"sagt\s+\S+\s+vorher", r"Vorhersage", r"prognostizier", r"\bPrognose",
]

PFLICHT_ABSCHNITTE = {
    "Ersetzt": r"\\section\{Ersetzt\}",
}

# Disclaimer muss in jedem A-Dokument stehen (Kapitelfassung).
DISCLAIMER_MARKER = r"\\section\{Verwendung von KI-Werkzeugen\}"

SCHICHT_MARKER = [r"\[K\]", r"\[B\]", r"\[S\]", r"\[SETZUNG\]"]

# ---------------------------------------------------------------- Hilfsfunktionen

class Befund:
    def __init__(self):
        self.fehler = []
        self.warnungen = []
        self.ok = []

    def f(self, doc, text):
        self.fehler.append((doc, text))

    def w(self, doc, text):
        self.warnungen.append((doc, text))

    def o(self, doc, text):
        self.ok.append((doc, text))


# Abschnitte, in denen die Sperrbegriffe erlaubt sind, weil dort gerade der
# Ausschluss erklaert wird.
FREIZONE_ABSCHNITTE = [
    "Was nicht Teil der A-Serie ist",
    "Verwendung von KI-Werkzeugen",
]


def in_freizone(text):
    """Menge der Zeilennummern, die in einem Freizonen-Abschnitt liegen."""
    frei = set()
    aktiv = False
    for i, z in enumerate(text.splitlines(), 1):
        m = re.match(r"\\section\{(.+?)\}", z.strip())
        if m:
            aktiv = any(f in m.group(1) for f in FREIZONE_ABSCHNITTE)
        if aktiv:
            frei.add(i)
    return frei


def zeilen_ohne_kommentar(text):
    """LaTeX-Kommentare entfernen, Zeilennummern erhalten."""
    out = []
    for i, z in enumerate(text.splitlines(), 1):
        z2 = re.sub(r"(?<!\\)%.*$", "", z)
        out.append((i, z2))
    return out


def absatz_index(text):
    """Ordnet jeder Zeilennummer den Text ihres Absatzes zu."""
    zeilen = text.splitlines()
    zuordnung = {}
    start = 0
    for i, z in enumerate(zeilen):
        if z.strip() == "":
            absatz = " ".join(zeilen[start:i])
            for nr in range(start + 1, i + 1):
                zuordnung[nr] = absatz
            start = i + 1
    absatz = " ".join(zeilen[start:])
    for nr in range(start + 1, len(zeilen) + 1):
        zuordnung[nr] = absatz
    return zuordnung


def abschnitt_index(text):
    """Ordnet jeder Zeilennummer den Volltext ihres \\section-Abschnitts zu."""
    zeilen = text.splitlines()
    grenzen = [i for i, z in enumerate(zeilen)
               if re.match(r"\\section\{", z.strip())] + [len(zeilen)]
    zuordnung = {}
    if not grenzen[:-1]:
        ganz = " ".join(zeilen)
        return {n: ganz for n in range(1, len(zeilen) + 1)}
    for a, b_ in zip(grenzen[:-1], grenzen[1:]):
        block = " ".join(zeilen[a:b_])
        for nr in range(a + 1, b_ + 1):
            zuordnung[nr] = block
    return zuordnung


def pruefe_kosmologie(doc, text, b):
    # Explizite Kosmologie-Dokumente: Sperre nicht anwenden
    KOSMOLOGIE_DOCS = ["A265"]
    if any(doc.startswith(kd) for kd in KOSMOLOGIE_DOCS):
        return 0
    treffer = 0
    frei = in_freizone(text)
    absaetze = absatz_index(text)
    for nr, z in zeilen_ohne_kommentar(text):
        if nr in frei:
            continue
        # Absatz-Ausnahme: die Sperrbegriffe duerfen genannt werden, wo
        # ueber den Ausschluss selbst gesprochen wird.
        kontext = absaetze.get(nr, "") + " " + z
        if any(m.lower() in kontext.lower() for m in AUSNAHME_MARKER):
            continue
        for pat in KOSMOLOGIE_SPERRE:
            if re.search(pat, z, re.IGNORECASE):
                b.f(doc, "Zeile %d: Kosmologie-Sperre '%s' -> %s"
                    % (nr, pat, z.strip()[:70]))
                treffer += 1
                break
    if treffer == 0:
        b.o(doc, "Kosmologie-Ausschluss eingehalten")



def pruefe_selbsttragend(doc, text, b):
    """Original-Dokumente (Dok.~NNN) und Registereintraege (P/R/K nnn) duerfen im
    JUSTIFIZIERENDEN Fliesstext nicht als Kruecke stehen -- die Begruendung muss
    ausgeschrieben im Dokument stehen. Sie gehoeren in den Ersetzt-Absatz.
    Interne A-Verweise (A020 etc.) sind erlaubt.

    Ausnahmen: A250 (Verweistabelle) und A230 (Sammel-/Registerdokument) haben die
    Zuordnung zu den Originalen als ihren eigentlichen Inhalt.
    """
    import re as _re
    if doc.startswith(("A250", "A230")):
        b.o(doc, "referenzielles Dokument -- Verweise sind hier Inhalt")
        return
    idx = text.find("\\section{Ersetzt}")
    body = text if idx < 0 else text[:idx]
    pats = [r"Dok\.~\d+", r"\bP4\d\b", r"\bR5\d\b", r"\bK[1-6]\b",
            r"Register bucht"]
    treffer = []
    for nr, z in zeilen_ohne_kommentar(body):
        if any(_re.search(pat, z) for pat in pats):
            treffer.append(nr)
    if treffer:
        b.f(doc, "Original-/Registerverweis im Fliesstext (nur in Ersetzt "
                 "erlaubt): Zeilen %s" % ", ".join(map(str, treffer[:8])))
    else:
        b.o(doc, "selbsttragend (keine externen Verweise im Fliesstext)")

def pruefe_prognosen(doc, text, b):
    # A210 IST das Falsifikations-/Prognosedokument der Serie: es fuehrt die
    # Liste der vier Prognosegroessen und den Abschnitt "Was KEINE Pruefgroesse
    # ist". Hier ist "Prognose" durchgehend legitimer Gegenstand, kein
    # unbelegter Anspruch. Ausnahme wie fuer die Kosmologie-Erklaerzone.
    if doc.startswith("A210"):
        return
    # ABSATZ-KORREKTUR (20.07.2026): zeilenweise Pruefung erzeugte vier
    # Fehlalarme in A110, wo "Vorhersage" und die Grundgroesse m_tau in
    # verschiedenen Zeilen desselben Absatzes standen. Der Kontext ist der
    # Absatz, nicht die Zeile.
    # ABSCHNITTS-KORREKTUR: der Bezug einer Prognoseaussage ist der ABSCHNITT.
    # Ein Schlusssatz wie "Das ist eine Vorhersage, keine Retrodiktion" nennt
    # die Groesse nicht noch einmal -- sie steht weiter oben im selben
    # Abschnitt. Absatzweite Pruefung liess hier zwei Fehlalarme stehen.
    frei = in_freizone(text)
    abschnitte = abschnitt_index(text)
    for nr, z in zeilen_ohne_kommentar(text):
        if nr in frei:
            continue
        z = abschnitte.get(nr, "") + " " + z
        if any(n.lower() in z.lower() for n in PROGNOSE_NEGATION):
            continue
        if any(re.search(t, z, re.IGNORECASE) for t in PROGNOSE_TRIGGER):
            if not any(g.lower() in z.lower() for g in GRUNDPROGNOSEN):
                b.w(doc, "Zeile %d: Prognose ohne Grundgroesse -> %s"
                    % (nr, z.strip()[:70]))


def pruefe_pflicht(doc, text, b):
    if not re.search(DISCLAIMER_MARKER, text):
        b.f(doc, "KI-Disclaimer fehlt (Abschnitt 'Verwendung von KI-Werkzeugen')")
    else:
        b.o(doc, "KI-Disclaimer vorhanden")
    for name, pat in PFLICHT_ABSCHNITTE.items():
        if not re.search(pat, text):
            b.f(doc, "Pflichtabschnitt fehlt: %s" % name)
        else:
            b.o(doc, "Pflichtabschnitt vorhanden: %s" % name)


def pruefe_schichten(doc, text, b):
    gefunden = [m for m in SCHICHT_MARKER if re.search(m, text)]
    if not gefunden:
        b.w(doc, "keine Schichtmarkierung [K]/[B]/[S]/[SETZUNG] verwendet")
    else:
        b.o(doc, "Schichtmarkierung verwendet (%d Arten)" % len(gefunden))


def pruefe_wrapper(doc, ch_pfad, wr_pfad, b):
    if not os.path.exists(wr_pfad):
        b.f(doc, "Wrapper fehlt: %s" % os.path.basename(wr_pfad))
        return
    with open(wr_pfad, encoding="utf-8") as fh:
        wr = fh.read()
    ch_name = os.path.basename(ch_pfad).replace(".tex", "")
    if ch_name not in wr:
        b.f(doc, "Wrapper zeigt nicht auf %s" % ch_name)
    else:
        b.o(doc, "Wrapper korrekt verdrahtet")


def pruefe_nummern(docs, b):
    nummern = []
    for d in docs:
        m = re.match(r"A(\d{3})", d)
        if not m:
            b.f(d, "Name folgt nicht dem Schema Axxx")
            continue
        nummern.append(int(m.group(1)))
    for n in nummern:
        if n % 10 != 0:
            b.w("A%03d" % n, "keine Zehnernummer (Einschub) -- zulaessig, "
                             "aber Gliederung pruefen")
    dubletten = {n for n in nummern if nummern.count(n) > 1}
    for n in sorted(dubletten):
        b.f("A%03d" % n, "Nummer doppelt vergeben")
    if nummern and not dubletten:
        b.o("(Serie)", "%d Dokumente, Nummern eindeutig: %s"
            % (len(nummern), ", ".join("A%03d" % n for n in sorted(nummern))))


# ---------------------------------------------------------------- Hauptlauf

def main():
    hier = os.path.dirname(os.path.abspath(__file__))
    basis = sys.argv[1] if len(sys.argv) > 1 else os.path.abspath(
        os.path.join(hier, "..", ".."))
    ch_dir = os.path.join(basis, "Sources", "ch")
    wr_dir = os.path.join(basis, "Sources", "wr_standalone_A4")

    if not os.path.isdir(ch_dir):
        print("FEHLER: ch-Verzeichnis nicht gefunden: %s" % ch_dir)
        return 1

    dateien = sorted(f for f in os.listdir(ch_dir)
                     if re.match(r"A\d{3}_.*_De_ch\.tex$", f))
    if not dateien:
        print("Keine A-Serien-Dokumente gefunden in %s" % ch_dir)
        return 1

    b = Befund()
    docs = []

    for f in dateien:
        doc = f.split("_")[0]
        docs.append(doc)
        ch_pfad = os.path.join(ch_dir, f)
        wr_pfad = os.path.join(wr_dir, f.replace("_ch.tex", ".tex"))
        with open(ch_pfad, encoding="utf-8") as fh:
            text = fh.read()

        pruefe_pflicht(doc, text, b)
        pruefe_kosmologie(doc, text, b)
        pruefe_prognosen(doc, text, b)
        pruefe_selbsttragend(doc, text, b)
        pruefe_schichten(doc, text, b)
        pruefe_wrapper(doc, ch_pfad, wr_pfad, b)

    pruefe_nummern(docs, b)

    # ------------------------------------------------------------ Ausgabe
    print("=" * 72)
    print("FFGFT A-Serie -- Strukturpruefung")
    print("Basis: %s" % basis)
    print("=" * 72)

    print("\n[OK]  %d bestandene Pruefungen" % len(b.ok))
    for doc, t in b.ok:
        print("      %-6s %s" % (doc, t))

    if b.warnungen:
        print("\n[WARNUNG]  %d" % len(b.warnungen))
        for doc, t in b.warnungen:
            print("      %-6s %s" % (doc, t))

    if b.fehler:
        print("\n[FEHLER]  %d" % len(b.fehler))
        for doc, t in b.fehler:
            print("      %-6s %s" % (doc, t))
        print("\nERGEBNIS: NICHT BESTANDEN")
        return 1

    print("\nERGEBNIS: BESTANDEN (%d Warnungen)" % len(b.warnungen))
    return 0


if __name__ == "__main__":
    sys.exit(main())
