#!/usr/bin/env python3
"""
pruef_uebertreibungen.py
Durchsucht die deutschen Korpusquellen nach Formulierungen, die als übertrieben gelesen
werden können (Werbesprache, Gewissheitsbehauptungen ohne Status, rhetorische Muster).

Ein Treffer ist KEIN Fehler, sondern eine Stelle zum Nachlesen: "bewiesen" kann mit [B]
belegt sein, "exakt" kann eine exakte Rechnung meinen. Das Skript sortiert nur vor.

Aufruf aus der Repo-Wurzel:  python3 2/python/Korpus_Pruefung/pruef_uebertreibungen.py
Ausgabe: uebertreibungen_treffer.csv (jede Stelle) und uebertreibungen_dokumente.csv
         (Rangliste der Dokumente) im aktuellen Verzeichnis oder in einem als
         erstes Argument angegebenen Verzeichnis.
"""
import csv
import glob
import os
import re
import sys

QUELLEN = sorted(glob.glob("2/Sources/ch/*_De_ch.tex") + glob.glob("2/ipi/*_De_ch.tex")
                 + glob.glob("A_Serie_Export/Sources/ch/*_De_ch.tex"))

# (Kategorie, Gewicht, Muster)  -- Gewicht 3 = fast immer zu streichen, 1 = prüfen
MUSTER = [
    # A: Werbe- und Superlativsprache
    ("A Werbesprache", 3, r"revolution(är|ieren|iert)\w*|Revolution\b"),
    ("A Werbesprache", 3, r"bahnbrechend\w*|Durchbruch\w*|Paradigmenwechsel|Meilenstein\w*"),
    ("A Werbesprache", 3, r"sensationell\w*|spektakulär\w*|atemberaubend\w*|grandios\w*|verblüffend\w*"),
    ("A Werbesprache", 3, r"Weltformel|Theorie von [Aa]llem|Theory of Everything|Nobelpreis\w*"),
    ("A Werbesprache", 2, r"erstaunlich\w*|bemerkenswert\w*|faszinierend\w*|beeindruckend\w*|wunderschön\w*"),
    ("A Werbesprache", 2, r"\belegant\w*|Eleganz|tiefgreifend\w*|einzigartig\w*|völlig neu\w*|radikal\w*"),
    # B: Gewissheit / Vollständigkeit ohne Einschränkung
    ("B Gewissheit", 3, r"zweifelsfrei|unwiderlegbar\w*|unbestreitbar\w*|ohne jeden Zweifel|zweifellos"),
    ("B Gewissheit", 3, r"endgültig\w*|definitiv\w*|ein für alle Mal"),
    ("B Gewissheit", 3, r"(eindeutig|mathematisch|streng|vollständig|rigoros) (bewiesen|belegt|gezeigt)"),
    ("B Gewissheit", 3, r"(vollständig|komplett|restlos|endgültig) (gelöst|erklärt|verstanden|hergeleitet)"),
    ("B Gewissheit", 3, r"löst (das|die|alle) \w*(Rätsel|Problem|Probleme|Frage)"),
    ("B Gewissheit", 3, r"erklärt (alle|sämtliche|jede)\b|alle Naturkonstanten|sämtliche Naturkonstanten"),
    ("B Gewissheit", 2, r"(ohne|keine|null) (einen |jeden )?freie[nr]? Parameter"),
    ("B Gewissheit", 2, r"(perfekte|exakte|vollkommene|vollständige) Übereinstimmung"),
    ("B Gewissheit", 2, r"\b100\s*\\?%|hundertprozentig\w*"),
    ("B Gewissheit", 2, r"\berstmals\b|zum ersten Mal in der Geschichte"),
    ("B Gewissheit", 1, r"\bzwingend\w*|\bnotwendigerweise\b|unausweichlich\w*"),
    # C: Abwertung anderer Rahmen
    ("C Abwertung", 3, r"(widerlegt|überflüssig|obsolet|hinfällig)\w*.{0,60}(Einstein|Standardmodell|Relativitätstheorie|Quantenmechanik|Dunkle[rn]? (Materie|Energie)|Urknall)"),
    ("C Abwertung", 3, r"(Einstein|Standardmodell|Relativitätstheorie|Quantenmechanik|Urknall).{0,60}(widerlegt|überflüssig|obsolet|falsch|hinfällig|ersetzt)"),
    ("C Abwertung", 2, r"Dunkle[rn]? (Materie|Energie).{0,40}(nicht nötig|unnötig|entfällt|existiert nicht)"),
    # D: rhetorische Muster
    ("D Rhetorik", 1, r"nicht (nur|bloß|einfach)\b[^.]{0,80}sondern (auch|vielmehr)?"),
    ("D Rhetorik", 1, r"Dies ist (keine|kein) [^.]{0,60}(sondern|–|---)"),
    ("D Rhetorik", 2, r"[✓✔✗✘🚀✨⚡🎯🔥💡]"),
    ("D Rhetorik", 1, r"(?<=[a-zäöüß\)])!(?=\s|$|\})"),
]
REGEX = [(k, g, re.compile(m, re.IGNORECASE)) for k, g, m in MUSTER]


