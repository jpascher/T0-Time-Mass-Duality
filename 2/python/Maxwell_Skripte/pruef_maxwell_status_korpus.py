#!/usr/bin/env python3
"""Prüfskript: Status der Maxwell-Dynamik im FFGFT-Korpus.
Behauptung (extern): 'Dok. 201 und 307 skizzieren die Herleitung des vollen
dynamischen Maxwell-Systems, Status [S]'. Geprüft wird gegen die Kapiteldateien.
Aufruf aus Repo-Wurzel: python3 2/python/Maxwell_Skripte/pruef_maxwell_status_korpus.py
"""
import re, glob, os, sys
root = os.path.join(os.path.dirname(__file__), "..", "..", "Sources", "ch")
def rd(p): return open(p, encoding="utf-8", errors="replace").read()
ok = 0; n = 0
def chk(cond, msg):
    global ok, n; n += 1; ok += bool(cond); print(("OK  " if cond else "FAIL"), msg)

d201 = rd(glob.glob(f"{root}/201_*_De_ch.tex")[0])
d307 = rd(glob.glob(f"{root}/307_*_De_ch.tex")[0])
d180 = rd(glob.glob(f"{root}/180_*_De_ch.tex")[0])
d190 = rd(f"{root}/190_T0_Korrekturen_De_ch.tex")
mx = re.compile(r"maxwell|elektrodynam|faraday|amp[eè]re", re.I)
FF = re.compile(r"F_\{\\mu\\nu\}\s*F\^\{\\mu\\nu\}")

chk(not mx.search(d201), "Dok. 201 nennt Maxwell/Elektrodynamik nirgends")
chk(not mx.search(d307), "Dok. 307 nennt Maxwell/Elektrodynamik nirgends")
chk(FF.search(d201), "Dok. 201 übernimmt -1/4 F_munu F^munu als Term des erweiterten Lagrangians (Eingang, keine Herleitung)")
chk(not FF.search(d307), "Dok. 307 enthält keinen Feldstärketerm; nur KK-Ladungsquantisierung Q∝n/R_T")
chk("Standardmodell-Lagrangian" in d180 and FF.search(d180), "Dok. 180 setzt den SM-Lagrangian inkl. F^2 explizit als Ausgangspunkt")
chk(not re.search(r"\[(S|B|K)\]", d201), "Dok. 201 trägt keine Statusmarker (Vorläufer der Markerpraxis)")
chk(not mx.search(d190), "Dok. 190 (Register + offene Brücken) führt keine Maxwell-Brücke, weder [S] noch geschlossen")
# Korpusweit: gibt es irgendeine Eigenaussage 'Maxwell hergeleitet'?
claims = []
for f in glob.glob(f"{root}/*_De_ch.tex"):
    for ln in rd(f).splitlines():
        if re.search(r"maxwell.{0,40}(gleichung|system)|(gleichung|system).{0,40}maxwell", ln, re.I) \
           and re.search(r"herleit|abgeleit|emergier|folgt aus", ln, re.I):
            claims.append(os.path.basename(f))
chk(not claims, f"keine Eigenaussage 'Maxwell-Gleichungen hergeleitet' im Korpus (Treffer: {claims})")
print(f"\n{ok}/{n}")
sys.exit(0 if ok == n else 1)
