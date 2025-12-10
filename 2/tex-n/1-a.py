#!/usr/bin/env python3
from pathlib import Path
import re

BASE = Path(__file__).parent
CHAPTER_DIR = BASE / "chapters_en"

EXCLUDE_SOURCES = {
    "T0_Book_En.tex",
    "T0_Book2_En.tex",
    "generate_book_chapters_en.tex",
    "generate_book_chapters1_en.tex",
    "generate_book_chapters1_en.py",
    "1.py",
}

GLOBAL_BIBITEMS: list[str] = []

# Nur diese Kapitel werden aktuell verarbeitet
ENABLED_CHAPTERS = [
    "T0_Introduction_En.tex",
    "T0_Grundlagen_En.tex",
    "T0_Modell_Uebersicht_En.tex",
    "T0_tm-erweiterung-x6_En.tex",
    "T0_Teilchenmassen_En.tex",
    "T0_Neutrinos_En.tex",
    "T0_xi-und-e_En.tex",
]

CHAPTER_ORDER = ENABLED_CHAPTERS[:]
CHAPTER_ORDER_INDEX = {name: i for i, name in enumerate(CHAPTER_ORDER)}

# Unicode-/Sonderzeichen-Mapping
UNICODE_MAP = {
    # griechisch klein
    "α": r"\alpha ", "β": r"\beta ", "γ": r"\gamma ", "δ": r"\delta ",
    "ε": r"\epsilon ", "ζ": r"\zeta ", "η": r"\eta ", "θ": r"\theta ",
    "ι": r"\iota ", "κ": r"\kappa ", "λ": r"\lambda ", "μ": r"\mu ",
    "ν": r"\nu ", "ξ": r"\xi ", "ο": r"o", "π": r"\pi ", "ρ": r"\rho ",
    "σ": r"\sigma ", "τ": r"\tau ", "υ": r"\upsilon ", "φ": r"\phi ",
    "χ": r"\chi ", "ψ": r"\psi ", "ω": r"\omega ",

    # griechisch groß
    "Α": r"A", "Β": r"B", "Γ": r"\Gamma ", "Δ": r"\Delta ", "Ε": r"E",
    "Ζ": r"Z", "Η": r"H", "Θ": r"\Theta ", "Ι": r"I", "Κ": r"K",
    "Λ": r"\Lambda ", "Μ": r"M", "Ν": r"N", "Ξ": r"\Xi ", "Ο": r"O",
    "Π": r"\Pi ", "Ρ": r"P", "Σ": r"\Sigma ", "Τ": r"T", "Υ": r"\Upsilon ",
    "Φ": r"\Phi ", "Χ": r"X", "Ψ": r"\Psi ", "Ω": r"\Omega ",

    # Mathe-Symbole / Operatoren
    "∞": r"\infty ", "∂": r"\partial ", "∇": r"\nabla ", "√": r"\sqrt{}",
    "≈": r"\approx ", "≠": r"\neq ", "≤": r"\leq ", "≥": r"\geq ",
    "↔": r"\leftrightarrow ", "⇒": r"\Rightarrow ", "⇐": r"\Leftarrow ",
    "⇔": r"\Leftrightarrow ", "∈": r"\in ", "∉": r"\notin ",
    "∩": r"\cap ", "∪": r"\cup ", "∅": r"\emptyset ",
    "∑": r"\sum ", "∏": r"\prod ", "∫": r"\int ", "∝": r"\propto ",

    # Sonstige
    "★": r"\star ", "✓": r"\checkmark ", "ħ": r"\hbar ",
}

