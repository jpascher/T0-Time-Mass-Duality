"""
ξ-FFT Windows Tuner
Frequency Tuner mit Mikrofon, Audio-Datei und Ton-Generator Support

Benötigte Pakete:
pip install pyaudio numpy matplotlib

Verwendung:
python xi_tuner_windows.py
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pyaudio
import numpy as np
import wave
import threading
import time
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import queue

# Import der ξ-FFT Library (angenommen im gleichen Verzeichnis)
try:
    from xi_fft_library import XiFFT
except ImportError:
    # Fallback: Vereinfachte ξ-FFT Implementation
    class XiFFT:
        def __init__(self, sample_rate, threshold=0.05):
            self.sample_rate = sample_rate
            self.threshold = threshold
        
        def analyze(self, signal, freq_range=(20, 2000)):
            peaks = self._find_spectral_peaks(signal, freq_range)
            return {
                'peaks': peaks,
                'peak_count': len(peaks)
            }
        
        def _find_spectral_peaks(self, signal, freq_range):
            peaks = []
            min_freq, max_freq = freq_range
            step_size = max(1, (max_freq - min_freq) // 200)
            
            for freq in range(min_freq, max_freq + 1, step_size):
                magnitude = self._calculate_magnitude(signal, freq)
                if magnitude > self.threshold:
                    peaks.append({
                        'frequency': freq,
                        'magnitude': magnitude
                    })
            
            return sorted(peaks, key=lambda x: x['magnitude'], reverse=True)
        
        def _calculate_magnitude(self, signal, frequency):
            N = len(signal)
            real = imag = 0.0
            
            for n in range(N):
                angle = -2 * math.pi * frequency * n / self.sample_rate
                real += signal[n] * math.cos(angle)
                imag += signal[n] * math.sin(angle)
            
            return math.sqrt(real * real + imag * imag) * 2 / N

class AudioManager:
    """Verwaltet Audio-Eingabe und -Ausgabe"""
    
    def __init__(self, sample_rate=44100, buffer_size=1024):
        self.sample_rate = sample_rate
        self.buffer_size = buffer_size
        self.audio = pyaudio.PyAudio()
        self.input_stream = None
        self.output_stream = None
        self.is_recording = False
        self.is_playing = False
        
        # Für Ton-Generator
        self.generator_frequency = 440.0
        self.generator_amplitude = 0.3
        self.phase = 0.0
        
        # Audio-Datei
        self.audio_data = None
        self.audio_position = 0
        
    def get_input_devices(self):
        """Liste verfügbare Audio-Eingabegeräte"""
        devices = []
        for i in range(self.audio.get_device_count()):
            device_info = self.audio.get_device_info_by_index(i)
            if device_info['maxInputChannels'] > 0:
                devices.append({
                    'index': i,
                    'name': device_info['name'],
                    'channels': device_info['maxInputChannels']
                })
        return devices
    
    def start_microphone(self, device_index=None):
        """Starte Mikrofon-Aufnahme"""
        try:
            self.input_stream = self.audio.open(
                format=pyaudio.paFloat32,
                channels=1,
                rate=self.sample_rate,
                input=True,
                input_device_index=device_index,
                frames_per_buffer=self.buffer_size
            )
            self.is_recording = True
            return True
        except Exception as e:
            print(f"Mikrofon-Fehler: {e}")
            return False
    
    def stop_microphone(self):
        """Stoppe Mikrofon-Aufnahme"""
        if self.input_stream:
            self.input_stream.stop_stream()
            self.input_stream.close()
            self.input_stream = None
        self.is_recording = False
    
    def read_microphone(self):
        """Lese Audio-Daten vom Mikrofon"""
        if self.input_stream and self.is_recording:
            try:
                data = self.input_stream.read(self.buffer_size, exception_on_overflow=False)
                return np.frombuffer(data, dtype=np.float32)
            except:
                return None
        return None
    
    def load_audio_file(self, filename):
        """Lade Audio-Datei"""
        try:
            with wave.open(filename, 'rb') as wav_file:
                frames = wav_file.readframes(-1)
                sound_info = pyaudio.paInt16
                if wav_file.getsampwidth() == 1:
                    sound_info = pyaudio.paInt8
                elif wav_file.getsampwidth() == 4:
                    sound_info = pyaudio.paInt32
                
                # Konvertiere zu Float32
                if wav_file.getsampwidth() == 2:
                    audio_data = np.frombuffer(frames, dtype=np.int16)
                    self.audio_data = audio_data.astype(np.float32) / 32768.0
                else:
                    audio_data = np.frombuffer(frames, dtype=np.int8)
                    self.audio_data = audio_data.astype(np.float32) / 128.0
                
                # Mono konvertieren wenn Stereo
                if wav_file.getnchannels() == 2:
                    self.audio_data = self.audio_data.reshape(-1, 2).mean(axis=1)
                
                self.audio_position = 0
                return True
        except Exception as e:
            print(f"Datei-Fehler: {e}")
            return False
    
    def read_audio_file(self):
        """Lese nächsten Block aus Audio-Datei"""
        if self.audio_data is not None:
            if self.audio_position + self.buffer_size < len(self.audio_data):
                data = self.audio_data[self.audio_position:self.audio_position + self.buffer_size]
                self.audio_position += self.buffer_size
                return data
            else:
                # Loop zurück zum Anfang
                self.audio_position = 0
                return self.read_audio_file()
        return None
    
    def start_tone_generator(self, frequency, amplitude=0.3):
        """Starte Ton-Generator"""
        self.generator_frequency = frequency
        self.generator_amplitude = amplitude
        self.phase = 0.0
        
        try:
            self.output_stream = self.audio.open(
                format=pyaudio.paFloat32,
                channels=1,
                rate=self.sample_rate,
                output=True,
                frames_per_buffer=self.buffer_size,
                stream_callback=self._generator_callback
            )
            self.output_stream.start_stream()
            self.is_playing = True
            return True
        except Exception as e:
            print(f"Generator-Fehler: {e}")
            return False
    
    def stop_tone_generator(self):
        """Stoppe Ton-Generator"""
        if self.output_stream:
            self.output_stream.stop_stream()
            self.output_stream.close()
            self.output_stream = None
        self.is_playing = False
    
    def _generator_callback(self, in_data, frame_count, time_info, status):
        """Callback für Ton-Generator"""
        samples = np.zeros(frame_count, dtype=np.float32)
        
        for i in range(frame_count):
            samples[i] = self.generator_amplitude * math.sin(self.phase)
            self.phase += 2 * math.pi * self.generator_frequency / self.sample_rate
            
            # Phase wrap
            if self.phase > 2 * math.pi:
                self.phase -= 2 * math.pi
        
        return (samples.tobytes(), pyaudio.paContinue)
    
    def read_generator(self):
        """Simuliere Generator-Output für Analyse"""
        samples = np.zeros(self.buffer_size, dtype=np.float32)
        
        for i in range(self.buffer_size):
            samples[i] = self.generator_amplitude * math.sin(self.phase)
            self.phase += 2 * math.pi * self.generator_frequency / self.sample_rate
            
            if self.phase > 2 * math.pi:
                self.phase -= 2 * math.pi
        
        return samples
    
    def cleanup(self):
        """Cleanup Audio-Ressourcen"""
        self.stop_microphone()
        self.stop_tone_generator()
        self.audio.terminate()

class FrequencyAnalyzer:
    """Frequenz-Analyse mit ξ-FFT"""
    
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate
        self.xi_fft = XiFFT(sample_rate, threshold=0.01)
        self.note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.A4_freq = 440.0
    
    def analyze(self, signal):
        """Analysiere Signal und gib Frequenz-Info zurück"""
        if signal is None or len(signal) == 0:
            return None
        
        # RMS berechnen
        rms = np.sqrt(np.mean(signal ** 2))
        
        # ξ-FFT Analyse
        result = self.xi_fft.analyze(signal.tolist(), freq_range=(20, 2000))
        
        if result['peaks']:
            strongest_peak = result['peaks'][0]
            frequency = strongest_peak['frequency']
            magnitude = strongest_peak['magnitude']
            
            # Note bestimmen
            note_info = self.frequency_to_note(frequency)
            
            return {
                'frequency': frequency,
                'magnitude': magnitude,
                'rms': rms,
                'note': note_info['name'],
                'cents': note_info['cents'],
                'peak_count': result['peak_count']
            }
        
        return {
            'frequency': 0,
            'magnitude': 0,
            'rms': rms,
            'note': '---',
            'cents': 0,
            'peak_count': 0
        }
    
    def frequency_to_note(self, frequency):
        """Konvertiere Frequenz zu Note mit Cent-Abweichung"""
        if frequency <= 0:
            return {'name': '---', 'cents': 0}
        
        # Halbtöne relativ zu A4
        semitones_from_a4 = 12 * math.log2(frequency / self.A4_freq)
        note_number = round(semitones_from_a4)
        octave = (note_number + 9) // 12 + 4
        note_index = (note_number % 12 + 12) % 12
        
        note_name = self.note_names[note_index] + str(octave)
        
        # Cent-Abweichung
        target_freq = self.A4_freq * (2 ** (note_number / 12))
        cents = round(1200 * math.log2(frequency / target_freq))
        
        return {
            'name': note_name,
            'cents': cents
        }

class TunerGUI:
    """Hauptfenster der Tuner-Anwendung"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ξ-FFT Frequenz-Tuner")
        self.root.geometry("800x600")
        
        # Audio und Analyse
        self.audio_manager = AudioManager()
        self.analyzer = FrequencyAnalyzer()
        
        # Audio-Modus
        self.audio_mode = tk.StringVar(value="microphone")
        self.is_running = False
        
        # Threading
        self.audio_queue = queue.Queue()
        self.analysis_thread = None
        
        self.setup_gui()
        self.start_analysis_loop()
    
    def setup_gui(self):
        """Erstelle GUI-Elemente"""
        
        # Hauptframe
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Audio-Quelle wählen
        source_frame = ttk.LabelFrame(main_frame, text="Audio-Quelle", padding="5")
        source_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Radiobutton(source_frame, text="Mikrofon", variable=self.audio_mode, 
                       value="microphone").grid(row=0, column=0, padx=5)
        ttk.Radiobutton(source_frame, text="Audio-Datei", variable=self.audio_mode, 
                       value="file").grid(row=0, column=1, padx=5)
        ttk.Radiobutton(source_frame, text="Ton-Generator", variable=self.audio_mode, 
                       value="generator").grid(row=0, column=2, padx=5)
        
        # Control Buttons
        control_frame = ttk.Frame(source_frame)
        control_frame.grid(row=1, column=0, columnspan=3, pady=5)
        
        self.start_button = ttk.Button(control_frame, text="Start", command=self.toggle_audio)
        self.start_button.grid(row=0, column=0, padx=5)
        
        self.load_file_button = ttk.Button(control_frame, text="Datei laden", 
                                          command=self.load_audio_file)
        self.load_file_button.grid(row=0, column=1, padx=5)
        
        # Ton-Generator Controls
        generator_frame = ttk.LabelFrame(main_frame, text="Ton-Generator", padding="5")
        generator_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(generator_frame, text="Frequenz (Hz):").grid(row=0, column=0, padx=5)
        self.freq_var = tk.DoubleVar(value=440.0)
        freq_scale = ttk.Scale(generator_frame, from_=80, to=2000, variable=self.freq_var, 
                              orient=tk.HORIZONTAL, length=200)
        freq_scale.grid(row=0, column=1, padx=5)
        self.freq_label = ttk.Label(generator_frame, text="440.0 Hz")
        self.freq_label.grid(row=0, column=2, padx=5)
        
        # Preset-Buttons
        preset_frame = ttk.Frame(generator_frame)
        preset_frame.grid(row=1, column=0, columnspan=3, pady=5)
        
        ttk.Button(preset_frame, text="A4 (440)", 
                  command=lambda: self.freq_var.set(440)).grid(row=0, column=0, padx=2)
        ttk.Button(preset_frame, text="C4 (262)", 
                  command=lambda: self.freq_var.set(262)).grid(row=0, column=1, padx=2)
        ttk.Button(preset_frame, text="E4 (330)", 
                  command=lambda: self.freq_var.set(330)).grid(row=0, column=2, padx=2)
        
        # Tuner Display
        tuner_frame = ttk.LabelFrame(main_frame, text="Tuner", padding="10")
        tuner_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        self.note_label = ttk.Label(tuner_frame, text="---", font=("Arial", 24, "bold"))
        self.note_label.grid(row=0, column=0, pady=5)
        
        self.freq_display = ttk.Label(tuner_frame, text="0.0 Hz", font=("Arial", 14))
        self.freq_display.grid(row=1, column=0, pady=2)
        
        self.cents_label = ttk.Label(tuner_frame, text="±0 Cent", font=("Arial", 12))
        self.cents_label.grid(row=2, column=0, pady=2)
        
        # Level Meter
        level_frame = ttk.LabelFrame(tuner_frame, text="Signal Level", padding="5")
        level_frame.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=5)
        
        self.level_var = tk.DoubleVar()
        self.level_bar = ttk.Progressbar(level_frame, variable=self.level_var, 
                                        maximum=100, length=200)
        self.level_bar.grid(row=0, column=0, padx=5)
        
        self.level_text = ttk.Label(level_frame, text="0%")
        self.level_text.grid(row=0, column=1, padx=5)
        
        # Oszilloskop
        scope_frame = ttk.LabelFrame(main_frame, text="Oszilloskop", padding="5")
        scope_frame.grid(row=2, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        self.setup_oscilloscope(scope_frame)
        
        # Status
        self.status_var = tk.StringVar(value="Bereit")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Update Frequency Label
        self.freq_var.trace('w', self.update_freq_label)
        
        # Grid configure
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
    
    def setup_oscilloscope(self, parent):
        """Erstelle Oszilloskop mit matplotlib"""
        self.fig = Figure(figsize=(4, 3), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim(0, 1024)
        self.ax.set_ylim(-1, 1)
        self.ax.set_title("Signal")
        self.ax.grid(True)
        
        self.canvas = FigureCanvasTkAgg(self.fig, parent)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Leere Linie
        self.line, = self.ax.plot([], [], 'g-', linewidth=1)
    
    def update_freq_label(self, *args):
        """Update Frequenz-Label"""
        freq = self.freq_var.get()
        self.freq_label.config(text=f"{freq:.1f} Hz")
    
    def toggle_audio(self):
        """Start/Stop Audio"""
        if not self.is_running:
            self.start_audio()
        else:
            self.stop_audio()
    
    def start_audio(self):
        """Starte Audio-Verarbeitung"""
        mode = self.audio_mode.get()
        
        if mode == "microphone":
            if self.audio_manager.start_microphone():
                self.is_running = True
                self.status_var.set("Mikrofon aktiv")
            else:
                messagebox.showerror("Fehler", "Mikrofon konnte nicht gestartet werden")
                return
        
        elif mode == "file":
            if self.audio_manager.audio_data is not None:
                self.is_running = True
                self.status_var.set("Audio-Datei wird abgespielt")
            else:
                messagebox.showwarning("Warnung", "Bitte laden Sie zuerst eine Audio-Datei")
                return
        
        elif mode == "generator":
            freq = self.freq_var.get()
            if self.audio_manager.start_tone_generator(freq):
                self.is_running = True
                self.status_var.set(f"Ton-Generator aktiv ({freq:.1f} Hz)")
            else:
                messagebox.showerror("Fehler", "Ton-Generator konnte nicht gestartet werden")
                return
        
        self.start_button.config(text="Stop")
        
        # Starte Analysis Thread
        if self.analysis_thread is None or not self.analysis_thread.is_alive():
            self.analysis_thread = threading.Thread(target=self.audio_loop, daemon=True)
            self.analysis_thread.start()
    
    def stop_audio(self):
        """Stoppe Audio-Verarbeitung"""
        self.is_running = False
        self.audio_manager.stop_microphone()
        self.audio_manager.stop_tone_generator()
        self.start_button.config(text="Start")
        self.status_var.set("Gestoppt")
    
    def load_audio_file(self):
        """Lade Audio-Datei"""
        filename = filedialog.askopenfilename(
            title="Audio-Datei wählen",
            filetypes=[("WAV-Dateien", "*.wav"), ("Alle Dateien", "*.*")]
        )
        
        if filename:
            if self.audio_manager.load_audio_file(filename):
                self.status_var.set(f"Datei geladen: {filename.split('/')[-1]}")
                self.audio_mode.set("file")
            else:
                messagebox.showerror("Fehler", "Audio-Datei konnte nicht geladen werden")
    
    def audio_loop(self):
        """Audio-Verarbeitungs-Loop (läuft in separatem Thread)"""
        while self.is_running:
            try:
                mode = self.audio_mode.get()
                audio_data = None
                
                if mode == "microphone":
                    audio_data = self.audio_manager.read_microphone()
                elif mode == "file":
                    audio_data = self.audio_manager.read_audio_file()
                elif mode == "generator":
                    # Update Generator-Frequenz wenn geändert
                    current_freq = self.freq_var.get()
                    if abs(current_freq - self.audio_manager.generator_frequency) > 0.1:
                        self.audio_manager.generator_frequency = current_freq
                        self.root.after(0, lambda: self.status_var.set(f"Generator: {current_freq:.1f} Hz"))
                    
                    audio_data = self.audio_manager.read_generator()
                
                if audio_data is not None:
                    # In Queue für GUI-Update
                    self.audio_queue.put(audio_data)
                
                time.sleep(0.01)  # 100 Hz Update-Rate
                
            except Exception as e:
                print(f"Audio-Loop Fehler: {e}")
                break
    
    def start_analysis_loop(self):
        """Starte GUI-Update-Loop"""
        self.update_display()
    
    def update_display(self):
        """Update GUI mit neuen Audio-Daten"""
        try:
            # Verarbeite alle verfügbaren Audio-Daten
            latest_data = None
            while not self.audio_queue.empty():
                latest_data = self.audio_queue.get_nowait()
            
            if latest_data is not None and self.is_running:
                # Analysiere Signal
                result = self.analyzer.analyze(latest_data)
                
                if result:
                    # Update Tuner Display
                    self.note_label.config(text=result['note'])
                    self.freq_display.config(text=f"{result['frequency']:.1f} Hz")
                    
                    # Cent-Anzeige mit Farbe
                    cents = result['cents']
                    cents_text = f"{cents:+d} Cent" if cents != 0 else "0 Cent"
                    
                    if abs(cents) <= 5:
                        color = "green"
                    elif abs(cents) <= 20:
                        color = "orange"
                    else:
                        color = "red"
                    
                    self.cents_label.config(text=cents_text, foreground=color)
                    
                    # Level Meter
                    level_percent = min(result['rms'] * 1000, 100)
                    self.level_var.set(level_percent)
                    self.level_text.config(text=f"{level_percent:.0f}%")
                    
                    # Update Oszilloskop
                    self.update_oscilloscope(latest_data)
        
        except queue.Empty:
            pass
        except Exception as e:
            print(f"Display-Update Fehler: {e}")
        
        # Schedule nächstes Update
        self.root.after(50, self.update_display)  # 20 Hz GUI-Update
    
    def update_oscilloscope(self, data):
        """Update Oszilloskop-Anzeige"""
        if len(data) > 0:
            # Zeige nur ersten Teil für bessere Sichtbarkeit
            display_samples = min(len(data), 512)
            x = np.arange(display_samples)
            y = data[:display_samples]
            
            self.line.set_data(x, y)
            self.ax.set_xlim(0, display_samples)
            self.ax.set_ylim(np.min(y) * 1.1, np.max(y) * 1.1)
            
            try:
                self.canvas.draw_idle()
            except:
                pass  # Ignore drawing errors during shutdown
    
    def on_closing(self):
        """Cleanup beim Schließen"""
        self.is_running = False
        self.audio_manager.cleanup()
        self.root.destroy()
    
    def run(self):
        """Starte GUI"""
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

# Hauptprogramm
if __name__ == "__main__":
    try:
        app = TunerGUI()
        app.run()
    except Exception as e:
        print(f"Anwendungsfehler: {e}")
        input("Drücken Sie Enter zum Beenden...")
