#!/usr/bin/env python3
"""
T0-COSMIC-ERROR-CORRECTION - VERBESSERTE VERSION (KORRIGIERT)
Mit realistischen Parametern und korrigierter Zeitoptimierung
"""

import numpy as np
from datetime import datetime, timedelta
from typing import List, Tuple, Dict, Any
import json
import math
import argparse
import sys
from collections import defaultdict

class EnhancedCosmicErrorCorrection:
  """Verbesserte kosmisch-synchrone Fehlerkorrektur mit realistischen Parametern"""
  
  def __init__(self, xi=0.001, location_lat=47.3769, location_lon=8.5417):
    self.xi = xi # Erhöht für stärkere Effekte
    self.D_f = 3 - xi
    self.location = (location_lat, location_lon)
    
    # REALISTISCHE Quantenfehlerkorrekturparameter (basierend auf aktueller Hardware)
    self.error_rates = {
      'single_qubit': 5e-3,   # 0.5% - typisch für moderne Transmons
      'two_qubit': 2e-2,     # 2% - typisch für CNOT-Gatter
      'measurement': 1e-2,    # 1% - Messfehler
      'idle': 5e-4,       # 0.05% pro Mikrosekunde - Dekohärenz
      'readout': 3e-2,      # 3% - Auslesefehler
      'reset': 2e-2,       # 2% - Reset-Fehler
    }
    
    # Kosmische Korrekturtabellen mit verstärkten Effekten
    self.correction_table = self._generate_enhanced_correction_table()
    self.quantum_codes = self._initialize_realistic_quantum_codes()
    
    # Simulationsdaten
    self.simulation_history = []
    self.error_log = []
    
    # Debug-Informationen
    self.debug_mode = False
    
  def _generate_enhanced_correction_table(self, hours=24, resolution=10):
    """Generiert Korrekturtabelle mit verstärkten kosmischen Effekten"""
    table = {}
    for hour in range(hours):
      for minute in range(0, 60, resolution):
        time_key = f"{hour:02d}:{minute:02d}"
        
        # Mehrere kosmische Faktoren kombinieren mit VERSTÄRKTEN Effekten
        time_of_day = hour + minute/60
        
        # 1. Tagesrhythmus (Sinus) - VERSTÄRKT
        daily_factor = np.sin(2*np.pi*time_of_day/24)
        
        # 2. Fraktale Modulation - VERSTÄRKT
        fractal_factor = 0.5 * np.sin(self.D_f * time_of_day * 2)
        
        # 3. Gezeiten-Effekt (vereinfacht) - VERSTÄRKT
        tide_factor = 0.3 * np.sin(2*np.pi*time_of_day/12.42)
        
        # 4. Saisonale Variation (Jahreszeit)
        day_of_year = datetime.now().timetuple().tm_yday
        seasonal_factor = 0.2 * np.sin(2*np.pi*day_of_year/365.25)
        
        # 5. Lunare Zyklen (Mondphasen)
        lunar_phase = (day_of_year % 29.53) / 29.53 # Vereinfacht
        lunar_factor = 0.15 * np.sin(2*np.pi*lunar_phase)
        
        # GESAMTKORREKTUR mit verstärkten Effekten (10x stärker als vorher)
        total_variation = (
          daily_factor * 3.0 +   # Tageseffekt verstärkt
          fractal_factor * 2.0 +  # Fraktaleffekt verstärkt 
          tide_factor +      # Gezeiten
          seasonal_factor +    # Jahreszeit
          lunar_factor       # Mondphasen
        )
        
        # Normalisiere und skaliere mit ξ (jetzt mit größerer Amplitude)
        correction = 1.0 + self.xi * 15.0 * total_variation
        
        # Begrenze auf realistische Werte (0.8 - 1.2 = ±20%)
        correction = max(0.8, min(1.2, correction))
        
        table[time_key] = correction
        
    return table
  
  def _initialize_realistic_quantum_codes(self):
    """Initialisiert realistische Quantenfehlerkorrekturcodes"""
    return {
      'surface_code': {
        'distance': 3,
        'threshold': 1e-2,   # 1% - theoretische Schwelle
        'overhead': 9,
        'realistic_threshold': 5e-3, # 0.5% - praktisch erreichbar
      },
      'color_code': {
        'distance': 3,
        'threshold': 2e-2,
        'overhead': 7,
        'realistic_threshold': 8e-3,
      },
      'repetition_code': {
        'distance': 5,
        'threshold': 5e-2,
        'overhead': 5,
        'realistic_threshold': 2e-2,
      },
      'cosmic_code': {
        'distance': max(3, int(1/self.xi)),
        'threshold': min(0.1, self.xi * 50), # Begrenzt auf 10%
        'overhead': max(5, int(3/self.xi)),
        'realistic_threshold': min(0.05, self.xi * 25),
      }
    }
  
  def get_time_correction(self, timestamp=None):
    """Gibt kosmische Korrektur für aktuellen Zeitpunkt mit realistischen Fluktuationen"""
    if timestamp is None:
      timestamp = datetime.now()
    
    hour = timestamp.hour
    minute = (timestamp.minute // 10) * 10 # 10-Minuten-Intervall für mehr Genauigkeit
    
    time_key = f"{hour:02d}:{minute:02d}"
    base_correction = self.correction_table.get(time_key, 1.0)
    
    # REALISTISCHE Quantenfluktuationen (stochastisch, aber begrenzt)
    quantum_fluctuation = 1.0 + np.random.normal(0, self.xi * 2)
    
    # Begrenze die Fluktuationen
    quantum_fluctuation = max(0.95, min(1.05, quantum_fluctuation))
    
    final_correction = base_correction * quantum_fluctuation
    
    if self.debug_mode:
      print(f"DEBUG: Zeit {time_key}, Basis={base_correction:.4f}, "
         f"Fluktuation={quantum_fluctuation:.4f}, Final={final_correction:.4f}")
    
    return final_correction
  
  def find_true_optimal_time(self, algorithm_type='shor', lookahead_hours=24):
    """Findet die tatsächlich optimale Zeit durch Suche über nächste 24 Stunden"""
    best_time = datetime.now()
    best_correction = 0
    best_window_info = None
    
    current_time = datetime.now()
    
    # Algorithmus-spezifische optimale Zeitfenster
    optimal_windows = {
      'shor': [(2, 6), (14, 18)],   # Primfaktorzerlegung
      'grover': [(0, 4), (20, 24)],  # Datenbanksuche
      'vqe': [(8, 12), (16, 20)],   # Variationsalgorithmus
      'qml': [(6, 10), (18, 22)],   # Quanten-ML
      'generic': [(0, 4), (12, 16)], # Allgemein
    }
    
    windows = optimal_windows.get(algorithm_type, optimal_windows['generic'])
    
    # Suche über nächste 24 Stunden
    for hour_offset in range(lookahead_hours):
      test_time = current_time + timedelta(hours=hour_offset)
      
      # Prüfe ob Zeit in optimalem Fenster
      test_hour = test_time.hour + test_time.minute/60
      in_optimal_window = False
      current_window = None
      
      for start, end in windows:
        if start <= test_hour < end:
          in_optimal_window = True
          current_window = (start, end)
          break
        
      # Wenn nicht in optimalem Fenster, geringere Priorität
      if not in_optimal_window:
        continue
        
      correction = self.get_time_correction(test_time)
      
      if correction > best_correction:
        best_correction = correction
        best_time = test_time
        best_window_info = current_window
    
    # Wenn nichts in optimalen Fenstern gefunden, suche allgemein
    if best_correction == 0:
      for hour_offset in range(lookahead_hours):
        test_time = current_time + timedelta(hours=hour_offset)
        correction = self.get_time_correction(test_time)
        
        if correction > best_correction:
          best_correction = correction
          best_time = test_time
    
    # Runde auf nächste volle 10 Minuten
    best_time = best_time.replace(
      minute=(best_time.minute // 10) * 10,
      second=0,
      microsecond=0
    )
    
    return {
      'optimal_start': best_time,
      'correction_factor': best_correction,
      'current_correction': self.get_time_correction(current_time),
      'improvement_percent': 100 * (best_correction - self.get_time_correction(current_time)),
      'wait_hours': (best_time - current_time).total_seconds() / 3600,
      'in_optimal_window': best_window_info is not None,
      'window': best_window_info,
    }
  
  def fractal_qubit_arrangement(self, n_qubits: int, arrangement_type='mandelbrot'):
    """Generiert fraktale Qubit-Anordnung mit realistischen Abständen"""
    positions = []
    
    # Realistische Chip-Dimensionen (in mm)
    chip_radius = 10.0 # 10mm Radius
    
    for i in range(n_qubits):
      if arrangement_type == 'logarithmic':
        angle = 2*np.pi*i/n_qubits
        radius = chip_radius * np.log(i+2) / np.log(n_qubits+1)
        
      elif arrangement_type == 'golden':
        angle = i * 2*np.pi * (1 - 1/1.618)
        radius = chip_radius * np.sqrt(i) / np.sqrt(n_qubits)
        
      elif arrangement_type == 'mandelbrot':
        angle = 2*np.pi*i/n_qubits
        base_radius = chip_radius * np.sqrt(i+1) / np.sqrt(n_qubits)
        radius = base_radius * (1 + 0.3*np.sin(7*angle))
        
      else: # 'circular'
        angle = 2*np.pi*i/n_qubits
        radius = chip_radius * (i+1) / n_qubits
      
      # D_f-abhängige Modulation
      fractal_mod = 0.5 * np.sin(self.D_f * angle) * np.cos(self.xi * radius * 10)
      
      # REALISTISCHE Positionen mit Mindestabstand
      min_distance = 0.5 # 0.5mm Mindestabstand zwischen Qubits
      
      x = radius * np.cos(angle) * (1 + 0.2*fractal_mod)
      y = radius * np.sin(angle) * (1 + 0.2*fractal_mod)
      z = 0.05 * np.sin(3*angle) * np.cos(2*radius) # Sehr kleine 3D-Variation
      
      # Sicherstellen, dass Mindestabstand eingehalten wird
      for attempt in range(10):
        too_close = False
        for px, py, pz in positions:
          dist = np.sqrt((x-px)**2 + (y-py)**2)
          if dist < min_distance:
            too_close = True
            # Leicht verschieben
            x += np.random.uniform(-0.1, 0.1)
            y += np.random.uniform(-0.1, 0.1)
            break
        
        if not too_close:
          break
      
      positions.append((float(x), float(y), float(z)))
    
    return positions
  
  def simulate_realistic_quantum_circuit(self, circuit_spec: Dict[str, Any]):
    """Simuliert Quantenschaltung mit realistischen Fehlerraten"""
    results = {
      'success_probability': 1.0,
      'success_probability_without_correction': 1.0,
      'corrected_errors': 0,
      'uncorrected_errors': 0,
      'total_errors': 0,
      'cosmic_improvement_factor': 1.0,
      'gate_fidelities': [],
      'gate_fidelities_without_correction': [],
      'error_events': [],
      'timestamps': [],
    }
    
    current_time = datetime.now()
    
    for gate_idx, gate in enumerate(circuit_spec.get('gates', [])):
      gate_type = gate.get('type', 'h')
      qubits = gate.get('qubits', [0])
      
      # REALISTISCHE Fehlerraten
      if len(qubits) > 1:
        base_error_rate = self.error_rates['two_qubit']
      elif gate_type == 'measure':
        base_error_rate = self.error_rates['measurement']
      elif gate_type == 'reset':
        base_error_rate = self.error_rates['reset']
      else:
        base_error_rate = self.error_rates['single_qubit']
      
      # Wende kosmische Korrektur an
      time_correction = self.get_time_correction(current_time)
      corrected_error_rate = base_error_rate / time_correction
      
      # Simuliere Fehlerereignisse
      rnd = np.random.random()
      
      if rnd < corrected_error_rate:
        error_type = 'corrected'
        results['corrected_errors'] += 1
        results['total_errors'] += 1
      elif rnd < base_error_rate:
        error_type = 'uncorrected'
        results['uncorrected_errors'] += 1
        results['total_errors'] += 1
      else:
        error_type = 'none'
      
      # Berechne Gatter-Treue
      fidelity_with_correction = 1.0 - corrected_error_rate
      fidelity_without_correction = 1.0 - base_error_rate
      
      results['gate_fidelities'].append(fidelity_with_correction)
      results['gate_fidelities_without_correction'].append(fidelity_without_correction)
      
      results['error_events'].append({
        'gate_idx': gate_idx,
        'gate_type': gate_type,
        'error_type': error_type,
        'base_error_rate': base_error_rate,
        'corrected_error_rate': corrected_error_rate,
        'correction_factor': time_correction,
      })
      
      results['timestamps'].append(current_time)
      
      # Fortschreiten der Zeit
      gate_duration = gate.get('duration', 0.1) # 100 ns standard
      current_time += timedelta(microseconds=gate_duration*1000)
    
    # Gesamtergebnis berechnen
    if results['gate_fidelities']:
      results['success_probability'] = np.prod(results['gate_fidelities'])
      results['success_probability_without_correction'] = np.prod(
        results['gate_fidelities_without_correction']
      )
      
      if results['success_probability_without_correction'] < 1.0:
        results['cosmic_improvement_factor'] = (
          (1 - results['success_probability_without_correction']) / 
          max(1e-10, (1 - results['success_probability']))
        )
      else:
        results['cosmic_improvement_factor'] = 1.0
    
    return results
  
  def calculate_realistic_threshold(self, code_type='surface_code'):
    """Berechnet realistische Fehlerschwellen mit kosmischen Korrekturen"""
    code_info = self.quantum_codes.get(code_type, self.quantum_codes['surface_code'])
    
    # Verwende realistische statt theoretische Schwellen
    realistic_threshold = code_info.get('realistic_threshold', code_info['threshold'])
    
    # Kosmische Verbesserung
    current_correction = self.get_time_correction()
    cosmic_enhancement = 1.0 + self.xi * 10 * (current_correction - 1)
    
    # Effektive Schwelle
    effective_threshold = realistic_threshold * cosmic_enhancement
    
    # Erforderliche Distanz für Zielgenauigkeit
    target_error = 1e-10 # Praktikableres Ziel als 1e-15
    if effective_threshold >= 1.0:
      required_distance = 1
    else:
      required_distance = math.ceil(
        math.log(target_error) / math.log(effective_threshold)
      )
    
    # Physikalische Qubit-Anzahl (realistisch)
    physical_qubits = code_info['overhead'] * (2*required_distance - 1)**2
    
    return {
      'code_type': code_type,
      'theoretical_threshold': code_info['threshold'],
      'realistic_threshold': realistic_threshold,
      'effective_threshold': effective_threshold,
      'cosmic_enhancement_factor': cosmic_enhancement,
      'required_distance': required_distance,
      'physical_qubits_per_logical': physical_qubits,
      'xi_parameter': self.xi,
      'fractal_dimension': self.D_f,
      'current_correction': current_correction,
    }
  
  def generate_adaptive_error_correction_schedule(self, computation_duration_hours=2):
    """Generiert adaptiven Fehlerkorrekturplan basierend auf Vorhersage"""
    schedule = []
    current_time = datetime.now()
    
    for hour_offset in range(computation_duration_hours):
      for minute_offset in [0, 20, 40]: # Alle 20 Minuten
        schedule_time = current_time + timedelta(
          hours=hour_offset, 
          minutes=minute_offset
        )
        
        time_correction = self.get_time_correction(schedule_time)
        
        # ADAPTIVE Fehlerkorrektur-Rate
        if time_correction > 1.10: # Sehr starke Unterstützung
          correction_rate = 'very_low'
          interval = 2000 # 2 Sekunden
          code = 'cosmic_code'
          
        elif time_correction > 1.05: # Starke Unterstützung
          correction_rate = 'low'
          interval = 1000 # 1 Sekunde
          code = 'cosmic_code'
          
        elif time_correction > 1.02: # Moderate Unterstützung
          correction_rate = 'medium'
          interval = 500  # 500 ms
          code = 'surface_code'
          
        elif time_correction > 0.98: # Neutrale Bedingungen
          correction_rate = 'high'
          interval = 200  # 200 ms
          code = 'surface_code'
          
        else: # Ungünstige Bedingungen
          correction_rate = 'very_high'
          interval = 100  # 100 ms
          code = 'repetition_code' # Robustester Code
        
        schedule.append({
          'time': schedule_time.strftime('%H:%M'),
          'correction_factor': time_correction,
          'correction_rate': correction_rate,
          'interval_ms': interval,
          'suggested_code': code,
          'estimated_fidelity_gain': (time_correction - 1) * 100,
        })
    
    return schedule
  
  def run_complete_analysis(self, n_qubits=12):
    """Führt eine vollständige kosmische Fehlerkorrekturaanalyse durch"""
    analysis = {}
    
    # 1. Aktuelle Bedingungen
    analysis['current_conditions'] = {
      'timestamp': datetime.now().isoformat(),
      'location': self.location,
      'xi': self.xi,
      'D_f': self.D_f,
      'current_correction': self.get_time_correction(),
      'improvement_percent': 100 * (self.get_time_correction() - 1),
    }
    
    # 2. Zeitoptimierung für verschiedene Algorithmen
    analysis['time_optimization'] = {}
    for algo in ['shor', 'grover', 'vqe', 'qml']:
      analysis['time_optimization'][algo] = self.find_true_optimal_time(
        algorithm_type=algo,
        lookahead_hours=48 # 2 Tage Vorausschau
      )
    
    # 3. Qubit-Anordnung
    analysis['qubit_arrangement'] = {
      'n_qubits': n_qubits,
      'positions': self.fractal_qubit_arrangement(n_qubits, 'mandelbrot'),
      'average_distance': self._calculate_average_qubit_distance(n_qubits),
    }
    
    # 4. Fehlerschwellen-Analyse
    analysis['threshold_analysis'] = {}
    for code in ['surface_code', 'color_code', 'cosmic_code']:
      analysis['threshold_analysis'][code] = self.calculate_realistic_threshold(code)
    
    # 5. Schaltungssimulation
    circuit = {
      'gates': [
        {
          'type': np.random.choice(['h', 'rz', 'cx', 't', 'measure']),
          'qubits': [np.random.randint(0, min(4, n_qubits))],
          'duration': 0.05 + 0.15 * np.random.random()
        }
        for _ in range(20) # 20 Gatter
      ]
    }
    analysis['simulation'] = self.simulate_realistic_quantum_circuit(circuit)
    
    # 6. Adaptiver Zeitplan
    analysis['adaptive_schedule'] = self.generate_adaptive_error_correction_schedule(6)
    
    # 7. Empfehlungen
    analysis['recommendations'] = self._generate_recommendations(analysis)
    
    return analysis
  
  def _calculate_average_qubit_distance(self, n_qubits):
    """Berechnet durchschnittlichen Abstand zwischen Qubits"""
    positions = self.fractal_qubit_arrangement(n_qubits, 'mandelbrot')
    total_distance = 0
    count = 0
    
    for i in range(n_qubits):
      for j in range(i+1, n_qubits):
        x1, y1, z1 = positions[i]
        x2, y2, z2 = positions[j]
        distance = np.sqrt((x1-x2)**2 + (y1-y2)**2)
        total_distance += distance
        count += 1
    
    return total_distance / count if count > 0 else 0
  
  def _generate_recommendations(self, analysis):
    """Generiert praktische Empfehlungen basierend auf der Analyse"""
    recs = []
    
    current_corr = analysis['current_conditions']['current_correction']
    
    if current_corr > 1.05:
      recs.append({
        'priority': 'high',
        'action': 'SOFORT STARTEN',
        'reason': f'Aktuelle kosmische Korrektur ist sehr günstig ({current_corr:.3f})',
        'expected_improvement': f'{100*(current_corr-1):.1f}%',
      })
    elif current_corr > 1.0:
      recs.append({
        'priority': 'medium',
        'action': 'Geeignet für nicht-kritische Berechnungen',
        'reason': f'Leichte kosmische Verbesserung ({current_corr:.3f})',
      })
    else:
      # Finde beste zukünftige Zeit
      best_algo = max(
        analysis['time_optimization'].items(),
        key=lambda x: x[1]['correction_factor']
      )
      recs.append({
        'priority': 'high',
        'action': 'WARTEN',
        'reason': f'Aktuelle Bedingungen ungünstig ({current_corr:.3f})',
        'recommended_wait': f'{best_algo[1]["wait_hours"]:.1f} Stunden',
        'recommended_time': best_algo[1]['optimal_start'].strftime('%H:%M'),
        'expected_improvement': f'{best_algo[1]["improvement_percent"]:.1f}%',
      })
    
    # Code-Empfehlung
    best_code = max(
      analysis['threshold_analysis'].items(),
      key=lambda x: x[1]['effective_threshold']
    )
    recs.append({
      'priority': 'medium',
      'action': f'Verwende {best_code[0]} für Fehlerkorrektur',
      'reason': f'Höchste effektive Schwelle: {best_code[1]["effective_threshold"]:.2e}',
    })
    
    return recs
  
  def save_analysis_report(self, analysis, filename=None):
    """Speichert Analysebericht im JSON-Format"""
    if filename is None:
      timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
      filename = f'cosmic_analysis_report_{timestamp}.json'
    
    # Füge Zusammenfassung hinzu
    summary = {
      'analysis_summary': {
        'total_qubits': analysis['qubit_arrangement']['n_qubits'],
        'best_algorithm_time': max(
          analysis['time_optimization'].items(),
          key=lambda x: x[1]['correction_factor']
        )[0],
        'best_correction_factor': max(
          algo_info['correction_factor'] 
          for algo_info in analysis['time_optimization'].values()
        ),
        'simulation_success_rate': analysis['simulation']['success_probability'],
        'recommended_action': analysis['recommendations'][0]['action'],
      }
    }
    
    analysis['summary'] = summary
    
    with open(filename, 'w') as f:
      json.dump(analysis, f, indent=2, default=str)
    
    return filename

def main():
  """Hauptfunktion mit erweiterten Befehlszeilenoptionen"""
  parser = argparse.ArgumentParser(
    description='VERBESSERTE T0-Kosmische Fehlerkorrektur für Quantencomputing',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog="""
Beispiele mit realistischen Parametern:
 %(prog)s --complete --qubits 16 --xi 0.001
 %(prog)s --find-best-time --algorithm grover --lookahead 48
 %(prog)s --realistic-simulation --gates 50
 %(prog)s --threshold-analysis --all-codes
 %(prog)s --adaptive-schedule --duration 8
 %(prog)s --debug --complete
    """
  )
  
  # Hauptparameter
  parser.add_argument('--xi', type=float, default=0.001,
            help='Fraktaler Parameter ξ (default: 0.001 für realistische Effekte)')
  parser.add_argument('--location', type=str, default='47.3769,8.5417',
            help='Geographische Position "lat,lon"')
  
  # Analysemodi
  parser.add_argument('--complete', action='store_true',
            help='Führt komplette Analyse durch')
  parser.add_argument('--qubits', type=int, default=12,
            help='Anzahl Qubits für Analyse (default: 12)')
  
  parser.add_argument('--find-best-time', action='store_true',
            help='Findet beste Zeit für Algorithmus')
  parser.add_argument('--algorithm', type=str, default='shor',
            choices=['shor', 'grover', 'vqe', 'qml', 'all'],
            help='Algorithmus für Zeitoptimierung')
  parser.add_argument('--lookahead', type=int, default=48,
            help='Vorausschau in Stunden (default: 48)')
  
  parser.add_argument('--realistic-simulation', action='store_true',
            help='Simuliert mit realistischen Fehlerraten')
  parser.add_argument('--gates', type=int, default=20,
            help='Anzahl Gatter für Simulation')
  
  parser.add_argument('--threshold-analysis', action='store_true',
            help='Fehlerschwellen-Analyse')
  parser.add_argument('--all-codes', action='store_true',
            help='Analysiert alle Quantencodes')
  
  parser.add_argument('--adaptive-schedule', action='store_true',
            help='Generiert adaptiven Fehlerkorrektur-Plan')
  parser.add_argument('--duration', type=int, default=6,
            help='Dauer des Zeitplans in Stunden')
  
  # Output-Optionen
  parser.add_argument('--output', type=str, default='',
            help='Ausgabedateiname (default: auto-generiert)')
  parser.add_argument('--verbose', '-v', action='store_true',
            help='Detaillierte Ausgabe')
  parser.add_argument('--debug', action='store_true',
            help='Debug-Modus mit zusätzlichen Informationen')
  parser.add_argument('--quiet', '-q', action='store_true',
            help='Minimale Ausgabe')
  
  args = parser.parse_args()
  
  # Initialisiere verbesserte kosmische Fehlerkorrektur
  try:
    lat, lon = map(float, args.location.split(','))
  except ValueError:
    print("Fehler: Ungültiges Koordinatenformat. Verwenden Sie 'lat,lon'")
    sys.exit(1)
    
  ce = EnhancedCosmicErrorCorrection(xi=args.xi, location_lat=lat, location_lon=lon)
  
  if args.debug:
    ce.debug_mode = True
  
  # Wenn keine Optionen angegeben wurden, Hilfe anzeigen
  if not any([args.complete, args.find_best_time, args.realistic_simulation,
        args.threshold_analysis, args.adaptive_schedule]) and len(sys.argv) > 1:
    parser.print_help()
    return
  
  # Standard: Komplette Analyse
  if len(sys.argv) == 1 or args.complete:
    if not args.quiet:
      print("=" * 80)
      print("VERBESSERTE KOSMISCHE FEHLERKORREKTUR - KOMPLETTE ANALYSE")
      print("=" * 80)
      print(f"\n🔧 Parameter: ξ={args.xi:.4f}, Qubits={args.qubits}, Ort={args.location}")
    
    analysis = ce.run_complete_analysis(n_qubits=args.qubits)
    
    # Ausgabe
    if not args.quiet:
      print(f"\n🌌 Aktuelle kosmische Bedingungen:")
      curr = analysis['current_conditions']
      print(f"  Korrektur: {curr['current_correction']:.4f}")
      print(f"  Verbesserung: {curr['improvement_percent']:+.2f}%")
      print(f"  Fraktale Dimension D_f: {curr['D_f']:.6f}")
      
      print(f"\n⏰ Beste Startzeiten:")
      for algo, info in analysis['time_optimization'].items():
        print(f"  {algo:6s}: {info['optimal_start'].strftime('%H:%M')} "
           f"(+{info['improvement_percent']:.1f}%, "
           f"Wartezeit: {info['wait_hours']:.1f}h)")
      
      print(f"\n⚡ Fehlerschwellen (effektiv):")
      for code, info in analysis['threshold_analysis'].items():
        print(f"  {code:15s}: {info['effective_threshold']:.2e} "
           f"(Verbesserung: {info['cosmic_enhancement_factor']:.3f}x)")
      
      print(f"\n🔌 Simulation ({len(analysis['simulation']['gate_fidelities'])} Gatter):")
      sim = analysis['simulation']
      print(f"  Erfolg mit Korrektur:  {sim['success_probability']*100:.2f}%")
      print(f"  Erfolg ohne Korrektur:  {sim['success_probability_without_correction']*100:.2f}%")
      print(f"  Kosmische Verbesserung: {sim['cosmic_improvement_factor']:.2f}x")
      print(f"  Korrigierte Fehler:   {sim['corrected_errors']}")
      print(f"  Unkorrigierte Fehler:  {sim['uncorrected_errors']}")
      
      print(f"\n📅 Adaptive Fehlerkorrektur (erste 3 Einträge):")
      for entry in analysis['adaptive_schedule'][:3]:
        print(f"  {entry['time']}: {entry['correction_rate']:10s} "
           f"(Faktor: {entry['correction_factor']:.4f})")
      
      print(f"\n💡 Empfehlungen:")
      for rec in analysis['recommendations']:
        print(f"  [{rec['priority'].upper():6s}] {rec['action']}")
        if 'reason' in rec:
          print(f"    Grund: {rec['reason']}")
    
    # Speichern
    filename = ce.save_analysis_report(
      analysis, 
      args.output if args.output else None
    )
    
    if not args.quiet:
      print(f"\n💾 Kompletter Bericht gespeichert in: {filename}")
      print("\n" + "=" * 80)
      print("🚀 VERBESSERTE KOSMISCHE FEHLERKORREKTUR ANALYSE ABGESCHLOSSEN!")
      print("=" * 80)
  
  elif args.find_best_time:
    if args.algorithm == 'all':
      for algo in ['shor', 'grover', 'vqe', 'qml']:
        result = ce.find_true_optimal_time(algo, args.lookahead)
        print(f"\n{algo.upper():6s}: {result['optimal_start'].strftime('%Y-%m-%d %H:%M')}")
        print(f"  Korrektur: {result['correction_factor']:.4f}")
        print(f"  Verbesserung: {result['improvement_percent']:+.2f}%")
        print(f"  Wartezeit: {result['wait_hours']:.1f}h")
    else:
      result = ce.find_true_optimal_time(args.algorithm, args.lookahead)
      print(f"\nOptimale Zeit für {args.algorithm}:")
      print(f"  Start: {result['optimal_start'].strftime('%Y-%m-%d %H:%M')}")
      print(f"  Korrektur: {result['correction_factor']:.4f}")
      print(f"  Aktuelle Korrektur: {result['current_correction']:.4f}")
      print(f"  Verbesserung: {result['improvement_percent']:+.2f}%")
      print(f"  Wartezeit: {result['wait_hours']:.1f}h")
      if result['in_optimal_window']:
        print(f"  Im optimalen Fenster: {result['window'][0]:02d}:00-{result['window'][1]:02d}:00")
  
  elif args.realistic_simulation:
    circuit = {
      'gates': [
        {
          'type': np.random.choice(['h', 'rz', 'cx', 't', 'measure', 'reset']),
          'qubits': [np.random.randint(0, 4)],
          'duration': 0.05 + 0.15 * np.random.random()
        }
        for _ in range(args.gates)
      ]
    }
    
    result = ce.simulate_realistic_quantum_circuit(circuit)
    
    print(f"\nRealistische Simulation ({args.gates} Gatter):")
    print(f"  Erfolg mit Korrektur:  {result['success_probability']*100:.2f}%")
    print(f"  Erfolg ohne Korrektur:  {result['success_probability_without_correction']*100:.2f}%")
    print(f"  Kosmische Verbesserung: {result['cosmic_improvement_factor']:.2f}x")
    print(f"  Gesamtfehler:      {result['total_errors']}")
    print(f"  Korrigierte Fehler:   {result['corrected_errors']}")
    print(f"  Unkorrigierte Fehler:  {result['uncorrected_errors']}")
    
    if args.verbose:
      print(f"\n  Gatter-Treue (erste 5):")
      for i, (f_with, f_without) in enumerate(
        zip(result['gate_fidelities'][:5], 
          result['gate_fidelities_without_correction'][:5])
      ):
        print(f"   Gatter {i}: {f_with*100:.1f}% (mit) vs {f_without*100:.1f}% (ohne)")
  
  elif args.threshold_analysis:
    codes_to_analyze = ['surface_code', 'color_code', 'repetition_code', 'cosmic_code'] \
      if args.all_codes else ['cosmic_code']
    
    print(f"\nFehlerschwellen-Analyse:")
    for code in codes_to_analyze:
      result = ce.calculate_realistic_threshold(code)
      print(f"\n{code.upper():15s}:")
      print(f"  Theoretische Schwelle: {result['theoretical_threshold']:.2e}")
      print(f"  Realistische Schwelle: {result['realistic_threshold']:.2e}")
      print(f"  Effektive Schwelle:   {result['effective_threshold']:.2e}")
      print(f"  Kosmische Verbesserung: {result['cosmic_enhancement_factor']:.3f}x")
      print(f"  Benötigte Distanz:   {result['required_distance']}")
      print(f"  Physikalische Qubits:  {result['physical_qubits_per_logical']:,}")
  
  elif args.adaptive_schedule:
    schedule = ce.generate_adaptive_error_correction_schedule(args.duration)
    
    print(f"\nAdaptiver Fehlerkorrektur-Plan ({args.duration} Stunden):")
    print(f"  Intervall: Alle 20 Minuten")
    print(f"\n  Zeit   | Rate    | Code      | Korrektur | Verbesserung")
    print(f"  " + "-" * 60)
    
    for entry in schedule[:min(12, len(schedule))]: # Max 12 Einträge anzeigen
      print(f"  {entry['time']} | {entry['correction_rate']:10s} | "
         f"{entry['suggested_code']:14s} | {entry['correction_factor']:.4f}  | "
         f"{entry['estimated_fidelity_gain']:+.2f}%")
    
    if len(schedule) > 12:
      print(f"  ... und {len(schedule)-12} weitere Einträge")

if __name__ == "__main__":
  main()
