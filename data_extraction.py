# data_extraction.py - Speichere diesen Code in der Datei
import os
import PyPDF2
import json
from pathlib import Path

class T0DataExtractor:
    def __init__(self):
        self.knowledge_base = {
            "core_concepts": [],
            "mathematical_relationships": [],
            "writing_style": []
        }
    
    def extract_pdf_text(self, pdf_path):
        try:
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"
                return text
        except Exception as e:
            return f"Fehler bei {pdf_path}: {str(e)}"
    
    def scan_repository(self):
        print("🔍 Scanne T0-Repository...")
        
        for root, dirs, files in os.walk("."):
            for file in files:
                file_path = os.path.join(root, file)
                
                if file.endswith(".pdf"):
                    print(f"📄 Verarbeite: {file}")
                    text = self.extract_pdf_text(file_path)
                    self.knowledge_base["core_concepts"].append({
                        "source": file,
                        "content": text[:2000]
                    })
                
                elif file in ["README.md"]:
                    print(f"📖 Dokumentation: {file}")
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            self.knowledge_base["writing_style"].append(content)
                    except:
                        pass

# Starte die Extraktion
if __name__ == "__main__":
    extractor = T0DataExtractor()
    extractor.scan_repository()
    
    with open('t0_knowledge_base.json', 'w', encoding='utf-8') as f:
        json.dump(extractor.knowledge_base, f, indent=2, ensure_ascii=False)
    
    print("✅ Daten-Extraktion abgeschlossen!")
    print(f"📊 Gefundene PDFs: {len(extractor.knowledge_base['core_concepts'])}")