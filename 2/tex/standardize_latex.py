#!/usr/bin/env python3
"""
standardize_latex.py - Standardisiert alle LaTeX-Dokumente im T0 Framework

Dieses Skript:
1. Konvertiert bestehende Dokumente zur Verwendung der einheitlichen Präambel
2. Fügt einheitliche Bibliographie-Referenzen hinzu
3. Behält dokumentspezifische Inhalte bei

Verwendung:
    python standardize_latex.py [--dry-run] [--verbose] [file.tex ...]
"""

import os
import re
import sys
import argparse
from pathlib import Path

# Standardmäßige Pfade
TEX_DIR = Path(__file__).parent
PREAMBLE_DE = "T0_Preamble_De.tex"
PREAMBLE_EN = "T0_Preamble_En.tex"
BIB_ITEMS_DE = "T0_Bibliography_Items_De.tex"
BIB_ITEMS_EN = "T0_Bibliography_Items_En.tex"

def detect_language(content):
    """Erkennt die Sprache des Dokuments basierend auf babel-Einstellungen."""
    if re.search(r'\\usepackage\[.*?ngerman.*?\]\{babel\}', content):
        return 'de'
    if re.search(r'\\usepackage\[.*?german.*?\]\{babel\}', content):
        return 'de'
    if re.search(r'\\usepackage\[.*?english.*?\]\{babel\}', content):
        return 'en'
    # Standard: Prüfe Dateinamen
    return None

def extract_document_class(content):
    """Extrahiert die documentclass-Deklaration."""
    match = re.search(r'\\documentclass(\[.*?\])?\{(\w+)\}', content)
    if match:
        options = match.group(1) or ''
        docclass = match.group(2)
        return f'\\documentclass{options}{{{docclass}}}'
    return '\\documentclass[12pt,a4paper]{article}'

def extract_title_author_date(content):
    """Extrahiert Titel, Autor und Datum aus dem Dokument."""
    title_match = re.search(r'\\title\{(.*?)\}', content, re.DOTALL)
    author_match = re.search(r'\\author\{(.*?)\}', content, re.DOTALL)
    date_match = re.search(r'\\date\{(.*?)\}', content, re.DOTALL)
    
    title = title_match.group(0) if title_match else None
    author = author_match.group(0) if author_match else None
    date = date_match.group(0) if date_match else '\\date{\\today}'
    
    return title, author, date

def extract_custom_commands(content):
    """Extrahiert dokumentspezifische benutzerdefinierte Befehle."""
    # Finde Befehle, die nicht in der Standard-Präambel enthalten sind
    custom_cmds = []
    
    # Suche nach \newcommand, \renewcommand, \newenvironment, etc.
    patterns = [
        r'\\newcommand\{\\[a-zA-Z]+\}.*',
        r'\\renewcommand\{\\[a-zA-Z]+\}.*',
        r'\\DeclareMathOperator.*',
        r'\\newtheorem\{[^}]+\}.*',
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, content)
        for m in matches:
            # Prüfe, ob dieser Befehl nicht bereits in der Standard-Präambel ist
            if not is_standard_command(m):
                custom_cmds.append(m)
    
    return custom_cmds

def is_standard_command(cmd):
    """Prüft, ob ein Befehl bereits in der Standard-Präambel enthalten ist."""
    standard_cmds = [
        'xipar', 'Tfield', 'Efield', 'betaT', 'alphaEM',
        'EP', 'lP', 'tP', 'mP', 'Tzero',
        'LCDM', 'OmegaLambda', 'OmegaDM',
        'GeV', 'MeV', 'eV', 'natunits',
        'keyresult', 'warning', 'formula', 'result', 'summary', 'important'
    ]
    for std_cmd in standard_cmds:
        if std_cmd in cmd:
            return True
    return False

def extract_document_body(content):
    """Extrahiert den Dokumentenkörper zwischen \\begin{document} und \\end{document}."""
    match = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ''

def extract_hypersetup(content):
    """Extrahiert dokumentspezifische hypersetup-Einstellungen."""
    match = re.search(r'\\hypersetup\{([^}]+(?:\{[^}]*\}[^}]*)*)\}', content, re.DOTALL)
    if match:
        hypersetup = match.group(1)
        # Extrahiere nur pdftitle und pdfsubject
        pdftitle = re.search(r'pdftitle\s*=\s*\{([^}]+)\}', hypersetup)
        pdfsubject = re.search(r'pdfsubject\s*=\s*\{([^}]+)\}', hypersetup)
        return pdftitle, pdfsubject
    return None, None

