#!/usr/bin/env python3
"""Erzeugt DOCUMENTS_de.md und DOCUMENTS.md (Repo-Wurzel) aus den vorhandenen PDFs.

Quelle: 2/pdf/NNN_*_{De,En}.pdf und 2/ipi/NNN_*_{De,En}.pdf.
Titel: aus \\title{...} bzw. \\chapter{...} der zugehörigen .tex-Datei.
Aufruf aus der Repo-Wurzel: python3 2/python/Werkzeuge/erzeuge_dokumentenliste.py
"""
import re, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PDF_DIRS = [ROOT/"2/pdf", ROOT/"2/ipi"]
TEX_DIRS = [ROOT/"2/Sources/wr_standalone_A4", ROOT/"2/Sources/ch", ROOT/"2/ipi"]

def clean(s):
    s = re.sub(r"(?<!\\)%[^\n]*", "", s)                       # LaTeX-Kommentare
    s = re.sub(r"\\\\\s*(\[[^\]]*\])?", " — ", s)               # Zeilenumbruch \\ bzw. \\[..]
    for a, b in {'\\"a': "ä", '\\"o': "ö", '\\"u': "ü", '\\"A': "Ä", '\\"O': "Ö", '\\"U': "Ü",
                 "{\\ss}": "ß", "\\ss{}": "ß", "\\ss ": "ß",
                 "\\,": " ", "\\ ": " ", "\\:": ":", "\;": " ", "\\-": "", "\\(": "", "\\)": "",
                 "\\[": "", "\\]": "", "\\&": "&", "\\%": "%", "\\_": "_"}.items():
        s = s.replace(a, b)
    s = re.sub(r"\\(?:color|vspace|hspace|fontsize|selectfont|Huge|huge|LARGE|Large|large)\*?(\{[^{}]*\})*", "", s)
    s = re.sub(r"\\texorpdfstring\{([^{}]*)\}\{[^{}]*\}", r"\1", s)
    for _ in range(3):
        s = re.sub(r"\\(?:textbf|emph|textit|mathrm|mathbb|mathcal|text|mbox|enquote|textsc|boldsymbol)\{([^{}]*)\}", r"\1", s)
    s = re.sub(r"\\[a-zA-Z]+\*?", "", s)
    s = s.replace("{", "").replace("}", "").replace("$", "")
    s = s.replace("~", " ").replace("---", "—").replace("--", "–").replace("–-", "–")
    s = re.sub(r"\s+", " ", s).strip(" :—")
    return re.sub(r"(\s*—\s*)+", " — ", s)

def balanced(txt, start):
    depth, i = 0, start
    while i < len(txt):
        if txt[i] == "{": depth += 1
        elif txt[i] == "}":
            depth -= 1
            if depth == 0: return txt[start+1:i]
        i += 1
    return ""

def title_for(stem, lang):
    cands = []
    for d in TEX_DIRS:
        cands += [d/f"{stem}.tex", d/f"{stem}_ch.tex", d/(stem.replace(f"_{lang}", f"_{lang}_ch")+".tex")]
    mid = stem[:-(len(lang)+1)]          # z. B. 256_RP3_T4_Grenzfall
    for d in TEX_DIRS:
        cands += sorted(d.glob(f"{mid}*_{lang}*.tex"))
    for p in cands:
        if not p.exists(): continue
        t = p.read_text(encoding="utf-8", errors="ignore")
        for cmd in (r"\title", r"\chapter", r"\section"):
            for m in re.finditer(re.escape(cmd) + r"\*?(\[[^\]]*\])?\{", t):
                if t[m.start():m.start()+12].startswith(r"\titleformat"): continue
                s = clean(balanced(t, m.end()-1))
                if len(s) > 3: return s[:160]
    pdf = next((d/f"{stem}.pdf" for d in PDF_DIRS if (d/f"{stem}.pdf").exists()), None)
    if pdf is not None:
        try:
            import subprocess
            info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
            m = re.search(r"^Title:\s*(.+)$", info, re.M)
            if m and len(m.group(1).strip()) > 3 and not m.group(1).strip().endswith(".tex") \
                    and not m.group(1).strip().startswith("Subject"):
                return clean(m.group(1))[:160]
        except Exception:
            pass
    return stem[:-(len(lang)+1)].split("_", 1)[-1].replace("_", " ").replace("-", " ").strip()

def collect(lang):
    docs = {}
    for d in PDF_DIRS:
        for p in sorted(d.glob(f"[0-9][0-9][0-9]*_{lang}.pdf")):
            m = re.match(r"(\d{3}[a-z]?)_", p.name)
            if not m: continue
            key = m.group(1)
            docs.setdefault(key, []).append(p)
    return docs

def write(lang, out, head, intro, col):
    docs = collect(lang)
    lines = [head, "", intro.format(n=len(docs), d=datetime.date.today().isoformat()), "",
             f"| {col[0]} | {col[1]} | PDF |", "|---|---|---|"]
    for key in sorted(docs, key=lambda k: (int(k[:3]), k)):
        for p in docs[key]:
            tit = title_for(p.stem, lang).replace("|", "/")
            lines.append(f"| {key} | {tit} | [PDF]({p.relative_to(ROOT).as_posix()}) |")
    (ROOT/out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(docs)

n_de = write("De", "DOCUMENTS_de.md", "# FFGFT — Dokumentenliste",
    "{n} nummerierte Dokumente (deutsche Fassungen), automatisch erzeugt am {d} aus den PDFs in `2/pdf/` und `2/ipi/` "
    "mit `2/python/Werkzeuge/erzeuge_dokumentenliste.py`. Korrekturen zu einzelnen Dokumenten stehen im Register Dok. 190.",
    ("Dok.", "Titel"))
n_en = write("En", "DOCUMENTS.md", "# FFGFT — Document list",
    "{n} numbered documents (English versions), generated automatically on {d} from the PDFs in `2/pdf/` and `2/ipi/` "
    "with `2/python/Werkzeuge/erzeuge_dokumentenliste.py`. Corrections to individual documents are kept in the register, Doc. 190.",
    ("Doc.", "Title"))
print("De:", n_de, "En:", n_en)