BOX_TO_SECTION = {
    "foundation": "Foundation",
    "alternative": "Alternative",
    "keyresult": "Key Result",
    "warning": "Warning",
    "experimental": "Experimental",
    "method": "Method",
    "equivalence": "Equivalence",
    "photon": "Photon",
    "speculation": "Speculation",
    "koidebox": "Koide",
    "insight": "Insight",
    "relation": "Relation",
    "treatise": "Treatise",
    "application": "Application",
    "dimensional": "Dimensional",
    "verification": "Verification",
    "interpretation": "Interpretation",
    "explanation": "Explanation",
    "derivation": "Derivation",
    "result": "Result",
    "historical": "Historical",
    "formula": "Formula",
    "definition": "Definition",
    "important": "Important",
    "summary": "Summary",
    "revolutionary": "Revolutionary",
    "experiment": "Experiment",
    "overview": "Overview",
    "documentbox": "Document",
    "achievement": "Achievement",
    "sibox": "SI-Box",
    "principle": "Principle",
    "caution": "Caution",
    "theorem": "Theorem",
    "neutrino": "Neutrino",
    "key": "Key",
    "analysis": "Analysis",
    "correct": "Correct",
    "units": "Units",
    "proof_step": "Proof Step",
    "lemma": "Lemma",
    "example": "Example",
    "category": "Category",
    "axiom": "Axiom",
    "algorithm": "Algorithm",
    "algorithmic": "Algorithmic",
    "quantum": "Quantum",
    "fundamental": "Fundamental",
    "newperspective": "New Perspective",
    "discovery": "Discovery",
    "numerical": "Numerical",
    "question": "Question",
    "technical": "Technical",
    "critical": "Critical",
    "revolution": "Revolution",
    "t0box": "T0 Box",
    "smbox": "SM Box",
    "pvbox": "PV Box",
    "gemeinsam": "Gemeinsam",
    "vergleich": "Vergleich",
    "vorteil": "Vorteil",
    "beweis": "Beweis",
    "folgerung": "Folgerung",
}


def is_english_source(path: Path) -> bool:
    name = path.name
    if not name.endswith(".tex"):
        return False
    if name in EXCLUDE_SOURCES:
        return False
    if name not in ENABLED_CHAPTERS:
        return False
    return True


def make_title_from_filename(stem: str) -> str:
    s = re.sub(r'[_\-](En|EN|en)$', "", stem)
    s = re.sub(r"[_\-]+", " ", s)
    words = s.split()
    words = [w.capitalize() for w in words]
    return " ".join(words)


def replace_unicode(line: str) -> str:
    for ch, macro in UNICODE_MAP.items():
        if ch in line:
            line = line.replace(ch, macro)
    return line


def convert_boxes_to_sections(line: str) -> str:
    stripped = line.strip()
    m = re.match(r"^\\begin\{([a-zA-Z_]+)\}", stripped)
    if m:
        env = m.group(1)
        if env in BOX_TO_SECTION:
            title = BOX_TO_SECTION[env]
            return f"\\section*{{{title}}}\n"
    m2 = re.match(r"^\\end\{([a-zA-Z_]+)\}", stripped)
    if m2 and m2.group(1) in BOX_TO_SECTION:
        return "% end box " + m2.group(1) + "\n"
    return line


def sanitize_heading_math(line: str) -> str:
    stripped = line.lstrip()
    if not stripped.startswith(("\\chapter", "\\section", "\\subsection", "\\subsubsection")):
        return line
    line = re.sub(r"\$[^$]*\$", "", line)
    m = re.search(r"({.*})", line)
    if not m:
        return line
    content = m.group(1)
    content = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?", "", content)
    content = re.sub(r"\^\{[^}]*\}", "", content)
    content = re.sub(r"\^[A-Za-z0-9]+", "", content)
    content = content.replace("_", " ")
    inner = content.strip()
    if inner.startswith("{") and inner.endswith("}"):
        inner = inner[1:-1]
    inner = re.sub(r"[{}]", "", inner)
    inner = re.sub(r"\s+", " ", inner).strip()
    content = "{" + inner + "}"
    return line[: m.start(1)] + content + line[m.end(1) :]


def normalize_headings_in_body(line: str) -> str:
    stripped = line.strip()
    if stripped.startswith(r"\chapter*{"):
        return line.replace(r"\chapter*{", r"\section*{", 1)
    if stripped.startswith(r"\chapter{"):
        return line.replace(r"\chapter{", r"\section{", 1)
    m = re.match(r"^\\textbf\{([^}]*)\}\\\\\s*$", stripped)
    if m:
        return f"\\section*{{{m.group(1).strip()}}}\n"
    m2 = re.match(r"^\\textbf\{([^}]*)\}\s*$", stripped)
    if m2:
        return f"\\section*{{{m2.group(1).strip()}}}\n"
    return line


