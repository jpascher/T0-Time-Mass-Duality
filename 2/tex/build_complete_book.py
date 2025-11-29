#!/usr/bin/env python3
"""
Build complete book by extracting content from standalone documents.
Preserves abstract sections with proper document titles.
"""
import os
import re
import sys

def extract_body_content(filepath, chapter_num=0):
    """Extract content between \\begin{document} and \\end{document}."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        # Find document body
        match = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', content, re.DOTALL)
        if match:
            body = match.group(1).strip()
            # Remove \maketitle if present
            body = re.sub(r'\\maketitle\s*', '', body)
            # Remove title commands that might break chapter
            body = re.sub(r'\\title\{[^}]*\}\s*', '', body)
            body = re.sub(r'\\author\{[^}]*\}\s*', '', body)
            body = re.sub(r'\\date\{[^}]*\}\s*', '', body)
            
            # Remove tableofcontents from chapters (only main TOC should exist)
            body = re.sub(r'\\tableofcontents\s*', '', body)
            
            # DO NOT prefix labels/refs - keep original references working within documents
            # The "multiply defined labels" warning is acceptable for a book compilation
            
            return body
        return None
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

def get_chapter_title(filepath):
    """Extract title from document."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        # Try to find title
        match = re.search(r'\\title\{([^}]+)\}', content)
        if match:
            title = match.group(1)
            # Clean up title - remove LaTeX formatting
            title = re.sub(r'\\\\', ' ', title)
            title = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r'\1', title)
            title = re.sub(r'\\[a-zA-Z]+', '', title)
            title = re.sub(r'[{}]', '', title)
            title = re.sub(r'\s+', ' ', title).strip()
            if len(title) > 100:
                title = title[:97] + "..."
            return title
        
        # Fallback to filename
        basename = os.path.basename(filepath)
        name = os.path.splitext(basename)[0]
        name = name.replace('_De', '').replace('_En', '')
        name = name.replace('_', ' ').replace('-', ' ')
        return name
    except:
        return os.path.basename(filepath)

