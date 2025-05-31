#!/usr/bin/env python3
"""
T0 Theory HTML Files Update Script
Macht minimale Änderungen an allen HTML-Dateien, damit GitHub sie als geändert erkennt.
Fügt unsichtbare Kommentare mit Zeitstempel hinzu.
"""

import os
import datetime
import re
from pathlib import Path

# Farben für Terminal-Output
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    WHITE = '\033[1;37m'
    NC = '\033[0m'  # No Color

def print_banner():
    """Zeigt das Banner an"""
    print(f"{Colors.BLUE}{'='*60}{Colors.NC}")
    print(f"{Colors.BLUE}    T0 Theory HTML Files Update Script{Colors.NC}")
    print(f"{Colors.BLUE}{'='*60}{Colors.NC}")
    print()

def get_timestamp():
    """Gibt aktuellen Zeitstempel zurück"""
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def update_html_file(file_path):
    """
    Aktualisiert eine HTML-Datei durch Hinzufügen/Aktualisieren eines Zeitstempel-Kommentars
    """
    try:
        # Datei lesen
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        timestamp = get_timestamp()
        new_comment = f"<!-- Last updated: {timestamp} -->"
        
        # Prüfen ob bereits ein Update-Kommentar existiert
        update_pattern = r'<!-- Last updated: .+? -->'
        
        if re.search(update_pattern, content):
            # Bestehenden Kommentar ersetzen
            updated_content = re.sub(update_pattern, new_comment, content)
            action = "Updated"
        else:
            # Neuen Kommentar nach <head> Tag hinzufügen
            if '<head>' in content:
                updated_content = content.replace('<head>', f'<head>\n    {new_comment}')
                action = "Added"
            else:
                # Falls kein <head> Tag, nach <!DOCTYPE> oder am Anfang hinzufügen
                if '<!DOCTYPE' in content:
                    lines = content.split('\n')
                    for i, line in enumerate(lines):
                        if '<!DOCTYPE' in line:
                            lines.insert(i + 1, new_comment)
                            break
                    updated_content = '\n'.join(lines)
                else:
                    updated_content = new_comment + '\n' + content
                action = "Added"
        
        # Datei schreiben
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        return True, action
    
    except Exception as e:
        return False, str(e)

