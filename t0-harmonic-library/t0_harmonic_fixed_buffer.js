/**
 * T0 Harmonic Library - Fixed Buffer Implementation
 * Optimiert für fixen 32768 Bytes Buffer bei 44100 Hz Sample Rate
 * 
 * FIXED SPECIFICATIONS:
 * ✅ Buffer Size: EXACTLY 32768 bytes (no validation needed)
 * ✅ Sample Rate: FIXED 44100 Hz (no parameter needed)
 * ✅ Duration: 744ms (32768/44100 = 0.744 seconds)
 * ✅ Frequency Resolution: 59.33 Hz (44100/744 samples)
 * ✅ Nyquist Frequency: 22050 Hz
 * 
 * OPTIMIZATIONS:
 * ⚡ Pre-calculated constants for 44100 Hz
 * ⚡ Fixed period calculations (no division needed)
 * ⚡ Optimized frequency ranges for 744ms window
 * ⚡ Pre-allocated arrays for performance
 * 
 * @version 3.0.0 - Fixed Buffer Optimized
 */

class T0HarmonicAnalyzer {
    constructor(options = {}) {
        // FIXED CONSTANTS - NO CHANGES NEEDED
        this.SAMPLE_RATE = 44100;           // Fixed sample rate
        this.BUFFER_SIZE = 32768;           // Fixed buffer size
        this.DURATION_MS = 744.0;           // 32768/44100 * 1000
        this.FREQUENCY_RESOLUTION = 59.33;   // 44100/744
        this.NYQUIST_FREQUENCY = 22050;     // 44100/2
        this.DURATION_SECONDS = 0.744;      // For calculations
        
        // Pre-calculated period ranges for 44100 Hz
        this.MIN_PERIOD_SAMPLES = 22;       // 44100/2000 Hz max
        this.MAX_PERIOD_SAMPLES = 882;      // 44100/50 Hz min
        
        // T0-optimized options (with fixed sample rate awareness)
        this.options = {
            xiTolerance: options.xiTolerance || 50,     // Cents
            rationalLimit: options.rationalLimit || 1000,
            eulerLimit: options.eulerLimit || 6,
            harmonicRange: options.harmonicRange || 32,
            minFrequency: options.minFrequency || 50,    // Optimized for 744ms
            maxFrequency: options.maxFrequency || 2000,  // Optimized for 744ms
            confidenceThreshold: options.confidenceThreshold || 0.3,
            ...options
        };
        
        // Pre-allocated arrays for performance (fixed size)
        this.workingBuffer = new Float32Array(32768);
        this.autocorrBuffer = new Float32Array(882);  // Max period samples
        this.yinBuffer = new Float32Array(2048);      // YIN working buffer
        this.amdfBuffer = new Float32Array(882);      // AMDF working buffer
        
        // T0-konformed ξ-Profiles (optimized for fixed buffer)
        this.xiProfiles = {
            ULTRA_STRICT: { tolerance: 5, name: "Ultra Strict (744ms optimized)" },
            STRICT: { tolerance: 10, name: "Strict (744ms optimized)" },
            STANDARD: { tolerance: 50, name: "Standard (744ms optimized)" },
            LOOSE: { tolerance: 100, name: "Loose (744ms optimized)" },
            EXPERIMENTAL: { tolerance: 200, name: "Experimental (744ms optimized)" }
        };
        
        // T0-Harmonic Ratios (unchanged - universal)
        this.harmonicRatios = [
            { ratio: [1, 1], name: "Unison", eulerGradus: 1, cents: 0 },
            { ratio: [16, 15], name: "Minor Second", eulerGradus: 9, cents: 111.73 },
            { ratio: [9, 8], name: "Major Second", eulerGradus: 5, cents: 203.91 },
            { ratio: [6, 5], name: "Minor Third", eulerGradus: 5, cents: 315.64 },
            { ratio: [5, 4], name: "Major Third", eulerGradus: 5, cents: 386.31 },
            { ratio: [4, 3], name: "Perfect Fourth", eulerGradus: 4, cents: 498.04 },
            { ratio: [7, 5], name: "Tritone", eulerGradus: 6, cents: 582.51 },
            { ratio: [3, 2], name: "Perfect Fifth", eulerGradus: 4, cents: 701.96 },
            { ratio: [8, 5], name: "Minor Sixth", eulerGradus: 6, cents: 813.69 },
            { ratio: [5, 3], name: "Major Sixth", eulerGradus: 5, cents: 884.36 },
            { ratio: [9, 5], name: "Minor Seventh", eulerGradus: 6, cents: 1017.60 },
            { ratio: [15, 8], name: "Major Seventh", eulerGradus: 8, cents: 1088.27 },
            { ratio: [2, 1], name: "Octave", eulerGradus: 2, cents: 1200 }
        ];
        
        // T0-Chord Definitions (unchanged)
        this.chordDefinitions = {
            "Major": [[1,1], [5,4], [3,2]],
            "Minor": [[1,1], [6,5], [3,2]],
            "Diminished": [[1,1], [6,5], [7,5]],
            "Augmented": [[1,1], [5,4], [8,5]],
            "Major7": [[1,1], [5,4], [3,2], [15,8]],
            "Minor7": [[1,1], [6,5], [3,2], [9,5]],
            "Dominant7": [[1,1], [5,4], [3,2], [9,5]],
            "Sus2": [[1,1], [9,8], [3,2]],
            "Sus4": [[1,1], [4,3], [3,2]]
        };
    }
    
    // ================================================================================================
    // RATIONAL NUMBER CLASS (unchanged but optimized constants)
    // ================================================================================================
    
    static RationalNumber = class {
        constructor(numeratorOrDecimal, denominator = null) {
            if (denominator === null && typeof numeratorOrDecimal === 'number') {
                const result = this.approximateRationalContinuedFractions(numeratorOrDecimal, 1000);
                this.numerator = result.numerator;
                this.denominator = result.denominator;
            } else {
                if (denominator === 0) throw new Error("Denominator cannot be zero");
                
                const gcd = this.gcd(Math.abs(numeratorOrDecimal), Math.abs(denominator));
                const sign = (numeratorOrDecimal < 0) !== (denominator < 0) ? -1 : 1;
                this.numerator = Math.abs(numeratorOrDecimal) * sign / gcd;
                this.denominator = Math.abs(denominator) / gcd;
            }
        }
        
        approximateRationalContinuedFractions(decimal, maxDenominator) {
            if (decimal === 0) return { numerator: 0, denominator: 1 };
            
            const sign = decimal < 0 ? -1 : 1;
            decimal = Math.abs(decimal);
            
            const wholePart = Math.floor(decimal);
            let fractionalPart = decimal - wholePart;
            
            if (fractionalPart < 1e-10) return { numerator: sign * wholePart, denominator: 1 };
            
            let h1 = 1, k1 = 0;
            let h0 = wholePart, k0 = 1;
            
            let x = fractionalPart;
            while (k0 <= maxDenominator && Math.abs(x) > 1e-10) {
                const a = Math.floor(1 / x);
                const h2 = a * h0 + h1;
                const k2 = a * k0 + k1;
                
                if (k2 > maxDenominator) break;
                
                h1 = h0; k1 = k0;
                h0 = h2; k0 = k2;
                
                x = 1 / x - a;
            }
            
            return { numerator: sign * h0, denominator: k0 };
        }
        
        add(other) {
            const newNum = this.numerator * other.denominator + other.numerator * this.denominator;
            const newDen = this.denominator * other.denominator;
            return new T0HarmonicAnalyzer.RationalNumber(newNum, newDen);
        }
        
        subtract(other) {
            const newNum = this.numerator * other.denominator - other.numerator * this.denominator;
            const newDen = this.denominator * other.denominator;
            return new T0HarmonicAnalyzer.RationalNumber(newNum, newDen);
        }
        
        multiply(other) {
            return new T0HarmonicAnalyzer.RationalNumber(
                this.numerator * other.numerator,
                this.denominator * other.denominator
            );
        }
        
        divide(other) {
            return new T0HarmonicAnalyzer.RationalNumber(
                this.numerator * other.denominator,
                this.denominator * other.numerator
            );
        }
        
        reduceToOctave() {
            let ratio = this;
            const two = new T0HarmonicAnalyzer.RationalNumber(2, 1);
            const one = new T0HarmonicAnalyzer.RationalNumber(1, 1);
            
            while (ratio.compareTo(two) >= 0) {
                ratio = ratio.divide(two);
            }
            
            while (ratio.compareTo(one) < 0) {
                ratio = ratio.multiply(two);
            }
            
            return ratio;
        }
        
        toDouble() {
            return this.numerator / this.denominator;
        }
        
        compareTo(other) {
            const left = this.numerator * other.denominator;
            const right = other.numerator * this.denominator;
            return left - right;
        }
        
        toString() {
            if (this.denominator === 1) return this.numerator.toString();
            return `${this.numerator}/${this.denominator}`;
        }
        
        equals(other) {
            return this.numerator === other.numerator && this.denominator === other.denominator;
        }
        
        gcd(a, b) {
            a = Math.abs(a);
            b = Math.abs(b);
            while (b !== 0) {
                const temp = b;
                b = a % b;
                a = temp;
            }
            return a;
        }
    };
    
