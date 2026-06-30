import os
import re
import random
import webbrowser
import requests
import json
from collections import defaultdict
import time
import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog

# Importieren des API-Schlüssels aus der config.py Datei
try:
  from config import ANTHROPIC_API_KEY
  print("API-Schlüssel aus config.py erfolgreich geladen.")
except ImportError:
  print("WARNUNG: Keine config.py Datei gefunden oder Fehler beim Import.")
  print("Bitte erstellen Sie eine config.py Datei mit folgendem Inhalt:")
  print('ANTHROPIC_API_KEY = "Ihr-API-Schlüssel-hier"')
  ANTHROPIC_API_KEY = None

try:
  import pyperclip
  has_pyperclip = True
except ImportError:
  has_pyperclip = False
  print("Hinweis: Das Paket 'pyperclip' ist nicht installiert.")
  print("Sie müssen die Antworten manuell kopieren.")
  print("Installieren Sie es mit 'pip install pyperclip' für automatisches Kopieren.")

# Verzeichnisse für TeX-Dateien (lokale Pfade)
TEX_DIRS = [
  r"C:\Users\johann\1\2\tex\English", # Englische TeX-Dateien
  r"C:\Users\johann\1\2\tex\Deutsch"  # Deutsche TeX-Dateien
]

# Aktuelles Verzeichnis für PDF-Dateien als Fallback
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Bevorzugte Sprache (en = Englisch, de = Deutsch)
DEFAULT_LANGUAGE = "en"

# Repository-URL-Muster für Ihre Dokumente
REPOSITORY_URL_PATTERN = r"https://github\.com/[A-Za-z0-9_\-]+/[A-Za-z0-9_\-]+/blob/[A-Za-z0-9_\-/]+\.pdf"

# Basis-URL für das Repository, falls in den Dokumenten keine expliziten URLs gefunden werden
DEFAULT_REPOSITORY_BASE = "https://github.com/johannpascher/t0-model/blob/main/"

# Relevante Subreddits für physikalische Diskussionen (als Referenz)
PHYSICS_SUBREDDITS = [
  "Physics",
  "AskPhysics",
  "TheoreticalPhysics",
  "cosmology",
  "AskScience"
]

# T0-Modell Kurzeinführung für Claude
T0_MODEL_INTRO = """
Das T0-Modell ist ein alternativer theoretischer Ansatz in der Physik, der auf einer Zeit-Masse-Dualität basiert. 
Hauptmerkmale des Modells:
1. Zeit wird als absolut betrachtet, während Masse variabel ist (im Gegensatz zur konventionellen Relativitätstheorie)
2. Ein intrinsisches Zeitfeld T(x) = ℏ/max(mc², ω) wird eingeführt
3. Gravitation entsteht aus Zeitfeldgradienten
4. Das Modell versucht, Quantenmechanik und Relativitätstheorie ohne die typischen Widersprüche zu vereinen
5. Bietet alternative Erklärungen für Phänomene, die üblicherweise mit dunkler Materie oder dunkler Energie erklärt werden

Bitte formuliere eine wissenchaftlich fundierte, freundliche und überzeugende Antwort basierend auf diesen Konzepten und den extrahierten Inhalten aus den Forschungsdokumenten.
"""

