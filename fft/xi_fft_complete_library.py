"""
ξ-FFT Complete Library - Vollständige Spektralanalyse-Bibliothek
==============================================================

Eine umfassende Bibliothek für Frequenzanalyse mit exakten harmonischen Verhältnissen,
optimiert für Schwebungsanalyse und musikalische Anwendungen.

Installation:
    pip install numpy fractions

Verwendung:
    from xi_fft_library import XiFFT, SignalGenerator, WAVUtils, HarmonicDatabase
    
    # Einfache Analyse:
    xi_fft = XiFFT(sample_rate=44100)
    signal = SignalGenerator.create_beating_signal(440, 5, duration=3)
    result = xi_fft.analyze(signal)
    
    # Harmonische Intelligenz:
    result = xi_fft.analyze(signal, f0_hint=440)
    
    # WAV Export:
    WAVUtils.save_wav(signal, "output.wav")

Autor: ξ-FFT Development Team
Version: 2.0.0
Datum: 13. Juni 2025
"""

import math
import numpy as np
from fractions import Fraction
from typing import List, Dict, Tuple, Optional, Union, Callable
import wave
import os

# ===== VERSION & METADATA =====
__version__ = "2.0.0"
__author__ = "ξ-FFT Development Team"
__date__ = "2025-06-13"
__description__ = "Advanced spectral analysis with exact harmonic ratios"

# ===== HARMONIC RATIO DATABASE =====
class HarmonicDatabase:
    """
    Datenbank für exakte musikalische Verhältnisse und harmonische Intelligenz
    
    Diese Klasse enthält eine umfassende Sammlung musikalischer Intervalle
    als exakte Brüche, sortiert nach Wahrscheinlichkeit und Einfachheit.
    """
    
    def __init__(self):
        """Initialisiere die harmonische Datenbank"""
        
        # Exakte musikalische Intervalle
        # Format: Fraction(numerator, denominator): (name, probability%, category, priority_level)
        self.EXACT_INTERVALS = {
            # Perfekte Konsonanzen (höchste Priorität):
            Fraction(1, 1):   ("Unison",           100, "Perfect", 1),
            Fraction(2, 1):   ("Oktave",           95,  "Perfect", 1),
            Fraction(3, 2):   ("Quinte",           90,  "Perfect", 2),
            Fraction(4, 3):   ("Quarte",           85,  "Perfect", 2),
            
            # Imperfekte Konsonanzen:
            Fraction(5, 4):   ("Große Terz",       80,  "Consonant", 3),
            Fraction(6, 5):   ("Kleine Terz",      75,  "Consonant", 3),
            Fraction(5, 3):   ("Große Sexte",      70,  "Consonant", 3),
            Fraction(8, 5):   ("Kleine Sexte",     65,  "Consonant", 3),
            
            # Weitere Konsonanzen:
            Fraction(8, 3):   ("Große Dezime",     60,  "Consonant", 4),
            Fraction(10, 3):  ("Große Undezime",   55,  "Consonant", 4),
            
            # Ganztöne und Sekunden:
            Fraction(9, 8):   ("Großer Ganzton",   50,  "Dissonant", 5),
            Fraction(10, 9):  ("Kleiner Ganzton",  45,  "Dissonant", 5),
            Fraction(16, 15): ("Kleiner Halbton",  40,  "Dissonant", 6),
            Fraction(25, 24): ("Chromatischer HT", 35,  "Dissonant", 6),
            
            # Septimen:
            Fraction(15, 8):  ("Große Septime",    30,  "Dissonant", 7),
            Fraction(16, 9):  ("Kleine Septime",   25,  "Dissonant", 7),
            Fraction(9, 5):   ("Kleine Septime alt", 22, "Dissonant", 7),
            
            # Harmonische Obertöne (Naturtonreihe):
            Fraction(7, 4):   ("Harmonische 7te",  20,  "Complex", 8),
            Fraction(9, 4):   ("Harmonische 9te",  18,  "Complex", 8),
            Fraction(11, 8):  ("Harmonische 11te", 15,  "Complex", 9),
            Fraction(13, 8):  ("Harmonische 13te", 12,  "Complex", 9),
            Fraction(15, 8):  ("Harmonische 15te", 10,  "Complex", 10),
            
            # Erweiterte harmonische Verhältnisse:
            Fraction(7, 6):   ("Subminor-Terz",    8,   "Complex", 10),
            Fraction(11, 6):  ("Neutral-Septime",  6,   "Complex", 11),
            Fraction(13, 12): ("Tridezimalhalb",   5,   "Complex", 11),
            
            # Mikro-Intervalle (wichtig für Schwebungsanalyse):
            Fraction(81, 80): ("Syntonisches Komma", 4,  "Microtone", 12),
            Fraction(256, 243): ("Limma",            3,  "Microtone", 12),
            Fraction(128, 125): ("Dieses",           2,  "Microtone", 13),
            Fraction(648, 625): ("Diaschisma",       1,  "Microtone", 13),
            
            # Schwebungs-relevante Verhältnisse:
            Fraction(1001, 1000): ("Millikomma",      0.5, "Beating", 14),
            Fraction(101, 100):   ("Centikomma",      0.3, "Beating", 14),
            Fraction(51, 50):     ("Zweiprozent",     0.2, "Beating", 15),
        }
        
        # Sortiert nach Priorität (niedrigste Zahl = höchste Priorität)
        self.PRIORITY_RATIOS = sorted(
            self.EXACT_INTERVALS.keys(),
            key=lambda r: (self.EXACT_INTERVALS[r][3], -self.EXACT_INTERVALS[r][1])
        )
        
        # Musikalische Muster für Erkennung
        self.MUSICAL_PATTERNS = {
            'dur_dreiklang': {Fraction(1,1), Fraction(5,4), Fraction(3,2)},
            'moll_dreiklang': {Fraction(1,1), Fraction(6,5), Fraction(3,2)},
            'dom7_akkord': {Fraction(1,1), Fraction(5,4), Fraction(3,2), Fraction(7,4)},
            'maj7_akkord': {Fraction(1,1), Fraction(5,4), Fraction(3,2), Fraction(15,8)},
            'quartzirkel': {Fraction(1,1), Fraction(4,3), Fraction(16,9), Fraction(64,27)},
            'quintenzirkel': {Fraction(1,1), Fraction(3,2), Fraction(9,4), Fraction(27,8)},
        }
        
        print(f"🎼 HarmonicDatabase: {len(self.EXACT_INTERVALS)} Intervalle, {len(self.MUSICAL_PATTERNS)} Muster")
    
    def get_interval_info(self, ratio_exact: Fraction) -> Optional[Dict]:
        """
        Hole detaillierte Informationen über ein musikalisches Intervall
        
        Args:
            ratio_exact: Exaktes Frequenzverhältnis als Fraction
            
        Returns:
            Dictionary mit Intervall-Informationen oder None
        """
        if ratio_exact in self.EXACT_INTERVALS:
            name, probability, category, priority = self.EXACT_INTERVALS[ratio_exact]
            return {
                'name': name,
                'probability': probability,
                'category': category,
                'priority': priority,
                'complexity': ratio_exact.numerator + ratio_exact.denominator,
                'is_consonant': category in ["Perfect", "Consonant"],
                'is_microtone': category in ["Microtone", "Beating"],
                'cents': self.ratio_to_cents(ratio_exact)
            }
        return None
    
    def frequency_to_exact_ratio(self, f1: float, f2: float, tolerance: float = 0.02) -> Optional[Fraction]:
        """
        Konvertiere Frequenz-Verhältnis zu exaktem Bruch
        
        Args:
            f1, f2: Frequenzen in Hz
            tolerance: Toleranz für Matching (default: 2%)
            
        Returns:
            Exakter Bruch oder None falls kein Match
        """
        ratio_float = max(f1, f2) / min(f1, f2)
        
        # Suche in bekannten Intervallen (nach Priorität sortiert):
        for exact_ratio in self.PRIORITY_RATIOS:
            if abs(float(exact_ratio) - ratio_float) / ratio_float < tolerance:
                return exact_ratio
        
        # Automatische Bruch-Approximation für unbekannte Verhältnisse:
        approx_fraction = Fraction(ratio_float).limit_denominator(max_denominator=100)
        
        # Nur wenn einfach genug (kleine ganze Zahlen):
        complexity = approx_fraction.numerator + approx_fraction.denominator
        if complexity <= 25:  # Akzeptiere einfache unbekannte Verhältnisse
            return approx_fraction
        
        return None
    
    def detect_musical_pattern(self, exact_ratios: List[Fraction]) -> str:
        """
        Erkenne musikalische Muster in einer Liste von Verhältnissen
        
        Args:
            exact_ratios: Liste exakter Frequenzverhältnisse
            
        Returns:
            Name des erkannten Musters oder "Unbekanntes Muster"
        """
        ratio_set = set(exact_ratios)
        
        # Teste bekannte Muster:
        for pattern_name, pattern_ratios in self.MUSICAL_PATTERNS.items():
            if pattern_ratios.issubset(ratio_set):
                return pattern_name.replace('_', '-').title()
        
        # Spezielle Erkennungen:
        if Fraction(2,1) in ratio_set:
            return "Oktav-Struktur"
        elif Fraction(3,2) in ratio_set and Fraction(4,3) in ratio_set:
            return "Quint-Quart-Struktur"
        elif any(r for r in exact_ratios if 1.01 <= float(r) <= 1.1):
            return "Schwebungs-Struktur"
        elif len([r for r in exact_ratios if r.denominator <= 8]) >= 3:
            return "Einfache Harmonische Reihe"
        
        return "Unbekanntes Muster"
    
    def get_harmonic_series(self, fundamental: Fraction, max_harmonics: int = 16) -> List[Fraction]:
        """
        Generiere harmonische Reihe basierend auf Grundton
        
        Args:
            fundamental: Grundfrequenz-Verhältnis
            max_harmonics: Maximale Anzahl Obertöne
            
        Returns:
            Liste harmonischer Verhältnisse
        """
        harmonics = []
        for n in range(1, max_harmonics + 1):
            harmonic = fundamental * n
            harmonics.append(harmonic)
        return harmonics
    
    @staticmethod
    def ratio_to_cents(ratio: Fraction) -> float:
        """
        Konvertiere Frequenzverhältnis zu Cent (1200 Cent = 1 Oktave)
        
        Args:
            ratio: Frequenzverhältnis als Fraction
            
        Returns:
            Intervall in Cent
        """
        return 1200 * math.log2(float(ratio))
    
    @staticmethod
    def cents_to_ratio(cents: float) -> float:
        """
        Konvertiere Cent zu Frequenzverhältnis
        
        Args:
            cents: Intervall in Cent
            
        Returns:
            Frequenzverhältnis als Float
        """
        return 2 ** (cents / 1200)