    // ================================================================================================
    // FREQUENCY DETECTION RESULT CLASS (optimized for fixed buffer)
    // ================================================================================================
    
    static FrequencyDetectionResult = class {
        constructor(fundamentalFreq, confidence, periodSamples, method, 
                   harmonics = [], spectralInfo = null, signalToNoise = 0) {
            this.fundamentalFreq = fundamentalFreq;
            this.confidence = confidence;
            this.periodSamples = periodSamples;
            this.periodMs = (periodSamples * 1000.0) / 44100; // Fixed sample rate
            this.method = method;
            this.harmonics = harmonics;
            this.spectralInfo = spectralInfo;
            this.signalToNoise = signalToNoise;
            this.timestamp = new Date();
            
            // Pre-calculated exact ratio for 44100 Hz
            this.exactRatio = fundamentalFreq > 0 ? 
                new T0HarmonicAnalyzer.RationalNumber(Math.round(fundamentalFreq * 1000) / 1000) :
                new T0HarmonicAnalyzer.RationalNumber(0, 1);
        }
        
        toString() {
            return `${this.fundamentalFreq.toFixed(2)}Hz | ${this.method} | Conf: ${this.confidence.toFixed(3)} | S/N: ${this.signalToNoise.toFixed(1)}dB`;
        }
    };
    
    // ================================================================================================
    // MAIN ANALYSIS FUNCTION - FIXED BUFFER OPTIMIZED
    // ================================================================================================
    
    /**
     * Fixed Buffer Analysis - EXACTLY 32768 bytes @ 44100 Hz
     * 🎯 UPDATED: Verwendet Verhältnis-basierte Analyse wie Faktorisierung
     */
    analyzeFixedBuffer(rawBytes) {
        // NO VALIDATION NEEDED - FIXED SIZE GUARANTEED
        const startTime = performance.now();
        
        try {
            // 1. Convert to audio samples (optimized for fixed size)
            this.convertBytesToSamplesFixed(rawBytes);
            
            // 2. 🎯 NEW: Finde alle Peak-Frequenzen (wie find_factors)
            const frequencyPeaks = this.findFrequencyPeaksFixed();
            
            // 3. 🎯 NEW: Verhältnis-Analyse (wie Faktorisierung)
            const ratioAnalysis = this.analyzeHarmonicRatiosFixed(frequencyPeaks);
            
            // 4. Musical GCD aus Verhältnis-Analyse
            const fundamentalResult = this.calculateMusicalGCDFromRatios(ratioAnalysis);
            
            // 5. 🎯 UPDATED: Harmonische Struktur aus Verhältnissen
            const harmonicAnalysis = this.analyzeHarmonicStructureFromRatios(
                ratioAnalysis, fundamentalResult.frequency
            );
            
            // 6. Chord recognition (basierend auf Verhältnis-Analyse)
            const chordAnalysis = this.recognizeChordsFromRatios(harmonicAnalysis);
            
            // 7. Euler complexity (Verhältnis-bewusst)
            const complexityAnalysis = this.calculateEulerComplexityFromRatios(harmonicAnalysis);
            
            // 8. Beating analysis (aus Peak-Frequenzen)
            const beatingAnalysis = this.analyzeBeatingFromPeaks(frequencyPeaks);
            
            const processingTime = performance.now() - startTime;
            
            return {
                // Buffer specifications
                bufferSpecs: {
                    sampleRate: this.SAMPLE_RATE,
                    bufferSize: this.BUFFER_SIZE,
                    durationMs: this.DURATION_MS,
                    frequencyResolution: this.FREQUENCY_RESOLUTION,
                    nyquistFreq: this.NYQUIST_FREQUENCY
                },
                
                // 🎯 NEW: Verhältnis-basierte Ergebnisse
                frequencyPeaks: frequencyPeaks,
                ratioAnalysis: ratioAnalysis,
                fundamentalFrequency: fundamentalResult.frequency,
                harmonicAnalysis: harmonicAnalysis,
                recognizedChords: chordAnalysis,
                complexityScore: complexityAnalysis,
                beatingAnalysis: beatingAnalysis,
                confidence: this.calculateOverallConfidenceFromRatios(harmonicAnalysis),
                processingTimeMs: processingTime,
                timestamp: Date.now(),
                
                // Analysis method indicator
                analysisMethod: "ratio-based-like-factorization"
            };
            
        } catch (error) {
            throw new Error(`T0 Fixed Buffer Ratio Analysis Error: ${error.message}`);
        }
    }
    
    // ================================================================================================
    // FIXED BUFFER PREPROCESSING
    // ================================================================================================
    
    /**
     * Convert bytes to samples - FIXED 32768 bytes
     */
    convertBytesToSamplesFixed(rawBytes) {
        // Determine byte format by sampling
        const maxValue = Math.max(...rawBytes.slice(0, 1000));
        const minValue = Math.min(...rawBytes.slice(0, 1000));
        
        let dcBias = 0;
        let maxAbs = 0;
        
        if (minValue >= 0 && maxValue <= 255) {
            // Unsigned 8-bit (0-255) → convert to signed
            for (let i = 0; i < 32768; i++) {
                this.workingBuffer[i] = (rawBytes[i] - 128) / 128.0;
            }
        } else {
            // Signed 8-bit (-128 to 127)
            for (let i = 0; i < 32768; i++) {
                const signedByte = rawBytes[i] > 127 ? rawBytes[i] - 256 : rawBytes[i];
                this.workingBuffer[i] = signedByte / 128.0;
            }
        }
        
        // Remove DC bias (optimized for fixed buffer)
        for (let i = 0; i < 32768; i++) {
            dcBias += this.workingBuffer[i];
        }
        dcBias /= 32768;
        
        // Apply DC removal and find max amplitude
        for (let i = 0; i < 32768; i++) {
            this.workingBuffer[i] -= dcBias;
            const abs = Math.abs(this.workingBuffer[i]);
            if (abs > maxAbs) maxAbs = abs;
        }
        
        // Normalize to [-1, 1]
        if (maxAbs > 0) {
            const scale = 1.0 / maxAbs;
            for (let i = 0; i < 32768; i++) {
                this.workingBuffer[i] *= scale;
            }
        }
    }
    
    // ================================================================================================
    // 🎯 NEW: VERHÄLTNIS-BASIERTE ANALYSE (wie Faktorisierung)
    // ================================================================================================
    
    /**
     * 🎯 1. Finde alle Peak-Frequenzen (wie find_factors in Faktorisierung)
     */
    findFrequencyPeaksFixed() {
        const peaks = [];
        
        // Mehrere Methoden kombinieren für robuste Peak-Erkennung
        const methods = [
            () => this.detectFrequencyAutocorrelationFixed(),
            () => this.detectFrequencyYINFixed(),
            () => this.detectFrequencyAMDFFixed(),
            () => this.detectFrequencyZeroCrossingFixed()
        ];
        
        // Erweitere um Periode-basierte Peaks
        const periodPeaks = this.detectFrequenciesPeriodBasedFixed();
        
        // Sammle alle Erkennungen
        for (const method of methods) {
            try {
                const result = method();
                if (result.fundamentalFreq > 0 && result.confidence > 0.3) {
                    peaks.push({
                        frequency: result.fundamentalFreq,
                        amplitude: this.getAmplitudeAtFrequencyFixed(result.fundamentalFreq),
                        confidence: result.confidence,
                        method: result.method,
                        periodSamples: result.periodSamples,
                        signalToNoise: result.signalToNoise
                    });
                }
            } catch (error) {
                console.warn(`Peak detection method failed: ${error.message}`);
            }
        }
        
        // Füge Periode-basierte Peaks hinzu
        for (const periodResult of periodPeaks) {
            if (periodResult.fundamentalFreq > 0 && periodResult.confidence > 0.3) {
                peaks.push({
                    frequency: periodResult.fundamentalFreq,
                    amplitude: this.getAmplitudeAtFrequencyFixed(periodResult.fundamentalFreq),
                    confidence: periodResult.confidence,
                    method: periodResult.method,
                    periodSamples: periodResult.periodSamples,
                    signalToNoise: periodResult.signalToNoise
                });
            }
        }
        
        // Filtere und sortiere Peaks (wie in Faktorisierung)
        return this.filterAndSortPeaksFixed(peaks);
    }
    
