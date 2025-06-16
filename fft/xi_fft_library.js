/**
 * ξ-FFT JavaScript Library
 * Spektralanalyse durch Frequenz-Verhältnisse mit Integer-Arithmetik
 * 
 * Version: 1.0.0
 * Author: ξ-FFT Team
 * License: MIT
 * 
 * Usage:
 *   const xiFFT = new XiFFT(1000);  // Sample rate 1000 Hz
 *   const signal = XiSignal.create([60, 120], [1.0, 0.5], 2.0);
 *   const result = xiFFT.analyze(signal);
 *   console.log('Dominant ξ:', result.dominantXi.xiRatio);
 */

// ===== HAUPT ξ-FFT KLASSE =====
class XiFFT {
    /**
     * Initialisiere ξ-FFT Analyzer
     * @param {number} sampleRate - Abtastrate in Hz
     * @param {number} threshold - Schwellwert für Peak-Erkennung (0.0-1.0, default: 0.02)
     */
    constructor(sampleRate, threshold = 0.02) {
        this.sampleRate = sampleRate;
        this.threshold = Math.floor(threshold * 1000);  // Konvertiere zu Integer
        this.version = '1.0.0';
    }

    /**
     * Analysiere Signal und berechne ξ-Verhältnisse
     * @param {Array<number>} signal - Signal als Array von Integer-Werten (× 1000 skaliert)
     * @param {Array<number>} freqRange - [minFreq, maxFreq] in Hz (default: [10, 500])
     * @returns {Object} Analyse-Ergebnis mit peaks, xiRatios, dominantXi, etc.
     */
    analyze(signal, freqRange = [10, 500]) {
        if (!Array.isArray(signal) || signal.length === 0) {
            throw new Error('Signal muss ein nicht-leeres Array sein');
        }

        const peaks = this.findSpectralPeaks(signal, freqRange);
        const xiRatios = this.calculateXiRatios(peaks);
        const signalStats = this.calculateSignalStats(signal);

        return {
            peaks: peaks,
            xiRatios: xiRatios,
            dominantXi: xiRatios[0] || null,
            peakCount: peaks.length,
            complexity: xiRatios.length,
            signalStats: signalStats,
            analysisTime: Date.now(),
            version: this.version
        };
    }

    /**
     * Finde spektrale Peaks mittels DFT
     * @private
     */
    findSpectralPeaks(signal, freqRange) {
        const peaks = [];
        const [minFreq, maxFreq] = freqRange;
        const stepSize = 5;

        for (let freq = minFreq; freq <= maxFreq; freq += stepSize) {
            const magnitude = this.calculateMagnitude(signal, freq);
            
            if (magnitude > this.threshold) {
                peaks.push({
                    frequency: freq,
                    magnitude: magnitude,
                    magnitudeFloat: magnitude / 1000.0  // Für Kompatibilität
                });
            }
        }

        return peaks.sort((a, b) => b.magnitude - a.magnitude).slice(0, 10);
    }

    /**
     * Berechne DFT-Magnitude für spezifische Frequenz
     * @private
     */
    calculateMagnitude(signal, frequency) {
        const N = signal.length;
        let real = 0;
        let imag = 0;

        for (let n = 0; n < N; n++) {
            const angle = -2 * Math.PI * frequency * n / this.sampleRate;
            const cosVal = Math.cos(angle);
            const sinVal = Math.sin(angle);
            
            // Signal ist × 1000 skaliert, also rückskalieren für DFT
            real += (signal[n] / 1000.0) * cosVal;
            imag += (signal[n] / 1000.0) * sinVal;
        }

        // Magnitude = sqrt(real² + imag²) × 2 / N, dann skalieren
        const magnitude = Math.sqrt(real * real + imag * imag) * 2 / N;
        return Math.floor(magnitude * 1000);
    }

