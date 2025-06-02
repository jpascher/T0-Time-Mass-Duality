#!/usr/bin/env python3
"""
HTML Links Reparatur Skript für T0-Theory Projekt
Konvertiert relative Links zu absoluten GitHub Pages URLs
"""

import os
import re
import glob
from pathlib import Path

# Konfiguration
BASE_URL = "https://jpascher.github.io/T0-Time-Mass-Duality"
HTML_DIR = "/2/html/"
PDF_DIR = "/2/pdf/"

def fix_html_links(file_path):
    """
    Repariert alle Links in einer HTML-Datei
    """
    print(f"📝 Bearbeite: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        original_content = content
        changes_made = 0
        
        # 1. Repariere HTML-Links (relative zu absolute)
        html_patterns = [
            # Einfache HTML-Dateien
            (r'href="([^"]*\.html)"', lambda m: f'href="{BASE_URL}{HTML_DIR}{m.group(1)}"' if not m.group(1).startswith('http') else m.group(0)),
            
            # Index-Links
            (r'href="index\.html"', f'href="{BASE_URL}{HTML_DIR}index.html"'),
            
            # Spezielle Dateien
            (r'href="([^"]*\.html)"(?![^<]*</a>[^<]*github\.io)', lambda m: f'href="{BASE_URL}{HTML_DIR}{m.group(1)}"' if not m.group(1).startswith('http') else m.group(0)),
        ]
        
        for pattern, replacement in html_patterns:
            if callable(replacement):
                new_content = re.sub(pattern, replacement, content)
            else:
                new_content = re.sub(pattern, replacement, content)
            
            if new_content != content:
                changes_made += content.count(re.search(pattern, content).group(0) if re.search(pattern, content) else "")
                content = new_content
        
        # 2. Repariere PDF-Links
        pdf_patterns = [
            # PDF-Dateien im /2/pdf/ Verzeichnis
            (r'href="([^"]*\.pdf)"', lambda m: f'href="{BASE_URL}{PDF_DIR}{m.group(1)}"' if not m.group(1).startswith('http') else m.group(0)),
            
            # Direkte PDF-Referenzen
            (r'href="/T0-Time-Mass-Duality/2/pdf/([^"]*\.pdf)"', f'href="{BASE_URL}{PDF_DIR}\\1"'),
        ]
        
        for pattern, replacement in pdf_patterns:
            if callable(replacement):
                new_content = re.sub(pattern, replacement, content)
            else:
                new_content = re.sub(pattern, replacement, content)
            
            if new_content != content:
                changes_made += 1
                content = new_content
        
        # 3. Repariere "Back to Main" Links
        back_to_main_patterns = [
            (r'<a href="index\.html" class="back-to-main"', f'<a href="{BASE_URL}{HTML_DIR}index.html" class="back-to-main"'),
            (r'<a href="index\.html" class="home-button"', f'<a href="{BASE_URL}{HTML_DIR}index.html" class="home-button"'),
            (r'<a href="index\.html" class="home-btn"', f'<a href="{BASE_URL}{HTML_DIR}index.html" class="home-btn"'),
        ]
        
        for pattern, replacement in back_to_main_patterns:
            new_content = re.sub(pattern, replacement, content)
            if new_content != content:
                changes_made += 1
                content = new_content
        
        # 4. Repariere GitHub Repository Links
        github_patterns = [
            (r'href="https://github\.com/jpascher/T0-Time-Mass-Duality"', f'href="https://github.com/jpascher/T0-Time-Mass-Duality"'),
        ]
        
        for pattern, replacement in github_patterns:
            content = re.sub(pattern, replacement, content)
        
        # 5. Repariere Sprachumschaltungs-Links
        language_patterns = [
            # Deutsche/Englische Versionen
            (r'href="([^"]*_de_?)\.html"', lambda m: f'href="{BASE_URL}{HTML_DIR}{m.group(1)}.html"' if not m.group(0).startswith('href="http') else m.group(0)),
            (r'href="([^"]*_en_?)\.html"', lambda m: f'href="{BASE_URL}{HTML_DIR}{m.group(1)}.html"' if not m.group(0).startswith('href="http') else m.group(0)),
        ]
        
        for pattern, replacement in language_patterns:
            if callable(replacement):
                content = re.sub(pattern, replacement, content)
            else:
                content = re.sub(pattern, replacement, content)
        
        # Nur schreiben wenn Änderungen vorgenommen wurden
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"✅ {changes_made} Links repariert in {file_path}")
            return True
        else:
            print(f"ℹ️  Keine Änderungen nötig in {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ Fehler bei {file_path}: {e}")
        return False

