# T0 Harmonic Library v2.0.1

> Advanced ratio-based chord analysis with optimized tuning  
> Part of **T0-Time-Mass-Duality** research by **Johann Pascher**

## 🚀 Installation

### From GitHub:
\\\ash
# Direct installation:
npm install git+https://github.com/jpascher/T0-Time-Mass-Duality.git

# Or in package.json:
"dependencies": {
  "t0-harmonic-library": "git+https://github.com/jpascher/T0-Time-Mass-Duality.git#main"
}
\\\

### Local Development:
\\\ash
git clone https://github.com/jpascher/T0-Time-Mass-Duality.git
cd T0-Time-Mass-Duality/t0-harmonic-library
npm install && npm run build
\\\

## 🎵 Quick Start

### Browser:
\\\html
<script src="dist/t0-audio-system.umd.js"></script>
<script>
  const t0 = new T0AudioSystem.T0AudioSystemComplete();
  t0.analyzeChord('C-Minor').then(result => {
    console.log('Optimized Minor:', result.ratios); // [1.0, 1.1875, 1.5]
  });
</script>
\\\

### Node.js:
\\\javascript
const { T0AudioSystemComplete } = require('./dist/t0-audio-system.cjs.js');
const t0 = new T0AudioSystemComplete();
const result = await t0.analyzeChord('A-Minor', 440);
\\\

## 🎯 Key Features

- **Optimized Moll**: 19/16 ratio (only 2.5 cents from temperament!)
- **Pure Dur**: 5/4 ratio (harmonically rich)
- **Multi-format**: UMD/ESM/CJS builds (10-12KB)
- **200+ chords** with mathematical precision

## 🔬 Research

Part of T0-Time-Mass-Duality research exploring optimal balance between:
- Mathematical purity (pure ratios)
- Practical compatibility (temperament)

**Result**: Minor chords only 2.5 cents from equal temperament while maintaining integer ratios!

## 👨‍🔬 Author

Johann Pascher | T0-Time-Mass-Duality Research  
GitHub: https://github.com/jpascher/T0-Time-Mass-Duality

## 📄 License

MIT
