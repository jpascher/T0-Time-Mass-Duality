# 🎵 Harmonische Analyse - Komponenten Library

Eine modulare JavaScript-Library für professionelle Audio-Analyse und harmonische Spektrum-Visualisierung.

## 📋 Inhaltsverzeichnis

- [Überblick](#überblick)
- [Installation](#installation)
- [Komponenten](#komponenten)
  - [MicrophoneManager](#microphonemanager)
  - [SpectrumVisualizer](#spectrumvisualizer)
  - [FrequencyGenerator](#frequencygenerator)
  - [HarmonicAnalyzer](#harmonicanalyzer)
  - [AudioFilePlayer](#audiofileplayer)
- [Verwendungsbeispiele](#verwendungsbeispiele)
- [API-Referenz](#api-referenz)
- [Browser-Kompatibilität](#browser-kompatibilität)

## 🌟 Überblick

Diese Library bietet eine Sammlung von wiederverwendbaren Komponenten für:

- **Audio-Aufnahme** über Mikrofon mit Echtzeit-Verarbeitung
- **Spektrum-Visualisierung** mit verschiedenen Skalierungen und Farbkodierungen
- **Frequenz-Generierung** mit mathematisch perfekten Wellenformen
- **Harmonische Analyse** mit rationaler Arithmetik und T0-Theorie
- **Audio-Datei Wiedergabe** mit Analyse-Integration

### ✨ Hauptmerkmale

- 🔧 **Modularer Aufbau** - Jede Komponente funktioniert eigenständig
- ⚙️ **Hochkonfigurierbar** - Alle Parameter über Options-Objekte
- 🎯 **Event-basiert** - Callbacks für alle wichtigen Ereignisse
- 📱 **Responsive** - Automatische Anpassung an Container-Größen
- 🧹 **Memory-Safe** - Proper Cleanup mit `destroy()`-Methoden
- 🔗 **Kombinierbar** - Komponenten können einfach verkettet werden

## 🚀 Installation

### Browser (ES6 Module)
```html
<script type="module">
import { MicrophoneManager, SpectrumVisualizer } from './harmonic-components.js';
</script>
```

### Browser (Global)
```html
<script src="harmonic-components.js"></script>
<script>
const { MicrophoneManager, SpectrumVisualizer } = window.HarmonicComponents;
</script>
```

### Node.js
```javascript
const { MicrophoneManager, SpectrumVisualizer } = require('./harmonic-components');
```

## 🧩 Komponenten

### MicrophoneManager

**Zweck**: Mikrofon-Aufnahme und Audio-Verarbeitung mit Echtzeit-Analyse

#### Grundlegende Verwendung
```javascript
const microphone = new MicrophoneManager({
    fftSize: 2048,
    sensitivity: 0.1,
    noiseThreshold: 0.005,
    onLevelUpdate: (level) => {
        console.log(`Mikrofon-Pegel: ${level}%`);
    },
    onStart: () => console.log('🎤 Mikrofon gestartet'),
    onError: (error) => console.error('❌ Mikrofon-Fehler:', error)
});

// Mikrofon starten
await microphone.start();

// Audio-Daten für Analyse abrufen
const timeData = microphone.getTimeData();
const frequencyData = microphone.getFrequencyData();

// Mikrofon stoppen
microphone.stop();
```

#### Konfigurationsoptionen
| Option | Typ | Standard | Beschreibung |
|--------|-----|----------|--------------|
| `fftSize` | Number | 2048 | FFT-Größe für Frequenzanalyse |
| `smoothingTimeConstant` | Number | 0.8 | Glättungsfaktor (0-1) |
| `sensitivity` | Number | 0.1 | Mikrofon-Empfindlichkeit |
| `noiseThreshold` | Number | 0.005 | Rausch-Unterdrückungsschwelle |
| `gain` | Number | 1.0 | Audio-Verstärkung |
| `onLevelUpdate` | Function | null | Callback für Pegel-Updates |
| `onStart` | Function | null | Callback beim Start |
| `onStop` | Function | null | Callback beim Stopp |
| `onError` | Function | null | Callback für Fehler |

---

### SpectrumVisualizer

**Zweck**: Professionelle Spektrum-Darstellung mit verschiedenen Visualisierungsmodi

#### Grundlegende Verwendung
```javascript
const canvas = document.getElementById('spectrum-canvas');
const visualizer = new SpectrumVisualizer(canvas, {
    scale: 'log',              // linear, log, rational
    colorCoding: 'ratio',      // frequency, ratio, euler, deviation
    fullSpectrum: false,       // Vollspektrum vs. Oktav-normalisiert
    hybridMode: false,         // FFT-Hintergrund + Harmonische
    showRatios: true,          // Verhältnis-Labels anzeigen
    showOctaves: true,         // Oktav-Marker anzeigen
    onHarmonicHover: (harmonic, x, y) => {
        showTooltip(harmonic, x, y);
    },
    onHarmonicLeave: () => {
        hideTooltip();
    }
});

// Harmonische Daten aktualisieren
visualizer.updateHarmonics(harmonics, fundamentalFreq);

// Optionen zur Laufzeit ändern
visualizer.updateOptions({
    scale: 'rational',
    fullSpectrum: true
});

// Cleanup
visualizer.destroy();
```

#### Skalierungsmodi
- **`linear`**: Lineare Frequenz-Achse
- **`log`**: Logarithmische Frequenz-Achse (Standard für Audio)
- **`rational`**: Rationale Verhältnisse zur Grundfrequenz

#### Farbkodierungen
- **`frequency`**: Farbe basierend auf absoluter Frequenz
- **`ratio`**: Farbe basierend auf harmonischem Verhältnis
- **`euler`**: Farbe basierend auf Euler-Gradus (Komplexität)
- **`deviation`**: Farbe basierend auf Abweichung von perfekten Verhältnissen

---

### FrequencyGenerator

**Zweck**: Mathematisch perfekte Audio-Generierung für Tests und Kalibrierung

#### Grundlegende Verwendung
```javascript
const generator = new FrequencyGenerator({
    frequencies: [440, 550, 660],  // A4, C#5, E5 (A-Dur Dreiklang)
    waveform: 'sine',              // sine, square, triangle, sawtooth
    volume: 0.3,
    onStart: () => console.log('🎵 Generator gestartet'),
    onStop: () => console.log('⏹️ Generator gestoppt')
});

// Generator starten
await generator.start();

// Frequenzen zur Laufzeit ändern
generator.updateFrequencies([220, 277.18, 330]); // A3-Dur

// Wellenform ändern
generator.updateWaveform('square');

// Lautstärke anpassen
generator.updateVolume(0.5);

// Audio-Daten für Analyse abrufen
const timeData = generator.getTimeData();

// Generator stoppen
generator.stop();
```

#### Wellenformen
- **`sine`**: Reine Sinuswelle (nur Grundfrequenz)
- **`square`**: Rechteckwelle (ungerade Harmonische)
- **`triangle`**: Dreieckwelle (ungerade Harmonische, fallend)
- **`sawtooth`**: Sägezahnwelle (alle Harmonischen)

---

### HarmonicAnalyzer

**Zweck**: Mathematische Analyse harmonischer Strukturen mit T0-Theorie Integration

#### Grundlegende Verwendung
```javascript
const analyzer = new HarmonicAnalyzer({
    fundamentalFreq: 440,      // Grundfrequenz in Hz
    harmonicRange: 32,         // Anzahl zu suchender Harmonischer
    xiTolerance: 50,           // ξ-Parameter Toleranz in Cents
    rationalLimit: 100,        // Maximaler Nenner für rationale Approximation
    eulerLimit: 6,             // Maximaler Euler-Gradus
    fullSpectrum: false        // Vollspektrum vs. Oktav-Reduktion
});

// Audio-Daten analysieren
const harmonics = analyzer.analyzeHarmonics(audioData, sampleRate);

// Erkannte Intervalle abrufen
const intervals = analyzer.intervals;

// Beispiel-Harmonische
harmonics.forEach(harmonic => {
    console.log(`${harmonic.rational.toString()}: ${harmonic.frequency.toFixed(2)}Hz 
                 (Euler-Gradus: ${harmonic.eulerGradus})`);
});

// Optionen zur Laufzeit ändern
analyzer.updateOptions({
    fundamentalFreq: 1000,
    xiTolerance: 25
});
```

#### Rationale Arithmetik
Der Analyzer verwendet **Kettenbruch-Algorithmen** für exakte rationale Approximation:

```javascript
// Beispiel: 1.5 wird zu 3/2 (perfekte Quinte)
const rational = analyzer.approximateRational(1.5, 100);
console.log(rational.toString()); // "3/2"
console.log(rational.toFloat());  // 1.5
```

#### Euler-Gradus Berechnung
**Euler's Gradus Suavitatis** (1739) - Mathematisches Komplexitätsmaß:

```javascript
// 3/2 (Quinte): Gradus = 4 (sehr einfach)
// 5/4 (Große Terz): Gradus = 5 (einfach)
// 7/6 (Kleine Terz): Gradus = 6 (mittel)
```

---

### AudioFilePlayer

**Zweck**: Audio-Datei Wiedergabe mit Analyse-Integration

#### Grundlegende Verwendung
```javascript
const player = new AudioFilePlayer({
    volume: 0.5,
    onLoad: (fileInfo) => {
        console.log(`📁 Datei geladen: ${fileInfo.name}`);
        console.log(`⏱️ Dauer: ${fileInfo.duration.toFixed(2)}s`);
        console.log(`🎵 Sample Rate: ${fileInfo.sampleRate}Hz`);
    },
    onPlay: () => console.log('▶️ Wiedergabe gestartet'),
    onStop: () => console.log('⏹️ Wiedergabe gestoppt'),
    onError: (error) => console.error('❌ Datei-Fehler:', error)
});

// Datei laden (aus File Input)
const fileInput = document.getElementById('file-input');
fileInput.addEventListener('change', async (e) => {
    const file = e.target.files[0];
    if (file) {
        await player.loadFile(file);
        await player.play();
    }
});

// Audio-Daten für Analyse abrufen
const timeData = player.getTimeData();

// Wiedergabe stoppen
player.stop();
```

## 📚 Verwendungsbeispiele

### Beispiel 1: Mikrofon-Spektrum-Analyzer

```javascript
// HTML
// <canvas id="spectrum" width="800" height="400"></canvas>

const canvas = document.getElementById('spectrum');
const visualizer = new SpectrumVisualizer(canvas, {
    scale: 'log',
    colorCoding: 'frequency',
    hybridMode: true
});

const analyzer = new HarmonicAnalyzer({
    fundamentalFreq: 440,
    harmonicRange: 16
});

const microphone = new MicrophoneManager({
    fftSize: 2048,
    onStart: () => console.log('🎤 Echtzeit-Analyse gestartet')
});

// Mikrofon starten und Analyse-Loop
await microphone.start();

setInterval(() => {
    const timeData = microphone.getTimeData();
    const fftData = microphone.getFrequencyData();
    
    if (timeData) {
        const harmonics = analyzer.analyzeHarmonics(timeData, 44100);
        visualizer.updateOptions({ fftData });
        visualizer.updateHarmonics(harmonics, 440);
    }
}, 50); // 20 FPS
```

### Beispiel 2: Intervall-Tuner

```javascript
const generator = new FrequencyGenerator({
    frequencies: [440], // A4
    waveform: 'sine',
    volume: 0.2
});

const analyzer = new HarmonicAnalyzer({
    fundamentalFreq: 440,
    xiTolerance: 5  // Sehr strenge Toleranz für Tuning
});

// Verschiedene Intervalle testen
const intervals = [
    { name: 'Oktave', ratio: 2/1, freq: 440 * 2 },
    { name: 'Quinte', ratio: 3/2, freq: 440 * 1.5 },
    { name: 'Quarte', ratio: 4/3, freq: 440 * (4/3) },
    { name: 'Große Terz', ratio: 5/4, freq: 440 * 1.25 }
];

async function testInterval(interval) {
    console.log(`🎵 Teste ${interval.name} (${interval.ratio})`);
    
    generator.updateFrequencies([440, interval.freq]);
    await generator.start();
    
    setTimeout(() => {
        const timeData = generator.getTimeData();
        const harmonics = analyzer.analyzeHarmonics(timeData, 44100);
        const detectedIntervals = analyzer.intervals;
        
        console.log(`✅ Erkannte Intervalle: ${detectedIntervals.length}`);
        detectedIntervals.forEach(int => {
            console.log(`  ${int.name}: ${int.rational.toString()} 
                         (${int.cents.toFixed(1)}¢ Abweichung)`);
        });
        
        generator.stop();
    }, 1000);
}

// Alle Intervalle der Reihe nach testen
for (const interval of intervals) {
    await testInterval(interval);
    await new Promise(resolve => setTimeout(resolve, 2000));
}
```

### Beispiel 3: Audio-Datei Harmonik-Analyse

```javascript
const canvas = document.getElementById('spectrum');
const visualizer = new SpectrumVisualizer(canvas, {
    scale: 'log',
    fullSpectrum: true,
    showRatios: true
});

const analyzer = new HarmonicAnalyzer({
    harmonicRange: 64,
    fullSpectrum: true
});

const player = new AudioFilePlayer({
    onLoad: (fileInfo) => {
        console.log(`📁 Analysiere: ${fileInfo.name}`);
        document.getElementById('file-info').innerHTML = `
            <strong>${fileInfo.name}</strong><br>
            Dauer: ${fileInfo.duration.toFixed(2)}s<br>
            Sample Rate: ${fileInfo.sampleRate}Hz<br>
            Kanäle: ${fileInfo.channels}
        `;
    }
});

// Datei-Input Handler
document.getElementById('file-input').addEventListener('change', async (e) => {
    const file = e.target.files[0];
    if (!file) return;
    
    await player.loadFile(file);
    await player.play();
    
    // Kontinuierliche Analyse während Wiedergabe
    const analysisInterval = setInterval(() => {
        const timeData = player.getTimeData();
        if (timeData && player.isPlaying) {
            const harmonics = analyzer.analyzeHarmonics(timeData, 44100);
            visualizer.updateHarmonics(harmonics);
            
            // Harmonik-Statistiken anzeigen
            document.getElementById('harmonic-count').textContent = harmonics.length;
            document.getElementById('interval-count').textContent = analyzer.intervals.length;
        } else {
            clearInterval(analysisInterval);
        }
    }, 100);
});
```

## 📖 API-Referenz

### Gemeinsame Methoden

Alle Komponenten implementieren:

```javascript
// Optionen zur Laufzeit aktualisieren
component.updateOptions(newOptions);

// Cleanup (wo anwendbar)
component.destroy();
```

### Events und Callbacks

Alle Callback-Funktionen sind optional und können zur Laufzeit geändert werden:

```javascript
// Callback nachträglich setzen
microphone.options.onLevelUpdate = (level) => {
    updateLevelMeter(level);
};

// Callback entfernen
microphone.options.onError = null;
```

### Fehlerbehandlung

```javascript
try {
    await microphone.start();
} catch (error) {
    if (error.name === 'NotAllowedError') {
        console.log('❌ Mikrofon-Zugriff verweigert');
    } else if (error.name === 'NotFoundError') {
        console.log('❌ Kein Mikrofon gefunden');
    } else {
        console.log('❌ Unbekannter Fehler:', error.message);
    }
}
```

## 🌐 Browser-Kompatibilität

### Unterstützte Browser

| Browser | Version | Mikrofon | Audio-Generierung | Canvas |
|---------|---------|----------|-------------------|--------|
| Chrome | 66+ | ✅ | ✅ | ✅ |
| Firefox | 60+ | ✅ | ✅ | ✅ |
| Safari | 11.1+ | ✅ | ✅ | ✅ |
| Edge | 79+ | ✅ | ✅ | ✅ |

### Erforderliche APIs

- **Web Audio API** - Für Audio-Verarbeitung
- **MediaDevices API** - Für Mikrofon-Zugriff
- **Canvas 2D API** - Für Visualisierung
- **File API** - Für Audio-Datei-Laden

### Feature Detection

```javascript
// Web Audio API Check
if (!window.AudioContext && !window.webkitAudioContext) {
    console.error('❌ Web Audio API nicht unterstützt');
}

// Mikrofon Check
if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
    console.error('❌ Mikrofon-API nicht unterstützt');
}

// Canvas Check
const canvas = document.createElement('canvas');
if (!canvas.getContext || !canvas.getContext('2d')) {
    console.error('❌ Canvas 2D nicht unterstützt');
}
```

## 🔧 Erweiterte Konfiguration

### Performance-Optimierung

```javascript
// Niedrige Latenz für Echtzeit-Anwendungen
const microphone = new MicrophoneManager({
    fftSize: 1024,        // Kleinere FFT für weniger Latenz
    smoothingTimeConstant: 0.3  // Weniger Glättung für schnellere Response
});

// Hohe Qualität für Analyse
const analyzer = new HarmonicAnalyzer({
    harmonicRange: 64,    // Mehr Harmonische suchen
    rationalLimit: 1000,  // Präzisere rationale Approximation
    xiTolerance: 1        // Sehr strenge Toleranz
});
```

### Memory Management

```javascript
// Cleanup-Routine für Single Page Applications
function cleanup() {
    microphone.stop();
    generator.stop();
    player.stop();
    visualizer.destroy();
}

// Bei Seitenwechsel aufrufen
window.addEventListener('beforeunload', cleanup);
```

### Custom Event Handling

```javascript
// Event-Emitter Pattern für komplexe Anwendungen
class HarmonicAnalysisApp {
    constructor() {
        this.eventHandlers = {};
        this.setupComponents();
    }
    
    on(event, handler) {
        if (!this.eventHandlers[event]) {
            this.eventHandlers[event] = [];
        }
        this.eventHandlers[event].push(handler);
    }
    
    emit(event, data) {
        if (this.eventHandlers[event]) {
            this.eventHandlers[event].forEach(handler => handler(data));
        }
    }
    
    setupComponents() {
        this.microphone = new MicrophoneManager({
            onLevelUpdate: (level) => this.emit('levelUpdate', level),
            onStart: () => this.emit('recordingStarted'),
            onStop: () => this.emit('recordingStopped')
        });
        
        this.analyzer = new HarmonicAnalyzer({
            fundamentalFreq: 440
        });
        
        this.visualizer = new SpectrumVisualizer(canvas, {
            onHarmonicHover: (harmonic) => this.emit('harmonicHover', harmonic)
        });
    }
}

// Verwendung
const app = new HarmonicAnalysisApp();
app.on('harmonicHover', (harmonic) => {
    console.log(`🎵 Harmonische: ${harmonic.frequency.toFixed(2)}Hz`);
});
```

---

## 📄 Lizenz

MIT License - Frei für kommerzielle und private Nutzung.

## 🤝 Beitrag leisten

1. Repository forken
2. Feature-Branch erstellen (`git checkout -b feature/neue-funktion`)
3. Änderungen committen (`git commit -am 'Neue Funktion hinzugefügt'`)
4. Branch pushen (`git push origin feature/neue-funktion`)
5. Pull Request erstellen

## 📞 Support

- **GitHub Issues**: Für Bugs und Feature-Requests
- **Dokumentation**: Vollständige API-Referenz im Code
- **Beispiele**: Siehe `examples/` Verzeichnis

---

**🎵 Erstellt mit Leidenschaft für präzise harmonische Analyse**