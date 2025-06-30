/**
 * T0 Enhanced File Loader - Audio Buffer Testing Suite
 * Umfassende File-Loading-Funktionen für Enhanced Difference Tone Analysis Tests
 * 
 * FEATURES:
 * ✅ .t0buf File Loading (32768 bytes)
 * ✅ .json Audio Data Loading  
 * ✅ .wav File Processing
 * ✅ Synthetic Test Signal Generation
 * ✅ Batch Testing Multiple Files
 * ✅ Real-time Audio Capture (Browser)
 * ✅ Automatic Format Detection
 * ✅ Enhanced Analysis Integration
 * 
 * @version 1.0.0 - Audio Testing Ready
 */

class T0EnhancedFileLoader {
    constructor(enhancedAnalyzer = null) {
        this.enhancedAnalyzer = enhancedAnalyzer;
        this.supportedFormats = ['.t0buf', '.json', '.wav', '.raw'];
        this.loadedFiles = new Map();
        this.testResults = [];
        
        // Audio Context für Browser-Tests
        this.audioContext = null;
        this.isRecording = false;
        
        console.log("🔧 T0 Enhanced File Loader initialisiert");
        console.log(`📁 Unterstützte Formate: ${this.supportedFormats.join(', ')}`);
    }
    
    // ================================================================================================
    // FILE LOADING FUNCTIONS
    // ================================================================================================
    
    /**
     * Universal File Loader - automatische Format-Erkennung
     */
    async loadAudioFile(filePath, options = {}) {
        console.log(`📂 Lade Audio-Datei: ${filePath}`);
        
        try {
            const extension = this.getFileExtension(filePath);
            const startTime = performance.now();
            
            let audioData;
            
            switch (extension) {
                case '.t0buf':
                    audioData = await this.loadT0BufferFile(filePath, options);
                    break;
                case '.json':
                    audioData = await this.loadJSONAudioFile(filePath, options);
                    break;
                case '.wav':
                    audioData = await this.loadWAVFile(filePath, options);
                    break;
                case '.raw':
                    audioData = await this.loadRawAudioFile(filePath, options);
                    break;
                default:
                    throw new Error(`Unsupported file format: ${extension}`);
            }
            
            const loadTime = performance.now() - startTime;
            
            const fileInfo = {
                filePath: filePath,
                format: extension,
                size: audioData.buffer.length,
                sampleRate: audioData.sampleRate || 44100,
                duration: audioData.duration || (audioData.buffer.length / 44100),
                loadTime: loadTime,
                timestamp: Date.now()
            };
            
            // Cache für wiederholte Tests
            this.loadedFiles.set(filePath, { audioData, fileInfo });
            
            console.log(`✅ Datei geladen: ${audioData.buffer.length} bytes in ${loadTime.toFixed(2)}ms`);
            
            return { audioData, fileInfo };
            
        } catch (error) {
            console.error(`❌ Fehler beim Laden von ${filePath}:`, error.message);
            throw new Error(`File loading failed: ${error.message}`);
        }
    }
    
    /**
     * T0 Buffer File Loader (.t0buf) - 32768 bytes exakt
     */
    async loadT0BufferFile(filePath, options = {}) {
        const response = await fetch(filePath);
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
        
        const arrayBuffer = await response.arrayBuffer();
        const buffer = new Uint8Array(arrayBuffer);
        
        // Validiere T0 Buffer Format
        if (buffer.length !== 32768) {
            console.warn(`⚠️ T0 Buffer size mismatch: ${buffer.length} bytes (expected 32768)`);
            
            if (options.enforceSize) {
                throw new Error(`Invalid T0 buffer size: ${buffer.length} bytes`);
            }
            
            // Auto-resize falls gewünscht
            if (options.autoResize) {
                return this.resizeBufferTo32768(buffer);
            }
        }
        
        return {
            buffer: buffer,
            sampleRate: 44100,
            duration: 32768 / 44100, // 0.744 seconds
            format: 't0buf',
            validated: buffer.length === 32768
        };
    }
    
