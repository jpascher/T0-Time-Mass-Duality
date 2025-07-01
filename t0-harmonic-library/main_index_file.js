// T0 Harmonic Library v2.0.2 - Implementierungs-differenzierte Architektur
// Autor: Johann Pascher - T0-Time-Mass-Duality Research

/**
 * T0 HARMONIC LIBRARY - HAUPTEINSTIEGSPUNKT
 * 
 * Diese Library bietet implementierungs-differenzierte T0-Harmonik-Analyse:
 * 
 * ✅ MATHEMATISCH: 100% zuverlässig, sofort verfügbar
 * 🔄 HARDWARE: Analog-Integration geplant (Q2-Q3 2025) 
 * ⚠️ BROWSER-AUDIO: Nur Bildung (85% Phantom-Rate)
 */

// =============================================================================
// IMPLEMENTIERUNGS-KLASSEN EXPORTS
// =============================================================================

// ✅ MATHEMATISCHE IMPLEMENTATION (Primär empfohlen)
export { 
    MathematicalHarmonicAnalyzer,
    FrequencyGenerator,
    ExactRatioCalculator 
} from './mathematical/index.js';

// 🔄 HARDWARE-INTERFACE (In Entwicklung)
export { 
    AnalogHardwareInterface,
    PLLMeasurement,
    HardwareValidation 
} from './hardware/index.js';

// ⚠️ EDUCATIONAL BROWSER-AUDIO (Nur Demonstration)
export { 
    BrowserAudioAnalyzer,
    DSPLimitationDemo,
    PhantomFrequencyDemo 
} from './educational/index.js';

// 🧮 CORE UTILITIES (Alle Implementierungen)
export { 
    T0Mathematics,
    RationalArithmetic,
    ValidationCertificate 
} from './core/index.js';

// 🏭 FACTORY & UTILITIES
export { 
    T0HarmonicLibraryFactory,
    ImplementationRecommender,
    CompatibilityChecker 
} from './factory/index.js';

// =============================================================================
// CONVENIENCE API für häufige Anwendungen
// =============================================================================

/**
 * EMPFOHLENE EINGANGS-API für neue Benutzer
 * Automatische Auswahl der besten verfügbaren Implementation
 */
export class T0HarmonicLibrary {
    constructor(options = {}) {
        const { 
            implementationType = "auto",
            showWarnings = true,
            educationalMode = false 
        } = options;
        
        this.showWarnings = showWarnings;
        this.educationalMode = educationalMode;
        
        // Implementation-Selection Logic
        this.analyzer = this._selectImplementation(implementationType);
        
        if (showWarnings) {
            this._showImplementationWarnings();
        }
    }
    
    _selectImplementation(type) {
        if (type === "auto") {
            // Standard: Mathematische Implementation (100% zuverlässig)
            if (this.showWarnings) {
                console.log(`
🎯 AUTO-SELECTION: Mathematische Implementation gewählt

✅ GRUND: 100% Zuverlässigkeit, sofort verfügbar
✅ GEEIGNET FÜR: Komposition, Theorie, Bildung
ℹ️ HINWEIS: Für Audio-Analyse Hardware-Entwicklung erforderlich (Q2-Q3 2025)
                `);
            }
            return T0HarmonicLibraryFactory.createAnalyzer("MATHEMATICAL");
        }
        
        return T0HarmonicLibraryFactory.createAnalyzer(type);
    }
    
    _showImplementationWarnings() {
        console.log(`
╔══════════════════════════════════════════════════════════════════════════════╗
║                    T0 HARMONIC LIBRARY v2.0.2                               ║
║              Implementierungs-differenzierte Architektur                     ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  ✅ MATHEMATISCH:    100% zuverlässig, 0% Phantoms (VERFÜGBAR)              ║
║  🔄 ANALOG-HARDWARE: 100% zuverlässig für Audio (IN ENTWICKLUNG Q2-Q3 2025) ║
║  ⚠️ BROWSER-AUDIO:   15% zuverlässig, 85% Phantoms (NUR BILDUNG)            ║
║                                                                              ║
║  📚 WISSENSCHAFTLICHE EHRLICHKEIT:                                          ║
║     T0-Theorie mathematisch korrekt → Hardware für Audio erforderlich       ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
        `);
    }
    
    // Delegiert an die gewählte Implementation
    analyzeFrequencies(frequencies, options = {}) {
        return this.analyzer.analyzeFrequencies(frequencies, options);
    }
    