def extract_main_title_from_line(line: str) -> str | None:
    stripped = line.strip()
    m = re.match(r"^\\title\{(.*)\}\s*$", stripped)
    if m:
        raw = m.group(1)
        tmp = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?", "", raw)
        parts = re.split(r"\\\\", tmp)
        first = parts[0].strip() if parts else ""
        return re.sub(r"\s+", " ", first) or None
    for pat in (r"^\\chapter\*?\{([^}]*)\}", r"^\\section\*?\{([^}]*)\}"):
        m = re.match(pat, stripped)
        if m:
            raw = m.group(1)
            tmp = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?", "", raw)
            parts = re.split(r"\\\\", tmp)
            first = parts[0].strip() if parts else ""
            return re.sub(r"\s+", " ", first) or None
    return None


def renumber_labels_and_refs(line: str, label_map: dict[str, str], doc_id: str, counter_ref: list[int]) -> str:
    def next_label():
        counter_ref[0] += 1
        return f"L-{doc_id}-{counter_ref[0]:04d}"

    def repl_label(m):
        old = m.group(1)
        if old in label_map:
            new = label_map[old]
        else:
            new = next_label()
            label_map[old] = new
        return r"\label{" + new + "}"

    line = re.sub(r"\\label\{([^}]+)\}", repl_label, line)

    def repl_ref(m):
        cmd = m.group(1)
        old = m.group(2)
        new = label_map.get(old, old)
        return "\\" + cmd + "{" + new + "}"

    line = re.sub(r"\\(ref|eqref|autoref|cref|Cref)\{([^}]+)\}", repl_ref, line)
    return line


def sort_key(path: Path):
    name = path.name
    if name in CHAPTER_ORDER_INDEX:
        return (0, CHAPTER_ORDER_INDEX[name])
    return (1, name.lower())