    /**
     * JSON Audio Data Loader - für gespeicherte Frequenz-Daten
     */
    async loadJSONAudioFile(filePath, options = {}) {
        const response = await fetch(filePath);
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
        
        const jsonData = await response.json();
        
        // Verschiedene JSON-Formate unterstützen
        let buffer;
        
        if (jsonData.audioBuffer || jsonData.buffer) {
            // Direkter Buffer
            const bufferData = jsonData.audioBuffer || jsonData.buffer;
            buffer = new Uint8Array(bufferData);
        } else if (jsonData.frequencies) {
            // Frequenz-Daten → synthetischer Buffer
            buffer = this.generateBufferFromFrequencies(jsonData.frequencies, options);
        } else if (jsonData.samples) {
            // Sample-Daten
            buffer = new Uint8Array(jsonData.samples);
        } else {
            throw new Error("Unknown JSON audio format");
        }
        
        return {
            buffer: buffer,
            sampleRate: jsonData.sampleRate || 44100,
            duration: buffer.length / (jsonData.sampleRate || 44100),
            format: 'json',
            metadata: jsonData.metadata || {},
            originalData: jsonData
        };
    }
    
    /**
     * WAV File Loader - konvertiert zu 32768-Byte Buffer
     */
    async loadWAVFile(filePath, options = {}) {
        const response = await fetch(filePath);
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
        
        const arrayBuffer = await response.arrayBuffer();
        const wavData = this.parseWAVFile(arrayBuffer);
        
        // Konvertiere zu T0-kompatiblem Format
        const t0Buffer = this.convertToT0Buffer(wavData, options);
        
        return {
            buffer: t0Buffer,
            sampleRate: wavData.sampleRate,
            duration: t0Buffer.length / wavData.sampleRate,
            format: 'wav',
            originalSampleRate: wavData.sampleRate,
            channels: wavData.channels,
            bitsPerSample: wavData.bitsPerSample
        };
    }
    
    /**
     * Raw Audio File Loader - binäre Audio-Daten
     */
    async loadRawAudioFile(filePath, options = {}) {
        const response = await fetch(filePath);
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
        
        const arrayBuffer = await response.arrayBuffer();
        const buffer = new Uint8Array(arrayBuffer);
        
        // Konfigurierbare Parameter für Raw-Daten
        const sampleRate = options.sampleRate || 44100;
        const channels = options.channels || 1;
        const bitsPerSample = options.bitsPerSample || 8;
        
        return {
            buffer: buffer,
            sampleRate: sampleRate,
            duration: buffer.length / sampleRate,
            format: 'raw',
            channels: channels,
            bitsPerSample: bitsPerSample
        };
    }
    
    // ================================================================================================
    // SYNTHETIC TEST SIGNAL GENERATION
    // ================================================================================================
    
