/**
 * Basic T0 Audio System Tests
 */

import { T0AudioSystemComplete } from '../src/index.js';

describe('T0AudioSystemComplete', () => {
  let t0System;
  
  beforeEach(() => {
    t0System = new T0AudioSystemComplete();
  });
  
  test('should initialize with correct version', () => {
    expect(t0System.version).toBe('2.0.0');
    expect(t0System.author).toBe('Johann Pascher');
    expect(t0System.project).toBe('T0-Time-Mass-Duality');
  });
  
  test('should initialize system state', () => {
    expect(t0System.state.isInitialized).toBe(true);
    expect(t0System.state.currentChord).toBe(null);
  });
  
  test('should analyze chord', async () => {
    const result = await t0System.analyzeChord('C-Major');
    expect(result.success).toBe(true);
    expect(result.chord).toBe('C-Major');
    expect(t0System.state.currentChord).toBe('C-Major');
  });
  
  test('should return system info', () => {
    const info = t0System.getSystemInfo();
    expect(info.version).toBe('2.0.0');
    expect(info.author).toBe('Johann Pascher');
    expect(info.isInitialized).toBe(true);
  });
});
