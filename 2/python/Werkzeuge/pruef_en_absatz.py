#!/usr/bin/env python3
"""Prüft eine englische LaTeX-Datei Absatz für Absatz auf deutsche Reste.
Aufruf: python3 pruef_en_absatz.py DATEI.tex  -> listet verdächtige Absätze, Exit 0 nur bei 0 Treffern."""
import re, sys
FW = re.compile(r"\b(der|die|das|und|nicht|ist|werden|eine|einer|mit|für|auf|wird|sind|dem|den|des|auch|oder|wenn|durch|zwischen|wir|sich|kein|keine|bei|nach|aus|zur|zum|wie|noch|nur)\b", re.I)
EN = re.compile(r"\b(the|and|of|is|to|in|that|are|with|for|this|which|by|as)\b", re.I)
UML = re.compile(r"[äöüßÄÖÜ]")
def strip(p):
    p = re.sub(r"(?<!\\)%.*", "", p)
    p = re.sub(r"\$[^$]*\$|\\\[.*?\\\]|\\\(.*?\\\)", " ", p, flags=re.S)
    p = re.sub(r"\\(cite|ref|label|eqref|url|href|includegraphics|input)\{[^}]*\}", " ", p)
    p = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?", " ", p)
    p = re.sub(r"[{}\\&]", " ", p)
    return re.sub(r"\s+", " ", p).strip()
t = open(sys.argv[1], encoding="utf-8").read()
hits = 0
for i, para in enumerate(re.split(r"\n\s*\n", t)):
    s = strip(para)
    if not s: continue
    fw, en, um = len(FW.findall(s)), len(EN.findall(s)), len(UML.findall(s))
    words = len(s.split())
    if (fw >= 2 and fw >= en) or (um and words < 8 and fw >= 1) or (fw >= 4):
        hits += 1
        print(f"--- Absatz {i} (de={fw}, en={en}, Umlaute={um}):\n{s[:400]}\n")
    elif um:
        print(f"[Hinweis Umlaut, Absatz {i}] {s[:160]}")
print(f"TREFFER: {hits}")
sys.exit(0 if hits == 0 else 1)