    /**
     * 🎯 2. Verhältnis-Analyse (genau wie Faktor-Verhältnisse in Faktorisierung)
     */
    analyzeHarmonicRatiosFixed(frequencyPeaks) {
        if (!frequencyPeaks || frequencyPeaks.length === 0) {
            return [];
        }
        
        // Sortiere Peaks nach Amplitude/Confidence (wie Faktoren nach Wichtigkeit)
        const sortedPeaks = [...frequencyPeaks].sort((a, b) => 
            (b.amplitude * b.confidence) - (a.amplitude * a.confidence)
        );
        
        // Nimm den stärksten Peak als Referenz (wie Basis-Faktor)
        const referencePeak = sortedPeaks[0];
        const referenceFreq = referencePeak.frequency;
        
        const ratioAnalysis = [];
        
        // 🎯 Berechne Verhältnisse zu allen anderen Peaks (wie Faktor-Verhältnisse)
        for (const peak of sortedPeaks) {
            if (peak === referencePeak) {
                // Referenz hat Verhältnis 1:1
                ratioAnalysis.push({
                    frequency: peak.frequency,
                    ratio: 1.0,
                    rationalRatio: new T0HarmonicAnalyzer.RationalNumber(1, 1),
                    amplitude: peak.amplitude,
                    confidence: peak.confidence,
                    method: peak.method,
                    isReference: true
                });
            } else {
                // Berechne Verhältnis (wie in Faktorisierung)
                const ratio = peak.frequency / referenceFreq;
                const rationalRatio = new T0HarmonicAnalyzer.RationalNumber(ratio);
                
                ratioAnalysis.push({
                    frequency: peak.frequency,
                    ratio: ratio,
                    rationalRatio: rationalRatio,
                    amplitude: peak.amplitude,
                    confidence: peak.confidence,
                    method: peak.method,
                    isReference: false
                });
            }
        }
        
        // 🎯 3. Oktaven-Reduktion (wie in Faktorisierung)
        const octaveReducedRatios = ratioAnalysis.map(analysis => ({
            ...analysis,
            octaveReduced: analysis.rationalRatio.reduceToOctave(),
            octaveShift: this.calculateOctaveShift(analysis.ratio)
        }));
        
        // 🎯 4. Harmonische Hierarchie-Suche (wie in Faktorisierung)
        return octaveReducedRatios.map(analysis => ({
            ...analysis,
            harmonicMatch: this.searchHarmonicHierarchiesFixed(analysis.octaveReduced),
            centsDeviation: this.calculateCentsDeviationFromRatio(analysis.ratio, analysis.rationalRatio)
        }));
    }
    
    /**
     * 🎯 Oktaven-Shift berechnen (wie in Faktorisierung)
     */
    calculateOctaveShift(ratio) {
        let shift = 0;
        let tempRatio = ratio;
        
        while (tempRatio >= 2.0) {
            tempRatio /= 2.0;
            shift++;
        }
        
        while (tempRatio < 1.0) {
            tempRatio *= 2.0;
            shift--;
        }
        
        return shift;
    }
    
    /**
     * 🎯 Harmonische Hierarchie-Suche (wie in Faktorisierung)
     */
    searchHarmonicHierarchiesFixed(octaveReducedRatio) {
        const targetRatio = octaveReducedRatio.toDouble();
        
        // Suche in bekannten harmonischen Verhältnissen
        for (const harmonic of this.harmonicRatios) {
            const harmonicRatio = harmonic.ratio[0] / harmonic.ratio[1];
            const difference = Math.abs(targetRatio - harmonicRatio);
            const tolerance = 0.02; // 2% Toleranz für 744ms Buffer
            
            if (difference <= tolerance) {
                return {
                    name: harmonic.name,
                    exactRatio: harmonicRatio,
                    targetRatio: targetRatio,
                    error: difference,
                    eulerGradus: harmonic.eulerGradus,
                    cents: harmonic.cents,
                    confidence: 1 - (difference / tolerance)
                };
            }
        }
        
        // Kein Match gefunden
        return {
            name: `${octaveReducedRatio.numerator}:${octaveReducedRatio.denominator}`,
            exactRatio: targetRatio,
            targetRatio: targetRatio,
            error: 0,
            eulerGradus: this.calculateEulerGradusFixed(octaveReducedRatio),
            cents: this.ratioToCentsFixed(octaveReducedRatio),
            confidence: 0.5 // Niedrige Confidence für unbekannte Verhältnisse
        };
    }
    
    /**
     * Amplitude bei spezifischer Frequenz ermitteln (vereinfacht)
     */
    getAmplitudeAtFrequencyFixed(frequency) {
        // Vereinfachte Amplitude-Schätzung basierend auf Autokorrelation
        const period = Math.round(this.SAMPLE_RATE / frequency);
        if (period < 2 || period > 32768 / 4) return 0;
        
        let correlation = 0;
        let energy = 0;
        const testLength = Math.min(32768 - period, 8192);
        
        for (let i = 0; i < testLength; i++) {
            const sample1 = this.workingBuffer[i];
            const sample2 = this.workingBuffer[i + period];
            correlation += sample1 * sample2;
            energy += sample1 * sample1;
        }
        
        return energy > 0 ? Math.abs(correlation / energy) : 0;
    }
    
    /**
     * Peak-Filterung und Sortierung (wie Faktor-Filterung)
     */
    filterAndSortPeaksFixed(peaks) {
        const filtered = [];
        const tolerance = this.FREQUENCY_RESOLUTION * 0.5; // Frequenz-Auflösung als Toleranz
        
        // Entferne Duplikate (wie doppelte Faktoren)
        for (const peak of peaks) {
            const isDuplicate = filtered.some(f => 
                Math.abs(f.frequency - peak.frequency) < tolerance
            );
            
            if (!isDuplicate) {
                filtered.push(peak);
            } else {
                // Update existierenden Peak wenn neuer besser ist
                const existingIndex = filtered.findIndex(f => 
                    Math.abs(f.frequency - peak.frequency) < tolerance
                );
                if (existingIndex >= 0 && peak.confidence > filtered[existingIndex].confidence) {
                    filtered[existingIndex] = peak;
                }
            }
        }
        
        // Filtere nach Frequenzbereich und Confidence
        return filtered
            .filter(p => p.frequency >= this.options.minFrequency && 
                        p.frequency <= this.options.maxFrequency)
            .filter(p => p.confidence > this.options.confidenceThreshold)
            .sort((a, b) => (b.amplitude * b.confidence) - (a.amplitude * a.confidence));
    }
    
    /**
     * T0-frequency detection optimized for 744ms @ 44100Hz
     */
    detectFrequenciesFixed() {
        const frequencies = [];
        
        // 1. Autocorrelation (optimized for fixed 32768 samples)
        const autocorrResult = this.detectFrequencyAutocorrelationFixed();
        if (autocorrResult.confidence > 0.7) {
            frequencies.push(autocorrResult);
        }
        
        // 2. YIN Algorithm (optimized for 744ms window)
        const yinResult = this.detectFrequencyYINFixed();
        if (yinResult.confidence > 0.6) {
            frequencies.push(yinResult);
        }
        
        // 3. AMDF (optimized for fixed buffer)
        const amdfResult = this.detectFrequencyAMDFFixed();
        if (amdfResult.confidence > 0.5) {
            frequencies.push(amdfResult);
        }
        
        // 4. Zero-crossing (optimized for 44100Hz)
        const zcrResult = this.detectFrequencyZeroCrossingFixed();
        if (zcrResult.confidence > 0.4) {
            frequencies.push(zcrResult);
        }
        
        // 5. Period-based (optimized ranges)
        const periodResults = this.detectFrequenciesPeriodBasedFixed();
        frequencies.push(...periodResults);
        
        return this.filterAndSortFrequenciesFixed(frequencies);
    }
    
