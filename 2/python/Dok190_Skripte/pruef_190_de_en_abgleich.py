#!/usr/bin/env python3
"""Abgleich Dok. 190 De/En (Registertabelle + offene Brücken).

Aufruf aus der Repo-Wurzel oder von überall:
    python3 2/python/Dok190_Skripte/pruef_190_de_en_abgleich.py
Exit-Code 0 = beide Fassungen synchron, 1 = Abweichungen gefunden.

Geprüft wird je Eintrag:
  1. gleiche Eintragsmenge (K<n> in De entspricht C<n> in En)
  2. gleiche Dokumentnummern in der Verweisspalte
  3. gleiche Statusmarker ([K] [B] [S] [X] [Q] [E] [SETZUNG])
  4. keine Kürzung mit \\ldots am Eintragsende auf nur einer Seite
     (Kurzform mit \\ldots ist gewollt, Ausführung im Archiv — sie muss
     aber in De und En gleich gesetzt sein)
  5. drei Spalten je Zeile, Zeilenende mit \\\\
  6. gleicher Registerstand „Stand R…“ / „as of R…“ = höchste R-Nummer
Das Skript übersetzt nichts und ändert keine Datei.
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]
CH = ROOT / "2" / "Sources" / "ch"
DE = CH / "190_T0_Korrekturen_De_ch.tex"
EN = CH / "190_T0_Korrekturen_En_ch.tex"
ROW = re.compile(r'^([KCPR]\d+[a-z]?)\s*&(.*?)(?=^[KCPR]\d+[a-z]?\s*&|\Z)', re.M | re.S)
MARK = re.compile(r'\[(K|B|S|X|Q|E|SETZUNG)\]')

def load(path):
    s = path.read_text(encoding="utf-8")
    table = s[:s.index("\\end{longtable}")]
    rows = {}
    for m in ROW.finditer(table):
        key = m.group(1)
        if key.startswith("C"):          # En: C<n> == De: K<n>
            key = "K" + key[1:]
        rows.setdefault(key, []).append(m.group(2).strip())
    stand = re.findall(r'(?:Stand|as of)\s+R(\d+)', s)
    return rows, stand

def split_cols(body):
    parts = re.split(r'(?<!\\)&', body)
    return [p.strip() for p in parts]

def docs(col):
    # 006a zählt als eigenes Dokument; 250er/250s (Serie) zählt als 250
    return sorted(set(re.findall(r'\b([A-Z]?\d{3}(?:[a-d](?![A-Za-z]))?)', col)))

def check():
    errs = []
    de, stand_de = load(DE)
    en, stand_en = load(EN)
    for name, rows in (("De", de), ("En", en)):
        for k, v in rows.items():
            if len(v) > 1:
                errs.append(f"{name}: Eintrag {k} kommt {len(v)}-mal vor")
    only_de = sorted(set(de) - set(en), key=lambda x: (x[0], int(re.sub(r'\D', '', x))))
    only_en = sorted(set(en) - set(de), key=lambda x: (x[0], int(re.sub(r'\D', '', x))))
    for k in only_de: errs.append(f"{k}: fehlt in En")
    for k in only_en: errs.append(f"{k}: fehlt in De")
    for k in sorted(set(de) & set(en)):
        d, e = de[k][0], en[k][0]
        cd, ce = split_cols(d), split_cols(e)
        for name, c, raw in (("De", cd, d), ("En", ce, e)):
            if len(c) != 2:
                errs.append(f"{k} ({name}): {len(c)+1} statt 3 Spalten")
            if not raw.rstrip().endswith("\\\\"):
                errs.append(f"{k} ({name}): Zeilenende \\\\ fehlt")
        if len(cd) >= 1 and len(ce) >= 1 and docs(cd[0]) != docs(ce[0]):
            errs.append(f"{k}: Dokumentverweise verschieden — De {docs(cd[0])} / En {docs(ce[0])}")
        md, me = sorted(set(MARK.findall(d))), sorted(set(MARK.findall(e)))
        if md != me:
            errs.append(f"{k}: Statusmarker verschieden — De {md} / En {me}")
        td = bool(re.search(r'\\ldots\s*\\\\\s*$', d)); te = bool(re.search(r'\\ldots\s*\\\\\s*$', e))
        if td != te:
            errs.append(f"{k}: mit \\ldots gekürzt nur in {'De' if td else 'En'}")
    rmax = max(int(k[1:]) for k in set(de) | set(en) if k.startswith("R") and k[1:].isdigit())
    for name, st in (("De", stand_de), ("En", stand_en)):
        if not st:
            errs.append(f"{name}: kein Registerstand im Brückenabschnitt gefunden")
        for n in st:
            if int(n) != rmax:
                errs.append(f"{name}: Stand R{n}, höchster Eintrag ist R{rmax}")
    print(f"Dok. 190 De/En-Abgleich — De {len(de)} / En {len(en)} Einträge, höchster R{rmax}")
    if errs:
        print(f"ABWEICHUNGEN: {len(errs)}")
        for x in errs: print("  -", x)
        return 1
    print("OK — beide Fassungen synchron (0 Abweichungen)")
    return 0

if __name__ == "__main__":
    sys.exit(check())
