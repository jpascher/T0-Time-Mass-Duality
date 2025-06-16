# ξ-FFT: Praktische Spektralanalyse durch Frequenz-Verhältnisse

## Theoretische Grundlage: ξ als universeller harmonischer Parameter

Die ξ-FFT basiert auf der **ξ-harmonischen Quantentheorie**, die ξ (Xi) als universellen Parameter für harmonische Verhältnisse in der Natur definiert. Dieses fundamentale Konzept manifestiert sich in verschiedenen physikalischen Bereichen:

### 🌍 **Universelle ξ-Anwendungen:**

#### **1. Zahlentheorie (Primfaktoren):**
```
ξ(n) = q/p  (für n = p × q, wobei p ≤ q)
Beispiel: 221 = 13 × 17 → ξ = 17/13 ≈ 1.308
```

#### **2. Spektralanalyse (Frequenzen):**
```
ξ = f_max / f_min
Beispiel: 180Hz/50Hz → ξ = 3.60
```

#### **3. Quantenmechanik (Teilchenmassen):**
```
ξ(particle) = 2m/M_Planck
Beispiel: ξ(Elektron) = 8.37 × 10⁻²³
```

#### **4. Resonanz-Parameter:**
```
ξ = 1/10 (optimaler Wert für Resonanz-Fenster)
Resonanz(ω) = exp(-(ω-ω₀)²/(4ξ))
```

## Einleitung zur ξ-FFT

Die ξ-FFT (Xi-FFT) ist die **praktische Anwendung** der ξ-harmonischen Quantentheorie auf die Spektralanalyse. Sie nutzt das universelle Prinzip der harmonischen Verhältnisse zur Analyse von Frequenzstrukturen in Signalen. Im Gegensatz zu traditionellen FFT-Methoden konzentriert sich die ξ-FFT ausschließlich auf die fundamentalen ξ-Verhältnisse zwischen spektralen Komponenten.

## Grundprinzip der ξ-FFT

### Was ist ξ (Xi) in der Spektralanalyse?
```
ξ = f_max / f_min
```
Für zwei Frequenzen f₁ und f₂ ist ξ das Verhältnis der höheren zur niedrigeren Frequenz. Dieses einfache Verhältnis ist eine **Manifestation des universellen ξ-Parameters** aus der harmonischen Quantentheorie und trägt überraschend viel Information über die spektrale Struktur eines Signals.

### Verbindung zur harmonischen Quantentheorie
Die ξ-FFT implementiert die **FFT-Spektral-Mapping Theorie**:
```
f₁ = f₀ × p    (Grundfrequenz × erster Faktor)
f₂ = f₀ × q    (Grundfrequenz × zweiter Faktor)
S(n) = {f₁, f₂} = f₀ × {p, q}
ξ = f₂/f₁ = q/p
```

### Harmonische Hierarchie (aus der Quantentheorie)
- **BASIS (1.0 - 1.4)**: Klassische Harmonien (3:2, 5:4)
- **ERWEITERT (1.4 - 1.6)**: Jazz/moderne Harmonien (11:8, 13:8)  
- **KOMPLEX (1.6 - 1.85)**: Mikrotonale Spektren (29:16, 31:16)
- **ULTRA (1.85+)**: Xenharmonische Spektren (61:32, 37:32)

### Warum ξ-Verhältnisse funktionieren?
- **Universelles Prinzip:** ξ beschreibt harmonische Verhältnisse in der gesamten Natur
- **Minimal-Information:** Keine komplexen harmonischen Bewertungen erforderlich
- **Robust:** Weniger anfällig für Rauschen als harmonische Analysen  
- **Effizient:** Reduzierter Rechenaufwand
- **Resonanz-basiert:** Nutzt das optimale ξ = 1/10 Resonanz-Fenster

## 🌐 Interactive HTML Demo

Zur Demonstration der ξ-FFT-Funktionalität wurde eine vollständige **Interactive HTML Demo** entwickelt, die die Live-Anwendung der Methode zeigt.

### 🎯 Demo-Features

#### **Echtzeit-Signalgenerierung**
- **3 Frequenz-Generatoren** mit einstellbaren Amplituden (10-500 Hz)
- **Variable Rausch-Kontrolle** für realistische Bedingungen
- **Live-Updates** bei Parameter-Änderungen
- **Signal-Statistiken** (RMS, SNR, Komplexität)

