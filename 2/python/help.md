# T0-Kosmische Fehlerkorrektur - Dokumentation

## 📋 Überblick
Das `t0_cosmic_error_correction.py` Skript implementiert eine **kosmisch-synchrone Fehlerkorrektur** für Quantencomputing basierend auf fraktalen Torus-Universum-Parametern.

## 🚀 Schnellstart

### Installation der Abhängigkeiten
```powershell
# Virtual Environment erstellen (empfohlen)
py -m venv cosmic_env
.\cosmic_env\Scripts\Activate.ps1

# Pakete installieren
pip install numpy ephem
```

### Basis-Ausführung
```powershell
# Immer 'python' oder 'py' vor dem Skript verwenden!
python t0_cosmic_error_correction.py --complete --verbose
```

## ⚙️ Befehlszeilenoptionen

### Hauptoptionen
| Option | Beschreibung | Beispiel |
|--------|-------------|----------|
| `--complete` | Vollständige Analyse durchführen | `--complete --verbose` |
| `--find-best-time` | Optimale Startzeit finden | `--find-best-time --algorithm grover` |
| `--realistic-simulation` | Realistische Schaltungssimulation | `--realistic-simulation --gates 50` |
| `--threshold-analysis` | Fehlerschwellen-Analyse | `--threshold-analysis --all-codes` |
| `--adaptive-schedule` | Adaptiven Zeitplan erstellen | `--adaptive-schedule --duration 8` |

### Parameter
| Parameter | Standard | Beschreibung |
|-----------|----------|-------------|
| `--xi` | 0.001 | Fraktaler Parameter ξ (4/30000 = 0.000133) |
| `--location` | "47.3769,8.5417" | Geografische Koordinaten "lat,lon" |
| `--qubits` | 12 | Anzahl Qubits für Analyse |
| `--algorithm` | shor | Algorithmustyp (shor, grover, vqe, qml) |
| `--lookahead` | 48 | Vorausschau in Stunden |
| `--gates` | 20 | Anzahl Gatter für Simulation |
| `--duration` | 6 | Dauer für Zeitplan in Stunden |

### Output-Optionen
| Option | Beschreibung |
|--------|-------------|
| `--verbose` | Detaillierte Ausgabe |
| `--quiet` | Minimale Ausgabe |
| `--debug` | Debug-Informationen |
| `--output DATEI` | Ergebnisse speichern |
| `--save-results` | Automatisch speichern |

## 🎯 Anwendungsbeispiele

### 1. Komplette Analyse
```powershell
# Standardanalyse
python t0_cosmic_error_correction.py --complete

# Mit erweiterten Parametern
python t0_cosmic_error_correction.py --complete --qubits 16 --xi 0.0015 --verbose

# Für bestimmten Standort
python t0_cosmic_error_correction.py --complete --location "52.5200,13.4050" --output berlin.json
```

### 2. Zeitoptimierung
```powershell
# Beste Zeit für Shor-Algorithmus
python t0_cosmic_error_correction.py --find-best-time --algorithm shor --lookahead 72

# Alle Algorithmen vergleichen
python t0_cosmic_error_correction.py --find-best-time --algorithm all --verbose
```

### 3. Realistische Simulation
```powershell
# 100-Gatter Simulation
python t0_cosmic_error_correction.py --realistic-simulation --gates 100

# Mit Debug-Output
python t0_cosmic_error_correction.py --realistic-simulation --gates 50 --debug
```

### 4. Fehlerschwellen-Analyse
```powershell
# Alle Quantencodes analysieren
python t0_cosmic_error_correction.py --threshold-analysis --all-codes

# Nur Cosmic Code
python t0_cosmic_error_correction.py --threshold-analysis --code-type cosmic_code
```

### 5. Adaptiver Zeitplan
```powershell
# 8-Stunden Plan
python t0_cosmic_error_correction.py --adaptive-schedule --duration 8

# Detaillierte Ausgabe
python t0_cosmic_error_correction.py --adaptive-schedule --duration 12 --verbose
```

## 📊 Ausgabe-Interpretation

### Korrekturfaktor
- **> 1.05**: Sehr günstige Bedingungen → SOFORT STARTEN
- **1.0 - 1.05**: Gute Bedingungen → Für kritische Berechnungen geeignet
- **0.95 - 1.0**: Neutrale Bedingungen → Für nicht-kritische Berechnungen
- **< 0.95**: Ungünstige Bedingungen → WARTEN

### Algorithmus-optimale Zeiten
- **Shor**: 02:00-06:00, 14:00-18:00
- **Grover**: 00:00-04:00, 20:00-24:00
- **VQE**: 08:00-12:00, 16:00-20:00
- **QML**: 06:00-10:00, 18:00-22:00