    // Informative Methoden über Implementierungs-Status
    getImplementationStatus() {
        return {
            current: this.analyzer.implementationClass,
            mathematical: {
                status: "AVAILABLE",
                reliability: 1.0,
                phantomRate: 0.0,
                suitableFor: ["Komposition", "Theorie", "Bildung", "Produktion"]
            },
            analogHardware: {
                status: "IN_DEVELOPMENT",
                expectedAvailability: "Q2-Q3 2025",
                estimatedCost: "€290",
                targetReliability: 1.0,
                targetPhantomRate: 0.0,
                suitableFor: ["Audio-Analyse", "Live-Tuning", "Forschung"]
            },
            browserAudio: {
                status: "EDUCATIONAL_ONLY", 
                reliability: 0.15,
                phantomRate: 0.85,
                accuracy: "±5-10Hz",
                suitableFor: ["Bildung", "Demonstration"],
                notSuitableFor: ["T0-Theorie", "Professionelle Analyse"]
            }
        };
    }
    
    getRecommendationFor(useCase) {
        const recommendations = {
            composition: {
                recommended: "MATHEMATICAL",
                reason: "Exakte Akkord-Generierung und -Analyse",
                availability: "Sofort verfügbar"
            },
            education: {
                recommended: "MATHEMATICAL",
                alternative: "BROWSER_AUDIO_EDUCATIONAL für DSP-Limitationen-Demo",
                reason: "T0-Theorie verstehen + Browser-Probleme demonstrieren"
            },
            audioAnalysis: {
                recommended: "ANALOG_HARDWARE",
                status: "In Entwicklung Q2-Q3 2025",
                currentAlternative: "MATHEMATICAL für Simulation",
                reason: "Browser-Audio zu ungenau (85% Phantom-Rate)"
            },
            research: {
                recommended: "ANALOG_HARDWARE", 
                status: "In Entwicklung",
                reason: "Wissenschaftliche Präzision erfordert Phantom-freie Messung"
            }
        };
        
        return recommendations[useCase] || {
            recommended: "MATHEMATICAL",
            reason: "Standard-Empfehlung für unbekannten Anwendungsfall"
        };
    }
}

// =============================================================================
// QUICK-START HELPERS
// =============================================================================

/**
 * Schnellste Art, T0-Analyse zu starten (Mathematisch)
 */
export function quickAnalyze(frequencies) {
    const analyzer = new MathematicalHarmonicAnalyzer();
    return analyzer.analyzeFrequencies(frequencies);
}

/**
 * Demonstriert Browser-Audio-Limitationen (Bildung)
 */
export function demonstrateBrowserLimitations() {
    const demo = new BrowserAudioAnalyzer();
    return demo.demonstrateLimitations();
}

/**
 * Zeigt Hardware-Entwicklungsstand
 */
export function getHardwareDevelopmentStatus() {
    const hardware = new AnalogHardwareInterface();
    return hardware.getPlannedSpecifications();
}

// =============================================================================
// VERSION & METADATA
// =============================================================================

export const VERSION = "2.0.2";
export const BUILD_DATE = new Date().toISOString();
export const IMPLEMENTATION_STATUS = {
    mathematical: "AVAILABLE",
    analogHardware: "IN_DEVELOPMENT",
    browserAudio: "EDUCATIONAL_ONLY"
};

// =============================================================================
// DEPRECATION WARNINGS für alte API
// =============================================================================

/**
 * @deprecated Verwende stattdessen MathematicalHarmonicAnalyzer
 * Alte HarmonicAnalyzer-Klasse wurde wegen Audio-Limitationen deprecated
 */
export class HarmonicAnalyzer {
    constructor() {
        console.warn(`
⚠️ DEPRECATED: HarmonicAnalyzer

Die alte HarmonicAnalyzer-Klasse ist deprecated wegen Audio-Pipeline-Limitationen.

✅ MIGRATION:
• Für mathematische Analyse: MathematicalHarmonicAnalyzer
• Für Audio-Analyse: Warten auf AnalogHardwareInterface (Q2-Q3 2025)
• Für Bildung: BrowserAudioAnalyzer (mit Limitationen-Hinweisen)

GRUND: 85% Phantom-Rate in Browser-Audio macht zuverlässige T0-Analyse unmöglich.
        `);
        
        // Automatische Migration zur mathematischen Version
        return new MathematicalHarmonicAnalyzer();
    }
}

/**
 * @deprecated Browser-Audio ist für T0-Theorie ungeeignet
 */
export function detectFrequencyFromAudio(audioData, sampleRate) {
    console.error(`
❌ DEPRECATED: detectFrequencyFromAudio()

Audio-basierte Frequenzerkennung ist für T0-Theorie ungeeignet:
• 85% Phantom-Rate
• ±5-10Hz Ungenauigkeit  
• 270× schlechter als erforderlich

✅ ALTERNATIVEN:
• Mathematische Frequenz-Eingabe: MathematicalHarmonicAnalyzer  
• Hardware-Entwicklung: AnalogHardwareInterface (Q2-Q3 2025)
• Bildung: BrowserAudioAnalyzer.demonstrateLimitations()
    `);
    
    throw new Error("Audio-basierte Erkennung deprecated. Verwende mathematische Implementation.");
}

// =============================================================================
// DEFAULT EXPORT für einfache Verwendung
// =============================================================================

export default T0HarmonicLibrary;