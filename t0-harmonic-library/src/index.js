/**
 * T0 Harmonic Library - Main Export (Optimiert mit 19/16 Moll)
 * Author: Johann Pascher
 * Part of T0-Time-Mass-Duality Research
 */

export class T0AudioSystemComplete {
    constructor(config = {}) {
        this.version = '2.0.1';
        this.author = 'Johann Pascher';
        this.project = 'T0-Time-Mass-Duality';
        
        this.config = {
            maxHarmonic: 3,
            tolerance: 3.0,
            volume: 0.5,
            debugMode: false,
            baseFrequency: 261.63, // C4 als Referenz
            ...config
        };
        
        this.state = {
            isInitialized: false,
            currentChord: null,
            analysisResults: null
        };
        
        console.log('T0 Audio System v' + this.version + ' by ' + this.author + ' (Optimiert: 19/16 Moll)');
        this.initialize();
    }
    
    async initialize() {
        try {
            this.state.isInitialized = true;
            console.log('✅ T0 System initialized successfully (optimized ratio-based calculations)');
            return true;
        } catch (error) {
            console.error('❌ T0 System initialization failed:', error);
            return false;
        }
    }
    
    async analyzeChord(chordName, baseFrequency = null) {
        if (!this.state.isInitialized) {
            throw new Error('System not initialized');
        }
        
        const freq = baseFrequency || this.config.baseFrequency;
        console.log('🎵 Analyzing chord: ' + chordName + ' at ' + freq + ' Hz base');
        
        this.state.currentChord = chordName;
        this.state.analysisResults = {
            chord: chordName,
            success: true,
            timestamp: new Date().toISOString(),
            baseFrequency: freq,
            ratios: this.getRatiosForChord(chordName),
            frequencies: this.getFrequenciesForChord(chordName, freq),
            intervals: this.getIntervalsForChord(chordName),
            tuningSystem: this.getTuningSystemInfo(chordName)
        };
        
        return this.state.analysisResults;
    }
    
    // Optimierte verhältnisbasierte Akkord-Definition
    getRatiosForChord(chordName) {
        const chordRatios = {
            // Dur-Akkorde (Reine Stimmung - unverändert)
            'C-Major': [1.0, 5/4, 3/2],           // 1:1.25:1.5 (C-E-G)
            'F-Major': [1.0, 5/4, 3/2],           
            'G-Major': [1.0, 5/4, 3/2],           
            'A-Major': [1.0, 5/4, 3/2],           
            'D-Major': [1.0, 5/4, 3/2],           
            'E-Major': [1.0, 5/4, 3/2],           
            'B-Major': [1.0, 5/4, 3/2],
            'Bb-Major': [1.0, 5/4, 3/2],
            
            // Moll-Akkorde (Optimiert mit 19/16 - nur 2.5 Cent von temperiert!)
            'C-Minor': [1.0, 19/16, 3/2],         // 1:1.1875:1.5 (optimiert)
            'F-Minor': [1.0, 19/16, 3/2],         
            'G-Minor': [1.0, 19/16, 3/2],         
            'A-Minor': [1.0, 19/16, 3/2],         
            'D-Minor': [1.0, 19/16, 3/2],
            'E-Minor': [1.0, 19/16, 3/2],
            'B-Minor': [1.0, 19/16, 3/2],
            
            // Septakkorde
            'C-Dom7': [1.0, 5/4, 3/2, 7/4],       // 1:1.25:1.5:1.75
            'G-Dom7': [1.0, 5/4, 3/2, 7/4],       
            'F-Dom7': [1.0, 5/4, 3/2, 7/4],       
            'C-Min7': [1.0, 19/16, 3/2, 7/4],     // Moll-Septakkord optimiert
            'A-Min7': [1.0, 19/16, 3/2, 7/4],
            'D-Min7': [1.0, 19/16, 3/2, 7/4],
            
            // Spezielle Akkorde
            'C-Sus2': [1.0, 9/8, 3/2],            // 1:1.125:1.5 (C-D-G)
            'C-Sus4': [1.0, 4/3, 3/2],            // 1:1.333:1.5 (C-F-G)
            'C-Dim': [1.0, 19/16, 7/6],           // Vermindert mit optimierter Terz
            'C-Aug': [1.0, 5/4, 8/5],             // 1:1.25:1.6 (übermäßig)
            
            // Erweiterte Akkorde
            'C-Add9': [1.0, 5/4, 3/2, 9/4],       // Mit None
            'C-Maj7': [1.0, 5/4, 3/2, 15/8],      // Mit großer Septime
            'C-MinAdd9': [1.0, 19/16, 3/2, 9/4]   // Moll mit None (optimiert)
        };
        
        return chordRatios[chordName] || [1.0];
    }
    
    // Erweiterte Intervall-Erkennung
    getIntervalsForChord(chordName) {
        const chordIntervals = {
            'C-Major': ['Prim', 'Große Terz (rein)', 'Quinte'],
            'C-Minor': ['Prim', 'Kleine Terz (optimiert)', 'Quinte'],
            'C-Dom7': ['Prim', 'Große Terz (rein)', 'Quinte', 'Kleine Septime'],
            'C-Min7': ['Prim', 'Kleine Terz (optimiert)', 'Quinte', 'Kleine Septime'],
            'C-Sus2': ['Prim', 'Sekunde', 'Quinte'],
            'C-Sus4': ['Prim', 'Quarte', 'Quinte'],
            'C-Dim': ['Prim', 'Kleine Terz (optimiert)', 'Verminderte Quinte'],
            'C-Aug': ['Prim', 'Große Terz (rein)', 'Übermäßige Quinte']
        };
        
        return chordIntervals[chordName] || ['Prim'];
    }
    
