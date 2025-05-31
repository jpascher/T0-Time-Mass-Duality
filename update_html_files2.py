#!/usr/bin/env python3
"""
T0 Theory HTML Files URL Replacement Script - Enhanced Version
Ersetzt GitHub Pages URLs mit GitHub Repository PDF URLs in allen HTML-Dateien.
Erweiterte Suche nach verschiedenen URL-Formaten.
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

def analyze_file_urls(file_path):
    """
    Analysiert eine Datei und zeigt alle gefundenen URLs an
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Suche nach verschiedenen URL-Patterns
        url_patterns = [
            r'href="(https://[^"]*)"',
            r'src="(https://[^"]*)"',
            r'url\((https://[^)]*)\)',
            r'(https://jpascher\.github\.io[^\s"\'<>]*)',
            r'(https://github\.com/jpascher[^\s"\'<>]*)'
        ]
        
        found_urls = set()
        for pattern in url_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            found_urls.update(matches)
        
        return list(found_urls)
        
    except Exception as e:
        return []

def replace_urls_in_file_enhanced(file_path):
    """
    Erweiterte URL-Ersetzung in einer HTML-Datei
    """
    try:
        # Datei lesen
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        total_replacements = 0
        
        # Verschiedene URL-Ersetzungen
        replacements = [
            # GitHub Pages zu GitHub Repository (für PDFs)
            (
                r'href="https://jpascher\.github\.io/T0-Time-Mass-Duality/([^"]*\.pdf)"',
                r'href="https://github.com/jpascher/T0-Time-Mass-Duality/tree/main/2/pdf/\1"'
            ),
            # Andere GitHub Pages Links (außer HTML)
            (
                r'href="https://jpascher\.github\.io/T0-Time-Mass-Duality/([^"]*(?<!\.html))"',
                r'href="https://github.com/jpascher/T0-Time-Mass-Duality/tree/main/2/pdf/\1"'
            ),
            # Website-Links zu Repository-Links (außer HTML)
            (
                r'href="https://jpascher\.github\.io/T0-Time-Mass-Duality/"(?![^<]*\.html)',
                r'href="https://github.com/jpascher/T0-Time-Mass-Duality/tree/main/2/pdf/"'
            )
        ]
        
        # Ersetzungen durchführen
        for old_pattern, new_pattern in replacements:
            matches = re.findall(old_pattern, content, re.IGNORECASE)
            if matches:
                content = re.sub(old_pattern, new_pattern, content, flags=re.IGNORECASE)
                total_replacements += len(matches)
        
        # Zusätzliche spezifische Ersetzungen
        # Einfache URL-Ersetzung (nicht in href)
        simple_replacements = [
            (
                'https://jpascher.github.io/T0-Time-Mass-Duality/',
                'https://github.com/jpascher/T0-Time-Mass-Duality/tree/main/'
            )
        ]
        
        for old_url, new_url in simple_replacements:
            if old_url in content:
                # Nur ersetzen wenn es nicht bereits ein href ist
                pattern = f'(?<!href="){re.escape(old_url)}'
                matches = re.findall(pattern, content)
                if matches:
                    content = re.sub(pattern, new_url, content)
                    total_replacements += len(matches)
        
        # Datei schreiben falls Änderungen vorgenommen wurden
        if total_replacements > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, total_replacements
        else:
            return False, 0
            
    except Exception as e:
        return False, str(e)

