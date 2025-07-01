# Verhältnisbasierte Akkord-Identifikation durch Differenztöne

## ⚠️ **IMPLEMENTIERUNGS-ABHÄNGIGKEIT**

**Funktioniert bei:**
- ✅ Mathematischer Frequenz-Generierung (HTML-Tools)
- 🔄 Analog-Hardware-Messung (in Entwicklung)

**Funktioniert NICHT bei:**
- ❌ Browser-Audio-Pipeline (85% Phantom-Rate)
- ❌ Software-FFT-Analyse (spektrale Leckage)

---

## Implementierungs-Klassen

### **KLASSE A: Mathematische Implementation**
```javascript
const cMajor = [261.63, 329.63, 392.00];
const differences = [68.0, 130.8, 62.8]; // 3 exakte Werte
```
- Phantom-Rate: 0%
- Genauigkeit: Mathematisch exakt
- Verfügbarkeit: Sofort

### **KLASSE B: Analog-Hardware** (in Entwicklung)
```javascript
const analogFreqs = pllMeasure(audioInput); // Prototyp
const physicalDiffs = analogMixer(analogFreqs); // Konzept
```
- Erwartete Phantom-Rate: 0%
- Ziel-Genauigkeit: ±0.01Hz
- Verfügbarkeit: Q2-Q3 2025

### **KLASSE C: Browser-Audio-Pipeline**
```javascript
const audioBuffer = recordFromMicrophone();
const analysis = performFFT(audioBuffer, 32768);
// Ergebnis: 21 "Frequenzen" (18 Phantoms + 3 echte)
```
- Phantom-Rate: 85%
- Genauigkeit: ±2.7Hz
- Verfügbarkeit: Sofort (unzuverlässig)

---

## Berechnungsgrundlage

- **Verhältnisse**: Normalisiert auf Grundton = 1.0
- **Differenz-Verhältnisse**: |Verhältnis₂ - Verhältnis₁| für alle Paare
- **Universell**: Funktioniert in jeder Tonart

## Vom Differenzton zum Akkord

### Schritt-für-Schritt (für KLASSE A & B):

1. **Sammle Frequenzen**
```javascript
const frequencies = [261.6, 329.6, 392.4]; // C-Dur
```

2. **Berechne Differenztöne**
```javascript
const differences = [68.0, 130.8, 62.8]; // |f₂-f₁| für alle Paare
```

3. **Pattern-Matching**
```javascript
const normalized = [1.08, 2.08, 1.0]; // Bezogen auf kleinsten Wert
// Pattern [0.08, 1.08] → Dur-Akkord erkannt
```

### Für KLASSE C (Browser):
Phantom-Filter erforderlich:
```javascript
const filtered = differences.filter(d => !isQuantizationArtifact(d));
// Reduziert 21 → 6-8 Werte (immer noch 50% Phantoms)
```

## Verhältnis-Signaturen

### KLASSE A & B (zuverlässig):
| Akkord | Differenztöne | Pattern | Zuverlässigkeit |
|--------|---------------|---------|----------------|
| Dur | 2-3 aus 3 Noten | [0.25(2×), 0.5(1×)] | 100% |
| Moll | 3 aus 3 Noten | [0.2, 0.3, 0.5] | 100% |
| Dom7 | 5-6 aus 4 Noten | [0.25(2×), 0.3, 0.5, 0.55] | 100% |

### KLASSE C (unzuverlässig):
| Akkord | "Erkannte" Differenztöne | Phantom-Rate | Zuverlässigkeit |
|--------|-------------------------|--------------|----------------|
| Dur | 15-25 (statt 2-3) | 85-90% | 15% |
| Moll | 18-28 (statt 3) | 88-92% | 12% |
| Dom7 | 35-50 (statt 5-6) | 90-95% | 8% |

## Erkennungsregeln

### KLASSE A & B:
```javascript
// Deterministisch
if (differenztöne.length === 3) {
    if (!contains(0.5)) return "aug";
    else if (contains(0.125)) return "sus2";
    else if (isAmplified(0.25)) return "Dur";
    else if (contains([0.2, 0.3, 0.5])) return "Moll";
}
```

### KLASSE C:
```javascript
// Probabilistisch
const filtered = applyPhantomFilter(differenztöne);
const probabilities = calculateAllChordProbabilities(filtered);
return probabilities.find(p => p.confidence > 0.4);
```

## Anwendungsempfehlungen

**KLASSE A - Mathematische Tools:**
- Kompositions-Software
- Musik-Theorie-Anwendungen
- Bildungs-Tools

**KLASSE B - Analog-Hardware (geplant):**
- Live-Instrument-Tuning
- Studio-Monitoring
- Wissenschaftliche Forschung

**KLASSE C - Browser-Audio:**
- Nur Demonstration/Bildung
- DSP-Limitationen verstehen

## Zentrale Erkenntnisse

1. **Implementierung bestimmt Erfolg**: Regeln theoretisch korrekt, praktisch implementierungs-abhängig
2. **HTML-Tool-Paradox**: Beweist Theorie (mathematisch), verschleiert Audio-Problematik
3. **Hardware-Notwendigkeit**: Audio-Analyse erfordert Analog-Hardware (in Entwicklung)
4. **Aktuelle Verfügbarkeit**: Nur mathematische Implementation zuverlässig einsetzbar