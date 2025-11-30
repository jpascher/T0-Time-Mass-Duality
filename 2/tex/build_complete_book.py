#!/usr/bin/env python3
"""
Build complete book - minimal changes: remove documentclass, begin/end document.
Uses T0_preamble for all definitions.

WICHTIG / IMPORTANT:
--------------------
Dieses Skript verarbeitet ALLE LaTeX-Dokumente aus dem Verzeichnis completed/
und erzeugt T0_Complete_Book_Full_De.tex bzw. T0_Complete_Book_Full_En.tex.

Die Kapitelauswahl für kürzere Buchversionen erfolgt NICHT in diesem Skript,
sondern direkt in den entsprechenden .tex-Dateien:
  - T0_Complete_Book_De.tex  (50 Kapitel - manuell erstellt)
  - T0_Complete_Book_En.tex  (49 Kapitel - manuell erstellt)

Um die Kapitelauswahl zu ändern, bearbeiten Sie die .tex-Datei direkt.
Das Skript bleibt für die Full-Versionen unverändert.

This script processes ALL LaTeX documents from the completed/ directory
and generates T0_Complete_Book_Full_De.tex or T0_Complete_Book_Full_En.tex.

Chapter selection for shorter book versions is NOT done in this script,
but directly in the corresponding .tex files:
  - T0_Complete_Book_De.tex  (50 chapters - manually created)
  - T0_Complete_Book_En.tex  (49 chapters - manually created)

To change chapter selection, edit the .tex file directly.
The script remains unchanged for Full versions.
"""
import os
import re
import sys

def extract_body_content(filepath):
    """Extract content between \begin{document} and \end{document}."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        match = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', content, re.DOTALL)
        if match:
            body = match.group(1).strip()
            # Remove only maketitle and tableofcontents
            body = re.sub(r'\\maketitle\s*', '', body)
            body = re.sub(r'\\tableofcontents\s*', '', body)
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
        
        match = re.search(r'\\title\{([^}]+)\}', content)
        if match:
            title = match.group(1)
            # Replace common Greek letters with text
            title = re.sub(r'\$\\xi\$', 'xi', title)
            title = re.sub(r'\$\\alpha\$', 'alpha', title)
            title = re.sub(r'\$\\beta\$', 'beta', title)
            title = re.sub(r'\$e\$', 'e', title)
            # Remove \\[...] vertical spacing commands like \\[0.5em]
            title = re.sub(r'\\\\\[[^\]]*\]', ' ', title)
            title = re.sub(r'\\\\', ' ', title)
            title = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r'\1', title)
            title = re.sub(r'\\[a-zA-Z]+', '', title)
            title = re.sub(r'\[[^\]]*\]', '', title)  # Remove remaining [...] 
            title = re.sub(r'\$[^$]*\$', '', title)  # Remove remaining math mode
            title = re.sub(r'[{}]', '', title)
            title = re.sub(r'\s+', ' ', title).strip()
            # Remove date/percentage info like "(November 2025, <3%)"
            title = re.sub(r'\s*\([^)]*20\d\d[^)]*\)', '', title)
            title = re.sub(r'\s*\([^)]*%[^)]*\)', '', title)
            if len(title) > 60:
                title = title[:57] + "..."
            return title
        
        basename = os.path.basename(filepath)
        return basename.replace('.tex', '').replace('_', ' ')
    except:
        return os.path.basename(filepath).replace('.tex', '')

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
    "completed/EliminationOfMassDe.tex",
    "completed/Elimination_Of_Mass_Dirac_LagDe.tex",
    "completed/Elimination_Of_Mass_Dirac_TabelleDe.tex",
    "completed/RSA_De.tex",
    "completed/RSAtest_De.tex",
    "completed/QM-Detrmistic_p_De.tex",
    "completed/HdokumentDe.tex",
    "completed/Moll_CandelaDe.tex",
    "completed/T0_netze_De.tex",
    "completed/ParameterSystemdipendentDe.tex",
    "completed/Zusammenfassung_De.tex",
    "completed/T0_Dokumentenübersicht_De.tex",
    "completed/T0_Bibliography_De.tex",
]

def write_book(lang='De'):
    chapters = CHAPTERS_DE if lang == 'De' else [ch.replace('_De.tex', '_En.tex').replace('De.tex', 'En.tex') for ch in CHAPTERS_DE]
    preamble = 'completed/T0_preamble_De' if lang == 'De' else 'completed/T0_preamble_En'
    cover = 'T0_deckblatt_De.png' if lang == 'De' else 'T0_deckblatt_En.png'
    toc_title = 'Inhaltsverzeichnis' if lang == 'De' else 'Table of Contents'
    
    output = f"T0_Complete_Book_Full_{lang}.tex"
    
    with open(output, 'w', encoding='utf-8') as f:
        # Minimal book preamble - use existing T0_preamble
        f.write(r'''\documentclass[a4paper,11pt]{book}
\input{''' + preamble + r'''}

% Define abstract for book class (not defined in book)
\newenvironment{abstract}{\begin{quote}\small}{\end{quote}}

% Short headers for book
\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[RE]{\scriptsize\nouppercase{\leftmark}}
\fancyhead[LO]{\scriptsize\nouppercase{\rightmark}}
\fancyfoot[C]{\scriptsize T0-Theorie}
\renewcommand{\chaptermark}[1]{\markboth{\thechapter.\ #1}{}}
\renewcommand{\sectionmark}[1]{\markright{\thesection.\ #1}}

\fancypagestyle{plain}{\fancyhf{}\fancyfoot[C]{\thepage}\renewcommand{\headrulewidth}{0pt}}

\title{T0-Theorie}
\author{Johann Pascher}
\date{2024}

\begin{document}

% Cover
\thispagestyle{empty}
\begin{center}
\vspace*{2cm}
\includegraphics[width=0.9\textwidth]{''' + cover + r'''}
\end{center}
\clearpage

% TOC
\tableofcontents
\clearpage

''')
        
        # GitHub base URL for original PDF documents
        github_base = "https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/"
        
        chapter_num = 0
        for chap_file in chapters:
            if not os.path.exists(chap_file):
                print(f"  Skipping (not found): {chap_file}")
                continue
            
            body = extract_body_content(chap_file)
            if body:
                title = get_chapter_title(chap_file)
                chapter_num += 1
                
                # Get original filename and convert to PDF (without completed/ prefix)
                orig_filename = os.path.basename(chap_file)
                pdf_filename = orig_filename.replace('.tex', '.pdf')
                github_url = github_base + pdf_filename
                
                f.write(f"\n\\chapter{{{title}}}\n")
                # Add link to original PDF document on GitHub
                f.write(f"\\noindent\\small\\textit{{Original: }}\\url{{{github_url}}}\n\n")
                f.write(body)
                f.write("\n\\clearpage\n")
                print(f"  Added chapter {chapter_num}: {title[:70]}...")
        
        f.write("\n\\end{document}\n")
    
    print(f"\nBook written to: {output}")
    print(f"Total chapters: {chapter_num}")

if __name__ == "__main__":
    lang = sys.argv[1] if len(sys.argv) > 1 else 'De'
    write_book(lang)