    /**
     * Generiere synthetische Test-Signale für bekannte Akkorde
     */
    generateTestSignal(chordType, options = {}) {
        console.log(`🎵 Generiere Test-Signal: ${chordType}`);
        
        const config = {
            sampleRate: options.sampleRate || 44100,
            duration: options.duration || 0.744, // T0 Buffer duration
            amplitude: options.amplitude || 0.3,
            addNoise: options.addNoise || 0.05,
            fundamental: options.fundamental || 264 // C4
        };
        
        const chordDefinitions = {
            'c_major': [1, 5/4, 3/2],           // C-E-G
            'a_minor': [1, 6/5, 3/2],           // A-C-E (relativ)
            'g_dom7': [1, 5/4, 3/2, 9/5],       // G-B-D-F
            'c_maj7': [1, 5/4, 3/2, 15/8],      // C-E-G-B
            'f_sus4': [1, 4/3, 3/2],            // F-Bb-C
            'single_tone': [1],                  // Einzelton
            'complex_chord': [1, 9/8, 5/4, 3/2, 9/5, 15/8] // Komplexer Akkord
        };
        
        const intervals = chordDefinitions[chordType.toLowerCase()] || chordDefinitions['c_major'];
        const frequencies = intervals.map(ratio => config.fundamental * ratio);
        
        const bufferSize = Math.round(config.sampleRate * config.duration);
        const buffer = new Uint8Array(bufferSize);
        
        for (let i = 0; i < bufferSize; i++) {
            let sample = 0;
            
            // Addiere alle Frequenzen
            frequencies.forEach((freq, index) => {
                const amplitude = config.amplitude / Math.sqrt(index + 1); // Abnehmende Amplitude
                const phase = (i / config.sampleRate) * freq * 2 * Math.PI;
                sample += Math.sin(phase) * amplitude;
            });
            
            // Füge Rauschen hinzu für Realismus
            if (config.addNoise > 0) {
                const noise = (Math.random() - 0.5) * config.addNoise;
                sample += noise;
            }
            
            // Konvertiere zu 8-bit unsigned
            buffer[i] = Math.max(0, Math.min(255, Math.round((sample + 1) * 127.5)));
        }
        
        console.log(`✅ Test-Signal generiert: ${frequencies.map(f => f.toFixed(1)).join(', ')} Hz`);
        
        return {
            buffer: buffer,
            sampleRate: config.sampleRate,
            duration: config.duration,
            format: 'synthetic',
            chordType: chordType,
            frequencies: frequencies,
            config: config
        };
    }
    
    /**
     * Batch-Generierung für alle Standard-Akkord-Tests
     */
    generateAllTestSignals(options = {}) {
        const testSuite = [
            'c_major', 'a_minor', 'g_dom7', 'c_maj7', 
            'f_sus4', 'single_tone', 'complex_chord'
        ];
        
        const testSignals = new Map();
        
        testSuite.forEach(chordType => {
            const signal = this.generateTestSignal(chordType, options);
            testSignals.set(chordType, signal);
        });
        
        console.log(`🎵 ${testSignals.size} Test-Signale generiert`);
        return testSignals;
    }
    
    // ================================================================================================
    // BROWSER AUDIO CAPTURE (für Live-Tests)
    // ================================================================================================
    
    /**
     * Starte Live-Audio-Capture für Echtzeit-Tests
     */
    async startLiveCapture(options = {}) {
        console.log("🎤 Starte Live-Audio-Capture...");
        
        try {
            // Audio Context initialisieren
            this.audioContext = new (window.AudioContext || window.webkitAudioContext)({
                sampleRate: 44100
            });
            
            // Mikrofonzugriff
            const stream = await navigator.mediaDevices.getUserMedia({
                audio: {
                    sampleRate: 44100,
                    channelCount: 1,
                    echoCancellation: false,
                    noiseSuppression: false
                }
            });
            
            // Audio-Processing-Setup
            const source = this.audioContext.createMediaStreamSource(stream);
            const processor = this.audioContext.createScriptProcessor(4096, 1, 1);
            
            // Buffer für kontinuierliche Aufnahme
            this.captureBuffer = new Float32Array(32768);
            this.captureIndex = 0;
            this.isRecording = true;
            
            processor.onaudioprocess = (event) => {
                if (!this.isRecording) return;
                
                const inputData = event.inputBuffer.getChannelData(0);
                
                // Fülle 32768-Sample-Buffer kontinuierlich
                for (let i = 0; i < inputData.length; i++) {
                    this.captureBuffer[this.captureIndex] = inputData[i];
                    this.captureIndex = (this.captureIndex + 1) % 32768;
                }
            };
            
            source.connect(processor);
            processor.connect(this.audioContext.destination);
            
            console.log("✅ Live-Capture aktiv");
            
            return {
                audioContext: this.audioContext,
                stream: stream,
                processor: processor
            };
            
        } catch (error) {
            console.error("❌ Live-Capture Fehler:", error.message);
            throw new Error(`Live capture failed: ${error.message}`);
        }
    }
    
