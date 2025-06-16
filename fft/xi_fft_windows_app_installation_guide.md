# ξ-FFT Windows Anwendung - Installationsanleitung

Eine vollständige Anleitung zur Installation und Nutzung der ξ-FFT Schwebungs-Analyse Anwendung.

## 📋 Inhaltsverzeichnis

- [System-Anforderungen](#system-anforderungen)
- [Installation](#installation)
- [Erste Schritte](#erste-schritte)
- [Problemlösung](#problemlösung)
- [Funktionen der Anwendung](#funktionen-der-anwendung)
- [Support](#support)

---

## 🖥️ System-Anforderungen

### Betriebssystem
- ✅ **Windows 7/8/10/11** (32-bit oder 64-bit)
- ✅ **Linux** (Ubuntu, Debian, CentOS, etc.)
- ✅ **macOS** (10.12 oder höher)

### Hardware (Minimum)
- 💾 **Arbeitsspeicher:** 2 GB RAM
- 💽 **Festplattenspeicher:** 500 MB frei
- 🖥️ **Bildschirmauflösung:** 1024x768 Pixel
- 🎧 **Audio:** Soundkarte für WAV-Wiedergabe (optional)

### Hardware (Empfohlen)
- 💾 **Arbeitsspeicher:** 4 GB RAM oder mehr
- 💽 **Festplattenspeicher:** 1 GB frei
- 🖥️ **Bildschirmauflösung:** 1280x800 Pixel oder größer

---

## 🔧 Installation

### Schritt 1: Python installieren

#### Windows:
1. Besuchen Sie [python.org/downloads](https://python.org/downloads/)
2. Laden Sie die **neueste Python-Version** herunter (empfohlen: 3.8-3.11)
3. Führen Sie das Installationsprogramm aus
4. **⚠️ WICHTIG:** Setzen Sie den Haken bei **"Add Python to PATH"**
5. Klicken Sie auf "Install Now"

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3 python3-pip python3-tk
```

#### Linux (CentOS/RHEL):
```bash
sudo yum install python3 python3-pip tkinter
```

#### macOS:
```bash
# Mit Homebrew (empfohlen):
brew install python3

# Oder von python.org herunterladen
```

### Schritt 2: Erforderliche Pakete installieren

Öffnen Sie die **Eingabeaufforderung** (Windows) oder **Terminal** (Linux/Mac):

#### Windows:
- Windows-Taste + R drücken
- `cmd` eingeben und Enter drücken

#### Dann für alle Systeme:
```bash
pip install numpy matplotlib
```

**Alternative (falls pip nicht funktioniert):**
```bash
python -m pip install numpy matplotlib
```

### Schritt 3: Anwendung herunterladen

1. Speichern Sie den Python-Code als `xi_fft_app.py`
2. Legen Sie die Datei in einen Ordner Ihrer Wahl (z.B. `C:\ξ-FFT\`)

### Schritt 4: Installation testen

Erstellen Sie eine Testdatei `test_installation.py`:

```python
#!/usr/bin/env python3
"""
Test der ξ-FFT Installation
"""

import sys
print("🔍 Teste ξ-FFT Installation...")
print(f"Python Version: {sys.version}")

try:
    import numpy as np
    print(f"✅ NumPy {np.__version__} - OK")
except ImportError:
    print("❌ NumPy fehlt - bitte installieren: pip install numpy")
    exit(1)

try:
    import matplotlib
    print(f"✅ Matplotlib {matplotlib.__version__} - OK")
except ImportError:
    print("❌ Matplotlib fehlt - bitte installieren: pip install matplotlib")
    exit(1)

try:
    import tkinter as tk
    print("✅ Tkinter - OK")
except ImportError:
    print("❌ Tkinter fehlt - bitte Python neu installieren oder tkinter nachinstallieren")
    exit(1)

try:
    import wave
    print("✅ Wave - OK")
except ImportError:
    print("❌ Wave fehlt (sollte Standard-Bibliothek sein)")
    exit(1)

print("\n🎉 Alle Abhängigkeiten erfolgreich installiert!")
print("Die ξ-FFT Anwendung sollte funktionieren.")
```

Führen Sie den Test aus:
```bash
python test_installation.py
```

---

## 🚀 Erste Schritte

### Anwendung starten

1. **Eingabeaufforderung öffnen** (Windows + R → `cmd`)
2. **Zum Anwendungsordner navigieren:**
   ```bash
   cd C:\ξ-FFT\
   ```
3. **Anwendung starten:**
   ```bash
   python xi_fft_app.py
   ```

### Grundlegende Nutzung

#### 1. Signal-Generator (Tab 1)
- **Grundfrequenz f₀:** Hauptfrequenz in Hz (z.B. 440 Hz = A4)
- **Schwebung Δf:** Schwebungsfrequenz in Hz (z.B. 5 Hz)
- **Dauer:** Signal-Länge in Sekunden (1-10s)

**Schritte:**
1. Parameter einstellen
2. "🎵 3-Ton Signal generieren" klicken
3. "🔍 ξ-FFT Analysieren" klicken
4. Ergebnisse im Tab "Analyse-Ergebnisse" betrachten

#### 2. Datei-Analyse (Tab 2)
- **WAV-Datei laden:** "📂 WAV-Datei auswählen"
- **Frequenzbereich:** Min/Max Frequenz für Analyse
- **Auflösung:** Genauigkeit der Analyse
- **Threshold:** Mindest-Amplitude für Peak-Erkennung

**Schritte:**
1. WAV-Datei auswählen
2. Analyse-Parameter einstellen
3. "🔍 Datei analysieren" klicken
4. Ergebnisse betrachten

#### 3. Erweiterte Einstellungen

**Auflösung:**
- **Ultra High (0.1 Hz):** Sehr präzise, aber langsam
- **High (0.25 Hz):** Hohe Genauigkeit
- **Medium (0.5 Hz):** Standard (empfohlen)
- **Low (1.0 Hz):** Schnell für Überblick
- **Fast (2.0 Hz):** Sehr schnell, aber ungenau

**Amplituden-Filter:**
- Aktivieren um schwache oder starke Signale zu filtern
- **Min. Amplitude:** Filtert schwache Signale heraus
- **Max. Amplitude:** Begrenzt starke Signale (Clipping-Schutz)

---

## 🔧 Problemlösung

### Häufige Probleme

#### Problem: "pip wird nicht erkannt"
**Lösung:**
```bash
python -m pip install numpy matplotlib
```

#### Problem: "tkinter nicht gefunden"
**Windows:** Python neu installieren mit "Add to PATH"
**Linux:**
```bash
sudo apt-get install python3-tk
```

#### Problem: "ModuleNotFoundError: No module named 'numpy'"
**Lösung:**
```bash
pip install --user numpy matplotlib
```

#### Problem: Anwendung startet nicht
**Prüfung:**
1. Python-Version prüfen: `python --version`
2. Pakete prüfen: `pip list | grep numpy`
3. Test-Script ausführen (siehe oben)

#### Problem: Langsame Analyse
**Optimierung:**
- Auflösung auf "Low" oder "Fast" stellen
- Kleineren Frequenzbereich wählen
- Kürzere Signale verwenden (1-2 Sekunden)

#### Problem: Keine Peaks gefunden
**Mögliche Ursachen:**
- Threshold zu hoch → Wert reduzieren (z.B. 0.001)
- Falscher Frequenzbereich → Bereich erweitern
- Signal zu schwach → Amplituden-Filter deaktivieren
- WAV-Datei stumm oder beschädigt

### Erweiterte Problemlösung

#### Installation in virtueller Umgebung (empfohlen)
```bash
# Virtuelle Umgebung erstellen
python -m venv xi_fft_env

# Aktivieren (Windows):
xi_fft_env\Scripts\activate

# Aktivieren (Linux/Mac):
source xi_fft_env/bin/activate

# Pakete installieren
pip install numpy matplotlib

# Anwendung starten
python xi_fft_app.py
```

#### Anaconda-Installation (Alternative)
```bash
# Anaconda installieren von anaconda.com
# Dann:
conda create -n xi_fft python=3.9
conda activate xi_fft
conda install numpy matplotlib tkinter
python xi_fft_app.py
```

---

## 🎵 Funktionen der Anwendung

### Signal-Generator
- **3-Frequenz Schwebungs-Signale** (f₀±Δf)
- **Einstellbare Parameter:** Grundfrequenz, Schwebungsrate, Dauer
- **Live-Frequenz-Anzeige** der generierten Töne
- **WAV-Export** der generierten Signale

### ξ-FFT Analyse-Engine
- **Spektralanalyse** mit Discrete Fourier Transform (DFT)
- **ξ-Verhältnisse** zwischen Frequenz-Peaks
- **Konfigurierbare Auflösung** (0.1 Hz - 2.0 Hz)
- **Amplituden-Filter** für Signal-Vorverarbeitung

### Datei-Analyse
- **WAV-Import** (Mono/Stereo, 8/16-bit)
- **Segment-Analyse** (erste 3 Sekunden für Performance)
- **Flexibler Frequenzbereich** (20 Hz - 5000 Hz)
- **WAV-Export** der analysierten Segmente

### Visualisierung
- **Zeitverlauf (Waveform):** Signal über Zeit
- **Frequenzspektrum:** Magnitude vs. Frequenz
- **Peak-Analyse:** Erkannte Frequenzen mit ξ-Verhältnissen
- **Detaillierte Text-Ausgabe** mit harmonischer Analyse

### Schwebungs-Erkennung
- **Automatische Erkennung** von Schwebungsmustern
- **Vergleich** mit erwarteten Werten (Generator)
- **Harmonische Klassifikation** (Oktave, Quinte, etc.)
- **Präzisionsmessung** mit Abweichungsanalyse

---

## 📊 Technische Details

### Unterstützte Audioformate
- **WAV:** Mono/Stereo, 8/16-bit, alle Sample-Raten
- **Export:** WAV, 16-bit, Mono, 44.1 kHz

### Analyse-Parameter
- **Frequenzbereich:** 20 Hz - 20 kHz (einstellbar)
- **Auflösung:** 0.1 Hz - 2.0 Hz
- **Threshold:** 0.001 - 0.1 (Magnitude)
- **Max. Signal-Länge:** 3 Sekunden (für Performance)

### Performance
- **Kleine Signale** (1-2s): Sekunden
- **Große Signale** (3s+): Minuten (je nach Auflösung)
- **Memory Usage:** ~100-500 MB (abhängig von Signal-Größe)

---

## 🆘 Support

### Bei Problemen
1. **Installations-Test** ausführen
2. **Konsolen-Ausgabe** prüfen (Fehlermeldungen)
3. **Python-Version** prüfen (`python --version`)
4. **Pakete aktualisieren:** `pip install --upgrade numpy matplotlib`

### Erweiterte Hilfe
- **Python-Dokumentation:** [docs.python.org](https://docs.python.org)
- **NumPy-Dokumentation:** [numpy.org](https://numpy.org)
- **Matplotlib-Dokumentation:** [matplotlib.org](https://matplotlib.org)

### System-Informationen sammeln
```python
import sys, platform, numpy, matplotlib
print(f"System: {platform.system()} {platform.release()}")
print(f"Python: {sys.version}")
print(f"NumPy: {numpy.__version__}")
print(f"Matplotlib: {matplotlib.__version__}")
```

---

## 📝 Lizenz und Verwendung

Diese Anwendung ist für **Bildungs- und Forschungszwecke** konzipiert.

### Eigenschaften
- **Open Source** Python-Code
- **Keine kommerziellen Abhängigkeiten**
- **Plattformübergreifend** (Windows/Linux/Mac)
- **Offline-Nutzung** möglich

### Anwendungsgebiete
- **Akustik-Forschung** und -Lehre
- **Musik-Analyse** und Harmonie-Studien
- **Signal-Processing** Experimente
- **Schwebungs-Phänomen** Demonstration

---

*Letzte Aktualisierung: 13. Juni 2025*
*Version: 1.0*