def main():
    """Hauptfunktion"""
    print_banner()
    
    # Deutsche HTML-Dateien
    german_files = [
        "2/html/complete_particle_spectrum_de.html",
        "2/html/einheiten_revolution_de.html", 
        "2/html/rsa_analyse_t0_de.html",
        "2/html/t0_verschraenkung_analyse_de.html",
        "2/html/t0_neutrinos_explorer_de.html",
        "2/html/t0_quantum_computing_de.html",
        "2/html/t0_theory_explorer_de.html"
    ]
    
    # Englische HTML-Dateien
    english_files = [
        "2/html/complete_particle_spectrum_en.html",
        "2/html/units_revolution_en.html",
        "2/html/rsa_analysis_t0_en.html", 
        "2/html/t0_entanglement_analysis_en.html",
        "2/html/t0_neutrinos_explorer_en.html",
        "2/html/t0_quantum_computing_en.html",
        "2/html/t0_theory_explorer.html"
    ]
    
    # Index-Datei
    index_files = [
        "index.html",
        "t0_theory_index.html"
    ]
    
    # Alle Dateien kombinieren
    all_files = german_files + english_files + index_files
    
    # Statistiken
    updated_count = 0
    error_count = 0
    not_found_count = 0
    
    print(f"{Colors.CYAN}Verarbeite HTML-Dateien...{Colors.NC}\n")
    
    # Deutsche Dateien verarbeiten
    print(f"{Colors.YELLOW}📁 Deutsche HTML-Dateien:{Colors.NC}")
    for file_path in german_files:
        if os.path.exists(file_path):
            success, action = update_html_file(file_path)
            if success:
                print(f"  {Colors.GREEN}✅ {os.path.basename(file_path)} - {action}{Colors.NC}")
                updated_count += 1
            else:
                print(f"  {Colors.RED}❌ {os.path.basename(file_path)} - Error: {action}{Colors.NC}")
                error_count += 1
        else:
            print(f"  {Colors.RED}❓ {os.path.basename(file_path)} - Nicht gefunden{Colors.NC}")
            not_found_count += 1
    
    print()
    
    # Englische Dateien verarbeiten
    print(f"{Colors.YELLOW}📁 Englische HTML-Dateien:{Colors.NC}")
    for file_path in english_files:
        if os.path.exists(file_path):
            success, action = update_html_file(file_path)
            if success:
                print(f"  {Colors.GREEN}✅ {os.path.basename(file_path)} - {action}{Colors.NC}")
                updated_count += 1
            else:
                print(f"  {Colors.RED}❌ {os.path.basename(file_path)} - Error: {action}{Colors.NC}")
                error_count += 1
        else:
            print(f"  {Colors.RED}❓ {os.path.basename(file_path)} - Nicht gefunden{Colors.NC}")
            not_found_count += 1
    
    print()
    
    # Index-Dateien verarbeiten
    print(f"{Colors.YELLOW}📁 Index-Dateien:{Colors.NC}")
    for file_path in index_files:
        if os.path.exists(file_path):
            success, action = update_html_file(file_path)
            if success:
                print(f"  {Colors.GREEN}✅ {os.path.basename(file_path)} - {action}{Colors.NC}")
                updated_count += 1
            else:
                print(f"  {Colors.RED}❌ {os.path.basename(file_path)} - Error: {action}{Colors.NC}")
                error_count += 1
        else:
            print(f"  {Colors.RED}❓ {os.path.basename(file_path)} - Nicht gefunden{Colors.NC}")
            not_found_count += 1
    
    # Zusammenfassung
    print(f"\n{Colors.BLUE}{'='*60}{Colors.NC}")
    print(f"{Colors.WHITE}📊 ZUSAMMENFASSUNG:{Colors.NC}")
    print(f"  {Colors.GREEN}✅ Erfolgreich aktualisiert: {updated_count}{Colors.NC}")
    print(f"  {Colors.RED}❌ Fehler: {error_count}{Colors.NC}")
    print(f"  {Colors.RED}❓ Nicht gefunden: {not_found_count}{Colors.NC}")
    print(f"  {Colors.CYAN}📁 Gesamt verarbeitet: {len(all_files)}{Colors.NC}")
    
    if updated_count > 0:
        print(f"\n{Colors.GREEN}🎉 {updated_count} Dateien wurden erfolgreich aktualisiert!{Colors.NC}")
        print(f"{Colors.CYAN}💡 GitHub wird diese Änderungen als Modifikationen erkennen.{Colors.NC}")
        
        # Git Befehle anzeigen
        print(f"\n{Colors.PURPLE}🔧 Empfohlene Git-Befehle:{Colors.NC}")
        print(f"  {Colors.WHITE}git add .{Colors.NC}")
        print(f"  {Colors.WHITE}git commit -m 'Update HTML files timestamp - {get_timestamp()}'{Colors.NC}")
        print(f"  {Colors.WHITE}git push{Colors.NC}")
    
    if error_count > 0:
        print(f"\n{Colors.RED}⚠️  {error_count} Dateien konnten nicht aktualisiert werden.{Colors.NC}")
    
    if not_found_count > 0:
        print(f"\n{Colors.YELLOW}📝 {not_found_count} Dateien wurden nicht gefunden.{Colors.NC}")
        print(f"{Colors.CYAN}💡 Stellen Sie sicher, dass alle Dateien im korrekten Verzeichnis sind.{Colors.NC}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}⏹️  Skript durch Benutzer abgebrochen.{Colors.NC}")
    except Exception as e:
        print(f"\n{Colors.RED}💥 Unerwarteter Fehler: {e}{Colors.NC}")