    /**
     * Erfasse aktuellen Audio-Buffer für Analyse
     */
    captureLiveBuffer() {
        if (!this.isRecording || !this.captureBuffer) {
            throw new Error("Live capture not active");
        }
        
        // Konvertiere Float32 zu Uint8 für T0-Kompatibilität
        const buffer = new Uint8Array(32768);
        
        for (let i = 0; i < 32768; i++) {
            // Normalisiere [-1, 1] zu [0, 255]
            const sample = Math.max(-1, Math.min(1, this.captureBuffer[i]));
            buffer[i] = Math.round((sample + 1) * 127.5);
        }
        
        return {
            buffer: buffer,
            sampleRate: 44100,
            duration: 0.744,
            format: 'live_capture',
            timestamp: Date.now()
        };
    }
    
    /**
     * Stoppe Live-Capture
     */
    stopLiveCapture() {
        this.isRecording = false;
        if (this.audioContext) {
            this.audioContext.close();
            this.audioContext = null;
        }
        console.log("🛑 Live-Capture gestoppt");
    }
    
    // ================================================================================================
    // BATCH TESTING & ANALYSIS
    // ================================================================================================
    
    /**
     * Führe Batch-Tests mit mehreren Dateien durch
     */
    async runBatchAnalysis(filePaths, options = {}) {
        console.log(`📊 Starte Batch-Analyse mit ${filePaths.length} Dateien...`);
        
        if (!this.enhancedAnalyzer) {
            throw new Error("Enhanced Analyzer required for batch analysis");
        }
        
        const results = [];
        const startTime = performance.now();
        
        for (let i = 0; i < filePaths.length; i++) {
            const filePath = filePaths[i];
            console.log(`\n📁 [${i+1}/${filePaths.length}] Analysiere: ${filePath}`);
            
            try {
                // Lade Datei
                const { audioData, fileInfo } = await this.loadAudioFile(filePath, options);
                
                // Enhanced Analysis
                const analysisResult = this.enhancedAnalyzer.analyzeDifferenceToneEnhanced(audioData.buffer);
                
                // Sammle Ergebnis
                const batchResult = {
                    filePath: filePath,
                    fileInfo: fileInfo,
                    analysisResult: analysisResult,
                    success: true,
                    
                    // Quick-Access Ergebnisse
                    chordType: analysisResult.enhancedResults.chordType.name,
                    chordConfidence: analysisResult.enhancedResults.chordTypeConfidence,
                    rootNote: analysisResult.enhancedResults.rootAnalysis?.bestCandidate?.note || "Unknown",
                    finalChord: analysisResult.enhancedResults.finalChordName,
                    overallConfidence: analysisResult.enhancedResults.overallConfidence,
                    processingTime: analysisResult.processingTimeMs,
                    reverseValidated: analysisResult.reverseValidation.validated
                };
                
                results.push(batchResult);
                
                console.log(`✅ ${batchResult.chordType} (${(batchResult.chordConfidence * 100).toFixed(1)}%) - ${batchResult.finalChord}`);
                
            } catch (error) {
                console.error(`❌ Fehler bei ${filePath}:`, error.message);
                results.push({
                    filePath: filePath,
                    success: false,
                    error: error.message
                });
            }
        }
        
        const totalTime = performance.now() - startTime;
        
        // Generiere Batch-Report
        const batchReport = this.generateBatchReport(results, totalTime);
        
        console.log("\n" + batchReport);
        
        return {
            results: results,
            summary: {
                totalFiles: filePaths.length,
                successful: results.filter(r => r.success).length,
                failed: results.filter(r => !r.success).length,
                totalTime: totalTime,
                averageTime: totalTime / filePaths.length
            }
        };
    }
    
