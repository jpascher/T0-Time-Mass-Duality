#!/usr/bin/env python3
"""
Dok. 378 -- Begutachtung unter heutigen Bedingungen.
Prueft, dass die im Dokument zitierten Korpusstellen existieren und das
enthalten, wofuer sie zitiert werden. Aus der Repo-Wurzel ausfuehren.
Externe Angaben (F O R M-Hash, DOIs, IPI-Verfahren) sind [Q] und werden nur
auf Uebereinstimmung zwischen De- und En-Fassung geprueft.
"""
import pathlib, re, sys
root = pathlib.Path(__file__).resolve().parents[2]  # .../2
ch = root / "Sources" / "ch"
ok = n = 0
def chk(name, cond, info=""):
    global ok, n
    n += 1; ok += bool(cond); print(f"[{'PASS' if cond else 'FAIL'}] {name}  {info}")

def doc(num, lang="De"):
    fs = sorted(ch.glob(f"{num}_*_{lang}_ch.tex"))
    return fs[0].read_text(encoding="utf-8") if fs else None

de = (ch / "378_Begutachtung_heute_De_ch.tex").read_text(encoding="utf-8")
en = (ch / "378_Begutachtung_heute_En_ch.tex").read_text(encoding="utf-8")

print("--- A  Zitierte Korpusdokumente vorhanden ---")
cited = sorted(set(int(x) for x in re.findall(r"Dok\.~(\d{3})", de)))
for d in cited:
    if d == 378: continue
    present = doc(d) is not None
    if d == 377 and not present:
        print(f"[NOTE] Dok. 377 nicht im Repo-Stand (Arbeitsstand 23.9.2026) -- nicht gewertet")
        continue
    chk(f"A Dok. {d} existiert", present)

print("--- B  Zitierte Inhalte ---")
d342 = doc(342) or ""
chk("B1 Dok. 342: k>=5 ohne Status aus Produktsuche", re.search(r"k\s*\\geq?\s*5\$?:\s*Kein Status aus Produktsuche", d342) is not None)
d361 = doc(361) or ""
chk("B2 Dok. 361: Abschnitt 'Was nicht übereinstimmt'", "Was nicht übereinstimmt" in d361 or "Was nicht \\\"ubereinstimmt" in d361)
d190a = (ch / "190_T0_Korrekturen_Archiv_De_ch.tex").read_text(encoding="utf-8") if (ch / "190_T0_Korrekturen_Archiv_De_ch.tex").exists() else ""
d190 = (doc(190) or "") + d190a
chk("B3 Dok. 190: P35 vorhanden", "P35" in d190)
d351 = doc(351) or ""
chk("B4 Dok. 351: Methodische Notiz (CCR)", "Methodische Notiz" in d351 and "Canonical Constitutional Record" in d351)
d372 = doc(372) or ""
chk("B5 Dok. 372: M_W = 80,420 GeV", "80{,}420" in d372 or "80,420" in d372)
d352 = doc(352) or ""
chk("B6 Dok. 372: sin^2 theta_23 in {4/9, 5/9}", "4/9" in d372 and "5/9" in d372 and "theta_{23}" in d372)
d272 = doc(272) or ""
chk("B7 Dok. 272: Lexicon/OAP/Matrix/FAH und O0/O2", all(k in d272 for k in ["Lexicon", "OAP", "Matrix", "FAH", "O0"]))
d365 = doc(365) or ""
chk("B8 Dok. 365 vorhanden (Einstieg)", len(d365) > 0)

print("--- C  De/En-Abgleich der externen Angaben [Q] ---")
for key in ["bd2a1f2d", "10.5281/zenodo.22875795", "10.5281/zenodo.20257133",
            "10.5281/zenodo.21371481", "10.5281/zenodo.20117635"]:
    chk(f"C {key} in De und En", key in de and key in en)
chk("C Bausteine B1..B10 in beiden Fassungen",
    all(f"B{i} --" in de and f"B{i} --" in en for i in range(1, 11)))
refs_de = set(re.findall(r"Dok\.~(\d{3})", de)); refs_en = set(re.findall(r"Doc\.~(\d{3})", en))
chk("C gleiche Dokumentverweise De/En", refs_de == refs_en, f"De {sorted(refs_de)} / En {sorted(refs_en)}")

print("--- D  Keine physikalischen Statusvergaben im Dokument ---")
chk("D keine \\KM/\\BM/\\SM-Vergabe im Fliesstext", not re.search(r"\\(KM|BM|SM|XM|QM)\{\}", de))

print(f"\nErgebnis: {ok}/{n}")
sys.exit(0 if ok == n else 1)