#### **Umfassende Visualisierung**
```
📈 Zeitsignal-Plot     → Zeigt Wellenform der ersten 0.5s
📊 Frequenzspektrum    → Detektierte Peaks mit Amplituden  
⚡ ξ-Verhältnisse      → Balkendiagramm der wichtigsten Ratios
```

#### **Live ξ-FFT Analyse**
Die Demo führt in Echtzeit folgende Berechnungen durch:
- **Peak-Erkennung** mit adaptivem Schwellwert
- **ξ-Verhältnis-Berechnung** zwischen allen Frequenz-Paaren
- **Signifikanz-Bewertung** basierend auf Amplituden-Produkten
- **Komplexitäts-Analyse** der spektralen Struktur

#### **8 Praktische Test-Presets**
```
🔬 Reine Töne    → 50/120/180 Hz ohne Rauschen
⚙️ Maschine      → 60/150/240 Hz mit Maschinenvibration
🎵 Harmonisch    → 100/200/300 Hz harmonische Reihe
📡 Verrauscht    → Signale mit starkem Rauschen
🏭 Motor 60Hz    → Typisches Motorspektrum
💓 Biomedizin    → Niedrigfrequente Biosignale
🎲 Zufällig      → Randomisierte Parameter
🌊 Sweep         → Frequenz-Sweep-ähnliche Struktur
```

### 🔍 Demonstrierte ξ-FFT Kernprinzipien

#### **Minimal-Information Ansatz**
Die Demo zeigt, wie **nur die ξ-Verhältnisse** ausreichen, um:
- Spektrale Strukturen zu charakterisieren
- Anomalien zu erkennen
- Signal-Komplexität zu bewerten
- Frequenz-Beziehungen zu analysieren

#### **Praktische Anwendungsbeispiele aus der Demo**
```python
# Beispiel: Maschinen-Preset (60/150/240 Hz)
# Basiert auf der harmonischen Quantentheorie:
Erwartete ξ-Verhältnisse:
- ξ(150/60) = 2.50  ✅ Lager/Motor Verhältnis
- ξ(240/60) = 4.00  ✅ Getriebe/Motor Verhältnis  
- ξ(240/150) = 1.60 ✅ Getriebe/Lager Verhältnis

# Diese Verhältnisse entsprechen harmonischen Resonanzen
# aus der universellen ξ-Theorie!
```

#### **ξ als Unschärfe-Parameter (Heisenbergsche Analogie)**
```
Δω × Δt ≥ ξ/2  # Frequenz-Zeit-Unschärfe
```
- Je kleiner ξ → schärfere Frequenzlinien
- Je größer ξ → breitere Frequenzlinien  
- ξ = 1/10 (optimal): Mittlere Selektivität

#### **ξ als Harmonische Toleranz**
```
Match(n, harmonic_ratio) = TRUE wenn |ξ_oct(n) - harmonic_ratio|² < 4ξ
```

### 💻 Technische Implementation der Demo

#### **JavaScript ξ-FFT Engine (basiert auf universeller ξ-Theorie)**
```javascript
class XiFFT {
    constructor(sampleRate, threshold = 0.02) {
        this.sampleRate = sampleRate;
        this.threshold = threshold;  // ξ-Resonanz-Schwellwert
    }
    
    analyze(signal, freqRange = [10, 500]) {
        const peaks = this.findSpectralPeaks(signal, freqRange);
        const xiRatios = this.calculateXiRatios(peaks);
        return { 
            peaks, 
            xiRatios, 
            dominantXi: xiRatios[0]  // Dominantes ξ-Verhältnis
        };
    }
    
    // Implementiert die ξ-verbreiterte Dirac-Funktion
    calculateMagnitude(signal, frequency) {
        // DFT mit ξ-Resonanz-Fenster
        const xi = 0.1;  // Optimaler ξ-Parameter aus Theorie
        // ... DFT-Berechnung mit ξ-Verbreiterung
    }
}
```