class PostInputDialog:
  """Dialog zum Eingeben von Post-Details"""
  
  def __init__(self, parent):
    self.result = None
    self.dialog = tk.Toplevel(parent)
    self.dialog.title("Post-Details eingeben")
    self.dialog.geometry("800x600")
    self.dialog.transient(parent)
    self.dialog.grab_set()
    
    # Titel
    tk.Label(self.dialog, text="Titel des Posts:", font=("Arial", 12, "bold")).pack(anchor=tk.W, padx=10, pady=(10,5))
    self.title_entry = tk.Entry(self.dialog, width=80, font=("Arial", 10))
    self.title_entry.pack(fill=tk.X, padx=10, pady=(0,10))
    
    # Post-Text
    tk.Label(self.dialog, text="Text des Posts (optional):", font=("Arial", 12, "bold")).pack(anchor=tk.W, padx=10, pady=(10,5))
    self.text_entry = scrolledtext.ScrolledText(self.dialog, height=10, width=80, font=("Arial", 10))
    self.text_entry.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0,10))
    
    # Buttons
    button_frame = tk.Frame(self.dialog)
    button_frame.pack(fill=tk.X, padx=10, pady=10)
    
    tk.Button(button_frame, text="Übernehmen", command=self.accept, bg="#4CAF50", fg="white", 
         font=("Arial", 11, "bold"), pady=5, padx=10).pack(side=tk.RIGHT, padx=5)
    
    tk.Button(button_frame, text="Abbrechen", command=self.cancel, bg="#f44336", fg="white",
         font=("Arial", 11), pady=5, padx=10).pack(side=tk.RIGHT, padx=5)
    
    # Dialog zentrieren
    self.dialog.update_idletasks()
    width = self.dialog.winfo_width()
    height = self.dialog.winfo_height()
    x = (parent.winfo_width() // 2) - (width // 2)
    y = (parent.winfo_height() // 2) - (height // 2)
    self.dialog.geometry(f"+{x}+{y}")
    
    # Fokus setzen
    self.title_entry.focus_set()
    
    # Warten auf den Benutzer
    parent.wait_window(self.dialog)
  
  def accept(self):
    title = self.title_entry.get().strip()
    if not title:
      messagebox.showerror("Fehler", "Bitte geben Sie mindestens einen Titel ein.")
      return
    
    text = self.text_entry.get("1.0", tk.END).strip()
    self.result = (title, text)
    self.dialog.destroy()
  
  def cancel(self):
    self.dialog.destroy()

class InteractiveEditor:
  """Interaktiver Dialog mit der KI zum Überarbeiten der Antwort"""
  
  def __init__(self, master, initial_response, topic, content_extracts, repository_urls, post_details=None):
    self.master = master
    self.initial_response = initial_response
    self.topic = topic
    self.content_extracts = content_extracts
    self.repository_urls = repository_urls
    self.post_details = post_details
    
    # Hauptfenster konfigurieren
    self.master.title("T0-Modell Antwort-Editor")
    self.master.geometry("1000x700")
    
    # Antwortbereich
    self.frame_response = tk.Frame(master)
    self.frame_response.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
    
    tk.Label(self.frame_response, text="Generierte Antwort:", font=("Arial", 12, "bold")).pack(anchor=tk.W)
    
    self.text_response = scrolledtext.ScrolledText(self.frame_response, wrap=tk.WORD, height=15, font=("Arial", 10))
    self.text_response.pack(fill=tk.BOTH, expand=True)
    self.text_response.insert(tk.END, initial_response)
    
    # Bearbeitungsanweisungen
    self.frame_edit = tk.Frame(master)
    self.frame_edit.pack(pady=10, padx=10, fill=tk.BOTH)
    
    tk.Label(self.frame_edit, text="Ihre Anweisungen an die KI:", font=("Arial", 12, "bold")).pack(anchor=tk.W)
    
    self.text_edit = scrolledtext.ScrolledText(self.frame_edit, wrap=tk.WORD, height=6, font=("Arial", 10))
    self.text_edit.pack(fill=tk.BOTH, expand=True)
    self.text_edit.insert(tk.END, "Bitte überarbeite die Antwort so, dass...")
    
    # Buttons
    self.frame_buttons = tk.Frame(master)
    self.frame_buttons.pack(pady=10, padx=10, fill=tk.X)
    
    tk.Button(self.frame_buttons, text="An KI senden", command=self.send_to_ai, bg="#4CAF50", fg="white", 
         font=("Arial", 11, "bold"), pady=5, padx=10).pack(side=tk.LEFT, padx=5)
    
    tk.Button(self.frame_buttons, text="Antwort übernehmen", command=self.accept_response, bg="#2196F3", fg="white",
         font=("Arial", 11, "bold"), pady=5, padx=10).pack(side=tk.LEFT, padx=5)
    
    tk.Button(self.frame_buttons, text="Manuell bearbeiten", command=self.edit_manually, bg="#FF9800", fg="white",
         font=("Arial", 11, "bold"), pady=5, padx=10).pack(side=tk.LEFT, padx=5)
    
    tk.Button(self.frame_buttons, text="Kopieren", command=self.copy_to_clipboard, bg="#9E9E9E", fg="white",
         font=("Arial", 11), pady=5, padx=10).pack(side=tk.RIGHT, padx=5)
    
    # Status
    self.label_status = tk.Label(master, text="Bereit. Sie können die Antwort überarbeiten lassen oder übernehmen.", bd=1, relief=tk.SUNKEN, anchor=tk.W)
    self.label_status.pack(side=tk.BOTTOM, fill=tk.X)
    
    # Ergebnis
    self.result = initial_response
  
  def send_to_ai(self):
    """Sendet die Bearbeitungsanweisungen an die KI"""
    instructions = self.text_edit.get("1.0", tk.END).strip()
    
    if not instructions or instructions == "Bitte überarbeite die Antwort so, dass...":
      messagebox.showwarning("Warnung", "Bitte geben Sie Anweisungen für die KI ein.")
      return
    
    self.label_status.config(text="Sende Anfrage an die KI...")
    self.master.update()
    
    try:
      # Prompt für die KI vorbereiten
      current_response = self.text_response.get("1.0", tk.END)
      
      prompt = f"""Hier ist eine generierte Antwort über das T0-Modell zum Thema '{self.topic}':

{current_response}

Bitte überarbeite diese Antwort entsprechend der folgenden Anweisungen:

{instructions}

Die überarbeitete Antwort sollte weiterhin wissenschaftlich korrekt bleiben und das T0-Modell positiv darstellen.
Gib nur die überarbeitete Antwort zurück, ohne Einleitung oder Erklärung.
"""
      
      # API-Anfrage an Anthropic Claude senden
      if ANTHROPIC_API_KEY:
        headers = {
          "x-api-key": ANTHROPIC_API_KEY,
          "anthropic-version": "2023-06-01",
          "content-type": "application/json"
        }
        
        data = {
          "model": "claude-3-haiku-20240307",
          "max_tokens": 1024,
          "messages": [
            {"role": "user", "content": prompt}
          ]
        }
        
        response = requests.post(
          "https://api.anthropic.com/v1/messages",
          headers=headers,
          json=data
        )
        
        if response.status_code == 200:
          response_json = response.json()
          new_response = response_json['content'][0]['text']
          
          # Aktualisiere den Textbereich mit der neuen Antwort
          self.text_response.delete("1.0", tk.END)
          self.text_response.insert(tk.END, new_response)
          self.result = new_response
          self.label_status.config(text="Antwort wurde erfolgreich überarbeitet!")
        else:
          messagebox.showerror("API-Fehler", f"Fehler bei der API-Anfrage: {response.status_code}\n{response.text}")
          self.label_status.config(text="Fehler bei der API-Anfrage!")
      else:
        messagebox.showwarning("API-Schlüssel fehlt", "Kein Anthropic API-Schlüssel gefunden. Bitte überprüfen Sie Ihre config.py.")
        self.label_status.config(text="Fehler: Kein API-Schlüssel gefunden!")
    
    except Exception as e:
      messagebox.showerror("Fehler", f"Fehler bei der Kommunikation mit der KI: {str(e)}")
      self.label_status.config(text="Fehler bei der Kommunikation mit der KI!")
  
  def accept_response(self):
    """Übernimmt die aktuelle Antwort und schließt den Dialog"""
    self.result = self.text_response.get("1.0", tk.END)
    self.master.destroy()
  
  def edit_manually(self):
    """Öffnet ein Fenster zur manuellen Bearbeitung der Antwort"""
    edit_window = tk.Toplevel(self.master)
    edit_window.title("Manuelle Bearbeitung")
    edit_window.geometry("800x600")
    
    tk.Label(edit_window, text="Bearbeiten Sie die Antwort direkt:", font=("Arial", 12, "bold")).pack(pady=(10, 5), padx=10, anchor=tk.W)
    
    text_edit = scrolledtext.ScrolledText(edit_window, wrap=tk.WORD, height=25, font=("Arial", 10))
    text_edit.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)
    text_edit.insert(tk.END, self.text_response.get("1.0", tk.END))
    
    def save_edits():
      new_text = text_edit.get("1.0", tk.END)
      self.text_response.delete("1.0", tk.END)
      self.text_response.insert(tk.END, new_text)
      self.result = new_text
      self.label_status.config(text="Antwort wurde manuell bearbeitet!")
      edit_window.destroy()
    
    tk.Button(edit_window, text="Änderungen übernehmen", command=save_edits, bg="#4CAF50", fg="white", 
         font=("Arial", 11, "bold"), pady=5, padx=10).pack(pady=10)
  
  def copy_to_clipboard(self):
    """Kopiert die aktuelle Antwort in die Zwischenablage"""
    text = self.text_response.get("1.0", tk.END)
    if has_pyperclip:
      try:
        pyperclip.copy(text)
        self.label_status.config(text="Antwort wurde in die Zwischenablage kopiert!")
      except Exception as e:
        messagebox.showerror("Fehler", f"Fehler beim Kopieren: {str(e)}")
        self.label_status.config(text="Fehler beim Kopieren in die Zwischenablage!")
    else:
      messagebox.showinfo("Hinweis", "Das Paket 'pyperclip' ist nicht installiert. Bitte installieren Sie es mit 'pip install pyperclip'.")

def get_tex_files(language="en"):
  """Findet alle TeX-Dateien in den konfigurierten Verzeichnissen"""
  tex_files = []
  
  # Wähle das Verzeichnis basierend auf der Sprache
  target_dirs = []
  if language == "en":
    target_dirs.append(TEX_DIRS[0]) # Englisches Verzeichnis
  elif language == "de":
    target_dirs.append(TEX_DIRS[1]) # Deutsches Verzeichnis
  else:
    target_dirs = TEX_DIRS # Beide Verzeichnisse
  
  # Suche nach TeX-Dateien in den Zielverzeichnissen
  for directory in target_dirs:
    try:
      if os.path.exists(directory) and os.path.isdir(directory):
        for file in os.listdir(directory):
          if file.lower().endswith(('.tex', '.latex')):
            tex_files.append(os.path.join(directory, file))
        print(f"Verzeichnis gefunden: {directory} - {len([f for f in os.listdir(directory) if f.lower().endswith(('.tex', '.latex'))])} TeX-Dateien")
      else:
        print(f"Verzeichnis nicht gefunden oder nicht zugänglich: {directory}")
    except Exception as e:
      print(f"Fehler beim Zugriff auf Verzeichnis {directory}: {e}")
  
  # Wenn keine TeX-Dateien gefunden wurden, durchsuche auch das aktuelle Verzeichnis als Fallback
  if not tex_files:
    try:
      for file in os.listdir(CURRENT_DIR):
        if file.lower().endswith(('.tex', '.latex')):
          tex_files.append(os.path.join(CURRENT_DIR, file))
      print(f"Verwende Fallback - Aktuelles Verzeichnis: {len([f for f in os.listdir(CURRENT_DIR) if f.lower().endswith(('.tex', '.latex'))])} TeX-Dateien")
    except Exception as e:
      print(f"Fehler beim Zugriff auf aktuelles Verzeichnis: {e}")
  
  return tex_files

def get_pdf_files():
  """Findet alle PDF-Dateien im aktuellen Verzeichnis als Fallback"""
  pdf_files = []
  try:
    for file in os.listdir(CURRENT_DIR):
      if file.lower().endswith('.pdf'):
        pdf_files.append(os.path.join(CURRENT_DIR, file))
  except Exception as e:
    print(f"Fehler beim Zugriff auf aktuelles Verzeichnis für PDFs: {e}")
  
  return pdf_files

def extract_repository_url(file_content):
  """Extrahiert die Repository-URL aus dem Dokument-Inhalt"""
  # Suche nach URLs, die dem Repository-Muster entsprechen
  urls = re.findall(REPOSITORY_URL_PATTERN, file_content)
  if urls:
    return urls[0] # Erste gefundene URL zurückgeben
  return None

def generate_repository_url(filename):
  """Generiert eine Repository-URL basierend auf dem Dateinamen"""
  # Nur den Basisnamen ohne Pfad und mit .pdf-Endung verwenden
  base_filename = os.path.basename(filename)
  if not base_filename.lower().endswith('.pdf'):
    base_filename += '.pdf'
  
  # URL zusammensetzen
  return DEFAULT_REPOSITORY_BASE + base_filename

def parse_tex_file(file_path):
  """Parse a LaTeX file and extract structured content"""
  try:
    with open(file_path, 'r', encoding='utf-8') as f:
      content = f.read()
  except UnicodeDecodeError:
    try:
      with open(file_path, 'r', encoding='latin-1') as f:
        content = f.read()
    except Exception as e:
      print(f" Fehler beim Lesen der Datei {os.path.basename(file_path)}: {e}")
      return [], None
  
  # Repository-URL aus dem Inhalt extrahieren
  repository_url = extract_repository_url(content)
  
  # Entferne Kommentare
  content = re.sub(r'(?m)^%.*$', '', content) # Kommentarzeilen entfernen
  content = re.sub(r'(?<!\\)%.*?$', '', content, flags=re.MULTILINE) # Inline-Kommentare entfernen

  # Extrahiere Abschnitte mit Überschriften
  sections = []
  
  # Finde Dokument-Umgebung
  document_match = re.search(r'\\begin{document}(.*?)\\end{document}', content, re.DOTALL)
  if document_match:
    document_content = document_match.group(1)
  else:
    document_content = content

  # Extrahiere Kapitel, Abschnitte, Unterabschnitte
  section_pattern = r'\\(sub)*section\{([^}]*)\}(.*?)(?=\\(sub)*section\{|$)'
  for match in re.finditer(section_pattern, document_content, re.DOTALL):
    section_type = match.group(1) or "section"
    section_title = match.group(2)
    section_content = match.group(3)
    
    # Entferne LaTeX-Befehle
    clean_content = re.sub(r'\\[a-zA-Z]+(\[.*?\])*(\{.*?\})*', ' ', section_content)
    clean_content = re.sub(r'\\\(|\\\)', ' ', clean_content) # Inline-Mathe
    clean_content = re.sub(r'\$\$.*?\$\$', ' ', clean_content, flags=re.DOTALL) # Display-Mathe
    clean_content = re.sub(r'\$.*?\$', ' ', clean_content) # Inline-Mathe
    
    # Teile in Absätze
    paragraphs = re.split(r'\n\s*\n', clean_content)
    for paragraph in paragraphs:
      clean_paragraph = re.sub(r'\s+', ' ', paragraph).strip()
      if clean_paragraph and len(clean_paragraph) > 50:
        sections.append({
          'title': section_title,
          'content': clean_paragraph,
          'type': section_type
        })
  
  return sections, repository_url

def extract_tex_content(topic, language="en"):
  """Durchsucht TeX-Dateien nach relevanten Inhalten zum Thema"""
  tex_files = get_tex_files(language)
  
  if not tex_files:
    print("Keine TeX-Dateien gefunden.")
    return {}
  
  # Suchbegriffe aus dem Thema extrahieren
  search_terms = topic.lower().split()
  additional_terms = []
  
  # Verwandte Begriffe hinzufügen (für bessere Suchergebnisse)
  topic_related_terms = {
    "dark matter": ["galaxy", "rotation", "curve", "missing mass", "halo"],
    "black hole": ["singularity", "horizon", "hawking", "entropy"],
    "quantum": ["mechanics", "superposition", "wave function", "particle"],
    "relativity": ["einstein", "spacetime", "curvature", "lorentz"],
    "gravity": ["force", "attraction", "gravitational", "newton"],
    "cosmology": ["universe", "expansion", "cosmic", "microwave", "background"],
    "particle": ["higgs", "boson", "electron", "standard model", "fermion"],
    "energy": ["conservation", "potential", "kinetic", "field"],
    "field": ["theory", "potential", "interaction", "quantum"]
  }
  
  # Verwandte Suchbegriffe hinzufügen
  for key, related_terms in topic_related_terms.items():
    if any(term in topic.lower() for term in key.split()):
      additional_terms.extend(related_terms)
  
  all_search_terms = search_terms + additional_terms
  
  # Ergebniscontainer
  results = defaultdict(list)
  repository_urls = {} # Speichere URLs für jede Datei
  
  print(f"\nSuche nach Inhalten zu '{topic}' in {len(tex_files)} TeX-Dokumenten...")
  print(f"Suchbegriffe: {', '.join(all_search_terms)}")
  
  for tex_path in tex_files:
    filename = os.path.basename(tex_path)
    print(f" Durchsuche: {filename}")
    
    try:
      # TeX-Datei parsen
      sections, repo_url = parse_tex_file(tex_path)
      
      # Repository-URL speichern
      if repo_url:
        repository_urls[filename] = repo_url
      else:
        # Fallback: URL basierend auf Dateinamen generieren
        repository_urls[filename] = generate_repository_url(filename)
      
      # Relevante Abschnitte finden
      for i, section in enumerate(sections):
        content = section['content'].lower()
        title = section['title'].lower()
        
        # Relevanz bewerten
        relevance_score = 0
        matched_terms = []
        
        # Prüfen, ob Suchbegriffe im Titel oder Inhalt vorkommen
        for term in all_search_terms:
          # Titel-Treffer sind besonders relevant
          if term in title:
            relevance_score += 3
            matched_terms.append(term)
          
          # Inhalt-Treffer
          if term in content:
            matches = len(re.findall(r'\b' + re.escape(term) + r'\b', content))
            relevance_score += matches
            if term not in matched_terms:
              matched_terms.append(term)
        
        # Nur relevante Abschnitte speichern
        if relevance_score > 0:
          results[filename].append({
            'title': section['title'],
            'text': section['content'],
            'relevance': relevance_score,
            'matched_terms': matched_terms,
            'section_type': section['type']
          })
    
    except Exception as e:
      print(f" Fehler bei {filename}: {e}")
  
  # Ergebnisse sortieren und begrenzen
  for filename in results:
    results[filename] = sorted(results[filename], key=lambda x: x['relevance'], reverse=True)
    # Nur die 3 relevantesten pro Datei behalten
    results[filename] = results[filename][:3]
  
  return results, repository_urls

def extract_from_pdf(topic):
  """Fallback-Funktion zur Suche in PDF-Dateien, falls keine TeX-Dateien verfügbar sind"""
  try:
    import PyPDF2
    has_pypdf2 = True
  except ImportError:
    print("Hinweis: Das Paket 'PyPDF2' ist nicht installiert.")
    print("Die PDF-Durchsuchung ist nicht verfügbar.")
    print("Installieren Sie es mit 'pip install PyPDF2' für PDF-Zugriff.")
    return {}, {}
  
  pdf_files = get_pdf_files()
  if not pdf_files:
    print("Keine PDF-Dateien gefunden.")
    return {}, {}
  
  # Suchbegriffe aus dem Thema extrahieren
  search_terms = topic.lower().split()
  additional_terms = []
  
  # Verwandte Begriffe (identisch mit TeX-Suche)
  topic_related_terms = {
    "dark matter": ["galaxy", "rotation", "curve", "missing mass", "halo"],
    "black hole": ["singularity", "horizon", "hawking", "entropy"],
    "quantum": ["mechanics", "superposition", "wave function", "particle"],
    "relativity": ["einstein", "spacetime", "curvature", "lorentz"],
    "gravity": ["force", "attraction", "gravitational", "newton"],
    "cosmology": ["universe", "expansion", "cosmic", "microwave", "background"],
    "particle": ["higgs", "boson", "electron", "standard model", "fermion"],
    "energy": ["conservation", "potential", "kinetic", "field"],
    "field": ["theory", "potential", "interaction", "quantum"]
  }
  
  # Verwandte Suchbegriffe hinzufügen
  for key, related_terms in topic_related_terms.items():
    if any(term in topic.lower() for term in key.split()):
      additional_terms.extend(related_terms)
  
  all_search_terms = search_terms + additional_terms
  
  # Ergebniscontainer
  results = defaultdict(list)
  repository_urls = {} # Speichere URLs für jede Datei
  
  print(f"\nSuche nach Inhalten zu '{topic}' in {len(pdf_files)} PDF-Dokumenten...")
  print(f"Suchbegriffe: {', '.join(all_search_terms)}")
  
  for pdf_path in pdf_files:
    filename = os.path.basename(pdf_path)
    print(f" Durchsuche: {filename}")
    
    try:
      # PDF öffnen
      reader = PyPDF2.PdfReader(pdf_path)
      total_pages = len(reader.pages)
      
      # Repository-URL aus der PDF extrahieren (erste Seite für Metadaten)
      first_page = reader.pages[0]
      first_page_text = first_page.extract_text() or ""
      repo_url = extract_repository_url(first_page_text)
      
      if repo_url:
        repository_urls[filename] = repo_url
      else:
        # Fallback: URL basierend auf Dateinamen generieren
        repository_urls[filename] = generate_repository_url(filename)
      
      # Relevante Textabschnitte sammeln
      for page_num in range(total_pages):
        page = reader.pages[page_num]
        text = page.extract_text() or ""
        
        # Text in Absätze aufteilen
        paragraphs = re.split(r'\n\s*\n', text)
        
        for paragraph in paragraphs:
          # Absatz bereinigen
          paragraph = paragraph.replace('\n', ' ').strip()
          if len(paragraph) < 50: # Zu kurze Absätze ignorieren
            continue
          
          # Relevanz bewerten
          relevance_score = 0
          matched_terms = []
          for term in all_search_terms:
            if term in paragraph.lower():
              matches = len(re.findall(r'\b' + re.escape(term) + r'\b', paragraph.lower()))
              relevance_score += matches
              if term not in matched_terms:
                matched_terms.append(term)
          
          # Nur relevante Absätze speichern
          if relevance_score > 0:
            results[filename].append({
              'title': f"Page {page_num + 1}",
              'text': paragraph,
              'relevance': relevance_score,
              'matched_terms': matched_terms,
              'page': page_num + 1
            })
    
    except Exception as e:
      print(f" Fehler bei {filename}: {e}")
  
  # Ergebnisse sortieren und begrenzen
  for filename in results:
    results[filename] = sorted(results[filename], key=lambda x: x['relevance'], reverse=True)
    results[filename] = results[filename][:3] # Nur die relevantesten behalten
  
  return results, repository_urls

def generate_ai_response(topic, content_extracts, repository_urls, post_details=None):
  """Generiert eine Antwort mit Anthropic Claude API basierend auf dem Thema, den extrahierten Inhalten 
  und optional den Post-Details"""
  
  # Überprüfen des API-Schlüssels
  if not ANTHROPIC_API_KEY:
    print("\nKein gültiger Anthropic API-Schlüssel gefunden.")
    print("Bitte stellen Sie sicher, dass Ihre config.py Datei korrekt ist.")
    print("Stattdessen wird eine vordefinierte Vorlage verwendet.\n")
    
    # Fallback zu den vordefinierten Vorlagen, wenn kein API-Schlüssel angegeben ist
    template = random.choice([
      "Interesting discussion about {topic}! The T0 model offers a unique perspective through time-mass duality, where time is considered absolute and mass is variable. This framework provides an alternative explanation for phenomena related to {topic} without requiring dark matter or dark energy.",
      
      "Looking at {topic} through the T0 model lens reveals interesting insights. In this framework, which is based on an intrinsic time field T(x) = ℏ/max(mc², ω), we can bridge quantum mechanics and relativity theory without the typical contradictions.",
      
      "The challenges in {topic} could be approached differently using the T0 model. By treating time as absolute and mass as variable (contrary to conventional relativity), we can derive emergent gravitation from time field gradients, potentially addressing some of the open questions in {topic}."
    ])
    
    response = template.format(topic=topic)
    
    # Extrakte hinzufügen, falls vorhanden
    if content_extracts:
      has_content = False
      
      # Die relevantesten Dokumente auswählen (maximal 2)
      top_documents = []
      for filename, extracts in content_extracts.items():
        if extracts:
          top_documents.append((filename, extracts))
      
      # Nach Relevanz der besten Extrakte sortieren
      top_documents.sort(key=lambda x: max(extract['relevance'] for extract in x[1]), reverse=True)
      top_documents = top_documents[:2] # Maximal 2 Dokumente
      
      if top_documents:
        response += "\n\nIn my research on the T0 model, I've specifically addressed this topic:"
        
        for filename, extracts in top_documents:
          if extracts:
            # Saubereren Dokumentnamen erstellen (ohne Dateiendung)
            doc_name = os.path.splitext(filename)[0]
            # Entferne Unterstrich, Bindestrich etc. und ersetze sie durch Leerzeichen
            doc_name = re.sub(r'[_\-]', ' ', doc_name)
            
            # Repository-URL für dieses Dokument
            repo_url = repository_urls.get(filename, generate_repository_url(filename))
            
            response += f"\n\nFrom my paper '[{doc_name}]({repo_url})':"
            
            # Den relevantesten Extrakt auswählen
            best_extract = extracts[0]
            
            # Absatz kürzen, wenn er zu lang ist
            extract_text = best_extract['text']
            words = extract_text.split()
            if len(words) > 100:
              extract_text = ' '.join(words[:100]) + "..."
            
            # Referenz je nach Typ (TeX-Abschnitt oder PDF-Seite)
            if 'section_type' in best_extract:
              reference = f"section: {best_extract['title']}"
            elif 'page' in best_extract:
              reference = f"page {best_extract['page']}"
            else:
              reference = ""
            
            response += f"\n\"{extract_text}\" ({reference})"
            has_content = True
      
      if not has_content:
        response += "\n\nMy research on the T0 model provides a comprehensive framework for understanding such phenomena through time-mass duality and the intrinsic time field."
    else:
      response += "\n\nMy research on the T0 model develops this concept in detail, offering a unified approach to quantum mechanics and relativity through the principle of time-mass duality."
    
    # Abschließender Verweis mit Repository-Link zur Hauptseite
    response += "\n\nFor more information on the T0 model and time-mass duality, you can explore my published papers at [my research repository](https://github.com/johannpascher/t0-model)."
    
    return response
  
  # Anthropic Claude API nutzen, wenn ein API-Schlüssel vorhanden ist
  try:
    # Erstellen Sie einen Prompt für Claude
    prompt = T0_MODEL_INTRO + f"\n\nThema der Diskussion: {topic}\n\n"
    
    # Post-Details zum Prompt hinzufügen, falls vorhanden
    if post_details:
      title, text = post_details
      prompt += f"Post-Text zum Beantworten:\n\n"
      prompt += f"Titel: {title}\n\n"
      
      if text:
        prompt += f"Text des Posts:\n{text}\n\n"
    
    # Extrahierte Inhalte zum Prompt hinzufügen
    if content_extracts:
      prompt += "Relevante Auszüge aus meinen Forschungsdokumenten:\n\n"
      
      # Alle relevanten Dokumente betrachten
      for filename, extracts in content_extracts.items():
        if extracts:
          # Saubereren Dokumentnamen erstellen (ohne Dateiendung)
          doc_name = os.path.splitext(filename)[0]
          doc_name = re.sub(r'[_\-]', ' ', doc_name)
          
          # Repository-URL für dieses Dokument
          repo_url = repository_urls.get(filename, generate_repository_url(filename))
          
          prompt += f"Aus dem Dokument '{doc_name}' ({repo_url}):\n"
          
          # Bis zu 2 der relevantesten Extrakte für dieses Dokument hinzufügen
          for i, extract in enumerate(extracts[:2]):
            # Referenz je nach Typ (TeX-Abschnitt oder PDF-Seite)
            if 'section_type' in extract:
              reference = f"Abschnitt: {extract['title']}"
            elif 'page' in extract:
              reference = f"Seite {extract['page']}"
            else:
              reference = ""
            
            prompt += f"- {extract['text']} ({reference})\n\n"
    
    # Weitere Anweisungen für die Antwort
    prompt += """
Bitte formuliere eine überzeugende Antwort, die:
1. Direkt auf den konkreten Post und dessen Inhalt eingeht (wenn vorhanden)
2. Das T0-Modell als Alternative zu bestehenden Theorien positioniert
3. Wissenschaftlich klingt, aber auch für interessierte Laien verständlich ist
4. Relevante Links zu meinen Forschungspapieren enthält, falls diese zum Thema passen
5. Endet mit einem Verweis auf mein Repository: https://github.com/johannpascher/t0-model

Wichtig: Die Antwort sollte in Markdown-Format sein.
Die Antwort sollte nicht zu lang sein, aber dennoch detailliert genug, um Interesse zu wecken.
"""
    
    # API-Anfrage an Anthropic Claude senden
    headers = {
      "x-api-key": ANTHROPIC_API_KEY,
      "anthropic-version": "2023-06-01",
      "content-type": "application/json"
    }
    
    data = {
      "model": "claude-3-haiku-20240307",
      "max_tokens": 1024,
      "messages": [
        {"role": "user", "content": prompt}
      ]
    }
    
    print("\nSende Anfrage an Claude API...")
    response = requests.post(
      "https://api.anthropic.com/v1/messages",
      headers=headers,
      json=data
    )
    
    if response.status_code == 200:
      response_json = response.json()
      ai_response = response_json['content'][0]['text']
      print("Antwort erfolgreich von Claude API erhalten.")
      return ai_response
    else:
      print(f"\nFehler bei der API-Anfrage: {response.status_code}")
      print(f"Fehlerdetails: {response.text}")
      print("Verwende vordefinierte Vorlage als Fallback...")
      # Bei Fehler zur vordefinierten Vorlage zurückkehren
      template = random.choice([
        "Interesting discussion about {topic}! The T0 model offers a unique perspective through time-mass duality, where time is considered absolute and mass is variable. This framework provides an alternative explanation for phenomena related to {topic} without requiring dark matter or dark energy.",
        
        "Looking at {topic} through the T0 model lens reveals interesting insights. In this framework, which is based on an intrinsic time field T(x) = ℏ/max(mc², ω), we can bridge quantum mechanics and relativity theory without the typical contradictions.",
        
        "The challenges in {topic} could be approached differently using the T0 model. By treating time as absolute and mass as variable (contrary to conventional relativity), we can derive emergent gravitation from time field gradients, potentially addressing some of the open questions in {topic}."
      ])
      
      response = template.format(topic=topic)
      return response
  
  except Exception as e:
    print(f"\nFehler bei der Verwendung der Anthropic API: {e}")
    print("Verwende vordefinierte Vorlage als Fallback...")
    # Bei Ausnahmefehlern ebenfalls zur vordefinierten Vorlage zurückkehren
    template = random.choice([
      "Interesting discussion about {topic}! The T0 model offers a unique perspective through time-mass duality, where time is considered absolute and mass is variable. This framework provides an alternative explanation for phenomena related to {topic} without requiring dark matter or dark energy.",
      
      "Looking at {topic} through the T0 model lens reveals interesting insights. In this framework, which is based on an intrinsic time field T(x) = ℏ/max(mc², ω), we can bridge quantum mechanics and relativity theory without the typical contradictions.",
      
      "The challenges in {topic} could be approached differently using the T0 model. By treating time as absolute and mass as variable (contrary to conventional relativity), we can derive emergent gravitation from time field gradients, potentially addressing some of the open questions in {topic}."
    ])
    
    response = template.format(topic=topic)
    return response

def open_url_in_browser(url=None):
  """Öffnet einen Browser mit der angegebenen URL oder einem leeren Tab"""
  if not url:
    # Standard-URLs für physikalische Diskussionen
    example_urls = [
      "https://www.reddit.com/r/Physics/",
      "https://www.reddit.com/r/TheoreticalPhysics/",
      "https://www.reddit.com/r/AskPhysics/"
    ]
    
    # Auswahl einer URL
    print("\nMögliche Webseiten:")
    for i, url in enumerate(example_urls, 1):
      print(f"{i}. {url}")
    
    choice = input("\nWählen Sie eine Webseite (1-3) oder drücken Sie Enter für benutzerdefinierte Eingabe: ")
    
    if choice.strip() and choice.isdigit() and 1 <= int(choice) <= len(example_urls):
      url = example_urls[int(choice)-1]
    else:
      url = input("Geben Sie die URL ein, die Sie öffnen möchten: ")
  
  # Browser öffnen
  print(f"\nÖffne {url} im Browser...")
  try:
    webbrowser.open(url)
    print("Browser wurde geöffnet.")
  except Exception as e:
    print(f"Fehler beim Öffnen des Browsers: {e}")
    print(f"Bitte öffnen Sie diese URL manuell: {url}")

def main():
  os.system('cls' if os.name == 'nt' else 'clear') # Bildschirm löschen
  
  print("T0-Modell Antwortgenerator mit KI-Integration")
  print("=========================================")
  
  # TeX-Verzeichnisse prüfen
  print("\nPrüfe verfügbare TeX-Verzeichnisse...")
  for dir_path in TEX_DIRS:
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
      print(f" ✓ Gefunden: {dir_path}")
    else:
      print(f" ✗ Nicht gefunden: {dir_path}")
  
  # Sprachauswahl
  print("\nWählen Sie die Sprache für die Dokumentensuche:")
  print("1. Englisch")
  print("2. Deutsch")
  print("3. Beide Sprachen")
  
  lang_choice = input("Auswahl (1-3) [Standard: Englisch]: ")
  
  language = "en" # Standardmäßig Englisch
  if lang_choice == "2":
    language = "de"
  elif lang_choice == "3":
    language = "both"
  
  # TeX-Dateien finden
  tex_files = get_tex_files(language)
  
  # Auswahl der Eingabemethode
  print("\nWie möchten Sie das Thema eingeben?")
  print("1. Einen Post-Titel und -Text manuell eingeben")
  print("2. Einen Browser öffnen, um einen Post zu finden (nur URL kopieren)")
  print("3. Nur Thema eingeben (ohne Post-Text)")
  
  method_choice = input("Auswahl (1-3) [Standard: 1]: ")
  
  if not method_choice:
    method_choice = "1"
  
  # Post-Details und Thema definieren
  post_details = None
  topic = "theoretical physics" # Standardthema
  
  # Eine Haupt-Anwendung erstellen, die für Dialoge verwendet wird
  root = tk.Tk()
  root.withdraw() # Hauptfenster ausblenden, wir verwenden es nur für Dialoge
  
  if method_choice == "1":
    # Manuelles Eingeben von Post-Titel und -Text
    dialog = PostInputDialog(root)
    
    if dialog.result:
      post_details = dialog.result
      topic = post_details[0] # Titel als Thema verwenden
    else:
      # Dialog abgebrochen, nach Thema fragen
      topic = simpledialog.askstring("Thema eingeben", "Geben Sie das Thema der Diskussion ein:", parent=root) or topic
  
  elif method_choice == "2":
    # Browser öffnen, um einen Post zu finden
    open_url_in_browser()
    
    # Manuelles Eingeben von Post-Titel und -Text, nachdem der Browser geöffnet wurde
    print("\nAnleitung:")
    print("1. Durchsuchen Sie die Beiträge im geöffneten Browser-Tab")
    print("2. Finden Sie eine relevante Diskussion")
    print("3. Kopieren Sie Titel und Text")
    
    # Dialog zur Eingabe öffnen
    dialog = PostInputDialog(root)
    
    if dialog.result:
      post_details = dialog.result
      topic = post_details[0] # Titel als Thema verwenden
    else:
      # Dialog abgebrochen, nach Thema fragen
      topic = simpledialog.askstring("Thema eingeben", "Geben Sie das Thema der Diskussion ein:", parent=root) or topic
  
  else: # method_choice == "3" oder ungültig
    # Nur Thema eingeben
    topic = simpledialog.askstring("Thema eingeben", "Geben Sie das Thema der Diskussion ein:", parent=root) or topic
  
  # Stellen Sie sicher, dass das Thema nicht leer ist
  if not topic.strip():
    topic = "theoretical physics"
  
  # Content-Extrakte und Repository-URLs aus Dokumenten
  content_extracts = {}
  repository_urls = {}
  
  # In TeX-Dateien nach relevanten Inhalten suchen
  if tex_files:
    content_extracts, repository_urls = extract_tex_content(topic, language)
  
  # Wenn keine TeX-Dateien gefunden wurden oder keine relevanten Inhalte, versuche es mit PDFs
  if not content_extracts:
    print("Keine relevanten Inhalte in TeX-Dateien gefunden. Versuche PDFs...")
    content_extracts, pdf_repo_urls = extract_from_pdf(topic)
    # Repository-URLs aus PDFs hinzufügen
    repository_urls.update(pdf_repo_urls)
  
  # Antwort mit KI generieren
  print("\nGeneriere Antwort mit KI-Integration...")
  initial_response = generate_ai_response(topic, content_extracts, repository_urls, post_details)
  
  print("\nAntwort generiert. Öffne interaktiven Editor...")
  
  # Interaktiven Editor starten
  root.deiconify() # Hauptfenster wieder anzeigen
  editor = InteractiveEditor(root, initial_response, topic, content_extracts, repository_urls, post_details)
  root.mainloop()
  
  # Überarbeitete Antwort erhalten
  response = editor.result
  
  print("\nEndgültige Antwort:")
  print("=" * 50)
  print(response)
  print("=" * 50)
  
  # In die Zwischenablage kopieren
  if has_pyperclip:
    try:
      pyperclip.copy(response)
      print("\nDie Antwort wurde in die Zwischenablage kopiert!")
      print("Sie können sie nun einfügen (Strg+V).")
    except Exception as e:
      print(f"\nFehler beim Kopieren in die Zwischenablage: {e}")
      print("Bitte kopieren Sie die Antwort manuell:")
      print("-" * 50)
      print(response)
      print("-" * 50)
  else:
    print("\nBitte kopieren Sie die Antwort manuell:")
    print("-" * 50)
    print(response)
    print("-" * 50)
  
  print("\nViel Erfolg bei der Verbreitung Ihres T0-Modells!")
  
  # Fragen, ob noch eine weitere Antwort generiert werden soll
  another = input("\nMöchten Sie eine weitere Antwort generieren? (j/n): ")
  if another.lower() == 'j':
    main() # Programm neu starten

if __name__ == "__main__":
  print("Starte main()-Funktion...")
  main()
  print("main()-Funktion abgeschlossen.")
