#!/usr/bin/env python3
"""Korpusweite Prüfung der Statusmarker (FFGFT).

Verbindliche Legende: 2/Sources/ch/000_Statusmarker_Legende_{De,En}_ch.tex

Geprüft wird in allen Kapiteldateien 2/Sources/ch/*_{De,En}_ch.tex:
  A  Marker außerhalb der erlaubten Liste (\\textbf{[..]}, $[..]$, Makros)
  B  Legendenzeilen, deren Bedeutung von der verbindlichen Legende abweicht
  C  Dokumente mit Markern, aber ohne Legende (weder eigene Zeilen noch \\input)
  D  Kernaussagen, die in verschiedenen Dokumenten verschiedene Marker tragen

Aufruf aus der Repo-Wurzel:
  python3 2/python/Korpus_Pruefung/pruef_statusmarker.py [--detail] [--csv DATEI]
Ausgabe: Zusammenfassung je Prüfteil; --detail listet jeden Treffer.
Das Skript ändert keine Dateien.
"""
import argparse
import collections
import csv
import glob
import os
import re
import sys

ERLAUBT = ["K", "B", "S", "SETZUNG", "Q", "E", "X", "L"]
LEGENDE_INPUT = "000_Statusmarker_Legende"

# Gleitumgebungs-Optionen und Einheiten, die wie Marker aussehen, aber keine sind
KEINE_MARKER = {"H", "T", "L", "M", "G", "F", "I", "P", "h", "t", "b", "p",
                "MeV", "GeV", "eV", "keV", "TeV", "PDF", "Online", "AT"}

# Bedeutungsprüfung je Marker: (Pflichtbegriffe – jeder Eintrag ist eine
# Alternativen-Gruppe, alle Gruppen müssen vorkommen; verbotene Begriffe)
REGELN = {
    "De": {
        "K": ([("hergeleit", "abgeleit", "ableitbar", "herleitbar", "aus $\\xi", "aus \\xi", "ξ"),
               ("prüfskript", "numerisch", "skript")], ()),
        "B": ([("bewiesen", "beweis"),], ()),
        "S": ([("skizz", "plausib"),], ("spekul",)),
        "SETZUNG": ([("setzung", "axiom", "gesetzt"),], ()),
        "Q": ([("literatur", "quelle", "extern"),], ("fraglich",)),
        "E": ([("etabliert",),], ()),
        "X": ([("widerleg", "ausgeschlossen", "nicht tragfähig"),], ()),
        "L": ([("lean",), ("bewiesen", "beweis")], ()),
    },
    "En": {
        "K": ([("derived", "derivable", "from $\\xi", "from \\xi", "ξ"),
               ("check script", "numeric", "script")], ()),
        "B": ([("proved", "proven", "proof"),], ()),
        "S": ([("sketch", "plausib"),], ("speculat",)),
        "SETZUNG": ([("postulate", "axiom", "setzung", "posited", "set by"),], ()),
        "Q": ([("literature", "source", "external"),], ("questionable",)),
        "E": ([("established",),], ()),
        "X": ([("refuted", "excluded", "not viable", "ruled out"),], ()),
        "L": ([("lean",), ("proved", "proof")], ()),
    },
}

# Kernaussagen: (Name, Muster, die alle in derselben Zeile stehen müssen)
KERNAUSSAGEN = [
    ("Confinement als Trialitäts-Selektion", [r"[Cc]onfinement", r"T_\{?R\}?\s*=\s*0|Trialit|[Tt]riality"]),
    ("SU(3)_c algebraisch aus Z3", [r"SU\(3\)_\{?c", r"Gell|algebra"]),
    ("Weinberg on-shell 2/9", [r"2/9|\\frac\{2\}\{9\}", r"Weinberg|M_W|\\theta_W|on-shell"]),
    ("Higgs 11/8", [r"11/8|\\frac\{11\}\{8\}", r"Higgs|m_h|M_H"]),
    ("Spurregel M_W²+M_Z²+m_h²=v²/2", [r"Spurregel|[Tt]race rule"]),
    ("Koide-Amplitude d/c = sqrt2", [r"d/c|\\frac\{d\}\{c\}", r"\\sqrt\{?2"]),
    ("Koide-Phase theta = 2/9", [r"\\theta|θ", r"2/9|\\frac\{2\}\{9\}", r"Koide|p_0"]),
    ("K_eff = 2 pi xi", [r"K_\{?\\?(?:text\{)?eff", r"2\\pi\s*\\xi|2π\s*ξ"]),
    ("xi = 4/30000", [r"\\xi\s*=\s*4/30000|\\xi\s*=\s*\\frac\{4\}\{30000\}|ξ\s*=\s*4/30000"]),
]
# Zulässige Kombinationen und Ausschlüsse je Kernaussage:
# xi: Form [K], Größenordnung [SETZUNG] (P33) – beides gehört zusammen;
# Zeilen über Faktorisierung betreffen eine andere Aussage (Dok. 075).
ZULAESSIG = {"xi = 4/30000": {"K", "SETZUNG"}}
AUSSCHLUSS = {"xi = 4/30000": r"[Ff]aktoris|[Ff]actori"}