def main():
    global GLOBAL_BIBITEMS

    CHAPTER_DIR.mkdir(exist_ok=True)

    sources = sorted([p for p in BASE.glob("*.tex") if is_english_source(p)], key=sort_key)
    if not sources:
        return

    chapter_files: list[Path] = []

    for src in sources:
        stem = src.stem
        chapter_path = CHAPTER_DIR / (stem + "_ch.tex")

        default_title = make_title_from_filename(stem)
        main_title: str | None = None

        with src.open("r", encoding="utf-8", errors="ignore") as fin:
            raw_lines = fin.readlines()

        # Nur Inhalt zwischen \begin{document} und \end{document}
        start_idx = 0
        end_idx = len(raw_lines)
        for i, ln in enumerate(raw_lines):
            if ln.strip().startswith(r"\begin{document}"):
                start_idx = i + 1
                break
        for i in range(len(raw_lines) - 1, -1, -1):
            if raw_lines[i].strip().startswith(r"\end{document}"):
                end_idx = i
                break
        core_lines = raw_lines[start_idx:end_idx]

        # Titel aus Präambel extrahieren (vor begin{document})
        for ln in raw_lines[:start_idx]:
            t = extract_main_title_from_line(ln)
            if t:
                main_title = t
                break

        # Jetzt core_lines filtern/transformieren
        content_started = False
        body_lines: list[str] = []

        # Label-Renumbering
        doc_id = re.sub(r'[_\-](En|EN|en)$', "", stem)
        label_map: dict[str, str] = {}
        label_counter = [0]  # mutable

        inside_bib = False

        for line in core_lines:
            stripped = line.strip()

            # Bibliographie-Blöcke global sammeln
            if stripped.startswith(r"\begin{thebibliography}"):
                inside_bib = True
                continue
            if inside_bib:
                if stripped.startswith(r"\end{thebibliography}"):
                    inside_bib = False
                    continue
                GLOBAL_BIBITEMS.append(line.rstrip("\n"))
                continue

            if not content_started:
                # Kommentare/Leerzeilen im inneren Kopf weg
                if not stripped or stripped.startswith('%'):
                    continue

                # Kopf-/Layout-Kommandos verwerfen
                if (
                    stripped.startswith(r"\chapter") or
                    stripped.startswith(r"\maketitle") or
                    stripped.startswith(r"\tableofcontents") or
                    stripped == r"\newpage" or
                    stripped.startswith(r"\fancy") or
                    stripped.startswith(r"\pagestyle") or
                    stripped.startswith(r"\thispagestyle") or
                    stripped.startswith(r"\large") or
                    stripped.startswith(r"\normalsize") or
                    stripped.startswith(r"\setlength{\cftsecindent}") or
                    stripped.startswith(r"\setlength{\cftsubsecindent}") or
                    ("Document" in stripped and "T0 Series" in stripped) or
                    stripped.startswith(r"\newunicodechar") or
                    stripped.startswith(r"\tcbuselibrary") or
                    stripped in {"}", "}%"}
                ):
                    continue

                # ab Abstract starten (wenn vorhanden)
                # wenn du statt dessen ab erster normalen Zeile starten willst,
                # kannst du diese Bedingung abschwächen
                if stripped.startswith(r"\begin{abstract}"):
                    content_started = True
                    # Zeile behalten
                else:
                    # solange bis zum Abstract alles weg
                    continue

            # ab hier: Inhalt
            line = sanitize_heading_math(line)
            line = normalize_headings_in_body(line)
            line = replace_unicode(line)
            line = convert_boxes_to_sections(line)
            line = renumber_labels_and_refs(line, label_map, doc_id, label_counter)

            body_lines.append(line)

        title_core = main_title if main_title else default_title
        file_label = re.sub(r'[_\-](En|EN|en)$', "", stem)
        full_title_display = f"{title_core.replace('_', ' ')} ({file_label.replace('_', ' ')})"
        short_title = full_title_display

        with chapter_path.open("w", encoding="utf-8") as fout:
            fout.write(f"\\chapter[{short_title}]{{{full_title_display}}}\n\n")
            for bl in body_lines:
                fout.write(bl)

        chapter_files.append(chapter_path)

    # Buch-TeX erzeugen
    book_path = BASE / "T0_Book_En.tex"
    with book_path.open("w", encoding="utf-8") as f:
        f.write(
            r"""\documentclass[11pt,a4paper,openany]{book}
\usepackage[a4paper,margin=2cm]{geometry}
\usepackage[utf8]{inputenc}
\usepackage[english]{babel}
\usepackage{lmodern}
\renewcommand{\familydefault}{\sfdefault}

\usepackage{amsmath,amssymb,amsthm}
\usepackage{graphicx}
\usepackage[unicode,pdfencoding=auto]{hyperref}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{siunitx}
\usepackage{fancyhdr}
\usepackage{float}
\usepackage{tikz}
\usepackage{setspace}
\usepackage{enumitem}
\usepackage{adjustbox}
\usepackage{xcolor}

\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt}

\hypersetup{
  colorlinks=true,
  linkcolor=blue,
  citecolor=blue,
  urlcolor=blue
}
\pagestyle{fancy}

\newcommand{\checkmarkx}{\checkmark}
\newcommand{\warningx}{\textbf{!}}

\title{T0 Time--Mass Duality\\Unified English Book}
\author{J. Pascher}
\date{\today}

\begin{document}

\maketitle
\tableofcontents
"""
        )
        f.write("\n%==============================\n% Automatisch generierte Kapitel:\n")
        for ch in chapter_files:
            rel = ch.relative_to(BASE).as_posix().replace(".tex", "")
            f.write(f"\n%%------------------------------\n\\input{{{rel}}}\n")

        if GLOBAL_BIBITEMS:
            f.write("\n%%==============================\n% Globales Literaturverzeichnis\n")
            f.write("\\chapter*{References}\n")
            f.write("\\addcontentsline{toc}{chapter}{References}\n")
            f.write("\\begin{thebibliography}{99}\n")
            for item in GLOBAL_BIBITEMS:
                f.write(item + "\n")
            f.write("\\end{thebibliography}\n")

        f.write("\n\\end{document}\n")


if __name__ == "__main__":
    main()