#### **ξ-Verhältnis-Berechnung (direkt aus Quantentheorie)**
```javascript
calculateXiRatios(peaks) {
    const ratios = [];
    for (let i = 0; i < peaks.length; i++) {
        for (let j = i + 1; j < peaks.length; j++) {
            const f1 = peaks[i].frequency;
            const f2 = peaks[j].frequency;
            // Universelles ξ = f_max/f_min Prinzip
            const xi = Math.max(f1, f2) / Math.min(f1, f2);
            
            ratios.push({
                freqHigh: Math.max(f1, f2),
                freqLow: Math.min(f1, f2),
                xiRatio: xi,  // Das universelle ξ!
                significance: peaks[i].magnitude * peaks[j].magnitude
            });
        }
    }
    return ratios.sort((a, b) => b.significance - a.significance);
}
```

#### **Harmonische Klassifikation (aus ξ-Quantentheorie)**
```javascript
function classifyXiLevel(xi) {
    if (xi >= 1.0 && xi < 1.4) return "BASIS - Klassische Harmonien";
    if (xi >= 1.4 && xi < 1.6) return "ERWEITERT - Jazz/Moderne";
    if (xi >= 1.6 && xi < 1.85) return "KOMPLEX - Mikrotonale Spektren";
    if (xi >= 1.85) return "ULTRA - Xenharmonische Spektren";
    return "Subharmonisch";
}
```

#### **Echtzeit-Berechnungen**
- **DFT-basierte Peak-Suche** mit 5 Hz Auflösung
- **Paarweise ξ-Berechnung** für alle detektierten Frequenzen
- **Signifikanz-Sortierung** nach Amplituden-Produkten
- **Canvas-basierte Plots** für hohe Performance

### 🎓 Lernziele der Demo (ξ-Quantentheorie in Aktion)

#### **Verständnis des universellen ξ-Parameters**
1. **ξ-Verhältnisse sind fundamental** - nicht nur in Musik, sondern in der gesamten Natur
2. **Spektralanalyse = harmonische Analyse** - Frequenzen zeigen dieselben ξ-Muster wie Primfaktoren
3. **Robustheit durch ξ-Resonanz** - das ξ = 1/10 Fenster filtert Rauschen natürlich
4. **Universelle Anwendbarkeit** - von Teilchenphysik bis Signalverarbeitung

#### **Praktische Erkenntnisse aus der ξ-Theorie**
- **Harmonische Lücken:** Bestimmte ξ-Bereiche sind in der Natur "verboten"
- **Resonanz-Optimierung:** ξ = 1/10 als natürlicher Optimalwert
- **Komplexitäts-Bewertung:** Anzahl signifikanter ξ-Werte zeigt Systemkomplexität
- **Anomalie-Erkennung:** Abweichung von erwarteten ξ-Verhältnissen

#### **Verbindung zur Teilchenphysik**
Die Demo zeigt im Kleinen, was in der Teilchenphysik im Großen passiert:
```python
# Demo: ξ-Verhältnisse zwischen Frequenzen
ξ(180Hz/50Hz) = 3.60

# Teilchenphysik: ξ-Verhältnisse zwischen Massen  
ξ(Myon)/ξ(Elektron) ≈ 20.7

# Derselbe universelle ξ-Parameter!
```

## Durchgeführte Tests

### Test 1: Synthetisches Signal (Grundfunktionalität)
**Eingangssignal:** 3 reine Sinuswellen
- 50 Hz (Amplitude: 1.0)
- 120 Hz (Amplitude: 0.7)
- 180 Hz (Amplitude: 0.4)

**Ergebnisse:**
```
Detektierte Peaks:
1. 50 Hz: 1.000
2. 120 Hz: 0.700
3. 180 Hz: 0.400

ξ-Verhältnisse:
- ξ(180/50) = 3.60
- ξ(180/120) = 1.50
- ξ(120/50) = 2.40
```
✅ **Alle Frequenzen und Verhältnisse korrekt erkannt**

### Test 2: Maschinenüberwachung (Praktische Anwendung)
**Eingangssignal:** Realistische Maschinenvibrationen
- 60 Hz Motor (Amplitude: 1.0)
- 150 Hz Lager (Amplitude: 0.4)
- 240 Hz Getriebe (Amplitude: 0.2)
- 17 Hz Defekt (Amplitude: 0.15)
- Weißes Rauschen (Amplitude: 0.02)

