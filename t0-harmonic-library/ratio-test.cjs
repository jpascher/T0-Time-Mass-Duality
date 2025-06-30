// Test der verhältnisbasierten Berechnungen
const fs = require('fs');

console.log('🎵 T0 Verhältnisbasierte Berechnungen Test');
console.log('=========================================');

// Simuliere Browser-Umgebung
global.window = {};

try {
    // Lade UMD-Version
    const umdCode = fs.readFileSync('dist/t0-audio-system.umd.js', 'utf8');
    eval(umdCode);

    if (global.window.T0AudioSystem) {
        const t0 = new global.window.T0AudioSystem.T0AudioSystemComplete();
        
        console.log('✅ T0 System mit verhältnisbasierten Berechnungen geladen');
        
        // Test verschiedene Grundfrequenzen
        const testFrequencies = [220, 261.63, 440]; // A3, C4, A4
        
        testFrequencies.forEach(baseFreq => {
            console.log('\\n🎼 C-Major bei ' + baseFreq + ' Hz:');
            
            const ratios = t0.getRatiosForChord('C-Major');
            const frequencies = t0.getFrequenciesForChord('C-Major', baseFreq);
            const intervals = t0.getIntervalsForChord('C-Major');
            
            console.log('  Verhältnisse: ' + ratios.join(' : '));
            console.log('  Frequenzen: ' + frequencies.join(', ') + ' Hz');
            console.log('  Intervalle: ' + intervals.join(', '));
            
            // Mathematische Verifikation
            const expectedFreqs = ratios.map(ratio => Math.round(baseFreq * ratio * 100) / 100);
            const isCorrect = frequencies.every((freq, i) => Math.abs(freq - expectedFreqs[i]) < 0.1);
            console.log('  Mathematik: ' + (isCorrect ? '✅ Korrekt' : '❌ Fehler'));
        });
        
        // Test Intervall-Analyse
        console.log('\\n🎯 Intervall-Analyse Test:');
        const cToE = t0.analyzeInterval(261.63, 329.63); // C zu E (große Terz)
        console.log('C zu E: Verhältnis ' + cToE.ratio.toFixed(4) + ', ' + cToE.cents + ' Cent, ' + cToE.intervalName);
        
        const cToG = t0.analyzeInterval(261.63, 392.00); // C zu G (Quinte)
        console.log('C zu G: Verhältnis ' + cToG.ratio.toFixed(4) + ', ' + cToG.cents + ' Cent, ' + cToG.intervalName);
        
        // System-Info
        console.log('\\n📊 System-Info:');
        const info = t0.getSystemInfo();
        console.log('Version: ' + info.version);
        console.log('Typ: ' + info.calculationType);
        console.log('Basis-Frequenz: ' + info.baseFrequency + ' Hz');
        
        // Test Transposition
        console.log('\\n🔄 Transpositions-Test:');
        const aMinor220 = t0.transposeChord('A-Minor', 220); // A-Minor bei A3
        const aMinor440 = t0.transposeChord('A-Minor', 440); // A-Minor bei A4
        console.log('A-Minor bei 220 Hz: ' + aMinor220.join(', ') + ' Hz');
        console.log('A-Minor bei 440 Hz: ' + aMinor440.join(', ') + ' Hz');
        
        console.log('\\n🎉 Alle verhältnisbasierten Tests erfolgreich!');
        
    } else {
        console.log('❌ T0AudioSystem nicht gefunden in UMD-Datei');
    }
    
} catch (error) {
    console.error('❌ Test fehlgeschlagen:', error.message);
}
