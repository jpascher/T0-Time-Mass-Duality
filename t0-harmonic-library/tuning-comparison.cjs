// Vergleich: Reine Stimmung vs. Gleichstufige Stimmung
console.log('🎼 Reine Stimmung vs. Gleichstufige Stimmung');
console.log('===========================================');

const baseFreq = 261.63; // C4

// Reine Stimmung (T0-Bibliothek)
const pureRatios = {
    'Prim': 1.0,
    'Große Terz': 5/4,      // 1.25
    'Quinte': 3/2,          // 1.5
    'Kleine Terz': 6/5      // 1.2
};

// Gleichstufige Stimmung (12-TET)
const equalRatios = {
    'Prim': 1.0,
    'Große Terz': Math.pow(2, 4/12),   // 1.2599
    'Quinte': Math.pow(2, 7/12),       // 1.4983  
    'Kleine Terz': Math.pow(2, 3/12)   // 1.1892
};

Object.keys(pureRatios).forEach(interval => {
    const pure = pureRatios[interval];
    const equal = equalRatios[interval];
    const pureFreq = Math.round(baseFreq * pure * 100) / 100;
    const equalFreq = Math.round(baseFreq * equal * 100) / 100;
    const cents = Math.round(1200 * Math.log2(pure / equal));
    
    console.log(interval + ':');
    console.log('  Reine Stimmung: ' + pure.toFixed(4) + ' (' + pureFreq + ' Hz)');
    console.log('  Gleichstufig: ' + equal.toFixed(4) + ' (' + equalFreq + ' Hz)');
    console.log('  Unterschied: ' + Math.abs(cents) + ' Cent');
    console.log('');
});

console.log('✅ Ihre T0-Bibliothek verwendet mathematisch reine Verhältnisse!');
console.log('🎵 Dies führt zu harmonischeren Klängen als gleichstufige Stimmung.');