    /**
     * Berechne alle ξ-Verhältnisse zwischen Peaks
     * @private
     */
    calculateXiRatios(peaks) {
        const ratios = [];

        for (let i = 0; i < peaks.length; i++) {
            for (let j = i + 1; j < peaks.length; j++) {
                const f1 = peaks[i].frequency;
                const f2 = peaks[j].frequency;
                
                const freqHigh = Math.max(f1, f2);
                const freqLow = Math.min(f1, f2);
                
                // ξ als Integer × 100 für Präzision
                const xiRatio = Math.floor((freqHigh * 100) / freqLow);
                
                // Signifikanz: magnitude1 × magnitude2
                const significance = Math.floor((peaks[i].magnitude * peaks[j].magnitude) / 1000);
                
                ratios.push({
                    freqHigh: freqHigh,
                    freqLow: freqLow,
                    xiRatio: xiRatio,
                    xiRatioFloat: xiRatio / 100.0,  // Für Kompatibilität
                    significance: significance,
                    peakIndices: [i, j]
                });
            }
        }

        return ratios.sort((a, b) => b.significance - a.significance);
    }

    /**
     * Berechne Signal-Statistiken
     * @private
     */
    calculateSignalStats(signal) {
        let sum = 0;
        let sumSquares = 0;
        let minVal = signal[0];
        let maxVal = signal[0];

        for (let i = 0; i < signal.length; i++) {
            const val = signal[i];
            sum += val;
            sumSquares += Math.floor((val * val) / 1000);
            if (val < minVal) minVal = val;
            if (val > maxVal) maxVal = val;
        }

        const mean = Math.floor(sum / signal.length);
        const variance = Math.floor(sumSquares / signal.length) - Math.floor((mean * mean) / 1000);
        const rms = Math.floor(Math.sqrt(Math.max(0, Math.floor(sumSquares / signal.length))));

        return {
            mean: mean,
            meanFloat: mean / 1000.0,
            rms: rms,
            rmsFloat: rms / 1000.0,
            variance: Math.max(0, variance),
            std: Math.floor(Math.sqrt(Math.max(0, variance))),
            min: minVal,
            max: maxVal,
            range: maxVal - minVal,
            sampleCount: signal.length
        };
    }

    /**
     * Setze neuen Schwellwert
     * @param {number} threshold - Neuer Schwellwert (0.0-1.0)
     */
    setThreshold(threshold) {
        this.threshold = Math.floor(threshold * 1000);
    }

    /**
     * Hole aktuellen Schwellwert
     * @returns {number} Schwellwert als Float (0.0-1.0)
     */
    getThreshold() {
        return this.threshold / 1000.0;
    }
}

// ===== SIGNAL-GENERATOR KLASSE =====
class XiSignal {
    /**
     * Erstelle Testsignal mit gegebenen Frequenzen
     * @param {Array<number>} frequencies - Frequenzen in Hz
     * @param {Array<number>} amplitudes - Amplituden (0.0-1.0)
     * @param {number} duration - Dauer in Sekunden (default: 2.0)
     * @param {number} sampleRate - Abtastrate in Hz (default: 1000)
     * @param {number} noise - Rauschpegel (0.0-1.0, default: 0.0)
     * @returns {Array<number>} Signal als Integer-Array (× 1000 skaliert)
     */
    static create(frequencies, amplitudes, duration = 2.0, sampleRate = 1000, noise = 0.0) {
        if (!Array.isArray(frequencies) || !Array.isArray(amplitudes)) {
            throw new Error('Frequenzen und Amplituden müssen Arrays sein');
        }
        if (frequencies.length !== amplitudes.length) {
            throw new Error('Frequenzen und Amplituden müssen gleiche Länge haben');
        }

        const samples = Math.floor(duration * sampleRate);
        const signal = [];

        for (let i = 0; i < samples; i++) {
            const t = i / sampleRate;
            let value = 0;

            // Addiere alle Frequenzkomponenten
            for (let j = 0; j < frequencies.length; j++) {
                if (amplitudes[j] > 0) {
                    value += amplitudes[j] * Math.sin(2 * Math.PI * frequencies[j] * t);
                }
            }

            // Addiere Rauschen
            if (noise > 0) {
                value += noise * (Math.random() - 0.5) * 2;
            }

            // Skaliere zu Integer
            signal.push(Math.floor(value * 1000));
        }

        return signal;
    }