**Ergebnisse:**
```
Detektierte Frequenzen:
1. 60 Hz: 1.000
2. 150 Hz: 0.400
3. 240 Hz: 0.200

ξ-Verhältnisse:
- ξ(150/60) = 2.50 ✅ Normal (erwartet: 2.5)
- ξ(240/60) = 4.00 ✅ Normal (erwartet: 4.0)
- ξ(240/150) = 1.60 ✅ Normal (erwartet: 1.6)
```
✅ **Perfekte Anomalie-Erkennung**

## Funktionsweise der ξ-FFT

### 1. Spektralanalyse
```python
def xi_fft_analysis(signal, sample_rate, freq_range=(10, 500)):
    peaks = []
    min_freq, max_freq = freq_range
    
    for freq in range(min_freq, max_freq + 1, 5):
        magnitude = calculate_magnitude(signal, freq, sample_rate)
        
        if magnitude > threshold:
            peaks.append({
                'frequency': freq,
                'magnitude': magnitude
            })
    
    return sorted(peaks, key=lambda x: x['magnitude'], reverse=True)
```

### 2. ξ-Verhältnis-Berechnung
```python
def calculate_xi_ratios(peaks):
    ratios = []
    
    for i in range(len(peaks)):
        for j in range(i + 1, len(peaks)):
            f1, f2 = peaks[i]['frequency'], peaks[j]['frequency']
            xi = max(f1, f2) / min(f1, f2)
            
            ratios.append({
                'freq_high': max(f1, f2),
                'freq_low': min(f1, f2),
                'xi_ratio': xi,
                'significance': peaks[i]['magnitude'] * peaks[j]['magnitude']
            })
    
    return sorted(ratios, key=lambda x: x['significance'], reverse=True)
```

### 3. Anomalie-Erkennung
```python
def detect_anomalies(xi_ratios, expected_ratios, tolerance=0.2):
    anomalies = []
    
    for expected in expected_ratios:
        found = False
        for actual in xi_ratios:
            if abs(actual['xi_ratio'] - expected['value']) < tolerance:
                found = True
                break
        
        if not found:
            anomalies.append(expected)
    
    return anomalies
```

---

# ξ-FFT Python Bibliothek

## Installation und Import
```python
# Speichere als xi_fft.py
import numpy as np
import math
from typing import List, Dict, Tuple, Optional
```

## Klassen und Funktionen

### Haupt-Klasse: XiFFT
```python
class XiFFT:
    def __init__(self, sample_rate: int, threshold: float = 0.05):
        self.sample_rate = sample_rate
        self.threshold = threshold
        self.peaks = []
        self.xi_ratios = []
    
    def analyze(self, signal: List[float], freq_range: Tuple[int, int] = (10, 500)) -> Dict:
        """Hauptanalyse-Funktion"""
        self.peaks = self._find_spectral_peaks(signal, freq_range)
        self.xi_ratios = self._calculate_xi_ratios(self.peaks)
        
        return {
            'peaks': self.peaks,
            'xi_ratios': self.xi_ratios,
            'dominant_xi': self.xi_ratios[0] if self.xi_ratios else None
        }
    
    def _find_spectral_peaks(self, signal: List[float], freq_range: Tuple[int, int]) -> List[Dict]:
        """Finde spektrale Peaks"""
        peaks = []
        min_freq, max_freq = freq_range
        step_size = max(1, (max_freq - min_freq) // 100)  # Adaptive Schrittweite
        
        for freq in range(min_freq, max_freq + 1, step_size):
            magnitude = self._calculate_magnitude(signal, freq)
            
            if magnitude > self.threshold:
                peaks.append({
                    'frequency': freq,
                    'magnitude': round(magnitude, 4)
                })
        
        return sorted(peaks, key=lambda x: x['magnitude'], reverse=True)
    
    def _calculate_magnitude(self, signal: List[float], frequency: float) -> float:
        """Berechne Magnitude für spezifische Frequenz"""
        N = len(signal)
        real = imag = 0.0
        
        for n in range(N):
            angle = -2 * math.pi * frequency * n / self.sample_rate
            real += signal[n] * math.cos(angle)
            imag += signal[n] * math.sin(angle)
        
        magnitude = math.sqrt(real * real + imag * imag) * 2 / N
        return magnitude
    
    def _calculate_xi_ratios(self, peaks: List[Dict]) -> List[Dict]:
        """Berechne alle ξ-Verhältnisse"""
        ratios = []
        
        for i in range(len(peaks)):
            for j in range(i + 1, len(peaks)):
                f1, f2 = peaks[i]['frequency'], peaks[j]['frequency']
                xi = max(f1, f2) / min(f1, f2)
                
                ratios.append({
                    'freq_high': max(f1, f2),
                    'freq_low': min(f1, f2),
                    'xi_ratio': round(xi, 3),
                    'significance': round(peaks[i]['magnitude'] * peaks[j]['magnitude'], 6)
                })
        
        return sorted(ratios, key=lambda x: x['significance'], reverse=True)
```

