/**
 * HARMONISCHE ANALYSE - KOMPONENTEN LIBRARY (CLEAN VERSION)
 * 
 * Modulare, wiederverwendbare Komponenten für harmonische Audio-Analyse
 * 
 * WICHTIG: Diese Version entfernt die redundante Goertzel-Implementierung
 * und verwendet stattdessen AudioSyncLib.GoertzelAnalyzer für präzise Analyse.
 * 
 * ABHÄNGIGKEITEN:
 * - AudioSyncLib (für GoertzelAnalyzer)
 * 
 * KOMPONENTEN:
 * - MicrophoneManager: Mikrofon-Aufnahme und Audio-Verarbeitung
 * - SpectrumVisualizer: Spektrum-Darstellung mit verschiedenen Modi
 * - FrequencyGenerator: Audio-Generator mit verschiedenen Wellenformen
 * - HarmonicAnalyzer: Mathematische harmonische Analyse (ohne Goertzel)
 * - IntervalDetector: Erkennung musikalischer Intervalle
 * - AudioFilePlayer: Audio-Datei Wiedergabe und Analyse
 * 
 * @version 2.1.0
 * @author T0-Harmonic Research Team
 */

// ================================================================================================
// MIKROFON MANAGER - Komponente für Audio-Aufnahme
// ================================================================================================

class MicrophoneManager {
    constructor(options = {}) {
        this.options = {
            fftSize: options.fftSize || 2048,
            smoothingTimeConstant: options.smoothingTimeConstant || 0.8,
            sampleRate: options.sampleRate || 44100,
            sensitivity: options.sensitivity || 0.1,
            noiseThreshold: options.noiseThreshold || 0.005,
            gain: options.gain || 1.0,
            onLevelUpdate: options.onLevelUpdate || null,
            onError: options.onError || null,
            onStart: options.onStart || null,
            onStop: options.onStop || null,
            ...options
        };
        
        this.audioContext = null;
        this.micStream = null;
        this.micSource = null;
        this.analyser = null;
        this.isActive = false;
        this.levelUpdateInterval = null;
    }
    
    async start() {
        try {
            console.log('MicrophoneManager: Starting microphone...');
            
            // Request microphone access
            this.micStream = await navigator.mediaDevices.getUserMedia({
                audio: {
                    echoCancellation: false,
                    noiseSuppression: false,
                    autoGainControl: false,
                    sampleRate: this.options.sampleRate
                }
            });
            
            // Create audio context if needed
            if (!this.audioContext) {
                this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
            }
            
            if (this.audioContext.state === 'suspended') {
                await this.audioContext.resume();
            }
            
            // Create audio nodes
            this.micSource = this.audioContext.createMediaStreamSource(this.micStream);
            this.analyser = this.audioContext.createAnalyser();
            this.analyser.fftSize = this.options.fftSize;
            this.analyser.smoothingTimeConstant = this.options.smoothingTimeConstant;
            
            // Connect nodes
            this.micSource.connect(this.analyser);
            
            this.isActive = true;
            
            // Start level monitoring if callback provided
            if (this.options.onLevelUpdate) {
                this.startLevelMonitoring();
            }
            
            if (this.options.onStart) {
                this.options.onStart();
            }
            
            console.log('MicrophoneManager: Successfully started');
            return true;
            
        } catch (error) {
            console.error('MicrophoneManager: Error starting microphone:', error);
            if (this.options.onError) {
                this.options.onError(error);
            }
            return false;
        }
    }
    
    stop() {
        try {
            if (this.micStream) {
                this.micStream.getTracks().forEach(track => track.stop());
                this.micStream = null;
            }
            
            if (this.micSource) {
                this.micSource.disconnect();
                this.micSource = null;
            }
            
            if (this.levelUpdateInterval) {
                clearInterval(this.levelUpdateInterval);
                this.levelUpdateInterval = null;
            }
            
            this.analyser = null;
            this.isActive = false;
            
            if (this.options.onStop) {
                this.options.onStop();
            }
            
            console.log('MicrophoneManager: Stopped');
            
        } catch (error) {
            console.error('MicrophoneManager: Error stopping microphone:', error);
        }
    }
    
    startLevelMonitoring() {
        if (!this.analyser || this.levelUpdateInterval) return;
        
        this.levelUpdateInterval = setInterval(() => {
            if (this.analyser) {
                const level = this.getCurrentLevel();
                if (this.options.onLevelUpdate) {
                    this.options.onLevelUpdate(level);
                }
            }
        }, 50); // 20 FPS
    }
    
    getCurrentLevel() {
        if (!this.analyser) return 0;
        
        const bufferLength = this.analyser.frequencyBinCount;
        const dataArray = new Uint8Array(bufferLength);
        this.analyser.getByteFrequencyData(dataArray);
        
        let sum = 0;
        for (let i = 0; i < bufferLength; i++) {
            sum += dataArray[i] * dataArray[i];
        }
        const rms = Math.sqrt(sum / bufferLength);
        return Math.min(100, (rms / 128) * 100);
    }
    
    getTimeData() {
        if (!this.analyser) return null;
        
        const bufferLength = this.analyser.fftSize;
        const timeData = new Float32Array(bufferLength);
        this.analyser.getFloatTimeDomainData(timeData);
        
        // Apply processing
        for (let i = 0; i < bufferLength; i++) {
            let sample = timeData[i] * this.options.gain * this.options.sensitivity;
            if (Math.abs(sample) < this.options.noiseThreshold) {
                sample = 0;
            }
            timeData[i] = sample;
        }
        
        return timeData;
    }
    
    getFrequencyData() {
        if (!this.analyser) return null;
        
        const bufferLength = this.analyser.frequencyBinCount;
        const dataArray = new Uint8Array(bufferLength);
        this.analyser.getByteFrequencyData(dataArray);
        return dataArray;
    }
    