# German chapters in order - Abstract first
CHAPTERS_DE = [
    "completed/T0_Book_Abstract_De.tex",
    "completed/T0_Introduction_De.tex",
    "completed/reise_De.tex",
    "completed/T0_Grundlagen_De.tex",
    "completed/T0_Modell_Uebersicht_De.tex",
    "completed/T0_7-fragen-3_De.tex",
    "completed/Hannah_De.tex",
    "completed/Markov_De.tex",
    "completed/T0-Theory-vs-Synergetics_De.tex",
    "completed/T0_threeclock_De.tex",
    "completed/T0_penrose_De.tex",
    "completed/T0_peratt_De.tex",
    "completed/T0_Analyse_MNRAS_Widerlegung_De.tex",
    "completed/T0vsESM_ConceptualAnalysis_De.tex",
    "completed/T0_Teilchenmassen_De.tex",
    "completed/Teilchenmassen_De.tex",
    "completed/T0_tm-erweiterung-x6_De.tex",
    "completed/T0_Neutrinos_De.tex",
    "completed/detailierte_formel_leptonen_anemal_De.tex",
    "completed/neutrino-Formel_De.tex",
    "completed/T0_koide-formel-3_De.tex",
    "completed/T0_xi-und-e_De.tex",
    "completed/T0_xi_ursprung_De.tex",
    "completed/xi_parmater_partikel_De.tex",
    "completed/T0_SI_De.tex",
    "completed/T0_nat-si_De.tex",
    "completed/NatEinheitenSystematikDe.tex",
    "completed/parameterherleitung_De.tex",
    "completed/T0_Vollstaendige_Berchnungen_De.tex",
    "completed/T0_verhaeltnis-absolut_De.tex",
    "completed/RelokativesZahlensystemDe.tex",
    "completed/E-mc2_De.tex",
    "completed/T0_Energie_De.tex",
    "completed/Formeln_Energiebasiert_De.tex",
    "completed/Bewegungsenergie_De.tex",
    "completed/T0_Feinstruktur_De.tex",
    "completed/FeinstrukturkonstanteDe.tex",
    "completed/137_De.tex",
    "completed/musical-spiral-137-De.tex",
    "completed/ResolvingTheConstantsAlfaDe.tex",
    "completed/T0_Gravitationskonstante_De.tex",
    "completed/gravitationskonstante_De.tex",
    "completed/gravitationskonstnte_De.tex",
    "completed/TempEinheitenCMBDe.tex",
    "completed/T0_Kosmologie_De.tex",
    "completed/cosmic_De.tex",
    "completed/T0_Geometrische_Kosmologie_De.tex",
    "completed/redshift_deflection_De.tex",
    "completed/Casimir_De.tex",
    "completed/Zwei-Dipole-CMB_De.tex",
    "completed/Ho_De.tex",
    "completed/T0_Anomale_Magnetische_Momente_De.tex",
    "completed/T0_Anomale-g2-6_De.tex",
    "completed/T0_Anomale-g2-9_De.tex",
    "completed/T0_lagrndian_De.tex",
    "completed/LagrandianVergleichDe.tex",
    "completed/lagrandian-einfachDe.tex",
    "completed/Notwendigkeit_zwei_lagrange_De.tex",
    "completed/diracDe.tex",
    "completed/diracVereinfachtDe.tex",
    "completed/T0_QM-QFT-RT_De.tex",
    "completed/QM-testenDe.tex",
    "completed/Bell_De.tex",
    "completed/QM-DetrmisticDe.tex",
    "completed/NoGoDe.tex",
    "completed/Mathematische_struktur_De.tex",
    "completed/systemDe.tex",
    "completed/QM_De.tex",
    "completed/QFT_De.tex",
    "completed/T0-QFT-ML_Addendum_De.tex",
    "completed/scheinbar_instantan_De.tex",
    "completed/T0_QAT_De.tex",
    "completed/T0_QM-optimierung_De.tex",
    "completed/Unit Charge_De.tex",
    "completed/MathZeitMasseLagrangeDe.tex",
    "completed/T0_g2-erweiterung-4_De.tex",
    "completed/Amper_Low_De.tex",
    "completed/DerivationVonBetaDe.tex",
    "completed/T0_freqeunz_De.tex",
    "completed/universale-ableitung_De.tex",
    "completed/T0_umkehrung_De.tex",
    "completed/DynMassePhotonenNichtlokalDe.tex",
    "completed/Zeit_De.tex",
    "completed/Zeit-konstant_De.tex",
    "completed/RSA_De.tex",
    "completed/RSAtest_De.tex",
    "completed/EliminationOfMassDe.tex",
    "completed/Elimination_Of_Mass_Dirac_LagDe.tex",
    "completed/Elimination_Of_Mass_Dirac_TabelleDe.tex",
    "completed/HdokumentDe.tex",
    "completed/Moll_CandelaDe.tex",
    "completed/T0_netze_De.tex",
    "completed/ParameterSystemdipendentDe.tex",
    "completed/Zusammenfassung_De.tex",
    "completed/T0_Dokumentenübersicht_De.tex",
    "completed/T0_Bibliography_De.tex",
]

CHAPTERS_EN = [ch.replace('_De.tex', '_En.tex').replace('De.tex', 'En.tex') for ch in CHAPTERS_DE]