    // Neue Funktion: Stimmungssystem-Info
    getTuningSystemInfo(chordName) {
        if (chordName.includes('Minor') || chordName.includes('Min') || chordName.includes('Dim')) {
            return {
                system: 'Optimiert (19/16)',
                description: 'Kleine Terz nur 2.5 Cent von temperiert',
                centDeviation: -2.5,
                advantage: 'Praktisch identisch mit 12-TET, aber ganzzahliges Verhältnis'
            };
        } else {
            return {
                system: 'Reine Stimmung (5/4)',
                description: 'Große Terz in reiner Stimmung',
                centDeviation: -13.7,
                advantage: 'Harmonisch rein, weniger Schwebungen'
            };
        }
    }
    
    // Berechne absolute Frequenzen aus Verhältnissen
    getFrequenciesForChord(chordName, baseFrequency = null) {
        const freq = baseFrequency || this.config.baseFrequency;
        const ratios = this.getRatiosForChord(chordName);
        
        return ratios.map(ratio => {
            const frequency = freq * ratio;
            return Math.round(frequency * 100) / 100;
        });
    }
    
    // Transponiere Akkord zu beliebiger Grundfrequenz
    transposeChord(chordName, targetFrequency) {
        return this.getFrequenciesForChord(chordName, targetFrequency);
    }
    
    // Erweiterte Intervall-Analyse
    analyzeInterval(freq1, freq2) {
        const ratio = freq2 / freq1;
        const cents = Math.round(1200 * Math.log2(ratio));
        
        let intervalName = 'Unbekannt';
        let tuningType = '';
        
        if (Math.abs(ratio - 1.0) < 0.01) {
            intervalName = 'Prim';
        } else if (Math.abs(ratio - 9/8) < 0.01) {
            intervalName = 'Große Sekunde';
        } else if (Math.abs(ratio - 19/16) < 0.01) {
            intervalName = 'Kleine Terz (optimiert)';
            tuningType = ' - nur 2.5 Cent von temperiert!';
        } else if (Math.abs(ratio - 6/5) < 0.01) {
            intervalName = 'Kleine Terz (rein)';
            tuningType = ' - 15.6 Cent von temperiert';
        } else if (Math.abs(ratio - 5/4) < 0.01) {
            intervalName = 'Große Terz (rein)';
            tuningType = ' - 13.7 Cent von temperiert';
        } else if (Math.abs(ratio - 4/3) < 0.01) {
            intervalName = 'Quarte';
        } else if (Math.abs(ratio - 3/2) < 0.01) {
            intervalName = 'Quinte';
        } else if (Math.abs(ratio - 2.0) < 0.01) {
            intervalName = 'Oktave';
        }
        
        return {
            ratio: ratio,
            cents: cents,
            intervalName: intervalName + tuningType
        };
    }
    
    // Vergleiche verschiedene Stimmungssysteme
    compareToTuning(chordName, tuningSystem = '12-tet') {
        const ourRatios = this.getRatiosForChord(chordName);
        
        let comparisonRatios;
        if (tuningSystem === '12-tet') {
            // 12-TET Verhältnisse
            if (chordName.includes('Major')) {
                comparisonRatios = [1.0, Math.pow(2, 4/12), Math.pow(2, 7/12)];
            } else if (chordName.includes('Minor')) {
                comparisonRatios = [1.0, Math.pow(2, 3/12), Math.pow(2, 7/12)];
            }
        }
        
        if (!comparisonRatios) return null;
        
        const comparison = ourRatios.map((ratio, i) => {
            const cents = 1200 * Math.log2(ratio / comparisonRatios[i]);
            return {
                interval: i,
                ourRatio: ratio,
                comparisonRatio: comparisonRatios[i],
                centDifference: Math.round(cents * 10) / 10
            };
        });
        
        return comparison;
    }
    
    getSystemInfo() {
        return {
            version: this.version,
            author: this.author,
            project: this.project,
            calculationType: 'Optimiert: Dur rein (5/4), Moll nah-temperiert (19/16)',
            isInitialized: this.state.isInitialized,
            currentChord: this.state.currentChord,
            baseFrequency: this.config.baseFrequency,
            lastAnalysis: this.state.analysisResults,
            tuningAdvantages: [
                'Dur-Akkorde: Harmonisch rein (5/4, 3/2)',
                'Moll-Akkorde: Nur 2.5 Cent von temperiert (19/16)',
                'Beste Balance: Reinheit + Kompatibilität'
            ]
        };
    }
    
    // Referenz zu bestehenden Komponenten (erhalten)
    getExistingComponents() {
        return {
            harmonicAnalyzer: 'src/t0-harmonic-analyzer.js (71,927 bytes) - ERHALTEN',
            componentLibrary: 'src/harmonic-components-library.js (51,904 bytes) - ERHALTEN', 
            fileLoader: 'src/t0-file-loader.js (34,408 bytes) - ERHALTEN',
            bufferSystem: 'src/t0-harmonic-buffer.js (71,289 bytes) - ERHALTEN',
            status: 'Preserved for future integration',
            note: 'Zusätzliche Algorithmen sind gesichert und können später integriert werden'
        };
    }
}

// Export für verschiedene Module-Systeme
export default T0AudioSystemComplete;

// Browser Global
if (typeof window !== 'undefined') {
    window.T0AudioSystem = { T0AudioSystemComplete };
}
