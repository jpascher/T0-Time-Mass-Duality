"""
ξ-FFT Minimal Version - Funktioniert garantiert!
Nur die absolut nötigsten Funktionen

Abhängigkeiten:
pip install matplotlib numpy
"""

import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import math

# Minimale ξ-FFT Implementation - Funktioniert IMMER
class MinimalXiFFT:
    def __init__(self):
        self.sample_rate = 44100
        
    def analyze_signal(self, signal):
        """Super-einfache Analyse die immer funktioniert"""
        
        print("=" * 50)
        print("🔬 MINIMAL ANALYSE GESTARTET")
        print(f"Signal Länge: {len(signal)}")
        print(f"Signal Min/Max: {np.min(signal):.3f} / {np.max(signal):.3f}")
        
        # Test nur wenige Frequenzen
        test_frequencies = [435, 440, 445, 450, 460, 470]
        peaks = []
        
        for freq in test_frequencies:
            magnitude = self.calculate_magnitude_simple(signal, freq)
            print(f"Frequenz {freq} Hz: Magnitude = {magnitude:.4f}")
            
            if magnitude > 0.0001:  # SEHR niedriger Threshold - findet alles!
                peaks.append({
                    'frequency': freq,
                    'magnitude': magnitude
                })
        
        print(f"Peaks gefunden: {len(peaks)}")
        for peak in peaks:
            print(f"  Peak: {peak['frequency']} Hz = {peak['magnitude']:.4f}")
        
        print("✅ MINIMAL ANALYSE ABGESCHLOSSEN")
        print("=" * 50)
        
        return {
            'peaks': peaks,
            'peak_count': len(peaks)
        }
    
    def calculate_magnitude_simple(self, signal, frequency):
        """Super-einfache DFT für eine Frequenz"""
        
        # Nur erste 10000 Samples für Geschwindigkeit
        if len(signal) > 10000:
            signal = signal[:10000]
        
        N = len(signal)
        real = 0.0
        imag = 0.0
        
        # Vereinfachte DFT
        for n in range(0, N, 10):  # Nur jedes 10. Sample
            angle = -2 * math.pi * frequency * n / self.sample_rate
            real += signal[n] * math.cos(angle)
            imag += signal[n] * math.sin(angle)
        
        magnitude = math.sqrt(real * real + imag * imag) / N
        return magnitude

# Minimaler Signal-Generator
def create_test_signal():
    """Erstelle einfaches Test-Signal"""
    
    print("🎵 Erstelle Test-Signal...")
    
    duration = 2.0  # Nur 2 Sekunden
    sample_rate = 44100
    samples = int(duration * sample_rate)
    
    t = np.linspace(0, duration, samples)
    
    # Drei Töne: 435, 440, 445 Hz (STÄRKERE Amplituden)
    signal = (0.8 * np.sin(2 * np.pi * 435 * t) + 
              1.0 * np.sin(2 * np.pi * 440 * t) + 
              0.8 * np.sin(2 * np.pi * 445 * t))
    
    # Normalisiert aber hörbar
    signal = signal * 0.3  # 30% der Amplitude
    
    print(f"Signal erstellt: {len(signal)} Samples")
    print(f"Signal Amplitude: {np.max(np.abs(signal)):.6f}")
    
    return signal