    /**
     * Teste alle synthetischen Signale
     */
    async testAllSyntheticSignals(options = {}) {
        console.log("🧪 Teste alle synthetischen Test-Signale...");
        
        const testSignals = this.generateAllTestSignals(options);
        const results = [];
        
        for (const [chordType, signalData] of testSignals) {
            console.log(`\n🎵 Teste: ${chordType}`);
            
            try {
                if (!this.enhancedAnalyzer) {
                    throw new Error("Enhanced Analyzer required");
                }
                
                const analysisResult = this.enhancedAnalyzer.analyzeDifferenceToneEnhanced(signalData.buffer);
                
                const testResult = {
                    expectedChord: chordType,
                    detectedChord: analysisResult.enhancedResults.chordType.name,
                    confidence: analysisResult.enhancedResults.chordTypeConfidence,
                    success: this.isChordMatchCorrect(chordType, analysisResult.enhancedResults.chordType.name),
                    analysisResult: analysisResult,
                    signalData: signalData
                };
                
                results.push(testResult);
                
                const status = testResult.success ? '✅' : '❌';
                console.log(`${status} Erwartet: ${chordType}, Erkannt: ${testResult.detectedChord} (${(testResult.confidence * 100).toFixed(1)}%)`);
                
            } catch (error) {
                console.error(`❌ Test-Fehler bei ${chordType}:`, error.message);
                results.push({
                    expectedChord: chordType,
                    success: false,
                    error: error.message
                });
            }
        }
        
        // Generiere Test-Report
        const testReport = this.generateSyntheticTestReport(results);
        console.log("\n" + testReport);
        
        return results;
    }
    
    // ================================================================================================
    // ENHANCED ANALYSIS INTEGRATION
    // ================================================================================================
    
    /**
     * Analysiere geladene Datei mit Enhanced Difference Tone Analysis
     */
    async analyzeFile(filePath, options = {}) {
        console.log(`🔍 Analysiere Datei: ${filePath}`);
        
        if (!this.enhancedAnalyzer) {
            throw new Error("Enhanced Analyzer not set. Use setEnhancedAnalyzer()");
        }
        
        // Lade Datei
        const { audioData, fileInfo } = await this.loadAudioFile(filePath, options);
        
        // Enhanced Analysis
        const startTime = performance.now();
        const analysisResult = this.enhancedAnalyzer.analyzeDifferenceToneEnhanced(audioData.buffer);
        const analysisTime = performance.now() - startTime;
        
        // Detaillierte Ergebnisse
        const detailedResult = {
            file: fileInfo,
            analysis: analysisResult,
            performance: {
                loadTime: fileInfo.loadTime,
                analysisTime: analysisTime,
                totalTime: fileInfo.loadTime + analysisTime
            },
            
            // Quick Access
            chord: {
                type: analysisResult.enhancedResults.chordType.name,
                typeConfidence: analysisResult.enhancedResults.chordTypeConfidence,
                root: analysisResult.enhancedResults.rootAnalysis?.bestCandidate?.note || "Unknown",
                rootConfidence: analysisResult.enhancedResults.rootConfidence || 0,
                final: analysisResult.enhancedResults.finalChordName,
                overallConfidence: analysisResult.enhancedResults.overallConfidence
            },
            
            // Validation
            validation: {
                reverseValidated: analysisResult.reverseValidation.validated,
                methodRecommendation: analysisResult.methodComparison.improvement.recommendation,
                qualityLevel: analysisResult.qualityIndicators.improvement.level
            }
        };
        
        console.log(`✅ Analyse abgeschlossen: ${detailedResult.chord.final} (${(detailedResult.chord.overallConfidence * 100).toFixed(1)}%)`);
        
        return detailedResult;
    }
    
    /**
     * Setze Enhanced Analyzer für File-Tests
     */
    setEnhancedAnalyzer(analyzer) {
        this.enhancedAnalyzer = analyzer;
        console.log("🔧 Enhanced Analyzer gesetzt für File-Tests");
    }
    