    updateSettings(newSettings) {
        Object.assign(this.options, newSettings);
        
        if (this.analyser && newSettings.fftSize) {
            this.analyser.fftSize = newSettings.fftSize;
        }
        if (this.analyser && newSettings.smoothingTimeConstant) {
            this.analyser.smoothingTimeConstant = newSettings.smoothingTimeConstant;
        }
    }
}

// ================================================================================================
// SPEKTRUM VISUALIZER - Komponente für Spektrum-Darstellung
// ================================================================================================

class SpectrumVisualizer {
    constructor(canvas, options = {}) {
        this.canvas = canvas;
        this.ctx = canvas.getContext('2d');
        this.options = {
            scale: options.scale || 'log', // 'linear', 'log', 'rational'
            colorCoding: options.colorCoding || 'ratio', // 'frequency', 'ratio', 'euler', 'deviation'
            showRatios: options.showRatios !== false,
            showOctaves: options.showOctaves !== false,
            showGrid: options.showGrid !== false,
            backgroundColor: options.backgroundColor || 'rgba(0, 0, 0, 0.9)',
            gridColor: options.gridColor || 'rgba(255, 255, 255, 0.3)',
            fundamentalColor: options.fundamentalColor || 'rgba(255, 215, 0, 0.8)',
            octaveColor: options.octaveColor || 'rgba(255, 255, 255, 0.3)',
            frequencyRange: options.frequencyRange || { min: 20, max: 4000 },
            fullSpectrum: options.fullSpectrum || false,
            hybridMode: options.hybridMode || false,
            onHarmonicHover: options.onHarmonicHover || null,
            onHarmonicLeave: options.onHarmonicLeave || null,
            ...options
        };
        
        this.harmonics = [];
        this.fundamentalFreq = 440;
        this.isHovering = false;
        
        this.setupEventListeners();
        this.resize();
    }
    
    setupEventListeners() {
        // Mouse events for harmonic info
        this.canvas.addEventListener('mousemove', (e) => this.handleMouseMove(e));
        this.canvas.addEventListener('mouseleave', () => this.handleMouseLeave());
        
        // Resize observer
        if (window.ResizeObserver) {
            this.resizeObserver = new ResizeObserver(() => this.resize());
            this.resizeObserver.observe(this.canvas.parentElement);
        } else {
            window.addEventListener('resize', () => this.resize());
        }
    }
    
    resize() {
        const container = this.canvas.parentElement;
        const rect = container.getBoundingClientRect();
        
        this.canvas.width = rect.width || 800;
        this.canvas.height = rect.height || 400;
        this.canvas.style.width = '100%';
        this.canvas.style.height = '100%';
        
        if (this.harmonics.length > 0) {
            this.render();
        }
    }
    
    updateHarmonics(harmonics, fundamentalFreq = 440) {
        this.harmonics = harmonics || [];
        this.fundamentalFreq = fundamentalFreq;
        this.render();
    }
    
    updateOptions(newOptions) {
        Object.assign(this.options, newOptions);
        this.render();
    }
    
    render() {
        const width = this.canvas.width;
        const height = this.canvas.height;
        
        // Clear canvas
        this.ctx.fillStyle = this.options.backgroundColor;
        this.ctx.fillRect(0, 0, width, height);
        
        // Draw FFT background if hybrid mode
        if (this.options.hybridMode && this.options.fftData) {
            this.drawFFTBackground();
        }
        
        // Draw grid and axis
        if (this.options.showGrid) {
            this.drawGrid();
        }
        
        // Draw fundamental frequency line
        this.drawFundamentalLine();
        
        // Draw octave markers
        if (this.options.showOctaves) {
            this.drawOctaveMarkers();
        }
        
        // Draw harmonics
        this.drawHarmonics();
        
        // Draw frequency axis
        this.drawFrequencyAxis();
        
        // Draw info overlay
        this.drawInfoOverlay();
    }
    
    drawFFTBackground() {
        if (!this.options.fftData) return;
        
        const width = this.canvas.width;
        const height = this.canvas.height;
        const sampleRate = this.options.sampleRate || 44100;
        
        for (let binIndex = 0; binIndex < this.options.fftData.length; binIndex++) {
            const freq = (binIndex * sampleRate) / (2 * this.options.fftData.length);
            const x = this.getXPosition(freq);
            
            if (x >= 0 && x < width) {
                const amplitude = this.options.fftData[binIndex] / 255;
                const barHeight = amplitude * height * 0.6;
                
                if (barHeight > 1) {
                    const hue = (freq / this.options.frequencyRange.max) * 240;
                    this.ctx.fillStyle = `hsla(${240 - hue}, 70%, 60%, 0.4)`;
                    this.ctx.fillRect(x, height - barHeight, 1, barHeight);
                }
            }
        }
    }
    
    drawGrid() {
        const width = this.canvas.width;
        const height = this.canvas.height;
        
        this.ctx.strokeStyle = this.options.gridColor;
        this.ctx.lineWidth = 1;
        this.ctx.setLineDash([2, 2]);
        
        // Horizontal lines
        for (let i = 1; i < 4; i++) {
            const y = (height * i) / 4;
            this.ctx.beginPath();
            this.ctx.moveTo(0, y);
            this.ctx.lineTo(width, y);
            this.ctx.stroke();
        }
        
        this.ctx.setLineDash([]);
    }
    
    drawFundamentalLine() {
        const x = this.getXPosition(this.fundamentalFreq);
        const width = this.canvas.width;
        const height = this.canvas.height;
        
        if (x >= 0 && x <= width) {
            this.ctx.fillStyle = this.options.fundamentalColor;
            this.ctx.fillRect(x - 2, 0, 4, height);
        }
    }
    