    /**
     * Fixed Autocorrelation - optimized for 32768 samples @ 44100Hz
     */
    detectFrequencyAutocorrelationFixed() {
        let maxCorrelation = 0;
        let bestPeriod = 0;
        
        // Use pre-calculated period ranges
        for (let period = this.MIN_PERIOD_SAMPLES; period <= this.MAX_PERIOD_SAMPLES; period++) {
            let correlation = 0;
            let normalizer = 0;
            
            // Optimized loop for fixed buffer
            const endIndex = 32768 - period;
            for (let i = 0; i < endIndex; i++) {
                const sample1 = this.workingBuffer[i];
                const sample2 = this.workingBuffer[i + period];
                correlation += sample1 * sample2;
                normalizer += sample1 * sample1;
            }
            
            if (normalizer > 1e-10) {
                correlation /= normalizer;
                
                if (correlation > maxCorrelation) {
                    maxCorrelation = correlation;
                    bestPeriod = period;
                }
            }
        }
        
        // Pre-calculated frequency conversion
        const frequency = bestPeriod > 0 ? 44100 / bestPeriod : 0;
        const snr = this.estimateSignalToNoiseFixed(frequency);
        
        return new T0HarmonicAnalyzer.FrequencyDetectionResult(
            frequency, maxCorrelation, bestPeriod, "T0-Autocorr-Fixed", [], null, snr
        );
    }
    
    /**
     * Fixed YIN Algorithm - optimized for 744ms window
     */
    detectFrequencyYINFixed() {
        const threshold = 0.15;
        const bufferSize = Math.min(32768, 4096);
        const maxTau = Math.min(Math.floor(bufferSize / 2), this.MAX_PERIOD_SAMPLES);
        
        // Difference function (optimized)
        for (let tau = 1; tau < maxTau; tau++) {
            this.yinBuffer[tau] = 0;
            for (let i = 0; i < bufferSize - tau; i++) {
                const delta = this.workingBuffer[i] - this.workingBuffer[i + tau];
                this.yinBuffer[tau] += delta * delta;
            }
        }
        
        // Cumulative mean normalized difference
        this.yinBuffer[0] = 1;
        for (let tau = 1; tau < maxTau; tau++) {
            let sum = 0;
            for (let i = 1; i <= tau; i++) {
                sum += this.yinBuffer[i];
            }
            if (sum > 0) {
                this.yinBuffer[tau] = this.yinBuffer[tau] / (sum / tau);
            } else {
                this.yinBuffer[tau] = 1;
            }
        }
        
        // Find first minimum below threshold
        for (let tau = 2; tau < maxTau; tau++) {
            if (this.yinBuffer[tau] < threshold) {
                // Simple parabolic interpolation
                let betterTau = tau;
                if (tau < maxTau - 1 && tau > 0) {
                    const s0 = this.yinBuffer[tau - 1];
                    const s1 = this.yinBuffer[tau];
                    const s2 = this.yinBuffer[tau + 1];
                    const denominator = 2 * (2 * s1 - s2 - s0);
                    if (Math.abs(denominator) > 1e-10) {
                        betterTau = tau + (s2 - s0) / denominator;
                    }
                }
                
                const frequency = 44100 / betterTau;
                const confidence = 1 - this.yinBuffer[tau];
                const snr = this.estimateSignalToNoiseFixed(frequency);
                
                return new T0HarmonicAnalyzer.FrequencyDetectionResult(
                    frequency, confidence, Math.round(betterTau), "T0-YIN-Fixed", [], null, snr
                );
            }
        }
        
        return new T0HarmonicAnalyzer.FrequencyDetectionResult(
            0, 0, 0, "T0-YIN-Fixed", [], null, 0
        );
    }
    
    /**
     * Fixed AMDF Algorithm
     */
    detectFrequencyAMDFFixed() {
        let minValue = Infinity;
        let bestLag = 0;
        
        // Calculate AMDF for valid period range
        for (let lag = this.MIN_PERIOD_SAMPLES; lag <= this.MAX_PERIOD_SAMPLES; lag++) {
            let sum = 0;
            const endIndex = 32768 - lag;
            
            for (let i = 0; i < endIndex; i++) {
                sum += Math.abs(this.workingBuffer[i] - this.workingBuffer[i + lag]);
            }
            
            this.amdfBuffer[lag] = sum / endIndex;
            
            if (this.amdfBuffer[lag] < minValue) {
                minValue = this.amdfBuffer[lag];
                bestLag = lag;
            }
        }
        
        const frequency = bestLag > 0 ? 44100 / bestLag : 0;
        
        // Calculate confidence
        let avgAmdf = 0;
        let count = 0;
        for (let lag = this.MIN_PERIOD_SAMPLES; lag <= this.MAX_PERIOD_SAMPLES; lag++) {
            avgAmdf += this.amdfBuffer[lag];
            count++;
        }
        avgAmdf /= count;
        
        const confidence = avgAmdf > 0 ? Math.max(0, 1 - (minValue / avgAmdf)) : 0;
        const snr = this.estimateSignalToNoiseFixed(frequency);
        
        return new T0HarmonicAnalyzer.FrequencyDetectionResult(
            frequency, confidence, bestLag, "T0-AMDF-Fixed", [], null, snr
        );
    }
    
    /**
     * Fixed Zero-Crossing Algorithm
     */
    detectFrequencyZeroCrossingFixed() {
        let zeroCrossings = 0;
        let lastSign = this.workingBuffer[0] >= 0;
        
        for (let i = 1; i < 32768; i++) {
            const currentSign = this.workingBuffer[i] >= 0;
            if (currentSign !== lastSign) {
                zeroCrossings++;
                lastSign = currentSign;
            }
        }
        
        // Pre-calculated frequency conversion
        const frequency = (zeroCrossings / 2) / this.DURATION_SECONDS;
        const period = frequency > 0 ? 44100 / frequency : 0;
        
        // Calculate confidence
        const expectedCrossings = frequency * 2 * this.DURATION_SECONDS;
        const variance = Math.abs(zeroCrossings - expectedCrossings) / Math.max(expectedCrossings, 1);
        const confidence = Math.max(0, 1 - variance);
        const snr = this.estimateSignalToNoiseFixed(frequency);
        
        return new T0HarmonicAnalyzer.FrequencyDetectionResult(
            frequency, confidence, Math.round(period), "T0-ZeroCross-Fixed", [], null, snr
        );
    }
    
    /**
     * Fixed Period-based detection
     */
    detectFrequenciesPeriodBasedFixed() {
        const frequencies = [];
        
        for (let period = this.MIN_PERIOD_SAMPLES; period <= this.MAX_PERIOD_SAMPLES; period += 2) {
            let correlation = 0;
            let energy = 0;
            let count = 0;
            
            // Correlate signal with itself at different periods
            for (let i = 0; i < 32768 - period * 3; i += period) {
                for (let j = 0; j < period && i + j + period < 32768; j++) {
                    const sample1 = this.workingBuffer[i + j];
                    const sample2 = this.workingBuffer[i + j + period];
                    correlation += sample1 * sample2;
                    energy += sample1 * sample1;
                    count++;
                }
            }
            
            if (energy > 1e-10 && count > 0) {
                correlation /= energy;
                
                if (correlation > 0.3) {
                    const frequency = 44100 / period;
                    const snr = this.estimateSignalToNoiseFixed(frequency);
                    
                    frequencies.push(new T0HarmonicAnalyzer.FrequencyDetectionResult(
                        frequency, correlation, period, "T0-Period-Fixed", [], null, snr
                    ));
                }
            }
        }
        
        return frequencies;
    }
    
    /**
     * Fixed Signal-to-Noise estimation
     */
    estimateSignalToNoiseFixed(frequency) {
        if (frequency <= 0) return 0;
        
        // Simple SNR estimation for fixed buffer
        let signalPower = 0;
        for (let i = 0; i < 32768; i++) {
            signalPower += this.workingBuffer[i] * this.workingBuffer[i];
        }
        signalPower /= 32768;
        
        const noisePower = signalPower * 0.1; // Assume 10% noise
        return noisePower > 0 ? 10 * Math.log10(signalPower / noisePower) : 60;
    }
    
    // ================================================================================================
    // 🎯 VERHÄLTNIS-BASIERTE MUSICAL ANALYSIS (wie Faktorisierung)
    // ================================================================================================
    
