// Jest Setup File
// Mocks für Web Audio API
Object.defineProperty(window, 'AudioContext', {
  writable: true,
  value: jest.fn().mockImplementation(() => ({
    createOscillator: jest.fn(),
    createGain: jest.fn(),
    destination: {},
    currentTime: 0
  }))
});

global.performance = {
  now: jest.fn(() => Date.now())
};