    drawOctaveMarkers() {
        const width = this.canvas.width;
        const height = this.canvas.height;
        const maxOctaves = this.options.fullSpectrum ? 12 : 8;
        
        for (let octave = 1; octave <= maxOctaves; octave++) {
            const octaveFreq = this.fundamentalFreq * Math.pow(2, octave);
            const x = this.getXPosition(octaveFreq);
            
            if (x > 0 && x < width) {
                this.ctx.fillStyle = this.options.octaveColor;
                this.ctx.fillRect(x - 1, 0, 2, height);
                
                if (this.options.fullSpectrum) {
                    this.ctx.fillStyle = '#ff6b35';
                    this.ctx.font = '10px Arial';
                    this.ctx.textAlign = 'center';
                    this.ctx.fillText(`Oct${octave}`, x, 15);
                }
            }
        }
    }
    
    drawHarmonics() {
        const height = this.canvas.height;
        
        this.harmonics.forEach((harmonic, index) => {
            const x = this.getXPosition(harmonic.frequency);
            const barHeight = Math.max(5, harmonic.magnitude * height * 0.8);
            
            if (x < 0 || x > this.canvas.width) return;
            
            // Get color based on coding system
            const color = this.getHarmonicColor(harmonic);
            
            // Draw bar with glow effect in hybrid mode
            if (this.options.hybridMode) {
                this.ctx.shadowColor = color;
                this.ctx.shadowBlur = 8;
                this.ctx.shadowOffsetX = 0;
                this.ctx.shadowOffsetY = 0;
            }
            
            this.ctx.fillStyle = color;
            const barWidth = this.options.fullSpectrum ? 4 : 6;
            this.ctx.fillRect(x - barWidth/2, height - barHeight, barWidth, barHeight);
            
            // Reset shadow
            if (this.options.hybridMode) {
                this.ctx.shadowBlur = 0;
                
                // White core for better contrast
                this.ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
                this.ctx.fillRect(x - 1, height - barHeight, 2, barHeight);
            }
            
            // Draw ratio labels
            if (this.options.showRatios && harmonic.rational && barHeight > 20) {
                this.ctx.fillStyle = '#ffffff';
                this.ctx.font = '9px Arial';
                this.ctx.textAlign = 'center';
                this.ctx.fillText(harmonic.rational.toString(), x, height - barHeight - 5);
            }
            
            // Draw frequency labels
            this.ctx.fillStyle = this.options.fullSpectrum ? '#ff6b35' : '#ffd700';
            this.ctx.font = '8px Arial';
            const freqLabel = harmonic.frequency >= 1000 ? 
                (harmonic.frequency/1000).toFixed(1) + 'k' : 
                harmonic.frequency.toFixed(0);
            this.ctx.fillText(freqLabel, x, height - 5);
            
            // Draw octave shift indicators in full spectrum mode
            if (this.options.fullSpectrum && harmonic.octaveShifts !== undefined && harmonic.octaveShifts !== 0) {
                this.ctx.fillStyle = '#ff6b35';
                this.ctx.font = '7px Arial';
                this.ctx.fillText(`+${harmonic.octaveShifts}`, x, height - 15);
            }
        });
    }
    
    drawFrequencyAxis() {
        const width = this.canvas.width;
        const height = this.canvas.height;
        const range = this.options.frequencyRange;
        
        this.ctx.strokeStyle = this.options.gridColor;
        this.ctx.lineWidth = 1;
        
        // Calculate frequency steps
        const freqRange = range.max - range.min;
        let step;
        
        if (freqRange <= 500) step = 50;
        else if (freqRange <= 2000) step = 200;
        else step = 500;
        
        for (let freq = Math.ceil(range.min/step)*step; freq <= range.max; freq += step) {
            const x = this.getXPosition(freq);
            
            if (x > 0 && x < width) {
                // Draw tick
                this.ctx.beginPath();
                this.ctx.moveTo(x, height - 20);
                this.ctx.lineTo(x, height);
                this.ctx.stroke();
                
                // Draw label
                this.ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
                this.ctx.font = '10px Arial';
                this.ctx.textAlign = 'center';
                
                const label = freq >= 1000 ? (freq/1000).toFixed(1) + 'k' : freq.toString();
                this.ctx.fillText(label + 'Hz', x, height - 25);
            }
        }
    }
    
    drawInfoOverlay() {
        const width = this.canvas.width;
        
        // Mode indicators
        let modeText = '';
        let modeColor = '#ffffff';
        
        if (this.options.hybridMode) {
            modeText = '🌊 HYBRID: HARMONISCHE + FFT-SPEKTRUM';
            modeColor = '#ff00ff';
        } else if (this.options.fullSpectrum) {
            modeText = '🌈 VOLLSPEKTRUM-MODUS';
            modeColor = '#ff6b35';
        } else {
            modeText = '🎯 OKTAV-NORMALISIERT';
            modeColor = '#00ff88';
        }
        
        this.ctx.fillStyle = modeColor;
        this.ctx.font = '12px Arial';
        this.ctx.textAlign = 'left';
        this.ctx.fillText(modeText, 10, 20);
        
        // Harmonic count
        if (this.harmonics.length > 0) {
            this.ctx.fillStyle = '#ffffff';
            this.ctx.font = '10px Arial';
            this.ctx.fillText(`${this.harmonics.length} Harmonische erkannt`, 10, 35);
        }
    }
    
    getXPosition(frequency) {
        const range = this.options.frequencyRange;
        const width = this.canvas.width;
        
        if (this.options.scale === 'log') {
            const logMin = Math.log10(range.min);
            const logMax = Math.log10(range.max);
            const logFreq = Math.log10(frequency);
            return ((logFreq - logMin) / (logMax - logMin)) * width;
        } else if (this.options.scale === 'rational') {
            const ratio = frequency / this.fundamentalFreq;
            const maxRatio = range.max / this.fundamentalFreq;
            return (ratio / maxRatio) * width;
        } else {
            return ((frequency - range.min) / (range.max - range.min)) * width;
        }
    }
    