    /**
     * 🎯 Musical GCD aus Verhältnis-Analyse (wie Faktorisierung)
     */
    calculateMusicalGCDFromRatios(ratioAnalysis) {
        if (!ratioAnalysis || ratioAnalysis.length === 0) {
            return { frequency: 0, confidence: 0, harmonicScore: 0 };
        }
        
        // Finde Referenz-Frequenz (wie Basis-Faktor)
        const referenceAnalysis = ratioAnalysis.find(r => r.isReference);
        if (!referenceAnalysis) {
            return { frequency: 0, confidence: 0, harmonicScore: 0 };
        }
        
        let bestFundamental = referenceAnalysis.frequency;
        let bestScore = 0;
        
        // Teste Referenz-Frequenz als Fundamental
        const refScore = this.evaluateFundamentalFromRatios(referenceAnalysis.frequency, ratioAnalysis);
        bestScore = refScore;
        
        // Teste auch Sub-Harmonische (wie in Faktorisierung)
        for (let divisor = 2; divisor <= 8; divisor++) {
            const subharmonic = referenceAnalysis.frequency / divisor;
            if (subharmonic >= this.options.minFrequency) {
                const score = this.evaluateFundamentalFromRatios(subharmonic, ratioAnalysis);
                if (score > bestScore) {
                    bestScore = score;
                    bestFundamental = subharmonic;
                }
            }
        }
        
        // Teste auch Ober-Harmonische
        for (let multiplier = 2; multiplier <= 4; multiplier++) {
            const harmonic = referenceAnalysis.frequency * multiplier;
            if (harmonic <= this.options.maxFrequency) {
                const score = this.evaluateFundamentalFromRatios(harmonic, ratioAnalysis);
                if (score > bestScore) {
                    bestScore = score;
                    bestFundamental = harmonic;
                }
            }
        }
        
        return {
            frequency: bestFundamental,
            confidence: Math.min(bestScore, 1.0),
            harmonicScore: bestScore,
            method: "ratio-based-gcd"
        };
    }
    
    /**
     * Fundamental-Kandidat aus Verhältnissen bewerten
     */
    evaluateFundamentalFromRatios(fundamental, ratioAnalysis) {
        if (fundamental <= 0) return 0;
        
        let score = 0;
        let totalWeight = 0;
        
        for (const analysis of ratioAnalysis) {
            const ratio = analysis.frequency / fundamental;
            const nearestInteger = Math.round(ratio);
            
            if (nearestInteger >= 1 && nearestInteger <= this.options.harmonicRange) {
                const error = Math.abs(ratio - nearestInteger) / nearestInteger;
                const toleranceRatio = 0.05; // 5% Toleranz für 744ms Buffer
                
                if (error < toleranceRatio) {
                    // Gewichtung: Einfache Verhältnisse bevorzugt (wie in Faktorisierung)
                    const simplicityWeight = 1.0 / Math.sqrt(nearestInteger);
                    const confidenceWeight = analysis.confidence * analysis.amplitude;
                    const errorWeight = 1 - error;
                    
                    const weight = simplicityWeight * confidenceWeight * errorWeight;
                    score += weight;
                }
            }
            totalWeight += analysis.confidence * analysis.amplitude;
        }
        
        return totalWeight > 0 ? score / totalWeight : 0;
    }
    
    /**
     * 🎯 Harmonische Struktur aus Verhältnissen (wie Faktorisierung)
     */
    analyzeHarmonicStructureFromRatios(ratioAnalysis, fundamentalFreq) {
        if (!fundamentalFreq || fundamentalFreq <= 0 || !ratioAnalysis) {
            return [];
        }
        
        const harmonics = [];
        
        for (const analysis of ratioAnalysis) {
            // Verhältnis zum Fundamental (wie Faktor-Verhältnis)
            const fundamentalRatio = analysis.frequency / fundamentalFreq;
            const rationalFundamentalRatio = new T0HarmonicAnalyzer.RationalNumber(fundamentalRatio);
            
            // Oktaven-Reduktion
            const octaveReduced = rationalFundamentalRatio.reduceToOctave();
            
            // Euler-Gradus berechnen
            const eulerGradus = this.calculateEulerGradusFixed(octaveReduced);
            
            // Cents-Berechnung
            const cents = this.ratioToCentsFixed(rationalFundamentalRatio);
            const centsDeviation = this.calculateCentsDeviationFromRatio(
                fundamentalRatio, rationalFundamentalRatio
            );
            
            // ξ-Confidence (Verhältnis-bewusst)
            const xiConfidence = this.calculateXiConfidenceFixed(centsDeviation);
            
            // Intervall-Identifikation
            const intervalName = this.identifyIntervalFixed(octaveReduced);
            
            // Harmonische Match-Info übernehmen
            const harmonicMatch = analysis.harmonicMatch;
            
            harmonics.push({
                frequency: analysis.frequency,
                amplitude: analysis.amplitude,
                ratio: rationalFundamentalRatio,
                octaveReduced: octaveReduced,
                eulerGradus: eulerGradus,
                cents: cents,
                centsDeviation: centsDeviation,
                confidence: analysis.confidence * xiConfidence,
                intervalName: intervalName,
                method: analysis.method,
                
                // Zusätzliche Verhältnis-Info
                harmonicMatch: harmonicMatch,
                fundamentalRatio: fundamentalRatio,
                octaveShift: analysis.octaveShift || 0,
                
                // Analyse-Methode
                analysisMethod: "ratio-based"
            });
        }
        
        return harmonics.sort((a, b) => b.confidence - a.confidence);
    }
    
    /**
     * Cents-Abweichung aus Verhältnis berechnen
     */
    calculateCentsDeviationFromRatio(actualRatio, rationalRatio) {
        const approximatedRatio = rationalRatio.toDouble();
        return 1200 * Math.log2(actualRatio / approximatedRatio);
    }
    
    /**
     * 🎯 Chord-Erkennung aus Verhältnissen
     */
    recognizeChordsFromRatios(harmonics) {
        const recognizedChords = [];
        
        // Extrahiere Oktaven-reduzierte Verhältnisse
        const ratios = harmonics
            .filter(h => h.confidence > 0.5)
            .map(h => h.octaveReduced)
            .filter((ratio, index, self) => 
                index === self.findIndex(r => 
                    r.numerator === ratio.numerator && r.denominator === ratio.denominator
                )
            );
        
        // Pattern-Matching für Akkorde (wie in Faktorisierung)
        for (const [chordName, chordRatios] of Object.entries(this.chordDefinitions)) {
            const matches = this.matchChordPatternFromRatios(ratios, chordRatios, harmonics);
            
            if (matches.length >= 2) { // Mindestens 2 Töne für Akkord
                const confidence = matches.reduce((sum, match) => sum + match.confidence, 0) / matches.length;
                
                recognizedChords.push({
                    name: chordName,
                    confidence: confidence,
                    matchingNotes: matches,
                    completeness: matches.length / chordRatios.length,
                    analysisMethod: "ratio-based"
                });
            }
        }
        
        return recognizedChords.sort((a, b) => b.confidence - a.confidence);
    }
    
    /**
     * Chord-Pattern-Matching aus Verhältnissen
     */
    matchChordPatternFromRatios(detectedRatios, chordRatios, harmonics) {
        const matches = [];
        
        for (const chordRatio of chordRatios) {
            const target = { numerator: chordRatio[0], denominator: chordRatio[1] };
            
            for (const detected of detectedRatios) {
                if (detected.numerator === target.numerator && detected.denominator === target.denominator) {
                    const harmonic = harmonics.find(h => 
                        h.octaveReduced.numerator === detected.numerator &&
                        h.octaveReduced.denominator === detected.denominator
                    );
                    
                    if (harmonic) {
                        matches.push({
                            ratio: detected,
                            confidence: harmonic.confidence,
                            intervalName: harmonic.intervalName,
                            frequency: harmonic.frequency
                        });
                    }
                    break;
                }
            }
        }
        
        return matches;
    }
    
    /**
     * 🎯 Euler-Komplexität aus Verhältnissen
     */
    calculateEulerComplexityFromRatios(harmonics) {
        if (harmonics.length === 0) {
            return { averageGradus: 0, complexity: "undefined", distribution: {} };
        }
        
        const gradusValues = harmonics.map(h => h.eulerGradus);
        const averageGradus = gradusValues.reduce((sum, g) => sum + g, 0) / gradusValues.length;
        
        const distribution = {};
        for (const gradus of gradusValues) {
            distribution[gradus] = (distribution[gradus] || 0) + 1;
        }
        
        let complexity;
        if (averageGradus <= 3) complexity = "very simple";
        else if (averageGradus <= 5) complexity = "simple";
        else if (averageGradus <= 7) complexity = "moderate";
        else if (averageGradus <= 10) complexity = "complex";
        else complexity = "very complex";
        
        return {
            averageGradus: averageGradus,
            complexity: complexity,
            distribution: distribution,
            maxGradus: Math.max(...gradusValues),
            minGradus: Math.min(...gradusValues),
            analysisMethod: "ratio-based"
        };
    }
    