    // ================================================================================================
    // UTILITY & HELPER FUNCTIONS
    // ================================================================================================
    
    /**
     * Automatische Datei-Extension-Erkennung
     */
    getFileExtension(filePath) {
        const lastDot = filePath.lastIndexOf('.');
        return lastDot > -1 ? filePath.substring(lastDot).toLowerCase() : '';
    }
    
    /**
     * Resize Buffer auf exakt 32768 Bytes
     */
    resizeBufferTo32768(buffer) {
        const targetSize = 32768;
        const resized = new Uint8Array(targetSize);
        
        if (buffer.length === targetSize) {
            return { buffer: buffer, resized: false };
        }
        
        if (buffer.length > targetSize) {
            // Verkürze durch Sampling
            const step = buffer.length / targetSize;
            for (let i = 0; i < targetSize; i++) {
                const sourceIndex = Math.round(i * step);
                resized[i] = buffer[sourceIndex];
            }
        } else {
            // Verlängere durch Wiederholung
            for (let i = 0; i < targetSize; i++) {
                resized[i] = buffer[i % buffer.length];
            }
        }
        
        console.log(`📏 Buffer resized: ${buffer.length} → ${targetSize} bytes`);
        
        return {
            buffer: resized,
            sampleRate: 44100,
            duration: targetSize / 44100,
            format: 'resized',
            originalSize: buffer.length,
            resized: true
        };
    }
    
    /**
     * Einfacher WAV-Parser (Header-Extraktion)
     */
    parseWAVFile(arrayBuffer) {
        const view = new DataView(arrayBuffer);
        
        // WAV Header parsen
        const sampleRate = view.getUint32(24, true);
        const channels = view.getUint16(22, true);
        const bitsPerSample = view.getUint16(34, true);
        const dataOffset = 44; // Standard WAV header size
        
        // Audio-Daten extrahieren
        const audioData = new Uint8Array(arrayBuffer, dataOffset);
        
        return {
            sampleRate: sampleRate,
            channels: channels,
            bitsPerSample: bitsPerSample,
            audioData: audioData,
            duration: audioData.length / sampleRate
        };
    }
    
    /**
     * Konvertiere zu T0-kompatiblem Buffer
     */
    convertToT0Buffer(wavData, options = {}) {
        const targetSize = options.targetSize || 32768;
        const targetSampleRate = options.targetSampleRate || 44100;
        
        let processedData = wavData.audioData;
        
        // Sample-Rate-Konvertierung (vereinfacht)
        if (wavData.sampleRate !== targetSampleRate) {
            processedData = this.resampleAudio(processedData, wavData.sampleRate, targetSampleRate);
        }
        
        // Auf Zielgröße anpassen
        if (processedData.length !== targetSize) {
            const { buffer } = this.resizeBufferTo32768(processedData);
            processedData = buffer;
        }
        
        return processedData;
    }
    
    /**
     * Vereinfachtes Audio-Resampling
     */
    resampleAudio(audioData, fromRate, toRate) {
        const ratio = fromRate / toRate;
        const outputLength = Math.round(audioData.length / ratio);
        const resampled = new Uint8Array(outputLength);
        
        for (let i = 0; i < outputLength; i++) {
            const sourceIndex = Math.round(i * ratio);
            resampled[i] = audioData[sourceIndex] || 0;
        }
        
        return resampled;
    }
    
    /**
     * Generiere Buffer aus Frequenz-Array
     */
    generateBufferFromFrequencies(frequencies, options = {}) {
        const sampleRate = options.sampleRate || 44100;
        const duration = options.duration || 0.744;
        const amplitude = options.amplitude || 0.3;
        
        const bufferSize = Math.round(sampleRate * duration);
        const buffer = new Uint8Array(bufferSize);
        
        for (let i = 0; i < bufferSize; i++) {
            let sample = 0;
            
            frequencies.forEach(freq => {
                const phase = (i / sampleRate) * freq * 2 * Math.PI;
                sample += Math.sin(phase) * amplitude;
            });
            
            buffer[i] = Math.round((sample + 1) * 127.5);
        }
        
        return buffer;
    }
    