def textzeilen(pfad):
    """Zeilen ohne Kommentare, Präambel und Literaturverzeichnis."""
    inhalt = open(pfad, encoding="utf-8", errors="replace").read().split("\n")
    im_text, im_bib = not any("\\begin{document}" in z for z in inhalt), False
    for nr, z in enumerate(inhalt, 1):
        if "\\begin{document}" in z:
            im_text = True
            continue
        if re.search(r"\\begin\{thebibliography\}|\\section\*?\{(Literatur|Quellen)", z):
            im_bib = True
        if re.search(r"\\end\{thebibliography\}", z):
            im_bib = False
            continue
        if not im_text or im_bib:
            continue
        z = re.sub(r"(?<!\\)%.*", "", z)
        if z.strip():
            yield nr, z


def main():
    ziel = sys.argv[1] if len(sys.argv) > 1 else "."
    os.makedirs(ziel, exist_ok=True)
    treffer, dok = [], {}
    for pfad in QUELLEN:
        name = os.path.basename(pfad).replace("_De_ch.tex", "")
        zeilen = 0
        score = 0
        kat = {}
        for nr, z in textzeilen(pfad):
            zeilen += 1
            for k, g, rx in REGEX:
                for m in rx.finditer(z):
                    if k == "D Rhetorik" and m.group(0) == "!" and "$" in z:
                        continue
                    kontext = z.strip()[:220]
                    treffer.append((name, nr, k, g, m.group(0).strip(), kontext))
                    score += g
                    kat[k] = kat.get(k, 0) + 1
        dok[name] = (score, zeilen, kat)
    with open(os.path.join(ziel, "uebertreibungen_treffer.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["Dokument", "Zeile", "Kategorie", "Gewicht", "Fund", "Kontext"])
        w.writerows(sorted(treffer, key=lambda t: (t[0], t[1])))
    rang = sorted(dok.items(), key=lambda kv: -kv[1][0])
    with open(os.path.join(ziel, "uebertreibungen_dokumente.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["Dokument", "Punkte", "Punkte je 100 Zeilen", "Zeilen",
                    "A Werbesprache", "B Gewissheit", "C Abwertung", "D Rhetorik"])
        for name, (s, n, kat) in rang:
            w.writerow([name, s, round(100 * s / max(n, 1), 2), n] +
                       [kat.get(k, 0) for k in ("A Werbesprache", "B Gewissheit", "C Abwertung", "D Rhetorik")])
    print(f"{len(QUELLEN)} Dokumente, {len(treffer)} Treffer")
    print(f"{'Dokument':<55} {'Punkte':>6} {'/100Z':>6}")
    for name, (s, n, kat) in rang[:40]:
        print(f"{name[:55]:<55} {s:>6} {100*s/max(n,1):>6.1f}")


if __name__ == "__main__":
    main()