    getHarmonicColor(harmonic) {
        switch (this.options.colorCoding) {
            case 'frequency':
                const hue = (harmonic.frequency / 2000) * 120 + 240;
                return `hsl(${hue}, 70%, 60%)`;
            case 'ratio':
                const ratio = harmonic.rational?.toFloat() || 1;
                const ratioHue = (ratio % 1) * 360;
                return `hsl(${ratioHue}, 80%, 60%)`;
            case 'euler':
                const eulerHue = (6 - (harmonic.eulerGradus || 6)) * 60;
                return `hsl(${eulerHue}, 90%, 60%)`;
            case 'deviation':
                const deviation = Math.abs(harmonic.harmonic - Math.round(harmonic.harmonic || 1));
                const devHue = (1 - deviation) * 120;
                return `hsl(${devHue}, 80%, 60%)`;
            default:
                return this.options.fullSpectrum ? '#ff6b35' : '#4CAF50';
        }
    }
    
    handleMouseMove(event) {
        const rect = this.canvas.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;
        
        let closestHarmonic = null;
        let minDistance = Infinity;
        
        this.harmonics.forEach(harmonic => {
            const harmonicX = this.getXPosition(harmonic.frequency);
            const distance = Math.abs(x - harmonicX);
            
            if (distance < minDistance && distance < 10) {
                minDistance = distance;
                closestHarmonic = harmonic;
            }
        });
        
        if (closestHarmonic && this.options.onHarmonicHover) {
            this.options.onHarmonicHover(closestHarmonic, event.clientX, event.clientY);
        } else if (!closestHarmonic && this.isHovering && this.options.onHarmonicLeave) {
            this.options.onHarmonicLeave();
        }
        
        this.isHovering = !!closestHarmonic;
    }
    
    handleMouseLeave() {
        if (this.isHovering && this.options.onHarmonicLeave) {
            this.options.onHarmonicLeave();
        }
        this.isHovering = false;
    }
    
    destroy() {
        if (this.resizeObserver) {
            this.resizeObserver.disconnect();
        }
        // Remove event listeners
        this.canvas.removeEventListener('mousemove', this.handleMouseMove);
        this.canvas.removeEventListener('mouseleave', this.handleMouseLeave);
    }
}

// ================================================================================================
// FREQUENCY GENERATOR - Komponente für Audio-Generierung
// ================================================================================================

class FrequencyGenerator {
    constructor(options = {}) {
        this.options = {
            volume: options.volume || 0.3,
            waveform: options.waveform || 'sine',
            frequencies: options.frequencies || [440],
            onStart: options.onStart || null,
            onStop: options.onStop || null,
            onError: options.onError || null,
            ...options
        };
        
        this.audioContext = null;
        this.oscillators = [];
        this.gainNode = null;
        this.analyser = null;
        this.isActive = false;
    }
    
    async start() {
        try {
            if (this.isActive) {
                this.stop();
            }
            
            // Create audio context if needed
            if (!this.audioContext) {
                this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
            }
            
            if (this.audioContext.state === 'suspended') {
                await this.audioContext.resume();
            }
            
            // Create gain node
            this.gainNode = this.audioContext.createGain();
            this.gainNode.gain.value = this.options.volume;
            
            // Create analyser for output monitoring
            this.analyser = this.audioContext.createAnalyser();
            this.analyser.fftSize = 2048;
            this.analyser.smoothingTimeConstant = 0.8;
            
            // Connect to destination
            this.gainNode.connect(this.analyser);
            this.gainNode.connect(this.audioContext.destination);
            
            // Create oscillators
            this.options.frequencies.forEach((freq, index) => {
                const oscillator = this.audioContext.createOscillator();
                const oscGain = this.audioContext.createGain();
                
                oscillator.type = this.options.waveform;
                oscillator.frequency.setValueAtTime(freq, this.audioContext.currentTime);
                
                const individualVolume = this.options.volume / this.options.frequencies.length;
                oscGain.gain.setValueAtTime(individualVolume, this.audioContext.currentTime);
                
                oscillator.connect(oscGain);
                oscGain.connect(this.gainNode);
                
                oscillator.start();
                this.oscillators.push(oscillator);
            });
            
            this.isActive = true;
            
            if (this.options.onStart) {
                this.options.onStart();
            }
            
            console.log(`FrequencyGenerator: Started with ${this.options.frequencies.length} frequencies`);
            return true;
            
        } catch (error) {
            console.error('FrequencyGenerator: Error starting:', error);
            if (this.options.onError) {
                this.options.onError(error);
            }
            return false;
        }
    }
    
    stop() {
        try {
            this.oscillators.forEach(osc => {
                try {
                    osc.stop();
                    osc.disconnect();
                } catch (e) {
                    // Oscillator already stopped
                }
            });
            this.oscillators = [];
            
            if (this.gainNode) {
                this.gainNode.disconnect();
                this.gainNode = null;
            }
            
            this.isActive = false;
            
            if (this.options.onStop) {
                this.options.onStop();
            }
            
            console.log('FrequencyGenerator: Stopped');
            
        } catch (error) {
            console.error('FrequencyGenerator: Error stopping:', error);
        }
    }
    
    updateFrequencies(frequencies) {
        const wasActive = this.isActive;
        if (wasActive) {
            this.stop();
        }
        
        this.options.frequencies = frequencies;
        
        if (wasActive) {
            setTimeout(() => this.start(), 100);
        }
    }
    
    updateVolume(volume) {
        this.options.volume = volume;
        if (this.gainNode) {
            this.gainNode.gain.setValueAtTime(volume, this.audioContext.currentTime);
        }
    }
    
    updateWaveform(waveform) {
        this.options.waveform = waveform;
        if (this.isActive) {
            this.stop();
            setTimeout(() => this.start(), 100);
        }
    }
    
    getAnalyser() {
        return this.analyser;
    }
    
