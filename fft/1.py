"""
ξ-FFT mit ECHTER Schwebungsanalyse und -visualisierung
======================================================

NEUE SCHWEBUNGS-FEATURES:
- Automatische Schwebungsrate-Extraktion
- Amplituden-Hüllkurven-Analyse
- Schwebungs-spezifische Spektrum-Darstellung
- Echtzeit Schwebungsfrequenz-Messung
- Modulationstiefe-Berechnung

Verwendung:
python beating_enhanced_xi_fft.py
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
from scipy import signal as scipy_signal
from scipy.signal import hilbert, find_peaks

# ===== SCHWEBUNGS-ANALYSATOR =====
class BeatingAnalyzer:
    """
    Spezialisierte Schwebungsanalyse mit Hüllkurven-Extraktion
    """
    
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate
        print(f"🌊 BeatingAnalyzer initialisiert: {sample_rate} Hz")
    
    def extract_beating_envelope(self, signal):
        """
        Extrahiere Schwebungs-Hüllkurve mittels Hilbert-Transformation
        """
        try:
            # Hilbert-Transformation für Hüllkurven-Extraktion
            analytic_signal = hilbert(signal)
            envelope = np.abs(analytic_signal)
            
            # Glätte Hüllkurve
            from scipy.signal import savgol_filter
            if len(envelope) > 51:
                envelope_smooth = savgol_filter(envelope, 51, 3)
            else:
                envelope_smooth = envelope
            
            return envelope_smooth
            
        except Exception as e:
            print(f"⚠️ Hüllkurven-Extraktion fehlgeschlagen: {e}")
            return np.abs(signal)  # Fallback
    
    def detect_beating_frequency(self, signal, freq_range=(0.1, 50)):
        """
        Detektiere Schwebungsfrequenz aus Amplituden-Modulation
        """
        try:
            # Extrahiere Hüllkurve
            envelope = self.extract_beating_envelope(signal)
            
            # FFT der Hüllkurve für Schwebungsfrequenz
            N = len(envelope)
            freqs = np.fft.fftfreq(N, 1/self.sample_rate)
            fft_envelope = np.abs(np.fft.fft(envelope))
            
            # Nur positive Frequenzen im Schwebungsbereich
            mask = (freqs >= freq_range[0]) & (freqs <= freq_range[1])
            valid_freqs = freqs[mask]
            valid_fft = fft_envelope[mask]
            
            if len(valid_fft) > 0:
                # Finde dominante Schwebungsfrequenz
                max_idx = np.argmax(valid_fft)
                beating_freq = valid_freqs[max_idx]
                beating_strength = valid_fft[max_idx]
                
                return {
                    'beating_frequency': abs(beating_freq),
                    'beating_strength': beating_strength,
                    'envelope': envelope,
                    'envelope_fft_freqs': valid_freqs,
                    'envelope_fft_magnitude': valid_fft
                }
            else:
                return None
                
        except Exception as e:
            print(f"⚠️ Schwebungsfrequenz-Detektion fehlgeschlagen: {e}")
            return None
    
    def analyze_modulation_depth(self, signal):
        """
        Berechne Modulationstiefe der Schwebung
        """
        try:
            envelope = self.extract_beating_envelope(signal)
            
            max_amp = np.max(envelope)
            min_amp = np.min(envelope)
            
            if max_amp > 0:
                modulation_depth = (max_amp - min_amp) / (max_amp + min_amp)
                modulation_percent = modulation_depth * 100
                
                return {
                    'modulation_depth': modulation_depth,
                    'modulation_percent': modulation_percent,
                    'max_amplitude': max_amp,
                    'min_amplitude': min_amp
                }
            else:
                return None
                
        except Exception as e:
            print(f"⚠️ Modulationstiefe-Analyse fehlgeschlagen: {e}")
            return None
    
    def find_beating_pairs(self, peaks, tolerance=5.0):
        """
        Finde Peak-Paare die Schwebungen erzeugen können
        """
        beating_pairs = []
        
        for i in range(len(peaks)):
            for j in range(i + 1, len(peaks)):
                f1 = peaks[i]['frequency']
                f2 = peaks[j]['frequency']
                
                freq_diff = abs(f1 - f2)
                
                # Schwebungen entstehen bei kleinen Frequenzunterschieden
                if 0.1 <= freq_diff <= tolerance:
                    beating_freq = freq_diff
                    avg_freq = (f1 + f2) / 2
                    
                    beating_pairs.append({
                        'freq1': f1,
                        'freq2': f2,
                        'freq_diff': freq_diff,
                        'beating_frequency': beating_freq,
                        'average_frequency': avg_freq,
                        'magnitude1': peaks[i]['magnitude'],
                        'magnitude2': peaks[j]['magnitude'],
                        'combined_magnitude': peaks[i]['magnitude'] * peaks[j]['magnitude']
                    })
        
        # Sortiere nach kombinierter Magnitude
        beating_pairs.sort(key=lambda x: x['combined_magnitude'], reverse=True)
        return beating_pairs

# ===== ERWEITERTE ξ-FFT MIT SCHWEBUNGSANALYSE =====
class BeatingEnhancedXiFFT:
    """
    ξ-FFT mit integrierter Schwebungsanalyse
    """
    
    def __init__(self, sample_rate=44100, threshold=0.005):
        self.sample_rate = sample_rate
        self.threshold = threshold
        self.beating_analyzer = BeatingAnalyzer(sample_rate)
        
        print(f"🌊 BeatingEnhancedXiFFT initialisiert: {sample_rate} Hz")
    
    def analyze_with_beating_detection(self, signal, freq_range=(20, 2000), progress_callback=None):
        """
        Vollständige Analyse mit Schwebungsdetektion
        """
        start_time = time.time()
        
        print(f"🌊 Starte Schwebungs-erweiterte ξ-FFT Analyse")
        
        if len(signal) == 0:
            return self._empty_result()
        
        # Schritt 1: Standard Peak-Detektion
        if progress_callback:
            progress_callback(20, "Peak-Detektion...")
        
        peaks = self._detect_frequency_peaks(signal, freq_range)
        
        # Schritt 2: Schwebungsanalyse
        if progress_callback:
            progress_callback(50, "Schwebungsanalyse...")
        
        beating_result = self.beating_analyzer.detect_beating_frequency(signal)
        modulation_result = self.beating_analyzer.analyze_modulation_depth(signal)
        beating_pairs = self.beating_analyzer.find_beating_pairs(peaks)
        
        # Schritt 3: ξ-Verhältnisse
        if progress_callback:
            progress_callback(70, "ξ-Verhältnisse...")
        
        xi_ratios = self._calculate_xi_ratios(peaks)
        
        # Schritt 4: Integrierte Auswertung
        if progress_callback:
            progress_callback(90, "Finale Auswertung...")
        
        analysis_time = time.time() - start_time
        
        result = {
            'peaks': peaks,
            'xiRatios': xi_ratios,
            'peakCount': len(peaks),
            'analysisTime': analysis_time,
            
            # NEUE SCHWEBUNGS-DATEN
            'beatingAnalysis': {
                'detected_beating': beating_result,
                'modulation_depth': modulation_result,
                'beating_pairs': beating_pairs,
                'has_beating': beating_result is not None and beating_result['beating_frequency'] > 0.1
            },
            
            'method': 'Enhanced with Beating Detection'
        }
        
        if progress_callback:
            progress_callback(100, "Abgeschlossen!")
        
        print(f"✅ Schwebungsanalyse abgeschlossen: {analysis_time:.2f}s")
        if beating_result:
            print(f"   🌊 Schwebungsfrequenz: {beating_result['beating_frequency']:.2f} Hz")
        
        return result
    
    def _detect_frequency_peaks(self, signal, freq_range):
        """Vereinfachte Peak-Detektion für Schwebungsanalyse"""
        peaks = []
        min_freq, max_freq = freq_range
        
        # Schritt für schnelle Analyse
        step = 1.0  # 1 Hz Schritte
        
        for freq in np.arange(min_freq, max_freq, step):
            magnitude = self._calculate_magnitude(signal, freq)
            
            if magnitude > self.threshold:
                peaks.append({
                    'frequency': round(freq, 2),
                    'magnitude': magnitude,
                    'magnitudeDB': 20 * math.log10(magnitude + 1e-10)
                })
        
        # Lokale Maxima finden (Peak-Refinement)
        peaks = self._refine_peaks(peaks)
        
        peaks.sort(key=lambda x: x['magnitude'], reverse=True)
        return peaks[:20]  # Top 20
    
    def _refine_peaks(self, rough_peaks):
        """Verfeinere Peaks durch lokale Maxima-Suche"""
        if len(rough_peaks) < 3:
            return rough_peaks
        
        refined_peaks = []
        
        for i in range(1, len(rough_peaks) - 1):
            current = rough_peaks[i]
            prev_mag = rough_peaks[i-1]['magnitude']
            next_mag = rough_peaks[i+1]['magnitude']
            
            # Ist lokales Maximum?
            if current['magnitude'] > prev_mag and current['magnitude'] > next_mag:
                refined_peaks.append(current)
        
        return refined_peaks
    
    def _calculate_magnitude(self, signal, frequency):
        """DFT-Magnitude für spezifische Frequenz"""
        N = len(signal)
        real = imag = 0.0
        
        angle_step = -2 * math.pi * frequency / self.sample_rate
        
        for n in range(N):
            angle = angle_step * n
            real += signal[n] * math.cos(angle)
            imag += signal[n] * math.sin(angle)
        
        return math.sqrt(real * real + imag * imag) * 2 / N
    
    def _calculate_xi_ratios(self, peaks):
        """ξ-Verhältniss-Berechnung"""
        ratios = []
        
        for i in range(len(peaks)):
            for j in range(i + 1, len(peaks)):
                f1, f2 = peaks[i]['frequency'], peaks[j]['frequency']
                xi_ratio = max(f1, f2) / min(f1, f2)
                
                if 1.01 <= xi_ratio <= 10.0:
                    ratios.append({
                        'freqHigh': max(f1, f2),
                        'freqLow': min(f1, f2),
                        'xiRatio': round(xi_ratio, 4),
                        'significance': peaks[i]['magnitude'] * peaks[j]['magnitude']
                    })
        
        ratios.sort(key=lambda x: x['significance'], reverse=True)
        return ratios[:15]
    
    def _empty_result(self):
        """Leeres Ergebnis"""
        return {
            'peaks': [],
            'xiRatios': [],
            'peakCount': 0,
            'analysisTime': 0,
            'beatingAnalysis': {
                'detected_beating': None,
                'modulation_depth': None,
                'beating_pairs': [],
                'has_beating': False
            }
        }

# ===== SCHWEBUNGS-OPTIMIERTE GUI =====
class BeatingXiFFTApp:
    """
    GUI mit spezieller Schwebungsvisualisierung
    """
    
    def __init__(self, root):
        self.root = root
        self.root.title("ξ-FFT mit ECHTER Schwebungsanalyse v3.0")
        self.root.geometry("1400x1000")
        
        # Komponenten
        self.xi_fft = BeatingEnhancedXiFFT()
        self.current_signal = None
        self.current_analysis = None
        
        print("🌊 Starte Schwebungs-optimierte ξ-FFT GUI v3.0...")
        self.setup_gui()
    
    def setup_gui(self):
        """Setup GUI mit Schwebungs-Fokus"""
        
        # Header
        header_frame = tk.Frame(self.root, bg='darkblue', height=45)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(header_frame, text="ξ-FFT mit ECHTER Schwebungsanalyse v3.0", 
                              fg='white', bg='darkblue', font=('Arial', 12, 'bold'))
        title_label.pack(side=tk.LEFT, padx=10, pady=8)
        
        self.status_var = tk.StringVar(value="🌊 Bereit für Schwebungsanalyse mit Hüllkurven-Detektion")
        status_label = tk.Label(header_frame, textvariable=self.status_var, 
                               fg='yellow', bg='darkblue', font=('Arial', 9))
        status_label.pack(side=tk.RIGHT, padx=10, pady=8)
        
        # Notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Tabs
        self.setup_beating_generator_tab()
        self.setup_beating_results_tab()
    
    def setup_beating_generator_tab(self):
        """Generator mit Schwebungs-Fokus"""
        gen_frame = ttk.Frame(self.notebook)
        self.notebook.add(gen_frame, text="🌊 Schwebungs-Generator")
        
        # Schwebungs-Parameter
        control_frame = ttk.LabelFrame(gen_frame, text="🌊 Schwebungs-Parameter")
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        param_grid = ttk.Frame(control_frame)
        param_grid.pack(fill=tk.X, padx=5, pady=5)
        
        # Grundfrequenz
        ttk.Label(param_grid, text="Grundfrequenz f₀ (Hz):").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.f0_var = tk.DoubleVar(value=440.0)
        ttk.Spinbox(param_grid, from_=100.0, to=1000.0, increment=10.0, 
                   textvariable=self.f0_var, width=10,
                   command=self.update_beating_preview).grid(row=0, column=1, padx=5, pady=2)
        
        # Schwebungsfrequenz (direkter Parameter!)
        ttk.Label(param_grid, text="Schwebungsfrequenz (Hz):").grid(row=0, column=2, sticky=tk.W, padx=5, pady=2)
        self.beat_freq_var = tk.DoubleVar(value=3.0)
        ttk.Spinbox(param_grid, from_=0.1, to=20.0, increment=0.1, 
                   textvariable=self.beat_freq_var, width=10,
                   command=self.update_beating_preview).grid(row=0, column=3, padx=5, pady=2)
        
        # Modulationstiefe
        ttk.Label(param_grid, text="Modulationstiefe (%):").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.mod_depth_var = tk.DoubleVar(value=50.0)
        ttk.Spinbox(param_grid, from_=10.0, to=100.0, increment=5.0, 
                   textvariable=self.mod_depth_var, width=10,
                   command=self.update_beating_preview).grid(row=1, column=1, padx=5, pady=2)
        
        # Dauer
        ttk.Label(param_grid, text="Dauer (s):").grid(row=1, column=2, sticky=tk.W, padx=5, pady=2)
        self.duration_var = tk.DoubleVar(value=3.0)
        ttk.Spinbox(param_grid, from_=2.0, to=8.0, increment=0.5, 
                   textvariable=self.duration_var, width=8,
                   command=self.update_beating_preview).grid(row=1, column=3, padx=5, pady=2)
        
        # Schwebungs-Vorschau
        preview_frame = ttk.LabelFrame(gen_frame, text="🌊 Schwebungs-Vorschau")
        preview_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.beating_preview_var = tk.StringVar()
        ttk.Label(preview_frame, textvariable=self.beating_preview_var, 
                 foreground="darkgreen", font=('Courier', 10)).pack(pady=5)
        
        # Buttons
        btn_frame = ttk.Frame(gen_frame)
        btn_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Button(btn_frame, text="🌊 Schwebungs-Signal generieren", 
                  command=self.generate_beating_signal).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="🔍 Mit Schwebungsdetektion analysieren", 
                  command=self.analyze_beating_signal).pack(side=tk.LEFT, padx=5)
        
        # Status
        self.gen_status_var = tk.StringVar(value="🌊 Bereit für Schwebungs-Generierung")
        ttk.Label(gen_frame, textvariable=self.gen_status_var, 
                 foreground="blue").pack(pady=5)
        
        self.gen_progress_var = tk.DoubleVar()
        self.gen_progress = ttk.Progressbar(gen_frame, variable=self.gen_progress_var, maximum=100)
        self.gen_progress.pack(fill=tk.X, padx=10, pady=2)
        
        # Initial-Update
        self.update_beating_preview()
    
    def setup_beating_results_tab(self):
        """Ergebnisse mit Schwebungs-Visualisierung"""
        results_frame = ttk.Frame(self.notebook)
        self.notebook.add(results_frame, text="📊 Schwebungs-Ergebnisse")
        
        # Schwebungs-Metriken
        metrics_frame = ttk.LabelFrame(results_frame, text="🌊 Schwebungs-Metriken")
        metrics_frame.pack(fill=tk.X, padx=10, pady=5)
        
        metrics_grid = ttk.Frame(metrics_frame)
        metrics_grid.pack(fill=tk.X, pady=5)
        
        # 4 Spalten für Schwebungs-Metriken
        col_frames = []
        for i in range(4):
            col = ttk.Frame(metrics_grid)
            col.grid(row=0, column=i, padx=5, pady=5, sticky=tk.N)
            col_frames.append(col)
        
        # Spalte 1: Schwebungsfrequenz
        ttk.Label(col_frames[0], text="Schwebungsfrequenz:", font=('Arial', 9, 'bold')).pack()
        self.detected_beat_freq_var = tk.StringVar(value="--")
        ttk.Label(col_frames[0], textvariable=self.detected_beat_freq_var, foreground="blue").pack()
        
        # Spalte 2: Modulationstiefe
        ttk.Label(col_frames[1], text="Modulationstiefe:", font=('Arial', 9, 'bold')).pack()
        self.detected_mod_depth_var = tk.StringVar(value="--")
        ttk.Label(col_frames[1], textvariable=self.detected_mod_depth_var, foreground="green").pack()
        
        # Spalte 3: Schwebungs-Paare
        ttk.Label(col_frames[2], text="Schwebungs-Paare:", font=('Arial', 9, 'bold')).pack()
        self.beating_pairs_var = tk.StringVar(value="--")
        ttk.Label(col_frames[2], textvariable=self.beating_pairs_var, foreground="orange").pack()
        
        # Spalte 4: Genauigkeit
        ttk.Label(col_frames[3], text="Detektions-Genauigkeit:", font=('Arial', 9, 'bold')).pack()
        self.detection_accuracy_var = tk.StringVar(value="--")
        ttk.Label(col_frames[3], textvariable=self.detection_accuracy_var, foreground="red").pack()
        
        # Matplotlib Plots (2x2 für Schwebungsanalyse)
        self.fig = Figure(figsize=(12, 8), facecolor='white')
        self.canvas = FigureCanvasTkAgg(self.fig, results_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # 2x2 Layout optimiert für Schwebungsanalyse
        self.ax_waveform = self.fig.add_subplot(2, 2, 1)
        self.ax_envelope = self.fig.add_subplot(2, 2, 2)
        self.ax_spectrum = self.fig.add_subplot(2, 2, 3)
        self.ax_beating_spectrum = self.fig.add_subplot(2, 2, 4)
        
        self.ax_waveform.set_title('Zeitverlauf mit Schwebung')
        self.ax_envelope.set_title('Amplituden-Hüllkurve')
        self.ax_spectrum.set_title('Frequenzspektrum')
        self.ax_beating_spectrum.set_title('Schwebungs-Spektrum')
        
        self.fig.tight_layout()
        
        # Schwebungs-Analyse Text
        text_frame = ttk.Frame(results_frame)
        text_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.results_text = tk.Text(text_frame, height=6, width=100)
        scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scrollbar.set)
        
        self.results_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # ===== SCHWEBUNGS-FUNKTIONEN =====
    def update_beating_preview(self):
        """Update Schwebungs-Vorschau"""
        try:
            f0 = self.f0_var.get()
            beat_freq = self.beat_freq_var.get()
            mod_depth = self.mod_depth_var.get()
            duration = self.duration_var.get()
            
            # Berechne resultierende Frequenzen
            f1 = f0 - beat_freq/2
            f2 = f0 + beat_freq/2
            
            preview_text = f"🌊 Schwebungs-Konfiguration:\n"
            preview_text += f"Trägerfrequenzen: {f1:.2f} Hz + {f2:.2f} Hz\n"
            preview_text += f"Erwartete Schwebung: {beat_freq:.1f} Hz bei {mod_depth:.0f}% Modulationstiefe\n"
            preview_text += f"Signal-Dauer: {duration:.1f}s → {int(beat_freq * duration)} Schwebungszyklen"
            
            self.beating_preview_var.set(preview_text)
            
        except tk.TclError:
            pass  # Fehler bei unvollständiger Eingabe ignorieren
    
    def generate_beating_signal(self):
        """Generiere präzises Schwebungs-Signal"""
        try:
            f0 = self.f0_var.get()
            beat_freq = self.beat_freq_var.get()  
            mod_depth = self.mod_depth_var.get() / 100.0  # Prozent zu Dezimal
            duration = self.duration_var.get()
            
            self.gen_status_var.set("🌊 Generiere Schwebungs-Signal...")
            self.gen_progress_var.set(25)
            self.root.update()
            
            # Zeitachse
            sample_rate = 44100
            t = np.linspace(0, duration, int(duration * sample_rate))
            
            # Zwei nahe Frequenzen für echte Schwebung
            f1 = f0 - beat_freq/2
            f2 = f0 + beat_freq/2
            
            # Amplituden-moduliertes Signal
            carrier1 = np.sin(2 * np.pi * f1 * t)
            carrier2 = np.sin(2 * np.pi * f2 * t)
            
            # Kombiniere für Schwebungseffekt
            signal = 0.5 * (carrier1 + carrier2)
            
            # Zusätzliche Amplituden-Modulation für stärkere Schwebung
            modulation = 1 + mod_depth * np.sin(2 * np.pi * beat_freq * t)
            signal = signal * modulation
            
            # Normalisierung
            signal = signal / np.max(np.abs(signal)) * 0.7
            
            self.current_signal = signal
            self.gen_progress_var.set(100)
            self.gen_status_var.set(f"✅ Schwebungs-Signal generiert: {len(signal)} Samples")
            
            self.status_var.set(f"🌊 Schwebungs-Signal bereit - {beat_freq:.1f} Hz Schwebung")
            
            # Zur Ergebnisse-Tab
            self.notebook.select(1)
            self.plot_generated_beating_signal()
            
        except Exception as e:
            self.gen_status_var.set(f"❌ Fehler: {str(e)}")
            messagebox.showerror("Fehler", f"Schwebungs-Generierung fehlgeschlagen:\n{str(e)}")
    
    def analyze_beating_signal(self):
        """Analysiere Signal mit Schwebungsdetektion"""
        if self.current_signal is None:
            messagebox.showwarning("Warnung", "Erst Schwebungs-Signal generieren!")
            return
        
        def analyze_thread():
            try:
                def progress_callback(progress, text):
                    self.gen_progress_var.set(progress)
                    self.gen_status_var.set(f"🔍 {text}")
                    self.root.update()
                
                analysis = self.xi_fft.analyze_with_beating_detection(
                    self.current_signal,
                    freq_range=(50, 2000),
                    progress_callback=progress_callback
                )
                
                self.current_analysis = analysis
                
                # UI-Update im Hauptthread
                self.root.after(0, lambda: self.display_beating_results(analysis))
                
            except Exception as e:
                self.root.after(0, lambda: self.handle_beating_error(str(e)))
        
        threading.Thread(target=analyze_thread, daemon=True).start()
    
    def plot_generated_beating_signal(self):
        """Plotte generiertes Schwebungs-Signal (ohne Analyse)"""
        if self.current_signal is None:
            return
        
        # Zeitverlauf mit Schwebung
        self.ax_waveform.clear()
        self.ax_waveform.set_title('Generiertes Schwebungs-Signal', fontsize=10)
        
        sample_rate = 44100
        duration = len(self.current_signal) / sample_rate
        
        # Zeige nur ersten Teil für bessere Sichtbarkeit
        display_duration = min(1.0, duration)  # Max 1 Sekunde
        display_samples = int(display_duration * sample_rate)
        
        t = np.linspace(0, display_duration, display_samples)
        signal_segment = self.current_signal[:display_samples]
        
        self.ax_waveform.plot(t, signal_segment, 'b-', linewidth=0.8)
        self.ax_waveform.set_xlabel('Zeit (s)')
        self.ax_waveform.set_ylabel('Amplitude')
        self.ax_waveform.grid(True, alpha=0.3)
        
        # Schwebungs-Info
        beat_freq = self.beat_freq_var.get()
        self.ax_waveform.text(0.02, 0.98, f'Erwartete Schwebung:\n{beat_freq:.1f} Hz', 
                            transform=self.ax_waveform.transAxes, fontsize=9, 
                            verticalalignment='top',
                            bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.7))
        
        # Andere Plots leeren
        for ax in [self.ax_envelope, self.ax_spectrum, self.ax_beating_spectrum]:
            ax.clear()
            ax.text(0.5, 0.5, 'Warten auf\nSchwebungsanalyse...', 
                   ha='center', va='center', transform=ax.transAxes)
        
        self.canvas.draw()
    
    def display_beating_results(self, analysis):
        """Zeige Schwebungsanalyse-Ergebnisse"""
        try:
            beating_analysis = analysis['beatingAnalysis']
            
            # Update Metriken
            detected_beating = beating_analysis['detected_beating']
            modulation_depth = beating_analysis['modulation_depth']
            beating_pairs = beating_analysis['beating_pairs']
            
            if detected_beating:
                self.detected_beat_freq_var.set(f"{detected_beating['beating_frequency']:.2f} Hz")
            else:
                self.detected_beat_freq_var.set("Nicht erkannt")
            
            if modulation_depth:
                self.detected_mod_depth_var.set(f"{modulation_depth['modulation_percent']:.1f}%")
            else:
                self.detected_mod_depth_var.set("Nicht messbar")
            
            self.beating_pairs_var.set(f"{len(beating_pairs)} Paare")
            
            # Genauigkeits-Bewertung
            expected_beat_freq = self.beat_freq_var.get()
            if detected_beating:
                actual_beat_freq = detected_beating['beating_frequency']
                accuracy = max(0, 100 - abs(expected_beat_freq - actual_beat_freq) / expected_beat_freq * 100)
                self.detection_accuracy_var.set(f"{accuracy:.1f}%")
            else:
                self.detection_accuracy_var.set("0%")
            
            # Plots
            self.plot_beating_analysis(analysis)
            
            # Text-Ergebnisse
            self.display_beating_text_results(analysis)
            
            # Status
            self.gen_status_var.set("✅ Schwebungsanalyse abgeschlossen")
            self.gen_progress_var.set(100)
            
            if detected_beating:
                beat_freq = detected_beating['beating_frequency']
                self.status_var.set(f"🌊 Schwebung detektiert: {beat_freq:.2f} Hz")
            else:
                self.status_var.set("⚠️ Keine eindeutige Schwebung detektiert")
            
        except Exception as e:
            print(f"❌ Display Error: {e}")
            messagebox.showerror("Fehler", f"Ergebnisse-Anzeige fehlgeschlagen:\n{str(e)}")
    
    def plot_beating_analysis(self, analysis):
        """Plotte komplette Schwebungsanalyse"""
        if self.current_signal is None:
            return
        
        sample_rate = 44100
        duration = len(self.current_signal) / sample_rate
        beating_analysis = analysis['beatingAnalysis']
        
        # 1. Zeitverlauf mit Schwebung
        self.ax_waveform.clear()
        self.ax_waveform.set_title('Zeitverlauf mit detektierter Schwebung', fontsize=10)
        
        # Zeige repräsentativen Ausschnitt
        display_duration = min(2.0, duration)
        display_samples = int(display_duration * sample_rate)
        t = np.linspace(0, display_duration, display_samples)
        signal_segment = self.current_signal[:display_samples]
        
        self.ax_waveform.plot(t, signal_segment, 'b-', linewidth=0.8, alpha=0.7, label='Signal')
        
        # Hüllkurve überlagern
        detected_beating = beating_analysis['detected_beating']
        if detected_beating and 'envelope' in detected_beating:
            envelope_segment = detected_beating['envelope'][:display_samples]
            self.ax_waveform.plot(t, envelope_segment, 'r-', linewidth=2, alpha=0.8, label='Hüllkurve')
            self.ax_waveform.plot(t, -envelope_segment, 'r-', linewidth=2, alpha=0.8)
        
        self.ax_waveform.set_xlabel('Zeit (s)')
        self.ax_waveform.set_ylabel('Amplitude')
        self.ax_waveform.legend()
        self.ax_waveform.grid(True, alpha=0.3)
        
        # 2. Hüllkurven-Detail
        self.ax_envelope.clear()
        self.ax_envelope.set_title('Amplituden-Hüllkurve (Schwebungsdetektion)', fontsize=10)
        
        if detected_beating and 'envelope' in detected_beating:
            envelope = detected_beating['envelope'][:display_samples]
            self.ax_envelope.plot(t, envelope, 'g-', linewidth=2, label='Extrahierte Hüllkurve')
            
            # Schwebungsfrequenz markieren
            beat_freq = detected_beating['beating_frequency']
            if beat_freq > 0:
                # Theoretische Schwebungskurve
                theoretical_envelope = 0.5 + 0.3 * np.cos(2 * np.pi * beat_freq * t)
                theoretical_envelope *= np.mean(envelope)  # Skaliere auf gemessene Amplitude
                self.ax_envelope.plot(t, theoretical_envelope, 'r--', linewidth=1.5, 
                                    alpha=0.7, label=f'Theoretisch {beat_freq:.1f} Hz')
            
            self.ax_envelope.set_xlabel('Zeit (s)')
            self.ax_envelope.set_ylabel('Hüllkurven-Amplitude')
            self.ax_envelope.legend()
            self.ax_envelope.grid(True, alpha=0.3)
        else:
            self.ax_envelope.text(0.5, 0.5, 'Keine Hüllkurve\nextrahiert', 
                                ha='center', va='center', transform=self.ax_envelope.transAxes)
        
        # 3. Frequenzspektrum
        self.ax_spectrum.clear()
        self.ax_spectrum.set_title('Frequenzspektrum', fontsize=10)
        
        peaks = analysis['peaks']
        if peaks:
            frequencies = [p['frequency'] for p in peaks[:10]]
            magnitudes = [p['magnitude'] for p in peaks[:10]]
            
            bars = self.ax_spectrum.bar(frequencies, magnitudes, width=2, alpha=0.8, color='steelblue')
            
            # Markiere erwartete Frequenzen
            expected_f1 = self.f0_var.get() - self.beat_freq_var.get()/2
            expected_f2 = self.f0_var.get() + self.beat_freq_var.get()/2
            
            self.ax_spectrum.axvline(x=expected_f1, color='red', linestyle='--', alpha=0.7, label=f'Erwartet f1={expected_f1:.1f}')
            self.ax_spectrum.axvline(x=expected_f2, color='red', linestyle='--', alpha=0.7, label=f'Erwartet f2={expected_f2:.1f}')
            
            self.ax_spectrum.set_xlabel('Frequenz (Hz)')
            self.ax_spectrum.set_ylabel('Magnitude')
            self.ax_spectrum.legend()
            self.ax_spectrum.grid(True, alpha=0.3)
        else:
            self.ax_spectrum.text(0.5, 0.5, 'Keine Peaks\ngefunden', 
                                ha='center', va='center', transform=self.ax_spectrum.transAxes)
        
        # 4. Schwebungs-Spektrum (FFT der Hüllkurve)
        self.ax_beating_spectrum.clear()
        self.ax_beating_spectrum.set_title('Schwebungs-Spektrum (Hüllkurven-FFT)', fontsize=10)
        
        if detected_beating and 'envelope_fft_freqs' in detected_beating:
            freqs = detected_beating['envelope_fft_freqs']
            magnitudes = detected_beating['envelope_fft_magnitude']
            
            # Normalisiere für bessere Darstellung
            magnitudes = magnitudes / np.max(magnitudes)
            
            self.ax_beating_spectrum.plot(freqs, magnitudes, 'purple', linewidth=2, label='Hüllkurven-FFT')
            
            # Markiere detektierte Schwebungsfrequenz
            beat_freq = detected_beating['beating_frequency']
            max_idx = np.argmax(magnitudes)
            peak_freq = freqs[max_idx]
            
            self.ax_beating_spectrum.axvline(x=peak_freq, color='red', linestyle='-', linewidth=3, 
                                           alpha=0.7, label=f'Detektiert: {beat_freq:.2f} Hz')
            
            # Erwartete Schwebungsfrequenz
            expected_beat = self.beat_freq_var.get()
            self.ax_beating_spectrum.axvline(x=expected_beat, color='green', linestyle='--', linewidth=2, 
                                           alpha=0.7, label=f'Erwartet: {expected_beat:.1f} Hz')
            
            self.ax_beating_spectrum.set_xlabel('Schwebungsfrequenz (Hz)')
            self.ax_beating_spectrum.set_ylabel('Relative Magnitude')
            self.ax_beating_spectrum.legend()
            self.ax_beating_spectrum.grid(True, alpha=0.3)
            self.ax_beating_spectrum.set_xlim(0, min(20, np.max(freqs)))
        else:
            self.ax_beating_spectrum.text(0.5, 0.5, 'Kein Schwebungs-\nSpektrum verfügbar', 
                                        ha='center', va='center', transform=self.ax_beating_spectrum.transAxes)
        
        self.canvas.draw()
    
    def display_beating_text_results(self, analysis):
        """Zeige detaillierte Schwebungsanalyse als Text"""
        self.results_text.delete(1.0, tk.END)
        
        text = "=== ξ-FFT SCHWEBUNGSANALYSE v3.0 ===\n\n"
        
        beating_analysis = analysis['beatingAnalysis']
        detected_beating = beating_analysis['detected_beating']
        modulation_depth = beating_analysis['modulation_depth']
        beating_pairs = beating_analysis['beating_pairs']
        
        # Schwebungs-Detektion
        text += "🌊 SCHWEBUNGS-DETEKTION:\n"
        text += "-" * 40 + "\n"
        
        if detected_beating:
            beat_freq = detected_beating['beating_frequency']
            beat_strength = detected_beating['beating_strength']
            
            text += f"✅ Schwebung detektiert: {beat_freq:.2f} Hz\n"
            text += f"   Signalstärke: {beat_strength:.1f}\n"
            
            # Vergleich mit Erwartung
            expected_beat = self.beat_freq_var.get()
            deviation = abs(beat_freq - expected_beat)
            deviation_percent = (deviation / expected_beat) * 100 if expected_beat > 0 else 0
            
            text += f"   Erwartete Schwebung: {expected_beat:.1f} Hz\n"
            text += f"   Abweichung: {deviation:.2f} Hz ({deviation_percent:.1f}%)\n"
            
            if deviation_percent <= 5:
                text += "   🎯 EXZELLENTE Übereinstimmung!\n"
            elif deviation_percent <= 15:
                text += "   ✅ Gute Übereinstimmung\n"
            elif deviation_percent <= 30:
                text += "   ⚠️ Moderate Abweichung\n"
            else:
                text += "   ❌ Hohe Abweichung - Prüfen Sie Parameter\n"
        else:
            text += "❌ Keine Schwebung detektiert\n"
            text += "   Mögliche Ursachen:\n"
            text += "   • Schwebungsfrequenz zu niedrig/hoch\n"
            text += "   • Modulationstiefe zu gering\n"
            text += "   • Signal zu kurz\n"
        
        text += "\n"
        
        # Modulationstiefe
        text += "📊 MODULATIONSANALYSE:\n"
        text += "-" * 40 + "\n"
        
        if modulation_depth:
            mod_percent = modulation_depth['modulation_percent']
            max_amp = modulation_depth['max_amplitude']
            min_amp = modulation_depth['min_amplitude']
            
            text += f"Modulationstiefe: {mod_percent:.1f}%\n"
            text += f"Max. Amplitude: {max_amp:.3f}\n"
            text += f"Min. Amplitude: {min_amp:.3f}\n"
            
            # Vergleich mit Erwartung
            expected_mod = self.mod_depth_var.get()
            mod_deviation = abs(mod_percent - expected_mod)
            
            text += f"Erwartete Modulation: {expected_mod:.0f}%\n"
            text += f"Abweichung: {mod_deviation:.1f}%\n"
            
            if mod_deviation <= 10:
                text += "✅ Modulationstiefe korrekt detektiert\n"
            else:
                text += "⚠️ Modulationstiefe weicht ab\n"
        else:
            text += "❌ Modulationstiefe nicht messbar\n"
        
        text += "\n"
        
        # Frequenz-Paare
        text += "🎵 SCHWEBUNGS-PAARE:\n"
        text += "-" * 40 + "\n"
        
        if beating_pairs:
            text += f"Gefundene Frequenz-Paare: {len(beating_pairs)}\n\n"
            
            for i, pair in enumerate(beating_pairs[:5], 1):
                f1 = pair['freq1']
                f2 = pair['freq2']
                beat_f = pair['beating_frequency']
                avg_f = pair['average_frequency']
                
                text += f"{i}. {f1:.2f} Hz + {f2:.2f} Hz\n"
                text += f"   → Schwebung: {beat_f:.2f} Hz (Träger: {avg_f:.1f} Hz)\n"
                
                # Bewertung
                expected_f1 = self.f0_var.get() - self.beat_freq_var.get()/2
                expected_f2 = self.f0_var.get() + self.beat_freq_var.get()/2
                
                if (abs(f1 - expected_f1) <= 2 and abs(f2 - expected_f2) <= 2) or \
                   (abs(f1 - expected_f2) <= 2 and abs(f2 - expected_f1) <= 2):
                    text += "   ✅ Stimmt mit erwarteten Frequenzen überein\n"
                else:
                    text += "   ⚠️ Abweichung von erwarteten Frequenzen\n"
                
                text += "\n"
        else:
            text += "❌ Keine Schwebungs-Paare gefunden\n"
            text += "   Frequenzen sind möglicherweise zu weit auseinander\n"
        
        # Performance
        text += "⚡ ANALYSE-PERFORMANCE:\n"
        text += "-" * 40 + "\n"
        text += f"Analysezeit: {analysis['analysisTime']:.3f}s\n"
        text += f"Gefundene Peaks: {analysis['peakCount']}\n"
        text += f"ξ-Verhältnisse: {len(analysis['xiRatios'])}\n"
        
        # Empfehlungen
        text += "\n💡 OPTIMIERUNGS-EMPFEHLUNGEN:\n"
        text += "-" * 40 + "\n"
        
        if not detected_beating:
            text += "• Erhöhen Sie die Modulationstiefe (>30%)\n"
            text += "• Verlängern Sie die Signal-Dauer (>3s)\n"
            text += "• Reduzieren Sie die Schwebungsfrequenz (<10Hz)\n"
        elif detected_beating and modulation_depth and modulation_depth['modulation_percent'] < 30:
            text += "• Schwebung detektiert aber schwach\n"
            text += "• Erhöhen Sie die Modulationstiefe für bessere Ergebnisse\n"
        else:
            text += "✅ Optimale Schwebungsparameter\n"
            text += "• Schwebung klar detektiert\n"
            text += "• Modulationstiefe ausreichend\n"
            text += "• Frequenz-Paare korrekt identifiziert\n"
        
        self.results_text.insert(tk.END, text)
    
    def handle_beating_error(self, error_msg):
        """Handle Schwebungsanalyse-Fehler"""
        self.gen_status_var.set(f"❌ Schwebungsanalyse fehlgeschlagen")
        self.gen_progress_var.set(0)
        self.status_var.set("❌ Schwebungsanalyse-Fehler")
        
        self.detected_beat_freq_var.set("Fehler")
        self.detected_mod_depth_var.set("Fehler") 
        self.beating_pairs_var.set("Fehler")
        self.detection_accuracy_var.set("0%")
        
        messagebox.showerror("Schwebungsanalyse Fehler", f"Schwebungsanalyse fehlgeschlagen:\n{error_msg}")

# ===== MAIN FUNCTION =====
def main():
    """Hauptfunktion für Schwebungs-optimierte ξ-FFT"""
    
    print("🌊 ξ-FFT mit ECHTER Schwebungsanalyse v3.0")
    print("=" * 60)
    print("🎯 Neue Schwebungs-Features:")
    print("   • Automatische Schwebungsfrequenz-Extraktion")
    print("   • Amplituden-Hüllkurven-Analyse (Hilbert-Transform)")
    print("   • Schwebungs-spezifische Spektrum-Darstellung")
    print("   • Modulationstiefe-Messung")
    print("   • Echtzeit Schwebungsparameter-Vergleich")
    print("   • Präzise Schwebungs-Paare-Detektion")
    print("=" * 60)
    
    # Prüfe Dependencies (erweitert für scipy)
    try:
        import tkinter
        import numpy
        import matplotlib
        import scipy
        print("✅ Alle Dependencies verfügbar (inkl. scipy für Schwebungsanalyse)")
    except ImportError as e:
        print(f"❌ Fehlendes Modul: {e}")
        print("Bitte installieren Sie: pip install numpy matplotlib scipy")
        sys.exit(1)
    
    # GUI starten
    root = tk.Tk()
    
    try:
        app = BeatingXiFFTApp(root)
        
        print("✅ Schwebungs-optimierte GUI bereit")
        print("\n🌊 SCHWEBUNGS-FEATURES:")
        print("• Hilbert-Transformation für Hüllkurven-Extraktion")
        print("• FFT der Amplituden-Hüllkurve für Schwebungsfrequenz")
        print("• Automatische Frequenz-Paar-Detektion")
        print("• Echtzeit Modulationstiefe-Messung")
        print("• Präzise Schwebungsparameter-Vergleiche")
        print("• 4-Panel Schwebungsvisualisierung")
        
        root.mainloop()
        
    except Exception as e:
        print(f"💥 Kritischer Fehler: {e}")
        messagebox.showerror("Kritischer Fehler", f"Schwebungsanalyse-App kann nicht gestartet werden:\n{str(e)}")
        sys.exit(1)
    
    print("👋 Schwebungs-optimierte ξ-FFT v3.0 beendet")
    print("🌊 Echte Schwebungsanalyse war aktiv")

if __name__ == "__main__":
    main()
