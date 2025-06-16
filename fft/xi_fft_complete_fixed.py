"""
ξ-FFT Schwebungs-Analyse - Windows GUI Version mit exakten Verhältnissen
KORRIGIERTE UND VOLLSTÄNDIGE VERSION

Abhängigkeiten:
pip install numpy matplotlib

Verwendung:
python xi_fft_complete.py
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import math
import wave
import threading
import time
import os
import sys
from fractions import Fraction

# ===== EXACT HARMONIC RATIOS DATABASE =====
class HarmonicRatioDatabase:
    """Datenbank für exakte musikalische Verhältnisse"""
    
    def __init__(self):
        # Exakte musikalische Intervalle (sortiert nach Einfachheit)
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
            
            # Häufige Ganztöne:
            Fraction(9, 8):   ("Großer Ganzton",   60,  "Dissonant", 4),
            Fraction(10, 9):  ("Kleiner Ganzton",  55,  "Dissonant", 4),
            
            # Halbtöne:
            Fraction(16, 15): ("Kleiner Halbton",  50,  "Dissonant", 5),
            Fraction(25, 24): ("Chromatischer HT", 45,  "Dissonant", 5),
            
            # Septimen:
            Fraction(15, 8):  ("Große Septime",    40,  "Dissonant", 4),
            Fraction(16, 9):  ("Kleine Septime",   35,  "Dissonant", 4),
            
            # Harmonische Obertöne:
            Fraction(7, 4):   ("Harmonische 7te",  30,  "Complex", 6),
            Fraction(9, 4):   ("Harmonische 9te",  25,  "Complex", 6),
            Fraction(11, 8):  ("Harmonische 11te", 20,  "Complex", 7),
            Fraction(13, 8):  ("Harmonische 13te", 15,  "Complex", 7),
            
            # Schwebungs-relevante kleine Intervalle:
            Fraction(81, 80): ("Syntonisches Komma", 10, "Microtone", 8),
            Fraction(256, 243): ("Limma",            8,  "Microtone", 8),
        }
        
        # Sortiert nach Priorität (Einfachheit + Wahrscheinlichkeit)
        self.PRIORITY_RATIOS = sorted(
            self.EXACT_INTERVALS.keys(),
            key=lambda r: (self.EXACT_INTERVALS[r][3], -self.EXACT_INTERVALS[r][1])
        )
        
        print(f"🎼 Harmonic Database: {len(self.EXACT_INTERVALS)} exakte Intervalle geladen")
    
    def get_interval_info(self, ratio_exact):
        """Hole Informationen über musikalisches Intervall"""
        if ratio_exact in self.EXACT_INTERVALS:
            name, probability, category, priority = self.EXACT_INTERVALS[ratio_exact]
            return {
                'name': name,
                'probability': probability,
                'category': category,
                'priority': priority,
                'complexity': ratio_exact.numerator + ratio_exact.denominator,
                'is_consonant': category in ["Perfect", "Consonant"]
            }
        return None
    
    def frequency_to_exact_ratio(self, f1, f2, tolerance=0.02):
        """Konvertiere Frequenz-Verhältnis zu exaktem Bruch"""
        ratio_float = max(f1, f2) / min(f1, f2)
        
        # Suche in bekannten Intervallen:
        for exact_ratio in self.PRIORITY_RATIOS:
            if abs(float(exact_ratio) - ratio_float) < tolerance:
                return exact_ratio
        
        # Automatische Bruch-Approximation für unbekannte Verhältnisse:
        approx_fraction = Fraction(ratio_float).limit_denominator(max_denominator=32)
        
        # Nur wenn einfach genug:
        if approx_fraction.denominator <= 16 and approx_fraction.numerator + approx_fraction.denominator <= 20:
            return approx_fraction
        
        return None
    
    def detect_musical_pattern(self, exact_ratios):
        """Erkenne musikalische Muster in den Verhältnissen"""
        ratio_set = set(exact_ratios)
        
        # Dur-Dreiklang: 1:5/4:3/2
        major_triad = {Fraction(1,1), Fraction(5,4), Fraction(3,2)}
        
        # Moll-Dreiklang: 1:6/5:3/2  
        minor_triad = {Fraction(1,1), Fraction(6,5), Fraction(3,2)}
        
        # Dominantseptakkord: 1:5/4:3/2:7/4
        dom7_chord = {Fraction(1,1), Fraction(5,4), Fraction(3,2), Fraction(7,4)}
        
        if major_triad.issubset(ratio_set):
            return "Dur-Dreiklang"
        elif minor_triad.issubset(ratio_set):
            return "Moll-Dreiklang"
        elif dom7_chord.issubset(ratio_set):
            return "Dominantseptakkord"
        elif Fraction(2,1) in ratio_set:
            return "Oktav-Struktur"
        elif Fraction(3,2) in ratio_set:
            return "Quinten-Struktur"
        
        return "Unbekanntes Muster"

# Globale Instanz
HARMONIC_DB = HarmonicRatioDatabase()

# ===== ξ-FFT LIBRARY =====
class XiFFT:
    """Erweiterte ξ-FFT Implementation mit exakten Verhältnissen"""
    
    def __init__(self, sample_rate=44100, threshold=0.005, resolution='medium', use_exact_ratios=True):
        self.sample_rate = sample_rate
        self.threshold = threshold
        self.resolution = resolution
        self.use_exact_ratios = use_exact_ratios
        self.harmonic_db = HARMONIC_DB
        print(f"🔬 XiFFT initialisiert: {sample_rate} Hz, Threshold: {threshold}, Resolution: {resolution}, Exakte Verhältnisse: {use_exact_ratios}")
    
    def analyze(self, signal, freq_range=(20, 2000), progress_callback=None, min_amplitude=None, max_amplitude=None, f0_hint=None):
        """Analysiere Signal mit intelligenter Harmonie-Suche"""
        print(f"🔍 Starte Analyse: {len(signal)} Samples, Bereich: {freq_range}")
        
        if len(signal) == 0:
            return {'peaks': [], 'xiRatios': [], 'peakCount': 0}
        
        # Amplituden-Filter anwenden
        if min_amplitude is not None or max_amplitude is not None:
            signal = self._filter_by_amplitude(signal, min_amplitude, max_amplitude)
            print(f"🔧 Amplituden-Filter angewendet: min={min_amplitude}, max={max_amplitude}")
        
        # Intelligente Analyse-Strategie basierend auf Hinweisen
        if f0_hint and self.use_exact_ratios:
            print(f"🎼 Nutze harmonische Intelligenz mit f₀={f0_hint} Hz")
            peaks = self._harmonic_intelligent_analysis(signal, f0_hint, freq_range, progress_callback)
        else:
            # Fallback: Standard-Analyse mit Optimierungen
            peaks = self._optimized_peak_analysis(signal, freq_range, progress_callback)
        
        # Berechne ξ-Verhältnisse mit exakten Brüchen
        if self.use_exact_ratios:
            xi_ratios = self._calculate_exact_xi_ratios(peaks)
        else:
            xi_ratios = self._calculate_xi_ratios(peaks)
        
        # Erweiterte Analyse
        musical_analysis = self._analyze_musical_structure(xi_ratios) if self.use_exact_ratios else {}
        
        result = {
            'peaks': peaks,
            'xiRatios': xi_ratios,
            'peakCount': len(peaks),
            'dominantXi': xi_ratios[0] if xi_ratios else None,
            'resolution': self.resolution,
            'amplitudeFiltered': min_amplitude is not None or max_amplitude is not None,
            'useExactRatios': self.use_exact_ratios,
            'musicalAnalysis': musical_analysis,
            'f0Hint': f0_hint
        }
        
        print(f"✅ Analyse abgeschlossen: {len(peaks)} Peaks, {len(xi_ratios)} ξ-Ratios")
        return result
    
    def _harmonic_intelligent_analysis(self, signal, f0_hint, freq_range, progress_callback):
        """Intelligente Analyse basierend auf harmonischen Verhältnissen"""
        peaks = []
        min_freq, max_freq = freq_range
        
        print(f"🎵 Harmonische Suche um f₀={f0_hint} Hz")
        
        # Teste priorisierte harmonische Verhältnisse
        total_tests = len(self.harmonic_db.PRIORITY_RATIOS)
        processed = 0
        
        for ratio_exact in self.harmonic_db.PRIORITY_RATIOS:
            # Berechne Zielfrequenz
            target_freq = f0_hint * float(ratio_exact)
            
            # Prüfe ob im gewünschten Frequenzbereich
            if min_freq <= target_freq <= max_freq:
                
                # Teste mit hoher Präzision in kleinem Bereich (±2Hz)
                best_magnitude = 0
                best_freq = target_freq
                
                test_range = np.arange(target_freq - 2, target_freq + 2, 0.1)
                for test_freq in test_range:
                    magnitude = self._calculate_magnitude(signal, test_freq)
                    if magnitude > best_magnitude:
                        best_magnitude = magnitude
                        best_freq = test_freq
                
                # Hole Intervall-Info
                interval_info = self.harmonic_db.get_interval_info(ratio_exact)
                
                # Adaptiver Threshold basierend auf Wahrscheinlichkeit
                threshold_adapted = self.threshold * (100 - interval_info['probability']) / 100
                
                if best_magnitude > threshold_adapted:
                    peaks.append({
                        'frequency': round(best_freq, 2),
                        'magnitude': best_magnitude,
                        'magnitudeDB': 20 * math.log10(best_magnitude + 1e-10),
                        'ratio_exact': ratio_exact,
                        'interval_name': interval_info['name'],
                        'interval_category': interval_info['category'],
                        'base_freq': f0_hint,
                        'is_harmonic_match': True
                    })
                    
                    print(f"  ✅ {interval_info['name']}: {best_freq:.1f} Hz (Magnitude: {best_magnitude:.4f})")
            
            processed += 1
            if progress_callback and processed % 5 == 0:
                progress = int((processed / total_tests) * 100)
                progress_callback(progress, f"Harmonische Analyse: {interval_info['name'] if interval_info else 'Unknown'}")
        
        # Ergänze mit Standard-Analyse für nicht-harmonische Peaks
        additional_peaks = self._find_additional_peaks(signal, freq_range, peaks, progress_callback)
        peaks.extend(additional_peaks)
        
        # Sortiere nach Magnitude
        peaks.sort(key=lambda x: x['magnitude'], reverse=True)
        return peaks[:100]  # Top 100
    
    def _find_additional_peaks(self, signal, freq_range, existing_peaks, progress_callback):
        """Finde zusätzliche Peaks die nicht harmonisch erklärt werden können"""
        additional_peaks = []
        min_freq, max_freq = freq_range
        
        # Bereits gefundene Frequenzen (±5Hz Ausschlussbereich)
        excluded_ranges = []
        for peak in existing_peaks:
            excluded_ranges.append((peak['frequency'] - 5, peak['frequency'] + 5))
        
        # Grobsuche in nicht-abgedeckten Bereichen
        step_size = 2.0  # Gröbere Suche für Ergänzung
        test_freqs = np.arange(min_freq, max_freq, step_size)
        
        for i, freq in enumerate(test_freqs):
            # Prüfe ob Frequenz bereits abgedeckt
            is_excluded = any(start <= freq <= end for start, end in excluded_ranges)
            
            if not is_excluded:
                magnitude = self._calculate_magnitude(signal, freq)
                
                if magnitude > self.threshold:
                    additional_peaks.append({
                        'frequency': round(freq, 1),
                        'magnitude': magnitude,
                        'magnitudeDB': 20 * math.log10(magnitude + 1e-10),
                        'is_harmonic_match': False
                    })
            
            # Progress update
            if progress_callback and i % 100 == 0:
                progress = 50 + int((i / len(test_freqs)) * 50)  # 50-100%
                progress_callback(progress, f"Zusätzliche Peaks: {freq:.0f} Hz")
        
        print(f"  📊 {len(additional_peaks)} zusätzliche Peaks gefunden")
        return additional_peaks
    
    def _calculate_exact_xi_ratios(self, peaks):
        """Berechne ξ-Verhältnisse mit exakten Brüchen"""
        ratios = []
        
        for i in range(len(peaks)):
            for j in range(i + 1, len(peaks)):
                f1, f2 = peaks[i]['frequency'], peaks[j]['frequency']
                
                # Versuche exaktes Verhältnis zu finden
                ratio_exact = self.harmonic_db.frequency_to_exact_ratio(f1, f2)
                
                if ratio_exact:
                    # Exaktes harmonisches Verhältnis gefunden
                    interval_info = self.harmonic_db.get_interval_info(ratio_exact)
                    
                    ratios.append({
                        'freqHigh': max(f1, f2),
                        'freqLow': min(f1, f2),
                        'xiRatio': round(float(ratio_exact), 6),
                        'xiRatioExact': ratio_exact,
                        'intervalName': interval_info['name'] if interval_info else 'Unbekannt',
                        'intervalCategory': interval_info['category'] if interval_info else 'Unknown',
                        'isConsonant': interval_info['is_consonant'] if interval_info else False,
                        'complexity': interval_info['complexity'] if interval_info else 999,
                        'significance': peaks[i]['magnitude'] * peaks[j]['magnitude'],
                        'isExactMatch': True
                    })
                else:
                    # Fallback: Gleitkomma-Verhältnis
                    xi_float = max(f1, f2) / min(f1, f2)
                    ratios.append({
                        'freqHigh': max(f1, f2),
                        'freqLow': min(f1, f2),
                        'xiRatio': round(xi_float, 6),
                        'xiRatioExact': None,
                        'intervalName': 'Unharmonisch',
                        'intervalCategory': 'Non-harmonic',
                        'isConsonant': False,
                        'complexity': 999,
                        'significance': peaks[i]['magnitude'] * peaks[j]['magnitude'],
                        'isExactMatch': False
                    })
        
        # Sortiere: Exakte harmonische Verhältnisse zuerst, dann nach Bedeutung
        ratios.sort(key=lambda x: (not x['isExactMatch'], x['complexity'], -x['significance']))
        return ratios[:50]  # Top 50
    
    def _analyze_musical_structure(self, xi_ratios):
        """Analysiere musikalische Struktur basierend auf exakten Verhältnissen"""
        exact_ratios = [r['xiRatioExact'] for r in xi_ratios if r['xiRatioExact']]
        
        if not exact_ratios:
            return {'pattern': 'Keine harmonischen Strukturen erkannt'}
        
        # Erkenne Muster
        pattern = self.harmonic_db.detect_musical_pattern(exact_ratios)
        
        # Zähle Kategorien
        categories = {}
        for ratio_data in xi_ratios:
            if ratio_data['isExactMatch']:
                cat = ratio_data['intervalCategory']
                categories[cat] = categories.get(cat, 0) + 1
        
        # Konsonanz-Analyse
        consonant_count = sum(1 for r in xi_ratios if r['isConsonant'])
        total_exact = sum(1 for r in xi_ratios if r['isExactMatch'])
        
        consonance_ratio = consonant_count / total_exact if total_exact > 0 else 0
        
        return {
            'pattern': pattern,
            'categories': categories,
            'exactRatioCount': total_exact,
            'consonantRatioCount': consonant_count,
            'consonanceRatio': round(consonance_ratio, 3),
            'harmonicity': 'Hoch' if consonance_ratio > 0.7 else 'Mittel' if consonance_ratio > 0.3 else 'Niedrig'
        }
    
    def _optimized_peak_analysis(self, signal, freq_range, progress_callback):
        """Optimierte Peak-Analyse ohne f₀-Hinweis"""
        # Limitiere Signal für Performance
        if len(signal) > 88200:  # Max 2 Sekunden bei 44100 Hz
            signal = signal[:88200]
            print(f"⚡ Signal begrenzt auf {len(signal)} Samples für Performance")
        
        return self._find_peaks(signal, freq_range, progress_callback)
    
    def _filter_by_amplitude(self, signal, min_amp, max_amp):
        """Filtere Signal nach Amplitude"""
        filtered_signal = signal.copy()
        
        if min_amp is not None:
            filtered_signal = np.where(np.abs(filtered_signal) >= min_amp, filtered_signal, 0)
        
        if max_amp is not None:
            filtered_signal = np.where(np.abs(filtered_signal) <= max_amp, filtered_signal, 
                                     np.sign(filtered_signal) * max_amp)
        
        return filtered_signal
    
    def _find_peaks(self, signal, freq_range, progress_callback=None):
        """Finde spektrale Peaks mit konfigurierbarer Auflösung"""
        peaks = []
        min_freq, max_freq = freq_range
        
        # Auflösung basierend auf Einstellung
        resolution_map = {
            'ultra_high': 0.1,    # 0.1 Hz - Sehr genau aber langsam
            'high': 0.25,         # 0.25 Hz - Gut für präzise Analyse  
            'medium': 0.5,        # 0.5 Hz - Standard
            'low': 1.0,           # 1.0 Hz - Schnell für Überblick
            'fast': 2.0           # 2.0 Hz - Sehr schnell
        }
        
        step_size = resolution_map.get(self.resolution, 0.5)
        
        total_steps = int((max_freq - min_freq) / step_size)
        processed = 0
        
        print(f"📊 Analysiere {total_steps} Frequenzen von {min_freq} bis {max_freq} Hz (Auflösung: {step_size} Hz)")
        
        for freq in np.arange(min_freq, max_freq, step_size):
            magnitude = self._calculate_magnitude(signal, freq)
            
            if magnitude > self.threshold:
                peaks.append({
                    'frequency': round(freq, 2),
                    'magnitude': magnitude,
                    'magnitudeDB': 20 * math.log10(magnitude + 1e-10)
                })
            
            processed += 1
            if progress_callback and processed % 25 == 0:  # Update alle 25 Schritte
                progress = int((processed / total_steps) * 100)
                progress_callback(progress, f"Analysiere {freq:.1f} Hz ({len(peaks)} Peaks)")
        
        # Sortiere nach Magnitude
        peaks.sort(key=lambda x: x['magnitude'], reverse=True)
        return peaks[:100]  # Top 100 Peaks
    
    def _calculate_magnitude(self, signal, frequency):
        """DFT für spezifische Frequenz"""
        N = len(signal)
        real = imag = 0.0
        
        for n in range(N):
            angle = -2 * math.pi * frequency * n / self.sample_rate
            real += signal[n] * math.cos(angle)
            imag += signal[n] * math.sin(angle)
        
        return math.sqrt(real * real + imag * imag) * 2 / N
    
    def _calculate_xi_ratios(self, peaks):
        """Berechne ξ-Verhältnisse (Standard-Implementierung)"""
        ratios = []
        
        for i in range(min(10, len(peaks))):  # Nur Top 10 für Performance
            for j in range(i + 1, min(10, len(peaks))):
                f1, f2 = peaks[i]['frequency'], peaks[j]['frequency']
                xi = max(f1, f2) / min(f1, f2)
                significance = peaks[i]['magnitude'] * peaks[j]['magnitude']
                
                ratios.append({
                    'freqHigh': max(f1, f2),
                    'freqLow': min(f1, f2),
                    'xiRatio': round(xi, 3),
                    'significance': significance,
                    'isExactMatch': False,
                    'intervalName': 'Standard',
                    'intervalCategory': 'Numeric',
                    'isConsonant': False
                })
        
        ratios.sort(key=lambda x: x['significance'], reverse=True)
        return ratios[:20]  # Top 20

# ===== SIGNAL GENERATOR =====
class SignalGenerator:
    """Einfacher Signal-Generator für Schwebungen"""
    
    @staticmethod
    def create_beating_signal(f0, delta_f, duration=5.0, sample_rate=44100):
        """Erstelle Schwebungs-Signal mit 3 Frequenzen"""
        print(f"🎵 Generiere Schwebungs-Signal: f0={f0}, Δf={delta_f}, {duration}s")
        
        t = np.linspace(0, duration, int(duration * sample_rate))
        
        # DREI Frequenzen für echte Schwebungsanalyse
        f1 = f0 - delta_f  # Unterton
        f2 = f0            # Grundton  
        f3 = f0 + delta_f  # Oberton
        
        print(f"📊 Frequenzen: f1={f1:.1f}Hz, f0={f2:.1f}Hz, f2={f3:.1f}Hz")
        
        # Drei Sinustöne mit unterschiedlichen Amplituden
        signal1 = 0.4 * np.sin(2 * np.pi * f1 * t)  # Unterton (40%)
        signal2 = 0.8 * np.sin(2 * np.pi * f2 * t)  # Grundton (80% - stärkster)
        signal3 = 0.4 * np.sin(2 * np.pi * f3 * t)  # Oberton (40%)
        
        # Kombiniere alle drei Signale
        signal = signal1 + signal2 + signal3
        
        # Normalisierung
        max_amplitude = np.max(np.abs(signal))
        if max_amplitude > 0:
            signal = signal / max_amplitude * 0.7  # 70% der Maximalamplitude
        
        print(f"✅ Signal generiert: {len(signal)} Samples, 3 Frequenzen kombiniert")
        print(f"   Schwebungsfrequenz: {f3-f1:.1f} Hz zwischen äußeren Tönen")
        return signal

# ===== WAV FILE UTILITIES =====
class WAVUtils:
    """WAV-Datei Utilities"""
    
    @staticmethod
    def save_wav(signal, filename, sample_rate=44100):
        """Speichere Signal als WAV"""
        try:
            # Normalisiere auf 16-bit
            signal_int = (signal * 32767).astype(np.int16)
            
            with wave.open(filename, 'w') as wav_file:
                wav_file.setnchannels(1)  # Mono
                wav_file.setsampwidth(2)  # 16-bit
                wav_file.setframerate(sample_rate)
                wav_file.writeframes(signal_int.tobytes())
                
            print(f"💾 WAV gespeichert: {filename}")
            return True
        except Exception as e:
            print(f"❌ WAV Fehler: {e}")
            return False
    
    @staticmethod
    def load_wav(filename):
        """Lade WAV-Datei"""
        try:
            with wave.open(filename, 'r') as wav_file:
                frames = wav_file.readframes(-1)
                sample_rate = wav_file.getframerate()
                channels = wav_file.getnchannels()
                
                # Konvertiere zu numpy array
                if wav_file.getsampwidth() == 2:  # 16-bit
                    signal = np.frombuffer(frames, dtype=np.int16)
                else:
                    signal = np.frombuffer(frames, dtype=np.int8)
                
                # Normalisiere
                signal = signal.astype(np.float32) / 32767.0
                
                # Mono-Konvertierung
                if channels == 2:
                    signal = signal[::2]  # Nur linker Kanal
                
                print(f"📁 WAV geladen: {len(signal)} Samples, {sample_rate} Hz")
                return signal, sample_rate
                
        except Exception as e:
            print(f"❌ WAV Lade-Fehler: {e}")
            return None, None

# ===== HAUPTANWENDUNG =====
class XiFFTApp:
    """Hauptanwendung mit Tkinter GUI"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("ξ-FFT Schwebungs-Analyse - Windows GUI mit Harmonischer Intelligenz")
        self.root.geometry("1400x900")
        
        # Initialisierung
        self.xi_fft = XiFFT()
        self.current_signal = None
        self.current_analysis = None
        self.loaded_signal = None
        self.loaded_sample_rate = None
        self.current_tab = "generator"  # Track aktueller Tab
        
        print("🚀 Starte ξ-FFT Windows GUI...")
        self.setup_gui()
        
    def setup_gui(self):
        """Erstelle GUI-Elemente"""
        
        # Notebook für Tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Tab 1: Generator
        self.setup_generator_tab()
        
        # Tab 2: Datei-Analyse
        self.setup_file_tab()
        
        # Tab 3: Ergebnisse
        self.setup_results_tab()
        
        # Tab-Wechsel Event
        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_changed)
        
        print("✅ GUI Setup abgeschlossen")
    
    def setup_generator_tab(self):
        """Generator Tab"""
        gen_frame = ttk.Frame(self.notebook)
        self.notebook.add(gen_frame, text="🎵 Signal-Generator")
        
        # Steuerung
        control_frame = ttk.LabelFrame(gen_frame, text="Signal-Parameter")
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Grundfrequenz
        ttk.Label(control_frame, text="Grundfrequenz f₀ (Hz):").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.f0_var = tk.DoubleVar(value=440.0)
        f0_spinbox = ttk.Spinbox(control_frame, from_=100.0, to=1000.0, increment=10.0, 
                                textvariable=self.f0_var, width=10)
        f0_spinbox.grid(row=0, column=1, padx=5, pady=2)
        
        # Schwebungsfrequenz
        ttk.Label(control_frame, text="Schwebung Δf (Hz):").grid(row=0, column=2, sticky=tk.W, padx=5, pady=2)
        self.delta_f_var = tk.DoubleVar(value=5.0)
        delta_spinbox = ttk.Spinbox(control_frame, from_=0.1, to=50.0, increment=0.5, 
                                   textvariable=self.delta_f_var, width=10)
        delta_spinbox.grid(row=0, column=3, padx=5, pady=2)
        
        # Frequenz-Anzeige
        freq_info_frame = ttk.Frame(control_frame)
        freq_info_frame.grid(row=1, column=0, columnspan=4, pady=5)
        
        self.freq_info_var = tk.StringVar()
        freq_info_label = ttk.Label(freq_info_frame, textvariable=self.freq_info_var, 
                                   foreground="darkgreen", font=("Courier", 9))
        freq_info_label.pack()
        
        # Update frequency display
        def update_freq_display():
            f0 = self.f0_var.get()
            df = self.delta_f_var.get()
            self.freq_info_var.set(f"🎵 Frequenzen: f₁={f0-df:.1f}Hz | f₀={f0:.1f}Hz | f₂={f0+df:.1f}Hz → Δf={2*df:.1f}Hz")
        
        f0_spinbox.configure(command=update_freq_display)
        delta_spinbox.configure(command=update_freq_display)
        update_freq_display()  # Initial display
        
        # Dauer
        ttk.Label(control_frame, text="Dauer (s):").grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
        self.duration_var = tk.DoubleVar(value=3.0)
        duration_spinbox = ttk.Spinbox(control_frame, from_=1.0, to=10.0, increment=1.0, 
                                      textvariable=self.duration_var, width=10)
        duration_spinbox.grid(row=2, column=1, padx=5, pady=2)
        
        # Buttons
        button_frame = ttk.Frame(control_frame)
        button_frame.grid(row=3, column=0, columnspan=4, pady=10)
        
        ttk.Button(button_frame, text="🎵 3-Ton Signal generieren", 
                  command=self.generate_signal).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="🔍 ξ-FFT Analysieren", 
                  command=self.analyze_generated).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="💾 Als WAV speichern", 
                  command=self.save_generated_wav).pack(side=tk.LEFT, padx=5)
        
        # Status
        self.gen_status_var = tk.StringVar(value="Bereit für 3-Frequenz Signal-Generierung")
        ttk.Label(control_frame, textvariable=self.gen_status_var, 
                 foreground="blue").grid(row=4, column=0, columnspan=4, pady=5)
        
        # Fortschrittbalken
        self.gen_progress_var = tk.DoubleVar()
        self.gen_progress = ttk.Progressbar(control_frame, variable=self.gen_progress_var, 
                                           maximum=100)
        self.gen_progress.grid(row=5, column=0, columnspan=4, sticky=tk.EW, padx=5, pady=2)
    
    def setup_file_tab(self):
        """Datei-Analyse Tab"""
        file_frame = ttk.Frame(self.notebook)
        self.notebook.add(file_frame, text="📁 Datei-Analyse")
        
        # Datei-Auswahl
        file_control_frame = ttk.LabelFrame(file_frame, text="WAV-Datei laden")
        file_control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Button(file_control_frame, text="📂 WAV-Datei auswählen", 
                  command=self.load_wav_file).pack(side=tk.LEFT, padx=5, pady=5)
        
        self.file_info_var = tk.StringVar(value="Keine Datei geladen")
        ttk.Label(file_control_frame, textvariable=self.file_info_var, 
                 foreground="gray").pack(side=tk.LEFT, padx=20)
        
        # Analyse-Parameter
        param_frame = ttk.LabelFrame(file_frame, text="Analyse-Parameter")
        param_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Frequenzbereich
        freq_frame = ttk.Frame(param_frame)
        freq_frame.grid(row=0, column=0, columnspan=4, pady=5, sticky=tk.EW)
        
        ttk.Label(freq_frame, text="Min. Frequenz (Hz):").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.min_freq_var = tk.IntVar(value=50)
        ttk.Spinbox(freq_frame, from_=20, to=1000, increment=10, 
                   textvariable=self.min_freq_var, width=10).grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(freq_frame, text="Max. Frequenz (Hz):").grid(row=0, column=2, sticky=tk.W, padx=5, pady=2)
        self.max_freq_var = tk.IntVar(value=2000)
        ttk.Spinbox(freq_frame, from_=100, to=5000, increment=100, 
                   textvariable=self.max_freq_var, width=10).grid(row=0, column=3, padx=5, pady=2)
        
        # Analyse-Auflösung
        resolution_frame = ttk.Frame(param_frame)
        resolution_frame.grid(row=1, column=0, columnspan=4, pady=5, sticky=tk.EW)
        
        ttk.Label(resolution_frame, text="Auflösung:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.resolution_var = tk.StringVar(value="medium")
        resolution_combo = ttk.Combobox(resolution_frame, textvariable=self.resolution_var, 
                                      values=["ultra_high", "high", "medium", "low", "fast"], 
                                      state="readonly", width=12)
        resolution_combo.grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(resolution_frame, text="Threshold:").grid(row=0, column=2, sticky=tk.W, padx=5, pady=2)
        self.threshold_var = tk.DoubleVar(value=0.005)
        threshold_spinbox = ttk.Spinbox(resolution_frame, from_=0.001, to=0.1, increment=0.001, 
                                       textvariable=self.threshold_var, width=10, format="%.3f")
        threshold_spinbox.grid(row=0, column=3, padx=5, pady=2)
        
        # Amplituden-Filter
        amplitude_frame = ttk.LabelFrame(param_frame, text="Amplituden-Filter (optional)")
        amplitude_frame.grid(row=2, column=0, columnspan=4, pady=5, sticky=tk.EW)
        
        self.use_amplitude_filter = tk.BooleanVar(value=False)
        ttk.Checkbutton(amplitude_frame, text="Amplituden-Filter aktivieren", 
                       variable=self.use_amplitude_filter, 
                       command=self.toggle_amplitude_filter).grid(row=0, column=0, columnspan=2, pady=2)
        
        ttk.Label(amplitude_frame, text="Min. Amplitude:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.min_amplitude_var = tk.DoubleVar(value=0.01)
        self.min_amp_spinbox = ttk.Spinbox(amplitude_frame, from_=0.001, to=1.0, increment=0.01, 
                                          textvariable=self.min_amplitude_var, width=10, format="%.3f", state="disabled")
        self.min_amp_spinbox.grid(row=1, column=1, padx=5, pady=2)
        
        ttk.Label(amplitude_frame, text="Max. Amplitude:").grid(row=1, column=2, sticky=tk.W, padx=5, pady=2)
        self.max_amplitude_var = tk.DoubleVar(value=1.0)
        self.max_amp_spinbox = ttk.Spinbox(amplitude_frame, from_=0.1, to=2.0, increment=0.1, 
                                          textvariable=self.max_amplitude_var, width=10, format="%.1f", state="disabled")
        self.max_amp_spinbox.grid(row=1, column=3, padx=5, pady=2)
        
        # Auflösungs-Info
        resolution_info = ttk.Frame(param_frame)
        resolution_info.grid(row=3, column=0, columnspan=4, pady=5)
        
        self.resolution_info_var = tk.StringVar()
        self.update_resolution_info()
        resolution_combo.bind('<<ComboboxSelected>>', lambda e: self.update_resolution_info())
        
        ttk.Label(resolution_info, textvariable=self.resolution_info_var, 
                 foreground="darkblue", font=("Arial", 8)).pack()
        
        # Erweiterte Einstellungen
        advanced_frame = ttk.LabelFrame(param_frame, text="Erweiterte Einstellungen")
        advanced_frame.grid(row=4, column=0, columnspan=4, pady=5, sticky=tk.EW)
        
        # Exakte Verhältnisse
        self.use_exact_ratios = tk.BooleanVar(value=True)
        ttk.Checkbutton(advanced_frame, text="Exakte Verhältnisse nutzen (empfohlen)", 
                       variable=self.use_exact_ratios).grid(row=0, column=0, columnspan=2, sticky=tk.W, pady=2)
        
        # Harmonische Intelligenz
        self.use_harmonic_intelligence = tk.BooleanVar(value=True)
        ttk.Checkbutton(advanced_frame, text="Harmonische Intelligenz aktivieren", 
                       variable=self.use_harmonic_intelligence).grid(row=0, column=2, columnspan=2, sticky=tk.W, pady=2)
        
        # Buttons
        file_button_frame = ttk.Frame(param_frame)
        file_button_frame.grid(row=5, column=0, columnspan=4, pady=10)
        
        ttk.Button(file_button_frame, text="🔍 Datei analysieren", 
                  command=self.analyze_file).pack(side=tk.LEFT, padx=5)
        ttk.Button(file_button_frame, text="💾 Analysiertes Segment speichern", 
                  command=self.save_analyzed_segment).pack(side=tk.LEFT, padx=5)
        ttk.Button(file_button_frame, text="🗑️ Analyse zurücksetzen", 
                  command=self.clear_file_analysis).pack(side=tk.LEFT, padx=5)
        
        # Status
        self.file_status_var = tk.StringVar(value="Bereit für Datei-Analyse")
        ttk.Label(param_frame, textvariable=self.file_status_var, 
                 foreground="blue").grid(row=6, column=0, columnspan=4, pady=5)
        
        # Fortschrittbalken
        self.file_progress_var = tk.DoubleVar()
        self.file_progress = ttk.Progressbar(param_frame, variable=self.file_progress_var, 
                                            maximum=100)
        self.file_progress.grid(row=7, column=0, columnspan=4, sticky=tk.EW, padx=5, pady=2)
    
    def setup_results_tab(self):
        """Ergebnisse Tab"""
        results_frame = ttk.Frame(self.notebook)
        self.notebook.add(results_frame, text="📊 Analyse-Ergebnisse")
        
        # Matplotlib Figure
        self.fig = Figure(figsize=(14, 10), facecolor='white')
        self.canvas = FigureCanvasTkAgg(self.fig, results_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Subplots
        self.ax_waveform = self.fig.add_subplot(3, 1, 1)
        self.ax_spectrum = self.fig.add_subplot(3, 1, 2)
        self.ax_peaks = self.fig.add_subplot(3, 1, 3)
        
        self.ax_waveform.set_title('Zeitverlauf (Waveform)')
        self.ax_spectrum.set_title('Frequenzspektrum')
        self.ax_peaks.set_title('Erkannte Peaks & ξ-Verhältnisse')
        
        self.fig.tight_layout()
        
        # Ergebnisse-Text
        text_frame = ttk.Frame(results_frame)
        text_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.results_text = tk.Text(text_frame, height=8, width=100)
        scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scrollbar.set)
        
        self.results_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # ===== TAB MANAGEMENT =====
    def on_tab_changed(self, event):
        """Wird beim Tab-Wechsel aufgerufen"""
        selected_tab = event.widget.tab('current')['text']
        old_tab = self.current_tab
        
        if "Generator" in selected_tab:
            self.current_tab = "generator"
        elif "Datei" in selected_tab:
            self.current_tab = "file"
        elif "Ergebnisse" in selected_tab:
            self.current_tab = "results"
        
        print(f"🔄 Tab-Wechsel: {old_tab} → {self.current_tab}")
        
        # Beim Wechsel zu einem neuen Tab: Ergebnisse nur anzeigen wenn passende Analyse vorhanden
        if self.current_tab == "results":
            self.update_results_for_current_context()
    
    def update_results_for_current_context(self):
        """Update Ergebnisse basierend auf aktuellem Kontext"""
        # Bestimme welche Analyse angezeigt werden soll
        if self.current_tab == "results":
            # Prüfe ob wir eine passende Analyse haben
            if hasattr(self, '_last_analysis_type'):
                if self._last_analysis_type == "generator" and self.current_signal is not None:
                    # Zeige Generator-Analyse
                    if hasattr(self, '_generator_analysis'):
                        self.display_analysis_results(self._generator_analysis, "generator")
                        return
                elif self._last_analysis_type == "file" and self.loaded_signal is not None:
                    # Zeige Datei-Analyse  
                    if hasattr(self, '_file_analysis'):
                        self.display_analysis_results(self._file_analysis, "file")
                        return
            
            # Keine passende Analyse - zeige leere Ergebnisse
            self.clear_results_display()
    
    def clear_results_display(self):
        """Leere die Ergebnisanzeige"""
        # Plots leeren
        for ax in [self.ax_waveform, self.ax_spectrum, self.ax_peaks]:
            ax.clear()
            ax.text(0.5, 0.5, 'Keine Analyse durchgeführt\nBitte erst Signal generieren oder Datei analysieren', 
                   ha='center', va='center', transform=ax.transAxes, fontsize=12,
                   bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray", alpha=0.7))
        
        self.ax_waveform.set_title('Zeitverlauf (Waveform)')
        self.ax_spectrum.set_title('Frequenzspektrum') 
        self.ax_peaks.set_title('Erkannte Peaks & ξ-Verhältnisse')
        
        self.canvas.draw()
        
        # Text leeren
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, "=== KEINE ANALYSE VERFÜGBAR ===\n\n")
        self.results_text.insert(tk.END, "Bitte führen Sie erst eine Analyse durch:\n")
        self.results_text.insert(tk.END, "• Tab 'Signal-Generator': Signal generieren und analysieren\n")
        self.results_text.insert(tk.END, "• Tab 'Datei-Analyse': WAV-Datei laden und analysieren\n")
    
    # ===== HELPER FUNCTIONS =====
    def toggle_amplitude_filter(self):
        """Toggle Amplituden-Filter Ein/Aus"""
        enabled = self.use_amplitude_filter.get()
        state = "normal" if enabled else "disabled"
        
        self.min_amp_spinbox.configure(state=state)
        self.max_amp_spinbox.configure(state=state)
        
        print(f"🔧 Amplituden-Filter: {'Aktiviert' if enabled else 'Deaktiviert'}")
    
    def update_resolution_info(self):
        """Update Auflösungs-Informationen"""
        resolution = self.resolution_var.get()
        
        info_map = {
            'ultra_high': "0.1 Hz - Sehr präzise (langsam)",
            'high': "0.25 Hz - Hohe Genauigkeit", 
            'medium': "0.5 Hz - Standard (empfohlen)",
            'low': "1.0 Hz - Schnell für Überblick",
            'fast': "2.0 Hz - Sehr schnell (ungenau)"
        }
        
        self.resolution_info_var.set(f"ℹ️ {info_map.get(resolution, 'Unbekannt')}")
    
    def clear_file_analysis(self):
        """Zurücksetzen der Datei-Analyse"""
        if hasattr(self, '_file_analysis'):
            delattr(self, '_file_analysis')
        
        self.file_status_var.set("Analyse zurückgesetzt")
        self.file_progress_var.set(0)
        
        # Wenn wir gerade im Results-Tab sind, leere die Anzeige
        if self.current_tab == "results":
            self.clear_results_display()
        
        print("🗑️ Datei-Analyse zurückgesetzt")
    
    # ===== GENERATOR FUNKTIONEN =====
    def generate_signal(self):
        """Generiere Schwebungs-Signal"""
        try:
            f0 = self.f0_var.get()
            delta_f = self.delta_f_var.get()
            duration = self.duration_var.get()
            
            self.gen_status_var.set("Generiere Signal...")
            self.root.update()
            
            self.current_signal = SignalGenerator.create_beating_signal(f0, delta_f, duration)
            
            self.gen_status_var.set(f"✅ Signal generiert: {len(self.current_signal)} Samples")
            
            # Lösche alte Generator-Analyse
            if hasattr(self, '_generator_analysis'):
                delattr(self, '_generator_analysis')
            
            # Automatisch zur Ergebnisse-Tab wechseln und Waveform anzeigen
            self._last_analysis_type = "generator"
            self.notebook.select(2)  # Results tab
            self.plot_waveform(self.current_signal, 44100)
            
        except Exception as e:
            self.gen_status_var.set(f"❌ Fehler: {str(e)}")
            messagebox.showerror("Fehler", f"Signal-Generierung fehlgeschlagen:\n{str(e)}")