    getTimeData() {
        if (!this.analyser) return null;
        
        const bufferLength = this.analyser.fftSize;
        const timeData = new Float32Array(bufferLength);
        this.analyser.getFloatTimeDomainData(timeData);
        return timeData;
    }
    
    getFrequencyData() {
        if (!this.analyser) return null;
        
        const bufferLength = this.analyser.frequencyBinCount;
        const dataArray = new Uint8Array(bufferLength);
        this.analyser.getByteFrequencyData(dataArray);
        return dataArray;
    }
}

// ================================================================================================
// HARMONIC ANALYZER - Mathematische Analyse-Komponente (OHNE GOERTZEL)
// ================================================================================================

class HarmonicAnalyzer {
    constructor(options = {}) {
        this.options = {
            fundamentalFreq: options.fundamentalFreq || 440,
            harmonicRange: options.harmonicRange || 32,
            xiTolerance: options.xiTolerance || 50,
            rationalLimit: options.rationalLimit || 100,
            eulerLimit: options.eulerLimit || 6,
            fullSpectrum: options.fullSpectrum || false,
            ...options
        };
        
        this.detectedHarmonics = [];
        this.intervals = [];
        this.rationalCache = new Map();
        
        // WICHTIG: Prüfe auf AudioSyncLib Verfügbarkeit
        if (typeof AudioSyncLib === 'undefined') {
            console.warn('HarmonicAnalyzer: AudioSyncLib nicht gefunden! Laden Sie audio_sync_library.js vor dieser Bibliothek.');
        }
    }
    
    // Rational Number class (simplified version)
    approximateRational(decimal, maxDenominator = 1000) {
        const cacheKey = `${decimal.toFixed(6)}_${maxDenominator}`;
        if (this.rationalCache.has(cacheKey)) {
            return this.rationalCache.get(cacheKey);
        }

        if (decimal === 0) {
            const result = { numerator: 0, denominator: 1, toFloat: () => 0, toString: () => '0' };
            this.rationalCache.set(cacheKey, result);
            return result;
        }
        
        let sign = decimal < 0 ? -1 : 1;
        decimal = Math.abs(decimal);
        
        let wholePart = Math.floor(decimal);
        let fractionalPart = decimal - wholePart;
        
        if (fractionalPart === 0) {
            const result = {
                numerator: sign * wholePart,
                denominator: 1,
                toFloat: function() { return this.numerator / this.denominator; },
                toString: function() { return this.denominator === 1 ? this.numerator.toString() : `${this.numerator}/${this.denominator}`; }
            };
            this.rationalCache.set(cacheKey, result);
            return result;
        }
        
        // Continued fractions
        let h1 = 1, k1 = 0;
        let h0 = wholePart, k0 = 1;
        
        let x = fractionalPart;
        let iterations = 0;
        while (k0 <= maxDenominator && x !== 0 && iterations < 50) {
            let a = Math.floor(1 / x);
            let h2 = a * h0 + h1;
            let k2 = a * k0 + k1;
            
            if (k2 > maxDenominator) break;
            
            h1 = h0; k1 = k0;
            h0 = h2; k0 = k2;
            
            x = 1 / x - a;
            if (Math.abs(x) < 1e-10) break;
            iterations++;
        }
        
        const result = {
            numerator: sign * h0,
            denominator: k0,
            toFloat: function() { return this.numerator / this.denominator; },
            toString: function() { return this.denominator === 1 ? this.numerator.toString() : `${this.numerator}/${this.denominator}`; }
        };
        this.rationalCache.set(cacheKey, result);
        return result;
    }
    
    calculateEulerGradus(rational) {
        const factors = (n) => {
            let count = 0;
            let factor = 2;
            let temp = Math.abs(n);
            
            while (factor * factor <= temp) {
                while (temp % factor === 0) {
                    count++;
                    temp = temp / factor;
                }
                factor++;
            }
            
            if (temp > 1) count++;
            return count;
        };
        
        return factors(rational.numerator) + factors(rational.denominator) + 1;
    }
    
    /**
     * ENTFERNT: goertzelDetection() Methode
     * 
     * Diese Methode wurde entfernt, um Duplikation mit AudioSyncLib.GoertzelAnalyzer zu vermeiden.
     * Verwenden Sie stattdessen:
     * 
     * const goertzelAnalyzer = new AudioSyncLib.GoertzelAnalyzer(sampleRate, windowSize);
     * const result = goertzelAnalyzer.analyzeFrequency(audioData, targetFreq);
     */
    
    analyzeHarmonics(audioData, sampleRate, goertzelAnalyzer = null) {
        // Prüfe auf externen Goertzel Analyzer
        if (!goertzelAnalyzer && typeof AudioSyncLib !== 'undefined') {
            console.log('HarmonicAnalyzer: Verwende AudioSyncLib.GoertzelAnalyzer für präzise Analyse');
            goertzelAnalyzer = new AudioSyncLib.GoertzelAnalyzer(sampleRate, audioData.length);
        }
        
        if (!goertzelAnalyzer) {
            console.warn('HarmonicAnalyzer: Kein Goertzel Analyzer verfügbar! Lade AudioSyncLib oder übergebe einen externen Analyzer.');
            return [];
        }
        
        this.detectedHarmonics = [];
        
        // Verwende den externen GoertzelAnalyzer
        const harmonics = goertzelAnalyzer.analyzeHarmonics(audioData, this.options.fundamentalFreq, this.options.harmonicRange);
        
        // Erweitere die Ergebnisse um Rational- und Euler-Analyse
        this.detectedHarmonics = harmonics.filter(h => h.magnitude > 0.01).map(h => {
            const rational = this.approximateRational(h.harmonic, this.options.rationalLimit);
            const eulerGradus = this.calculateEulerGradus(rational);
            
            return {
                ...h,
                rational: rational,
                eulerGradus: eulerGradus,
                source: 'audiosynclib-enhanced'
            };
        }).filter(h => h.eulerGradus <= this.options.eulerLimit);
        
        this.detectIntervals();
        return this.detectedHarmonics;
    }
    
