#!/usr/bin/env python3
"""
Build complete book by extracting content from standalone documents.
"""
import os
import re
import sys

def extract_body_content(filepath):
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
            # Fix common issues
            body = re.sub(r'\\section\*?\{', r'\\section{', body)
            body = re.sub(r'\\subsection\*?\{', r'\\subsection{', body)
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
            title = re.sub(r'\\\\', ' ', title)  # Replace \\ with space
            title = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r'\1', title)  # Remove commands like \textbf{...}
            title = re.sub(r'\\[a-zA-Z]+', '', title)  # Remove standalone commands
            title = re.sub(r'[{}]', '', title)  # Remove remaining braces
            title = re.sub(r'\s+', ' ', title).strip()  # Normalize whitespace
            # Limit length
            if len(title) > 100:
                title = title[:97] + "..."
            return title
        
        # Fallback to filename
        basename = os.path.basename(filepath)
        name = os.path.splitext(basename)[0]
        # Clean up name
        name = name.replace('_De', '').replace('_En', '')
        name = name.replace('_', ' ').replace('-', ' ')
        return name
    except:
        return os.path.basename(filepath)

# German chapters in order
CHAPTERS_DE = [
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

# English chapters
CHAPTERS_EN = [
    "completed/T0_Introduction_En.tex",
    "completed/reise_En.tex",
    "completed/T0_Grundlagen_En.tex",
    "completed/T0_Modell_Uebersicht_En.tex",
    "completed/T0_7-fragen-3_En.tex",
    "completed/Hannah_En.tex",
    "completed/Markov_En.tex",
    "completed/T0-Theory-vs-Synergetics_En.tex",
    "completed/T0_threeclock_En.tex",
    "completed/T0_penrose_En.tex",
    "completed/T0_peratt_En.tex",
    "completed/T0_Analyse_MNRAS_Widerlegung_En.tex",
    "completed/T0vsESM_ConceptualAnalysis_En.tex",
    "completed/T0_Teilchenmassen_En.tex",
    "completed/Teilchenmassen_En.tex",
    "completed/T0_tm-erweiterung-x6_En.tex",
    "completed/T0_Neutrinos_En.tex",
    "completed/detailierte_formel_leptonen_anemal_En.tex",
    "completed/neutrino-Formel_En.tex",
    "completed/T0_koide-formel-3_En.tex",
    "completed/T0_xi-und-e_En.tex",
    "completed/T0_xi_ursprung_En.tex",
    "completed/xi_parmater_partikel_En.tex",
    "completed/T0_SI_En.tex",
    "completed/T0_nat-si_En.tex",
    "completed/NatEinheitenSystematikEn.tex",
    "completed/parameterherleitung_En.tex",
    "completed/T0_Vollstaendige_Berchnungen_En.tex",
    "completed/T0_verhaeltnis-absolut_En.tex",
    "completed/RelokativesZahlensystemEn.tex",
    "completed/E-mc2_En.tex",
    "completed/T0_Energie_En.tex",
    "completed/Formeln_Energiebasiert_En.tex",
    "completed/Bewegungsenergie_En.tex",
    "completed/T0_Feinstruktur_En.tex",
    "completed/FeinstrukturkonstanteEn.tex",
    "completed/137_En.tex",
    "completed/musical-spiral-137-En.tex",
    "completed/ResolvingTheConstantsAlfaEn.tex",
    "completed/T0_Gravitationskonstante_En.tex",
    "completed/gravitationskonstante_En.tex",
    "completed/gravitationskonstnte_En.tex",
    "completed/TempEinheitenCMBEn.tex",
    "completed/T0_Kosmologie_En.tex",
    "completed/cosmic_En.tex",
    "completed/T0_Geometrische_Kosmologie_En.tex",
    "completed/redshift_deflection_En.tex",
    "completed/Casimir_En.tex",
    "completed/Zwei-Dipole-CMB_En.tex",
    "completed/Ho_En.tex",
    "completed/T0_Anomale_Magnetische_Momente_En.tex",
    "completed/T0_Anomale-g2-6_En.tex",
    "completed/T0_Anomale-g2-9_En.tex",
    "completed/T0_lagrndian_En.tex",
    "completed/LagrandianVergleichEn.tex",
    "completed/lagrandian-einfachEn.tex",
    "completed/Notwendigkeit_zwei_lagrange_En.tex",
    "completed/diracEn.tex",
    "completed/diracVereinfachtEn.tex",
    "completed/T0_QM-QFT-RT_En.tex",
    "completed/QM-testenEn.tex",
    "completed/Bell_En.tex",
    "completed/QM-DetrmisticEn.tex",
    "completed/NoGoEn.tex",
    "completed/Mathematische_struktur_En.tex",
    "completed/systemEn.tex",
    "completed/QM_En.tex",
    "completed/QFT_En.tex",
    "completed/T0-QFT-ML_Addendum_En.tex",
    "completed/scheinbar_instantan_En.tex",
    "completed/T0_QAT_En.tex",
    "completed/T0_QM-optimierung_En.tex",
    "completed/Unit Charge_En.tex",
    "completed/MathZeitMasseLagrangeEn.tex",
    "completed/T0_g2-erweiterung-4_En.tex",
    "completed/Amper_Low_En.tex",
    "completed/DerivationVonBetaEn.tex",
    "completed/T0_freqeunz_En.tex",
    "completed/universale-ableitung_En.tex",
    "completed/T0_umkehrung_En.tex",
    "completed/DynMassePhotonenNichtlokalEn.tex",
    "completed/Zeit_En.tex",
    "completed/Zeit-konstant_En.tex",
    "completed/RSA_En.tex",
    "completed/RSAtest_En.tex",
    "completed/EliminationOfMassEn.tex",
    "completed/Elimination_Of_Mass_Dirac_LagEn.tex",
    "completed/Elimination_Of_Mass_Dirac_TabelleEn.tex",
    "completed/HdokumentEn.tex",
    "completed/Moll_CandelaEn.tex",
    "completed/T0_netze_En.tex",
    "completed/ParameterSystemdipendentEn.tex",
    "completed/Zusammenfassung_En.tex",
    "completed/T0_Dokumentenübersicht_En.tex",
    "completed/T0_Bibliography_En.tex",
]

def build_book(lang='De'):
    """Build complete book for given language."""
    chapters = CHAPTERS_DE if lang == 'De' else CHAPTERS_EN
    cover_image = f"T0_deckblatt_{lang}.png"
    
    # Book header
    if lang == 'De':
        book_content = r"""\documentclass[a4paper,11pt]{book}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[ngerman]{babel}
\usepackage{graphicx}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{hyperref}
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

\setlength{\headheight}{14pt}

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

\geometry{margin=2.5cm}
\pagestyle{fancy}
\fancyhead{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[RE]{\leftmark}
\fancyhead[LO]{\rightmark}

\title{\Huge\textbf{T0-Theorie}\\[0.5cm]\Large Zeit-Masse-Dualität\\[0.3cm]\normalsize Alle Naturkonstanten aus einer Zahl: $\alpha \approx 1/137$}
\author{Johann Pascher}
\date{2024}

\begin{document}

% Cover page with image
\begin{titlepage}
\centering
"""
        book_content += f"\\includegraphics[width=\\textwidth,height=\\textheight,keepaspectratio]{{{cover_image}}}\n"
        book_content += r"""\end{titlepage}

\frontmatter
\tableofcontents

\mainmatter

"""
    else:
        book_content = r"""\documentclass[a4paper,11pt]{book}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[english]{babel}
\usepackage{graphicx}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{hyperref}
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

\setlength{\headheight}{14pt}

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

\geometry{margin=2.5cm}
\pagestyle{fancy}
\fancyhead{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[RE]{\leftmark}
\fancyhead[LO]{\rightmark}

\title{\Huge\textbf{T0-Theory}\\[0.5cm]\Large Time-Mass-Duality\\[0.3cm]\normalsize All Natural Constants from One Number: $\alpha \approx 1/137$}
\author{Johann Pascher}
\date{2024}

\begin{document}

% Cover page with image
\begin{titlepage}
\centering
"""
        book_content += f"\\includegraphics[width=\\textwidth,height=\\textheight,keepaspectratio]{{{cover_image}}}\n"
        book_content += r"""\end{titlepage}

\frontmatter
\tableofcontents

\mainmatter

"""
    
    # Add chapters
    chapter_num = 0
    for chapter_path in chapters:
        if os.path.exists(chapter_path):
            chapter_num += 1
            title = get_chapter_title(chapter_path)
            body = extract_body_content(chapter_path)
            
            if body:
                book_content += f"\n\\chapter{{{title}}}\n\\label{{ch:{chapter_num}}}\n\n"
                book_content += body + "\n\n\\clearpage\n"
                print(f"  Added chapter {chapter_num}: {title}")
            else:
                print(f"  Skipped (no body): {chapter_path}")
        else:
            print(f"  Not found: {chapter_path}")
    
    # Book footer
    book_content += r"""
\backmatter

\end{document}
"""
    
    # Write book file
    output_file = f"T0_Complete_Book_Full_{lang}.tex"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(book_content)
    
    print(f"\nBook written to: {output_file}")
    print(f"Total chapters: {chapter_num}")
    return output_file

if __name__ == "__main__":
    lang = sys.argv[1] if len(sys.argv) > 1 else 'De'
    build_book(lang)