    /**
     * Prüfe ob Akkord-Erkennung korrekt ist
     */
    isChordMatchCorrect(expected, detected) {
        const normalize = (str) => str.toLowerCase().replace(/[^a-z]/g, '');
        
        const expectedNorm = normalize(expected);
        const detectedNorm = normalize(detected);
        
        // Exakte Übereinstimmung
        if (expectedNorm === detectedNorm) return true;
        
        // Familien-Übereinstimmung
        if (expectedNorm.includes('major') && detectedNorm.includes('dur')) return true;
        if (expectedNorm.includes('minor') && detectedNorm.includes('moll')) return true;
        if (expectedNorm.includes('dom') && detectedNorm.includes('dominant')) return true;
        
        return false;
    }
    
    // ================================================================================================
    // REPORT GENERATION
    // ================================================================================================
    
    /**
     * Generiere Batch-Analysis-Report
     */
    generateBatchReport(results, totalTime) {
        const successful = results.filter(r => r.success);
        const failed = results.filter(r => !r.success);
        
        const lines = [];
        lines.push("=== T0 ENHANCED FILE LOADER - BATCH ANALYSIS REPORT ===");
        lines.push(`Total Files: ${results.length}`);
        lines.push(`Successful: ${successful.length} (${(successful.length/results.length*100).toFixed(1)}%)`);
        lines.push(`Failed: ${failed.length}`);
        lines.push(`Total Time: ${totalTime.toFixed(2)}ms`);
        lines.push(`Average Time: ${(totalTime/results.length).toFixed(2)}ms per file`);
        lines.push("");
        
        if (successful.length > 0) {
            lines.push("📊 SUCCESSFUL ANALYSES:");
            successful.forEach((result, i) => {
                lines.push(`${i+1}. ${result.filePath.split('/').pop()}`);
                lines.push(`   Chord: ${result.finalChord} (${(result.overallConfidence*100).toFixed(1)}%)`);
                lines.push(`   Type: ${result.chordType} (${(result.chordConfidence*100).toFixed(1)}%)`);
                lines.push(`   Root: ${result.rootNote}`);
                lines.push(`   Validated: ${result.reverseValidated ? 'YES' : 'NO'}`);
                lines.push(`   Time: ${result.processingTime.toFixed(2)}ms`);
                lines.push("");
            });
        }
        
        if (failed.length > 0) {
            lines.push("❌ FAILED ANALYSES:");
            failed.forEach((result, i) => {
                lines.push(`${i+1}. ${result.filePath.split('/').pop()}: ${result.error}`);
            });
            lines.push("");
        }
        
        if (successful.length > 0) {
            const avgConfidence = successful.reduce((sum, r) => sum + r.overallConfidence, 0) / successful.length;
            const avgProcessingTime = successful.reduce((sum, r) => sum + r.processingTime, 0) / successful.length;
            const validatedCount = successful.filter(r => r.reverseValidated).length;
            
            lines.push("📈 PERFORMANCE METRICS:");
            lines.push(`Average Confidence: ${(avgConfidence*100).toFixed(1)}%`);
            lines.push(`Average Processing Time: ${avgProcessingTime.toFixed(2)}ms`);
            lines.push(`Reverse Validation Rate: ${(validatedCount/successful.length*100).toFixed(1)}%`);
        }
        
        return lines.join('\n');
    }
    
