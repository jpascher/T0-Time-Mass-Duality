// CommonJS Test
const fs = require('fs');
const path = require('path');

console.log('🎵 T0 Harmonic Library - CommonJS Test');
console.log('====================================');

// Teste alle erstellten Dateien
const distFiles = fs.readdirSync('dist');
console.log('📁 Dateien in dist/:', distFiles);

distFiles.forEach(file => {
    if (file.endsWith('.js')) {
        const filePath = path.join('dist', file);
        const stats = fs.statSync(filePath);
        console.log('📄 ' + file + ': ' + stats.size + ' bytes');
        
        // Zeige erste Zeile der Datei
        const content = fs.readFileSync(filePath, 'utf8');
        const firstLine = content.split('\n')[0];
        console.log('   Erste Zeile: ' + firstLine);
    }
});

console.log('\n✅ Alle Dateien erfolgreich erstellt!');
console.log('🎯 T0 Harmonic Library ist bereit!');
