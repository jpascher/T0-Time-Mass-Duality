"""
ξ-FFT Schwebungs-Analyse - Windows GUI Version
Minimale, funktionsfähige Python-Anwendung

Abhängigkeiten:
pip install numpy matplotlib tkinter wave

Verwendung:
python xi_fft_windows_app.py
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

# ===== ξ-FFT LIBRARY =====
class XiFFT:
    """Minimale ξ-FFT Implementation für Windows GUI"""
    
    def __init__(self, sample_rate=44100, threshold=0.005, resolution='medium'):
        self.sample_rate = sample_rate
        self.threshold = threshold
        self.resolution = resolution
        print(f"🔬 XiFFT initialisiert: {sample_rate} Hz, Threshold: {threshold}, Resolution: {resolution}")
    
    def analyze(self, signal, freq_range=(20, 2000), progress_callback=None, min_amplitude=None, max_amplitude=None):
        """Analysiere Signal mit Fortschrittsanzeige und Amplituden-Filter"""
        print(f"🔍 Starte Analyse: {len(signal)} Samples, Bereich: {freq_range}")
        
        if len(signal) == 0:
            return {'peaks': [], 'xiRatios': [], 'peakCount': 0}
        
        # Amplituden-Filter anwenden
        if min_amplitude is not None or max_amplitude is not None:
            signal = self._filter_by_amplitude(signal, min_amplitude, max_amplitude)
            print(f"🔧 Amplituden-Filter angewendet: min={min_amplitude}, max={max_amplitude}")
        
        # Limitiere Signal für Performance
        if len(signal) > 88200:  # Max 2 Sekunden bei 44100 Hz
            signal = signal[:88200]
            print(f"⚡ Signal begrenzt auf {len(signal)} Samples für Performance")
        
        peaks = self._find_peaks(signal, freq_range, progress_callback)
        xi_ratios = self._calculate_xi_ratios(peaks)
        
        result = {
            'peaks': peaks,
            'xiRatios': xi_ratios,
            'peakCount': len(peaks),
            'dominantXi': xi_ratios[0] if xi_ratios else None,
            'resolution': self.resolution,
            'amplitudeFiltered': min_amplitude is not None or max_amplitude is not None
        }
        
        print(f"✅ Analyse abgeschlossen: {len(peaks)} Peaks, {len(xi_ratios)} ξ-Ratios")
        return result
    
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
        """Berechne ξ-Verhältnisse"""
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
                    'significance': significance
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
    
    @staticmethod
    def create_pure_tone(frequency, duration=2.0, sample_rate=44100):
        """Erstelle reinen Ton"""
        t = np.linspace(0, duration, int(duration * sample_rate))
        signal = 0.5 * np.sin(2 * np.pi * frequency * t)
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
        self.root.title("ξ-FFT Schwebungs-Analyse - Windows GUI")
        self.root.geometry("1200x800")
        
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
        
        # Buttons
        file_button_frame = ttk.Frame(param_frame)
        file_button_frame.grid(row=4, column=0, columnspan=4, pady=10)
        
        ttk.Button(file_button_frame, text="🔍 Datei analysieren", 
                  command=self.analyze_file).pack(side=tk.LEFT, padx=5)
        ttk.Button(file_button_frame, text="💾 Analysiertes Segment speichern", 
                  command=self.save_analyzed_segment).pack(side=tk.LEFT, padx=5)
        ttk.Button(file_button_frame, text="🗑️ Analyse zurücksetzen", 
                  command=self.clear_file_analysis).pack(side=tk.LEFT, padx=5)
        
        # Status
        self.file_status_var = tk.StringVar(value="Bereit für Datei-Analyse")
        ttk.Label(param_frame, textvariable=self.file_status_var, 
                 foreground="blue").grid(row=5, column=0, columnspan=4, pady=5)
        
        # Fortschrittbalken
        self.file_progress_var = tk.DoubleVar()
        self.file_progress = ttk.Progressbar(param_frame, variable=self.file_progress_var, 
                                            maximum=100)
        self.file_progress.grid(row=6, column=0, columnspan=4, sticky=tk.EW, padx=5, pady=2)
    
    def setup_results_tab(self):
        """Ergebnisse Tab"""
        results_frame = ttk.Frame(self.notebook)
        self.notebook.add(results_frame, text="📊 Analyse-Ergebnisse")
        
        # Matplotlib Figure
        self.fig = Figure(figsize=(12, 8), facecolor='white')
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
        
        self.results_text = tk.Text(text_frame, height=6, width=80)
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
    
    def analyze_generated(self):
        """Analysiere generiertes Signal"""
        if self.current_signal is None:
            messagebox.showwarning("Warnung", "Erst Signal generieren!")
            return
        
        def analyze_thread():
            try:
                f0 = self.f0_var.get()
                delta_f = self.delta_f_var.get()
                
                # Update XiFFT mit aktuellen Einstellungen (falls im File-Tab geändert)
                resolution = getattr(self, 'resolution_var', tk.StringVar(value="medium")).get()
                threshold = getattr(self, 'threshold_var', tk.DoubleVar(value=0.005)).get()
                
                self.xi_fft = XiFFT(44100, threshold, resolution)
                
                # Frequenzbereich um f0 ± 5*delta_f
                freq_range = (max(20, f0 - 5*delta_f), min(5000, f0 + 5*delta_f))
                
                def progress_callback(progress, text):
                    self.gen_progress_var.set(progress)
                    self.gen_status_var.set(text)
                    self.root.update()
                
                self.gen_status_var.set("🔍 Analysiere Signal...")
                
                # Amplituden-Filter (falls aktiviert)
                use_filter = getattr(self, 'use_amplitude_filter', tk.BooleanVar(value=False)).get()
                min_amp = self.min_amplitude_var.get() if use_filter else None
                max_amp = self.max_amplitude_var.get() if use_filter else None
                
                analysis = self.xi_fft.analyze(self.current_signal, freq_range, progress_callback, min_amp, max_amp)
                
                # Speichere Analyse als Generator-spezifisch
                self._generator_analysis = analysis
                self._last_analysis_type = "generator"
                
                # UI Update in main thread
                self.root.after(0, lambda: self.update_results_after_analysis(analysis, "generator"))
                
            except Exception as e:
                self.root.after(0, lambda: self.handle_analysis_error(str(e), "gen"))
        
        # Starte Analyse in separatem Thread
        threading.Thread(target=analyze_thread, daemon=True).start()
    
    def save_generated_wav(self):
        """Speichere generiertes Signal als WAV"""
        if self.current_signal is None:
            messagebox.showwarning("Warnung", "Erst Signal generieren!")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".wav",
            filetypes=[("WAV files", "*.wav"), ("All files", "*.*")],
            title="Signal als WAV speichern"
        )
        
        if filename:
            if WAVUtils.save_wav(self.current_signal, filename):
                self.gen_status_var.set(f"💾 WAV gespeichert: {os.path.basename(filename)}")
                messagebox.showinfo("Erfolg", f"Signal gespeichert als:\n{filename}")
            else:
                messagebox.showerror("Fehler", "WAV-Export fehlgeschlagen")
    
    # ===== DATEI FUNKTIONEN =====
    def load_wav_file(self):
        """Lade WAV-Datei"""
        filename = filedialog.askopenfilename(
            filetypes=[("WAV files", "*.wav"), ("All files", "*.*")],
            title="WAV-Datei auswählen"
        )
        
        if filename:
            try:
                self.file_status_var.set("📁 Lade Datei...")
                self.root.update()
                
                signal, sample_rate = WAVUtils.load_wav(filename)
                
                if signal is not None:
                    self.loaded_signal = signal
                    self.loaded_sample_rate = sample_rate
                    
                    # Update XiFFT sample rate
                    self.xi_fft = XiFFT(sample_rate)
                    
                    duration = len(signal) / sample_rate
                    self.file_info_var.set(f"📄 {os.path.basename(filename)} ({duration:.1f}s, {sample_rate}Hz)")
                    self.file_status_var.set("✅ Datei erfolgreich geladen")
                    
                    # Zeige Waveform
                    self.notebook.select(2)  # Results tab
                    self.plot_waveform(signal, sample_rate)
                    
                else:
                    self.file_status_var.set("❌ Datei konnte nicht geladen werden")
                    
            except Exception as e:
                self.file_status_var.set(f"❌ Fehler: {str(e)}")
                messagebox.showerror("Fehler", f"Datei-Laden fehlgeschlagen:\n{str(e)}")
    
    def analyze_file(self):
        """Analysiere geladene Datei"""
        if self.loaded_signal is None:
            messagebox.showwarning("Warnung", "Erst WAV-Datei laden!")
            return
        
        def analyze_thread():
            try:
                min_freq = self.min_freq_var.get()
                max_freq = self.max_freq_var.get()
                freq_range = (min_freq, max_freq)
                
                # Update XiFFT mit aktuellen Einstellungen
                resolution = self.resolution_var.get()
                threshold = self.threshold_var.get()
                
                self.xi_fft = XiFFT(self.loaded_sample_rate, threshold, resolution)
                
                def progress_callback(progress, text):
                    self.file_progress_var.set(progress)
                    self.file_status_var.set(text)
                    self.root.update()
                
                self.file_status_var.set("🔍 Analysiere Datei...")
                
                # Limitiere Signal für Performance (erste 3 Sekunden)
                max_samples = min(len(self.loaded_signal), self.loaded_sample_rate * 3)
                signal_segment = self.loaded_signal[:max_samples]
                
                # Amplituden-Filter (falls aktiviert)
                use_filter = self.use_amplitude_filter.get()
                min_amp = self.min_amplitude_var.get() if use_filter else None
                max_amp = self.max_amplitude_var.get() if use_filter else None
                
                analysis = self.xi_fft.analyze(signal_segment, freq_range, progress_callback, min_amp, max_amp)
                
                # Speichere Analyse als Datei-spezifisch
                self._file_analysis = analysis
                self._last_analysis_type = "file"
                
                # UI Update in main thread
                self.root.after(0, lambda: self.update_results_after_analysis(analysis, "file"))
                
            except Exception as e:
                self.root.after(0, lambda: self.handle_analysis_error(str(e), "file"))
        
        # Starte Analyse in separatem Thread
        threading.Thread(target=analyze_thread, daemon=True).start()
    
    def save_analyzed_segment(self):
        """Speichere analysiertes Segment"""
        if self.loaded_signal is None:
            messagebox.showwarning("Warnung", "Erst Datei laden und analysieren!")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".wav",
            filetypes=[("WAV files", "*.wav"), ("All files", "*.*")],
            title="Analysiertes Segment speichern"
        )
        
        if filename:
            # Ersten 3 Sekunden speichern (wie analysiert)
            max_samples = min(len(self.loaded_signal), self.loaded_sample_rate * 3)
            segment = self.loaded_signal[:max_samples]
            
            if WAVUtils.save_wav(segment, filename, self.loaded_sample_rate):
                self.file_status_var.set(f"💾 Segment gespeichert: {os.path.basename(filename)}")
                messagebox.showinfo("Erfolg", f"Segment gespeichert als:\n{filename}")
            else:
                messagebox.showerror("Fehler", "WAV-Export fehlgeschlagen")
    
    # ===== ERGEBNISSE FUNKTIONEN =====
    def update_results_after_analysis(self, analysis, analysis_type):
        """Update GUI nach Analyse"""
        if analysis is None:
            return
        
        try:
            # Plots aktualisieren basierend auf Analyse-Typ
            if analysis_type == "generator" and self.current_signal is not None:
                self.plot_spectrum(analysis, self.current_signal, 44100)
                self.plot_waveform(self.current_signal, 44100)
            elif analysis_type == "file" and self.loaded_signal is not None:
                max_samples = min(len(self.loaded_signal), self.loaded_sample_rate * 3)
                segment = self.loaded_signal[:max_samples]
                self.plot_spectrum(analysis, segment, self.loaded_sample_rate)
                self.plot_waveform(segment, self.loaded_sample_rate)
            
            self.plot_peaks_and_xi(analysis)
            
            # Text-Ergebnisse
            self.display_analysis_text(analysis, analysis_type)
            
            # Status updates
            peak_count = analysis['peakCount']
            xi_count = len(analysis['xiRatios'])
            
            if analysis_type == "generator":
                self.gen_status_var.set(f"✅ Analyse komplett: {peak_count} Peaks, {xi_count} ξ-Ratios")
                self.gen_progress_var.set(100)
            elif analysis_type == "file":
                self.file_status_var.set(f"✅ Analyse komplett: {peak_count} Peaks, {xi_count} ξ-Ratios")
                self.file_progress_var.set(100)
            
            # Wechsle zur Ergebnisse-Tab
            self.notebook.select(2)
            
        except Exception as e:
            print(f"❌ Update Error: {e}")
            messagebox.showerror("Fehler", f"Ergebnisse-Update fehlgeschlagen:\n{str(e)}")
    
    def display_analysis_results(self, analysis, analysis_type):
        """Zeige gespeicherte Analyse-Ergebnisse"""
        if analysis_type == "generator" and self.current_signal is not None:
            self.plot_spectrum(analysis, self.current_signal, 44100)
            self.plot_waveform(self.current_signal, 44100)
        elif analysis_type == "file" and self.loaded_signal is not None:
            max_samples = min(len(self.loaded_signal), self.loaded_sample_rate * 3)
            segment = self.loaded_signal[:max_samples]
            self.plot_spectrum(analysis, segment, self.loaded_sample_rate)
            self.plot_waveform(segment, self.loaded_sample_rate)
        
        self.plot_peaks_and_xi(analysis)
        self.display_analysis_text(analysis, analysis_type)
    
    def handle_analysis_error(self, error_msg, source):
        """Handle Analyse-Fehler"""
        if source == "gen":
            self.gen_status_var.set(f"❌ Analyse-Fehler: {error_msg}")
            self.gen_progress_var.set(0)
        else:
            self.file_status_var.set(f"❌ Analyse-Fehler: {error_msg}")
            self.file_progress_var.set(0)
        
        messagebox.showerror("Analyse-Fehler", f"Analyse fehlgeschlagen:\n{error_msg}")
    
    def plot_waveform(self, signal, sample_rate):
        """Plotte Waveform"""
        self.ax_waveform.clear()
        self.ax_waveform.set_title('Zeitverlauf (Waveform)')
        
        # Für Performance nur erste 2000 Punkte
        if len(signal) > 2000:
            step = len(signal) // 2000
            plot_signal = signal[::step]
        else:
            plot_signal = signal
        
        t = np.linspace(0, len(signal)/sample_rate, len(plot_signal))
        
        self.ax_waveform.plot(t, plot_signal, 'b-', linewidth=0.8)
        self.ax_waveform.set_xlabel('Zeit (s)')
        self.ax_waveform.set_ylabel('Amplitude')
        self.ax_waveform.grid(True, alpha=0.3)
        
        self.canvas.draw()
    
    def plot_spectrum(self, analysis, signal, sample_rate):
        """Plotte Frequenzspektrum"""
        self.ax_spectrum.clear()
        self.ax_spectrum.set_title('Frequenzspektrum')
        
        peaks = analysis['peaks']
        if len(peaks) == 0:
            self.ax_spectrum.text(0.5, 0.5, 'Keine Peaks gefunden', 
                                ha='center', va='center', transform=self.ax_spectrum.transAxes)
            self.canvas.draw()
            return
        
        # Frequenzen und Magnitudes
        frequencies = [p['frequency'] for p in peaks[:20]]  # Top 20
        magnitudes = [p['magnitude'] for p in peaks[:20]]
        
        # Balkendiagramm
        bars = self.ax_spectrum.bar(frequencies, magnitudes, width=2, alpha=0.7, color='steelblue')
        
        # Highlighte den stärksten Peak
        if len(bars) > 0:
            bars[0].set_color('red')
        
        # Labels für stärkste Peaks
        for i, (freq, mag) in enumerate(zip(frequencies[:5], magnitudes[:5])):
            self.ax_spectrum.text(freq, mag + max(magnitudes)*0.05, f'{freq:.1f}Hz', 
                                ha='center', va='bottom', fontsize=8)
        
        self.ax_spectrum.set_xlabel('Frequenz (Hz)')
        self.ax_spectrum.set_ylabel('Magnitude')
        self.ax_spectrum.grid(True, alpha=0.3)
        
        self.canvas.draw()
    
    def plot_peaks_and_xi(self, analysis):
        """Plotte Peaks und ξ-Verhältnisse"""
        self.ax_peaks.clear()
        self.ax_peaks.set_title('Top Peaks & ξ-Verhältnisse')
        
        peaks = analysis['peaks'][:10]  # Top 10
        xi_ratios = analysis['xiRatios'][:10]  # Top 10
        
        if len(peaks) == 0:
            self.ax_peaks.text(0.5, 0.5, 'Keine Daten verfügbar', 
                             ha='center', va='center', transform=self.ax_peaks.transAxes)
            self.canvas.draw()
            return
        
        # Peaks als Scatter-Plot
        frequencies = [p['frequency'] for p in peaks]
        magnitudes = [p['magnitude'] for p in peaks]
        
        scatter = self.ax_peaks.scatter(frequencies, magnitudes, c=range(len(frequencies)), 
                                      cmap='viridis', s=100, alpha=0.7)
        
        # Beschriftung der stärksten Peaks
        for i, (freq, mag) in enumerate(zip(frequencies[:5], magnitudes[:5])):
            self.ax_peaks.annotate(f'{freq:.1f}Hz', (freq, mag), 
                                 xytext=(5, 5), textcoords='offset points', fontsize=8)
        
        # ξ-Verhältnisse als Linien
        colors = plt.cm.Set3(np.linspace(0, 1, len(xi_ratios)))
        for i, ratio in enumerate(xi_ratios[:5]):  # Nur Top 5 für Übersichtlichkeit
            f_low = ratio['freqLow']
            f_high = ratio['freqHigh']
            xi = ratio['xiRatio']
            
            # Finde entsprechende Peaks
            low_mag = next((p['magnitude'] for p in peaks if abs(p['frequency'] - f_low) < 1), 0)
            high_mag = next((p['magnitude'] for p in peaks if abs(p['frequency'] - f_high) < 1), 0)
            
            if low_mag > 0 and high_mag > 0:
                self.ax_peaks.plot([f_low, f_high], [low_mag, high_mag], 
                                 color=colors[i], linewidth=2, alpha=0.6,
                                 label=f'ξ={xi:.2f}')
        
        self.ax_peaks.set_xlabel('Frequenz (Hz)')
        self.ax_peaks.set_ylabel('Magnitude')
        self.ax_peaks.grid(True, alpha=0.3)
        
        if len(xi_ratios) > 0:
            self.ax_peaks.legend(loc='upper right', fontsize=8)
        
        self.canvas.draw()
    
    def display_analysis_text(self, analysis, analysis_type):
        """Zeige Analyse-Ergebnisse als Text"""
        self.results_text.delete(1.0, tk.END)
        
        result_text = "=== ξ-FFT ANALYSE ERGEBNISSE ===\n\n"
        
        # Analyse-Kontext
        if analysis_type == "generator":
            result_text += "🎵 GENERIERTES SIGNAL\n"
        elif analysis_type == "file":
            result_text += "📁 DATEI-ANALYSE\n"
        
        result_text += f"Auflösung: {analysis.get('resolution', 'Standard')}\n"
        if analysis.get('amplitudeFiltered', False):
            result_text += "⚠️ Amplituden-Filter angewendet\n"
        result_text += "\n"
        
        peaks = analysis['peaks']
        xi_ratios = analysis['xiRatios']
        
        result_text += f"📊 Peaks gefunden: {len(peaks)}\n"
        result_text += f"⚡ ξ-Verhältnisse: {len(xi_ratios)}\n\n"
        
        # Erwartete Frequenzen anzeigen (nur für Generator)
        if analysis_type == "generator" and hasattr(self, 'f0_var'):
            f0 = self.f0_var.get()
            df = self.delta_f_var.get()
            result_text += f"🎯 ERWARTETE FREQUENZEN:\n"
            result_text += f"   f₁ = {f0-df:.1f} Hz (Unterton)\n"
            result_text += f"   f₀ = {f0:.1f} Hz (Grundton)\n" 
            result_text += f"   f₂ = {f0+df:.1f} Hz (Oberton)\n"
            result_text += f"   Schwebung = {2*df:.1f} Hz\n\n"
        
        if len(peaks) > 0:
            result_text += "🎵 DETEKTIERTE FREQUENZEN:\n"
            result_text += "-" * 50 + "\n"
            for i, peak in enumerate(peaks[:15], 1):
                # Markiere erwartete Frequenzen (nur für Generator)
                marker = ""
                if analysis_type == "generator" and hasattr(self, 'f0_var'):
                    f0 = self.f0_var.get()
                    df = self.delta_f_var.get()
                    expected_freqs = [f0-df, f0, f0+df]
                    
                    for exp_f in expected_freqs:
                        if abs(peak['frequency'] - exp_f) <= 2.0:  # 2Hz Toleranz
                            if abs(exp_f - f0) < 0.1:
                                marker = " ← GRUNDTON f₀"
                            elif exp_f < f0:
                                marker = " ← UNTERTON f₁"  
                            else:
                                marker = " ← OBERTON f₂"
                            break
                
                result_text += f"{i:2}. {peak['frequency']:7.2f} Hz  →  {peak['magnitude']:8.4f}  ({peak['magnitudeDB']:+6.1f} dB){marker}\n"
            
            result_text += "\n⚡ TOP ξ-VERHÄLTNISSE:\n"
            result_text += "-" * 50 + "\n"
            for i, ratio in enumerate(xi_ratios[:10], 1):
                result_text += f"{i:2}. ξ({ratio['freqHigh']:7.2f}/{ratio['freqLow']:7.2f}) = {ratio['xiRatio']:6.3f}"
                
                # Spezielle Verhältnisse markieren
                xi_val = ratio['xiRatio']
                if abs(xi_val - 2.0) < 0.1:
                    result_text += " ← OKTAVE (2:1)"
                elif abs(xi_val - 1.5) < 0.1:
                    result_text += " ← QUINTE (3:2)"
                elif 1.01 < xi_val < 1.2:
                    result_text += " ← SCHWEBUNG"
                
                result_text += "\n"
                
            # Schwebungsanalyse
            result_text += "\n🌊 SCHWEBUNGS-ANALYSE:\n"
            result_text += "-" * 50 + "\n"
            
            # Suche nach Schwebungsmustern
            beating_pairs = []
            for ratio in xi_ratios[:10]:
                if 1.01 < ratio['xiRatio'] < 1.3:  # Potentielle Schwebung
                    beat_freq = ratio['freqHigh'] - ratio['freqLow']
                    beating_pairs.append((ratio['freqLow'], ratio['freqHigh'], beat_freq))
            
            if beating_pairs:
                result_text += "Erkannte Schwebungen:\n"
                for low_f, high_f, beat_f in beating_pairs[:5]:
                    result_text += f"   {high_f:.2f} Hz - {low_f:.2f} Hz = {beat_f:.2f} Hz Schwebung\n"
                    
                # Vergleich mit erwartetem Wert (nur für Generator)
                if analysis_type == "generator" and hasattr(self, 'delta_f_var'):
                    expected_beat = 2 * self.delta_f_var.get()
                    actual_beat = beating_pairs[0][2] if beating_pairs else 0
                    result_text += f"\n   Erwartet: {expected_beat:.1f} Hz\n"
                    result_text += f"   Gemessen: {actual_beat:.2f} Hz\n"
                    if abs(expected_beat - actual_beat) <= 1.0:
                        result_text += "   ✅ Schwebung korrekt detektiert!\n"
                    else:
                        result_text += f"   ⚠️  Abweichung: {abs(expected_beat - actual_beat):.2f} Hz\n"
            else:
                result_text += "Keine klaren Schwebungsmuster erkannt.\n"
                
        else:
            result_text += "❌ Keine Peaks gefunden.\n"
            result_text += "Mögliche Ursachen:\n"
            result_text += "• Threshold zu hoch\n"
            result_text += "• Signal zu schwach\n" 
            result_text += "• Falscher Frequenzbereich\n"
            result_text += "• Amplituden-Filter zu restriktiv\n"
        
        self.results_text.insert(tk.END, result_text)

# ===== MAIN FUNCTION =====
def main():
    """Hauptfunktion"""
    
    print("🚀 ξ-FFT Schwebungs-Analyse - Windows GUI")
    print("=" * 50)
    print("Minimale, funktionsfähige Python-Version")
    print("der HTML-Anwendung mit Tkinter GUI")
    print("=" * 50)
    
    # Prüfe Dependencies
    try:
        import tkinter
        import numpy
        import matplotlib
        print("✅ Alle Dependencies verfügbar")
    except ImportError as e:
        print(f"❌ Fehlendes Modul: {e}")
        print("Bitte installieren Sie: pip install numpy matplotlib")
        sys.exit(1)
    
    # Tkinter GUI
    root = tk.Tk()
    
    try:
        # App erstellen
        app = XiFFTApp(root)
        
        print("✅ GUI bereit - Starte Anwendung...")
        print("\nFunktionen:")
        print("• Signal-Generator: Schwebungs-Signale erzeugen")
        print("• Datei-Analyse: WAV-Dateien analysieren")
        print("• ξ-FFT: Spektralanalyse mit Frequenz-Verhältnissen")
        print("• WAV-Export: Signale und Segmente speichern")
        
        # GUI starten
        root.mainloop()
        
    except Exception as e:
        print(f"💥 Kritischer Fehler: {e}")
        messagebox.showerror("Kritischer Fehler", f"Anwendung kann nicht gestartet werden:\n{str(e)}")
        sys.exit(1)
    
    print("👋 ξ-FFT GUI beendet")

if __name__ == "__main__":
    main()
