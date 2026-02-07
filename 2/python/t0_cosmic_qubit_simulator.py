#!/usr/bin/env python3
"""
T0-COSMIC-QUBIT-SIMULATOR - ERWEITERTE VERSION (KORRIGIERT)
Simuliert Qubits im faltigen Torus-Universum mit erweiterten kosmischen Korrekturen
Speicherort: 2/python/t0_cosmic_qubit_simulator.py
"""

import numpy as np
from datetime import datetime, timedelta
import ephem # Für astronomische Berechnungen
import random
import json
import os

# Try to import matplotlib, but make it optional
try:
  import matplotlib.pyplot as plt
  from mpl_toolkits.mplot3d import Axes3D
  MATPLOTLIB_AVAILABLE = True
except ImportError:
  MATPLOTLIB_AVAILABLE = False
  print("Hinweis: matplotlib nicht installiert. Visualisierung deaktiviert.")
  print("Installieren mit: pip install matplotlib")

class EnhancedCosmicQubit:
  """Ein Qubit im faltigen Torus-Universum mit erweiterten kosmischen Effekten"""
  
  def __init__(self, qubit_id, position=(0,0,0), creation_time=None, qubit_type='transmon'):
    self.qubit_id = qubit_id
    self.position = np.array(position, dtype=float)
    self.creation_time = creation_time or datetime.now()
    self.qubit_type = qubit_type
    self.xi = 4/30000 # Fraktaler Korrekturparameter
    self.D_f = 3 - self.xi # Fraktale Dimension
    
    # Kosmische Parameter
    self.observer = ephem.Observer()
    self.observer.lat = '47.3769' # Zürich
    self.observer.lon = '8.5417'
    self.observer.elevation = 408 # Meter über Meer
    
    # Quantenfluktuations-Historie
    self.quantum_fluctuations = []
    self.t2_history = []
    
    # Zusätzliche astronomische Körper
    self.sun = ephem.Sun()
    self.jupiter = ephem.Jupiter()
    self.venus = ephem.Venus()
    
    # Kosmische Strahlung (vereinfachtes Modell)
    self.cosmic_ray_base = 1.0
    self.solar_cycle_phase = 0.0
    
    # Quantengravitationsparameter (vereinfacht)
    self.planck_time = 5.391e-44 # Sekunden
    self.hbar = 1.0545718e-34 # Reduzierte Planck-Konstante
    
  def get_cosmic_alignment(self, current_time=None):
    """Berechnet Ausrichtung zu kosmischen Strukturen"""
    if current_time is None:
      current_time = datetime.now()
    
    self.observer.date = current_time
    
    # Galaktische Ausrichtung
    try:
      galactic_center = ephem.GalacticCenter()
      galactic_center.compute(self.observer)
      galactic_lat = galactic_center.glat
      galactic_lon = galactic_center.glon
    except:
      galactic_lat = 0.0
      galactic_lon = 0.0
    
    # Planetenausrichtungen
    self.sun.compute(self.observer)
    self.jupiter.compute(self.observer)
    self.venus.compute(self.observer)
    
    # CMB-Dipol-Korrektur (vereinfacht)
    # Bewegung relativ zu CMB: ~370 km/s in Richtung (l,b) = (264°, 48°)
    cmb_dipol_amplitude = 3.346e-3 # mK
    sidereal_hour = (current_time.hour + current_time.minute/60 + 
            current_time.second/3600) * 1.0027379
    cmb_factor = 0.001 * np.sin(2*np.pi * sidereal_hour / 24)
    
    return {
      'galactic_lat': float(galactic_lat),
      'galactic_lon': float(galactic_lon),
      'sun_alt': float(self.sun.alt),
      'sun_az': float(self.sun.az),
      'jupiter_alt': float(self.jupiter.alt),
      'venus_alt': float(self.venus.alt),
      'cmb_correction': cmb_factor,
      'sidereal_hour': sidereal_hour
    }
  
  def get_cosmic_phase_correction(self, current_time=None):
    """Berechnet kosmische Phasenkorrektur für aktuellen Zeitpunkt"""
    if current_time is None:
      current_time = datetime.now()
    
    # 1. Tageszeit-Effekt (präziser)
    hour = current_time.hour + current_time.minute/60 + current_time.second/3600
    day_factor = 0.5 * (1 - np.cos(2*np.pi*hour/24))
    
    # 2. Mondphasen-Effekt
    self.observer.date = current_time
    moon = ephem.Moon(self.observer)
    moon_phase = moon.phase / 100 # 0-1
    moon_factor = 0.1 * np.sin(2*np.pi*moon_phase)
    
    # 3. Jahreszeit-Effekt (präziser)
    day_of_year = current_time.timetuple().tm_yday
    year_factor = 0.05 * np.sin(2*np.pi*day_of_year/365.25)
    
    # 4. Kosmische Ausrichtung
    alignment = self.get_cosmic_alignment(current_time)
    
    # 5. Gezeiten-Effekt (Mond und Sonne)
    moon_alt = ephem.Moon(self.observer).alt
    sun_alt = self.sun.alt
    tidal_factor = 0.02 * (np.sin(float(moon_alt)) + 0.3 * np.sin(float(sun_alt)))
    
    # 6. Kosmische Strahlung (vereinfacht)
    cosmic_ray_factor = self.cosmic_ray_base + 0.1 * np.sin(2*np.pi * day_of_year/27.3) # Sonnenrotation
    
    # 7. Quantengravitations-Fluktuationen
    seconds_since_midnight = (current_time - current_time.replace(
      hour=0, minute=0, second=0, microsecond=0)).total_seconds()
    quantum_gravity_factor = 1e-15 * np.sin(2*np.pi * seconds_since_midnight / self.planck_time)
    
    # Gesamtkorrektur (gewichtet)
    total_correction = self.xi * (
      day_factor + 
      moon_factor + 
      year_factor + 
      0.5 * tidal_factor + 
      0.3 * alignment['cmb_correction'] +
      0.2 * cosmic_ray_factor +
      quantum_gravity_factor
    )
    
    # Speichere Quantenfluktuation
    self.quantum_fluctuations.append({
      'timestamp': current_time,
      'correction': total_correction,
      'alignment': alignment
    })
    
    return np.exp(1j * total_correction)
  
  def apply_quantum_gravity_correction(self, qubit_state, current_time=None):
    """Fügt Quantengravitationseffekte hinzu (vereinfacht)"""
    if current_time is None:
      current_time = datetime.now()
      
    # Zyklische Quantenfluktuationen auf Planck-Skala
    seconds_since_epoch = current_time.timestamp()
    gravity_phase = 1e-12 * np.sin(2*np.pi * seconds_since_epoch / self.planck_time)
    
    return qubit_state * np.exp(1j * gravity_phase)
  
  def get_position_factor(self, chip_geometry='ibm_sherbrooke'):
    """Berechnet Positionsfaktor basierend auf Chip-Layout"""
    x, y, z = self.position
    
    # IBM Sherbrooke 127-Qubit Layout (fraktale Anordnung)
    if chip_geometry == 'ibm_sherbrooke':
      # Fraktales Muster (Mandelbrot-ähnlich)
      r = np.sqrt(x**2 + y**2)
      theta = np.arctan2(y, x)
      
      # "Gehirnwindungen" auf dem Chip (gyrus/sulcus)
      gyrus_pattern = 0.5 * (1 + np.sin(3*theta) * np.cos(2*r))
      
      # Fraktale Dimension-Effekt
      fractal_effect = 0.1 * np.sin(self.D_f * r) * np.cos(self.D_f * theta)
      
      # Positionsfaktor: 1.0 = optimal (Gyrus), 0.85 = schlecht (Sulcus)
      position_factor = 0.9 + 0.1 * gyrus_pattern + 0.05 * fractal_effect
      
    elif chip_geometry == 'honeycomb':
      # Wabenstruktur (z.B. Google Sycamore)
      hex_x = x
      hex_y = y + 0.5 * (x % 2)
      position_factor = 0.95 + 0.05 * np.sin(2*np.pi * hex_x/3) * np.cos(2*np.pi * hex_y/3)
      
    elif chip_geometry == 'square_lattice':
      # Quadratisches Gitter (einfach)
      position_factor = 0.93 + 0.07 * np.sin(x) * np.cos(y)
      
    else:
      position_factor = 1.0
    
    return np.clip(position_factor, 0.8, 1.0)
  
  def effective_coherence_time(self, base_T2=100e-6):
    """Berechnet effektive Kohärenzzeit mit erweiterten kosmischen Korrekturen"""
    position_factor = self.get_position_factor('ibm_sherbrooke')
    cosmic_factor = np.abs(self.get_cosmic_phase_correction())
    
    # Quantengravitations-Korrektur
    quantum_gravity_factor = 1.0 + 1e-6 * np.random.randn() # Kleine stochastische Fluktuationen
    
    # Temperaturabhängigkeit (vereinfacht) - Optimal um Mittag
    current_hour = datetime.now().hour
    temperature_factor = 1.0 - 0.0005 * (current_hour - 12)**2 # KORREKTUR: Kommentarzeichen hinzugefügt
    
    result = base_T2 * position_factor * cosmic_factor * quantum_gravity_factor * temperature_factor
    
    # Speichere in History
    self.t2_history.append({
      'timestamp': datetime.now(),
      't2': result,
      'position_factor': position_factor,
      'cosmic_factor': cosmic_factor,
      'quantum_gravity_factor': quantum_gravity_factor,
      'temperature_factor': temperature_factor
    })
    
    return result
  
  def simulate_decoherence_path(self, steps=1000, dt=1e-6):
    """Simuliert Dekohärenz-Pfad mit kosmischen Störungen"""
    times = np.arange(0, steps*dt, dt)
    coherence = np.zeros(steps)
    
    for i in range(steps):
      current_time = datetime.now() + timedelta(seconds=i*dt)
      cosmic_factor = np.abs(self.get_cosmic_phase_correction(current_time))
      coherence[i] = np.exp(-times[i] / self.effective_coherence_time()) * cosmic_factor
    
    return times, coherence
  
  def get_quantum_state_vector(self, alpha=1/np.sqrt(2), beta=1/np.sqrt(2)):
    """Erzeugt quantenmechanischen Zustandsvektor mit kosmischen Korrekturen"""
    # Basis-Zustand
    state = np.array([alpha, beta], dtype=complex)
    
    # Wende kosmische Korrekturen an
    cosmic_correction = self.get_cosmic_phase_correction()
    state *= cosmic_correction
    
    # Quantengravitations-Korrektur
    state = self.apply_quantum_gravity_correction(state)
    
    # Normiere
    norm = np.sqrt(np.abs(state[0])**2 + np.abs(state[1])**2)
    return state / norm
  
  def to_dict(self):
    """Serialisiert Qubit-Daten für JSON-Export"""
    return {
      'qubit_id': self.qubit_id,
      'position': self.position.tolist(),
      'creation_time': self.creation_time.isoformat(),
      'qubit_type': self.qubit_type,
      'xi': self.xi,
      'D_f': self.D_f,
      't2_current': float(self.effective_coherence_time()),
      'quantum_fluctuations_count': len(self.quantum_fluctuations),
      't2_history_count': len(self.t2_history)
    }
  
  def save_to_file(self, filename=None):
    """Speichert Qubit-Daten in JSON-Datei"""
    if filename is None:
      filename = f"qubit_{self.qubit_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    data = self.to_dict()
    with open(filename, 'w') as f:
      json.dump(data, f, indent=2)
    
    return filename

