#!/usr/bin/env python3
"""
Repariert doppelte Pfadstrukturen in HTML-Links
Speziell für: //T0-Time-Mass-Duality/2/html/ und //T0-Time-Mass-Duality/2/pdf/
"""

import os
import re

def fix_duplicate_paths(file_path):
    """Repariert doppelte Pfadstrukturen in einer HTML-Datei"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes_made = 0
    
    # Pattern 1: Doppelte HTML-Pfade
    # Von: /2/html//T0-Time-Mass-Duality/2/html/
    # Zu:  /2/html/
    pattern1 = r'(/2/html/)(/T0-Time-Mass-Duality/2/html/)'
    content = re.sub(pattern1, r'\1', content)
    changes_html = len(re.findall(pattern1, original_content))
    
    # Pattern 2: Doppelte PDF-Pfade  
    # Von: /2/pdf//T0-Time-Mass-Duality/2/pdf/
    # Zu:  /2/pdf/
    pattern2 = r'(/2/pdf/)(/T0-Time-Mass-Duality/2/pdf/)'
    content = re.sub(pattern2, r'\1', content)
    changes_pdf = len(re.findall(pattern2, original_content))
    
    total_changes = changes_html + changes_pdf
    
    if total_changes > 0:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ {file_path}: {changes_html} HTML + {changes_pdf} PDF Links repariert")
        return True
    else:
        print(f"ℹ️  {file_path}: Keine Änderungen nötig")
        return False

def main():
    """Hauptfunktion - repariert alle HTML-Dateien"""
    
    print("🔧 LINK-REPARATUR GESTARTET")
    print("=" * 40)
    
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    if not html_files:
        print("❌ Keine HTML-Dateien gefunden!")
        return
    
    print(f"📁 Gefundene HTML-Dateien: {len(html_files)}")
    print()
    
    files_changed = 0
    
    for html_file in sorted(html_files):
        if fix_duplicate_paths(html_file):
            files_changed += 1
    
    print()
    print("=" * 40)
    print(f"🎉 FERTIG! {files_changed} Dateien repariert")
    
    if files_changed > 0:
        print("\n✅ Alle doppelten Pfade wurden entfernt!")
        print("💡 Testen Sie jetzt Ihre Links:")
        print("   - Öffnen Sie index.html im Browser")
        print("   - Klicken Sie auf die reparierten Links")
        print("   - Alle sollten jetzt funktionieren!")

if __name__ == "__main__":
    main()