    detectIntervals() {
        this.intervals = [];
        
        for (let i = 0; i < this.detectedHarmonics.length; i++) {
            for (let j = i + 1; j < this.detectedHarmonics.length; j++) {
                const h1 = this.detectedHarmonics[i];
                const h2 = this.detectedHarmonics[j];
                
                const ratio = h2.frequency / h1.frequency;
                const rationalRatio = this.approximateRational(ratio, this.options.rationalLimit);
                
                const cents = Math.abs(1200 * Math.log2(ratio / rationalRatio.toFloat()));
                
                if (cents <= this.options.xiTolerance) {
                    this.intervals.push({
                        freq1: h1.frequency,
                        freq2: h2.frequency,
                        ratio: ratio,
                        rational: rationalRatio,
                        cents: cents,
                        name: this.getIntervalName(rationalRatio)
                    });
                }
            }
        }
    }
    
    getIntervalName(rational) {
        const intervalNames = {
            '1/1': 'Unison',
            '2/1': 'Oktave',
            '3/2': 'Quinte',
            '4/3': 'Quarte',
            '5/4': 'Große Terz',
            '6/5': 'Kleine Terz',
            '9/8': 'Ganzton',
            '16/15': 'Halbton',
            '5/3': 'Große Sexte',
            '8/5': 'Kleine Sexte',
            '15/8': 'Große Septime',
            '16/9': 'Kleine Septime'
        };
        
        return intervalNames[rational.toString()] || `${rational.toString()} (${rational.toFloat().toFixed(3)})`;
    }
    
    updateOptions(newOptions) {
        Object.assign(this.options, newOptions);
    }
}

// ================================================================================================
// AUDIO FILE PLAYER - Komponente für Datei-Wiedergabe
// ================================================================================================

class AudioFilePlayer {
    constructor(options = {}) {
        this.options = {
            volume: options.volume || 0.5,
            onLoad: options.onLoad || null,
            onPlay: options.onPlay || null,
            onStop: options.onStop || null,
            onError: options.onError || null,
            ...options
        };
        
        this.audioContext = null;
        this.audioBuffer = null;
        this.audioSource = null;
        this.gainNode = null;
        this.analyser = null;
        this.isPlaying = false;
        this.fileInfo = null;
    }
    
    async loadFile(file) {
        try {
            if (!this.audioContext) {
                this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
            }
            
            const arrayBuffer = await file.arrayBuffer();
            this.audioBuffer = await this.audioContext.decodeAudioData(arrayBuffer);
            
            this.fileInfo = {
                name: file.name,
                duration: this.audioBuffer.duration,
                sampleRate: this.audioBuffer.sampleRate,
                channels: this.audioBuffer.numberOfChannels,
                size: file.size
            };
            
            if (this.options.onLoad) {
                this.options.onLoad(this.fileInfo);
            }
            
            console.log('AudioFilePlayer: File loaded successfully');
            return true;
            
        } catch (error) {
            console.error('AudioFilePlayer: Error loading file:', error);
            if (this.options.onError) {
                this.options.onError(error);
            }
            return false;
        }
    }
    
    async play() {
        if (!this.audioBuffer) {
            console.warn('AudioFilePlayer: No audio buffer loaded');
            return false;
        }
        
        try {
            this.stop(); // Stop any current playback
            
            if (this.audioContext.state === 'suspended') {
                await this.audioContext.resume();
            }
            
            this.audioSource = this.audioContext.createBufferSource();
            this.audioSource.buffer = this.audioBuffer;
            
            this.gainNode = this.audioContext.createGain();
            this.gainNode.gain.value = this.options.volume;
            
            this.analyser = this.audioContext.createAnalyser();
            this.analyser.fftSize = 2048;
            this.analyser.smoothingTimeConstant = 0.8;
            
            this.audioSource.connect(this.gainNode);
            this.gainNode.connect(this.analyser);
            this.gainNode.connect(this.audioContext.destination);
            
            this.audioSource.onended = () => {
                this.stop();
            };
            
            this.audioSource.start();
            this.isPlaying = true;
            
            if (this.options.onPlay) {
                this.options.onPlay();
            }
            
            console.log('AudioFilePlayer: Playback started');
            return true;
            
        } catch (error) {
            console.error('AudioFilePlayer: Error playing file:', error);
            if (this.options.onError) {
                this.options.onError(error);
            }
            return false;
        }
    }
    
    stop() {
        try {
            if (this.audioSource) {
                this.audioSource.stop();
                this.audioSource.disconnect();
                this.audioSource = null;
            }
            
            if (this.gainNode) {
                this.gainNode.disconnect();
                this.gainNode = null;
            }
            
            this.analyser = null;
            this.isPlaying = false;
            
            if (this.options.onStop) {
                this.options.onStop();
            }
            
            console.log('AudioFilePlayer: Playback stopped');
            
        } catch (error) {
            console.error('AudioFilePlayer: Error stopping playback:', error);
        }
    }
    
    updateVolume(volume) {
        this.options.volume = volume;
        if (this.gainNode) {
            this.gainNode.gain.setValueAtTime(volume, this.audioContext.currentTime);
        }
    }
    
    getAnalyser() {
        return this.analyser;
    }
    
    getTimeData() {
        if (!this.analyser) return null;
        
        const bufferLength = this.analyser.fftSize;
        const timeData = new Float32Array(bufferLength);
        this.analyser.getFloatTimeDomainData(timeData);
        return timeData;
    }
    
    getFrequencyData() {
        if (!this.analyser) return null;
        
        const bufferLength = this.analyser.frequencyBinCount;
        const dataArray = new Uint8Array(bufferLength);
        this.analyser.getByteFrequencyData(dataArray);
        return dataArray;
    }
    
    getFileInfo() {
        return this.fileInfo;
    }
}

