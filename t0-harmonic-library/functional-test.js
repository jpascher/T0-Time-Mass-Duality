// Funktionaler Test der T0 Harmonic Library
console.log('🎵 T0 Harmonic Library - Funktionstest');
console.log('=====================================');

try {
    // Simuliere Browser-Umgebung für UMD-Test
    global.window = {};
    
    // Lade die UMD-Version
    const fs = require('fs');
    const umdCode = fs.readFileSync('dist/t0-audio-system.umd.js', 'utf8');
    
    // Führe UMD-Code aus
    eval(umdCode);
    
    // Teste ob T0AudioSystem verfügbar ist
    if (global.window.T0AudioSystem) {
        console.log('✅ UMD-Version geladen');
        
        const t0 = new global.window.T0AudioSystem.T0AudioSystemComplete({
            debugMode: true
        });
        
        console.log('✅ T0 System initialisiert');
        console.log('📊 System Info:', t0.getSystemInfo());
        
        // Teste Akkord-Analyse
        t0.analyzeChord('C-Major').then(result => {
            console.log('🎵 Akkord-Analyse:', result);
            console.log('✅ Alle Tests erfolgreich!');
        });
    } else {
        console.log('❌ T0AudioSystem nicht gefunden');
    }
    
} catch (error) {
    console.error('❌ Test fehlgeschlagen:', error.message);
}
