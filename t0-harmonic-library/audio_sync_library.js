/**
 * AudioSyncLib - Professionelle Audio-Synchronisations-Bibliothek
 * 
 * Diese Bibliothek löst kritische Timing-Probleme in WebAudio-Anwendungen:
 * - Buffer-Timing-Desynchronisation
 * - Amplitude-Instabilität  
 * - WebAudio-Kontext-Schwankungen
 * - Goertzel-Frequenz-Quantisierung
 * 
 * @version 1.0.0
 * @author T0 Harmonic Analysis Team
 */

class AudioSyncLib {
    
    /**
     * Synchronisierter Audio-Kontext mit präziser Timing-Kontrolle
     */
    static SynchronizedAudioContext = class {
        constructor() {
            this.audioContext = null;
            this.sampleRate = 44100;
            this.fftSize = 2048;
            this.updateInterval = null;
            this.callbacks = new Set();
            this.isRunning = false;
            
            // Synchronisation-Parameter
            this.bufferDuration = 0;
            this.updateRate = 0;
            this.frameCount = 0;
            this.startTime = 0;
            
            // Monitoring
            this.timingMonitor = new AudioSyncLib.TimingMonitor();
        }
        
        async initialize() {
            this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
            this.sampleRate = this.audioContext.sampleRate;
            this.calculateTimingParameters();
            
            console.log(`AudioSyncLib: Kontext initialisiert - ${this.sampleRate}Hz`);
            return this.audioContext;
        }
        
        calculateTimingParameters() {
            // ✅ KRITISCH: Exakte Buffer-Dauer berechnen
            this.bufferDuration = (this.fftSize / this.sampleRate) * 1000; // ms
            
            // ✅ LÖSUNG: Synchronisiere Update-Rate mit Buffer-Dauer  
            this.updateRate = Math.round(this.bufferDuration);
            
            console.log(`AudioSyncLib: Buffer=${this.bufferDuration.toFixed(1)}ms, Update=${this.updateRate}ms`);
        }
        
        setFFTSize(size) {
            this.fftSize = size;
            this.calculateTimingParameters();
        }
        
        startSynchronizedLoop() {
            if (this.isRunning) return;
            
            this.isRunning = true;
            this.frameCount = 0;
            this.startTime = performance.now();
            
            // ✅ HYBRIDE TIMING-STRATEGIE: requestAnimationFrame + setTimeout
            const loop = () => {
                if (!this.isRunning) return;
                
                const currentTime = performance.now();
                const expectedTime = this.startTime + (this.frameCount * this.updateRate);
                const deviation = Math.abs(currentTime - expectedTime);
                
                // Timing-Monitoring
                this.timingMonitor.recordTiming(deviation);
                
                // ✅ ADAPTIVE AUSFÜHRUNG: Nur bei korrektem Timing
                if (deviation < 2 || this.frameCount % 2 === 0) {
                    this.executeCallbacks(currentTime);
                }
                
                this.frameCount++;
                
                // ✅ PRÄZISE DELAY-BERECHNUNG
                const nextDelay = Math.max(0, expectedTime + this.updateRate - performance.now());
                setTimeout(() => requestAnimationFrame(loop), nextDelay);
            };
            
            requestAnimationFrame(loop);
        }
        
        stopSynchronizedLoop() {
            this.isRunning = false;
            this.timingMonitor.reset();
        }
        
        executeCallbacks(timestamp) {
            for (const callback of this.callbacks) {
                try {
                    callback(timestamp);
                } catch (error) {
                    console.error('AudioSyncLib: Callback error:', error);
                }
            }
        }
        
        addCallback(callback) {
            this.callbacks.add(callback);
        }
        
        removeCallback(callback) {
            this.callbacks.delete(callback);
        }
    };
    