    /**
     * Erstelle Sweep-Signal (veränderliche Frequenz)
     * @param {number} startFreq - Startfrequenz in Hz
     * @param {number} endFreq - Endfrequenz in Hz
     * @param {number} duration - Dauer in Sekunden
     * @param {number} amplitude - Amplitude (0.0-1.0, default: 1.0)
     * @param {number} sampleRate - Abtastrate in Hz (default: 1000)
     * @returns {Array<number>} Sweep-Signal als Integer-Array
     */
    static createSweep(startFreq, endFreq, duration = 2.0, amplitude = 1.0, sampleRate = 1000) {
        const samples = Math.floor(duration * sampleRate);
        const signal = [];

        for (let i = 0; i < samples; i++) {
            const t = i / sampleRate;
            const progress = t / duration;
            
            // Lineare Frequenz-Interpolation
            const freq = startFreq + (endFreq - startFreq) * progress;
            
            // Phasen-kontinuierliche Frequenz-Modulation
            const phase = 2 * Math.PI * (startFreq * t + 0.5 * (endFreq - startFreq) * t * t / duration);
            const value = amplitude * Math.sin(phase);

            signal.push(Math.floor(value * 1000));
        }

        return signal;
    }

    /**
     * Lade Signal aus Array und konvertiere zu Integer
     * @param {Array<number>} floatSignal - Signal als Float-Array
     * @returns {Array<number>} Signal als Integer-Array (× 1000 skaliert)
     */
    static fromFloat(floatSignal) {
        if (!Array.isArray(floatSignal)) {
            throw new Error('Input muss ein Array sein');
        }
        
        return floatSignal.map(value => Math.floor(value * 1000));
    }

    /**
     * Konvertiere Integer-Signal zu Float
     * @param {Array<number>} intSignal - Signal als Integer-Array (× 1000 skaliert)
     * @returns {Array<number>} Signal als Float-Array
     */
    static toFloat(intSignal) {
        if (!Array.isArray(intSignal)) {
            throw new Error('Input muss ein Array sein');
        }
        
        return intSignal.map(value => value / 1000.0);
    }
}

// ===== ANOMALIE-DETEKTOR KLASSE =====
class XiAnomalyDetector {
    /**
     * Initialisiere Anomalie-Detektor
     * @param {Array<Object>} expectedRatios - Erwartete ξ-Verhältnisse 
     *   Format: [{name: 'Motor/Lager', value: 2.5, tolerance: 0.2}, ...]
     * @param {number} defaultTolerance - Standard-Toleranz (default: 0.2)
     */
    constructor(expectedRatios, defaultTolerance = 0.2) {
        this.expectedRatios = expectedRatios || [];
        this.defaultTolerance = defaultTolerance;
        this.history = [];
    }

    /**
     * Erkenne Abweichungen von erwarteten ξ-Verhältnissen
     * @param {Array<Object>} xiRatios - ξ-Verhältnisse aus XiFFT.analyze()
     * @returns {Object} Anomalie-Bericht mit matches, anomalies, healthScore
     */
    detect(xiRatios) {
        const anomalies = [];
        const matches = [];
        const timestamp = Date.now();

        for (const expected of this.expectedRatios) {
            const tolerance = expected.tolerance || this.defaultTolerance;
            let bestMatch = null;
            let minDeviation = Infinity;

            // Finde beste Übereinstimmung
            for (const actual of xiRatios) {
                const actualValue = actual.xiRatioFloat || (actual.xiRatio / 100.0);
                const deviation = Math.abs(actualValue - expected.value);
                
                if (deviation < minDeviation) {
                    minDeviation = deviation;
                    bestMatch = actual;
                }
            }

            const result = {
                expected: expected,
                actual: bestMatch,
                deviation: Math.round(minDeviation * 1000) / 1000,
                timestamp: timestamp
            };

            if (minDeviation <= tolerance) {
                result.status = 'normal';
                matches.push(result);
            } else {
                result.status = 'anomaly';
                anomalies.push(result);
            }
        }

        const healthScore = this.expectedRatios.length > 0 ? 
            Math.round((matches.length / this.expectedRatios.length) * 100) / 100 : 1.0;

        const report = {
            anomalies: anomalies,
            matches: matches,
            anomalyCount: anomalies.length,
            matchCount: matches.length,
            healthScore: healthScore,
            status: healthScore >= 0.8 ? 'healthy' : (healthScore >= 0.5 ? 'warning' : 'critical'),
            timestamp: timestamp
        };

        // Füge zu Historie hinzu
        this.history.push(report);
        if (this.history.length > 100) {
            this.history.shift();
        }

        return report;
    }

