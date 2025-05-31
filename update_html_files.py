#!/usr/bin/env python3
"""
T0 Theory HTML Files URL Replacement Script
Ersetzt GitHub Pages URLs mit GitHub Repository PDF URLs in allen HTML-Dateien.
Lässt HTML-Links unverändert.
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

def find_all_html_files():
    """
    Findet alle HTML-Dateien in verschiedenen Verzeichnissen
    """
    html_files = []
    
    # Verschiedene mögliche Verzeichnisse
    search_paths = [
        "*.html",           # Hauptverzeichnis
        "2/html/*.html",    # Unterverzeichnis
        "html/*.html",      # Alternatives Verzeichnis
    ]
    
    for pattern in search_paths:
        files = glob.glob(pattern)
        html_files.extend(files)
    
    # Duplikate entfernen
    html_files = list(set(html_files))
    return html_files

def replace_urls_in_file(file_path):
    """
    Ersetzt URLs in einer HTML-Datei
    """
    try:
        # Datei lesen
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # URL-Ersetzungen definieren
        old_base_url = "https://jpascher.github.io/T0-Time-Mass-Duality/"
        new_base_url = "https://github.com/jpascher/T0-Time-Mass-Duality/tree/main/2/pdf/"
        
        # Zähler für Ersetzungen
        pdf_replacements = 0
        
        # Suche nach PDF-Links mit der alten URL
        # Pattern: href="https://jpascher.github.io/T0-Time-Mass-Duality/irgendwas.pdf"
        pdf_pattern = re.compile(
            r'href="' + re.escape(old_base_url) + r'([^"]*\.pdf)"',
            re.IGNORECASE
        )
        
        def replace_pdf_link(match):
            nonlocal pdf_replacements
            pdf_file = match.group(1)
            pdf_replacements += 1
            return f'href="{new_base_url}{pdf_file}"'
        
        # PDF-Links ersetzen
        content = pdf_pattern.sub(replace_pdf_link, content)
        
        # Zusätzliche allgemeine URL-Ersetzungen (nur wenn es KEINE HTML-Datei ist)
        general_replacements = 0
        
        # Suche nach anderen Links (nicht PDF, nicht HTML)
        general_pattern = re.compile(
            r'href="' + re.escape(old_base_url) + r'([^"]*(?<!\.html)(?<!\.pdf))"',
            re.IGNORECASE
        )
        
        def replace_general_link(match):
            nonlocal general_replacements
            file_path = match.group(1)
            # Prüfen ob es ein PDF-ähnlicher Pfad ist
            if any(keyword in file_path.lower() for keyword in ['pdf', 'doc', 'paper']):
                general_replacements += 1
                return f'href="{new_base_url}{file_path}"'
            else:
                # Andere Links unverändert lassen
                return match.group(0)
        
        # Allgemeine Links ersetzen
        content = general_pattern.sub(replace_general_link, content)
        
        # Datei schreiben falls Änderungen vorgenommen wurden
        total_changes = pdf_replacements + general_replacements
        
        if total_changes > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, total_changes, pdf_replacements, general_replacements
        else:
            return False, 0, 0, 0
            
    except Exception as e:
        return False, str(e), 0, 0

def main():
    """Hauptfunktion"""
    print(f"{Colors.BLUE}T0 Theory HTML Files - URL Replacement Script{Colors.NC}")
    print(f"{Colors.BLUE}{'='*55}{Colors.NC}")
    print(f"{Colors.CYAN}Ersetzt GitHub Pages URLs mit GitHub Repository PDF URLs{Colors.NC}")
    print(f"{Colors.YELLOW}HTML-Links bleiben unverändert!{Colors.NC}\n")
    
    # Alle HTML-Dateien finden
    html_files = find_all_html_files()
    
    if not html_files:
        print(f"{Colors.RED}❌ Keine HTML-Dateien gefunden!{Colors.NC}")
        return
    
    print(f"{Colors.CYAN}📁 {len(html_files)} HTML-Dateien gefunden{Colors.NC}")
    print(f"{Colors.WHITE}Gefundene Dateien:{Colors.NC}")
    for file_path in html_files:
        print(f"  - {file_path}")
    print()
    
    # URL-Ersetzungen anzeigen
    print(f"{Colors.YELLOW}🔄 URL-Ersetzungen:{Colors.NC}")
    print(f"  {Colors.WHITE}Von:{Colors.NC} https://jpascher.github.io/T0-Time-Mass-Duality/")
    print(f"  {Colors.WHITE}Zu: {Colors.NC} https://github.com/jpascher/T0-Time-Mass-Duality/tree/main/2/pdf/")
    print(f"  {Colors.GREEN}✅ PDF-Links: Werden ersetzt{Colors.NC}")
    print(f"  {Colors.CYAN}⏭️  HTML-Links: Bleiben unverändert{Colors.NC}")
    print()
    
    # Bestätigung
    print(f"{Colors.YELLOW}Möchten Sie fortfahren? (j/n): {Colors.NC}", end="")
    confirmation = input().strip().lower()
    
    if confirmation not in ['j', 'ja', 'y', 'yes']:
        print(f"{Colors.YELLOW}⏹️  Abgebrochen durch Benutzer.{Colors.NC}")
        return
    
    # URLs in Dateien ersetzen
    print(f"\n{Colors.CYAN}🔄 Ersetze URLs...{Colors.NC}\n")
    
    success_count = 0
    error_count = 0
    total_pdf_changes = 0
    total_general_changes = 0
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        
        result = replace_urls_in_file(file_path)
        
        if len(result) == 4:  # Erfolgreiche Ausführung
            success, total_changes, pdf_changes, general_changes = result
            
            if success:
                print(f"  {Colors.GREEN}✅ {filename}{Colors.NC}")
                print(f"    📄 PDF-Links: {pdf_changes} | 🔗 Andere: {general_changes}")
                success_count += 1
                total_pdf_changes += pdf_changes
                total_general_changes += general_changes
            else:
                print(f"  {Colors.YELLOW}⏭️  {filename} - keine Änderungen nötig{Colors.NC}")
        else:  # Fehler
            success, error_msg, _, _ = result
            print(f"  {Colors.RED}❌ {filename} - Fehler: {error_msg}{Colors.NC}")
            error_count += 1
    
    # Zusammenfassung
    print(f"\n{Colors.BLUE}{'='*55}{Colors.NC}")
    print(f"{Colors.WHITE}📊 ZUSAMMENFASSUNG:{Colors.NC}")
    print(f"  Verarbeitete Dateien: {len(html_files)}")
    print(f"  {Colors.GREEN}✅ Erfolgreich geändert: {success_count}{Colors.NC}")
    print(f"  {Colors.RED}❌ Fehler: {error_count}{Colors.NC}")
    print(f"  {Colors.CYAN}📄 PDF-Link Änderungen: {total_pdf_changes}{Colors.NC}")
    print(f"  {Colors.CYAN}🔗 Andere Änderungen: {total_general_changes}{Colors.NC}")
    print(f"  {Colors.WHITE}📈 Gesamt Änderungen: {total_pdf_changes + total_general_changes}{Colors.NC}")
    
    if success_count > 0:
        print(f"\n{Colors.GREEN}🎉 {success_count} Dateien erfolgreich aktualisiert!{Colors.NC}")
        print(f"{Colors.CYAN}💡 Alle PDF-Links zeigen jetzt auf das GitHub Repository.{Colors.NC}")
        
        # Git Befehle anzeigen
        print(f"\n{Colors.BLUE}🔧 Empfohlene Git-Befehle:{Colors.NC}")
        print(f"  {Colors.WHITE}git add .{Colors.NC}")
        print(f"  {Colors.WHITE}git commit -m 'Update PDF URLs to GitHub repository links'{Colors.NC}")
        print(f"  {Colors.WHITE}git push{Colors.NC}")
    
    if error_count > 0:
        print(f"\n{Colors.RED}⚠️  {error_count} Dateien konnten nicht verarbeitet werden.{Colors.NC}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}⏹️  Skript durch Benutzer abgebrochen.{Colors.NC}")
    except Exception as e:
        print(f"\n{Colors.RED}💥 Unerwarteter Fehler: {e}{Colors.NC}")