// ================================================================================================
// VOLLSTÄNDIGES ANWENDUNGSBEISPIEL MIT AUDIOSYNCLIB INTEGRATION
// ================================================================================================

/**
 * VERWENDUNGSBEISPIEL MIT AUDIOSYNCLIB:
 * 
 * // HTML Setup
 * <script src="audio_sync_library.js"></script>
 * <script src="harmonic_components_library_clean.js"></script>
 * 
 * <canvas id="spectrum-canvas" width="800" height="400"></canvas>
 * <div id="harmonic-info"></div>
 * <input type="file" id="file-input" accept="audio/*">
 * 
 * // JavaScript Initialisierung
 * 
 * class IntegratedAnalyzer {
 *     constructor() {
 *         this.syncContext = null;
 *         this.goertzelAnalyzer = null;
 *         this.harmonicAnalyzer = null;
 *         this.microphone = null;
 *         this.visualizer = null;
 *     }
 * 
 *     async initialize() {
 *         // AudioSyncLib - Synchronisation
 *         this.syncContext = new AudioSyncLib.SynchronizedAudioContext();
 *         await this.syncContext.initialize();
 * 
 *         // AudioSyncLib - Goertzel Analyzer
 *         this.goertzelAnalyzer = new AudioSyncLib.GoertzelAnalyzer(
 *             this.syncContext.sampleRate, 
 *             this.syncContext.fftSize
 *         );
 * 
 *         // HarmonicComponents - Visualizer
 *         const canvas = document.getElementById('spectrum-canvas');
 *         this.visualizer = new HarmonicComponents.SpectrumVisualizer(canvas, {
 *             scale: 'log',
 *             colorCoding: 'ratio',
 *             hybridMode: true
 *         });
 * 
 *         // HarmonicComponents - Harmonic Analyzer (ohne Goertzel)
 *         this.harmonicAnalyzer = new HarmonicComponents.HarmonicAnalyzer({
 *             fundamentalFreq: 440,
 *             harmonicRange: 32
 *         });
 * 
 *         // HarmonicComponents - Microphone
 *         this.microphone = new HarmonicComponents.MicrophoneManager({
 *             fftSize: this.syncContext.fftSize
 *         });
 * 
 *         // Synchronisierte Analyse
 *         this.syncContext.addCallback(() => this.analyze());
 *     }
 * 
 *     async start() {
 *         await this.microphone.start();
 *         this.syncContext.startSynchronizedLoop();
 *     }
 * 
 *     analyze() {
 *         const timeData = this.microphone.getTimeData();
 *         const frequencyData = this.microphone.getFrequencyData();
 * 
 *         if (timeData) {
 *             // AudioSyncLib: Präzise Goertzel-Analyse
 *             const harmonics = this.goertzelAnalyzer.analyzeHarmonics(timeData, 440, 16);
 * 
 *             // HarmonicComponents: Erweiterte Analyse (nutzt externen Goertzel)
 *             const enhancedHarmonics = this.harmonicAnalyzer.analyzeHarmonics(
 *                 timeData, 
 *                 this.syncContext.sampleRate, 
 *                 this.goertzelAnalyzer
 *             );
 * 
 *             // HarmonicComponents: Visualisierung
 *             this.visualizer.updateHarmonics(enhancedHarmonics, 440);
 *             this.visualizer.updateOptions({ 
 *                 fftData: frequencyData,
 *                 sampleRate: this.syncContext.sampleRate
 *             });
 *         }
 *     }
 * }
 * 
 * // Verwendung
 * const analyzer = new IntegratedAnalyzer();
 * await analyzer.initialize();
 * await analyzer.start();
 */

// ================================================================================================
// INTERVAL DETECTOR - Komponente für Intervall-Erkennung
// ================================================================================================

class IntervalDetector {
    constructor(options = {}) {
        this.options = {
            toleranceCents: options.toleranceCents || 50,
            minMagnitude: options.minMagnitude || 0.01,
            onIntervalDetected: options.onIntervalDetected || null,
            onIntervalLost: options.onIntervalLost || null,
            ...options
        };
        
        this.detectedIntervals = [];
        this.lastIntervals = [];
        this.intervalHistory = [];
        this.maxHistoryLength = 10;
    }
    
    analyzeIntervals(harmonics) {
        this.detectedIntervals = [];
        
        // Alle möglichen Intervall-Kombinationen prüfen
        for (let i = 0; i < harmonics.length; i++) {
            for (let j = i + 1; j < harmonics.length; j++) {
                const h1 = harmonics[i];
                const h2 = harmonics[j];
                
                if (h1.magnitude < this.options.minMagnitude || h2.magnitude < this.options.minMagnitude) {
                    continue;
                }
                
                const interval = this.calculateInterval(h1, h2);
                if (interval && interval.cents <= this.options.toleranceCents) {
                    this.detectedIntervals.push(interval);
                }
            }
        }
        
        // Intervall-Änderungen erkennen
        this.detectIntervalChanges();
        
        // History aktualisieren
        this.updateHistory();
        
        return this.detectedIntervals;
    }
    