def write_book_header_de():
    return r'''\documentclass[a4paper,11pt]{book}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[ngerman]{babel}
\usepackage{graphicx}
\usepackage{amsmath,amssymb,amsthm}
\usepackage[pdfusetitle,colorlinks=true,linkcolor=blue,urlcolor=blue,citecolor=blue]{hyperref}
\usepackage{geometry}
\usepackage{fancyhdr}
\usepackage{tcolorbox}
\tcbuselibrary{breakable,skins}
\usepackage{xcolor}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage{multirow}
\usepackage{caption}
\usepackage{float}
\usepackage{enumitem}
\usepackage{tikz}
\usepackage{url}

\setlength{\headheight}{14pt}

% German hyphenation settings for long words
\tolerance=1000
\emergencystretch=3em
\hyphenpenalty=50
\exhyphenpenalty=50
\sloppy

% Suppress hyperref warnings in PDF strings
\pdfstringdefDisableCommands{%
  \def\\{ }%
  \def\texttt#1{#1}%
  \def\textsf#1{#1}%
  \def\textbf#1{#1}%
  \def\textit#1{#1}%
}

% T0 specific commands
\newcommand{\Tzero}{T_0}
\newcommand{\betaT}{\beta_T}
\newcommand{\xipar}{\xi}
\newcommand{\alphaEM}{\alpha_{\text{EM}}}
\providecommand{\meff}{m_{\text{eff}}}
\providecommand{\Tfield}{T}
\providecommand{\Lp}{L_P}
\providecommand{\Tp}{T_P}
\providecommand{\Mp}{M_P}
\providecommand{\Ep}{E_P}
\providecommand{\hbar}{\hslash}
\providecommand{\kB}{k_B}

% Colors
\definecolor{theoremcolor}{RGB}{0,100,150}
\definecolor{definitioncolor}{RGB}{0,100,50}
\definecolor{t0blue}{RGB}{0,102,204}
\definecolor{boxgray}{RGB}{128,128,128}
\definecolor{gold}{RGB}{255,215,0}
\definecolor{tocblue}{RGB}{0,51,102}

% Theorem environments
\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[chapter]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Beispiel}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Bemerkung}

% tcolorbox environments
\newtcolorbox{keyresult}[1][Schlüsselergebnis]{colback=blue!5,colframe=blue!75!black,title=#1,breakable}
\newtcolorbox{important}[1][Wichtig]{colback=red!5,colframe=red!75!black,title=#1,breakable}
\newtcolorbox{note}[1][Hinweis]{colback=yellow!5,colframe=yellow!75!black,title=#1,breakable}
\newtcolorbox{summary}[1][Zusammenfassung]{colback=green!5,colframe=green!75!black,title=#1,breakable}
\newtcolorbox{foundation}[1][Grundlage]{colback=gray!5,colframe=gray!75!black,title=#1,breakable}
\newtcolorbox{alternative}[1][Alternative]{colback=orange!5,colframe=orange!75!black,title=#1,breakable}
\newtcolorbox{interpretation}[1][Interpretation]{colback=purple!5,colframe=purple!75!black,title=#1,breakable}
\newtcolorbox{explanation}[1][Erklärung]{colback=cyan!5,colframe=cyan!75!black,title=#1,breakable}
\newtcolorbox{category}[1][Kategorie]{colback=brown!5,colframe=brown!75!black,title=#1,breakable}
\newtcolorbox{key}[1][Schlüssel]{colback=blue!5,colframe=blue!75!black,title=#1,breakable}
\newtcolorbox{technical}[1][Technisch]{colback=gray!5,colframe=gray!75!black,title=#1,breakable}
\newtcolorbox{proof_step}[1][Beweisschritt]{colback=yellow!5,colframe=yellow!75!black,title=#1,breakable}
\newtcolorbox{experimental}[1][Experimentell]{colback=green!5,colframe=green!75!black,title=#1,breakable}

\geometry{margin=2.5cm}
\pagestyle{fancy}
\fancyhead{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[RE]{\nouppercase{\leftmark}}
\fancyhead[LO]{\nouppercase{\rightmark}}

\title{\Huge\textbf{T0-Theorie}\\[0.5cm]\Large Zeit-Masse-Dualität\\[0.3cm]\normalsize Alle Naturkonstanten aus einer Zahl}
\author{Johann Pascher}
\date{2024}

\begin{document}

% Cover page with image
\begin{titlepage}
\centering
\includegraphics[width=\textwidth,height=\textheight,keepaspectratio]{T0_deckblatt_De.png}
\end{titlepage}

\frontmatter

% ABSTRAKT
\chapter*{Abstrakt}
\addcontentsline{toc}{chapter}{Abstrakt}

Die T0-Theorie (Zeit-Masse-Dualität) stellt einen fundamentalen Paradigmenwechsel in der theoretischen Physik dar. Das zentrale Ergebnis dieser Arbeit ist die Erkenntnis, dass \textbf{alle natürlichen Konstanten und physikalischen Parameter aus einer einzigen dimensionslosen Zahl abgeleitet werden können}: der universellen geometrischen Konstante
\[
\xi = \frac{4}{3} \times 10^{-4}.
\]

\begin{keyresult}[Zentrales Theorem der T0-Theorie]
Alle physikalischen Konstanten -- Gravitationskonstante $G$, Planck-Konstante $\hbar$, Lichtgeschwindigkeit $c$, Elementarladung $e$ sowie alle Teilchenmassen und Kopplungskonstanten -- können mathematisch aus der universellen geometrischen Konstante $\xi$ abgeleitet werden.

Aus $\xi$ folgt die Feinstrukturkonstante:
\[
\alpha = f_\alpha(\xi) \approx \frac{1}{137.035999084}
\]
\end{keyresult}

Diese Sammlung von über 200 wissenschaftlichen Dokumenten entwickelt systematisch eine vollständige physikalische Theorie, die Quantenmechanik, Relativität und Kosmologie vereinheitlicht -- basierend auf dem Prinzip der absoluten Zeit $T_0$ und der intrinsischen Zeit-Feld-Masse-Beziehung.

\vspace{1em}
\begin{center}
\textit{``Die Natur verwendet nur die längsten Fäden, um ihre Muster zu weben, sodass jedes kleine Stück ihres Gewebes die Organisation des gesamten Wandteppichs offenbart.''} -- Richard Feynman
\end{center}

% INHALTSVERZEICHNIS mit blauem Text
\clearpage
{\color{tocblue}
\tableofcontents
}

\mainmatter

'''

