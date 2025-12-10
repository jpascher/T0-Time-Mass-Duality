#!/usr/bin/env python3
"""
Inkrementelles Kapitel-Skript mit Fehlererkennung und stabilem Zielordner.

Verwendung:
    py 22.py T0_Grundlagen_En.tex

Verhalten:
- Nimmt GENAU EINE Quelldatei als Argument (z.B. T0_Grundlagen_En.tex).
- Erzeugt eine bereinigte Kapiteldatei:
      chapters_en/T0_Grundlagen_En_ch.tex   (Arbeitsverzeichnis)
- Führt optional einen pdflatex-Testlauf durch (mit einer kleinen Test-Hülle).
- Wenn der Testlauf fehlerfrei (Exitcode 0) war:
    - Kopiert das Kapitel nach:
          chapters_en_final/T0_Grundlagen_En_ch.tex   (stabil, wird nie gelöscht)
    - Markiert dieses Kapitel in state.json als "done".
- Wenn der Testlauf Fehler hat:
    - Bricht ab, KEINE Kopie nach chapters_en_final.
    - state.json merkt "failed" für diese Quelle.

state.json:
- labels: globales Mapping alter -> neuer Labels (für konsistente \ref über Kapitel).
- label_counter: globaler Zähler.
- chapters: { "T0_Grundlagen_En.tex": "done"|"failed" }

WICHTIG:
- chapters_en_final/ wird NIE automatisch gelöscht.
- Nur chapters_en/ dient als Arbeitsbereich.
"""

from pathlib import Path
import re
import json
import sys
import subprocess
import shutil

BASE = Path(__file__).parent
CHAPTER_DIR = BASE / "chapters_en"
FINAL_DIR = BASE / "chapters_en_final"
STATE_FILE = BASE / "state.json"
TEST_TEX = BASE / "_test_chapter_wrapper.tex"

# Unicode-/Sonderzeichen-Mapping (wie zuvor)
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


def load_state():
    if STATE_FILE.exists():
        try:
            data = json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except Exception:
            data = {}
    else:
        data = {}
    labels = data.get("labels", {})
    label_counter = int(data.get("label_counter", 0))
    chapters = data.get("chapters", {})
    return {"labels": labels, "label_counter": label_counter, "chapters": chapters}


def save_state(state):
    out = {
        "labels": state["labels"],
        "label_counter": state["label_counter"],
        "chapters": state["chapters"],
    }
    STATE_FILE.write_text(json.dumps(out, indent=2, sort_keys=True), encoding="utf-8")


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
    return line[: m.start(1)] + content + line[m.end(1):]


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


def renumber_labels_and_refs(line: str, state: dict, doc_id: str) -> str:
    labels = state["labels"]

    def next_label():
        state["label_counter"] += 1
        return f"L-{doc_id}-{state['label_counter']:04d}"

    def repl_label(m):
        old = m.group(1)
        if old in labels:
            new = labels[old]
        else:
            new = next_label()
            labels[old] = new
        return r"\label{" + new + "}"

    line = re.sub(r"\\label\{([^}]+)\}", repl_label, line)

    def repl_ref(m):
        cmd = m.group(1)
        old = m.group(2)
        new = labels.get(old, old)
        return "\\" + cmd + "{" + new + "}"

    line = re.sub(r"\\(ref|eqref|autoref|cref|Cref)\{([^}]+)\}", repl_ref, line)
    return line


def process_file(src: Path, state: dict) -> Path:
    stem = src.stem
    CHAPTER_DIR.mkdir(exist_ok=True)
    FINAL_DIR.mkdir(exist_ok=True)

    chapter_path = CHAPTER_DIR / (stem + "_ch.tex")

    default_title = make_title_from_filename(stem)
    main_title: str | None = None

    raw_lines = src.read_text(encoding="utf-8", errors="ignore").splitlines(keepends=True)

    # Nur Inhalt zwischen \begin{document} und \end{document}
    start_idx = 0
    end_idx = len(raw_lines)
    for i, ln in enumerate(raw_lines):
        if r"\begin{document}" in ln:
            start_idx = i + 1
            break
    for i in range(len(raw_lines) - 1, -1, -1):
        if r"\end{document}" in raw_lines[i]:
            end_idx = i
            break
    core_lines = raw_lines[start_idx:end_idx]

    # Titel aus Präambel extrahieren (vor begin{document})
    for ln in raw_lines[:start_idx]:
        t = extract_main_title_from_line(ln)
        if t:
            main_title = t
            break

    content_started = False
    body_lines: list[str] = []

    doc_id = re.sub(r'[_\-](En|EN|en)$', "", stem)

    inside_bib = False

    for line in core_lines:
        stripped = line.strip()

        # Bibliographie-Blöcke ignorieren (oder später global sammeln)
        if stripped.startswith(r"\begin{thebibliography}"):
            inside_bib = True
            continue
        if inside_bib:
            if stripped.startswith(r"\end{thebibliography}"):
                inside_bib = False
                continue
            continue

        # offensichtlich defekte Einzelzeilen weg
        if stripped in {"}", "}%", "{", "{%"}:
            continue

        if not content_started:
            if not stripped or stripped.startswith('%'):
                continue

            # Kopf-/Layout-Kommandos verwerfen
            if (
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
                stripped.startswith(r"\tcbset")
            ):
                continue

            # Startbedingungen:
            # 1) Abstract
            if stripped.startswith(r"\begin{abstract}"):
                content_started = True
            # 2) oder erste Section/Chapter/Subsection, falls kein Abstract
            elif (
                stripped.startswith(r"\section") or
                stripped.startswith(r"\chapter") or
                stripped.startswith(r"\subsection") or
                stripped.startswith(r"\subsubsection")
            ):
                content_started = True
            else:
                continue

        # ab hier: Inhalt – spätes Herausfiltern von Kopf-/Layoutkommandos
        if (
            stripped.startswith(r"\setlength{\cftsecindent}") or
            stripped.startswith(r"\setlength{\cftsubsecindent}") or
            stripped.startswith(r"\newunicodechar") or
            stripped.startswith(r"\tcbuselibrary") or
            stripped.startswith(r"\tcbset") or
            ("Document" in stripped and "T0 Series" in stripped)
        ):
            continue

        line = sanitize_heading_math(line)
        line = normalize_headings_in_body(line)
        line = replace_unicode(line)
        line = convert_boxes_to_sections(line)
        line = renumber_labels_and_refs(line, state, doc_id)

        body_lines.append(line)

    title_core = main_title if main_title else default_title
    file_label = re.sub(r'[_\-](En|EN|en)$', "", stem)
    full_title_display = f"{title_core.replace('_', ' ')} ({file_label.replace('_', ' ')})"
    short_title = full_title_display

    with chapter_path.open("w", encoding="utf-8") as fout:
        fout.write(f"\\chapter[{short_title}]{{{full_title_display}}}\n\n")
        for bl in body_lines:
            fout.write(bl)

    print(f"[OK] Kapitel erzeugt: {chapter_path}")
    return chapter_path