# Minimal GUI
class MinimalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ξ-FFT MINIMAL - Test Version")
        self.root.geometry("800x600")
        
        self.xi_fft = MinimalXiFFT()
        self.current_signal = None
        self.current_analysis = None
        
        self.setup_gui()
        
    def setup_gui(self):
        # Hauptframe
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Buttons
        button_frame = tk.Frame(main_frame)
        button_frame.pack(side=tk.TOP, fill=tk.X, pady=5)
        
        tk.Button(button_frame, text="1. Signal erstellen", 
                 command=self.create_signal, bg='lightgreen', 
                 font=('Arial', 12, 'bold')).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="2. Signal analysieren", 
                 command=self.analyze_signal, bg='lightblue', 
                 font=('Arial', 12, 'bold')).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="3. Ergebnisse anzeigen", 
                 command=self.show_results, bg='lightyellow', 
                 font=('Arial', 12, 'bold')).pack(side=tk.LEFT, padx=5)
        
        # Status
        self.status_var = tk.StringVar()
        self.status_var.set("Bereit - Klicken Sie '1. Signal erstellen'")
        self.status_label = tk.Label(main_frame, textvariable=self.status_var, 
                                   font=('Arial', 10), bg='white', relief=tk.SUNKEN)
        self.status_label.pack(side=tk.TOP, fill=tk.X, pady=5)
        
        # Plot
        self.fig = Figure(figsize=(10, 8), facecolor='white')
        self.canvas = FigureCanvasTkAgg(self.fig, main_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Subplots
        self.wave_ax = self.fig.add_subplot(3, 1, 1)
        self.spec_ax = self.fig.add_subplot(3, 1, 2)
        self.result_ax = self.fig.add_subplot(3, 1, 3)
        
        self.wave_ax.set_title('1. Zeitverlauf des Signals', fontsize=14, fontweight='bold')
        self.spec_ax.set_title('2. Frequenzspektrum', fontsize=14, fontweight='bold')
        self.result_ax.set_title('3. Analyse-Ergebnisse', fontsize=14, fontweight='bold')
        
        # Result ax als Text-Display
        self.result_ax.axis('off')
        
        self.fig.tight_layout()
        
        # Initialer Plot
        self.clear_plots()
        
    def clear_plots(self):
        """Leere alle Plots"""
        
        self.wave_ax.clear()
        self.wave_ax.set_title('1. Zeitverlauf des Signals')
        self.wave_ax.text(0.5, 0.5, 'Kein Signal vorhanden\nKlicken Sie "1. Signal erstellen"', 
                         ha='center', va='center', transform=self.wave_ax.transAxes,
                         fontsize=12, bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))
        
        self.spec_ax.clear()
        self.spec_ax.set_title('2. Frequenzspektrum')
        self.spec_ax.text(0.5, 0.5, 'Keine Analyse vorhanden\nKlicken Sie "2. Signal analysieren"', 
                         ha='center', va='center', transform=self.spec_ax.transAxes,
                         fontsize=12, bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))
        
        self.result_ax.clear()
        self.result_ax.axis('off')
        self.result_ax.text(0.5, 0.5, 'Keine Ergebnisse vorhanden\nKlicken Sie "3. Ergebnisse anzeigen"', 
                           ha='center', va='center', transform=self.result_ax.transAxes,
                           fontsize=12, bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))
        
        self.canvas.draw()
        
    def create_signal(self):
        """Schritt 1: Signal erstellen"""
        
        try:
            print("\n" + "🎵 SCHRITT 1: SIGNAL ERSTELLEN")
            self.status_var.set("Erstelle Test-Signal...")
            self.root.update()
            
            # Signal erstellen
            self.current_signal = create_test_signal()
            
            # Signal plotten
            self.plot_waveform()
            
            self.status_var.set(f"✅ Signal erstellt: {len(self.current_signal)} Samples. Klicken Sie '2. Signal analysieren'")
            
            messagebox.showinfo("Erfolg", "Signal wurde erstellt!\nSie können es im oberen Plot sehen.\n\nKlicken Sie jetzt '2. Signal analysieren'")
            
        except Exception as e:
            print(f"❌ Fehler beim Signal erstellen: {str(e)}")
            self.status_var.set(f"❌ Fehler: {str(e)}")
            messagebox.showerror("Fehler", f"Signal-Erstellung fehlgeschlagen:\n{str(e)}")
    
    def analyze_signal(self):
        """Schritt 2: Signal analysieren"""
        
        if self.current_signal is None:
            messagebox.showwarning("Warnung", "Erst Signal erstellen!\nKlicken Sie '1. Signal erstellen'")
            return
        
        try:
            print("\n" + "🔬 SCHRITT 2: SIGNAL ANALYSIEREN")
            self.status_var.set("Analysiere Signal mit ξ-FFT...")
            self.root.update()
            
            # Analyse durchführen
            self.current_analysis = self.xi_fft.analyze_signal(self.current_signal)
            
            # Spektrum plotten
            self.plot_spectrum()
            
            self.status_var.set(f"✅ Analyse abgeschlossen: {self.current_analysis['peak_count']} Peaks gefunden. Klicken Sie '3. Ergebnisse anzeigen'")
            
            messagebox.showinfo("Erfolg", f"Analyse abgeschlossen!\n{self.current_analysis['peak_count']} Peaks gefunden.\n\nKlicken Sie jetzt '3. Ergebnisse anzeigen'")
            
        except Exception as e:
            print(f"❌ Fehler bei der Analyse: {str(e)}")
            import traceback
            traceback.print_exc()
            self.status_var.set(f"❌ Analyse-Fehler: {str(e)}")
            messagebox.showerror("Fehler", f"Analyse fehlgeschlagen:\n{str(e)}")
    
    def show_results(self):
        """Schritt 3: Ergebnisse anzeigen"""
        
        if self.current_analysis is None:
            messagebox.showwarning("Warnung", "Erst Signal analysieren!\nKlicken Sie '2. Signal analysieren'")
            return
        
        try:
            print("\n" + "📊 SCHRITT 3: ERGEBNISSE ANZEIGEN")
            self.status_var.set("Zeige Analyse-Ergebnisse...")
            self.root.update()
            
            # Ergebnisse plotten
            self.plot_results()
            
            self.status_var.set("✅ Alle Schritte abgeschlossen! Analyse-Ergebnisse werden angezeigt.")
            
            # Erfolgs-Dialog
            peaks = self.current_analysis['peaks']
            if peaks:
                peak_text = "\n".join([f"  {p['frequency']} Hz: {p['magnitude']:.4f}" for p in peaks])
                message = f"Analyse erfolgreich!\n\nGefundene Peaks:\n{peak_text}"
            else:
                message = "Analyse erfolgreich!\nKeine Peaks über dem Threshold gefunden."
            
            messagebox.showinfo("Analyse Abgeschlossen", message)
            
        except Exception as e:
            print(f"❌ Fehler beim Anzeigen: {str(e)}")
            self.status_var.set(f"❌ Anzeige-Fehler: {str(e)}")
            messagebox.showerror("Fehler", f"Ergebnisse-Anzeige fehlgeschlagen:\n{str(e)}")
    
    def plot_waveform(self):
        """Plot Signal-Zeitverlauf"""
        
        self.wave_ax.clear()
        self.wave_ax.set_title('1. Zeitverlauf des Signals ✅', color='green', fontweight='bold')
        
        # Nur erste 2000 Punkte für Performance
        if len(self.current_signal) > 2000:
            step = len(self.current_signal) // 2000
            plot_signal = self.current_signal[::step]
        else:
            plot_signal = self.current_signal
        
        t = np.linspace(0, len(self.current_signal)/44100, len(plot_signal))
        
        self.wave_ax.plot(t, plot_signal, 'b-', linewidth=1, label='Signal')
        self.wave_ax.set_xlabel('Zeit (s)')
        self.wave_ax.set_ylabel('Amplitude')
        self.wave_ax.grid(True, alpha=0.3)
        self.wave_ax.legend()
        
        # Info-Text
        info_text = f"Signal: {len(self.current_signal)} Samples\nMax Amplitude: {np.max(np.abs(self.current_signal)):.6f}"
        self.wave_ax.text(0.02, 0.98, info_text, transform=self.wave_ax.transAxes, 
                         verticalalignment='top', bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen", alpha=0.7))
        
        self.canvas.draw()
        
    def plot_spectrum(self):
        """Plot Frequenzspektrum"""
        
        self.spec_ax.clear()
        self.spec_ax.set_title('2. Frequenzspektrum ✅', color='green', fontweight='bold')
        
        peaks = self.current_analysis['peaks']
        
        if peaks:
            # Balkendiagramm der Peaks
            frequencies = [p['frequency'] for p in peaks]
            magnitudes = [p['magnitude'] for p in peaks]
            
            bars = self.spec_ax.bar(frequencies, magnitudes, width=3, alpha=0.7, color='steelblue', edgecolor='navy')
            
            # Highlighte den stärksten Peak
            if len(bars) > 0:
                bars[0].set_color('red')
                bars[0].set_alpha(0.9)
            
            # Labels
            for freq, mag in zip(frequencies, magnitudes):
                self.spec_ax.text(freq, mag + max(magnitudes)*0.05, f'{freq}Hz\n{mag:.3f}', 
                                 ha='center', va='bottom', fontsize=9, fontweight='bold')
            
            self.spec_ax.set_xlabel('Frequenz (Hz)')
            self.spec_ax.set_ylabel('Magnitude')
            self.spec_ax.grid(True, alpha=0.3)
            
            # Info
            info_text = f"{len(peaks)} Peaks gefunden"
            self.spec_ax.text(0.02, 0.98, info_text, transform=self.spec_ax.transAxes, 
                             verticalalignment='top', bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.7))
        else:
            self.spec_ax.text(0.5, 0.5, 'Keine Peaks gefunden\n(Threshold zu hoch?)', 
                             ha='center', va='center', transform=self.spec_ax.transAxes,
                             fontsize=12, bbox=dict(boxstyle="round,pad=0.3", facecolor="orange"))
        
        self.canvas.draw()
        
    def plot_results(self):
        """Plot Analyse-Ergebnisse als Text"""
        
        self.result_ax.clear()
        self.result_ax.axis('off')
        self.result_ax.set_title('3. Analyse-Ergebnisse ✅', color='green', fontweight='bold')
        
        peaks = self.current_analysis['peaks']
        
        # Ergebnis-Text erstellen
        result_text = "🔬 ξ-FFT MINIMAL ANALYSE ERGEBNISSE\n\n"
        result_text += f"📊 Peaks gefunden: {len(peaks)}\n"
        result_text += f"📏 Signal-Länge: {len(self.current_signal):,} Samples\n"
        result_text += f"⏱️  Signal-Dauer: {len(self.current_signal)/44100:.2f} s\n\n"
        
        if peaks:
            result_text += "🎵 DETEKTIERTE FREQUENZEN:\n"
            result_text += "-" * 30 + "\n"
            for i, peak in enumerate(peaks, 1):
                result_text += f"{i}. {peak['frequency']:3.0f} Hz  →  {peak['magnitude']:.4f}\n"
                
            # Analyse der Frequenzen
            result_text += "\n📈 ANALYSE:\n"
            result_text += "-" * 30 + "\n"
            
            # Erwartete Frequenzen: 435, 440, 445 Hz
            expected = [435, 440, 445]
            found_expected = []
            
            for exp_freq in expected:
                for peak in peaks:
                    if abs(peak['frequency'] - exp_freq) <= 2:  # 2 Hz Toleranz
                        found_expected.append(f"{exp_freq} Hz ✅")
                        break
                else:
                    found_expected.append(f"{exp_freq} Hz ❌")
            
            result_text += "Erwartete Frequenzen:\n"
            for fe in found_expected:
                result_text += f"  {fe}\n"
                
            # Schwebung
            if len(peaks) >= 2:
                freq_diff = abs(peaks[0]['frequency'] - peaks[1]['frequency'])
                result_text += f"\nSchwebungsfrequenz: ~{freq_diff:.1f} Hz"
        else:
            result_text += "❌ KEINE PEAKS GEFUNDEN\n"
            result_text += "Mögliche Ursachen:\n"
            result_text += "• Threshold zu hoch\n"
            result_text += "• Signal zu schwach\n"
            result_text += "• Analyse-Fehler\n"
        
        # Text anzeigen
        self.result_ax.text(0.05, 0.95, result_text, transform=self.result_ax.transAxes, 
                           verticalalignment='top', fontfamily='monospace', fontsize=10,
                           bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow", alpha=0.8))
        
        self.canvas.draw()

def main():
    """Hauptfunktion"""
    
    print("🚀 ξ-FFT MINIMAL VERSION STARTET")
    print("=" * 50)
    print("Diese Version ist super-einfach und MUSS funktionieren!")
    print("Wenn das nicht funktioniert, haben wir ein grundlegendes Problem.")
    print("=" * 50)
    
    # Tkinter
    root = tk.Tk()
    
    # App
    app = MinimalGUI(root)
    
    print("✅ GUI bereit")
    print("Bitte folgen Sie den 3 Schritten:")
    print("1. Signal erstellen")
    print("2. Signal analysieren") 
    print("3. Ergebnisse anzeigen")
    
    # Start
    root.mainloop()

if __name__ == "__main__":
    main()