def write_book_header_en():
    return r'''\documentclass[a4paper,11pt]{book}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[english]{babel}
\usepackage{graphicx}
\usepackage{amsmath,amssymb,amsthm}
\usepackage[pdfusetitle,colorlinks=true,linkcolor=blue,urlcolor=blue,citecolor=blue]{hyperref}
\usepackage{geometry}
\usepackage{fancyhdr}
\usepackage{tcolorbox}
\tcbuselibrary{breakable,skins}
\usepackage{xcolor}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage{multirow}
\usepackage{caption}
\usepackage{float}
\usepackage{enumitem}
\usepackage{tikz}
\usepackage{url}

\setlength{\headheight}{14pt}

% Suppress hyperref warnings in PDF strings
\pdfstringdefDisableCommands{%
  \def\\{ }%
  \def\texttt#1{#1}%
  \def\textsf#1{#1}%
  \def\textbf#1{#1}%
  \def\textit#1{#1}%
}

% T0 specific commands
\newcommand{\Tzero}{T_0}
\newcommand{\betaT}{\beta_T}
\newcommand{\xipar}{\xi}
\newcommand{\alphaEM}{\alpha_{\text{EM}}}
\providecommand{\meff}{m_{\text{eff}}}
\providecommand{\Tfield}{T}
\providecommand{\Lp}{L_P}
\providecommand{\Tp}{T_P}
\providecommand{\Mp}{M_P}
\providecommand{\Ep}{E_P}
\providecommand{\hbar}{\hslash}
\providecommand{\kB}{k_B}

% Colors
\definecolor{theoremcolor}{RGB}{0,100,150}
\definecolor{definitioncolor}{RGB}{0,100,50}
\definecolor{t0blue}{RGB}{0,102,204}
\definecolor{boxgray}{RGB}{128,128,128}
\definecolor{gold}{RGB}{255,215,0}
\definecolor{tocblue}{RGB}{0,51,102}

% Theorem environments
\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[chapter]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}

% tcolorbox environments
\newtcolorbox{keyresult}[1][Key Result]{colback=blue!5,colframe=blue!75!black,title=#1,breakable}
\newtcolorbox{important}[1][Important]{colback=red!5,colframe=red!75!black,title=#1,breakable}
\newtcolorbox{note}[1][Note]{colback=yellow!5,colframe=yellow!75!black,title=#1,breakable}
\newtcolorbox{summary}[1][Summary]{colback=green!5,colframe=green!75!black,title=#1,breakable}
\newtcolorbox{foundation}[1][Foundation]{colback=gray!5,colframe=gray!75!black,title=#1,breakable}
\newtcolorbox{alternative}[1][Alternative]{colback=orange!5,colframe=orange!75!black,title=#1,breakable}
\newtcolorbox{interpretation}[1][Interpretation]{colback=purple!5,colframe=purple!75!black,title=#1,breakable}
\newtcolorbox{explanation}[1][Explanation]{colback=cyan!5,colframe=cyan!75!black,title=#1,breakable}
\newtcolorbox{category}[1][Category]{colback=brown!5,colframe=brown!75!black,title=#1,breakable}
\newtcolorbox{key}[1][Key]{colback=blue!5,colframe=blue!75!black,title=#1,breakable}
\newtcolorbox{technical}[1][Technical]{colback=gray!5,colframe=gray!75!black,title=#1,breakable}
\newtcolorbox{proof_step}[1][Proof Step]{colback=yellow!5,colframe=yellow!75!black,title=#1,breakable}
\newtcolorbox{experimental}[1][Experimental]{colback=green!5,colframe=green!75!black,title=#1,breakable}

\geometry{margin=2.5cm}
\pagestyle{fancy}
\fancyhead{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[RE]{\nouppercase{\leftmark}}
\fancyhead[LO]{\nouppercase{\rightmark}}

\title{\Huge\textbf{T0-Theory}\\[0.5cm]\Large Time-Mass Duality\\[0.3cm]\normalsize All Natural Constants from One Number}
\author{Johann Pascher}
\date{2024}

\begin{document}

% Cover page with image
\begin{titlepage}
\centering
\includegraphics[width=\textwidth,height=\textheight,keepaspectratio]{T0_deckblatt_En.png}
\end{titlepage}

\frontmatter

% ABSTRACT
\chapter*{Abstract}
\addcontentsline{toc}{chapter}{Abstract}

The T0-Theory (Time-Mass Duality) represents a fundamental paradigm shift in theoretical physics. The central result of this work is the recognition that \textbf{all natural constants and physical parameters can be derived from a single dimensionless number}: the universal geometric constant
\[
\xi = \frac{4}{3} \times 10^{-4}.
\]

\begin{keyresult}[Central Theorem of T0-Theory]
All physical constants -- gravitational constant $G$, Planck constant $\hbar$, speed of light $c$, elementary charge $e$ as well as all particle masses and coupling constants -- can be mathematically derived from the universal geometric constant $\xi$.

From $\xi$ follows the fine structure constant:
\[
\alpha = f_\alpha(\xi) \approx \frac{1}{137.035999084}
\]
\end{keyresult}

This collection of over 200 scientific documents systematically develops a complete physical theory that unifies quantum mechanics, relativity and cosmology -- based on the principle of absolute time $T_0$ and the intrinsic time-field-mass relationship.

\vspace{1em}
\begin{center}
\textit{``Nature uses only the longest threads to weave her patterns, so that each small piece of her fabric reveals the organization of the entire tapestry.''} -- Richard Feynman
\end{center}

% TABLE OF CONTENTS with blue text
\clearpage
{\color{tocblue}
\tableofcontents
}

\mainmatter

'''

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 build_complete_book.py [De|En]")
        sys.exit(1)
    
    lang = sys.argv[1]
    
    if lang == "De":
        chapters = CHAPTERS_DE
        header = write_book_header_de()
        output_file = "T0_Complete_Book_Full_De.tex"
    elif lang == "En":
        chapters = CHAPTERS_EN
        header = write_book_header_en()
        output_file = "T0_Complete_Book_Full_En.tex"
    else:
        print(f"Unknown language: {lang}")
        sys.exit(1)
    
    # Start building the book
    book_content = header
    
    chapter_num = 0
    for chapter_path in chapters:
        if not os.path.exists(chapter_path):
            print(f"  Skipping (not found): {chapter_path}")
            continue
        
        chapter_num += 1
        title = get_chapter_title(chapter_path)
        body = extract_body_content(chapter_path, chapter_num)
        
        if body:
            # Add chapter with title
            book_content += f"\n\\chapter{{{title}}}\n"
            book_content += f"\\label{{ch:{chapter_num}}}\n\n"
            book_content += body
            book_content += "\n\\clearpage\n"
            print(f"  Added chapter {chapter_num}: {title[:80]}...")
        else:
            print(f"  Warning: Could not extract content from {chapter_path}")
    
    # End document
    book_content += "\n\\end{document}\n"
    
    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(book_content)
    
    print(f"\nBook written to: {output_file}")
    print(f"Total chapters: {chapter_num}")

if __name__ == "__main__":
    main()