# ===== SIGNAL GENERATOR =====
class SignalGenerator:
    """
    Erweiterte Signal-Generierung für verschiedene Anwendungen
    """
    
    @staticmethod
    def create_beating_signal(f0: float, delta_f: float, duration: float = 5.0, 
                            sample_rate: int = 44100, amplitudes: Tuple[float, float, float] = (0.4, 0.8, 0.4),
                            phase_shifts: Tuple[float, float, float] = (0, 0, 0)) -> np.ndarray:
        """
        Erstelle 3-Frequenz Schwebungs-Signal mit konfigurierbaren Parametern
        
        Args:
            f0: Grundfrequenz in Hz
            delta_f: Schwebungsfrequenz in Hz
            duration: Signal-Dauer in Sekunden
            sample_rate: Abtastrate in Hz
            amplitudes: Amplituden für (f0-Δf, f0, f0+Δf)
            phase_shifts: Phasenverschiebungen in Radiant
            
        Returns:
            Generiertes Signal als NumPy Array
        """
        print(f"🎵 Generiere 3-Ton Schwebung: f₀={f0}Hz, Δf={delta_f}Hz, {duration}s")
        
        t = np.linspace(0, duration, int(duration * sample_rate))
        
        # Drei Frequenzen
        f1 = f0 - delta_f  # Unterton
        f2 = f0            # Grundton  
        f3 = f0 + delta_f  # Oberton
        
        # Phasenverschiebungen
        phase1, phase2, phase3 = phase_shifts
        
        # Drei Sinustöne mit individuellen Parametern
        signal1 = amplitudes[0] * np.sin(2 * np.pi * f1 * t + phase1)
        signal2 = amplitudes[1] * np.sin(2 * np.pi * f2 * t + phase2)
        signal3 = amplitudes[2] * np.sin(2 * np.pi * f3 * t + phase3)
        
        # Kombiniere alle drei Signale
        signal = signal1 + signal2 + signal3
        
        # Normalisierung
        max_amplitude = np.max(np.abs(signal))
        if max_amplitude > 0:
            signal = signal / max_amplitude * 0.8  # 80% der Maximalamplitude
        
        print(f"✅ Signal generiert: {len(signal)} Samples, Frequenzen: {f1:.1f}, {f2:.1f}, {f3:.1f} Hz")
        return signal
    
    @staticmethod
    def create_harmonic_series(fundamental: float, harmonics: List[int], 
                             amplitudes: Optional[List[float]] = None,
                             duration: float = 3.0, sample_rate: int = 44100) -> np.ndarray:
        """
        Erstelle Signal aus harmonischer Reihe
        
        Args:
            fundamental: Grundfrequenz in Hz
            harmonics: Liste der Harmonics (z.B. [1, 2, 3, 4, 5])
            amplitudes: Amplituden für jeden Harmonic (optional)
            duration: Signal-Dauer in Sekunden
            sample_rate: Abtastrate in Hz
            
        Returns:
            Harmonisches Signal als NumPy Array
        """
        if amplitudes is None:
            # Standard-Amplituden: 1/n (natürliche harmonische Reihe)
            amplitudes = [1.0 / n for n in harmonics]
        
        if len(amplitudes) != len(harmonics):
            raise ValueError("Anzahl Harmonics muss Anzahl Amplituden entsprechen")
        
        t = np.linspace(0, duration, int(duration * sample_rate))
        signal = np.zeros_like(t)
        
        for harmonic, amplitude in zip(harmonics, amplitudes):
            frequency = fundamental * harmonic
            signal += amplitude * np.sin(2 * np.pi * frequency * t)
        
        # Normalisierung
        signal = signal / np.max(np.abs(signal)) * 0.8
        
        print(f"🎼 Harmonische Reihe generiert: f₀={fundamental}Hz, Harmonics: {harmonics}")
        return signal
    
    @staticmethod
    def create_chord(frequencies: List[float], amplitudes: Optional[List[float]] = None,
                    duration: float = 3.0, sample_rate: int = 44100) -> np.ndarray:
        """
        Erstelle Akkord aus beliebigen Frequenzen
        
        Args:
            frequencies: Liste der Frequenzen in Hz
            amplitudes: Amplituden für jede Frequenz (optional)
            duration: Signal-Dauer in Sekunden
            sample_rate: Abtastrate in Hz
            
        Returns:
            Akkord-Signal als NumPy Array
        """
        if amplitudes is None:
            amplitudes = [1.0] * len(frequencies)
        
        if len(amplitudes) != len(frequencies):
            raise ValueError("Anzahl Frequenzen muss Anzahl Amplituden entsprechen")
        
        t = np.linspace(0, duration, int(duration * sample_rate))
        signal = np.zeros_like(t)
        
        for freq, amp in zip(frequencies, amplitudes):
            signal += amp * np.sin(2 * np.pi * freq * t)
        
        # Normalisierung
        signal = signal / np.max(np.abs(signal)) * 0.8
        
        print(f"🎶 Akkord generiert: {len(frequencies)} Töne, Frequenzen: {frequencies}")
        return signal
    
    @staticmethod
    def create_sweep(start_freq: float, end_freq: float, duration: float = 5.0,
                    sample_rate: int = 44100, sweep_type: str = 'linear') -> np.ndarray:
        """
        Erstelle Frequenz-Sweep (Gleitton)
        
        Args:
            start_freq: Startfrequenz in Hz
            end_freq: Endfrequenz in Hz
            duration: Signal-Dauer in Sekunden
            sample_rate: Abtastrate in Hz
            sweep_type: 'linear' oder 'logarithmic'
            
        Returns:
            Sweep-Signal als NumPy Array
        """
        t = np.linspace(0, duration, int(duration * sample_rate))
        
        if sweep_type == 'linear':
            # Lineare Frequenzänderung
            instantaneous_freq = start_freq + (end_freq - start_freq) * t / duration
        elif sweep_type == 'logarithmic':
            # Logarithmische Frequenzänderung
            instantaneous_freq = start_freq * (end_freq / start_freq) ** (t / duration)
        else:
            raise ValueError("sweep_type muss 'linear' oder 'logarithmic' sein")
        
        # Berechne Phase durch Integration der Momentanfrequenz
        phase = 2 * np.pi * np.cumsum(instantaneous_freq) / sample_rate
        signal = np.sin(phase)
        
        print(f"🌊 Sweep generiert: {start_freq}Hz → {end_freq}Hz, {sweep_type}")
        return signal