    /**
     * Hole Trend-Analyse der letzten Messungen
     * @param {number} windowSize - Anzahl letzter Messungen (default: 10)
     * @returns {Object} Trend-Information
     */
    getTrend(windowSize = 10) {
        if (this.history.length < 2) {
            return { status: 'insufficient_data', samples: this.history.length };
        }

        const recent = this.history.slice(-windowSize);
        const healthScores = recent.map(r => r.healthScore);
        
        const mean = healthScores.reduce((a, b) => a + b, 0) / healthScores.length;
        const variance = healthScores.reduce((a, b) => a + Math.pow(b - mean, 2), 0) / healthScores.length;
        const std = Math.sqrt(variance);

        // Trend-Richtung
        const first = healthScores[0];
        const last = healthScores[healthScores.length - 1];
        const trend = last > first + 0.1 ? 'improving' : 
                     last < first - 0.1 ? 'degrading' : 'stable';

        return {
            status: 'success',
            samples: recent.length,
            meanHealthScore: Math.round(mean * 1000) / 1000,
            stdDeviation: Math.round(std * 1000) / 1000,
            trend: trend,
            currentHealth: last,
            stability: std < 0.1 ? 'stable' : (std < 0.2 ? 'moderate' : 'unstable')
        };
    }

    /**
     * Füge erwartetes ξ-Verhältnis hinzu
     * @param {string} name - Name des Verhältnisses
     * @param {number} value - Erwarteter ξ-Wert
     * @param {number} tolerance - Toleranz (optional)
     */
    addExpectedRatio(name, value, tolerance) {
        this.expectedRatios.push({
            name: name,
            value: value,
            tolerance: tolerance || this.defaultTolerance
        });
    }

    /**
     * Lösche Historie
     */
    clearHistory() {
        this.history = [];
    }
}

// ===== STREAM-PROCESSOR KLASSE =====
class XiStreamProcessor {
    /**
     * Initialisiere Echtzeit-Stream-Processor
     * @param {number} sampleRate - Abtastrate in Hz
     * @param {number} bufferSize - Puffergröße für Analyse (default: 1024)
     * @param {number} overlapRatio - Überlappung (0.0-1.0, default: 0.25)
     */
    constructor(sampleRate, bufferSize = 1024, overlapRatio = 0.25) {
        this.sampleRate = sampleRate;
        this.bufferSize = bufferSize;
        this.overlapSize = Math.floor(bufferSize * overlapRatio);
        this.buffer = [];
        this.xiFFT = new XiFFT(sampleRate);
        this.results = [];
        this.callbacks = [];
    }

    /**
     * Füge Sample hinzu und analysiere bei vollem Puffer
     * @param {number} sample - Einzelner Messwert (Float)
     * @returns {Object|null} Analyse-Ergebnis wenn Puffer voll, sonst null
     */
    processSample(sample) {
        // Konvertiere zu Integer und füge hinzu
        this.buffer.push(Math.floor(sample * 1000));

        if (this.buffer.length >= this.bufferSize) {
            const result = this.xiFFT.analyze(this.buffer);
            result.bufferIndex = this.results.length;
            
            // Speichere Ergebnis
            this.results.push(result);
            if (this.results.length > 1000) {
                this.results.shift();
            }

            // Rufe Callbacks auf
            this.callbacks.forEach(callback => {
                try {
                    callback(result);
                } catch (error) {
                    console.error('Stream callback error:', error);
                }
            });

            // Puffer mit Überlappung zurücksetzen
            this.buffer = this.buffer.slice(-this.overlapSize);
            
            return result;
        }

        return null;
    }

    /**
     * Füge mehrere Samples hinzu
     * @param {Array<number>} samples - Array von Float-Samples
     * @returns {Array<Object>} Array von Analyse-Ergebnissen
     */
    processSamples(samples) {
        const results = [];
        for (const sample of samples) {
            const result = this.processSample(sample);
            if (result) {
                results.push(result);
            }
        }
        return results;
    }