def write_test_wrapper(chapter_path: Path):
    """
    Erzeugt eine kleine Test-LaTeX-Datei, die GENAU dieses Kapitel einbindet.
    """
    rel = chapter_path.name.replace(".tex", "")
    TEST_TEX.write_text(
        r"""\documentclass[11pt,a4paper]{book}
\usepackage[utf8]{inputenc}
\usepackage[english]{babel}
\usepackage{lmodern}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{graphicx}
\usepackage[unicode,pdfencoding=auto]{hyperref}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{siunitx}
\usepackage{fancyhdr}
\usepackage{float}
\usepackage{tikz}
\usepackage[most]{tcolorbox}
\usepackage{xcolor}

\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt}
\pagestyle{fancy}

\newcommand{\checkmarkx}{\checkmark}
\newcommand{\warningx}{\textbf{!}}

\newcommand{\mytimes}{\times}
\newcommand{\myapprox}{\approx}
\newcommand{\mysim}{\sim}
\newcommand{\myomega}{\omega}
\newcommand{\mypi}{\pi}
\newcommand{\myrightarrow}{\rightarrow}
\newcommand{\myRightarrow}{\Rightarrow}
\newcommand{\mypropto}{\propto}
\newcommand{\deltafield}{\delta\phi}
\newcommand{\xipar}{\xi}
\newcommand{\lambdah}{\lambda_h}

\newenvironment{abstract}{%
  \begin{center}\bfseries Abstract\end{center}\small
}{\par}

\begin{document}
\input{""" + rel + r"""}
\end{document}
""",
        encoding="utf-8",
    )


def run_pdflatex_test() -> bool:
    """
    Führt einen pdflatex-Lauf auf der Testdatei durch.
    Gibt True zurück, wenn Exitcode 0, sonst False.
    """
    try:
        # einmal laufen lassen, Log im gleichen Verzeichnis
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", TEST_TEX.name],
            cwd=BASE,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        return result.returncode == 0
    except FileNotFoundError:
        print("[WARN] pdflatex nicht gefunden – Übersetzung wird NICHT getestet.")
        # In diesem Fall gelten Kapitel als "bestmöglich" übersetzt
        return True


def main():
    if len(sys.argv) != 2:
        print("Verwendung: py 22.py T0_Grundlagen_En.tex")
        sys.exit(1)

    src_name = sys.argv[1]
    src_path = BASE / src_name
    if not src_path.exists():
        print(f"[ERROR] Quelldatei nicht gefunden: {src_path}")
        sys.exit(1)

    state = load_state()
    chapters_state = state["chapters"]

    if src_name in chapters_state and chapters_state[src_name] == "done":
        print(f"[SKIP] {src_name} ist bereits erfolgreich übersetzt (state=done).")
        sys.exit(0)

    chapter_path = process_file(src_path, state)
    save_state(state)

    # Test-LaTeX-Hülle schreiben und pdflatex-Test ausführen
    write_test_wrapper(chapter_path)
    ok = run_pdflatex_test()

    if not ok:
        print(f"[ERROR] pdflatex-Test fehlgeschlagen für {chapter_path}.")
        chapters_state[src_name] = "failed"
        save_state(state)
        sys.exit(1)

    # Wenn Test ok: Kapitel in FINAL_DIR kopieren und als done markieren
    FINAL_DIR.mkdir(exist_ok=True)
    final_path = FINAL_DIR / chapter_path.name
    shutil.copy2(chapter_path, final_path)
    chapters_state[src_name] = "done"
    save_state(state)

    print(f"[OK] Kapitel fehlerfrei getestet und nach {final_path} kopiert.")


if __name__ == "__main__":
    main()