# ===== WAV FILE UTILITIES =====
class WAVUtils:
    """
    Erweiterte WAV-Datei Utilities mit robuster Fehlerbehandlung
    """
    
    @staticmethod
    def save_wav(signal: np.ndarray, filename: str, sample_rate: int = 44100, 
                bit_depth: int = 16) -> bool:
        """
        Speichere Signal als WAV-Datei
        
        Args:
            signal: Audio-Signal als NumPy Array
            filename: Ausgabe-Dateiname
            sample_rate: Abtastrate in Hz
            bit_depth: Bit-Tiefe (8 oder 16)
            
        Returns:
            True bei Erfolg, False bei Fehler
        """
        try:
            # Sicherstellen dass Verzeichnis existiert
            os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)
            
            # Normalisiere und konvertiere zu Integer
            if bit_depth == 16:
                signal_int = (signal * 32767).astype(np.int16)
                sampwidth = 2
            elif bit_depth == 8:
                signal_int = ((signal + 1) * 127.5).astype(np.uint8)
                sampwidth = 1
            else:
                raise ValueError("bit_depth muss 8 oder 16 sein")
            
            with wave.open(filename, 'w') as wav_file:
                wav_file.setnchannels(1)  # Mono
                wav_file.setsampwidth(sampwidth)
                wav_file.setframerate(sample_rate)
                wav_file.writeframes(signal_int.tobytes())
                
            print(f"💾 WAV gespeichert: {filename} ({len(signal)} Samples, {sample_rate}Hz, {bit_depth}bit)")
            return True
            
        except Exception as e:
            print(f"❌ WAV Speicher-Fehler: {e}")
            return False
    
    @staticmethod
    def load_wav(filename: str) -> Tuple[Optional[np.ndarray], Optional[int]]:
        """
        Lade WAV-Datei mit robuster Fehlerbehandlung
        
        Args:
            filename: WAV-Dateiname
            
        Returns:
            Tuple (signal, sample_rate) oder (None, None) bei Fehler
        """
        try:
            with wave.open(filename, 'r') as wav_file:
                frames = wav_file.readframes(-1)
                sample_rate = wav_file.getframerate()
                channels = wav_file.getnchannels()
                sampwidth = wav_file.getsampwidth()
                
                # Konvertiere zu numpy array
                if sampwidth == 2:  # 16-bit
                    signal = np.frombuffer(frames, dtype=np.int16)
                    signal = signal.astype(np.float32) / 32767.0
                elif sampwidth == 1:  # 8-bit
                    signal = np.frombuffer(frames, dtype=np.uint8)
                    signal = (signal.astype(np.float32) - 127.5) / 127.5
                else:
                    raise ValueError(f"Nicht unterstützte Bit-Tiefe: {sampwidth * 8}")
                
                # Mono-Konvertierung bei Stereo
                if channels == 2:
                    signal = signal.reshape(-1, 2)
                    signal = np.mean(signal, axis=1)  # Stereo zu Mono
                elif channels > 2:
                    signal = signal.reshape(-1, channels)
                    signal = signal[:, 0]  # Nur erster Kanal
                
                print(f"📁 WAV geladen: {filename} ({len(signal)} Samples, {sample_rate}Hz, {channels}ch)")
                return signal, sample_rate
                
        except Exception as e:
            print(f"❌ WAV Lade-Fehler: {e}")
            return None, None
    
    @staticmethod
    def get_wav_info(filename: str) -> Optional[Dict]:
        """
        Hole WAV-Datei Informationen ohne Laden der Audio-Daten
        
        Args:
            filename: WAV-Dateiname
            
        Returns:
            Dictionary mit Datei-Informationen oder None
        """
        try:
            with wave.open(filename, 'r') as wav_file:
                info = {
                    'channels': wav_file.getnchannels(),
                    'sample_rate': wav_file.getframerate(),
                    'frames': wav_file.getnframes(),
                    'sample_width': wav_file.getsampwidth(),
                    'duration': wav_file.getnframes() / wav_file.getframerate(),
                    'bit_depth': wav_file.getsampwidth() * 8
                }
                return info
        except Exception as e:
            print(f"❌ WAV Info-Fehler: {e}")
            return None

