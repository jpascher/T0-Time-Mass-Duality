#!/usr/bin/env python3
"""
ξ-FFT Interactive Demo - Direkte Nutzung der lokalen Bibliothek
Keine Flask-Server erforderlich - läuft direkt mit der xi_fft_library.py
"""

import sys
import os
import math
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time

# Importiere die lokale xi_fft_library
try:
    from xi_fft_library import XiFFT, XiAnomalyDetector, create_test_signal
    print("✅ xi_fft_library erfolgreich importiert")
except ImportError as e:
    print(f"❌ Fehler beim Importieren: {e}")
    print("Stelle sicher, dass xi_fft_library.py im gleichen Verzeichnis liegt")
    sys.exit(1)

class XiFFTDemo:
    """
    Interaktive GUI-Demo für ξ-FFT Analyse
    Fokussiert auf mittleren Oktavbereich (80-800 Hz)
    """
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ξ-FFT Interactive Demo - Direkte Python-Bibliothek")
        self.root.geometry("1200x800")
        
        # Aktuelle Parameter
        self.current_signal = []
        self.current_freqs = []
        self.current_amps = []
        self.analysis_result = None
        self.auto_update = False
        
        # XiFFT Instanz mit fokussiertem Bereich
        self.xi_fft = XiFFT(sample_rate=1000, threshold=0.03)
        
        # GUI aufbauen
        self.setup_gui()
        
        # Matplotlib für Plots
        self.setup_plots()
        
        # Initialisiere mit Standard-Werten
        self.update_displays()
        
    def setup_gui(self):
        """Erstelle die Benutzeroberfläche"""
        
        # Hauptframe
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Titel
        title_label = ttk.Label(main_frame, text="ξ-FFT Interactive Demo", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Info-Text
        info_text = ("Spektralanalyse durch Frequenz-Verhältnisse\n"
                    "Fokussiert auf mittleren Oktavbereich (80-800 Hz)\n"
                    "Verhindert Oktaven-Sprünge durch begrenzte Analyse")
        info_label = ttk.Label(main_frame, text=info_text, 
                              font=("Arial", 10), foreground="blue")
        info_label.grid(row=1, column=0, columnspan=3, pady=(0, 20))
        
        # Linke Spalte: Steuerung
        self.setup_controls(main_frame)
        
        # Rechte Spalte: Ergebnisse
        self.setup_results(main_frame)
        
        # Unten: Plots (werden später mit matplotlib hinzugefügt)
        self.plot_frame = ttk.Frame(main_frame)
        self.plot_frame.grid(row=2, column=0, columnspan=3, pady=20, sticky=(tk.W, tk.E))
        
    def setup_controls(self, parent):
        """Erstelle Steuerelemente"""
        
        # Steuerungs-Frame
        control_frame = ttk.LabelFrame(parent, text="🎵 Schwebungs-Generator", padding="10")
        control_frame.grid(row=2, column=0, padx=(0, 10), sticky=(tk.W, tk.E, tk.N))
        
        row = 0
        
        # Grundton-Auswahl
        ttk.Label(control_frame, text="Grundton:").grid(row=row, column=0, sticky=tk.W)
        self.note_var = tk.StringVar(value="A")
        note_combo = ttk.Combobox(control_frame, textvariable=self.note_var, 
                                 values=["C", "C#", "D", "D#", "E", "F", 
                                        "F#", "G", "G#", "A", "A#", "B"],
                                 state="readonly")
        note_combo.grid(row=row, column=1, padx=(5, 0), sticky=(tk.W, tk.E))
        note_combo.bind('<<ComboboxSelected>>', self.on_parameter_change)
        row += 1
        
        # Oktave (begrenzt auf mittleren Bereich)
        ttk.Label(control_frame, text="Oktave:").grid(row=row, column=0, sticky=tk.W)
        self.octave_var = tk.IntVar(value=4)
        octave_scale = ttk.Scale(control_frame, from_=2, to=6, variable=self.octave_var,
                               orient=tk.HORIZONTAL, command=self.on_parameter_change)
        octave_scale.grid(row=row, column=1, padx=(5, 0), sticky=(tk.W, tk.E))
        self.octave_label = ttk.Label(control_frame, text="4")
        self.octave_label.grid(row=row, column=2, padx=(5, 0))
        row += 1
        
        # Schwebungs-Rate
        ttk.Label(control_frame, text="Schwebungs-Rate (Hz):").grid(row=row, column=0, sticky=tk.W)
        self.beat_rate_var = tk.DoubleVar(value=2.0)
        beat_scale = ttk.Scale(control_frame, from_=0.5, to=8.0, variable=self.beat_rate_var,
                             orient=tk.HORIZONTAL, command=self.on_parameter_change)
        beat_scale.grid(row=row, column=1, padx=(5, 0), sticky=(tk.W, tk.E))
        self.beat_rate_label = ttk.Label(control_frame, text="2.0 Hz")
        self.beat_rate_label.grid(row=row, column=2, padx=(5, 0))
        row += 1
        
        # Grundton-Amplitude
        ttk.Label(control_frame, text="Grundton-Amplitude:").grid(row=row, column=0, sticky=tk.W)
        self.base_amp_var = tk.DoubleVar(value=0.8)
        base_amp_scale = ttk.Scale(control_frame, from_=0.0, to=1.0, variable=self.base_amp_var,
                                 orient=tk.HORIZONTAL, command=self.on_parameter_change)
        base_amp_scale.grid(row=row, column=1, padx=(5, 0), sticky=(tk.W, tk.E))
        self.base_amp_label = ttk.Label(control_frame, text="0.8")
        self.base_amp_label.grid(row=row, column=2, padx=(5, 0))
        row += 1
        
        # Schwebungs-Amplitude
        ttk.Label(control_frame, text="Schwebungs-Amplitude:").grid(row=row, column=0, sticky=tk.W)
        self.beat_amp_var = tk.DoubleVar(value=0.6)
        beat_amp_scale = ttk.Scale(control_frame, from_=0.0, to=1.0, variable=self.beat_amp_var,
                                 orient=tk.HORIZONTAL, command=self.on_parameter_change)
        beat_amp_scale.grid(row=row, column=1, padx=(5, 0), sticky=(tk.W, tk.E))
        self.beat_amp_label = ttk.Label(control_frame, text="0.6")
        self.beat_amp_label.grid(row=row, column=2, padx=(5, 0))
        row += 1
        
        # Buttons
        button_frame = ttk.Frame(control_frame)
        button_frame.grid(row=row, column=0, columnspan=3, pady=10)
        
        ttk.Button(button_frame, text="🎵 Generieren & Analysieren", 
                  command=self.generate_and_analyze).pack(side=tk.LEFT, padx=2)
        ttk.Button(button_frame, text="🔍 Nur Analysieren", 
                  command=self.analyze_only).pack(side=tk.LEFT, padx=2)
        
        # Auto-Update Checkbox
        self.auto_update_var = tk.BooleanVar()
        auto_checkbox = ttk.Checkbutton(button_frame, text="Auto-Update", 
                                       variable=self.auto_update_var,
                                       command=self.toggle_auto_update)
        auto_checkbox.pack(side=tk.LEFT, padx=10)
        row += 1
        
        # Presets
        preset_frame = ttk.LabelFrame(control_frame, text="Presets", padding="5")
        preset_frame.grid(row=row, column=0, columnspan=3, pady=10, sticky=(tk.W, tk.E))
        
        presets = [
            ("Reiner Ton", self.preset_pure),
            ("Leichte Schwebung", self.preset_light_beat),
            ("Starke Schwebung", self.preset_heavy_beat),
            ("Klavier", self.preset_piano)
        ]
        
        for i, (name, command) in enumerate(presets):
            ttk.Button(preset_frame, text=name, command=command).grid(
                row=i//2, column=i%2, padx=2, pady=2, sticky=(tk.W, tk.E))
        
        # Spalten-Konfiguration
        control_frame.columnconfigure(1, weight=1)
        preset_frame.columnconfigure(0, weight=1)
        preset_frame.columnconfigure(1, weight=1)
        
    def setup_results(self, parent):
        """Erstelle Ergebnis-Anzeige"""
        
        # Ergebnis-Frame
        result_frame = ttk.LabelFrame(parent, text="🔍 Analyse-Ergebnisse", padding="10")
        result_frame.grid(row=2, column=1, padx=(5, 0), sticky=(tk.W, tk.E, tk.N))
        
        # Aktuelle Einstellungen
        settings_frame = ttk.LabelFrame(result_frame, text="Aktuelle Einstellungen", padding="5")
        settings_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.base_freq_label = ttk.Label(settings_frame, text="Grundfrequenz: 440.0 Hz")
        self.base_freq_label.pack()
        
        self.freq_range_label = ttk.Label(settings_frame, text="Analysebereich: 80-800 Hz")
        self.freq_range_label.pack()
        
        self.threshold_label = ttk.Label(settings_frame, text="Schwellwert: 0.03")
        self.threshold_label.pack()
        
        # Peaks
        peaks_frame = ttk.LabelFrame(result_frame, text="🎯 Detektierte Peaks", padding="5")
        peaks_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        self.peaks_text = tk.Text(peaks_frame, height=8, width=40, font=("Courier", 9))
        peaks_scroll = ttk.Scrollbar(peaks_frame, orient=tk.VERTICAL, command=self.peaks_text.yview)
        self.peaks_text.configure(yscrollcommand=peaks_scroll.set)
        self.peaks_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        peaks_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        # ξ-Verhältnisse
        xi_frame = ttk.LabelFrame(result_frame, text="⚡ ξ-Verhältnisse", padding="5")
        xi_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        self.xi_text = tk.Text(xi_frame, height=8, width=40, font=("Courier", 9))
        xi_scroll = ttk.Scrollbar(xi_frame, orient=tk.VERTICAL, command=self.xi_text.yview)
        self.xi_text.configure(yscrollcommand=xi_scroll.set)
        self.xi_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        xi_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Status
        self.status_label = ttk.Label(result_frame, text="Status: Bereit", 
                                     font=("Arial", 10, "bold"))
        self.status_label.pack(pady=5)
        
    def setup_plots(self):
        """Erstelle Matplotlib-Plots"""
        
        try:
            import matplotlib.pyplot as plt
            from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
            from matplotlib.figure import Figure
            
            # Figure mit Subplots
            self.fig = Figure(figsize=(12, 8), dpi=100)
            
            # Signal-Plot
            self.ax_signal = self.fig.add_subplot(3, 1, 1)
            self.ax_signal.set_title("Schwebungs-Signal (Zeitbereich)")
            self.ax_signal.set_xlabel("Zeit (s)")
            self.ax_signal.set_ylabel("Amplitude")
            self.ax_signal.grid(True, alpha=0.3)
            
            # Spektrum-Plot (fokussiert auf mittleren Oktavbereich)
            self.ax_spectrum = self.fig.add_subplot(3, 1, 2)
            self.ax_spectrum.set_title("ξ-FFT Spektrum (80-800 Hz Fokus)")
            self.ax_spectrum.set_xlabel("Frequenz (Hz)")
            self.ax_spectrum.set_ylabel("Magnitude")
            self.ax_spectrum.grid(True, alpha=0.3)
            self.ax_spectrum.set_xlim(80, 800)  # Mittlerer Oktavbereich
            
            # ξ-Verhältnisse Plot
            self.ax_xi = self.fig.add_subplot(3, 1, 3)
            self.ax_xi.set_title("ξ-Verhältnisse und Cent-Intervalle")
            self.ax_xi.set_xlabel("ξ-Verhältnis")
            self.ax_xi.set_ylabel("Significance")
            self.ax_xi.grid(True, alpha=0.3)
            
            self.fig.tight_layout()
            
            # Canvas in Tkinter einbetten
            self.canvas = FigureCanvasTkAgg(self.fig, self.plot_frame)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            
        except ImportError:
            # Fallback ohne Plots
            no_plot_label = ttk.Label(self.plot_frame, 
                                     text="Matplotlib nicht verfügbar - keine Plots",
                                     font=("Arial", 12))
            no_plot_label.pack(pady=20)
            self.fig = None
            
    def get_note_frequency(self, note, octave):
        """Berechne Frequenz für Note und Oktave"""
        note_freqs = {
            'C': 261.63, 'C#': 277.18, 'D': 293.66, 'D#': 311.13,
            'E': 329.63, 'F': 349.23, 'F#': 369.99, 'G': 392.00,
            'G#': 415.30, 'A': 440.00, 'A#': 466.16, 'B': 493.88
        }
        base_freq = note_freqs[note]
        return base_freq * (2 ** (octave - 4))
        
    def update_displays(self):
        """Aktualisiere alle Anzeige-Elemente"""
        
        # Parameter auslesen
        note = self.note_var.get()
        octave = self.octave_var.get()
        beat_rate = self.beat_rate_var.get()
        base_amp = self.base_amp_var.get()
        beat_amp = self.beat_amp_var.get()
        
        # Frequenz berechnen
        base_freq = self.get_note_frequency(note, octave)
        
        # Labels aktualisieren
        self.octave_label.config(text=str(octave))
        self.beat_rate_label.config(text=f"{beat_rate:.1f} Hz")
        self.base_amp_label.config(text=f"{base_amp:.1f}")
        self.beat_amp_label.config(text=f"{beat_amp:.1f}")
        
        # Einstellungen aktualisieren
        self.base_freq_label.config(text=f"Grundfrequenz: {base_freq:.1f} Hz ({note}{octave})")
        
        # Signal-Parameter setzen
        self.current_freqs = [
            base_freq,                    # Grundton
            base_freq - beat_rate/2,     # Untere Schwebung
            base_freq + beat_rate/2      # Obere Schwebung
        ]
        self.current_amps = [base_amp, beat_amp, beat_amp]
        
    def generate_signal(self):
        """Generiere Schwebungs-Signal"""
        
        if not self.current_freqs:
            self.update_displays()
        
        try:
            # Signal generieren mit create_test_signal
            self.current_signal = create_test_signal(
                freqs=self.current_freqs,
                amplitudes=self.current_amps,
                duration=2.0,
                sample_rate=1000
            )
            
            self.plot_signal()
            self.status_label.config(text="Status: Signal generiert")
            
        except Exception as e:
            self.status_label.config(text=f"Status: Fehler - {str(e)}")
            messagebox.showerror("Fehler", f"Signal-Generierung fehlgeschlagen: {str(e)}")
            
    def analyze_signal(self):
        """Analysiere aktuelles Signal mit xi_fft_library"""
        
        if not self.current_signal:
            self.status_label.config(text="Status: Kein Signal zum Analysieren")
            return
            
        try:
            self.status_label.config(text="Status: Analysiere...")
            self.root.update()
            
            # Analyse mit fokussiertem Frequenzbereich (80-800 Hz)
            self.analysis_result = self.xi_fft.analyze(
                self.current_signal, 
                freq_range=(80, 800)  # Mittlerer Oktavbereich
            )
            
            self.display_results()
            self.plot_spectrum()
            self.plot_xi_ratios()
            
            peak_count = self.analysis_result['peak_count']
            xi_count = len(self.analysis_result['xi_ratios'])
            self.status_label.config(text=f"Status: ✅ {peak_count} Peaks, {xi_count} ξ-Verhältnisse")
            
        except Exception as e:
            self.status_label.config(text=f"Status: Analyse-Fehler - {str(e)}")
            messagebox.showerror("Fehler", f"Analyse fehlgeschlagen: {str(e)}")
            
    def display_results(self):
        """Zeige Analyse-Ergebnisse in Text-Widgets"""
        
        if not self.analysis_result:
            return
            
        # Peaks anzeigen
        self.peaks_text.delete(1.0, tk.END)
        if self.analysis_result['peaks']:
            self.peaks_text.insert(tk.END, "Freq (Hz)  | Magnitude | Note\n")
            self.peaks_text.insert(tk.END, "-" * 35 + "\n")
            
            for peak in self.analysis_result['peaks'][:10]:  # Top 10 Peaks
                freq = peak['frequency']
                mag = peak['magnitude']
                note = self.frequency_to_note(freq)
                note_str = note if note else "---"
                self.peaks_text.insert(tk.END, f"{freq:8.1f}  | {mag:8.3f} | {note_str}\n")
        else:
            self.peaks_text.insert(tk.END, "Keine Peaks im Bereich 80-800 Hz gefunden\n")
            self.peaks_text.insert(tk.END, "Eventuell Schwellwert zu hoch oder Signal zu schwach")
        
        # ξ-Verhältnisse anzeigen
        self.xi_text.delete(1.0, tk.END)
        if self.analysis_result['xi_ratios']:
            self.xi_text.insert(tk.END, "ξ-Ratio | Freqs (Hz)  | Cents | Significance\n")
            self.xi_text.insert(tk.END, "-" * 50 + "\n")
            
            for ratio in self.analysis_result['xi_ratios'][:10]:  # Top 10 ξ-Verhältnisse
                xi = ratio['xi_ratio']
                f_high = ratio['freq_high']
                f_low = ratio['freq_low']
                cents = 1200 * math.log2(xi)  # Berechne Cent-Intervall
                sig = ratio['significance']
                
                self.xi_text.insert(tk.END, 
                    f"{xi:6.2f}  | {f_high:3.0f}/{f_low:3.0f}   | {cents:5.0f} | {sig:.4f}\n")
        else:
            self.xi_text.insert(tk.END, "Zu wenige Peaks für ξ-Verhältnisse\n")
            self.xi_text.insert(tk.END, "Benötige mindestens 2 detektierte Peaks")
            
    def frequency_to_note(self, frequency):
        """Konvertiere Frequenz zu musikalischer Note"""
        A4 = 440
        C0 = A4 * (2 ** (-4.75))
        
        if frequency <= 0:
            return None
            
        h = round(12 * math.log2(frequency / C0))
        octave = h // 12
        n = h % 12
        
        note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        
        if 0 <= octave <= 9:
            return note_names[n] + str(octave)
        return None
        
    def plot_signal(self):
        """Zeichne Signal-Plot"""
        
        if not self.fig or not self.current_signal:
            return
            
        self.ax_signal.clear()
        self.ax_signal.set_title("Schwebungs-Signal (Zeitbereich)")
        self.ax_signal.set_xlabel("Zeit (s)")
        self.ax_signal.set_ylabel("Amplitude")
        self.ax_signal.grid(True, alpha=0.3)
        
        # Zeitachse
        time_axis = np.linspace(0, 2, len(self.current_signal))
        
        # Signal plotten
        self.ax_signal.plot(time_axis, self.current_signal, 'b-', linewidth=1.5, label='Signal')
        
        # Schwebungs-Hüllkurve
        beat_rate = self.beat_rate_var.get()
        if beat_rate > 0:
            envelope = np.abs(np.cos(np.pi * beat_rate * time_axis))
            max_amp = max(self.current_amps)
            self.ax_signal.plot(time_axis, envelope * max_amp, 'r--', alpha=0.7, label='Beat-Hüllkurve')
            self.ax_signal.plot(time_axis, -envelope * max_amp, 'r--', alpha=0.7)
        
        self.ax_signal.legend()
        self.canvas.draw()
        
    def plot_spectrum(self):
        """Zeichne Spektrum-Plot"""
        
        if not self.fig or not self.analysis_result:
            return
            
        self.ax_spectrum.clear()
        self.ax_spectrum.set_title("ξ-FFT Spektrum (80-800 Hz Fokus)")
        self.ax_spectrum.set_xlabel("Frequenz (Hz)")
        self.ax_spectrum.set_ylabel("Magnitude")
        self.ax_spectrum.grid(True, alpha=0.3)
        self.ax_spectrum.set_xlim(80, 800)
        
        peaks = self.analysis_result['peaks']
        if peaks:
            frequencies = [p['frequency'] for p in peaks]
            magnitudes = [p['magnitude'] for p in peaks]
            
            # Spektrum-Balken
            bars = self.ax_spectrum.bar(frequencies, magnitudes, width=5, alpha=0.7)
            
            # Farb-Kodierung: Erwartete Frequenzen hervorheben
            for i, (freq, bar) in enumerate(zip(frequencies, bars)):
                # Prüfe ob Frequenz nah an erwarteten Werten liegt
                expected_match = False
                for expected_freq in self.current_freqs:
                    if abs(freq - expected_freq) < 10:  # 10 Hz Toleranz
                        expected_match = True
                        break
                
                if expected_match:
                    bar.set_color('red')
                    bar.set_alpha(0.8)
                else:
                    bar.set_color('blue')
                    bar.set_alpha(0.6)
            
            # Erwartete Frequenzen als vertikale Linien
            for expected_freq in self.current_freqs:
                if 80 <= expected_freq <= 800:
                    self.ax_spectrum.axvline(x=expected_freq, color='red', linestyle='--', 
                                           alpha=0.5, label=f'Erwartet: {expected_freq:.1f} Hz')
        
        self.canvas.draw()
        
    def plot_xi_ratios(self):
        """Zeichne ξ-Verhältnisse Plot"""
        
        if not self.fig or not self.analysis_result:
            return
            
        self.ax_xi.clear()
        self.ax_xi.set_title("ξ-Verhältnisse und Cent-Intervalle")
        self.ax_xi.set_xlabel("ξ-Verhältnis")
        self.ax_xi.set_ylabel("Significance")
        self.ax_xi.grid(True, alpha=0.3)
        
        xi_ratios = self.analysis_result['xi_ratios']
        if xi_ratios:
            xi_values = [r['xi_ratio'] for r in xi_ratios]
            significances = [r['significance'] for r in xi_ratios]
            
            # Scatter-Plot
            scatter = self.ax_xi.scatter(xi_values, significances, alpha=0.7, s=50)
            
            # Annotiere wichtige ξ-Verhältnisse
            for i, ratio in enumerate(xi_ratios[:5]):  # Top 5
                xi = ratio['xi_ratio']
                sig = ratio['significance']
                cents = 1200 * math.log2(xi)
                self.ax_xi.annotate(f'{xi:.2f}\n({cents:.0f}¢)', 
                                  (xi, sig), 
                                  xytext=(5, 5), textcoords='offset points',
                                  fontsize=8, alpha=0.8)
        
        self.canvas.draw()
        
    def on_parameter_change(self, event=None):
        """Callback für Parameter-Änderungen"""
        self.update_displays()
        if self.auto_update:
            self.generate_and_analyze()
            
    def generate_and_analyze(self):
        """Generiere Signal und analysiere es"""
        self.generate_signal()
        if self.current_signal:
            self.analyze_signal()
            
    def analyze_only(self):
        """Analysiere nur das aktuelle Signal"""
        if self.current_signal:
            self.analyze_signal()
        else:
            self.status_label.config(text="Status: Kein Signal vorhanden - erst generieren")
            
    def toggle_auto_update(self):
        """Toggle Auto-Update Modus"""
        self.auto_update = self.auto_update_var.get()
        if self.auto_update:
            self.status_label.config(text="Status: Auto-Update aktiviert")
        else:
            self.status_label.config(text="Status: Auto-Update deaktiviert")
            
    # Preset-Funktionen
    def preset_pure(self):
        """Reiner Ton ohne Schwebung"""
        self.note_var.set("A")
        self.octave_var.set(4)
        self.beat_rate_var.set(0.0)
        self.base_amp_var.set(1.0)
        self.beat_amp_var.set(0.0)
        self.update_displays()
        
    def preset_light_beat(self):
        """Leichte Schwebung"""
        self.note_var.set("A")
        self.octave_var.set(4)
        self.beat_rate_var.set(2.0)
        self.base_amp_var.set(0.8)
        self.beat_amp_var.set(0.4)
        self.update_displays()
        
    def preset_heavy_beat(self):
        """Starke Schwebung"""
        self.note_var.set("C")
        self.octave_var.set(4)
        self.beat_rate_var.set(5.0)
        self.base_amp_var.set(0.7)
        self.beat_amp_var.set(0.8)
        self.update_displays()
        
    def preset_piano(self):
        """Klavier-typische Schwebung"""
        self.note_var.set("C")
        self.octave_var.set(4)
        self.beat_rate_var.set(1.5)
        self.base_amp_var.set(0.9)
        self.beat_amp_var.set(0.3)
        self.update_displays()
        
    def run(self):
        """Starte die GUI"""
        print("🚀 Starte ξ-FFT Interactive Demo...")
        print("📊 Fokussiert auf mittleren Oktavbereich (80-800 Hz)")
        print("🎵 Verhindert Oktaven-Sprünge durch begrenzte Analyse")
        self.root.mainloop()

def main():
    """Hauptfunktion"""
    print("ξ-FFT Interactive Demo - Direkte Python-Bibliothek")
    print("=" * 50)
    
    # Prüfe Abhängigkeiten
    try:
        import matplotlib.pyplot as plt
        print("✅ Matplotlib verfügbar - Plots werden angezeigt")
    except ImportError:
        print("⚠️  Matplotlib nicht verfügbar - nur Text-Ausgabe")
        print("   Installation: pip install matplotlib")
    
    try:
        import numpy as np
        print("✅ NumPy verfügbar")
    except ImportError:
        print("❌ NumPy erforderlich: pip install numpy")
        return
    
    # Starte Demo
    try:
        demo = XiFFTDemo()
        demo.run()
    except KeyboardInterrupt:
        print("\n👋 Demo beendet")
    except Exception as e:
        print(f"❌ Fehler beim Starten der Demo: {e}")

if __name__ == "__main__":
    main()
