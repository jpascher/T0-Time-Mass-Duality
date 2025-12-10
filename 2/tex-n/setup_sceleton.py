#!/usr/bin/env python3
"""
Legt ein Gerüst für den englischen Buch-Build an.

Es werden NICHTS überschrieben, sondern nur Verzeichnisse und Dateien angelegt,
die noch nicht existieren.
"""

from pathlib import Path

BASE = Path(__file__).parent

# Verzeichnisse, die wir brauchen
DIRS = [
    BASE / "chapters_en",          # generierte Kapitel (alt)
    BASE / "chapters_en_sceleton", # alternative Spielwiese (sceleton)
]

# Inhalte für Dateien
SKELETON_PY = """#!/usr/bin/env python3
\"\"\"Skeleton-Skript für den englischen Buch-Build.

Dieses Skript wird später von Copilot mit Logik gefüllt.
Aktuell macht es noch nichts.
\"\"\"

from pathlib import Path


def main() -> None:
    base = Path(__file__).parent
    print(f\"Skeleton-Skript ausgeführt. Basisverzeichnis: {base}\")


if __name__ == \"__main__\":
    main()
"""

BOOK_TEX = r"""\documentclass[11pt,a4paper,openany]{book}
% Skeleton-Buchdatei. Wird später automatisch mit Inhalt gefüllt.

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

\title{T0 Time--Mass Duality\\Unified English Book (Skeleton)}
\author{J. Pascher}
\date{\today}

\begin{document}

\maketitle
\tableofcontents

% Hier werden später automatisch generierte Kapitel eingefügt.

\end{document}
"""

BUILD_BAT = r"""@echo off
REM Skeleton-Build für das englische Buch (nutzt 1_sceleton.py)

cd /d "%~dp0"
py 1_sceleton.py
if errorlevel 1 (
  echo [ERROR] 1_sceleton.py ist fehlgeschlagen.
  exit /b 1
)

pdflatex -interaction=nonstopmode T0_Book_En_sceleton.tex
"""

README_TXT = """# English Book Skeleton

This directory contains a skeleton setup for building the unified English T0 book.

## Files

- 1_sceleton.py
  Placeholder script. Will be filled with logic to:
  - extract content between \\begin{document} and \\end{document},
  - strip document-local headers,
  - normalize labels and references,
  - replace unicode symbols,
  - generate chapters_en_sceleton/*.tex,
  - generate T0_Book_En_sceleton.tex.

- T0_Book_En_sceleton.tex
  Minimal book preamble. Intended to include generated chapter files.

- build_book_sceleton.bat
  Simple Windows batch to:
    1. run 'py 1_sceleton.py',
    2. run 'pdflatex' on 'T0_Book_En_sceleton.tex'.

- chapters_en_sceleton/
  Target directory for generated chapter files.

## Next steps

1. Run:

   cd 2\\tex
   py setup_sceleton.py

2. Commit and push the newly created files and directories.

3. Copilot will then fill '1_sceleton.py' with the actual transformation logic,
   and use 'T0_Book_En_sceleton.tex' as the main book file for the unified English book.
"""

# Leere (oder minimale) Dateien, die als "Korsett" dienen
FILES = {
    BASE / "1_sceleton.py": SKELETON_PY,
    BASE / "T0_Book_En_sceleton.tex": BOOK_TEX,
    BASE / "build_book_sceleton.bat": BUILD_BAT,
    BASE / "README_book_en_sceleton.txt": README_TXT,
}


def main() -> None:
    # Verzeichnisse anlegen
    for d in DIRS:
        d.mkdir(parents=True, exist_ok=True)

    # Dateien anlegen, falls sie noch nicht existieren
    for path, content in FILES.items():
        if path.exists():
            # Bestehende Dateien NICHT überschreiben
            continue
        path.write_text(content, encoding="utf-8")
        print(f"[CREATED] {path.relative_to(BASE)}")


if __name__ == "__main__":
    main()