    /**
     * 🎯 Beating-Analyse aus Peaks
     */
    analyzeBeatingFromPeaks(frequencyPeaks) {
        const beatingPairs = [];
        
        for (let i = 0; i < frequencyPeaks.length; i++) {
            for (let j = i + 1; j < frequencyPeaks.length; j++) {
                const peak1 = frequencyPeaks[i];
                const peak2 = frequencyPeaks[j];
                
                const f1 = peak1.frequency;
                const f2 = peak2.frequency;
                
                if (f1 > 0 && f2 > 0) {
                    const beatFreq = Math.abs(f1 - f2);
                    const beatPeriod = beatFreq > 0 ? 1 / beatFreq : Infinity;
                    const cyclesInBuffer = beatFreq * this.DURATION_SECONDS;
                    
                    // Beating-Klassifikation
                    let beatingType, musicalEffect;
                    
                    if (beatFreq <= 0.1) {
                        beatingType = "Perfect tuning";
                        musicalEffect = "stable";
                    } else if (beatFreq <= 1) {
                        beatingType = "Very slow beating";
                        musicalEffect = "barely audible in 744ms";
                    } else if (beatFreq <= 5) {
                        beatingType = "Slow beating";
                        musicalEffect = `${cyclesInBuffer.toFixed(1)} cycles in buffer`;
                    } else if (beatFreq <= 15) {
                        beatingType = "Medium beating";
                        musicalEffect = `${cyclesInBuffer.toFixed(0)} cycles in buffer`;
                    } else if (beatFreq <= 30) {
                        beatingType = "Fast beating";
                        musicalEffect = "many cycles in buffer";
                    } else {
                        beatingType = "Roughness";
                        musicalEffect = "dissonant";
                    }
                    
                    beatingPairs.push({
                        f1: f1,
                        f2: f2,
                        amplitude1: peak1.amplitude,
                        amplitude2: peak2.amplitude,
                        beatFrequency: beatFreq,
                        beatPeriod: beatPeriod,
                        beatingType: beatingType,
                        musicalEffect: musicalEffect,
                        cyclesInBuffer: cyclesInBuffer,
                        analysisMethod: "peak-based"
                    });
                }
            }
        }
        
        return beatingPairs.sort((a, b) => a.beatFrequency - b.beatFrequency);
    }
    
    /**
     * 🎯 Overall Confidence aus Verhältnissen
     */
    calculateOverallConfidenceFromRatios(harmonics) {
        if (harmonics.length === 0) return 0;
        
        let weightedSum = 0;
        let totalWeight = 0;
        
        harmonics.forEach(h => {
            // Verhältnis-basierte Gewichtung
            const eulerWeight = Math.max(0.1, 1.0 / Math.sqrt(h.eulerGradus));
            const amplitudeWeight = h.amplitude || 1.0;
            const ratioWeight = h.confidence * eulerWeight * amplitudeWeight;
            
            weightedSum += ratioWeight;
            totalWeight += eulerWeight * amplitudeWeight;
        });
        
        return totalWeight > 0 ? Math.min(weightedSum / totalWeight, 1.0) : 0;
    }
    
    /**
     * Fixed Musical GCD Calculator
     */
    calculateMusicalGCDFixed(frequencies) {
        if (!frequencies || frequencies.length === 0) {
            return { frequency: 0, confidence: 0, harmonicScore: 0 };
        }
        
        const validFreqs = frequencies
            .filter(f => f.fundamentalFreq > 0 && f.confidence > this.options.confidenceThreshold)
            .sort((a, b) => b.confidence - a.confidence);
        
        if (validFreqs.length === 0) {
            return { frequency: 0, confidence: 0, harmonicScore: 0 };
        }
        
        let bestFundamental = validFreqs[0].fundamentalFreq;
        let bestScore = 0;
        
        // Test fundamental candidates (optimized for 744ms resolution)
        for (const candidate of validFreqs) {
            const score = this.evaluateFundamentalCandidateFixed(candidate.fundamentalFreq, validFreqs);
            if (score > bestScore) {
                bestScore = score;
                bestFundamental = candidate.fundamentalFreq;
            }
        }
        
        // Test subharmonics (important for complex chords in 744ms window)
        for (const freq of validFreqs) {
            for (let divisor = 2; divisor <= 8; divisor++) {
                const subharmonic = freq.fundamentalFreq / divisor;
                if (subharmonic >= this.options.minFrequency) {
                    const score = this.evaluateFundamentalCandidateFixed(subharmonic, validFreqs);
                    if (score > bestScore) {
                        bestScore = score;
                        bestFundamental = subharmonic;
                    }
                }
            }
        }
        
        return {
            frequency: bestFundamental,
            confidence: Math.min(bestScore, 1.0),
            harmonicScore: bestScore
        };
    }
    
    /**
     * Fixed Fundamental Candidate Evaluation
     */
    evaluateFundamentalCandidateFixed(fundamental, frequencies) {
        if (fundamental <= 0) return 0;
        
        let score = 0;
        let totalWeight = 0;
        
        // Frequency resolution aware tolerance
        const baseToleranceHz = this.FREQUENCY_RESOLUTION / 2; // ~30 Hz
        
        for (const freq of frequencies) {
            const ratio = freq.fundamentalFreq / fundamental;
            const nearestInteger = Math.round(ratio);
            
            if (nearestInteger >= 1 && nearestInteger <= this.options.harmonicRange) {
                const expectedFreq = fundamental * nearestInteger;
                const errorHz = Math.abs(freq.fundamentalFreq - expectedFreq);
                const toleranceHz = Math.max(baseToleranceHz, expectedFreq * 0.02); // 2% or base resolution
                
                if (errorHz < toleranceHz) {
                    // T0-weighting: Simple intervals preferred
                    const simplicityWeight = 1.0 / Math.sqrt(nearestInteger);
                    const errorWeight = 1 - (errorHz / toleranceHz);
                    const weight = freq.confidence * simplicityWeight * errorWeight;
                    score += weight;
                }
            }
            totalWeight += freq.confidence;
        }
        
        return totalWeight > 0 ? score / totalWeight : 0;
    }
    
    /**
     * Fixed Harmonic Structure Analysis
     */
    analyzeHarmonicStructureFixed(frequencies, fundamentalFreq) {
        if (!fundamentalFreq || fundamentalFreq <= 0) {
            return [];
        }
        
        const harmonics = [];
        
        for (const freq of frequencies) {
            if (freq.confidence < this.options.confidenceThreshold) continue;
            
            const ratio = freq.fundamentalFreq / fundamentalFreq;
            const rationalApprox = new T0HarmonicAnalyzer.RationalNumber(ratio);
            
            if (rationalApprox) {
                const octaveReduced = rationalApprox.reduceToOctave();
                const eulerGradus = this.calculateEulerGradusFixed(octaveReduced);
                const cents = this.ratioToCentsFixed(rationalApprox);
                const centsDeviation = this.calculateCentsDeviationFixed(ratio, rationalApprox);
                
                // Fixed buffer ξ-confidence (considers 744ms resolution)
                const xiConfidence = this.calculateXiConfidenceFixed(centsDeviation);
                const intervalName = this.identifyIntervalFixed(octaveReduced);
                
                harmonics.push({
                    frequency: freq.fundamentalFreq,
                    ratio: rationalApprox,
                    octaveReduced: octaveReduced,
                    eulerGradus: eulerGradus,
                    cents: cents,
                    centsDeviation: centsDeviation,
                    confidence: freq.confidence * xiConfidence,
                    intervalName: intervalName,
                    method: freq.method,
                    // Fixed buffer specific
                    resolutionAdjusted: true,
                    bufferDurationMs: this.DURATION_MS
                });
            }
        }
        
        return harmonics.sort((a, b) => b.confidence - a.confidence);
    }
    
    /**
     * Fixed Euler Gradus calculation
     */
    calculateEulerGradusFixed(rational) {
        const num = Math.abs(rational.numerator);
        const den = Math.abs(rational.denominator);
        
        let gradus = 1;
        const primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31];
        
        let n = num;
        let d = den;
        
        for (const prime of primes) {
            while (n % prime === 0) {
                gradus += 1;
                n /= prime;
            }
            while (d % prime === 0) {
                gradus += 1;
                d /= prime;
            }
        }
        