def create_link_inventory(directory):
    """
    Erstellt eine Übersicht aller verfügbaren Dateien
    """
    print(f"\n📋 Erstelle Link-Inventar für {directory}...")
    
    html_files = glob.glob(os.path.join(directory, "*.html"))
    pdf_files = glob.glob(os.path.join(directory, "../pdf/*.pdf")) if os.path.exists(os.path.join(directory, "../pdf/")) else []
    
    inventory = {
        "html_files": [],
        "pdf_files": [],
        "suggested_links": {}
    }
    
    for html_file in html_files:
        filename = os.path.basename(html_file)
        inventory["html_files"].append(filename)
        inventory["suggested_links"][filename] = f"{BASE_URL}{HTML_DIR}{filename}"
    
    for pdf_file in pdf_files:
        filename = os.path.basename(pdf_file)
        inventory["pdf_files"].append(filename)
        inventory["suggested_links"][filename] = f"{BASE_URL}{PDF_DIR}{filename}"
    
    return inventory

def main():
    """
    Hauptfunktion - repariert alle HTML-Dateien im Verzeichnis
    """
    print("🚀 T0-Theory HTML Links Reparatur")
    print("=" * 50)
    
    # Verzeichnis bestimmen (aktuelles Verzeichnis als Standard)
    current_dir = os.getcwd()
    print(f"📁 Arbeitsverzeichnis: {current_dir}")
    
    # Alle HTML-Dateien im Verzeichnis finden
    html_files = glob.glob("*.html")
    
    if not html_files:
        print("❌ Keine HTML-Dateien im aktuellen Verzeichnis gefunden!")
        print("💡 Stelle sicher, dass du das Skript im richtigen Verzeichnis ausführst.")
        return
    
    print(f"📄 Gefundene HTML-Dateien: {len(html_files)}")
    for file in html_files:
        print(f"   - {file}")
    
    # Link-Inventar erstellen
    inventory = create_link_inventory(current_dir)
    
    print(f"\n📊 Inventar:")
    print(f"   HTML-Dateien: {len(inventory['html_files'])}")
    print(f"   PDF-Dateien: {len(inventory['pdf_files'])}")
    
    # Bestätigung
    response = input(f"\n❓ Sollen alle {len(html_files)} HTML-Dateien repariert werden? (j/N): ")
    if response.lower() not in ['j', 'ja', 'y', 'yes']:
        print("❌ Abgebrochen.")
        return
    
    # Dateien reparieren
    print("\n🔧 Repariere Links...")
    fixed_count = 0
    
    for html_file in html_files:
        if fix_html_links(html_file):
            fixed_count += 1
    
    print(f"\n✅ Fertig! {fixed_count} von {len(html_files)} Dateien wurden modifiziert.")
    
    # Übersicht der verfügbaren Links
    print(f"\n📋 Vollständige Link-Übersicht:")
    print("=" * 50)
    
    print("\n🔗 HTML-Dateien:")
    for filename in sorted(inventory['html_files']):
        print(f"   {BASE_URL}{HTML_DIR}{filename}")
    
    if inventory['pdf_files']:
        print("\n📄 PDF-Dateien:")
        for filename in sorted(inventory['pdf_files']):
            print(f"   {BASE_URL}{PDF_DIR}{filename}")
    
    print(f"\n🌐 Hauptseite: {BASE_URL}{HTML_DIR}index.html")
    print(f"📂 Repository: https://github.com/jpascher/T0-Time-Mass-Duality")

def create_test_report():
    """
    Erstellt einen Test-Report für die reparierten Links
    """
    print("\n🧪 Erstelle Test-Report...")
    
    html_files = glob.glob("*.html")
    report = []
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Prüfe auf verbleibende relative Links
            relative_links = re.findall(r'href="(?!http)([^"]*\.html)"', content)
            pdf_links = re.findall(r'href="([^"]*\.pdf)"', content)
            
            report.append({
                'file': html_file,
                'relative_html_links': relative_links,
                'pdf_links': pdf_links,
                'status': 'OK' if not relative_links else 'WARNUNG'
            })
            
        except Exception as e:
            report.append({
                'file': html_file,
                'error': str(e),
                'status': 'FEHLER'
            })
    
    print("\n📊 Test-Report:")
    print("=" * 50)
    
    for item in report:
        print(f"\n📄 {item['file']}: {item['status']}")
        if 'relative_html_links' in item and item['relative_html_links']:
            print(f"   ⚠️  Verbleibende relative Links: {item['relative_html_links']}")
        if 'error' in item:
            print(f"   ❌ Fehler: {item['error']}")

if __name__ == "__main__":
    main()
    
    # Optional: Test-Report erstellen
    create_test = input("\n❓ Test-Report erstellen? (j/N): ")
    if create_test.lower() in ['j', 'ja', 'y', 'yes']:
        create_test_report()
    
    print("\n🎉 Skript beendet!")