class CosmicQubitVisualizer:
  """Visualisiert kosmische Qubit-Simulationen"""
  
  @staticmethod
  def plot_qubit_positions(qubits, chip_geometry='ibm_sherbrooke'):
    """Visualisiert Qubit-Positionen auf dem Chip"""
    if not MATPLOTLIB_AVAILABLE:
      print("Visualisierung deaktiviert: matplotlib nicht installiert")
      return None
      
    fig = plt.figure(figsize=(12, 10))
    
    # 3D-Plot
    ax1 = fig.add_subplot(221, projection='3d')
    positions = np.array([q.position for q in qubits])
    t2_values = [q.effective_coherence_time()*1e6 for q in qubits]
    
    scatter = ax1.scatter(positions[:,0], positions[:,1], positions[:,2], 
              c=t2_values, cmap='viridis', s=100)
    ax1.set_xlabel('X Position')
    ax1.set_ylabel('Y Position')
    ax1.set_zlabel('Z Position')
    ax1.set_title('Qubit-Positionen und T2-Zeiten (3D)')
    plt.colorbar(scatter, ax=ax1, label='T2 (μs)')
    
    # 2D-Heatmap
    ax2 = fig.add_subplot(222)
    if len(positions) > 0:
      # Einfache Scatter-Plot statt Interpolation (keine scipy Abhängigkeit)
      scatter2 = ax2.scatter(positions[:,0], positions[:,1], c=t2_values, 
                 cmap='plasma', s=100, edgecolors='black')
      plt.colorbar(scatter2, ax=ax2, label='T2 (μs)')
    
    ax2.set_xlabel('X Position')
    ax2.set_ylabel('Y Position')
    ax2.set_title('T2 auf Chip')
    
    # T2-Verteilung
    ax3 = fig.add_subplot(223)
    ax3.hist(t2_values, bins=20, alpha=0.7, color='skyblue', edgecolor='black')
    ax3.axvline(np.mean(t2_values), color='red', linestyle='--', label=f'Mittelwert: {np.mean(t2_values):.1f} μs')
    ax3.set_xlabel('T2 (μs)')
    ax3.set_ylabel('Anzahl Qubits')
    ax3.set_title('Verteilung der T2-Zeiten')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Kosmische Korrekturen über Zeit
    ax4 = fig.add_subplot(224)
    if len(qubits) > 0 and len(qubits[0].quantum_fluctuations) > 0:
      q = qubits[0]
      times = [f['timestamp'] for f in q.quantum_fluctuations[-24:]] # Letzte 24 Einträge
      corrections = [np.abs(f['correction']) for f in q.quantum_fluctuations[-24:]]
      
      ax4.plot(range(len(times)), corrections, 'o-', linewidth=2)
      ax4.set_xlabel('Messung')
      ax4.set_ylabel('Kosmische Korrektur')
      ax4.set_title('Kosmische Korrekturen (letzte 24)')
      ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig
  
  @staticmethod
  def plot_decoherence_simulation(qubit, steps=500):
    """Visualisiert Dekohärenz-Simulation für ein Qubit"""
    if not MATPLOTLIB_AVAILABLE:
      print("Visualisierung deaktiviert: matplotlib nicht installiert")
      return None
      
    times, coherence = qubit.simulate_decoherence_path(steps)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Dekohärenz-Kurve
    ax1.plot(times*1e6, coherence, 'b-', linewidth=2, label='Kohärenz')
    ax1.axhline(1/np.e, color='r', linestyle='--', label=f'1/e = {1/np.e:.3f}')
    ax1.set_xlabel('Zeit (μs)')
    ax1.set_ylabel('Kohärenz')
    ax1.set_title(f'Dekohärenz von Qubit {qubit.qubit_id}')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Zustandsvektor auf Bloch-Kugel (vereinfacht)
    ax2 = fig.add_subplot(122, projection='3d')
    
    # Erzeuge Bloch-Kugel
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))
    
    ax2.plot_surface(x, y, z, color='lightblue', alpha=0.3)
    
    # Qubit-Zustand
    state = qubit.get_quantum_state_vector()
    theta = 2 * np.arccos(np.abs(state[0]))
    phi = np.angle(state[1]) - np.angle(state[0])
    
    x_state = np.sin(theta) * np.cos(phi)
    y_state = np.sin(theta) * np.sin(phi)
    z_state = np.cos(theta)
    
    ax2.scatter([x_state], [y_state], [z_state], color='red', s=100, label='Qubit-Zustand')
    ax2.plot([0, x_state], [0, y_state], [0, z_state], 'r-', linewidth=2)
    
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')
    ax2.set_title('Zustand auf Bloch-Kugel')
    ax2.legend()
    
    plt.tight_layout()
    return fig

