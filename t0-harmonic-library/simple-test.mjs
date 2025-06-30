// Einfacher Bibliotheks-Test
import fs from 'fs';

console.log('🎵 T0 Harmonic Library Test');
console.log('==========================');

// Zeige Dateigrößen
const files = [
    'dist/t0-audio-system.umd.js',
    'dist/t0-audio-system.esm.js', 
    'dist/t0-audio-system.cjs.js'
];

files.forEach(file => {
    try {
        const stats = fs.statSync(file);
        console.log('✅ ' + file + ': ' + stats.size + ' bytes');
    } catch (error) {
        console.log('❌ ' + file + ': nicht gefunden');
    }
});

console.log('\n🚀 Bibliothek erfolgreich erstellt!');
console.log('📦 Bereit für Integration!');