    /**
     * Registriere Callback für neue Ergebnisse
     * @param {Function} callback - Callback-Funktion (result) => {}
     */
    onResult(callback) {
        if (typeof callback === 'function') {
            this.callbacks.push(callback);
        }
    }

    /**
     * Entferne Callback
     * @param {Function} callback - Zu entfernende Callback-Funktion
     */
    removeCallback(callback) {
        const index = this.callbacks.indexOf(callback);
        if (index > -1) {
            this.callbacks.splice(index, 1);
        }
    }

    /**
     * Hole Trend-Analyse der ξ-Verhältnisse
     * @param {number} windowSize - Anzahl letzter Analysen (default: 10)
     * @returns {Object} Trend-Information
     */
    getTrend(windowSize = 10) {
        if (this.results.length < 2) {
            return { status: 'insufficient_data', samples: this.results.length };
        }

        const recent = this.results.slice(-windowSize);
        const dominantXis = recent
            .filter(r => r.dominantXi)
            .map(r => r.dominantXi.xiRatioFloat || (r.dominantXi.xiRatio / 100.0));

        if (dominantXis.length === 0) {
            return { status: 'no_dominant_xi' };
        }

        const mean = dominantXis.reduce((a, b) => a + b, 0) / dominantXis.length;
        const variance = dominantXis.reduce((a, b) => a + Math.pow(b - mean, 2), 0) / dominantXis.length;
        const std = Math.sqrt(variance);

        return {
            status: 'success',
            meanXi: Math.round(mean * 1000) / 1000,
            stdXi: Math.round(std * 1000) / 1000,
            trend: std < 0.1 ? 'stable' : 'unstable',
            latestXi: dominantXis[dominantXis.length - 1],
            sampleCount: dominantXis.length,
            stability: std < 0.05 ? 'very_stable' : (std < 0.1 ? 'stable' : 'unstable')
        };
    }

    /**
     * Setze Puffergröße
     * @param {number} newSize - Neue Puffergröße
     */
    setBufferSize(newSize) {
        this.bufferSize = newSize;
        this.overlapSize = Math.floor(newSize * 0.25);
        if (this.buffer.length > newSize) {
            this.buffer = this.buffer.slice(-this.overlapSize);
        }
    }

    /**
     * Lösche alle Daten
     */
    reset() {
        this.buffer = [];
        this.results = [];
    }
}

// ===== UTILITIES KLASSE =====
class XiUtils {
    /**
     * Konvertiere ξ-Ratio zu lesbarem Text
     * @param {number} xiRatio - ξ-Verhältnis (Float oder Integer × 100)
     * @param {boolean} isInteger - Ob Input Integer × 100 ist
     * @returns {string} Formatierter Text
     */
    static formatXiRatio(xiRatio, isInteger = false) {
        const value = isInteger ? xiRatio / 100.0 : xiRatio;
        return value.toFixed(2);
    }

    /**
     * Berechne SNR (Signal-to-Noise Ratio)
     * @param {Object} signalStats - Signal-Statistiken aus analyze()
     * @param {number} noiseLevel - Rauschpegel
     * @returns {number} SNR in dB
     */
    static calculateSNR(signalStats, noiseLevel) {
        if (noiseLevel <= 0) return Infinity;
        const signalPower = signalStats.rmsFloat || (signalStats.rms / 1000.0);
        return 20 * Math.log10(signalPower / noiseLevel);
    }

    /**
     * Exportiere Ergebnisse als JSON
     * @param {Object} analysisResult - Ergebnis von analyze()
     * @returns {string} JSON String
     */
    static exportToJSON(analysisResult) {
        return JSON.stringify(analysisResult, null, 2);
    }

    /**
     * Exportiere Ergebnisse als CSV
     * @param {Array<Object>} results - Array von Analyse-Ergebnissen
     * @returns {string} CSV String
     */
    static exportToCSV(results) {
        if (!Array.isArray(results) || results.length === 0) {
            return 'No data to export';
        }

        const headers = ['timestamp', 'peakCount', 'complexity', 'dominantXi', 'healthScore'];
        const csvRows = [headers.join(',')];

        for (const result of results) {
            const row = [
                result.analysisTime || Date.now(),
                result.peakCount || 0,
                result.complexity || 0,
                result.dominantXi ? (result.dominantXi.xiRatioFloat || result.dominantXi.xiRatio / 100.0) : '',
                result.healthScore || ''
            ];
            csvRows.push(row.join(','));
        }

        return csvRows.join('\n');
    }