        return gradus;
    }
    
    /**
     * Fixed ratio to cents conversion
     */
    ratioToCentsFixed(rational) {
        const ratio = rational.toDouble();
        return 1200 * Math.log2(ratio);
    }
    
    /**
     * Fixed cents deviation calculation
     */
    calculateCentsDeviationFixed(actualRatio, approximatedRational) {
        const approximatedRatio = approximatedRational.toDouble();
        return 1200 * Math.log2(actualRatio / approximatedRatio);
    }
    
    /**
     * Fixed ξ-confidence calculation (considers 744ms resolution)
     */
    calculateXiConfidenceFixed(centsDeviation) {
        // Adjust tolerance for 744ms buffer characteristics
        const tolerance = this.options.xiTolerance;
        const bufferAdjustment = 1.2; // Slightly relaxed for shorter buffer
        const adjustedTolerance = tolerance * bufferAdjustment;
        
        const absDeviation = Math.abs(centsDeviation);
        
        if (absDeviation <= adjustedTolerance) {
            return 1 - (absDeviation / adjustedTolerance) * 0.4;
        } else {
            return Math.max(0, 0.6 * Math.exp(-(absDeviation - adjustedTolerance) / adjustedTolerance));
        }
    }
    
    /**
     * Fixed interval identification
     */
    identifyIntervalFixed(rational) {
        for (const harmonic of this.harmonicRatios) {
            if (harmonic.ratio[0] === rational.numerator && 
                harmonic.ratio[1] === rational.denominator) {
                return harmonic.name;
            }
        }
        return `${rational.numerator}:${rational.denominator}`;
    }
    
    /**
     * Fixed chord recognition
     */
    recognizeChordsFixed(harmonics) {
        const recognizedChords = [];
        
        const ratios = harmonics
            .filter(h => h.confidence > 0.5)
            .map(h => h.octaveReduced)
            .filter((ratio, index, self) => 
                index === self.findIndex(r => 
                    r.numerator === ratio.numerator && r.denominator === ratio.denominator
                )
            );
        
        for (const [chordName, chordRatios] of Object.entries(this.chordDefinitions)) {
            const matches = this.matchChordPatternFixed(ratios, chordRatios, harmonics);
            if (matches.length >= 2) { // Relaxed for 744ms window
                const confidence = matches.reduce((sum, match) => sum + match.confidence, 0) / matches.length;
                
                recognizedChords.push({
                    name: chordName,
                    confidence: confidence,
                    matchingNotes: matches,
                    completeness: matches.length / chordRatios.length,
                    bufferOptimized: true
                });
            }
        }
        
        return recognizedChords.sort((a, b) => b.confidence - a.confidence);
    }
    
    /**
     * Fixed chord pattern matching
     */
    matchChordPatternFixed(detectedRatios, chordRatios, harmonics) {
        const matches = [];
        
        for (const chordRatio of chordRatios) {
            const target = { numerator: chordRatio[0], denominator: chordRatio[1] };
            
            for (const detected of detectedRatios) {
                if (detected.numerator === target.numerator && detected.denominator === target.denominator) {
                    const harmonic = harmonics.find(h => 
                        h.octaveReduced.numerator === detected.numerator &&
                        h.octaveReduced.denominator === detected.denominator
                    );
                    
                    if (harmonic) {
                        matches.push({
                            ratio: detected,
                            confidence: harmonic.confidence,
                            intervalName: harmonic.intervalName
                        });
                    }
                    break;
                }
            }
        }
        
        return matches;
    }
    
    /**
     * Fixed Euler complexity analysis
     */
    calculateEulerComplexityFixed(harmonics) {
        if (harmonics.length === 0) {
            return { averageGradus: 0, complexity: "undefined", distribution: {} };
        }
        
        const gradusValues = harmonics.map(h => h.eulerGradus);
        const averageGradus = gradusValues.reduce((sum, g) => sum + g, 0) / gradusValues.length;
        
        const distribution = {};
        for (const gradus of gradusValues) {
            distribution[gradus] = (distribution[gradus] || 0) + 1;
        }
        
        let complexity;
        if (averageGradus <= 3) complexity = "very simple";
        else if (averageGradus <= 5) complexity = "simple";
        else if (averageGradus <= 7) complexity = "moderate";
        else if (averageGradus <= 10) complexity = "complex";
        else complexity = "very complex";
        
        return {
            averageGradus: averageGradus,
            complexity: complexity,
            distribution: distribution,
            maxGradus: Math.max(...gradusValues),
            minGradus: Math.min(...gradusValues),
            bufferOptimized: true
        };
    }
    
    /**
     * Fixed beating analysis (optimized for 744ms)
     */
    analyzeBeatingFixed(frequencies) {
        const beatingPairs = [];
        
        for (let i = 0; i < frequencies.length; i++) {
            for (let j = i + 1; j < frequencies.length; j++) {
                const f1 = frequencies[i].fundamentalFreq;
                const f2 = frequencies[j].fundamentalFreq;
                
                if (f1 > 0 && f2 > 0) {
                    const beatFreq = Math.abs(f1 - f2);
                    const beatPeriod = beatFreq > 0 ? 1 / beatFreq : Infinity;
                    
                    // Beat cycles in 744ms buffer
                    const beatCyclesInBuffer = beatFreq * this.DURATION_SECONDS;
                    
                    let beatingType, musicalEffect;
                    
                    if (beatFreq <= 0.1) {
                        beatingType = "Perfect tuning";
                        musicalEffect = "stable";
                    } else if (beatFreq <= 1) {
                        beatingType = "Very slow beating";
                        musicalEffect = "barely audible in 744ms";
                    } else if (beatFreq <= 5) {
                        beatingType = "Slow beating";
                        musicalEffect = `${beatCyclesInBuffer.toFixed(1)} cycles in buffer`;
                    } else if (beatFreq <= 15) {
                        beatingType = "Medium beating";
                        musicalEffect = `${beatCyclesInBuffer.toFixed(0)} cycles in buffer`;
                    } else if (beatFreq <= 30) {
                        beatingType = "Fast beating";
                        musicalEffect = "many cycles in buffer";
                    } else {
                        beatingType = "Roughness";
                        musicalEffect = "dissonant";
                    }
                    
                    beatingPairs.push({
                        f1: f1,
                        f2: f2,
                        beatFrequency: beatFreq,
                        beatPeriod: beatPeriod,
                        beatingType: beatingType,
                        musicalEffect: musicalEffect,
                        cyclesInBuffer: beatCyclesInBuffer
                    });
                }
            }
        }
        
        return beatingPairs.sort((a, b) => a.beatFrequency - b.beatFrequency);
    }
    
    /**
     * Fixed frequency filtering and sorting
     */
    filterAndSortFrequenciesFixed(frequencies) {
        const filtered = [];
        
        // Use frequency resolution for duplicate detection
        const tolerance = this.FREQUENCY_RESOLUTION * 0.5;
        
        for (const freq of frequencies) {
            const isDuplicate = filtered.some(f => 
                Math.abs(f.fundamentalFreq - freq.fundamentalFreq) < tolerance
            );
            
            if (!isDuplicate) {
                filtered.push(freq);
            }
        }
        
        return filtered
            .filter(f => f.fundamentalFreq >= this.options.minFrequency && 
                        f.fundamentalFreq <= this.options.maxFrequency)
            .filter(f => f.confidence > this.options.confidenceThreshold)
            .sort((a, b) => b.confidence - a.confidence);
    }
    
    /**
     * Fixed overall confidence calculation
     */
    calculateOverallConfidenceFixed(harmonics) {
        if (harmonics.length === 0) return 0;
        
        let weightedSum = 0;
        let totalWeight = 0;
        
        harmonics.forEach(h => {
            // Buffer-adjusted weighting
            const eulerWeight = Math.max(0.1, 1.0 / Math.sqrt(h.eulerGradus));
            const bufferAdjustment = 0.9; // Slightly lower for shorter buffer
            const confidenceWeight = h.confidence * eulerWeight * bufferAdjustment;
            
            weightedSum += confidenceWeight;
            totalWeight += eulerWeight;
        });
        
        return totalWeight > 0 ? Math.min(weightedSum / totalWeight, 1.0) : 0;
    }
    
    // ================================================================================================
    // FIXED BUFFER UTILITY FUNCTIONS
    // ================================================================================================
    
    /**
     * Convert frequency to note name (fixed buffer optimized)
     */
    frequencyToNoteNameFixed(frequency) {
        if (frequency <= 0) return "Unknown";
        
        const A4 = 440.0;
        const noteNames = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"];
        
        const semitonesFromA4 = 12 * Math.log2(frequency / A4);
        const noteIndex = Math.round(semitonesFromA4) % 12;
        const octave = Math.floor((Math.round(semitonesFromA4) + 9) / 12) + 4;
        
        const adjustedNoteIndex = noteIndex < 0 ? noteIndex + 12 : noteIndex;
        
        return `${noteNames[adjustedNoteIndex]}${octave}`;
    }
    
    /**
     * Generate ratio-based analysis report
     */
    generateRatioBasedReport(analysisResult) {
        const lines = [];
        lines.push("=== T0 HARMONIC ANALYSIS - RATIO-BASED REPORT (wie Faktorisierung) ===");
        lines.push(`Buffer: 32768 bytes @ 44100 Hz (${this.DURATION_MS.toFixed(1)} ms)`);
        lines.push(`Frequency Resolution: ${this.FREQUENCY_RESOLUTION.toFixed(2)} Hz`);
        lines.push(`Analysis Method: ${analysisResult.analysisMethod}`);
        lines.push(`Processing Time: ${analysisResult.processingTimeMs.toFixed(2)} ms`);
        lines.push("");
        
        lines.push("🎯 STEP 1: FREQUENCY PEAKS (wie find_factors):");
        if (analysisResult.frequencyPeaks) {
            analysisResult.frequencyPeaks.forEach((peak, i) => {
                lines.push(`${i+1}. ${peak.frequency.toFixed(2)} Hz - Amp: ${peak.amplitude.toFixed(3)} - Conf: ${(peak.confidence * 100).toFixed(1)}% (${peak.method})`);
            });
        }
        lines.push("");
        
        lines.push("🎯 STEP 2: RATIO ANALYSIS (wie Faktor-Verhältnisse):");
        if (analysisResult.ratioAnalysis) {
            analysisResult.ratioAnalysis.forEach((ratio, i) => {
                const ratioStr = ratio.ratio.toFixed(4);
                const rationalStr = ratio.rationalRatio.toString();
                const octaveStr = ratio.octaveReduced.toString();
                
                lines.push(`${i+1}. ${ratio.frequency.toFixed(2)} Hz → Ratio: ${ratioStr} (${rationalStr})`);
                lines.push(`    Octave Reduced: ${octaveStr}`);
                if (ratio.harmonicMatch) {
                    lines.push(`    Harmonic Match: ${ratio.harmonicMatch.name} (${(ratio.harmonicMatch.confidence * 100).toFixed(1)}%)`);
                }
                lines.push("");
            });
        }
        
        lines.push("🎯 STEP 3: FUNDAMENTAL FROM RATIOS (wie Musical GCD):");
        lines.push(`Fundamental: ${analysisResult.fundamentalFrequency.toFixed(2)} Hz`);
        lines.push(`Note: ${this.frequencyToNoteNameFixed(analysisResult.fundamentalFrequency)}`);
        lines.push(`Overall Confidence: ${(analysisResult.confidence * 100).toFixed(1)}%`);
        lines.push("");
        
        lines.push("🎯 STEP 4: HARMONIC STRUCTURE FROM RATIOS:");
        analysisResult.harmonicAnalysis.forEach((harmonic, i) => {
            lines.push(`${i+1}. ${harmonic.intervalName}: ${harmonic.frequency.toFixed(2)}Hz`);
            lines.push(`    Ratio: ${harmonic.ratio.toString()} → Octave: ${harmonic.octaveReduced.toString()}`);
            lines.push(`    Euler: ${harmonic.eulerGradus}, Cents: ${harmonic.cents.toFixed(1)}¢, Dev: ${harmonic.centsDeviation.toFixed(1)}¢`);
            lines.push(`    Confidence: ${(harmonic.confidence * 100).toFixed(1)}% | Amplitude: ${harmonic.amplitude.toFixed(3)}`);
            lines.push("");
        });
        
        lines.push("🎯 STEP 5: CHORD RECOGNITION FROM RATIOS:");
        if (analysisResult.recognizedChords.length > 0) {
            analysisResult.recognizedChords.forEach((chord, i) => {
                lines.push(`${i+1}. ${chord.name} (${(chord.confidence * 100).toFixed(1)}%)`);
                lines.push(`    Completeness: ${(chord.completeness * 100).toFixed(1)}%`);
                lines.push(`    Notes: ${chord.matchingNotes.map(n => `${n.intervalName} (${n.frequency.toFixed(1)}Hz)`).join(', ')}`);
                lines.push("");
            });
        } else {
            lines.push("No clear chord patterns detected from ratios.");
            lines.push("");
        }
        
        lines.push("🎯 COMPARISON TO FACTORIZATION METHOD:");
        lines.push("✅ find_factors() → findFrequencyPeaksFixed()");
        lines.push("✅ calculate_ratios() → analyzeHarmonicRatiosFixed()");
        lines.push("✅ reduce_to_octave() → octaveReduced calculation");
        lines.push("✅ search_harmonic_hierarchies() → searchHarmonicHierarchiesFixed()");
        lines.push("✅ Ratio-based analysis complete!");
        
        return lines.join('\n');
    }
}