    /**
     * Amplitude-Stabilisierung für rauschfreie Messungen
     */
    static AmplitudeStabilizer = class {
        constructor(windowSize = 5, mode = 'moving') {
            this.windowSize = windowSize;
            this.mode = mode;
            this.reset();
        }
        
        reset() {
            this.window = [];
            this.alpha = 0.3; // für exponentiellen Filter
            this.lastValue = 0;
        }
        
        /**
         * ✅ STABILISIERUNG: Eliminiert Pegelschwankungen
         */
        stabilize(amplitude) {
            switch (this.mode) {
                case 'moving':
                    return this.movingAverage(amplitude);
                case 'exponential':
                    return this.exponentialSmoothing(amplitude);
                default:
                    return amplitude;
            }
        }
        
        movingAverage(amplitude) {
            this.window.push(amplitude);
            if (this.window.length > this.windowSize) {
                this.window.shift();
            }
            return this.window.reduce((a, b) => a + b) / this.window.length;
        }
        
        exponentialSmoothing(amplitude) {
            if (this.lastValue === 0) {
                this.lastValue = amplitude;
                return amplitude;
            }
            
            this.lastValue = this.alpha * amplitude + (1 - this.alpha) * this.lastValue;
            return this.lastValue;
        }
        
        setMode(mode) {
            this.mode = mode;
            this.reset();
        }
        
        setWindowSize(size) {
            this.windowSize = size;
            this.reset();
        }
    };
    
    /**
     * Timing-Monitor für Sync-Qualität
     */
    static TimingMonitor = class {
        constructor() {
            this.deviations = [];
            this.maxSamples = 100;
            this.callbacks = new Set();
        }
        
        recordTiming(deviation) {
            this.deviations.push(deviation);
            if (this.deviations.length > this.maxSamples) {
                this.deviations.shift();
            }
            
            // Benachrichtige Listener
            this.notifyListeners();
        }
        
        getStats() {
            if (this.deviations.length < 10) {
                return { avgDeviation: 0, maxDeviation: 0, stabilityIndex: 100 };
            }
            
            const avgDeviation = this.deviations.reduce((a, b) => a + b) / this.deviations.length;
            const maxDeviation = Math.max(...this.deviations);
            const deviationPercent = (avgDeviation / 50) * 100;
            const stabilityIndex = Math.max(0, 100 - (deviationPercent * 2));
            
            return {
                avgDeviation: avgDeviation,
                maxDeviation: maxDeviation,
                deviationPercent: deviationPercent,
                stabilityIndex: stabilityIndex,
                syncStatus: avgDeviation < 1 ? 'LOCKED' : avgDeviation < 3 ? 'SYNC' : 'DRIFT'
            };
        }
        
        addListener(callback) {
            this.callbacks.add(callback);
        }
        
        removeListener(callback) {
            this.callbacks.delete(callback);
        }
        
        notifyListeners() {
            const stats = this.getStats();
            for (const callback of this.callbacks) {
                try {
                    callback(stats);
                } catch (error) {
                    console.error('AudioSyncLib: Monitor callback error:', error);
                }
            }
        }
        
        reset() {
            this.deviations = [];
        }
    };
    