def standardize_document(filepath, dry_run=False, verbose=False):
    """
    Standardisiert ein einzelnes LaTeX-Dokument.
    
    Args:
        filepath: Pfad zur .tex-Datei
        dry_run: Wenn True, werden keine Änderungen geschrieben
        verbose: Wenn True, werden detaillierte Ausgaben gemacht
    
    Returns:
        True wenn erfolgreich, False sonst
    """
    filepath = Path(filepath)
    
    if verbose:
        print(f"\nVerarbeite: {filepath.name}")
    
    # Lese Inhalt
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Fehler beim Lesen von {filepath}: {e}")
        return False
    
    # Überspringe bereits standardisierte Dokumente
    if '% STANDARDIZED WITH T0_Preamble' in content:
        if verbose:
            print(f"  Bereits standardisiert, überspringe.")
        return True
    
    # Überspringe Präambel- und Bibliographie-Dateien
    if filepath.name.startswith('T0_Preamble') or filepath.name.startswith('T0_Bibliography'):
        if verbose:
            print(f"  Template-Datei, überspringe.")
        return True
    
    # Überspringe Chapter-Dateien (diese haben keine eigene Präambel)
    if 'chapters_en' in str(filepath) or '_ch.tex' in filepath.name:
        if verbose:
            print(f"  Chapter-Datei, überspringe.")
        return True
    
    # Erkenne Sprache
    lang = detect_language(content)
    if lang is None:
        # Versuche aus Dateinamen zu erkennen
        if '_De.' in filepath.name or filepath.name.endswith('De.tex'):
            lang = 'de'
        elif '_En.' in filepath.name or filepath.name.endswith('En.tex'):
            lang = 'en'
        else:
            if verbose:
                print(f"  Sprache nicht erkannt, überspringe.")
            return False
    
    preamble_file = PREAMBLE_DE if lang == 'de' else PREAMBLE_EN
    
    # Extrahiere Komponenten
    docclass = extract_document_class(content)
    title, author, date = extract_title_author_date(content)
    body = extract_document_body(content)
    pdftitle, pdfsubject = extract_hypersetup(content)
    
    if not body:
        if verbose:
            print(f"  Kein Dokumentenkörper gefunden, überspringe.")
        return False
    
    # Baue standardisiertes Dokument
    new_content = []
    new_content.append(f"% STANDARDIZED WITH T0_Preamble - {lang.upper()}")
    new_content.append(f"% Original file: {filepath.name}")
    new_content.append("")
    new_content.append(docclass)
    new_content.append("")
    new_content.append(f"% Einheitliche T0 Präambel laden")
    new_content.append(f"\\input{{{preamble_file.replace('.tex', '')}}}")
    new_content.append("")
    
    # Dokumentspezifische hypersetup-Ergänzungen
    if pdftitle or pdfsubject:
        new_content.append("% Dokumentspezifische PDF-Metadaten")
        new_content.append("\\hypersetup{")
        if pdftitle:
            new_content.append(f"  pdftitle={{{pdftitle.group(1)}}},")
        if pdfsubject:
            new_content.append(f"  pdfsubject={{{pdfsubject.group(1)}}}")
        new_content.append("}")
        new_content.append("")
    
    # Titel, Autor, Datum
    if title:
        new_content.append(title)
    if author:
        new_content.append(author)
    new_content.append(date)
    new_content.append("")
    
    # Dokument-Body
    new_content.append("\\begin{document}")
    new_content.append("")
    new_content.append(body)
    new_content.append("")
    new_content.append("\\end{document}")
    
    final_content = '\n'.join(new_content)
    
    if dry_run:
        if verbose:
            print(f"  DRY RUN: Würde {len(final_content)} Zeichen schreiben")
        return True
    
    # Schreibe aktualisiertes Dokument
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(final_content)
        if verbose:
            print(f"  Erfolgreich standardisiert ({lang.upper()})")
        return True
    except Exception as e:
        print(f"Fehler beim Schreiben von {filepath}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(
        description='Standardisiert LaTeX-Dokumente im T0 Framework'
    )
    parser.add_argument(
        '--dry-run', '-n',
        action='store_true',
        help='Keine Änderungen schreiben, nur anzeigen was passieren würde'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Ausführliche Ausgabe'
    )
    parser.add_argument(
        'files',
        nargs='*',
        help='Spezifische Dateien zum Verarbeiten (Standard: alle .tex im Verzeichnis)'
    )
    
    args = parser.parse_args()
    
    if args.files:
        tex_files = [Path(f) for f in args.files]
    else:
        tex_files = list(TEX_DIR.glob('*.tex'))
    
    success_count = 0
    fail_count = 0
    skip_count = 0
    
    for tex_file in sorted(tex_files):
        if tex_file.name.startswith('T0_Preamble') or tex_file.name.startswith('T0_Bibliography'):
            skip_count += 1
            continue
        
        if standardize_document(tex_file, args.dry_run, args.verbose):
            success_count += 1
        else:
            fail_count += 1
    
    print(f"\n{'='*50}")
    print(f"Zusammenfassung:")
    print(f"  Erfolgreich: {success_count}")
    print(f"  Übersprungen: {skip_count}")
    print(f"  Fehlgeschlagen: {fail_count}")
    
    return 0 if fail_count == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
