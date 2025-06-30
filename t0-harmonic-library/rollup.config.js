export default {
  input: 'src/index.js',
  output: [
    {
      name: 'T0AudioSystem',
      file: 'dist/t0-audio-system.umd.js',
      format: 'umd',
      banner: '/* T0 Harmonic Library v2.0.0 by Johann Pascher */',
      exports: 'named'
    },
    {
      file: 'dist/t0-audio-system.esm.js',
      format: 'es',
      banner: '/* T0 Harmonic Library v2.0.0 by Johann Pascher */'
    },
    {
      file: 'dist/t0-audio-system.cjs.js',
      format: 'cjs',
      banner: '/* T0 Harmonic Library v2.0.0 by Johann Pascher */',
      exports: 'named'
    }
  ]
};