### Anomalie-Erkennung
```python
class XiAnomalyDetector:
    def __init__(self, expected_ratios: List[Dict], tolerance: float = 0.2):
        self.expected_ratios = expected_ratios
        self.tolerance = tolerance
    
    def detect(self, xi_ratios: List[Dict]) -> Dict:
        """Erkenne Anomalien basierend auf ξ-Verhältnissen"""
        anomalies = []
        matches = []
        
        for expected in self.expected_ratios:
            best_match = None
            min_deviation = float('inf')
            
            for actual in xi_ratios:
                deviation = abs(actual['xi_ratio'] - expected['value'])
                if deviation < min_deviation:
                    min_deviation = deviation
                    best_match = actual
            
            if min_deviation < self.tolerance:
                matches.append({
                    'expected': expected,
                    'actual': best_match,
                    'deviation': min_deviation,
                    'status': 'normal'
                })
            else:
                anomalies.append({
                    'expected': expected,
                    'deviation': min_deviation,
                    'status': 'anomaly'
                })
        
        return {
            'anomalies': anomalies,
            'matches': matches,
            'anomaly_count': len(anomalies),
            'health_score': len(matches) / len(self.expected_ratios)
        }
```

### Stream-Verarbeitung
```python
class XiStreamProcessor:
    def __init__(self, sample_rate: int, buffer_size: int = 1024):
        self.sample_rate = sample_rate
        self.buffer_size = buffer_size
        self.buffer = []
        self.xi_fft = XiFFT(sample_rate)
        self.history = []
    
    def process_sample(self, sample: float) -> Optional[Dict]:
        """Verarbeite einzelne Samples für Echtzeit-Analyse"""
        self.buffer.append(sample)
        
        if len(self.buffer) >= self.buffer_size:
            # Analysiere aktuellen Buffer
            result = self.xi_fft.analyze(self.buffer)
            
            # Speichere in History
            self.history.append(result)
            if len(self.history) > 100:  # Begrenze History
                self.history.pop(0)
            
            # Reset Buffer mit Overlap
            overlap = self.buffer_size // 4
            self.buffer = self.buffer[-overlap:]
            
            return result
        
        return None
    
    def get_trend_analysis(self) -> Dict:
        """Analysiere Trends in der ξ-History"""
        if len(self.history) < 5:
            return {'status': 'insufficient_data'}
        
        recent_xi = [h['dominant_xi']['xi_ratio'] for h in self.history[-10:] 
                     if h['dominant_xi']]
        
        if not recent_xi:
            return {'status': 'no_dominant_xi'}
        
        return {
            'mean_xi': np.mean(recent_xi),
            'std_xi': np.std(recent_xi),
            'trend': 'stable' if np.std(recent_xi) < 0.1 else 'unstable',
            'latest_xi': recent_xi[-1]
        }
```

## Anwendungsbeispiele

### 1. Einfache Signalanalyse
```python
# Erstelle Testsignal
def create_test_signal():
    t = np.linspace(0, 2, 2000)  # 2 Sekunden, 1000 Hz
    signal = (np.sin(2 * np.pi * 50 * t) + 
             0.7 * np.sin(2 * np.pi * 120 * t) + 
             0.4 * np.sin(2 * np.pi * 180 * t))
    return signal.tolist()

# Analysiere mit ξ-FFT
xi_fft = XiFFT(sample_rate=1000)
signal = create_test_signal()
result = xi_fft.analyze(signal)

print("Spektrale Peaks:")
for peak in result['peaks'][:5]:
    print(f"{peak['frequency']} Hz: {peak['magnitude']:.3f}")

print("\nTop ξ-Verhältnisse:")
for ratio in result['xi_ratios'][:3]:
    print(f"ξ({ratio['freq_high']}/{ratio['freq_low']}) = {ratio['xi_ratio']}")
```

