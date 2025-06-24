import pdfplumber
import os
import re
import argparse

def extract_slides_from_pdf(pdf_path, output_dir="extracted_slides"):
    """
    Extrahiert Text aus jeder Seite eines PDF (typischerweise Slides) und speichert
    diese als separate Textdateien für die Verwendung mit d-id.
    
    Args:
        pdf_path (str): Pfad zur PDF-Datei
        output_dir (str): Verzeichnis, in dem die extrahierten Slides gespeichert werden
    """
    # Ausgabeverzeichnis erstellen, falls es nicht existiert
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    try:
        # PDF öffnen
        with pdfplumber.open(pdf_path) as pdf:
            total_pages = len(pdf.pages)
            print(f"PDF geöffnet: {pdf_path}")
            print(f"Anzahl der Seiten: {total_pages}")
            
            for i, page in enumerate(pdf.pages, 1):
                # Text extrahieren
                text = page.extract_text()
                
                if text:
                    # Text bereinigen
                    # Unnötige Leerzeilen entfernen
                    text = re.sub(r'\n\s*\n', '\n', text)
                    
                    # Suche nach einem möglichen Titel (typischerweise am Anfang der Seite)
                    lines = text.split('\n')
                    title = lines[0] if lines else f"Slide_{i}"
                    
                    # Formatiere den Text für d-id
                    # Entferne mögliche Seitenzahlen, Fußzeilen, etc.
                    # Dies kann je nach PDF-Layout angepasst werden müssen
                    
                    # Dateiname erstellen
                    filename = f"slide_{i:02d}_{re.sub(r'[^\w]', '_', title[:30])}.txt"
                    filepath = os.path.join(output_dir, filename)
                    
                    # Slide als Textdatei speichern
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(text)
                    
                    print(f"Slide {i}/{total_pages} extrahiert: {filename}")
                else:
                    print(f"Warnung: Keine Textinhalte auf Seite {i} gefunden.")
            
            print(f"\nExtraktion abgeschlossen. {total_pages} Slides wurden nach '{output_dir}' extrahiert.")
    
    except Exception as e:
        print(f"Fehler beim Extrahieren der Slides: {str(e)}")

def extract_slides_for_did(pdf_path, output_dir="did_slides"):
    """
    Verarbeitet PDF-Slides speziell für d-id, mit besonderem Fokus auf
    die Formatierung und Anpassung der Inhalte für die Sprachsynthese.
    
    Args:
        pdf_path (str): Pfad zur PDF-Datei
        output_dir (str): Verzeichnis für die d-id optimierten Slides
    """
    # Ausgabeverzeichnis erstellen
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    try:
        # PDF öffnen
        with pdfplumber.open(pdf_path) as pdf:
            total_pages = len(pdf.pages)
            print(f"PDF wird für d-id verarbeitet: {pdf_path}")
            
            for i, page in enumerate(pdf.pages, 1):
                # Text extrahieren
                text = page.extract_text()
                
                if text:
                    # Text für d-id optimieren
                    # 1. Mathematische Formeln vereinfachen
                    text = re.sub(r'\\[a-zA-Z]+{.*?}', '', text)  # LaTeX-Befehle entfernen
                    text = re.sub(r'\$.*?\$', '', text)           # Inline-Mathe entfernen
                    text = re.sub(r'\$\$.*?\$\$', '', text)       # Display-Mathe entfernen
                    
                    # 2. Bullet-Points formatieren
                    text = re.sub(r'•\s*', '- ', text)
                    
                    # 3. Unnötige Zeichen entfernen
                    text = re.sub(r'[\[\]\{\}\\]', '', text)
                    
                    # 4. Doppelte Leerzeilen reduzieren
                    text = re.sub(r'\n\s*\n', '\n', text)
                    
                    # Slide-Titel extrahieren (erste nicht-leere Zeile)
                    lines = [line for line in text.split('\n') if line.strip()]
                    title = lines[0] if lines else f"Slide {i}"
                    
                    # Sprechtext vorbereiten (ohne Titel, Fußzeilen, etc.)
                    content = "\n".join(lines[1:]) if len(lines) > 1 else ""
                    
                    # d-id Textformat: Titel + Inhalt
                    did_text = f"{title}\n\n{content}"
                    
                    # Datei speichern
                    filename = f"did_slide_{i:02d}.txt"
                    filepath = os.path.join(output_dir, filename)
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(did_text)
                    
                    print(f"d-id Slide {i}/{total_pages} erstellt")
            
            print(f"\nVerarbeitung abgeschlossen. {total_pages} d-id optimierte Slides wurden nach '{output_dir}' exportiert.")
    
    except Exception as e:
        print(f"Fehler bei der d-id Verarbeitung: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extrahiert Slides aus einem PDF für d-id')
    parser.add_argument('pdf_path', type=str, help='Pfad zur PDF-Datei')
    parser.add_argument('--output', type=str, default='did_slides', help='Ausgabeverzeichnis')
    parser.add_argument('--format', type=str, choices=['raw', 'did'], default='did', 
                        help='Extraktionsformat: raw für Rohtext, did für d-id optimiert')
    
    args = parser.parse_args()
    
    if args.format == 'raw':
        extract_slides_from_pdf(args.pdf_path, args.output)
    else:
        extract_slides_for_did(args.pdf_path, args.output)