MARKER_RE = re.compile(r"\[(K|B|S|SETZUNG|Q|E|X|L)\]")
FETT_RE = re.compile(r"\\textbf\{\[([^\]\n]{1,25})\]\}|\$\[([^\]\n$]{1,25})\]\$")
MAKRO_RE = re.compile(r"\\(?:provide|new|renew)command\{?\\(\w+)\}?(?:\[\d\])?\{[^{}]*?\[([^\]\n]{1,25})\]")
# Legendenzeile: Zeile beginnt mit dem Marker (ggf. nach \\item), danach Definition
LEGENDZEILE_RE = re.compile(
    r"^\s*(?:\\item\s*)?(?:\$)?\\textbf\{\[(K|B|S|SETZUNG|Q|E|X|L)\]\}\$?\s*(?:&|=|:|—|--|\\quad)\s*(.{4,160})")


def dokname(pfad):
    return os.path.basename(pfad).replace("_ch.tex", "")


def ohne_kommentar(zeile):
    return re.sub(r"(?<!\\)%.*", "", zeile)


def pruefe(sprache, detail):
    dateien = sorted(glob.glob(f"2/Sources/ch/*_{sprache}_ch.tex"))
    # Register Dok. 190 hat ein eigenes Prüfskript (pruef_190_de_en_abgleich.py)
    dateien = [d for d in dateien if LEGENDE_INPUT not in d
               and not os.path.basename(d).startswith("190_")]
    A, B, C = [], [], []
    D = collections.defaultdict(lambda: collections.defaultdict(set))
    for pfad in dateien:
        doc = dokname(pfad)
        text = open(pfad, encoding="utf-8", errors="ignore").read()
        zeilen = [ohne_kommentar(z) for z in text.splitlines()]
        rein = "\n".join(zeilen)
        # als Statusmarker benutzt: fett gesetzt oder über ein Marker-Makro
        # (nicht $[E]$ o. ä. als Dimensionsklammer)
        benutzt = set(re.findall(r"\\textbf\{[^{}]*\[(K|B|S|SETZUNG|Q|E|X|L)\]", rein)) | \
            set(re.findall(r"command\{?\\\w+\}?\{\\textbf\{\[(K|B|S|SETZUNG|Q|E|X|L)\]", rein))
        # A: unbekannte Marker
        for nr, z in enumerate(zeilen, 1):
            for m in FETT_RE.finditer(z):
                tok = (m.group(1) or m.group(2)).strip()
                if m.group(2) and "," in tok:   # Kommutator $[A, B]$
                    continue
                for teil in re.split(r"[/,]\s*", tok):
                    if re.fullmatch(r"K\|P\d+", tok):
                        break
                    if teil and teil not in ERLAUBT and teil not in KEINE_MARKER \
                            and re.fullmatch(r"[A-ZÄÖÜ][A-Za-zÄÖÜäöü\-]{0,20}", teil):
                        A.append((doc, nr, tok, z.strip()[:110]))
                        break
        for m in MAKRO_RE.finditer(rein):
            tok = m.group(2).strip()
            if tok not in ERLAUBT:
                A.append((doc, 0, tok, f"Makro \\{m.group(1)}"))
        # B: abweichende Legendenzeilen
        hat_legende = LEGENDE_INPUT in text
        for nr, z in enumerate(zeilen, 1):
            m = LEGENDZEILE_RE.match(z)
            if not m:
                continue
            mk, bed = m.group(1), m.group(2).lower()
            pflicht, verboten = REGELN[sprache][mk]
            hat_legende = True
            fehlt = [g[0] for g in pflicht if not any(w in bed for w in g)]
            falsch = [w for w in verboten if w in bed]
            if fehlt or falsch:
                B.append((doc, nr, mk, ("fehlt: " + ",".join(fehlt) if fehlt else "")
                          + (" verboten: " + ",".join(falsch) if falsch else ""), z.strip()[:110]))
        # B': eigene Legendensätze im Fließtext (statt der verbindlichen Legende)
        for nr, z in enumerate(zeilen, 1):
            if re.search(r"(Aussagen mit|Statements marked)\s*\\textbf\{\[", z):
                B.append((doc, nr, "-", "eigener Legendensatz", z.strip()[:110]))
        # C: Marker ohne Legende
        if benutzt and not hat_legende:
            C.append((doc, ",".join(sorted(benutzt))))
        # D: Kernaussagen (ohne Register Dok. 190: dort stehen Statuswechsel
        # mehrerer Aussagen in einer Zeile)
        for name, muster in ([] if doc.startswith("190_") else KERNAUSSAGEN):
            for nr, z in enumerate(zeilen, 1):
                if all(re.search(p, z) for p in muster) and not (
                        name in AUSSCHLUSS and re.search(AUSSCHLUSS[name], z)):
                    for mk in MARKER_RE.findall(z):
                        D[name][mk].add(f"{doc}:{nr}")
    # Konflikt nur, wenn verschiedene Dokumente verschiedene Marker setzen
    D_konflikt = {}
    for n, v in D.items():
        docs_je_mk = {mk: {o.rsplit(":", 1)[0] for o in orte} for mk, orte in v.items()}
        if set(v) <= ZULAESSIG.get(n, set()):
            continue
        if len(v) > 1 and len(set().union(*docs_je_mk.values())) > 1:
            D_konflikt[n] = v
    return dateien, A, B, C, D_konflikt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--detail", action="store_true")
    ap.add_argument("--csv")
    args = ap.parse_args()
    if not os.path.isdir("2/Sources/ch"):
        sys.exit("Aus der Repo-Wurzel aufrufen.")
    gesamt = 0
    zeilen_csv = []
    for sp in ("De", "En"):
        dateien, A, B, C, D = pruefe(sp, args.detail)
        print(f"=== {sp}: {len(dateien)} Kapiteldateien")
        print(f"  A  nicht erlaubte Marker:        {len(A):4d} Treffer in {len({a[0] for a in A})} Dokumenten")
        print(f"  B  abweichende Legendenzeilen:   {len(B):4d} Treffer in {len({b[0] for b in B})} Dokumenten")
        print(f"  C  Marker ohne Legende:          {len(C):4d} Dokumente")
        print(f"  D  Kernaussagen mit >1 Marker:   {len(D):4d} von {len(KERNAUSSAGEN)}")
        gesamt += len(A) + len(B) + len(C) + len(D)
        if args.detail:
            for a in A:
                print(f"    A {a[0]}:{a[1]}  [{a[2]}]  {a[3]}")
            for b in B:
                print(f"    B {b[0]}:{b[1]}  [{b[2]}] {b[3]} | {b[4]}")
            for c in C:
                print(f"    C {c[0]}  benutzt {c[1]}")
        for name, v in D.items():
            print(f"    D {name}:")
            for mk, orte in sorted(v.items()):
                liste = sorted(orte)
                print(f"        [{mk}] {len(liste):3d}×  {', '.join(liste[:8])}{' …' if len(liste) > 8 else ''}")
        for a in A:
            zeilen_csv.append([sp, "A", a[0], a[1], a[2], a[3]])
        for b in B:
            zeilen_csv.append([sp, "B", b[0], b[1], b[2], b[3] + " | " + b[4]])
        for c in C:
            zeilen_csv.append([sp, "C", c[0], "", c[1], ""])
        for name, v in D.items():
            for mk, orte in v.items():
                for o in orte:
                    zeilen_csv.append([sp, "D", o.split(":")[0], o.split(":")[1], mk, name])
    if args.csv:
        with open(args.csv, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f, delimiter=";")
            w.writerow(["Sprache", "Teil", "Dokument", "Zeile", "Marker", "Text"])
            w.writerows(zeilen_csv)
    print(f"\nGesamt: {gesamt} Befunde (0 = korpusweit einheitlich)")
    return 0 if gesamt == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