# ===== MAIN ξ-FFT CLASS =====
class XiFFT:
    """
    Erweiterte ξ-FFT Implementation mit harmonischer Intelligenz
    
    Diese Klasse bietet fortgeschrittene Spektralanalyse mit:
    - Exakte harmonische Verhältnisse (Fraction-basiert)
    - Intelligente Frequenz-Suche basierend auf musikalischen Prinzipien
    - Optimierte Performance durch Priorisierung
    - Umfassende musikalische Analyse
    """
    
    def __init__(self, sample_rate: int = 44100, threshold: float = 0.005, 
                 resolution: str = 'medium', use_exact_ratios: bool = True):
        """
        Initialisiere ξ-FFT Analyzer
        
        Args:
            sample_rate: Abtastrate in Hz
            threshold: Minimum-Amplitude für Peak-Erkennung
            resolution: Frequenz-Auflösung ('ultra_high', 'high', 'medium', 'low', 'fast')
            use_exact_ratios: Verwende exakte Brüche für Verhältnisse
        """
        self.sample_rate = sample_rate
        self.threshold = threshold
        self.resolution = resolution
        self.use_exact_ratios = use_exact_ratios
        self.harmonic_db = HarmonicDatabase()
        
        # Auflösungseinstellungen
        self.resolution_map = {
            'ultra_high': 0.1,    # 0.1 Hz - Sehr genau aber langsam
            'high': 0.25,         # 0.25 Hz - Gut für präzise Analyse  
            'medium': 0.5,        # 0.5 Hz - Standard
            'low': 1.0,           # 1.0 Hz - Schnell für Überblick
            'fast': 2.0           # 2.0 Hz - Sehr schnell
        }
        
        print(f"🔬 XiFFT v{__version__} initialisiert:")
        print(f"   Sample Rate: {sample_rate} Hz")
        print(f"   Threshold: {threshold}")
        print(f"   Resolution: {resolution} ({self.resolution_map.get(resolution, 0.5)} Hz)")
        print(f"   Exakte Verhältnisse: {'✅' if use_exact_ratios else '❌'}")
    
    def analyze(self, signal: np.ndarray, freq_range: Tuple[int, int] = (20, 2000),
               progress_callback: Optional[Callable] = None, 
               min_amplitude: Optional[float] = None, max_amplitude: Optional[float] = None,
               f0_hint: Optional[float] = None, max_peaks: int = 100) -> Dict:
        """
        Hauptanalyse-Funktion mit intelligenter Strategie-Auswahl
        
        Args:
            signal: Eingangssignal als NumPy Array
            freq_range: Frequenzbereich (min_freq, max_freq) in Hz
            progress_callback: Callback-Funktion für Fortschritts-Updates
            min_amplitude: Minimum Amplitude Filter (optional)
            max_amplitude: Maximum Amplitude Filter (optional)
            f0_hint: Grundfrequenz-Hinweis für harmonische Intelligenz (optional)
            max_peaks: Maximale Anzahl zurückgegebener Peaks
            
        Returns:
            Dictionary mit Analyse-Ergebnissen
        """
        print(f"🔍 Starte ξ-FFT Analyse:")
        print(f"   Signal: {len(signal)} Samples ({len(signal)/self.sample_rate:.2f}s)")
        print(f"   Frequenzbereich: {freq_range[0]}-{freq_range[1]} Hz")
        print(f"   f₀-Hinweis: {f0_hint or 'Nicht verfügbar'}")
        
        if len(signal) == 0:
            return self._empty_result()
        
        # Preprocessing
        processed_signal = self._preprocess_signal(signal, min_amplitude, max_amplitude)
        
        # Strategische Analyse basierend auf verfügbaren Hinweisen
        if f0_hint and self.use_exact_ratios:
            print("🎼 Nutze harmonische Intelligenz-Strategie")
            peaks = self._harmonic_intelligent_analysis(processed_signal, f0_hint, freq_range, progress_callback)
        else:
            print("📊 Nutze Standard-Spektralanalyse")
            peaks = self._standard_spectral_analysis(processed_signal, freq_range, progress_callback)
        
        # Limitiere Peaks
        peaks = peaks[:max_peaks]
        
        # Berechne ξ-Verhältnisse
        if self.use_exact_ratios:
            xi_ratios = self._calculate_exact_xi_ratios(peaks)
        else:
            xi_ratios = self._calculate_standard_xi_ratios(peaks)
        
        # Erweiterte Analysen
        musical_analysis = self._analyze_musical_structure(xi_ratios) if self.use_exact_ratios else {}
        statistical_analysis = self._calculate_signal_statistics(processed_signal)
        
        # Zusammenstellung der Ergebnisse
        result = {
            'peaks': peaks,
            'xiRatios': xi_ratios,
            'peakCount': len(peaks),
            'dominantXi': xi_ratios[0] if xi_ratios else None,
            
            # Konfiguration
            'sampleRate': self.sample_rate,
            'resolution': self.resolution,
            'threshold': self.threshold,
            'useExactRatios': self.use_exact_ratios,
            
            # Eingabe-Parameter
            'signalLength': len(signal),
            'duration': len(signal) / self.sample_rate,
            'freqRange': freq_range,
            'f0Hint': f0_hint,
            
            # Filter-Status
            'amplitudeFiltered': min_amplitude is not None or max_amplitude is not None,
            'minAmplitude': min_amplitude,
            'maxAmplitude': max_amplitude,
            
            # Erweiterte Analysen
            'musicalAnalysis': musical_analysis,
            'statisticalAnalysis': statistical_analysis,
            
            # Metadaten
            'analysisTimestamp': None,  # Könnte mit datetime gefüllt werden
            'version': __version__
        }
        
        print(f"✅ ξ-FFT Analyse abgeschlossen:")
        print(f"   {len(peaks)} Peaks gefunden")
        print(f"   {len(xi_ratios)} ξ-Verhältnisse berechnet")
        if musical_analysis:
            print(f"   Muster: {musical_analysis.get('pattern', 'Unbekannt')}")
        
        return result
    
    def _empty_result(self) -> Dict:
        """Returne leeres Ergebnis für ungültige Eingaben"""
        return {
            'peaks': [], 'xiRatios': [], 'peakCount': 0, 'dominantXi': None,
            'musicalAnalysis': {}, 'statisticalAnalysis': {},
            'error': 'Empty or invalid signal'
        }
    
    def _preprocess_signal(self, signal: np.ndarray, min_amp: Optional[float], max_amp: Optional[float]) -> np.ndarray:
        """
        Signal-Preprocessing: Amplituden-Filter und Längen-Begrenzung
        """
        processed = signal.copy()
        
        # Amplituden-Filter
        if min_amp is not None:
            processed = np.where(np.abs(processed) >= min_amp, processed, 0)
            print(f"🔧 Min-Amplituden-Filter angewendet: {min_amp}")
        
        if max_amp is not None:
            processed = np.clip(processed, -max_amp, max_amp)
            print(f"🔧 Max-Amplituden-Filter angewendet: {max_amp}")
        
        # Längen-Begrenzung für Performance (max 4 Sekunden)
        max_samples = self.sample_rate * 4
        if len(processed) > max_samples:
            processed = processed[:max_samples]
            print(f"⚡ Signal begrenzt auf {len(processed)} Samples ({len(processed)/self.sample_rate:.1f}s)")
        
        return processed
    
    def _harmonic_intelligent_analysis(self, signal: np.ndarray, f0_hint: float, 
                                     freq_range: Tuple[int, int], progress_callback: Optional[Callable]) -> List[Dict]:
        """
        Intelligente harmonische Analyse basierend auf f₀-Hinweis
        """
        peaks = []
        min_freq, max_freq = freq_range
        
        print(f"🎵 Harmonische Intelligenz um f₀={f0_hint} Hz")
        
        # Teste priorisierte harmonische Verhältnisse
        total_tests = len(self.harmonic_db.PRIORITY_RATIOS)
        processed = 0
        
        for ratio_exact in self.harmonic_db.PRIORITY_RATIOS:
            # Berechne Zielfrequenz
            target_freq = f0_hint * float(ratio_exact)
            
            # Prüfe Frequenzbereich
            if min_freq <= target_freq <= max_freq:
                
                # Hochauflösende Suche in ±3Hz Bereich
                best_magnitude = 0
                best_freq = target_freq
                
                search_resolution = 0.05  # 50mHz für höchste Präzision
                test_range = np.arange(target_freq - 3, target_freq + 3, search_resolution)
                
                for test_freq in test_range:
                    magnitude = self._calculate_magnitude(signal, test_freq)
                    if magnitude > best_magnitude:
                        best_magnitude = magnitude
                        best_freq = test_freq
                
                # Hole Intervall-Info
                interval_info = self.harmonic_db.get_interval_info(ratio_exact)
                
                # Adaptiver Threshold
                if interval_info:
                    threshold_factor = (100 - interval_info['probability']) / 100
                    threshold_adapted = self.threshold * (0.1 + 0.9 * threshold_factor)
                else:
                    threshold_adapted = self.threshold
                
                if best_magnitude > threshold_adapted:
                    peak_data = {
                        'frequency': round(best_freq, 3),
                        'magnitude': best_magnitude,
                        'magnitudeDB': 20 * math.log10(best_magnitude + 1e-10),
                        'base_freq': f0_hint,
                        'is_harmonic_match': True
                    }
                    
                    if interval_info:
                        peak_data.update({
                            'ratio_exact': ratio_exact,
                            'interval_name': interval_info['name'],
                            'interval_category': interval_info['category'],
                            'is_consonant': interval_info['is_consonant'],
                            'interval_cents': interval_info['cents']
                        })
                    
                    peaks.append(peak_data)
                    print(f"  ✅ {interval_info['name'] if interval_info else 'Unknown'}: {best_freq:.2f} Hz")
            
            processed += 1
            if progress_callback and processed % 3 == 0:
                progress = int((processed / total_tests) * 70)  # 70% für harmonische Analyse
                progress_callback(progress, f"Harmonisch: {interval_info['name'] if interval_info else 'Test'}")
        
        # Ergänzende Breitband-Suche für nicht-harmonische Peaks
        additional_peaks = self._find_additional_peaks(signal, freq_range, peaks, progress_callback)
        peaks.extend(additional_peaks)
        
        # Sortiere nach Magnitude
        peaks.sort(key=lambda x: x['magnitude'], reverse=True)
        return peaks
    
    def _find_additional_peaks(self, signal: np.ndarray, freq_range: Tuple[int, int], 
                             existing_peaks: List[Dict], progress_callback: Optional[Callable]) -> List[Dict]:
        """
        Ergänzende Breitband-Suche für nicht-harmonische Peaks
        """
        additional_peaks = []
        min_freq, max_freq = freq_range
        
        # Bereits abgedeckte Frequenz-Bereiche (±4Hz Ausschluss)
        excluded_ranges = []
        for peak in existing_peaks:
            excluded_ranges.append((peak['frequency'] - 4, peak['frequency'] + 4))
        
        # Grobsuche mit Standard-Auflösung
        step_size = self.resolution_map.get(self.resolution, 0.5)
        test_freqs = np.arange(min_freq, max_freq, step_size * 2)  # Gröbere Suche
        
        for i, freq in enumerate(test_freqs):
            # Prüfe Ausschluss-Bereiche
            is_excluded = any(start <= freq <= end for start, end in excluded_ranges)
            
            if not is_excluded:
                magnitude = self._calculate_magnitude(signal, freq)
                
                if magnitude > self.threshold:
                    additional_peaks.append({
                        'frequency': round(freq, 2),
                        'magnitude': magnitude,
                        'magnitudeDB': 20 * math.log10(magnitude + 1e-10),
                        'is_harmonic_match': False
                    })
            
            # Progress update (30% für ergänzende Suche)
            if progress_callback and i % 50 == 0:
                progress = 70 + int((i / len(test_freqs)) * 30)
                progress_callback(progress, f"Zusätzlich: {freq:.0f} Hz")
        
        print(f"  📊 {len(additional_peaks)} zusätzliche Peaks gefunden")
        return additional_peaks
    
    def _standard_spectral_analysis(self, signal: np.ndarray, freq_range: Tuple[int, int],
                                   progress_callback: Optional[Callable]) -> List[Dict]:
        """
        Standard-Spektralanalyse ohne harmonische Vorannahmen
        """
        peaks = []
        min_freq, max_freq = freq_range
        step_size = self.resolution_map.get(self.resolution, 0.5)
        
        test_freqs = np.arange(min_freq, max_freq, step_size)
        total_tests = len(test_freqs)
        
        print(f"📊 Standard-Analyse: {total_tests} Frequenzen, Schritt {step_size} Hz")
        
        for i, freq in enumerate(test_freqs):
            magnitude = self._calculate_magnitude(signal, freq)
            
            if magnitude > self.threshold:
                peaks.append({
                    'frequency': round(freq, 2),
                    'magnitude': magnitude,
                    'magnitudeDB': 20 * math.log10(magnitude + 1e-10),
                    'is_harmonic_match': False
                })
            
            # Progress updates
            if progress_callback and i % 100 == 0:
                progress = int((i / total_tests) * 100)
                progress_callback(progress, f"Spektrum: {freq:.1f} Hz ({len(peaks)} Peaks)")
        
        # Sortiere nach Magnitude
        peaks.sort(key=lambda x: x['magnitude'], reverse=True)
        print(f"📊 {len(peaks)} Peaks in Standard-Analyse gefunden")
        return peaks
    
    def _calculate_magnitude(self, signal: np.ndarray, frequency: float) -> float:
        """
        Berechne Magnitude für spezifische Frequenz mittels DFT
        
        Args:
            signal: Eingangssignal
            frequency: Zielfrequenz in Hz
            
        Returns:
            Magnitude der Frequenz-Komponente
        """
        N = len(signal)
        real = imag = 0.0
        
        # Optimierte DFT-Berechnung
        angle_step = -2 * math.pi * frequency / self.sample_rate
        
        for n in range(N):
            angle = angle_step * n
            cos_val = math.cos(angle)
            sin_val = math.sin(angle)
            
            sample_val = float(signal[n])
            real += sample_val * cos_val
            imag += sample_val * sin_val
        
        # Magnitude-Berechnung und Normalisierung
        magnitude = math.sqrt(real * real + imag * imag) * 2 / N
        return magnitude
    
    def _calculate_exact_xi_ratios(self, peaks: List[Dict]) -> List[Dict]:
        """
        Berechne ξ-Verhältnisse mit exakten Brüchen und harmonischer Klassifikation
        """
        ratios = []
        
        # Alle Peak-Paare untersuchen
        for i in range(len(peaks)):
            for j in range(i + 1, len(peaks)):
                f1, f2 = peaks[i]['frequency'], peaks[j]['frequency']
                
                # Versuche exaktes harmonisches Verhältnis zu finden
                ratio_exact = self.harmonic_db.frequency_to_exact_ratio(f1, f2, tolerance=0.03)
                
                ratio_data = {
                    'freqHigh': max(f1, f2),
                    'freqLow': min(f1, f2),
                    'xiRatio': round(max(f1, f2) / min(f1, f2), 6),
                    'significance': peaks[i]['magnitude'] * peaks[j]['magnitude'],
                    'peakIndices': [i, j]
                }
                
                if ratio_exact:
                    # Exaktes harmonisches Verhältnis gefunden
                    interval_info = self.harmonic_db.get_interval_info(ratio_exact)
                    
                    ratio_data.update({
                        'xiRatioExact': ratio_exact,
                        'intervalName': interval_info['name'],
                        'intervalCategory': interval_info['category'],
                        'isConsonant': interval_info['is_consonant'],
                        'complexity': interval_info['complexity'],
                        'intervalCents': interval_info['cents'],
                        'isMicrotone': interval_info['is_microtone'],
                        'isExactMatch': True
                    })
                else:
                    # Kein exaktes Verhältnis - Fallback
                    ratio_data.update({
                        'xiRatioExact': None,
                        'intervalName': 'Unharmonisch',
                        'intervalCategory': 'Non-harmonic',
                        'isConsonant': False,
                        'complexity': 999,
                        'intervalCents': 1200 * math.log2(ratio_data['xiRatio']),
                        'isMicrotone': False,
                        'isExactMatch': False
                    })
                
                ratios.append(ratio_data)
        
        # Intelligente Sortierung: Exakte harmonische Verhältnisse zuerst
        ratios.sort(key=lambda x: (
            not x['isExactMatch'],     # Exakte zuerst
            x['complexity'],           # Dann nach Einfachheit
            not x['isConsonant'],      # Konsonante bevorzugt
            -x['significance']         # Höchste Significance zuerst
        ))
        
        return ratios[:50]  # Top 50 Verhältnisse
    
    def _calculate_standard_xi_ratios(self, peaks: List[Dict]) -> List[Dict]:
        """
        Standard ξ-Verhältnis-Berechnung ohne exakte Brüche (Fallback)
        """
        ratios = []
        
        for i in range(len(peaks)):
            for j in range(i + 1, len(peaks)):
                f1, f2 = peaks[i]['frequency'], peaks[j]['frequency']
                xi_ratio = max(f1, f2) / min(f1, f2)
                
                ratios.append({
                    'freqHigh': max(f1, f2),
                    'freqLow': min(f1, f2),
                    'xiRatio': round(xi_ratio, 6),
                    'significance': peaks[i]['magnitude'] * peaks[j]['magnitude'],
                    'isExactMatch': False,
                    'intervalName': self._classify_float_ratio(xi_ratio)
                })
        
        ratios.sort(key=lambda x: -x['significance'])
        return ratios[:30]
    
    def _classify_float_ratio(self, ratio: float) -> str:
        """Klassifiziere Float-Verhältnis zu musikalischem Intervall (Näherung)"""
        if abs(ratio - 1.0) < 0.01:
            return "~Unison"
        elif abs(ratio - 2.0) < 0.05:
            return "~Oktave"
        elif abs(ratio - 1.5) < 0.03:
            return "~Quinte"
        elif abs(ratio - 1.333) < 0.03:
            return "~Quarte"
        elif abs(ratio - 1.25) < 0.02:
            return "~Große Terz"
        elif abs(ratio - 1.2) < 0.02:
            return "~Kleine Terz"
        elif 1.01 < ratio < 1.1:
            return "~Schwebung"
        else:
            return "Unklassifiziert"
    
    def _analyze_musical_structure(self, xi_ratios: List[Dict]) -> Dict:
        """
        Umfassende musikalische Struktur-Analyse
        """
        exact_ratios = [r['xiRatioExact'] for r in xi_ratios if r.get('xiRatioExact')]
        
        if not exact_ratios:
            return {'pattern': 'Keine harmonischen Strukturen', 'harmonicity': 'Sehr niedrig'}
        
        # Muster-Erkennung
        pattern = self.harmonic_db.detect_musical_pattern(exact_ratios)
        
        # Kategorie-Analyse
        categories = {}
        consonant_count = 0
        microtone_count = 0
        
        for ratio_data in xi_ratios:
            if ratio_data.get('isExactMatch'):
                cat = ratio_data.get('intervalCategory', 'Unknown')
                categories[cat] = categories.get(cat, 0) + 1
                
                if ratio_data.get('isConsonant'):
                    consonant_count += 1
                if ratio_data.get('isMicrotone'):
                    microtone_count += 1
        
        total_exact = len(exact_ratios)
        consonance_ratio = consonant_count / total_exact if total_exact > 0 else 0
        
        # Harmonizitäts-Bewertung
        if consonance_ratio > 0.8:
            harmonicity = 'Sehr hoch'
        elif consonance_ratio > 0.6:
            harmonicity = 'Hoch'
        elif consonance_ratio > 0.4:
            harmonicity = 'Mittel'
        elif consonance_ratio > 0.2:
            harmonicity = 'Niedrig'
        else:
            harmonicity = 'Sehr niedrig'
        
        return {
            'pattern': pattern,
            'categories': categories,
            'exactRatioCount': total_exact,
            'consonantRatioCount': consonant_count,
            'microtoneCount': microtone_count,
            'consonanceRatio': round(consonance_ratio, 3),
            'harmonicity': harmonicity,
            'complexity_avg': sum(r.get('complexity', 999) for r in xi_ratios if r.get('isExactMatch')) / max(total_exact, 1)
        }
    
    def _calculate_signal_statistics(self, signal: np.ndarray) -> Dict:
        """
        Berechne grundlegende Signal-Statistiken
        """
        return {
            'length': len(signal),
            'duration': len(signal) / self.sample_rate,
            'rms': float(np.sqrt(np.mean(signal**2))),
            'peak': float(np.max(np.abs(signal))),
            'mean': float(np.mean(signal)),
            'std': float(np.std(signal)),
            'dynamic_range_db': 20 * math.log10(np.max(np.abs(signal)) / (np.std(signal) + 1e-10))
        }