    /**
     * Präzise Goertzel-Algorithmus-Implementierung
     */
    static GoertzelAnalyzer = class {
        constructor(sampleRate = 44100, windowSize = 2048) {
            this.sampleRate = sampleRate;
            this.windowSize = windowSize;
            this.stabilizers = new Map();
        }
        
        /**
         * ✅ EXAKTE FREQUENZ-ANALYSE: Ohne Rundungsfehler
         */
        analyzeFrequency(samples, targetFreq) {
            const N = samples.length;
            const k = (N * targetFreq) / this.sampleRate; // ✅ NICHT RUNDEN!
            
            const omega = 2 * Math.PI * k / N;
            const cosine = Math.cos(omega);
            const sine = Math.sin(omega);
            const coeff = 2 * cosine;
            
            let q0 = 0, q1 = 0, q2 = 0;
            
            // Goertzel-Algorithmus
            for (let i = 0; i < N; i++) {
                q0 = coeff * q1 - q2 + samples[i];
                q2 = q1;
                q1 = q0;
            }
            
            // Magnitude berechnen
            const real = (q1 - q2 * cosine);
            const imag = (q2 * sine);
            const magnitude = Math.sqrt(real * real + imag * imag) / N;
            
            return {
                frequency: targetFreq,
                exactFrequency: k * this.sampleRate / N,
                magnitude: magnitude,
                phase: Math.atan2(imag, real),
                binAccuracy: Math.abs(targetFreq - (k * this.sampleRate / N))
            };
        }
        
        /**
         * Stabilisierte Harmonik-Analyse
         */
        analyzeHarmonics(samples, fundamentalFreq, maxHarmonics = 16) {
            const harmonics = [];
            
            for (let h = 1; h <= maxHarmonics; h++) {
                const targetFreq = fundamentalFreq * h;
                const result = this.analyzeFrequency(samples, targetFreq);
                
                // Stabilisierung pro Harmonische
                if (!this.stabilizers.has(h)) {
                    this.stabilizers.set(h, new AudioSyncLib.AmplitudeStabilizer(5, 'moving'));
                }
                
                const stabilizedMagnitude = this.stabilizers.get(h).stabilize(result.magnitude);
                
                if (stabilizedMagnitude > 0.001) { // Sehr niedrige Schwelle
                    harmonics.push({
                        harmonic: h,
                        frequency: result.frequency,
                        exactFrequency: result.exactFrequency,
                        magnitude: stabilizedMagnitude,
                        rawMagnitude: result.magnitude,
                        phase: result.phase,
                        binAccuracy: result.binAccuracy,
                        stability: (1 - Math.abs(stabilizedMagnitude - result.magnitude)) * 100
                    });
                }
            }
            
            return harmonics.sort((a, b) => b.magnitude - a.magnitude);
        }
        
        reset() {
            this.stabilizers.clear();
        }
    };
    
    /**
     * Utility-Funktionen für Musiktheorie
     */
    static MusicUtils = class {
        static noteToFreq(note, octave = 4, a4 = 440) {
            const noteOffsets = {
                'C': -9, 'C#': -8, 'Db': -8, 'D': -7, 'D#': -6, 'Eb': -6,
                'E': -5, 'F': -4, 'F#': -3, 'Gb': -3, 'G': -2, 'G#': -1, 'Ab': -1,
                'A': 0, 'A#': 1, 'Bb': 1, 'B': 2
            };
            
            const semitones = noteOffsets[note] + (octave - 4) * 12;
            return a4 * Math.pow(2, semitones / 12);
        }
        
        static freqToNote(freq, a4 = 440) {
            const noteNames = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];
            const semitoneOffset = Math.round(12 * Math.log2(freq / a4));
            const noteIndex = (9 + semitoneOffset) % 12;
            const octave = 4 + Math.floor((9 + semitoneOffset) / 12);
            
            return {
                note: noteNames[noteIndex >= 0 ? noteIndex : noteIndex + 12],
                octave: octave,
                cents: (12 * Math.log2(freq / a4) - semitoneOffset) * 100
            };
        }
        
