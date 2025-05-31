#!/usr/bin/env python3
"""
T0 Theory HTML Files Rename Script
Fügt einen Unterstrich am Ende aller HTML-Dateinamen im Verzeichnis 2/html/ ein
und aktualisiert die Verweise in den Index-Dateien.
"""

import os
import glob
import re

# Farben für Terminal-Output
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    CYAN = '\033[0;36m'
    WHITE = '\033[1;37m'
    NC = '\033[0m'  # No Color

def debug_directory_structure():
    """
    Zeigt die aktuelle Verzeichnisstruktur für Debugging
    """
    print(f"{Colors.YELLOW}🔍 Debug: Verzeichnisstruktur{Colors.NC}")
    print(f"  Aktuelles Verzeichnis: {os.getcwd()}")
    
    # Prüfe verschiedene mögliche Pfade
    possible_paths = [
        "2/html",
        "./2/html", 
        "html",
        "2\\html"  # Windows-Pfad
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            print(f"  {Colors.GREEN}✅ Gefunden: {path}{Colors.NC}")
            files = os.listdir(path)
            html_files = [f for f in files if f.endswith('.html')]
            print(f"    HTML-Dateien: {len(html_files)}")
            for html_file in html_files[:3]:  # Zeige nur erste 3
                print(f"      - {html_file}")
            if len(html_files) > 3:
                print(f"      ... und {len(html_files) - 3} weitere")
        else:
            print(f"  {Colors.RED}❌ Nicht gefunden: {path}{Colors.NC}")
    
    # Zeige alle Unterverzeichnisse
    print(f"\n  Verfügbare Unterverzeichnisse:")
    for item in os.listdir('.'):
        if os.path.isdir(item):
            print(f"    📁 {item}")
    print()

def find_html_directory():
    """
    Findet das korrekte HTML-Verzeichnis
    """
    possible_paths = [
        "2/html",
        "./2/html",
        "html",
        "2\\html"
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            html_files = glob.glob(os.path.join(path, "*.html"))
            if html_files:
                return path, html_files
    
    return None, []

def update_index_files(renamed_files, html_dir):
    """
    Aktualisiert die Verweise in den Index-Dateien
    """
    index_files = [
        "index.html",
        "t0_theory_index.html"
    ]
    
    print(f"\n{Colors.CYAN}🔗 Aktualisiere Index-Dateien...{Colors.NC}")
    
    for index_file in index_files:
        if not os.path.exists(index_file):
            print(f"  {Colors.YELLOW}⏭️  {index_file} - nicht gefunden{Colors.NC}")
            continue
        
        try:
            # Datei lesen
            with open(index_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Verweise aktualisieren
            updated_content = content
            links_updated = 0
            
            for old_name, new_name in renamed_files.items():
                # Verschiedene mögliche Pfad-Formate berücksichtigen
                old_patterns = [
                    f"{html_dir}/{old_name}",
                    f"2/html/{old_name}",
                    f"./2/html/{old_name}"
                ]
                
                new_path = f"{html_dir}/{new_name}"
                
                for old_pattern in old_patterns:
                    if old_pattern in updated_content:
                        updated_content = updated_content.replace(old_pattern, new_path)
                        links_updated += 1
            
            # Datei schreiben falls Änderungen vorgenommen wurden
            if links_updated > 0:
                with open(index_file, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"  {Colors.GREEN}✅ {index_file} - {links_updated} Links aktualisiert{Colors.NC}")
            else:
                print(f"  {Colors.YELLOW}⏭️  {index_file} - keine Links zu aktualisieren gefunden{Colors.NC}")
                
        except Exception as e:
            print(f"  {Colors.RED}❌ {index_file} - Fehler: {e}{Colors.NC}")

def main():
    """Hauptfunktion"""
    print(f"{Colors.BLUE}T0 Theory HTML Files - Unterstrich hinzufügen{Colors.NC}")
    print(f"{Colors.BLUE}{'='*50}{Colors.NC}\n")
    
    # Debug-Informationen anzeigen
    debug_directory_structure()
    
    # HTML-Verzeichnis finden
    html_dir, html_files = find_html_directory()
    
    if not html_dir:
        print(f"{Colors.RED}❌ Kein HTML-Verzeichnis mit .html Dateien gefunden!{Colors.NC}")
        print(f"{Colors.CYAN}💡 Stellen Sie sicher, dass Sie das Skript im Hauptverzeichnis ausführen.{Colors.NC}")
        return
    
    print(f"{Colors.GREEN}✅ HTML-Verzeichnis gefunden: {html_dir}{Colors.NC}")
    print(f"{Colors.CYAN}📁 {len(html_files)} HTML-Dateien gefunden{Colors.NC}\n")
    
    # Alle gefundenen Dateien anzeigen
    print(f"{Colors.WHITE}Gefundene HTML-Dateien:{Colors.NC}")
    for file_path in html_files:
        filename = os.path.basename(file_path)
        print(f"  - {filename}")
    print()
    
    success_count = 0
    error_count = 0
    renamed_files = {}  # Mapping: alter_name -> neuer_name
    
    # Dateien umbenennen
    print(f"{Colors.CYAN}🔄 Benenne Dateien um...{Colors.NC}")
    for file_path in html_files:
        old_filename = os.path.basename(file_path)
        
        # Prüfen ob bereits einen Unterstrich hat
        if old_filename.endswith('_.html'):
            print(f"  {Colors.YELLOW}⏭️  {old_filename} - bereits mit Unterstrich{Colors.NC}")
            continue
        
        # Neuen Namen erstellen: Unterstrich vor .html einfügen
        name_without_ext = os.path.splitext(old_filename)[0]
        new_filename = name_without_ext + "_.html"
        new_path = os.path.join(html_dir, new_filename)
        
        try:
            # Prüfen ob Zieldatei bereits existiert
            if os.path.exists(new_path):
                print(f"  {Colors.YELLOW}⏭️  {old_filename} → {new_filename} (existiert bereits){Colors.NC}")
                renamed_files[old_filename] = new_filename
                continue
            
            # Datei umbenennen
            os.rename(file_path, new_path)
            print(f"  {Colors.GREEN}✅ {old_filename} → {new_filename}{Colors.NC}")
            success_count += 1
            renamed_files[old_filename] = new_filename
            
        except Exception as e:
            print(f"  {Colors.RED}❌ {old_filename} - Fehler: {e}{Colors.NC}")
            error_count += 1
    
    # Index-Dateien aktualisieren falls Dateien umbenannt wurden
    if renamed_files:
        update_index_files(renamed_files, html_dir)
    else:
        print(f"\n{Colors.YELLOW}⚠️  Keine Dateien zum Umbenennen gefunden oder alle bereits umbenannt.{Colors.NC}")
    
    # Zusammenfassung
    print(f"\n{Colors.BLUE}{'='*50}{Colors.NC}")
    print(f"{Colors.WHITE}📊 ZUSAMMENFASSUNG:{Colors.NC}")
    print(f"  HTML-Verzeichnis: {html_dir}")
    print(f"  Gefundene Dateien: {len(html_files)}")
    print(f"  Erfolgreich umbenannt: {success_count}")
    print(f"  Fehler: {error_count}")
    print(f"  Links aktualisiert: {len(renamed_files)}")
    
    if success_count > 0:
        print(f"\n{Colors.GREEN}🎉 {success_count} Dateien erfolgreich umbenannt!{Colors.NC}")
    elif renamed_files:
        print(f"\n{Colors.CYAN}💡 Index-Links wurden aktualisiert für bereits umbenannte Dateien.{Colors.NC}")

if __name__ == "__main__":
    main()