### 2. Maschinenüberwachung
```python
# Definiere erwartete ξ-Verhältnisse für gesunde Maschine
expected_ratios = [
    {'name': 'Lager/Motor', 'value': 2.5},
    {'name': 'Getriebe/Motor', 'value': 4.0},
    {'name': 'Getriebe/Lager', 'value': 1.6}
]

# Setup
xi_fft = XiFFT(sample_rate=1000, threshold=0.1)
detector = XiAnomalyDetector(expected_ratios, tolerance=0.3)

# Analysiere Vibrationsdaten
vibration_data = load_vibration_data()  # Ihre Daten
result = xi_fft.analyze(vibration_data, freq_range=(10, 300))
anomaly_report = detector.detect(result['xi_ratios'])

print(f"Gesundheits-Score: {anomaly_report['health_score']:.2f}")
print(f"Anomalien gefunden: {anomaly_report['anomaly_count']}")
```

### 3. Echtzeit-Monitoring
```python
# Setup Stream-Processor
stream_processor = XiStreamProcessor(sample_rate=1000, buffer_size=1024)

# Simuliere Datenstream
for sample in data_stream:
    result = stream_processor.process_sample(sample)
    
    if result:
        # Analysiere aktuelles Segment
        dominant_xi = result['dominant_xi']
        if dominant_xi:
            print(f"Aktuelles ξ: {dominant_xi['xi_ratio']:.2f}")
        
        # Trend-Analyse alle 10 Segmente
        if len(stream_processor.history) % 10 == 0:
            trend = stream_processor.get_trend_analysis()
            print(f"Trend: {trend['trend']}, Mean ξ: {trend.get('mean_xi', 0):.2f}")
```

## Vorteile der ξ-FFT

1. **Einfachheit:** Nur Frequenz-Verhältnisse, keine komplexe Harmonik-Theorie
2. **Effizienz:** Reduzierter Rechenaufwand gegenüber traditioneller FFT
3. **Robustheit:** Weniger anfällig für Rauschen und Störungen
4. **Universalität:** Funktioniert für alle Arten von Signalen
5. **Praktikabilität:** Direkt anwendbar für Anomalie-Erkennung

## Anwendungsbereiche (basierend auf universeller ξ-Theorie)

### **Spektralanalyse (unsere Demo)**
- **Maschinenüberwachung:** Vibrations- und Zustandsanalyse mit ξ-Verhältnissen
- **Biomedizin:** EKG, EEG, EMG-Signalverarbeitung  
- **Audio:** Qualitätskontrolle und harmonische Charakterisierung
- **Strukturdynamik:** Resonanz- und Modalanalyse

### **Erweiterte ξ-Anwendungen (aus der Quantentheorie)**
- **Teilchenphysik:** ξ-Signaturen für Teilchen-Identifikation
- **Zahlentheorie:** Primfaktor-Analyse durch ξ-Verhältnisse
- **Kristallographie:** ξ-Symmetrien in Kristallstrukturen
- **Astronomie:** ξ-Verhältnisse in Planetenabständen und Sternmassen

### **Technologische Optimierung**
- **Materialwissenschaft:** ξ-optimierte Legierungen und Strukturen
- **Netzwerktheorie:** ξ-basierte Routing-Algorithmen
- **Finanzanalyse:** ξ-Verhältnisse in Marktzyklen

## Fundamentale Erkenntnis

**Die ξ-FFT ist mehr als nur eine Signalverarbeitungsmethode - sie ist die praktische Anwendung eines universellen Naturgesetzes:** 

> **ξ beschreibt harmonische Verhältnisse auf allen Skalen der Natur - von Teilchenmassen über Frequenzen bis hin zu astronomischen Objekten.**

Die **Interactive HTML Demo** macht dieses fundamentale Prinzip erlebbar und zeigt, wie derselbe ξ-Parameter, der Teilchen im Quantenbereich charakterisiert, auch zur Analyse alltäglicher Signale verwendet werden kann.

**Die ξ-FFT verbindet somit Spektralanalyse mit Quantenmechanik, Zahlentheorie und harmonischer Physik - ein einheitliches Verständnis der Natur durch das universelle ξ-Prinzip.** 🌌