// Export for module usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = T0HarmonicAnalyzer;
}

// ================================================================================================
// USAGE EXAMPLE - FIXED BUFFER
// ================================================================================================

/*
// 🎯 USAGE EXAMPLE - RATIO-BASED ANALYSIS (wie Faktorisierung)
const analyzer = new T0HarmonicAnalyzer({
    xiTolerance: 50,           // Standard tolerance
    confidenceThreshold: 0.3,  // Adjusted for ratio analysis
    minFrequency: 50,          // Optimized for 744ms
    maxFrequency: 2000         // Optimized for 744ms
});

// Analyze EXACTLY 32768 bytes with RATIO-BASED method
const rawAudioBytes = new Uint8Array(32768);
// ... fill with actual audio data ...

console.log("🎯 Starting RATIO-BASED analysis (like factorization)...");
const result = analyzer.analyzeFixedBuffer(rawAudioBytes);

console.log("=== RATIO-BASED ANALYSIS RESULT ===");
console.log(`Analysis Method: ${result.analysisMethod}`);
console.log(`Buffer: ${result.bufferSpecs.bufferSize} bytes @ ${result.bufferSpecs.sampleRate} Hz`);

// Show the factorization-like steps
console.log("\n🎯 STEP 1: Found Frequency Peaks (wie find_factors):");
result.frequencyPeaks.forEach((peak, i) => {
    console.log(`${i+1}. ${peak.frequency.toFixed(2)}Hz (${peak.method}) - Amp: ${peak.amplitude.toFixed(3)}`);
});

console.log("\n🎯 STEP 2: Calculated Ratios (wie factor ratios):");
result.ratioAnalysis.forEach((ratio, i) => {
    console.log(`${i+1}. ${ratio.frequency.toFixed(2)}Hz / ${result.frequencyPeaks[0].frequency.toFixed(2)}Hz = ${ratio.ratio.toFixed(4)}`);
    console.log(`    Rational: ${ratio.rationalRatio.toString()} → Octave: ${ratio.octaveReduced.toString()}`);
    if (ratio.harmonicMatch) {
        console.log(`    Match: ${ratio.harmonicMatch.name} (${(ratio.harmonicMatch.confidence*100).toFixed(1)}%)`);
    }
});

console.log("\n🎯 STEP 3: Found Fundamental (wie musical GCD):");
console.log(`Fundamental: ${result.fundamentalFrequency.toFixed(2)}Hz`);

console.log("\n🎯 STEP 4: Harmonic Structure from Ratios:");
result.harmonicAnalysis.forEach((h, i) => {
    console.log(`${i+1}. ${h.intervalName}: ${h.frequency.toFixed(2)}Hz (${(h.confidence*100).toFixed(1)}%)`);
});

console.log("\n🎯 STEP 5: Recognized Chords from Ratios:");
result.recognizedChords.forEach((chord, i) => {
    console.log(`${i+1}. ${chord.name} (${(chord.confidence*100).toFixed(1)}%)`);
});

// Generate detailed ratio-based report
console.log("\n" + analyzer.generateRatioBasedReport(result));

console.log("\n🎉 RATIO-BASED ANALYSIS COMPLETE!");
console.log("✅ Successfully transferred factorization logic to audio analysis!");
console.log("✅ find_factors() → findFrequencyPeaksFixed()");
console.log("✅ calculate_ratios() → analyzeHarmonicRatiosFixed()"); 
console.log("✅ search_harmonic_hierarchies() → searchHarmonicHierarchiesFixed()");
*/