### Quantencodes
| Code | Theoretische Schwelle | Realistische Schwelle | Overhead |
|------|---------------------|----------------------|----------|
| Surface Code | 1% | 0.5% | 9:1 |
| Color Code | 2% | 0.8% | 7:1 |
| Repetition Code | 5% | 2% | 5:1 |
| Cosmic Code | ξ×50 | ξ×25 | 3/ξ |

## 🔧 Technische Details

### Kosmische Korrekturen
Das Skript berücksichtigt:
- **Tagesrhythmus** (24-Stunden Zyklus)
- **Fraktale Modulation** (basierend auf D_f)
- **Gezeiteneffekte** (12.42-Stunden Zyklus)
- **Saisonale Variation** (Jahreszeiten)
- **Lunare Zyklen** (Mondphasen)

### Fehlerraten (realistisch)
- **Single-Qubit Gatter**: 0.5%
- **Two-Qubit Gatter**: 2%
- **Messung**: 1%
- **Leerlauf**: 0.05%/μs
- **Auslesen**: 3%
- **Reset**: 2%

### Fraktale Parameter
- **ξ (xi)**: Fraktaler Korrekturparameter (Standard: 0.001)
- **D_f**: Fraktale Dimension = 3 - ξ
- **Chip-Dimensionen**: 10mm Radius realistischer Chip

## 💾 Datenausgabe

### JSON-Export
```powershell
# Automatischer Export
python t0_cosmic_error_correction.py --complete --save-results

# Benutzerdefinierter Dateiname
python t0_cosmic_error_correction.py --complete --output meine_analyse.json
```

### Dateiinhalt
```json
{
  "current_conditions": {...},
  "time_optimization": {...},
  "qubit_arrangement": {...},
  "threshold_analysis": {...},
  "simulation": {...},
  "adaptive_schedule": [...],
  "recommendations": [...],
  "summary": {...}
}
```

## 🐛 Fehlerbehebung

### Häufige Fehler
1. **"NameError: name 'start' is not defined"**
   - Problem: Alte Version des Skripts
   - Lösung: Aktuelle Version verwenden

2. **"ModuleNotFoundError: No module named 'numpy'"**
   - Problem: Pakete nicht installiert
   - Lösung: `pip install numpy ephem`

3. **Neues Fenster öffnet und schließt sofort**
   - Problem: `python` vergessen
   - Lösung: Immer `python skript.py` verwenden

4. **Virtual Environment nicht aktiv**
   - Problem: Pakete in falscher Umgebung
   - Lösung: `.\cosmic_env\Scripts\Activate.ps1`

### Debug-Modus
```powershell
python t0_cosmic_error_correction.py --complete --debug --verbose
```

## 🔬 Wissenschaftliche Grundlagen

### Fraktales Torus-Universum
- **ξ = 4/30000** = 0.000133 (theoretischer Wert)
- **D_f = 3 - ξ** = Fraktale Dimension
- **Kosmische Korrektur**: 1.0 ± 20% möglich

### Threshold-Theorem
- **Theoretische Schwelle**: 1% für Surface Code
- **Praktische Schwelle**: 0.5% mit aktueller Hardware
- **Kosmische Verbesserung**: Bis zu 1.2x möglich

### Quantenfehlerkorrektur
- **Distanz**: Anzahl korrigierbarer Fehler
- **Overhead**: Physikalische/logische Qubits
- **Adaptive Rate**: 100ms - 2000ms je nach Bedingungen

## 📈 Beispielausgabe

```
🌌 Aktuelle kosmische Bedingungen:
   Korrektur: 1.0456
   Verbesserung: +4.56%

⏰ Beste Startzeit für grover:
   Start: 22:15 (+8.7%, Wartezeit: 0.0h)

⚡ cosmic_code Fehlerschwelle:
   Effektiv: 5.23e-02 (Verbesserung: 1.046x)

🔌 Simulation (20 Gatter):
   Erfolg mit Korrektur: 89.23%
   Kosmische Verbesserung: 1.28x

💡 Empfehlungen:
   [HIGH] SOFORT STARTEN
```

## 📚 Nächste Schritte

1. **Parameter optimieren**: Experimentieren Sie mit verschiedenen ξ-Werten
2. **Standortanalyse**: Vergleichen Sie verschiedene geografische Positionen
3. **Algorithmus-Tuning**: Finden Sie die besten Zeiten für Ihre spezifischen Algorithmen
4. **Visualisierung**: Erweitern Sie mit matplotlib für grafische Darstellungen

## 📞 Support
- **Virtual Environment**: `.\cosmic_env\Scripts\Activate.ps1`
- **Paket-Installation**: `pip install numpy ephem`
- **Skript-Ausführung**: `python t0_cosmic_error_correction.py --help`

---

**Hinweis**: Für optimale Ergebnisse führen Sie die Analyse regelmäßig durch, da sich die kosmischen Bedingungen ständig ändern.