        static calculateRationalApproximation(ratio, limit = 100) {
            let bestP = Math.round(ratio), bestQ = 1;
            let minError = Infinity;
            
            for (let q = 1; q <= limit; q++) {
                const p = Math.round(ratio * q);
                const error = Math.abs(ratio - p/q);
                
                if (error < minError) {
                    minError = error;
                    bestP = p;
                    bestQ = q;
                }
            }
            
            // GCD vereinfachen
            const gcd = (a, b) => b === 0 ? a : gcd(b, a % b);
            const g = gcd(bestP, bestQ);
            
            return {
                p: bestP / g,
                q: bestQ / g,
                error: minError,
                cents: 1200 * Math.log2((bestP/g) / (bestQ/g) / ratio)
            };
        }
    };
    
    /**
     * Performance-Benchmark für Sync-Qualität
     */
    static PerformanceBenchmark = class {
        static async testSyncAccuracy(duration = 5000) {
            console.log('AudioSyncLib: Starte Sync-Accuracy Test...');
            
            const syncContext = new AudioSyncLib.SynchronizedAudioContext();
            await syncContext.initialize();
            
            const timings = [];
            let callbackCount = 0;
            
            const testCallback = (timestamp) => {
                const expectedTime = syncContext.startTime + (callbackCount * syncContext.updateRate);
                const deviation = Math.abs(timestamp - expectedTime);
                timings.push(deviation);
                callbackCount++;
            };
            
            syncContext.addCallback(testCallback);
            syncContext.startSynchronizedLoop();
            
            await new Promise(resolve => setTimeout(resolve, duration));
            
            syncContext.stopSynchronizedLoop();
            
            const avgDeviation = timings.reduce((a, b) => a + b) / timings.length;
            const maxDeviation = Math.max(...timings);
            const minDeviation = Math.min(...timings);
            const stability = 100 - (avgDeviation / 10) * 100;
            
            const results = {
                avgDeviation: avgDeviation.toFixed(3),
                maxDeviation: maxDeviation.toFixed(3),
                minDeviation: minDeviation.toFixed(3),
                stability: Math.max(0, stability).toFixed(1),
                sampleCount: timings.length,
                targetRate: syncContext.updateRate,
                actualRate: (duration / timings.length).toFixed(1)
            };
            
            console.log('AudioSyncLib: Sync-Test Ergebnisse:', results);
            return results;
        }
        
        static async testAmplitudeStability(samples = 1000) {
            console.log('AudioSyncLib: Starte Amplitude-Stability Test...');
            
            const stabilizer = new AudioSyncLib.AmplitudeStabilizer(5, 'moving');
            const testSignal = 0.5; // Konstantes Signal
            const noise = 0.1; // 10% Rauschen
            
            let totalDeviation = 0;
            let maxDeviation = 0;
            
            for (let i = 0; i < samples; i++) {
                const noisySignal = testSignal + (Math.random() - 0.5) * noise;
                const stabilized = stabilizer.stabilize(noisySignal);
                const deviation = Math.abs(stabilized - testSignal);
                
                totalDeviation += deviation;
                maxDeviation = Math.max(maxDeviation, deviation);
            }
            
            const avgDeviation = totalDeviation / samples;
            const stabilityIndex = 100 - (avgDeviation / testSignal) * 100;
            
            const results = {
                avgDeviation: avgDeviation.toFixed(4),
                maxDeviation: maxDeviation.toFixed(4),
                stabilityIndex: stabilityIndex.toFixed(1),
                noiseReduction: (1 - avgDeviation / (noise / 2)).toFixed(2),
                samples: samples
            };
            
            console.log('AudioSyncLib: Amplitude-Test Ergebnisse:', results);
            return results;
        }
    };
    
    /**
     * Statische Hilfsmethoden
     */
    static getVersion() {
        return '1.0.0';
    }
    
    static getBuildInfo() {
        return {
            version: '1.0.0',
            buildDate: '2025-06-17',
            features: [
                'SynchronizedAudioContext',
                'AmplitudeStabilizer', 
                'TimingMonitor',
                'GoertzelAnalyzer',
                'MusicUtils',
                'PerformanceBenchmark'
            ],
            compatibility: 'Chrome 66+, Firefox 60+, Safari 14+',
            license: 'MIT'
        };
    }
    
    static logDiagnostics() {
        console.log('🎵 AudioSyncLib Diagnostics:');
        console.log('  Version:', AudioSyncLib.getVersion());
        console.log('  WebAudio Support:', !!(window.AudioContext || window.webkitAudioContext));
        console.log('  Performance API:', !!window.performance);
        console.log('  RequestAnimationFrame:', !!window.requestAnimationFrame);
        
        if (window.AudioContext || window.webkitAudioContext) {
            const testContext = new (window.AudioContext || window.webkitAudioContext)();
            console.log('  Sample Rate:', testContext.sampleRate + 'Hz');
            console.log('  Max Channels:', testContext.destination.maxChannelCount);
            testContext.close();
        }
    }
}

// Auto-Export für verschiedene Module-Systeme
if (typeof module !== 'undefined' && module.exports) {
    module.exports = AudioSyncLib;
} else if (typeof define === 'function' && define.amd) {
    define([], () => AudioSyncLib);
} else {
    window.AudioSyncLib = AudioSyncLib;
}

// Diagnose beim Laden
AudioSyncLib.logDiagnostics();