# ===== CONVENIENCE FUNCTIONS =====
def quick_analysis(signal: np.ndarray, sample_rate: int = 44100, 
                  freq_range: Tuple[int, int] = (20, 2000),
                  f0_hint: Optional[float] = None) -> Dict:
    """
    Schnelle ξ-FFT Analyse mit Standard-Parametern
    
    Args:
        signal: Audio-Signal
        sample_rate: Abtastrate
        freq_range: Frequenzbereich
        f0_hint: Optional Grundfrequenz-Hinweis
        
    Returns:
        Analyse-Ergebnisse
    """
    xi_fft = XiFFT(sample_rate=sample_rate)
    return xi_fft.analyze(signal, freq_range=freq_range, f0_hint=f0_hint)

def analyze_beating_signal(f0: float, delta_f: float, duration: float = 3.0,
                          sample_rate: int = 44100) -> Dict:
    """
    Generiere und analysiere Schwebungs-Signal in einem Aufruf
    
    Args:
        f0: Grundfrequenz
        delta_f: Schwebungsfrequenz
        duration: Signal-Dauer
        sample_rate: Abtastrate
        
    Returns:
        Vollständige Analyse des Schwebungs-Signals
    """
    # Generiere Signal
    signal = SignalGenerator.create_beating_signal(f0, delta_f, duration, sample_rate)
    
    # Analysiere mit harmonischer Intelligenz
    xi_fft = XiFFT(sample_rate=sample_rate, use_exact_ratios=True)
    result = xi_fft.analyze(signal, f0_hint=f0)
    
    # Füge Generator-Info hinzu
    result['generated_signal'] = {
        'f0': f0, 'delta_f': delta_f, 'duration': duration,
        'expected_frequencies': [f0 - delta_f, f0, f0 + delta_f]
    }
    
    return result

