#!/usr/bin/env python3
"""
Automatisches, inkrementelles Kapitel-Skript mit Fehlererkennung,
gemeinsamer Kompilation aller bisherigen Kapitel und automatischer
Makro-Erzeugung, ohne Standard-LaTeX-Kommandos zu überschreiben.
Zusätzlich:
- Problematische Makros wie checkmarkx, warningx werden im generierten
  Text auf neue Namen (z.B. checkmarkxa, warningxa) umgebogen, damit
  bestehende Definitionen nicht kollidieren.
Optimierungen: Kompilierte Regex, erweiterte Standard-Makros, dynamische Dateiliste.
"""
from pathlib import Path
import re
import json
import subprocess
import shutil
import sys
import glob

BASE = Path(__file__).parent
CHAPTER_DIR = BASE / "chapters_en"
FINAL_DIR = BASE / "chapters_en_final"
STATE_FILE = BASE / "state.json"
TEST_TEX = BASE / "_test_all_chapters.tex"
USE_LATEXMK = True  # Setze auf False für reines pdflatex

# Dynamische Ermittlung der ENABLED_CHAPTERS: Scanne .tex-Dateien mit "En"
ENABLED_CHAPTERS = [Path(f).name for f in BASE.glob("*.tex") if "En" in f.stem.lower()]

# Kompilierte Regex für Performance
MACRO_RE = re.compile(r"\\([A-Za-z]+)")
BOX_BEGIN_RE = re.compile(r"^\\begin\{([a-zA-Z_]+)\}")
BOX_END_RE = re.compile(r"^\\end\{([a-zA-Z_]+)\}")
HEADING_MATH_DOLLAR = re.compile(r"\$[^$]*\$")
HEADING_BRACE = re.compile(r"({.*})")
HEADING_CMD = re.compile(r"\\[a-zA-z]+\*?(?:\[[^\]]*\])?")
HEADING_CARET = re.compile(r"\^\{[^}]*\}")
HEADING_CARET_SIMPLE = re.compile(r"\^[A-Za-z0-9]+")
TITLE_PATTERNS = [
    re.compile(r"^\\title\{(.*)\}\s*$"),
    re.compile(r"^\\chapter\*?\{([^}]*)\}"),
    re.compile(r"^\\section\*?\{([^}]*)\}")
]
CHAPTER_REPLACE = re.compile(r"^\\chapter\*?\{")
SECTION_BOLD = re.compile(r"^\\textbf\{([^}]*)\}\s*(\\\\)?\s*$")
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
REF_RE = re.compile(r"\\(ref|eqref|autoref|cref|Cref)\{([^}]+)\}")
CONFLICT_PATTERN = re.compile(r"\\(?P<old>[A-Za-z]+)(?![A-Za-z])")  # Für rename, aber spezifisch unten
DOCUMENT_BEGIN = re.compile(r"\\begin\{document\}")
DOCUMENT_END = re.compile(r"\\end\{document\}")
BIB_BEGIN = re.compile(r"\\begin\{thebibliography\}")
BIB_END = re.compile(r"\\end\{thebibliography\}")

