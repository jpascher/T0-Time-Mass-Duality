// Test der verhältnisbasierten Berechnungen
import { T0AudioSystemComplete } from './dist/t0-audio-system.esm.js';

console.log('🎵 T0 Verhältnisbasierte Berechnungen Test');
console.log('=========================================');

const t0 = new T0AudioSystemComplete();

// Test verschiedene Grundfrequenzen
const testFrequencies = [220, 261.63, 440]; // A3, C4, A4

testFrequencies.forEach(async baseFreq => {
    const result = await t0.analyzeChord('C-Major', baseFreq);
    console.log(\\nC-Major bei \ Hz:\);
    console.log(\Verhältnisse: \\);
    console.log(\Frequenzen: \ Hz\);
    console.log(\Intervalle: \\);
});