# Beispiel-Nutzung und Demo
if __name__ == "__main__":
  print("=" * 80)
  print("T0-COSMIC-QUBIT-SIMULATOR - ERWEITERTE VERSION (KORRIGIERT)")
  print(f"Startzeit: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
  print("=" * 80)
  
  # Erstelle ein Array von Qubits mit verschiedenen Positionen
  print("\n📊 Initialisiere Qubit-Array...")
  qubits = []
  
  # Erzeuge Qubits in fraktaler Anordnung
  np.random.seed(42) # Für Reproduzierbarkeit
  n_qubits = 16
  
  for i in range(n_qubits):
    # Fraktale Positionen (Mandelbrot-ähnlich)
    angle = 2 * np.pi * i / n_qubits
    radius = 2 + 0.5 * np.sin(3 * angle)
    x = radius * np.cos(angle)
    y = radius * np.sin(angle)
    z = 0.5 * np.sin(2 * angle) # Leichte 3D-Variation
    
    qubit = EnhancedCosmicQubit(
      qubit_id=f"Q{i:03d}",
      position=(x, y, z),
      qubit_type='transmon'
    )
    qubits.append(qubit)
    
    if i < 3: # Zeige Details für erste 3 Qubits
      print(f" Qubit {qubit.qubit_id}: Position ({x:.2f}, {y:.2f}, {z:.2f})")
  
  print(f"✅ {len(qubits)} Qubits initialisiert")
  
  # Analysiere Qubits
  print("\n🔬 Analysiere kosmische Qubit-Eigenschaften...")
  
  t2_values = []
  position_factors = []
  
  for qubit in qubits:
    t2 = qubit.effective_coherence_time() * 1e6 # In Mikrosekunden
    t2_values.append(t2)
    
    # Speichere einige Qubit-Daten
    if qubit.qubit_id in ["Q000", "Q001", "Q002"]:
      filename = qubit.save_to_file()
      print(f" {qubit.qubit_id}: T2 = {t2:.2f} μs (gespeichert in {filename})")
  
  # Statistische Analyse
  print("\n📈 Statistische Analyse:")
  print(f" Mittlere T2-Zeit: {np.mean(t2_values):.2f} ± {np.std(t2_values):.2f} μs")
  print(f" Minimum T2: {np.min(t2_values):.2f} μs")
  print(f" Maximum T2: {np.max(t2_values):.2f} μs")
  print(f" Variationskoeffizient: {(np.std(t2_values)/np.mean(t2_values)*100):.1f}%")
  
  # Kosmische Ausrichtung für erstes Qubit
  print("\n🌌 Kosmische Ausrichtung (Qubit Q000):")
  alignment = qubits[0].get_cosmic_alignment()
  for key, value in alignment.items():
    if isinstance(value, float):
      print(f" {key}: {value:.4f}")
  
  # Visualisierung (nur wenn matplotlib verfügbar)
  if MATPLOTLIB_AVAILABLE:
    print("\n🎨 Erzeuge Visualisierungen...")
    
    try:
      # Visualisiere Qubit-Positionen
      visualizer = CosmicQubitVisualizer()
      fig1 = visualizer.plot_qubit_positions(qubits)
      if fig1:
        fig1.savefig('qubit_positions.png', dpi=150, bbox_inches='tight')
        print(" ✅ Qubit-Positionsplot gespeichert als 'qubit_positions.png'")
      
      # Visualisiere Dekohärenz für ein Qubit
      fig2 = visualizer.plot_decoherence_simulation(qubits[0], steps=200)
      if fig2:
        fig2.savefig('decoherence_simulation.png', dpi=150, bbox_inches='tight')
        print(" ✅ Dekohärenz-Simulation gespeichert als 'decoherence_simulation.png'")
      
    except Exception as e:
      print(f" ⚠️ Visualisierung fehlgeschlagen: {e}")
  else:
    print("\nℹ️ Für Visualisierung installieren: pip install matplotlib")
  
  # Quantenzustände analysieren
  print("\n⚛️ Quantenzustandsanalyse:")
  for i, qubit in enumerate(qubits[:2]):
    state = qubit.get_quantum_state_vector()
    print(f" {qubit.qubit_id}: |ψ⟩ = ({state[0].real:.3f}{'+' if state[0].imag >= 0 else ''}{state[0].imag:.3f}i)|0⟩ + " +
       f"({state[1].real:.3f}{'+' if state[1].imag >= 0 else ''}{state[1].imag:.3f}i)|1⟩")
  
  # Fraktale Dimension Information
  print("\n🔶 Fraktale Torus-Parameter:")
  print(f" ξ = 4/30000 = {qubits[0].xi:.10f}")
  print(f" Fraktale Dimension D_f = 3 - ξ = {qubits[0].D_f:.10f}")
  print(f" Planck-Zeit: {qubits[0].planck_time:.2e} s")
  
  # Exportiere Zusammenfassung
  summary = {
    'simulation_time': datetime.now().isoformat(),
    'n_qubits': len(qubits),
    't2_mean': float(np.mean(t2_values)),
    't2_std': float(np.std(t2_values)),
    't2_min': float(np.min(t2_values)),
    't2_max': float(np.max(t2_values)),
    'qubit_types': list(set(q.qubit_type for q in qubits)),
    'fractal_dimension': float(qubits[0].D_f),
    'xi_parameter': float(qubits[0].xi)
  }
  
  with open('simulation_summary.json', 'w') as f:
    json.dump(summary, f, indent=2)
  
  print("\n💾 Simulations-Zusammenfassung gespeichert als 'simulation_summary.json'")
  
  print("\n" + "=" * 80)
  print("🚀 Simulation erfolgreich abgeschlossen!")
  print("=" * 80)
  
  if MATPLOTLIB_AVAILABLE:
    print("\n📁 Generierte Dateien:")
    print(" - qubit_positions.png (Visualisierung der Qubit-Positionen)")
    print(" - decoherence_simulation.png (Dekohärenz-Simulation)")
    print(" - simulation_summary.json (Statistische Zusammenfassung)")
    print(" - qubit_*.json (Einzelne Qubit-Daten)")
  
  print("\n🔧 Nächste Schritte:")
  print(" 1. Installieren Sie matplotlib für Visualisierung: pip install matplotlib")
  print(" 2. Erhöhen Sie n_qubits für detailliertere Simulationen")
  print(" 3. Experimentieren Sie mit verschiedenen Chip-Geometrien")
  print(" 4. Fügen Sie weitere kosmische Effekte hinzu (Sonnenstürme, etc.)")
  print(" 5. Nutzen Sie die JSON-Exporte für weitere Analysen")