    /**
     * Erstelle Zusammenfassung der Analyse
     * @param {Object} result - Analyse-Ergebnis
     * @returns {string} Zusammenfassung als Text
     */
    static createSummary(result) {
        const lines = [
            '=== ξ-FFT Analyse Zusammenfassung ===',
            `Peaks gefunden: ${result.peakCount}`,
            `ξ-Verhältnisse berechnet: ${result.complexity}`,
            ''
        ];

        if (result.peaks && result.peaks.length > 0) {
            lines.push('Top Frequenzen:');
            result.peaks.slice(0, 5).forEach((peak, i) => {
                const mag = peak.magnitudeFloat || (peak.magnitude / 1000.0);
                lines.push(`${i + 1}. ${peak.frequency} Hz: ${mag.toFixed(3)}`);
            });
            lines.push('');
        }

        if (result.xiRatios && result.xiRatios.length > 0) {
            lines.push('Top ξ-Verhältnisse:');
            result.xiRatios.slice(0, 5).forEach((ratio, i) => {
                const xi = ratio.xiRatioFloat || (ratio.xiRatio / 100.0);
                lines.push(`${i + 1}. ξ(${ratio.freqHigh}/${ratio.freqLow}) = ${xi.toFixed(2)}`);
            });
        }

        return lines.join('\n');
    }
}

// ===== EXPORT FÜR VERSCHIEDENE MODULE-SYSTEME =====

// CommonJS (Node.js)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        XiFFT,
        XiSignal,
        XiAnomalyDetector,
        XiStreamProcessor,
        XiUtils
    };
}

// AMD (RequireJS)
if (typeof define === 'function' && define.amd) {
    define([], function() {
        return {
            XiFFT,
            XiSignal,
            XiAnomalyDetector,
            XiStreamProcessor,
            XiUtils
        };
    });
}

// ES6 Modules (falls unterstützt)
if (typeof window !== 'undefined') {
    window.XiFFT = XiFFT;
    window.XiSignal = XiSignal;
    window.XiAnomalyDetector = XiAnomalyDetector;
    window.XiStreamProcessor = XiStreamProcessor;
    window.XiUtils = XiUtils;
}

// ===== BEISPIEL-USAGE =====
/**
 * BEISPIEL 1: Einfache Analyse
 * 
 * const xiFFT = new XiFFT(1000);  // 1000 Hz Sample Rate
 * const signal = XiSignal.create([60, 120], [1.0, 0.5], 2.0);
 * const result = xiFFT.analyze(signal);
 * console.log('Dominantes ξ:', result.dominantXi.xiRatioFloat);
 */

/**
 * BEISPIEL 2: Maschinenüberwachung
 * 
 * const xiFFT = new XiFFT(1000, 0.1);  // Höherer Threshold
 * const detector = new XiAnomalyDetector([
 *     {name: 'Motor/Lager', value: 2.5, tolerance: 0.3},
 *     {name: 'Getriebe/Motor', value: 4.0, tolerance: 0.5}
 * ]);
 * 
 * const machineSignal = XiSignal.create([60, 150, 240], [1.0, 0.4, 0.2]);
 * const result = xiFFT.analyze(machineSignal);
 * const anomalyReport = detector.detect(result.xiRatios);
 * console.log('Gesundheits-Score:', anomalyReport.healthScore);
 */

/**
 * BEISPIEL 3: Echtzeit-Stream
 * 
 * const processor = new XiStreamProcessor(1000, 512);
 * processor.onResult(result => {
 *     console.log('Neues Ergebnis:', result.dominantXi);
 * });
 * 
 * // Simuliere kontinuierliche Daten
 * setInterval(() => {
 *     const sample = Math.sin(2 * Math.PI * 60 * Date.now() / 1000);
 *     processor.processSample(sample);
 * }, 1);
 */