def main():
    """Hauptfunktion"""
    print(f"{Colors.BLUE}T0 Theory HTML Files - Enhanced URL Replacement Script{Colors.NC}")
    print(f"{Colors.BLUE}{'='*60}{Colors.NC}")
    print(f"{Colors.CYAN}Analysiert und ersetzt GitHub URLs in HTML-Dateien{Colors.NC}\n")
    
    # Alle HTML-Dateien finden
    html_files = []
    search_paths = ["*.html", "2/html/*.html", "html/*.html"]
    
    for pattern in search_paths:
        files = glob.glob(pattern)
        html_files.extend(files)
    
    html_files = list(set(html_files))
    
    if not html_files:
        print(f"{Colors.RED}❌ Keine HTML-Dateien gefunden!{Colors.NC}")
        return
    
    print(f"{Colors.CYAN}📁 {len(html_files)} HTML-Dateien gefunden{Colors.NC}\n")
    
    # Erst analysieren - URLs in ersten paar Dateien anzeigen
    print(f"{Colors.YELLOW}🔍 URL-Analyse (erste 3 Dateien):{Colors.NC}")
    for i, file_path in enumerate(html_files[:3]):
        filename = os.path.basename(file_path)
        urls = analyze_file_urls(file_path)
        print(f"\n📄 {filename}:")
        
        github_urls = [url for url in urls if 'github' in url.lower()]
        jpascher_urls = [url for url in urls if 'jpascher' in url.lower()]
        
        if github_urls:
            print(f"  {Colors.GREEN}GitHub URLs gefunden: {len(github_urls)}{Colors.NC}")
            for url in github_urls[:2]:  # Zeige nur erste 2
                print(f"    - {url}")
        
        if jpascher_urls:
            print(f"  {Colors.CYAN}jpascher URLs gefunden: {len(jpascher_urls)}{Colors.NC}")
            for url in jpascher_urls[:2]:  # Zeige nur erste 2
                print(f"    - {url}")
        
        if not github_urls and not jpascher_urls:
            print(f"  {Colors.YELLOW}Keine relevanten URLs gefunden{Colors.NC}")
    
    print(f"\n{Colors.YELLOW}Möchten Sie die URL-Ersetzung durchführen? (j/n): {Colors.NC}", end="")
    confirmation = input().strip().lower()
    
    if confirmation not in ['j', 'ja', 'y', 'yes']:
        print(f"{Colors.YELLOW}⏹️  Abgebrochen durch Benutzer.{Colors.NC}")
        return
    
    # URLs ersetzen
    print(f"\n{Colors.CYAN}🔄 Ersetze URLs...{Colors.NC}\n")
    
    success_count = 0
    error_count = 0
    total_changes = 0
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        
        result = replace_urls_in_file_enhanced(file_path)
        
        if isinstance(result[1], int):  # Erfolgreiche Ausführung
            success, changes = result
            
            if success:
                print(f"  {Colors.GREEN}✅ {filename} - {changes} Änderungen{Colors.NC}")
                success_count += 1
                total_changes += changes
            else:
                print(f"  {Colors.YELLOW}⏭️  {filename} - keine Änderungen nötig{Colors.NC}")
        else:  # Fehler
            success, error_msg = result
            print(f"  {Colors.RED}❌ {filename} - Fehler: {error_msg}{Colors.NC}")
            error_count += 1
    
    # Zusammenfassung
    print(f"\n{Colors.BLUE}{'='*60}{Colors.NC}")
    print(f"{Colors.WHITE}📊 ZUSAMMENFASSUNG:{Colors.NC}")
    print(f"  Verarbeitete Dateien: {len(html_files)}")
    print(f"  {Colors.GREEN}✅ Erfolgreich geändert: {success_count}{Colors.NC}")
    print(f"  {Colors.RED}❌ Fehler: {error_count}{Colors.NC}")
    print(f"  {Colors.WHITE}📈 Gesamt URL-Änderungen: {total_changes}{Colors.NC}")
    
    if success_count > 0:
        print(f"\n{Colors.GREEN}🎉 {success_count} Dateien erfolgreich aktualisiert!{Colors.NC}")
        print(f"{Colors.CYAN}💡 URLs wurden auf GitHub Repository umgestellt.{Colors.NC}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}⏹️  Skript durch Benutzer abgebrochen.{Colors.NC}")
    except Exception as e:
        print(f"\n{Colors.RED}💥 Unerwarteter Fehler: {e}{Colors.NC}")