    calculateInterval(harmonic1, harmonic2) {
        const freq1 = harmonic1.frequency;
        const freq2 = harmonic2.frequency;
        
        const ratio = freq2 / freq1;
        const cents = 1200 * Math.log2(ratio);
        
        // Bekannte Intervalle
        const knownIntervals = [
            { name: 'Unison', ratio: 1, cents: 0 },
            { name: 'Halbton', ratio: 16/15, cents: 112 },
            { name: 'Ganzton', ratio: 9/8, cents: 204 },
            { name: 'Kleine Terz', ratio: 6/5, cents: 316 },
            { name: 'Große Terz', ratio: 5/4, cents: 386 },
            { name: 'Quarte', ratio: 4/3, cents: 498 },
            { name: 'Tritonus', ratio: Math.sqrt(2), cents: 600 },
            { name: 'Quinte', ratio: 3/2, cents: 702 },
            { name: 'Kleine Sexte', ratio: 8/5, cents: 814 },
            { name: 'Große Sexte', ratio: 5/3, cents: 884 },
            { name: 'Kleine Septime', ratio: 16/9, cents: 996 },
            { name: 'Große Septime', ratio: 15/8, cents: 1088 },
            { name: 'Oktave', ratio: 2, cents: 1200 }
        ];
        
        // Nächstes bekanntes Intervall finden
        let closestInterval = null;
        let minDeviation = Infinity;
        
        for (const interval of knownIntervals) {
            const deviation = Math.abs(cents - interval.cents);
            if (deviation < minDeviation) {
                minDeviation = deviation;
                closestInterval = interval;
            }
        }
        
        if (closestInterval && minDeviation <= this.options.toleranceCents) {
            return {
                name: closestInterval.name,
                freq1: freq1,
                freq2: freq2,
                ratio: ratio,
                expectedRatio: closestInterval.ratio,
                cents: cents,
                expectedCents: closestInterval.cents,
                deviation: minDeviation,
                magnitude: Math.min(harmonic1.magnitude, harmonic2.magnitude),
                stability: this.calculateStability(freq1, freq2)
            };
        }
        
        return null;
    }
    
    calculateStability(freq1, freq2) {
        // Einfache Stabilität basierend auf rationalen Verhältnissen
        const ratio = freq2 / freq1;
        
        // Suche nach kleinen ganzzahligen Verhältnissen
        for (let denom = 1; denom <= 16; denom++) {
            for (let num = denom; num <= denom * 2; num++) {
                const testRatio = num / denom;
                const error = Math.abs(ratio - testRatio) / testRatio;
                
                if (error < 0.01) { // 1% Toleranz
                    const complexity = num + denom;
                    return Math.max(0, 100 - complexity * 5); // Höhere Zahlen = niedrigere Stabilität
                }
            }
        }
        
        return 0; // Kein einfaches Verhältnis gefunden
    }
    
    detectIntervalChanges() {
        const currentNames = this.detectedIntervals.map(i => i.name);
        const lastNames = this.lastIntervals.map(i => i.name);
        
        // Neue Intervalle
        const newIntervals = this.detectedIntervals.filter(i => !lastNames.includes(i.name));
        if (newIntervals.length > 0 && this.options.onIntervalDetected) {
            newIntervals.forEach(interval => this.options.onIntervalDetected(interval));
        }
        
        // Verlorene Intervalle
        const lostIntervals = this.lastIntervals.filter(i => !currentNames.includes(i.name));
        if (lostIntervals.length > 0 && this.options.onIntervalLost) {
            lostIntervals.forEach(interval => this.options.onIntervalLost(interval));
        }
        
        this.lastIntervals = [...this.detectedIntervals];
    }
    
    updateHistory() {
        this.intervalHistory.push({
            timestamp: Date.now(),
            intervals: [...this.detectedIntervals]
        });
        
        if (this.intervalHistory.length > this.maxHistoryLength) {
            this.intervalHistory.shift();
        }
    }
    
    getStableIntervals(minOccurrences = 3) {
        const intervalCounts = new Map();
        
        this.intervalHistory.forEach(entry => {
            entry.intervals.forEach(interval => {
                const key = interval.name;
                intervalCounts.set(key, (intervalCounts.get(key) || 0) + 1);
            });
        });
        
        return Array.from(intervalCounts.entries())
            .filter(([name, count]) => count >= minOccurrences)
            .map(([name, count]) => ({ name, occurrences: count }));
    }
    
    getIntervalStatistics() {
        const allIntervals = this.intervalHistory.flatMap(entry => entry.intervals);
        
        if (allIntervals.length === 0) {
            return { count: 0, stability: 0, mostCommon: null };
        }
        
        // Häufigstes Intervall
        const intervalCounts = new Map();
        allIntervals.forEach(interval => {
            intervalCounts.set(interval.name, (intervalCounts.get(interval.name) || 0) + 1);
        });
        
        const mostCommon = Array.from(intervalCounts.entries())
            .sort(([,a], [,b]) => b - a)[0];
        
        // Durchschnittliche Stabilität
        const avgStability = allIntervals.reduce((sum, i) => sum + i.stability, 0) / allIntervals.length;
        
        return {
            count: allIntervals.length,
            stability: avgStability,
            mostCommon: mostCommon ? { name: mostCommon[0], count: mostCommon[1] } : null,
            uniqueIntervals: intervalCounts.size
        };
    }
    
    reset() {
        this.detectedIntervals = [];
        this.lastIntervals = [];
        this.intervalHistory = [];
    }
}

// ================================================================================================
// EXPORT UND BROWSER GLOBALS
// ================================================================================================

// Export für Module
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        MicrophoneManager,
        SpectrumVisualizer,
        FrequencyGenerator,
        HarmonicAnalyzer,
        AudioFilePlayer,
        IntervalDetector
    };
} else if (typeof window !== 'undefined') {
    // Browser globals
    window.HarmonicComponents = {
        MicrophoneManager,
        SpectrumVisualizer,
        FrequencyGenerator,
        HarmonicAnalyzer,
        AudioFilePlayer,
        IntervalDetector
    };
    
    // Kompatibilitätsprüfung
    if (typeof AudioSyncLib === 'undefined') {
        console.warn('🔄 HarmonicComponents: AudioSyncLib nicht gefunden!');
        console.log('📦 Bitte laden Sie audio_sync_library.js vor harmonic_components_library.js');
        console.log('💡 Für optimale Ergebnisse verwenden Sie beide Bibliotheken zusammen.');
    } else {
        console.log('✅ HarmonicComponents: AudioSyncLib Integration erkannt');
        console.log('🎵 Beide Bibliotheken sind bereit für harmonische Analyse');
    }
} 