def batch_analyze_files(file_paths: List[str], **kwargs) -> List[Dict]:
    """
    Batch-Analyse mehrerer WAV-Dateien
    
    Args:
        file_paths: Liste der WAV-Datei-Pfade
        **kwargs: Parameter für XiFFT.analyze()
        
    Returns:
        Liste der Analyse-Ergebnisse
    """
    results = []
    xi_fft = XiFFT()
    
    for file_path in file_paths:
        print(f"📁 Analysiere: {file_path}")
        signal, sample_rate = WAVUtils.load_wav(file_path)
        
        if signal is not None:
            xi_fft.sample_rate = sample_rate
            result = xi_fft.analyze(signal, **kwargs)
            result['source_file'] = file_path
            results.append(result)
        else:
            results.append({'error': f'Konnte {file_path} nicht laden', 'source_file': file_path})
    
    return results

# ===== EXPORT FUNCTIONS =====
def export_analysis_to_text(analysis_result: Dict, filename: str) -> bool:
    """
    Exportiere Analyse-Ergebnisse als formatierte Text-Datei
    
    Args:
        analysis_result: Ergebnis von XiFFT.analyze()
        filename: Ausgabe-Dateiname
        
    Returns:
        True bei Erfolg
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write(f"ξ-FFT ANALYSE BERICHT v{__version__}\n")
            f.write("=" * 60 + "\n\n")
            
            # Signal-Info
            f.write("SIGNAL-INFORMATIONEN:\n")
            f.write("-" * 30 + "\n")
            f.write(f"Länge: {analysis_result.get('signalLength', 'N/A')} Samples\n")
            f.write(f"Dauer: {analysis_result.get('duration', 'N/A'):.3f} s\n")
            f.write(f"Sample Rate: {analysis_result.get('sampleRate', 'N/A')} Hz\n")
            f.write(f"Frequenzbereich: {analysis_result.get('freqRange', 'N/A')}\n\n")
            
            # Peaks
            f.write("DETEKTIERTE FREQUENZEN:\n")
            f.write("-" * 30 + "\n")
            for i, peak in enumerate(analysis_result.get('peaks', [])[:20], 1):
                harmonic_info = ""
                if peak.get('is_harmonic_match') and peak.get('interval_name'):
                    harmonic_info = f" [{peak['interval_name']}]"
                
                f.write(f"{i:2d}. {peak['frequency']:8.2f} Hz  "
                       f"Mag: {peak['magnitude']:8.4f}  "
                       f"dB: {peak['magnitudeDB']:+6.1f}{harmonic_info}\n")
            
            # ξ-Verhältnisse
            f.write(f"\nξ-VERHÄLTNISSE (Top 15):\n")
            f.write("-" * 40 + "\n")
            for i, ratio in enumerate(analysis_result.get('xiRatios', [])[:15], 1):
                interval_info = ""
                if ratio.get('isExactMatch'):
                    interval_info = f" [{ratio.get('intervalName', 'Unknown')}]"
                    if ratio.get('isConsonant'):
                        interval_info += " ♪"
                
                f.write(f"{i:2d}. ξ({ratio['freqHigh']:7.2f}/{ratio['freqLow']:7.2f}) = "
                       f"{ratio['xiRatio']:8.4f}{interval_info}\n")
            
            # Musikalische Analyse
            if 'musicalAnalysis' in analysis_result:
                musical = analysis_result['musicalAnalysis']
                f.write(f"\nMUSIKALISCHE ANALYSE:\n")
                f.write("-" * 30 + "\n")
                f.write(f"Muster: {musical.get('pattern', 'Unbekannt')}\n")
                f.write(f"Harmonizität: {musical.get('harmonicity', 'Unbekannt')}\n")
                f.write(f"Konsonanz-Ratio: {musical.get('consonanceRatio', 0):.1%}\n")
                f.write(f"Exakte Verhältnisse: {musical.get('exactRatioCount', 0)}\n")
        
        print(f"📄 Analyse-Bericht exportiert: {filename}")
        return True
        
    except Exception as e:
        print(f"❌ Export-Fehler: {e}")
        return False

# ===== MAIN DEMO =====
if __name__ == "__main__":
    print(f"🎵 ξ-FFT Library v{__version__} - Demonstration")
    print("=" * 60)
    
    # Demo 1: Schwebungs-Analyse
    print("\n1. SCHWEBUNGS-SIGNAL ANALYSE:")
    print("-" * 40)
    
    result = analyze_beating_signal(f0=440, delta_f=5, duration=2)
    
    print(f"Peaks gefunden: {result['peakCount']}")
    print(f"Muster: {result['musicalAnalysis'].get('pattern', 'Unbekannt')}")
    print(f"Harmonizität: {result['musicalAnalysis'].get('harmonicity', 'Unbekannt')}")
    
    # Zeige Top-5 Peaks
    print("\nTop-5 Frequenzen:")
    for i, peak in enumerate(result['peaks'][:5], 1):
        interval = peak.get('interval_name', 'Unknown')
        print(f"  {i}. {peak['frequency']:.2f} Hz - {interval}")
    
    # Demo 2: Harmonische Reihe
    print("\n2. HARMONISCHE REIHE ANALYSE:")
    print("-" * 40)
    
    harmonic_signal = SignalGenerator.create_harmonic_series(
        fundamental=220,  # A3
        harmonics=[1, 2, 3, 4, 5],
        duration=2
    )
    
    harmonic_result = quick_analysis(harmonic_signal, f0_hint=220)
    print(f"Harmonische Peaks: {harmonic_result['peakCount']}")
    print(f"Muster: {harmonic_result['musicalAnalysis'].get('pattern', 'Unbekannt')}")
    
    # Demo 3: WAV Export
    print("\n3. WAV EXPORT DEMO:")
    print("-" * 40)
    
    chord_signal = SignalGenerator.create_chord([261.63, 329.63, 392.00])  # C-Dur
    success = WAVUtils.save_wav(chord_signal, "demo_chord.wav")
    
    if success:
        print("✅ C-Dur Akkord als demo_chord.wav gespeichert")
    
    print(f"\n🎵 ξ-FFT Library Demo abgeschlossen!")
    print("Nutzen Sie 'from xi_fft_library import *' für eigene Projekte.")
