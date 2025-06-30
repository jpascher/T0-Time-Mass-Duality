# T0 Harmonic Library

> Advanced difference tone-based chord analysis and reconstruction system  
> Part of the **T0-Time-Mass-Duality** research project by **Johann Pascher**

[![npm version](https://badge.fury.io/js/t0-harmonic-library.svg)](https://badge.fury.io/js/t0-harmonic-library)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🎵 Overview

This library combines all existing T0 harmonic analysis components into a unified, npm-ready package. Built on years of research into difference tone theory and harmonic analysis.

### Existing Components Integrated:
- \Audio_Analyzer.html\ - Main analysis interface
- \	0_harmonic_analyzer.js\ - Core analysis functions  
- \harmonic_components_library.js\ - Component library
- \	0_audio_test_program-85%.html\ - Test program
- \difference_tone_rules.md\ - Theory documentation
- And all other research files...

## 🚀 Quick Start

\\\ash
npm install t0-harmonic-library
\\\

\\\javascript
import { T0AudioSystemComplete } from 't0-harmonic-library';

const t0 = new T0AudioSystemComplete();
await t0.analyzeChord('C-Major');
console.log(t0.getSystemInfo());
\\\

## 📁 Project Structure

Your existing research files are now organized as:
- \src/\ - Source code (integrated from your existing JS files)
- \dist/\ - Built library files
- \examples/\ - Usage examples
- \	ests/\ - Test suite
- \docs/\ - Documentation

## 🔧 Development Commands

\\\ash
npm install        # Install dependencies
npm run build      # Build the library
npm test           # Run tests
npm run lint       # Check code quality
\\\

## 📊 Your Research Files

All your existing files remain unchanged:
- Audio_Analyzer.html (\ bytes)
- t0_harmonic_analyzer.js (\ bytes)
- harmonic_components_library.js (\ bytes)
- And \ other research files...

## 👨‍🔬 Author

**Johann Pascher**  
T0-Time-Mass-Duality Research  
GitHub: https://github.com/jpascher

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details.
