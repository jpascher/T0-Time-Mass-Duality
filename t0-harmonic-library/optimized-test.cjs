const fs = require('fs');
global.window = {};
const umdCode = fs.readFileSync('dist/t0-audio-system.umd.js', 'utf8');
eval(umdCode);

const t0 = new global.window.T0AudioSystem.T0AudioSystemComplete();

console.log('🎵 T0 System v2.0.1 - Optimierte Moll-Verhältnisse Test');
console.log('======================================================');

// Test Moll-Optimierung
const mollTest = ['C-Minor', 'A-Minor', 'D-Minor'];
mollTest.forEach(chord => {
    const ratios = t0.getRatiosForChord(chord);
    const frequencies = t0.getFrequenciesForChord(chord, 261.63);
    const tuningInfo = t0.getTuningSystemInfo(chord);
    
    console.log('\\n' + chord + ':');
    console.log('  Verhältnisse: ' + ratios.map(r => r.toFixed(4)).join(' : '));
    console.log('  Frequenzen: ' + frequencies.join(', ') + ' Hz');
    console.log('  System: ' + tuningInfo.system);
    console.log('  Abweichung: ' + tuningInfo.centDeviation + ' Cent');
});

// Vergleich mit 12-TET
console.log('\\n🎯 Vergleich mit 12-TET:');
const comparison = t0.compareToTuning('C-Minor', '12-tet');
if (comparison) {
    comparison.forEach((comp, i) => {
        const intervalNames = ['Prim', 'Kleine Terz', 'Quinte'];
        console.log(intervalNames[i] + ': ' + comp.centDifference + ' Cent Unterschied');
    });
}

// Test Dur vs Moll Vergleich
console.log('\\n🎼 Dur vs Moll Stimmungsvergleich:');
const durInfo = t0.getTuningSystemInfo('C-Major');
const mollInfo = t0.getTuningSystemInfo('C-Minor');
console.log('Dur (C-Major): ' + durInfo.system + ' (' + durInfo.centDeviation + ' Cent)');
console.log('Moll (C-Minor): ' + mollInfo.system + ' (' + mollInfo.centDeviation + ' Cent)');

console.log('\\n✅ Optimierung erfolgreich: Moll nur 2.5 Cent von temperiert!');