    /**
     * Generiere Synthetic Test Report
     */
    generateSyntheticTestReport(results) {
        const successful = results.filter(r => r.success);
        const correctRecognitions = results.filter(r => r.success && this.isChordMatchCorrect(r.expectedChord, r.detectedChord));
        
        const lines = [];
        lines.push("=== T0 ENHANCED FILE LOADER - SYNTHETIC SIGNAL TEST REPORT ===");
        lines.push(`Total Tests: ${results.length}`);
        lines.push(`Successful: ${successful.length}`);
        lines.push(`Correct Recognitions: ${correctRecognitions.length} (${(correctRecognitions.length/results.length*100).toFixed(1)}%)`);
        lines.push("");
        
        lines.push("🧪 TEST RESULTS:");
        results.forEach((result, i) => {
            const status = result.success ? (this.isChordMatchCorrect(result.expectedChord, result.detectedChord) ? '✅' : '⚠️') : '❌';
            lines.push(`${i+1}. ${status} ${result.expectedChord}`);
            if (result.success) {
                lines.push(`   Detected: ${result.detectedChord} (${(result.confidence*100).toFixed(1)}%)`);
                lines.push(`   Match: ${this.isChordMatchCorrect(result.expectedChord, result.detectedChord) ? 'CORRECT' : 'INCORRECT'}`);
            } else {
                lines.push(`   Error: ${result.error}`);
            }
            lines.push("");
        });
        
        if (correctRecognitions.length > 0) {
            const avgConfidence = correctRecognitions.reduce((sum, r) => sum + r.confidence, 0) / correctRecognitions.length;
            lines.push(`📊 ACCURACY METRICS:`);
            lines.push(`Recognition Accuracy: ${(correctRecognitions.length/results.length*100).toFixed(1)}%`);
            lines.push(`Average Confidence (Correct): ${(avgConfidence*100).toFixed(1)}%`);
        }
        
        return lines.join('\n');
    }
}

// Export
if (typeof module !== 'undefined' && module.exports) {
    module.exports = T0EnhancedFileLoader;
}

// ================================================================================================
// USAGE EXAMPLES & QUICK START GUIDE
// ================================================================================================

/*
// 🎯 QUICK START - File Loading & Analysis

// 1. Initialize File Loader with Enhanced Analyzer
const enhancedAnalyzer = new T0DifferenceToneAnalyzer();
const fileLoader = new T0EnhancedFileLoader(enhancedAnalyzer);

// 2. Load and analyze single file
const result = await fileLoader.analyzeFile('path/to/chord.t0buf');
console.log(`Detected: ${result.chord.final} (${result.chord.overallConfidence*100}%)`);

// 3. Batch analysis of multiple files
const batchResults = await fileLoader.runBatchAnalysis([
    'recordings/c_major.t0buf',
    'recordings/a_minor.t0buf', 
    'recordings/g_dom7.t0buf'
]);

// 4. Test with synthetic signals
const syntheticResults = await fileLoader.testAllSyntheticSignals();

// 5. Live audio capture and analysis
await fileLoader.startLiveCapture();
setInterval(() => {
    const liveBuffer = fileLoader.captureLiveBuffer();
    const result = enhancedAnalyzer.analyzeDifferenceToneEnhanced(liveBuffer.buffer);
    console.log(`Live: ${result.enhancedResults.finalChordName}`);
}, 1000);

// 6. Load different file formats
const t0bufData = await fileLoader.loadAudioFile('chord.t0buf');
const wavData = await fileLoader.loadAudioFile('chord.wav');
const jsonData = await fileLoader.loadAudioFile('frequencies.json');

// 7. Generate test signals for validation
const testSignal = fileLoader.generateTestSignal('c_major', {
    fundamental: 220,  // A3 instead of C4
    amplitude: 0.5,
    addNoise: 0.1
});

// 8. File format validation
try {
    const data = await fileLoader.loadT0BufferFile('test.t0buf', {
        enforceSize: true,  // Strict 32768 bytes
        autoResize: false   // No automatic resizing
    });
} catch (error) {
    console.log('File validation failed:', error.message);
}
*/