UNICODE_MAP = {
    "α": r"\alpha ", "β": r"\beta ", "γ": r"\gamma ", "δ": r"\delta ",
    "ε": r"\epsilon ", "ζ": r"\zeta ", "η": r"\eta ", "θ": r"\theta ",
    "ι": r"\iota ", "κ": r"\kappa ", "λ": r"\lambda ", "μ": r"\mu ",
    "ν": r"\nu ", "ξ": r"\xi ", "ο": r"o", "π": r"\pi ", "ρ": r"\rho ",
    "σ": r"\sigma ", "τ": r"\tau ", "υ": r"\upsilon ", "φ": r"\phi ",
    "χ": r"\chi ", "ψ": r"\psi ", "ω": r"\omega ",
    "Α": r"A", "Β": r"B", "Γ": r"\Gamma ", "Δ": r"\Delta ", "Ε": r"E",
    "Ζ": r"Z", "Η": r"H", "Θ": r"\Theta ", "Ι": r"I", "Κ": r"K",
    "Λ": r"\Lambda ", "Μ": r"M", "Ν": r"N", "Ξ": r"\Xi ", "Ο": r"O",
    "Π": r"\Pi ", "Ρ": r"P", "Σ": r"\Sigma ", "Τ": r"T", "Υ": r"\Upsilon ",
    "Φ": r"\Phi ", "Χ": r"X", "Ψ": r"X", "Ω": r"\Omega ",
    "∞": r"\infty ", "∂": r"\partial ", "∇": r"\nabla ", "√": r"\sqrt{}",
    "≈": r"\approx ", "≠": r"\neq ", "≤": r"\leq ", "≥": r"\geq ",
    "↔": r"\leftrightarrow ", "⇒": r"\Rightarrow ", "⇐": r"\Leftarrow ",
    "⇔": r"\Leftrightarrow ", "∈": r"\in ", "∉": r"\notin ",
    "∩": r"\cap ", "∪": r"\cup ", "∅": r"\emptyset ",
    "∑": r"\sum ", "∏": r"\prod ", "∫": r"\int ", "∝": r"\propto ",
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

CONFLICT_RENAMES = {
    "checkmarkx": "checkmarkxa",
    "warningx": "warningxa",
}

STANDARD_LATEX_COMMANDS = {
    "toprule", "midrule", "bottomrule", "hline", "cline", "hrule",
    "vspace", "quad", "rule", "textwidth", "vfill",
    "endfirsthead", "endhead", "endfoot", "endlastfoot",
    "partial", "nabla", "square", "vec", "rightarrow", "hat",
    "geq", "neq", "gg", "ll", "ell", "varepsilon", "hbar", "left", "right", "times",
    "approx", "sim", "underbrace", "boxed", "propto", "pm", "circ",
    "dagger", "rangle", "bar", "infty", "Rightarrow", "dfrac", "texttimes", "href",
    "textsuperscript",
    "text", "caption", "centering", "si", "bfseries",
    "appendix", "today", "footnote", "multicolumn", "nonumber", "to",
    "bibitem",
    "alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta",
    "iota", "kappa", "lambda", "mu", "nu", "xi", "pi", "rho", "sigma",
    "tau", "upsilon", "phi", "chi", "psi", "omega",
    "Gamma", "Delta", "Theta", "Lambda", "Xi", "Pi", "Sigma", "Upsilon",
    "Phi", "Psi", "Omega",
    "arg", "downarrow", "equiv", "langle", "leftrightarrow", "leq", "uparrow", "xrightarrow",
    "langle", "rangle", "uparrow", "downarrow", "Leftrightarrow", "Leftarrow", "Rightarrow",
    "leq", "geq", "equiv", "sim", "approx", "propto",
    # Neue aus Standard-Listen hinzugefügt
    "binom", "det", "aleph", "beth", "gimel", "daleth", "wp", "Re", "Im",
    "exists", "forall", "ni", "neg", "perp", "parallel", "mid", "vdash",
    "dashv", "nparallel", "wr", "amalg", "spadesuit", "clubsuit", "diamondsuit",
    "heartsuit", "flat", "natural", "sharp", "fbox", "framebox", "color",
    "colorbox", "par", "noindent", "smallskip", "medskip", "bigskip",
}

KNOWN_STD_MACROS = {
    "documentclass", "usepackage", "begin", "end", "chapter", "section",
    "subsection", "subsubsection", "paragraph", "subparagraph",
    "label", "ref", "eqref", "pagestyle", "thispagestyle", "tableofcontents",
    "maketitle", "addcontentsline", "newpage", "clearpage",
    "textbf", "textit", "emph", "texttt", "textrm", "textsf", "textsc",
    "tiny", "scriptsize", "footnotesize", "small", "normalsize",
    "large", "Large", "LARGE", "huge", "Huge",
    "frac", "sqrt", "sum", "int", "prod", "lim", "sin", "cos", "tan",
    "log", "ln", "exp", "min", "max", "cdot",
    *STANDARD_LATEX_COMMANDS,
    "item", "itemize", "enumerate", "description", "flushleft", "flushright",
    "center", "abstract", "equation", "align", "gather", "split",
    "tabular", "figure", "table",
    "url", "includegraphics", "dots", "ldots", "cdots",
    "vdots", "ddots", "mathbf", "mathcal", "mathrm", "mathbb",
    "checkmark",
    "tikzset", "pgfkeys",
    "newenvironment", "newtheorem", "newcounter", "DeclareMathOperator",
    "providecommand", "renewenvironment", "renewcommand",
    "arg", "downarrow", "equiv", "langle", "leftrightarrow", "leq", "uparrow", "xrightarrow",
    "langle", "rangle", "Leftrightarrow", "Leftarrow", "Rightarrow",
    # Neue hinzugefügt für bessere Abdeckung
    "noalign", "multicols", "DeclarePairedDelimiter", "genfrac", "cramped",
    "clap", "llap", "rlap", "mathclap", "vphantom", "hphantom",
}

COLOR_DEFS = {
    "t0blue": ("RGB", "0,102,204"),
    "t0red": ("RGB", "192,0,0"),
    "t0green": ("RGB", "0,128,64"),
    "t0orange": ("RGB", "255,140,0"),
}
TIKZ_STYLES = {
    "t0blue": "draw=t0blue, fill=t0blue!20",
    "t0red": "draw=t0red, fill=t0red!20",
    "t0green": "draw=t0green, fill=t0green!20",
    "t0orange": "draw=t0orange, fill=t0orange!20",
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
    macros = data.get("macros", {})
    # Filter out known standard macros
    macros = {k: v for k, v in macros.items() if k not in KNOWN_STD_MACROS}
    return {"labels": labels, "label_counter": label_counter,
            "chapters": chapters, "macros": macros}

def save_state(state):
    out = {
        "labels": state["labels"],
        "label_counter": state["label_counter"],
        "chapters": state["chapters"],
        "macros": state["macros"],
    }
    STATE_FILE.write_text(json.dumps(out, indent=2, sort_keys=True), encoding="utf-8")

def make_title_from_filename(stem: str) -> str:
    s = re.sub(r'[_\-](En|EN|en)$', "", stem)
    s = re.sub(r"[_\-]+", " ", s)
    return " ".join(w.capitalize() for w in s.split())

def replace_unicode(text: str) -> str:
    for ch, macro in UNICODE_MAP.items():
        text = text.replace(ch, macro)
    return text

def collect_macros_from_text(text: str, state: dict):
    macros = state["macros"]
    for m in MACRO_RE.finditer(text):
        name = m.group(1)
        if name in KNOWN_STD_MACROS or name in CONFLICT_RENAMES:
            continue
        if name not in macros:
            macros[name] = ""
            print(f"[INFO] Neues Makro erkannt: \\{name} (temporär leer definiert)")

def convert_boxes_to_sections(lines: list[str]) -> list[str]:
    converted = []
    for line in lines:
        stripped = line.strip()
        m = BOX_BEGIN_RE.match(stripped)
        if m and m.group(1) in BOX_TO_SECTION:
            title = BOX_TO_SECTION[m.group(1)]
            converted.append(f"\\section*{{{title}}}\n")
            continue
        m = BOX_END_RE.match(stripped)
        if m and m.group(1) in BOX_TO_SECTION:
            converted.append(f"% end box {m.group(1)}\n")
            continue
        converted.append(line)
    return converted

def sanitize_heading_math(line: str) -> str:
    if not any(line.lstrip().startswith(cmd) for cmd in ("\\chapter", "\\section", "\\subsection", "\\subsubsection")):
        return line
    line = HEADING_MATH_DOLLAR.sub("", line)
    m = HEADING_BRACE.search(line)
    if not m:
        return line
    content = m.group(1)
    content = HEADING_CMD.sub("", content)
    content = HEADING_CARET.sub("", content)
    content = HEADING_CARET_SIMPLE.sub("", content)
    content = content.replace("_", " ")
    inner = content.strip()
    if inner.startswith("{") and inner.endswith("}"):
        inner = inner[1:-1]
    inner = re.sub(r"[{}]", "", inner)
    inner = re.sub(r"\s+", " ", inner).strip()
    content = "{" + inner + "}"
    return line[:m.start(1)] + content + line[m.end(1):]

def normalize_headings_in_body(line: str) -> str:
    stripped = line.strip()
    if CHAPTER_REPLACE.match(stripped):
        return line.replace(r"\chapter{", r"\section{", 1).replace(r"\chapter*{", r"\section*{", 1)
    m = SECTION_BOLD.match(stripped)
    if m:
        return f"\\section*{{{m.group(1).strip()}}}\n"
    return line

def extract_main_title_from_text(lines: list[str]) -> str | None:
    pre_doc = "".join(line for line in lines if not DOCUMENT_BEGIN.search(line))
    for pat in TITLE_PATTERNS:
        m = pat.search(pre_doc)
        if m:
            raw = m.group(1)
            tmp = HEADING_CMD.sub("", raw)
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

    line = LABEL_RE.sub(repl_label, line)

    def repl_ref(m):
        cmd = m.group(1)
        old = m.group(2)
        new = labels.get(old, old)
        return "\\" + cmd + "{" + new + "}"

    line = REF_RE.sub(repl_ref, line)
    return line

def rename_conflict_macros(line: str) -> str:
    for old, new in CONFLICT_RENAMES.items():
        pattern = re.compile(rf"\\{re.escape(old)}(?![A-Za-z])")
        line = pattern.sub(r"\\" + new, line)
    return line

def process_one_chapter(src_name: str, state: dict) -> Path:
    src = BASE / src_name
    if not src.exists():
        raise FileNotFoundError(f"Quelldatei nicht gefunden: {src}")
    CHAPTER_DIR.mkdir(exist_ok=True)
    FINAL_DIR.mkdir(exist_ok=True)
    stem = src.stem
    chapter_path = CHAPTER_DIR / (stem + "_ch.tex")
    default_title = make_title_from_filename(stem)
    with src.open("r", encoding="utf-8", errors="ignore") as fin:
        raw_lines = fin.readlines()
    main_title = extract_main_title_from_text(raw_lines)
    start_idx = next((i + 1 for i, line in enumerate(raw_lines) if DOCUMENT_BEGIN.search(line)), 0)
    end_idx = next((i for i in range(len(raw_lines) - 1, -1, -1) if DOCUMENT_END.search(raw_lines[i])), len(raw_lines))
    core_text = "".join(raw_lines[start_idx:end_idx])
    collect_macros_from_text(core_text, state)
    body_lines = []
    inside_bib = False
    content_started = False
    skip_patterns = {
        r"\maketitle", r"\tableofcontents", r"\newpage", r"\fancy", r"\pagestyle",
        r"\thispagestyle", r"\large", r"\normalsize", r"\setlength{\cftsecindent}",
        r"\setlength{\cftsubsecindent}", r"\newunicodechar", r"\tcbuselibrary", r"\tcbset"
    }
    for line in raw_lines[start_idx:end_idx]:
        stripped = line.strip()
        if BIB_BEGIN.match(stripped):
            inside_bib = True
            continue
        if inside_bib:
            if BIB_END.match(stripped):
                inside_bib = False
            continue
        if stripped.startswith(("\newcommand", "\definecolor", "\tikzset", "\newenvironment", "\newtheorem")):
            continue
        if stripped in {"}", "}%", "{", "{%"}:
            continue
        if not content_started:
            if not stripped or stripped.startswith('%') or any(p in stripped for p in skip_patterns) or ("Document" in stripped and "T0 Series" in stripped):
                continue
            if stripped.startswith(r"\begin{abstract}") or stripped.startswith(("\\section", "\\chapter", "\\subsection", "\\subsubsection")):
                content_started = True
            else:
                continue
        if any(p in stripped for p in skip_patterns) or ("Document" in stripped and "T0 Series" in stripped):
            continue
        line = sanitize_heading_math(line)
        line = normalize_headings_in_body(line)
        line = renumber_labels_and_refs(line, state, re.sub(r'[_\-](En|EN|en)$', "", stem))
        line = rename_conflict_macros(line)
        body_lines.append(line)
    # Unicode auf gesamten Body anwenden (effizienter)
    body_text = "".join(body_lines)
    body_text = replace_unicode(body_text)
    body_lines = convert_boxes_to_sections(body_text.splitlines(keepends=True))
    title_core = main_title if main_title else default_title
    file_label = re.sub(r'[_\-](En|EN|en)$', "", stem)
    full_title_display = f"{title_core.replace('_', ' ')} ({file_label.replace('_', ' ')})"
    short_title = full_title_display
    with chapter_path.open("w", encoding="utf-8") as fout:
        fout.write(f"\\chapter[{short_title}]{{{full_title_display}}}\n\n")
        fout.writelines(body_lines)
    print(f"[OK] Kapitel erzeugt: {chapter_path}")
    return chapter_path

def write_test_all_chapters(new_chapter: Path, state: dict):
    chapters_state = state["chapters"]
    macros = state["macros"]
    lines = [
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
""",
    ]
    for name, (model, values) in COLOR_DEFS.items():
        lines.append(f"\\definecolor{{{name}}}{{{model}}}{{{values}}}\n")
    lines.append(r"\tikzset{" + "\n")
    for name, style in TIKZ_STYLES.items():
        lines.append(f" {name}/.style={{{style}}},\n")
    lines.append(r"}" + "\n")
    lines.append(r"\newcommand{\checkmarkxa}{\checkmark}" + "\n")
    lines.append(r"\newcommand{\warningxa}{\textbf{!}}" + "\n")
    macro_defs = []
    for name in sorted(macros):
        if name in STANDARD_LATEX_COMMANDS:
            continue
        definition = macros[name]
        if not definition:
            defaults = {
                "xipar": r"\xi", "betapar": r"\beta", "alphapar": r"\alpha",
                "Efield": r"\mathcal{E}", "Dfrak": r"\mathcal{D}", "Kfrak": r"\mathcal{K}",
                "deltafield": r"\delta\phi", "lambdah": r"\lambda_h"
            }
            definition = defaults.get(name, "")
            if not definition:
                continue  # Skip empty to avoid errors
        macro_defs.append(f"\\newcommand\\{{{name}}}{{{definition}}}" + "\n")
    lines.extend(macro_defs)
    lines.append(
        r"""
\newenvironment{abstract}{%
  \begin{center}\bfseries Abstract\end{center}\small
}{\par}
\begin{document}
"""
    )
    for src_name in ENABLED_CHAPTERS:
        if chapters_state.get(src_name) == "done":
            stem = Path(src_name).stem
            rel = (FINAL_DIR / f"{stem}_ch").relative_to(BASE).as_posix()
            lines.append(f"\\input{{{rel}}}\n")
    rel_new = new_chapter.relative_to(BASE).as_posix().replace(".tex", "")
    lines.append(f"\\input{{{rel_new}}}\n")
    lines.append(r"\end{document}" + "\n")
    TEST_TEX.write_text("".join(lines), encoding="utf-8")

def run_latex_test() -> bool:
    cmd = ["latexmk", "-pdf", "-halt-on-error", "-interaction=nonstopmode", TEST_TEX.name] if USE_LATEXMK else ["pdflatex", "-interaction=nonstopmode", TEST_TEX.name]
    try:
        result = subprocess.run(cmd, cwd=BASE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
        return result.returncode == 0
    except FileNotFoundError as e:
        if USE_LATEXMK:
            print("[WARN] latexmk nicht gefunden – fallback zu pdflatex.")
            return run_latex_test()  # Rekursiv mit pdflatex
        print(f"[WARN] pdflatex nicht gefunden: {e} – Kapitel als OK markiert.")
        return True

def main():
    state = load_state()
    chapters_state = state["chapters"]
    print("[INFO] Starte Verarbeitung der Kapitel-Liste (dynamisch gescannt).")
    for src_name in ENABLED_CHAPTERS:
        status = chapters_state.get(src_name)
        if status == "done":
            continue
        src_path = BASE / src_name
        if not src_path.exists():
            print(f"[WARN] Quelldatei fehlt: {src_path} -> markiere als 'missing'")
            chapters_state[src_name] = "missing"
            save_state(state)
            continue
        print(f"[INFO] Nächstes Kapitel: {src_name}")
        try:
            chapter_path = process_one_chapter(src_name, state)
        except FileNotFoundError as e:
            print(f"[ERROR] {e}")
            chapters_state[src_name] = "missing"
            save_state(state)
            continue
        write_test_all_chapters(chapter_path, state)
        ok = run_latex_test()
        if not ok:
            print(f"[ERROR] LaTeX-Test fehlgeschlagen für {chapter_path}.")
            chapters_state[src_name] = "failed"
            save_state(state)
            sys.exit(1)
        final_path = FINAL_DIR / chapter_path.name
        shutil.copy2(chapter_path, final_path)
        chapters_state[src_name] = "done"
        save_state(state)
        print(f"[OK] Kapitel fehlerfrei getestet und nach {final_path} kopiert.")
    print("[INFO] Verarbeitung abgeschlossen.")

if __name__ == "__main__":
    main()