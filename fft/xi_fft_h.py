"""
ξ-FFT mit Harmonischen-Auswahl - ERWEITERTE Version
================================================

Neue Features:
- Konfigurierbare Harmonischen-Auswahl
- Anpassbare Harmonien-Sets für verschiedene Anwendungen
- Performance-Optimierung durch selektive Analyse
- Benutzerfreundliche Harmonien-Presets

Verwendung:
python xi_fft_harmonic_selection.py

Abhängigkeiten:
pip install numpy matplotlib tkinter wave

NEUE HARMONIEN-KONFIGURATION:
- Preset-Auswahl (Minimal, Standard, Vollständig, Benutzerdef.)
- Kategorien-basierte Auswahl (Perfekt, Konsonant, Dissonant)
- Prioritäts-basierte Begrenzung
- Individuelle Harmonien-Aktivierung
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
from typing import List, Dict, Set, Optional, Tuple
from fractions import Fraction

# ===== ERWEITERTE HARMONISCHE KONFIGURATION =====
class HarmonicConfiguration:
    """
    Erweiterte Konfiguration für Harmonische Auswahl und Priorisierung
    
    Ermöglicht flexible Anpassung der harmonischen Suche:
    - Preset-basierte Konfiguration
    - Kategorien-Filter
    - Prioritäts-Limits
    - Individuelle Harmonien-Auswahl
    """
    
    def __init__(self):
        """Initialisiere Harmonische Konfiguration"""
        
        # Vollständige Harmonische Datenbank
        self.ALL_HARMONICS = {
            # Perfekte Konsonanzen (Phase 1):
            'unison': {'ratio': 1.0, 'name': 'Unison', 'category': 'Perfect', 'priority': 1, 'phase': 1},
            'octave': {'ratio': 2.0, 'name': 'Oktave', 'category': 'Perfect', 'priority': 1, 'phase': 1},
            'fifth': {'ratio': 1.5, 'name': 'Quinte', 'category': 'Perfect', 'priority': 2, 'phase': 1},
            'fourth': {'ratio': 4/3, 'name': 'Quarte', 'category': 'Perfect', 'priority': 2, 'phase': 1},
            
            # Imperfekte Konsonanzen (Phase 2):
            'major_third': {'ratio': 1.25, 'name': 'Große Terz', 'category': 'Consonant', 'priority': 3, 'phase': 2},
            'minor_third': {'ratio': 1.2, 'name': 'Kleine Terz', 'category': 'Consonant', 'priority': 3, 'phase': 2},
            'major_sixth': {'ratio': 5/3, 'name': 'Große Sexte', 'category': 'Consonant', 'priority': 3, 'phase': 2},
            'minor_sixth': {'ratio': 1.6, 'name': 'Kleine Sexte', 'category': 'Consonant', 'priority': 3, 'phase': 2},
            
            # Erweiterte Konsonanzen:
            'major_tenth': {'ratio': 2.5, 'name': 'Große Dezime', 'category': 'Consonant', 'priority': 4, 'phase': 2},
            'compound_fifth': {'ratio': 3.0, 'name': 'Compound Quinte', 'category': 'Consonant', 'priority': 4, 'phase': 2},
            
            # Dissonanzen (Phase 3):
            'major_second': {'ratio': 9/8, 'name': 'Großer Ganzton', 'category': 'Dissonant', 'priority': 5, 'phase': 3},
            'minor_second': {'ratio': 10/9, 'name': 'Kleiner Ganzton', 'category': 'Dissonant', 'priority': 5, 'phase': 3},
            'major_seventh': {'ratio': 15/8, 'name': 'Große Septime', 'category': 'Dissonant', 'priority': 6, 'phase': 3},
            'minor_seventh': {'ratio': 16/9, 'name': 'Kleine Septime', 'category': 'Dissonant', 'priority': 6, 'phase': 3},
            
            # Harmonische Obertöne (Phase 3):
            'harmonic_7th': {'ratio': 1.75, 'name': 'Harmonische 7te', 'category': 'Complex', 'priority': 7, 'phase': 3},
            'harmonic_9th': {'ratio': 2.25, 'name': 'Harmonische 9te', 'category': 'Complex', 'priority': 7, 'phase': 3},
            'harmonic_11th': {'ratio': 2.75, 'name': 'Harmonische 11te', 'category': 'Complex', 'priority': 8, 'phase': 3},
            'harmonic_13th': {'ratio': 3.25, 'name': 'Harmonische 13te', 'category': 'Complex', 'priority': 8, 'phase': 3},
            
            # Mikrotonale Intervalle (Phase 4):
            'semitone': {'ratio': 16/15, 'name': 'Kleiner Halbton', 'category': 'Microtone', 'priority': 9, 'phase': 4},
            'chromatic': {'ratio': 25/24, 'name': 'Chromatischer HT', 'category': 'Microtone', 'priority': 9, 'phase': 4},
            'comma': {'ratio': 81/80, 'name': 'Syntonisches Komma', 'category': 'Microtone', 'priority': 10, 'phase': 4},
            
            # Schwebungs-relevante Verhältnisse (Phase 4):
            'beating_1': {'ratio': 1.01, 'name': '1% Schwebung', 'category': 'Beating', 'priority': 11, 'phase': 4},
            'beating_2': {'ratio': 1.02, 'name': '2% Schwebung', 'category': 'Beating', 'priority': 11, 'phase': 4},
            'beating_5': {'ratio': 1.05, 'name': '5% Schwebung', 'category': 'Beating', 'priority': 11, 'phase': 4},
            'beating_10': {'ratio': 1.1, 'name': '10% Schwebung', 'category': 'Beating', 'priority': 11, 'phase': 4},
        }
        
        # Vordefinierte Presets
        self.PRESETS = {
            'minimal': {
                'name': 'Minimal (Nur Grundlagen)',
                'description': '4 wichtigste Harmonien - Sehr schnell',
                'harmonics': {'unison', 'octave', 'fifth', 'fourth'},
                'max_phases': 1,
                'estimated_time_factor': 0.2
            },
            'standard': {
                'name': 'Standard (Musikalisch)',
                'description': '8 Standard-Harmonien - Gute Balance',
                'harmonics': {'unison', 'octave', 'fifth', 'fourth', 'major_third', 'minor_third', 'major_sixth', 'minor_sixth'},
                'max_phases': 2,
                'estimated_time_factor': 0.5
            },
            'extended': {
                'name': 'Erweitert (Vollständig)',
                'description': '16 Harmonien inkl. Dissonanzen',
                'harmonics': {'unison', 'octave', 'fifth', 'fourth', 'major_third', 'minor_third', 'major_sixth', 'minor_sixth',
                             'major_tenth', 'compound_fifth', 'major_second', 'minor_second', 'major_seventh', 'minor_seventh',
                             'harmonic_7th', 'harmonic_9th'},
                'max_phases': 3,
                'estimated_time_factor': 0.8
            },
            'complete': {
                'name': 'Komplett (Alle Harmonien)',
                'description': 'Alle 24 Harmonien - Sehr präzise aber langsam',
                'harmonics': set(self.ALL_HARMONICS.keys()),
                'max_phases': 4,
                'estimated_time_factor': 1.0
            },
            'beating_focus': {
                'name': 'Schwebungs-Fokus',
                'description': 'Optimiert für Schwebungsanalyse',
                'harmonics': {'unison', 'octave', 'fifth', 'fourth', 'beating_1', 'beating_2', 'beating_5', 'beating_10'},
                'max_phases': 4,
                'estimated_time_factor': 0.4
            },
            'consonant_only': {
                'name': 'Nur Konsonanzen',
                'description': 'Perfekte + Imperfekte Konsonanzen',
                'harmonics': {k for k, v in self.ALL_HARMONICS.items() if v['category'] in ['Perfect', 'Consonant']},
                'max_phases': 2,
                'estimated_time_factor': 0.6
            },
            'custom': {
                'name': 'Benutzerdefiniert',
                'description': 'Individuelle Auswahl',
                'harmonics': set(),
                'max_phases': 4,
                'estimated_time_factor': 0.5
            }
        }
        
        # Aktuelle Konfiguration
        self.current_preset = 'standard'
        self.active_harmonics = self.PRESETS['standard']['harmonics'].copy()
        self.max_phases = self.PRESETS['standard']['max_phases']
        
        print(f"🎼 HarmonicConfiguration: {len(self.ALL_HARMONICS)} Harmonien, {len(self.PRESETS)} Presets")
    
    def set_preset(self, preset_name: str) -> bool:
        """
        Setze vordefiniertes Harmonien-Preset
        
        Args:
            preset_name: Name des Presets
            
        Returns:
            True bei Erfolg
        """
        if preset_name in self.PRESETS:
            self.current_preset = preset_name
            preset = self.PRESETS[preset_name]
            self.active_harmonics = preset['harmonics'].copy()
            self.max_phases = preset['max_phases']
            
            print(f"🎵 Preset '{preset['name']}' aktiviert: {len(self.active_harmonics)} Harmonien")
            return True
        return False
    
    def get_active_harmonics_list(self) -> List[Dict]:
        """
        Hole Liste der aktiven Harmonien für die Analyse
        
        Returns:
            Liste der aktiven Harmonien mit Details
        """
        active_list = []
        
        for harmonic_id in self.active_harmonics:
            if harmonic_id in self.ALL_HARMONICS:
                harmonic = self.ALL_HARMONICS[harmonic_id].copy()
                harmonic['id'] = harmonic_id
                harmonic['search_width'] = self._get_search_width(harmonic)
                harmonic['resolution'] = self._get_resolution(harmonic)
                active_list.append(harmonic)
        
        # Sortiere nach Priorität
        active_list.sort(key=lambda h: (h['priority'], h['phase']))
        return active_list
    
    def _get_search_width(self, harmonic: Dict) -> float:
        """Bestimme Such-Breite basierend auf Harmonie-Typ"""
        category = harmonic['category']
        priority = harmonic['priority']
        
        if category == 'Perfect':
            return 3.0
        elif category == 'Consonant':
            return 2.0
        elif category == 'Dissonant':
            return 1.5
        elif category in ['Complex', 'Microtone']:
            return 1.0
        elif category == 'Beating':
            return 0.5
        else:
            return 2.0
    
    def _get_resolution(self, harmonic: Dict) -> float:
        """Bestimme Auflösung basierend auf Harmonie-Typ"""
        category = harmonic['category']
        priority = harmonic['priority']
        
        if category == 'Perfect':
            return 0.05
        elif category == 'Consonant':
            return 0.1
        elif category == 'Dissonant':
            return 0.15
        elif category in ['Complex', 'Microtone']:
            return 0.2
        elif category == 'Beating':
            return 0.02  # Sehr fein für Schwebungen
        else:
            return 0.1
    
    def add_harmonic(self, harmonic_id: str) -> bool:
        """Füge Harmonie zur aktiven Liste hinzu"""
        if harmonic_id in self.ALL_HARMONICS:
            self.active_harmonics.add(harmonic_id)
            if self.current_preset != 'custom':
                self.current_preset = 'custom'
            return True
        return False
    
    def remove_harmonic(self, harmonic_id: str) -> bool:
        """Entferne Harmonie aus aktiver Liste"""
        if harmonic_id in self.active_harmonics:
            self.active_harmonics.remove(harmonic_id)
            if self.current_preset != 'custom':
                self.current_preset = 'custom'
            return True
        return False
    
    def get_category_harmonics(self, category: str) -> Set[str]:
        """Hole alle Harmonien einer Kategorie"""
        return {k for k, v in self.ALL_HARMONICS.items() if v['category'] == category}
    
    def get_phase_harmonics(self, phase: int) -> Set[str]:
        """Hole alle Harmonien einer Phase"""
        return {k for k, v in self.ALL_HARMONICS.items() if v['phase'] == phase}
    
    def estimate_analysis_time(self, base_time: float) -> float:
        """Schätze Analysezeit basierend auf aktiver Konfiguration"""
        if self.current_preset in self.PRESETS:
            factor = self.PRESETS[self.current_preset]['estimated_time_factor']
        else:
            factor = len(self.active_harmonics) / len(self.ALL_HARMONICS)
        
        return base_time * factor
    
    def get_configuration_summary(self) -> str:
        """Hole Zusammenfassung der aktuellen Konfiguration"""
        preset_info = self.PRESETS.get(self.current_preset, {})
        active_count = len(self.active_harmonics)
        total_count = len(self.ALL_HARMONICS)
        
        categories = {}
        phases = {}
        
        for harmonic_id in self.active_harmonics:
            if harmonic_id in self.ALL_HARMONICS:
                h = self.ALL_HARMONICS[harmonic_id]
                cat = h['category']
                phase = h['phase']
                categories[cat] = categories.get(cat, 0) + 1
                phases[phase] = phases.get(phase, 0) + 1
        
        summary = f"Preset: {preset_info.get('name', 'Unbekannt')}\n"
        summary += f"Aktive Harmonien: {active_count}/{total_count}\n"
        summary += f"Kategorien: {', '.join(f'{k}({v})' for k, v in categories.items())}\n"
        summary += f"Phasen: {', '.join(f'P{k}({v})' for k, v in phases.items())}\n"
        summary += f"Max. Phasen: {self.max_phases}\n"
        
        return summary

# ===== ERWEITERTE ξ-FFT MIT HARMONISCHEN-AUSWAHL =====
class SelectiveXiFFT:
    """
    Erweiterte ξ-FFT mit konfigurierbarer Harmonischen-Auswahl
    
    Features:
    - Flexible Harmonien-Konfiguration
    - Adaptive Suchstrategien pro Harmonie
    - Performance-Optimierung durch selektive Analyse
    - Detaillierte Harmonien-Metriken
    """
    
    def __init__(self, sample_rate=44100, threshold=0.005, harmonic_config=None):
        self.sample_rate = sample_rate
        self.threshold = threshold
        self.harmonic_config = harmonic_config or HarmonicConfiguration()
        
        print(f"🧠 SelectiveXiFFT initialisiert:")
        print(f"   Sample Rate: {sample_rate} Hz")
        print(f"   Harmonische Konfiguration: {len(self.harmonic_config.active_harmonics)} aktive Harmonien")
        print(f"   Preset: {self.harmonic_config.current_preset}")
    
    def analyze(self, signal, freq_range=(20, 2000), progress_callback=None, 
                min_amplitude=None, max_amplitude=None, f0_hint=None):
        """
        Selective harmonische Analyse mit konfigurierbaren Harmonien
        """
        start_time = time.time()
        
        print(f"🎼 Starte SELECTIVE ξ-FFT Analyse:")
        print(f"   Signal: {len(signal)} Samples")
        print(f"   Aktive Harmonien: {len(self.harmonic_config.active_harmonics)}")
        print(f"   f₀-Hinweis: {f0_hint or 'Auto-Detect'}")
        
        if len(signal) == 0:
            return {'peaks': [], 'xiRatios': [], 'peakCount': 0, 'analysisTime': 0}
        
        # Signal-Preprocessing
        processed_signal = self._preprocess_signal(signal, min_amplitude, max_amplitude)
        
        # Harmonische Analyse mit Auswahl
        if f0_hint:
            peaks = self._selective_harmonic_search(processed_signal, f0_hint, freq_range, progress_callback)
        else:
            peaks = self._standard_analysis_with_selection(processed_signal, freq_range, progress_callback)
        
        # ξ-Verhältnisse berechnen
        xi_ratios = self._calculate_xi_ratios(peaks)
        
        analysis_time = time.time() - start_time
        
        # Harmonische Metriken
        harmonic_metrics = self._calculate_harmonic_metrics(peaks)
        
        result = {
            'peaks': peaks,
            'xiRatios': xi_ratios,
            'peakCount': len(peaks),
            'dominantXi': xi_ratios[0] if xi_ratios else None,
            'analysisTime': analysis_time,
            'method': 'Selective Harmonic Search',
            
            # Harmonische Konfiguration
            'harmonicConfig': {
                'preset': self.harmonic_config.current_preset,
                'activeHarmonics': len(self.harmonic_config.active_harmonics),
                'totalHarmonics': len(self.harmonic_config.ALL_HARMONICS),
                'maxPhases': self.harmonic_config.max_phases
            },
            
            # Harmonische Metriken
            'harmonicMetrics': harmonic_metrics,
            
            # Performance-Metriken
            'performanceMetrics': {
                'totalTime': analysis_time,
                'peaksPerSecond': len(peaks) / analysis_time if analysis_time > 0 else 0,
                'harmonicsTestedCount': len(self.harmonic_config.active_harmonics),
                'efficiency': len(peaks) / len(self.harmonic_config.active_harmonics) if len(self.harmonic_config.active_harmonics) > 0 else 0
            }
        }
        
        print(f"✅ SELECTIVE Analyse abgeschlossen:")
        print(f"   Zeit: {analysis_time:.2f}s")
        print(f"   Peaks: {len(peaks)}")
        print(f"   Harmonische Treffer: {harmonic_metrics.get('harmonic_matches', 0)}")
        
        return result
    
    def _preprocess_signal(self, signal, min_amp, max_amp):
        """Signal-Preprocessing"""
        processed = signal.copy()
        
        # Amplituden-Filter
        if min_amp is not None:
            processed = np.where(np.abs(processed) >= min_amp, processed, 0)
        if max_amp is not None:
            processed = np.clip(processed, -max_amp, max_amp)
        
        # Performance-Optimierung: Limitiere auf 3 Sekunden
        max_samples = self.sample_rate * 3
        if len(processed) > max_samples:
            processed = processed[:max_samples]
            print(f"⚡ Signal optimiert: {len(processed)} Samples ({len(processed)/self.sample_rate:.1f}s)")
        
        return processed
    
    def _selective_harmonic_search(self, signal, f0_hint, freq_range, progress_callback):
        """
        Selective harmonische Suche mit konfigurierten Harmonien
        """
        peaks = []
        total_dft_calculations = 0
        min_freq, max_freq = freq_range
        
        print(f"🎼 Selective harmonische Suche um f₀={f0_hint} Hz")
        
        # Hole aktive Harmonien (bereits sortiert nach Priorität)
        active_harmonics = self.harmonic_config.get_active_harmonics_list()
        
        # Phase-basierte Analyse
        current_phase = 1
        phase_peaks = {}
        strong_peaks_found = 0
        
        for i, harmonic in enumerate(active_harmonics):
            # Phase-Wechsel-Logik
            if harmonic['phase'] > current_phase:
                current_phase = harmonic['phase']
                
                # Prüfe ob genügend starke Peaks in vorherigen Phasen gefunden
                if current_phase > self.harmonic_config.max_phases:
                    print(f"   ⏭️ Phase {current_phase} übersprungen (max_phases={self.harmonic_config.max_phases})")
                    break
                
                if current_phase > 2 and strong_peaks_found < 2:
                    print(f"   ⏭️ Phase {current_phase} übersprungen (zu wenige starke Peaks: {strong_peaks_found})")
                    break
                
                print(f"🔍 Phase {current_phase}: {harmonic['category']}-Harmonien")
            
            target_freq = f0_hint * harmonic['ratio']
            
            if min_freq <= target_freq <= max_freq:
                best_magnitude, best_freq, dft_count = self._precise_frequency_search(
                    signal, target_freq, harmonic['search_width'], harmonic['resolution']
                )
                total_dft_calculations += dft_count
                
                # Adaptiver Threshold basierend auf Priorität
                threshold_factor = 1.0 + (harmonic['priority'] - 1) * 0.1
                adapted_threshold = self.threshold * threshold_factor
                
                if best_magnitude > adapted_threshold:
                    peak_data = {
                        'frequency': round(best_freq, 3),
                        'magnitude': best_magnitude,
                        'magnitudeDB': 20 * math.log10(best_magnitude + 1e-10),
                        'harmonic_id': harmonic['id'],
                        'harmonic_name': harmonic['name'],
                        'harmonic_ratio': harmonic['ratio'],
                        'harmonic_category': harmonic['category'],
                        'priority': harmonic['priority'],
                        'phase': harmonic['phase'],
                        'is_harmonic_match': True
                    }
                    
                    peaks.append(peak_data)
                    
                    # Phase-Statistiken
                    phase_key = f"phase_{harmonic['phase']}"
                    if phase_key not in phase_peaks:
                        phase_peaks[phase_key] = 0
                    phase_peaks[phase_key] += 1
                    
                    # Starke Peaks zählen (für Phase-Entscheidungen)
                    if best_magnitude > self.threshold * 3:
                        strong_peaks_found += 1
                    
                    print(f"  ✅ {harmonic['name']}: {best_freq:.2f} Hz (Mag: {best_magnitude:.3f})")
            
            # Progress-Update
            if progress_callback:
                progress = int((i + 1) / len(active_harmonics) * 80)  # 80% für Harmonien
                progress_callback(progress, f"Harmonien: {harmonic['name']}")
        
        print(f"   📊 Phase-Verteilung: {phase_peaks}")
        print(f"   💪 Starke Peaks: {strong_peaks_found}")
        
        # Ergänzende Suche (falls wenige Harmonien gefunden)
        if len(peaks) < 4:
            print(f"🔍 Ergänzende Suche (wenige Harmonien gefunden)...")
            additional_peaks = self._supplementary_search(signal, freq_range, peaks, progress_callback)
            peaks.extend(additional_peaks)
        
        # Sortierung nach Magnitude
        peaks.sort(key=lambda x: x['magnitude'], reverse=True)
        return peaks[:50]  # Top 50
    
    def _standard_analysis_with_selection(self, signal, freq_range, progress_callback):
        """Standard-Analyse ohne f0-Hinweis aber mit Harmonien-Auswahl"""
        print(f"📊 Standard-Analyse mit Harmonien-Auswahl")
        peaks = []
        min_freq, max_freq = freq_range
        
        # Adaptive Auflösung
        active_count = len(self.harmonic_config.active_harmonics)
        if active_count <= 8:
            step_size = 0.5  # Fein für wenige Harmonien
        elif active_count <= 16:
            step_size = 1.0  # Mittel
        else:
            step_size = 2.0  # Grob für viele Harmonien
        
        test_freqs = np.arange(min_freq, max_freq, step_size)
        total_tests = len(test_freqs)
        
        print(f"   Teste {total_tests} Frequenzen mit {step_size} Hz Schritten")
        
        for i, freq in enumerate(test_freqs):
            magnitude = self._calculate_magnitude(signal, freq)
            
            if magnitude > self.threshold:
                # Versuche Harmonien-Zuordnung
                harmonic_match = self._find_harmonic_match(freq)
                
                peak_data = {
                    'frequency': round(freq, 2),
                    'magnitude': magnitude,
                    'magnitudeDB': 20 * math.log10(magnitude + 1e-10),
                    'is_harmonic_match': harmonic_match is not None
                }
                
                if harmonic_match:
                    peak_data.update({
                        'harmonic_id': harmonic_match['id'],
                        'harmonic_name': harmonic_match['name'],
                        'harmonic_category': harmonic_match['category'],
                        'estimated_f0': freq / harmonic_match['ratio']
                    })
                else:
                    peak_data.update({
                        'harmonic_name': 'Nicht-harmonisch',
                        'harmonic_category': 'Non-harmonic'
                    })
                
                peaks.append(peak_data)
            
            # Progress-Update
            if progress_callback and i % 50 == 0:
                progress = int((i / total_tests) * 100)
                progress_callback(progress, f"Standard: {freq:.1f} Hz ({len(peaks)} Peaks)")
        
        peaks.sort(key=lambda x: x['magnitude'], reverse=True)
        return peaks[:100]
    
    def _find_harmonic_match(self, frequency: float, tolerance: float = 0.05) -> Optional[Dict]:
        """
        Versuche eine Frequenz einer aktiven Harmonie zuzuordnen
        
        Args:
            frequency: Frequenz in Hz
            tolerance: Toleranz für Matching (5%)
            
        Returns:
            Harmonie-Info oder None
        """
        for harmonic_id in self.harmonic_config.active_harmonics:
            harmonic = self.harmonic_config.ALL_HARMONICS[harmonic_id]
            
            # Schätze mögliche Grundfrequenzen
            estimated_f0 = frequency / harmonic['ratio']
            
            # Prüfe ob f0 in realistischem Bereich (80-800 Hz)
            if 80 <= estimated_f0 <= 800:
                # Berechne erwartete Frequenz zurück
                expected_freq = estimated_f0 * harmonic['ratio']
                
                # Prüfe Toleranz
                if abs(expected_freq - frequency) / frequency <= tolerance:
                    result = harmonic.copy()
                    result['id'] = harmonic_id
                    result['estimated_f0'] = estimated_f0
                    return result
        
        return None
    
    def _precise_frequency_search(self, signal, target_freq, search_width, resolution):
        """Präzise Frequenz-Suche"""
        best_magnitude = 0
        best_freq = target_freq
        dft_count = 0
        
        search_start = target_freq - search_width
        search_end = target_freq + search_width
        
        for freq in np.arange(search_start, search_end, resolution):
            magnitude = self._calculate_magnitude(signal, freq)
            dft_count += 1
            
            if magnitude > best_magnitude:
                best_magnitude = magnitude
                best_freq = freq
        
        return best_magnitude, best_freq, dft_count
    
    def _supplementary_search(self, signal, freq_range, existing_peaks, progress_callback):
        """Ergänzende Breitband-Suche"""
        min_freq, max_freq = freq_range
        additional_peaks = []
        
        # Bereits abgedeckte Bereiche
        excluded_ranges = []
        for peak in existing_peaks:
            excluded_ranges.append((peak['frequency'] - 3, peak['frequency'] + 3))
        
        # Grobe Suche
        step_size = 3.0
        for freq in np.arange(min_freq, max_freq, step_size):
            is_excluded = any(start <= freq <= end for start, end in excluded_ranges)
            
            if not is_excluded:
                magnitude = self._calculate_magnitude(signal, freq)
                
                if magnitude > self.threshold * 0.5:
                    additional_peaks.append({
                        'frequency': round(freq, 1),
                        'magnitude': magnitude,
                        'magnitudeDB': 20 * math.log10(magnitude + 1e-10),
                        'harmonic_name': 'Ergänzend',
                        'harmonic_category': 'Supplementary',
                        'is_harmonic_match': False
                    })
        
        return additional_peaks[:8]  # Max 8 zusätzliche
    
    def _calculate_magnitude(self, signal, frequency):
        """DFT-Magnitude-Berechnung"""
        N = len(signal)
        real = imag = 0.0
        
        angle_step = -2 * math.pi * frequency / self.sample_rate
        
        for n in range(N):
            angle = angle_step * n
            real += signal[n] * math.cos(angle)
            imag += signal[n] * math.sin(angle)
        
        return math.sqrt(real * real + imag * imag) * 2 / N
    
    def _calculate_xi_ratios(self, peaks):
        """ξ-Verhältnis-Berechnung mit Harmonien-Bewertung"""
        ratios = []
        
        # Top 15 Peaks für Performance
        top_peaks = peaks[:15]
        
        for i in range(len(top_peaks)):
            for j in range(i + 1, len(top_peaks)):
                f1, f2 = top_peaks[i]['frequency'], top_peaks[j]['frequency']
                xi_ratio = max(f1, f2) / min(f1, f2)
                
                if 1.01 <= xi_ratio <= 10.0:
                    # Harmonische Klassifikation
                    harmonic_quality = self._assess_harmonic_quality(top_peaks[i], top_peaks[j])
                    
                    ratios.append({
                        'freqHigh': max(f1, f2),
                        'freqLow': min(f1, f2),
                        'xiRatio': round(xi_ratio, 4),
                        'significance': top_peaks[i]['magnitude'] * top_peaks[j]['magnitude'],
                        'peakIndices': [i, j],
                        'intervalName': self._classify_ratio(xi_ratio),
                        'harmonicQuality': harmonic_quality
                    })
        
        ratios.sort(key=lambda x: (
            -x['harmonicQuality']['score'],  # Höchste harmonische Qualität zuerst
            -x['significance']               # Dann nach Significance
        ))
        return ratios[:25]
    
    def _assess_harmonic_quality(self, peak1: Dict, peak2: Dict) -> Dict:
        """Bewerte harmonische Qualität zwischen zwei Peaks"""
        score = 0
        details = []
        
        # Bonus für harmonische Matches
        if peak1.get('is_harmonic_match', False):
            score += 5
            details.append("Peak1 harmonisch")
        
        if peak2.get('is_harmonic_match', False):
            score += 5
            details.append("Peak2 harmonisch")
        
        # Bonus für gleiche Harmonien-Kategorie
        cat1 = peak1.get('harmonic_category', 'Unknown')
        cat2 = peak2.get('harmonic_category', 'Unknown')
        
        if cat1 == cat2 and cat1 != 'Unknown':
            score += 3
            details.append(f"Gleiche Kategorie: {cat1}")
        
        # Bonus für perfekte/konsonante Kategorien
        if cat1 in ['Perfect', 'Consonant'] or cat2 in ['Perfect', 'Consonant']:
            score += 2
            details.append("Konsonante Harmonie")
        
        # Bonus für ähnliche f0-Schätzungen (wenn verfügbar)
        f0_1 = peak1.get('estimated_f0')
        f0_2 = peak2.get('estimated_f0')
        
        if f0_1 and f0_2:
            if abs(f0_1 - f0_2) / max(f0_1, f0_2) < 0.1:  # 10% Toleranz
                score += 4
                details.append(f"Ähnliche f0: {f0_1:.1f}≈{f0_2:.1f}")
        
        return {
            'score': score,
            'details': details,
            'max_possible': 19  # 5+5+3+2+4
        }
    
    def _classify_ratio(self, ratio):
        """Klassifiziere Verhältnis"""
        if abs(ratio - 2.0) < 0.05:
            return "~Oktave"
        elif abs(ratio - 1.5) < 0.03:
            return "~Quinte"
        elif abs(ratio - 1.333) < 0.03:
            return "~Quarte"
        elif abs(ratio - 1.25) < 0.02:
            return "~Große Terz"
        elif abs(ratio - 1.2) < 0.02:
            return "~Kleine Terz"
        elif 1.01 < ratio < 1.15:
            return "~Schwebung"
        else:
            return "Komplex"
    
    def _calculate_harmonic_metrics(self, peaks):
        """Berechne detaillierte Harmonische Metriken"""
        total_peaks = len(peaks)
        harmonic_matches = len([p for p in peaks if p.get('is_harmonic_match', False)])
        
        # Kategorie-Verteilung
        categories = {}
        phases = {}
        
        for peak in peaks:
            if peak.get('is_harmonic_match'):
                cat = peak.get('harmonic_category', 'Unknown')
                phase = peak.get('phase', 0)
                
                categories[cat] = categories.get(cat, 0) + 1
                phases[phase] = phases.get(phase, 0) + 1
        
        # Harmonische Qualität
        harmonic_ratio = harmonic_matches / total_peaks if total_peaks > 0 else 0
        
        if harmonic_ratio > 0.8:
            quality = 'Exzellent'
        elif harmonic_ratio > 0.6:
            quality = 'Gut'
        elif harmonic_ratio > 0.4:
            quality = 'Mittel'
        elif harmonic_ratio > 0.2:
            quality = 'Niedrig'
        else:
            quality = 'Sehr niedrig'
        
        return {
            'total_peaks': total_peaks,
            'harmonic_matches': harmonic_matches,
            'harmonic_ratio': round(harmonic_ratio, 3),
            'quality': quality,
            'category_distribution': categories,
            'phase_distribution': phases,
            'config_efficiency': harmonic_matches / len(self.harmonic_config.active_harmonics) if len(self.harmonic_config.active_harmonics) > 0 else 0
        }

# ===== ERWEITERTE GUI MIT HARMONISCHEN-AUSWAHL =====
class HarmonicSelectionXiFFTApp:
    """
    Erweiterte GUI mit Harmonischen-Auswahl und Konfiguration
    """
    
    def __init__(self, root):
        self.root = root
        self.root.title("ξ-FFT mit Harmonischen-Auswahl v2.1")
        self.root.geometry("1400x950")
        
        # Komponenten initialisieren
        self.harmonic_config = HarmonicConfiguration()
        self.xi_fft = SelectiveXiFFT(harmonic_config=self.harmonic_config)
        
        # Daten
        self.current_signal = None
        self.loaded_signal = None
        self.loaded_sample_rate = None
        self.current_analysis = None
        
        print("🎼 Starte ξ-FFT mit Harmonischen-Auswahl GUI v2.1...")
        self.setup_gui()
    
    def setup_gui(self):
        """Setup der erweiterten GUI"""
        
        # Header
        header_frame = tk.Frame(self.root, bg='darkgreen', height=45)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(header_frame, text="ξ-FFT mit Harmonischen-Auswahl v2.1", 
                              fg='white', bg='darkgreen', font=('Arial', 14, 'bold'))
        title_label.pack(side=tk.LEFT, padx=10, pady=8)
        
        self.status_var = tk.StringVar(value="🎼 Bereit für konfigurierbare Harmonien-Analyse")
        status_label = tk.Label(header_frame, textvariable=self.status_var, 
                               fg='yellow', bg='darkgreen', font=('Arial', 10))
        status_label.pack(side=tk.RIGHT, padx=10, pady=8)
        
        # Notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Tabs
        self.setup_harmonic_config_tab()
        self.setup_generator_tab()
        self.setup_file_analysis_tab()
        self.setup_results_tab()
        
        print("✅ Erweiterte GUI mit Harmonischen-Auswahl bereit")
    
    def setup_harmonic_config_tab(self):
        """Tab für Harmonische Konfiguration"""
        config_frame = ttk.Frame(self.notebook)
        self.notebook.add(config_frame, text="🎼 Harmonische Konfiguration")
        
        # Preset-Auswahl
        preset_frame = ttk.LabelFrame(config_frame, text="Harmonien-Presets")
        preset_frame.pack(fill=tk.X, padx=10, pady=5)
        
        preset_grid = ttk.Frame(preset_frame)
        preset_grid.pack(fill=tk.X, padx=5, pady=5)
        
        # Preset-Buttons in 3 Spalten
        self.preset_var = tk.StringVar(value=self.harmonic_config.current_preset)
        
        presets = list(self.harmonic_config.PRESETS.keys())
        for i, preset_key in enumerate(presets):
            preset_info = self.harmonic_config.PRESETS[preset_key]
            
            btn = ttk.Radiobutton(preset_grid, text=preset_info['name'], 
                                 variable=self.preset_var, value=preset_key,
                                 command=lambda p=preset_key: self.on_preset_changed(p))
            btn.grid(row=i//3, column=i%3, sticky=tk.W, padx=5, pady=2)
        
        # Preset-Beschreibung
        self.preset_desc_var = tk.StringVar()
        self.update_preset_description()
        ttk.Label(preset_frame, textvariable=self.preset_desc_var, 
                 foreground="darkblue", font=('Arial', 9)).pack(pady=5)
        
        # Harmonien-Details
        details_frame = ttk.LabelFrame(config_frame, text="Harmonische Details")
        details_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # 2-Spalten Layout
        details_grid = ttk.Frame(details_frame)
        details_grid.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Linke Spalte: Aktive Harmonien
        left_frame = ttk.LabelFrame(details_grid, text="Aktive Harmonien")
        left_frame.grid(row=0, column=0, sticky=tk.NSEW, padx=5, pady=5)
        
        # Treeview für aktive Harmonien
        self.active_tree = ttk.Treeview(left_frame, columns=('Ratio', 'Category', 'Phase'), height=12)
        self.active_tree.heading('#0', text='Name')
        self.active_tree.heading('Ratio', text='Verhältnis')
        self.active_tree.heading('Category', text='Kategorie')
        self.active_tree.heading('Phase', text='Phase')
        
        self.active_tree.column('#0', width=120)
        self.active_tree.column('Ratio', width=80)
        self.active_tree.column('Category', width=100)
        self.active_tree.column('Phase', width=60)
        
        self.active_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Rechte Spalte: Verfügbare Harmonien
        right_frame = ttk.LabelFrame(details_grid, text="Verfügbare Harmonien")
        right_frame.grid(row=0, column=1, sticky=tk.NSEW, padx=5, pady=5)
        
        # Treeview für verfügbare Harmonien
        self.available_tree = ttk.Treeview(right_frame, columns=('Ratio', 'Category', 'Phase'), height=12)
        self.available_tree.heading('#0', text='Name')
        self.available_tree.heading('Ratio', text='Verhältnis')
        self.available_tree.heading('Category', text='Kategorie')
        self.available_tree.heading('Phase', text='Phase')
        
        self.available_tree.column('#0', width=120)
        self.available_tree.column('Ratio', width=80)
        self.available_tree.column('Category', width=100)
        self.available_tree.column('Phase', width=60)
        
        self.available_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Spalten-Layout konfigurieren
        details_grid.columnconfigure(0, weight=1)
        details_grid.columnconfigure(1, weight=1)
        details_grid.rowconfigure(0, weight=1)
        
        # Control-Buttons
        btn_frame = ttk.Frame(details_frame)
        btn_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(btn_frame, text="← Hinzufügen", 
                  command=self.add_harmonic).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Entfernen →", 
                  command=self.remove_harmonic).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="🔄 Aktualisieren", 
                  command=self.refresh_harmonic_lists).pack(side=tk.LEFT, padx=20)
        
        # Performance-Schätzung
        perf_frame = ttk.LabelFrame(config_frame, text="Performance-Schätzung")
        perf_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.perf_estimate_var = tk.StringVar()
        ttk.Label(perf_frame, textvariable=self.perf_estimate_var, 
                 foreground="darkgreen", font=('Courier', 10)).pack(pady=5)
        
        # Konfiguration-Zusammenfassung
        summary_frame = ttk.LabelFrame(config_frame, text="Aktuelle Konfiguration")
        summary_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.config_summary_var = tk.StringVar()
        ttk.Label(summary_frame, textvariable=self.config_summary_var, 
                 foreground="darkblue", font=('Courier', 9), justify=tk.LEFT).pack(pady=5, anchor=tk.W)
        
        # Initial-Update
        self.refresh_harmonic_lists()
        self.update_configuration_display()
    
    def setup_generator_tab(self):
        """Generator Tab mit Harmonien-Info"""
        gen_frame = ttk.Frame(self.notebook)
        self.notebook.add(gen_frame, text="🎵 Signal-Generator")
        
        # Standard Generator-Steuerung
        control_frame = ttk.LabelFrame(gen_frame, text="Signal-Parameter")
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Parameter-Grid
        param_grid = ttk.Frame(control_frame)
        param_grid.pack(fill=tk.X, padx=5, pady=5)
        
        # Grundfrequenz
        ttk.Label(param_grid, text="Grundfrequenz f₀ (Hz):").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.f0_var = tk.DoubleVar(value=440.0)
        ttk.Spinbox(param_grid, from_=100.0, to=1000.0, increment=10.0, 
                   textvariable=self.f0_var, width=10, 
                   command=self.update_generator_preview).grid(row=0, column=1, padx=5, pady=2)
        
        # Schwebung
        ttk.Label(param_grid, text="Schwebung Δf (Hz):").grid(row=0, column=2, sticky=tk.W, padx=5, pady=2)
        self.delta_f_var = tk.DoubleVar(value=5.0)
        ttk.Spinbox(param_grid, from_=0.1, to=50.0, increment=0.5, 
                   textvariable=self.delta_f_var, width=10,
                   command=self.update_generator_preview).grid(row=0, column=3, padx=5, pady=2)
        
        # Dauer
        ttk.Label(param_grid, text="Dauer (s):").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.duration_var = tk.DoubleVar(value=2.0)
        ttk.Spinbox(param_grid, from_=1.0, to=5.0, increment=0.5, 
                   textvariable=self.duration_var, width=8,
                   command=self.update_generator_preview).grid(row=1, column=1, padx=5, pady=2)
        
        # Harmonische Vorhersage
        self.use_harmonic_prediction = tk.BooleanVar(value=True)
        ttk.Checkbutton(param_grid, text="🎼 Harmonische Vorhersage verwenden", 
                       variable=self.use_harmonic_prediction,
                       command=self.update_generator_preview).grid(row=1, column=2, columnspan=2, padx=5, pady=2)
        
        # Frequenz-Preview
        preview_frame = ttk.LabelFrame(gen_frame, text="Signal-Vorschau")
        preview_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.freq_preview_var = tk.StringVar()
        ttk.Label(preview_frame, textvariable=self.freq_preview_var, 
                 foreground="darkgreen", font=('Courier', 10)).pack(pady=5)
        
        self.harmonic_prediction_var = tk.StringVar()
        ttk.Label(preview_frame, textvariable=self.harmonic_prediction_var, 
                 foreground="darkblue", font=('Arial', 9), justify=tk.LEFT).pack(pady=5)
        
        # Buttons
        btn_frame = ttk.Frame(gen_frame)
        btn_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Button(btn_frame, text="🎵 Signal generieren", 
                  command=self.generate_signal).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="🧠 Mit Harmonien analysieren", 
                  command=self.analyze_generated_signal).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="💾 Als WAV speichern", 
                  command=self.save_generated_wav).pack(side=tk.LEFT, padx=5)
        
        # Status
        self.gen_status_var = tk.StringVar(value="🎼 Bereit für Signal-Generierung mit Harmonien-Vorhersage")
        ttk.Label(gen_frame, textvariable=self.gen_status_var, 
                 foreground="blue").pack(pady=5)
        
        self.gen_progress_var = tk.DoubleVar()
        self.gen_progress = ttk.Progressbar(gen_frame, variable=self.gen_progress_var, maximum=100)
        self.gen_progress.pack(fill=tk.X, padx=10, pady=2)
        
        # Initial-Update
        self.update_generator_preview()
    
    def setup_file_analysis_tab(self):
        """Datei-Analyse Tab"""
        file_frame = ttk.Frame(self.notebook)
        self.notebook.add(file_frame, text="📁 Datei-Analyse")
        
        # Datei-Steuerung
        file_control = ttk.LabelFrame(file_frame, text="WAV-Datei")
        file_control.pack(fill=tk.X, padx=10, pady=5)
        
        file_btn_frame = ttk.Frame(file_control)
        file_btn_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(file_btn_frame, text="📂 WAV-Datei laden", 
                  command=self.load_wav_file).pack(side=tk.LEFT, padx=5)
        
        self.file_info_var = tk.StringVar(value="Keine Datei geladen")
        ttk.Label(file_btn_frame, textvariable=self.file_info_var, 
                 foreground="gray").pack(side=tk.LEFT, padx=20)
        
        # Analyse-Parameter
        param_frame = ttk.LabelFrame(file_frame, text="Analyse-Parameter")
        param_frame.pack(fill=tk.X, padx=10, pady=5)
        
        param_grid = ttk.Frame(param_frame)
        param_grid.pack(fill=tk.X, padx=5, pady=5)
        
        # Frequenzbereich
        ttk.Label(param_grid, text="Frequenzbereich:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.min_freq_var = tk.IntVar(value=50)
        ttk.Spinbox(param_grid, from_=20, to=1000, increment=10, 
                   textvariable=self.min_freq_var, width=8).grid(row=0, column=1, padx=2, pady=2)
        ttk.Label(param_grid, text="bis").grid(row=0, column=2, padx=2)
        self.max_freq_var = tk.IntVar(value=2000)
        ttk.Spinbox(param_grid, from_=100, to=5000, increment=100, 
                   textvariable=self.max_freq_var, width=8).grid(row=0, column=3, padx=2, pady=2)
        ttk.Label(param_grid, text="Hz").grid(row=0, column=4, padx=2)
        
        # f0-Hinweis
        self.use_f0_hint = tk.BooleanVar(value=False)
        ttk.Checkbutton(param_grid, text="f₀-Hinweis:", 
                       variable=self.use_f0_hint,
                       command=self.toggle_f0_hint).grid(row=0, column=5, padx=10, pady=2)
        
        self.f0_hint_var = tk.DoubleVar(value=440.0)
        self.f0_hint_spinbox = ttk.Spinbox(param_grid, from_=50.0, to=2000.0, increment=10.0, 
                                          textvariable=self.f0_hint_var, width=8, state="disabled")
        self.f0_hint_spinbox.grid(row=0, column=6, padx=2, pady=2)
        
        # Threshold
        ttk.Label(param_grid, text="Threshold:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.threshold_var = tk.DoubleVar(value=0.005)
        ttk.Spinbox(param_grid, from_=0.001, to=0.1, increment=0.001, 
                   textvariable=self.threshold_var, width=8, format="%.3f").grid(row=1, column=1, padx=2, pady=2)
        
        # Buttons
        btn_frame = ttk.Frame(file_frame)
        btn_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Button(btn_frame, text="🧠 Mit Harmonien analysieren", 
                  command=self.analyze_file_with_harmonics).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="⚡ Schnell-Analyse", 
                  command=self.quick_analyze_file).pack(side=tk.LEFT, padx=5)
        
        # Status
        self.file_status_var = tk.StringVar(value="📁 Bereit für Datei-Analyse mit konfigurierten Harmonien")
        ttk.Label(file_frame, textvariable=self.file_status_var).pack(pady=5)
        
        self.file_progress_var = tk.DoubleVar()
        self.file_progress = ttk.Progressbar(file_frame, variable=self.file_progress_var, maximum=100)
        self.file_progress.pack(fill=tk.X, padx=10, pady=2)
    
    def setup_results_tab(self):
        """Ergebnisse Tab mit Harmonien-Details"""
        results_frame = ttk.Frame(self.notebook)
        self.notebook.add(results_frame, text="📊 Analyse-Ergebnisse")
        
        # Harmonische Metriken
        metrics_frame = ttk.LabelFrame(results_frame, text="🎼 Harmonische Metriken")
        metrics_frame.pack(fill=tk.X, padx=10, pady=5)
        
        metrics_grid = ttk.Frame(metrics_frame)
        metrics_grid.pack(fill=tk.X, pady=5)
        
        # Metriken in 4 Spalten
        col_frames = []
        for i in range(4):
            col = ttk.Frame(metrics_grid)
            col.grid(row=0, column=i, padx=5, pady=5, sticky=tk.N)
            col_frames.append(col)
        
        # Spalte 1: Peaks
        ttk.Label(col_frames[0], text="Peaks:", font=('Arial', 9, 'bold')).pack()
        self.total_peaks_var = tk.StringVar(value="--")
        ttk.Label(col_frames[0], textvariable=self.total_peaks_var).pack()
        self.harmonic_peaks_var = tk.StringVar(value="--")
        ttk.Label(col_frames[0], textvariable=self.harmonic_peaks_var, foreground="green").pack()
        
        # Spalte 2: Qualität
        ttk.Label(col_frames[1], text="Qualität:", font=('Arial', 9, 'bold')).pack()
        self.harmonic_ratio_var = tk.StringVar(value="--")
        ttk.Label(col_frames[1], textvariable=self.harmonic_ratio_var).pack()
        self.quality_var = tk.StringVar(value="--")
        ttk.Label(col_frames[1], textvariable=self.quality_var, foreground="blue").pack()
        
        # Spalte 3: Konfiguration
        ttk.Label(col_frames[2], text="Konfiguration:", font=('Arial', 9, 'bold')).pack()
        self.config_efficiency_var = tk.StringVar(value="--")
        ttk.Label(col_frames[2], textvariable=self.config_efficiency_var).pack()
        self.active_harmonics_var = tk.StringVar(value="--")
        ttk.Label(col_frames[2], textvariable=self.active_harmonics_var, foreground="orange").pack()
        
        # Spalte 4: Performance
        ttk.Label(col_frames[3], text="Performance:", font=('Arial', 9, 'bold')).pack()
        self.analysis_time_var = tk.StringVar(value="--")
        ttk.Label(col_frames[3], textvariable=self.analysis_time_var).pack()
        self.efficiency_var = tk.StringVar(value="--")
        ttk.Label(col_frames[3], textvariable=self.efficiency_var, foreground="red").pack()
        
        # Plots
        self.fig = Figure(figsize=(12, 8), facecolor='white')
        self.canvas = FigureCanvasTkAgg(self.fig, results_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # 2x2 Layout für Plots
        self.ax_waveform = self.fig.add_subplot(2, 2, 1)
        self.ax_spectrum = self.fig.add_subplot(2, 2, 2)
        self.ax_harmonics = self.fig.add_subplot(2, 2, 3)
        self.ax_config = self.fig.add_subplot(2, 2, 4)
        
        self.ax_waveform.set_title('Zeitverlauf')
        self.ax_spectrum.set_title('Frequenzspektrum')
        self.ax_harmonics.set_title('Harmonische Analyse')
        self.ax_config.set_title('Konfiguration-Effizienz')
        
        self.fig.tight_layout()
        
        # Detaillierte Ergebnisse
        text_frame = ttk.Frame(results_frame)
        text_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.results_text = tk.Text(text_frame, height=6, width=100)
        scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scrollbar.set)
        
        self.results_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # ===== HARMONISCHE KONFIGURATION FUNCTIONS =====
    def on_preset_changed(self, preset_key):
        """Preset-Änderung Handler"""
        if self.harmonic_config.set_preset(preset_key):
            self.xi_fft.harmonic_config = self.harmonic_config
            self.refresh_harmonic_lists()
            self.update_configuration_display()
            self.update_preset_description()
            self.status_var.set(f"🎼 Preset '{self.harmonic_config.PRESETS[preset_key]['name']}' aktiviert")
    
    def update_preset_description(self):
        """Update Preset-Beschreibung"""
        preset_key = self.preset_var.get()
        if preset_key in self.harmonic_config.PRESETS:
            preset = self.harmonic_config.PRESETS[preset_key]
            desc = f"{preset['description']} ({len(preset['harmonics'])} Harmonien)"
            self.preset_desc_var.set(desc)
    
    def refresh_harmonic_lists(self):
        """Aktualisiere Harmonien-Listen"""
        # Leere Treeviews
        for item in self.active_tree.get_children():
            self.active_tree.delete(item)
        for item in self.available_tree.get_children():
            self.available_tree.delete(item)
        
        # Aktive Harmonien
        active_harmonics = self.harmonic_config.get_active_harmonics_list()
        for harmonic in active_harmonics:
            self.active_tree.insert('', 'end', text=harmonic['name'],
                                   values=(f"{harmonic['ratio']:.3f}", 
                                          harmonic['category'], 
                                          harmonic['phase']))
        
        # Verfügbare (nicht aktive) Harmonien
        all_harmonics = self.harmonic_config.ALL_HARMONICS
        for harmonic_id, harmonic in all_harmonics.items():
            if harmonic_id not in self.harmonic_config.active_harmonics:
                self.available_tree.insert('', 'end', text=harmonic['name'],
                                          values=(f"{harmonic['ratio']:.3f}", 
                                                 harmonic['category'], 
                                                 harmonic['phase']))
    
    def add_harmonic(self):
        """Füge ausgewählte Harmonie hinzu"""
        selection = self.available_tree.selection()
        if not selection:
            messagebox.showwarning("Warnung", "Bitte wählen Sie eine Harmonie aus der rechten Liste!")
            return
        
        # Finde Harmonie-ID basierend auf Name
        selected_name = self.available_tree.item(selection[0])['text']
        harmonic_id = None
        
        for hid, harmonic in self.harmonic_config.ALL_HARMONICS.items():
            if harmonic['name'] == selected_name:
                harmonic_id = hid
                break
        
        if harmonic_id and self.harmonic_config.add_harmonic(harmonic_id):
            self.refresh_harmonic_lists()
            self.update_configuration_display()
            self.status_var.set(f"✅ Harmonie '{selected_name}' hinzugefügt")
    
    def remove_harmonic(self):
        """Entferne ausgewählte Harmonie"""
        selection = self.active_tree.selection()
        if not selection:
            messagebox.showwarning("Warnung", "Bitte wählen Sie eine Harmonie aus der linken Liste!")
            return
        
        # Finde Harmonie-ID
        selected_name = self.active_tree.item(selection[0])['text']
        harmonic_id = None
        
        for hid, harmonic in self.harmonic_config.ALL_HARMONICS.items():
            if harmonic['name'] == selected_name:
                harmonic_id = hid
                break
        
        if harmonic_id and self.harmonic_config.remove_harmonic(harmonic_id):
            self.refresh_harmonic_lists()
            self.update_configuration_display()
            self.status_var.set(f"❌ Harmonie '{selected_name}' entfernt")
    
    def update_configuration_display(self):
        """Update Konfiguration-Anzeige"""
        # Zusammenfassung
        summary = self.harmonic_config.get_configuration_summary()
        self.config_summary_var.set(summary)
        
        # Performance-Schätzung
        base_time = 2.0  # Geschätzte Basis-Zeit
        estimated_time = self.harmonic_config.estimate_analysis_time(base_time)
        
        efficiency = len(self.harmonic_config.active_harmonics) / len(self.harmonic_config.ALL_HARMONICS)
        
        perf_text = f"Geschätzte Analysezeit: {estimated_time:.1f}s (Effizienz: {efficiency:.1%})\n"
        perf_text += f"Aktive Harmonien: {len(self.harmonic_config.active_harmonics)}/{len(self.harmonic_config.ALL_HARMONICS)}"
        
        self.perf_estimate_var.set(perf_text)
        
        # Update Generator-Preview
        self.update_generator_preview()
    
    # ===== GENERATOR FUNCTIONS =====
    def update_generator_preview(self):
        """Update Generator-Vorschau"""
        try:
            f0 = self.f0_var.get()
            delta_f = self.delta_f_var.get()
            duration = self.duration_var.get()
            use_prediction = self.use_harmonic_prediction.get()
            
            # Frequenz-Info
            f1, f2, f3 = f0 - delta_f, f0, f0 + delta_f
            freq_text = f"🎵 Frequenzen: {f1:.1f} Hz | {f0:.1f} Hz | {f3:.1f} Hz"
            freq_text += f" → Schwebung: {2*delta_f:.1f} Hz"
            self.freq_preview_var.set(freq_text)
            
            # Harmonische Vorhersage
            if use_prediction:
                prediction_text = self.predict_harmonics_for_signal(f0, delta_f)
                self.harmonic_prediction_var.set(prediction_text)
            else:
                self.harmonic_prediction_var.set("Harmonische Vorhersage deaktiviert")
                
        except tk.TclError:
            pass  # Fehler bei unvollständiger Eingabe ignorieren
    
    def predict_harmonics_for_signal(self, f0, delta_f):
        """Vorhersage welche Harmonien erkannt werden"""
        predicted = []
        test_freqs = [f0 - delta_f, f0, f0 + delta_f]
        
        active_harmonics = self.harmonic_config.get_active_harmonics_list()
        
        for harmonic in active_harmonics[:8]:  # Top 8 für Anzeige
            for test_freq in test_freqs:
                expected_freq = f0 * harmonic['ratio']
                if abs(expected_freq - test_freq) / test_freq < 0.05:  # 5% Toleranz
                    predicted.append(f"{harmonic['name']} (~{expected_freq:.1f} Hz)")
                    break
        
        if predicted:
            return f"🎯 Erwartete Treffer: {', '.join(predicted[:4])}" + ("..." if len(predicted) > 4 else "")
        else:
            return "⚠️ Keine direkten Harmonien-Treffer erwartet"
    
    def generate_signal(self):
        """Generiere Signal"""
        try:
            f0 = self.f0_var.get()
            delta_f = self.delta_f_var.get()
            duration = self.duration_var.get()
            
            self.gen_status_var.set("🎵 Generiere Signal...")
            self.gen_progress_var.set(25)
            self.root.update()
            
            # Generiere 3-Frequenz Schwebungs-Signal
            t = np.linspace(0, duration, int(duration * 44100))
            f1, f2, f3 = f0 - delta_f, f0, f0 + delta_f
            
            signal = (0.4 * np.sin(2 * np.pi * f1 * t) + 
                     0.8 * np.sin(2 * np.pi * f2 * t) + 
                     0.4 * np.sin(2 * np.pi * f3 * t))
            
            # Normalisierung
            signal = signal / np.max(np.abs(signal)) * 0.7
            
            self.current_signal = signal
            self.gen_progress_var.set(100)
            self.gen_status_var.set(f"✅ Signal generiert: {len(signal)} Samples, {duration:.1f}s")
            
            self.status_var.set(f"🎵 Signal bereit - {len(signal)} Samples")
            
            # Zur Ergebnisse-Tab wechseln und Waveform zeigen
            self.notebook.select(3)
            self.plot_waveform(signal, 44100)
            
        except Exception as e:
            self.gen_status_var.set(f"❌ Fehler: {str(e)}")
            messagebox.showerror("Fehler", f"Signal-Generierung fehlgeschlagen:\n{str(e)}")
    
    def analyze_generated_signal(self):
        """Analysiere generiertes Signal mit Harmonien"""
        if self.current_signal is None:
            messagebox.showwarning("Warnung", "Erst Signal generieren!")
            return
        
        def analyze_thread():
            try:
                f0 = self.f0_var.get()
                use_prediction = self.use_harmonic_prediction.get()
                
                # Konfiguriere Analyzer
                self.xi_fft.threshold = 0.005
                
                def progress_callback(progress, text):
                    self.gen_progress_var.set(progress)
                    self.gen_status_var.set(f"🧠 {text}")
                    self.root.update()
                
                # Analyse mit f0-Hinweis wenn Vorhersage aktiv
                f0_hint = f0 if use_prediction else None
                
                analysis = self.xi_fft.analyze(
                    self.current_signal,
                    freq_range=(20, 2000),
                    progress_callback=progress_callback,
                    f0_hint=f0_hint
                )
                
                self.current_analysis = analysis
                
                # UI-Update im Hauptthread
                self.root.after(0, lambda: self.display_analysis_results(analysis, "generator"))
                
            except Exception as e:
                self.root.after(0, lambda: self.handle_analysis_error(str(e), "generator"))
        
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
            try:
                # Konvertiere zu int16
                signal_int = (self.current_signal * 32767).astype(np.int16)
                
                with wave.open(filename, 'w') as wav_file:
                    wav_file.setnchannels(1)
                    wav_file.setsampwidth(2)
                    wav_file.setframerate(44100)
                    wav_file.writeframes(signal_int.tobytes())
                
                self.gen_status_var.set(f"💾 WAV gespeichert: {os.path.basename(filename)}")
                messagebox.showinfo("Erfolg", f"Signal gespeichert als:\n{filename}")
                
            except Exception as e:
                messagebox.showerror("Fehler", f"WAV-Export fehlgeschlagen:\n{str(e)}")
    
    # ===== FILE ANALYSIS FUNCTIONS =====
    def toggle_f0_hint(self):
        """Toggle f0-Hinweis"""
        enabled = self.use_f0_hint.get()
        state = "normal" if enabled else "disabled"
        self.f0_hint_spinbox.configure(state=state)
    
    def load_wav_file(self):
        """Lade WAV-Datei"""
        filename = filedialog.askopenfilename(
            filetypes=[("WAV files", "*.wav"), ("All files", "*.*")],
            title="WAV-Datei für Harmonien-Analyse auswählen"
        )
        
        if filename:
            try:
                self.file_status_var.set("📁 Lade Datei...")
                self.root.update()
                
                # Lade WAV
                with wave.open(filename, 'r') as wav_file:
                    frames = wav_file.readframes(-1)
                    sample_rate = wav_file.getframerate()
                    channels = wav_file.getnchannels()
                    
                    if wav_file.getsampwidth() == 2:
                        signal = np.frombuffer(frames, dtype=np.int16).astype(np.float32)
                        signal = signal / 32767.0
                    else:
                        signal = np.frombuffer(frames, dtype=np.int8).astype(np.float32)
                        signal = signal / 127.0
                    
                    if channels == 2:
                        signal = signal[::2]  # Nur linker Kanal
                
                self.loaded_signal = signal
                self.loaded_sample_rate = sample_rate
                
                duration = len(signal) / sample_rate
                size_mb = len(signal) * 4 / (1024 * 1024)
                
                self.file_info_var.set(f"📄 {os.path.basename(filename)} ({duration:.1f}s, {sample_rate}Hz, {size_mb:.1f}MB)")
                self.file_status_var.set("✅ Datei geladen - Bereit für Harmonien-Analyse")
                
                self.status_var.set(f"📁 WAV geladen - {duration:.1f}s Audio")
                
                # Zeige Waveform
                self.notebook.select(3)
                self.plot_waveform(signal, sample_rate)
                
            except Exception as e:
                self.file_status_var.set(f"❌ Fehler: {str(e)}")
                messagebox.showerror("Fehler", f"Datei-Laden fehlgeschlagen:\n{str(e)}")
    
    def analyze_file_with_harmonics(self):
        """Analysiere Datei mit Harmonien-Konfiguration"""
        if self.loaded_signal is None:
            messagebox.showwarning("Warnung", "Erst WAV-Datei laden!")
            return
        
        def analyze_thread():
            try:
                # Konfiguriere Analyzer
                self.xi_fft.sample_rate = self.loaded_sample_rate
                self.xi_fft.threshold = self.threshold_var.get()
                
                # Parameter
                freq_range = (self.min_freq_var.get(), self.max_freq_var.get())
                f0_hint = self.f0_hint_var.get() if self.use_f0_hint.get() else None
                
                def progress_callback(progress, text):
                    self.file_progress_var.set(progress)
                    self.file_status_var.set(f"🎼 {text}")
                    self.root.update()
                
                # Analysiere nur erste 3 Sekunden für Performance
                max_samples = min(len(self.loaded_signal), self.loaded_sample_rate * 3)
                signal_segment = self.loaded_signal[:max_samples]
                
                analysis = self.xi_fft.analyze(
                    signal_segment,
                    freq_range=freq_range,
                    progress_callback=progress_callback,
                    f0_hint=f0_hint
                )
                
                self.current_analysis = analysis
                
                # UI-Update
                self.root.after(0, lambda: self.display_analysis_results(analysis, "file"))
                
            except Exception as e:
                self.root.after(0, lambda: self.handle_analysis_error(str(e), "file"))
        
        threading.Thread(target=analyze_thread, daemon=True).start()
    
    def quick_analyze_file(self):
        """Schnelle Datei-Analyse mit Minimal-Harmonien"""
        # Temporär auf Minimal-Preset setzen
        original_preset = self.harmonic_config.current_preset
        self.harmonic_config.set_preset('minimal')
        
        # Starte Analyse
        self.analyze_file_with_harmonics()
        
        # Stelle ursprüngliches Preset wieder her
        self.harmonic_config.set_preset(original_preset)
    
    # ===== RESULTS & PLOTTING FUNCTIONS =====
    def display_analysis_results(self, analysis, source):
        """Zeige Analyse-Ergebnisse"""
        try:
            # Update Harmonische Metriken
            harmonic_metrics = analysis.get('harmonicMetrics', {})
            
            self.total_peaks_var.set(f"Total: {harmonic_metrics.get('total_peaks', 0)}")
            self.harmonic_peaks_var.set(f"Harmonisch: {harmonic_metrics.get('harmonic_matches', 0)}")
            
            harmonic_ratio = harmonic_metrics.get('harmonic_ratio', 0)
            self.harmonic_ratio_var.set(f"{harmonic_ratio:.1%}")
            self.quality_var.set(harmonic_metrics.get('quality', 'Unbekannt'))
            
            config_efficiency = harmonic_metrics.get('config_efficiency', 0)
            self.config_efficiency_var.set(f"{config_efficiency:.2f}")
            
            active_count = len(self.harmonic_config.active_harmonics)
            self.active_harmonics_var.set(f"{active_count} aktiv")
            
            # Performance-Metriken
            perf_metrics = analysis.get('performanceMetrics', {})
            analysis_time = perf_metrics.get('totalTime', 0)
            efficiency = perf_metrics.get('efficiency', 0)
            
            self.analysis_time_var.set(f"{analysis_time:.2f}s")
            self.efficiency_var.set(f"{efficiency:.2f}")
            
            # Plots
            if source == "generator" and self.current_signal is not None:
                self.plot_analysis_results(analysis, self.current_signal, 44100)
            elif source == "file" and self.loaded_signal is not None:
                max_samples = min(len(self.loaded_signal), self.loaded_sample_rate * 3)
                segment = self.loaded_signal[:max_samples]
                self.plot_analysis_results(analysis, segment, self.loaded_sample_rate)
            
            # Text-Ergebnisse
            self.display_text_results(analysis, source)
            
            # Status-Updates
            peak_count = analysis['peakCount']
            if source == "generator":
                self.gen_status_var.set(f"✅ Harmonien-Analyse: {peak_count} Peaks in {analysis_time:.2f}s")
                self.gen_progress_var.set(100)
            else:
                self.file_status_var.set(f"✅ Harmonien-Analyse: {peak_count} Peaks in {analysis_time:.2f}s")
                self.file_progress_var.set(100)
            
            self.status_var.set(f"📊 Analyse komplett - {harmonic_metrics.get('harmonic_matches', 0)} harmonische Treffer")
            
            # Wechsle zu Results-Tab
            self.notebook.select(3)
            
        except Exception as e:
            print(f"❌ Display Error: {e}")
            messagebox.showerror("Fehler", f"Ergebnisse-Anzeige fehlgeschlagen:\n{str(e)}")
    
    def plot_analysis_results(self, analysis, signal, sample_rate):
        """Plotte Analyse-Ergebnisse"""
        # Waveform
        self.plot_waveform(signal, sample_rate)
        
        # Spektrum mit Harmonien-Markierung
        self.plot_harmonic_spectrum(analysis)
        
        # Harmonische Analyse
        self.plot_harmonic_analysis(analysis)
        
        # Konfiguration-Effizienz
        self.plot_configuration_efficiency(analysis)
        
        self.canvas.draw()
    
    def plot_waveform(self, signal, sample_rate):
        """Plotte Waveform"""
        self.ax_waveform.clear()
        self.ax_waveform.set_title('Zeitverlauf', fontsize=10)
        
        # Downsampling für Performance
        if len(signal) > 2000:
            step = len(signal) // 2000
            plot_signal = signal[::step]
        else:
            plot_signal = signal
        
        t = np.linspace(0, len(signal)/sample_rate, len(plot_signal))
        self.ax_waveform.plot(t, plot_signal, 'b-', linewidth=0.8)
        self.ax_waveform.set_xlabel('Zeit (s)', fontsize=8)
        self.ax_waveform.set_ylabel('Amplitude', fontsize=8)
        self.ax_waveform.grid(True, alpha=0.3)
        self.ax_waveform.tick_params(labelsize=8)
    
    def plot_harmonic_spectrum(self, analysis):
        """Plotte Spektrum mit Harmonien-Markierung"""
        self.ax_spectrum.clear()
        self.ax_spectrum.set_title('Harmonisches Spektrum', fontsize=10)
        
        peaks = analysis['peaks'][:15]  # Top 15
        if not peaks:
            self.ax_spectrum.text(0.5, 0.5, 'Keine Peaks', ha='center', va='center', 
                                 transform=self.ax_spectrum.transAxes)
            return
        
        frequencies = [p['frequency'] for p in peaks]
        magnitudes = [p['magnitude'] for p in peaks]
        
        # Farben basierend auf Harmonien-Kategorie
        colors = []
        for peak in peaks:
            if peak.get('is_harmonic_match', False):
                category = peak.get('harmonic_category', 'Unknown')
                if category == 'Perfect':
                    colors.append('red')
                elif category == 'Consonant':
                    colors.append('orange')
                elif category == 'Dissonant':
                    colors.append('yellow')
                elif category in ['Complex', 'Microtone', 'Beating']:
                    colors.append('purple')
                else:
                    colors.append('green')
            else:
                colors.append('lightgray')
        
        bars = self.ax_spectrum.bar(frequencies, magnitudes, color=colors, alpha=0.8)
        
        # Labels für Top 5
        for i, (freq, mag, peak) in enumerate(zip(frequencies[:5], magnitudes[:5], peaks[:5])):
            name = peak.get('harmonic_name', 'Unknown')
            if len(name) > 10:
                name = name[:10] + "..."
            
            self.ax_spectrum.text(freq, mag + max(magnitudes)*0.05, 
                                f'{freq:.1f}Hz\n{name}', 
                                ha='center', va='bottom', fontsize=7)
        
        self.ax_spectrum.set_xlabel('Frequenz (Hz)', fontsize=8)
        self.ax_spectrum.set_ylabel('Magnitude', fontsize=8)
        self.ax_spectrum.grid(True, alpha=0.3)
        self.ax_spectrum.tick_params(labelsize=8)
    
    def plot_harmonic_analysis(self, analysis):
        """Plotte Harmonische Analyse"""
        self.ax_harmonics.clear()
        self.ax_harmonics.set_title('Harmonische Verteilung', fontsize=10)
        
        harmonic_metrics = analysis.get('harmonicMetrics', {})
        category_dist = harmonic_metrics.get('category_distribution', {})
        
        if not category_dist:
            self.ax_harmonics.text(0.5, 0.5, 'Keine harmonischen\nDaten verfügbar', 
                                  ha='center', va='center', transform=self.ax_harmonics.transAxes)
            return
        
        categories = list(category_dist.keys())
        counts = list(category_dist.values())
        
        # Farben für Kategorien
        category_colors = {
            'Perfect': 'red',
            'Consonant': 'orange', 
            'Dissonant': 'yellow',
            'Complex': 'purple',
            'Microtone': 'cyan',
            'Beating': 'magenta',
            'Non-harmonic': 'lightgray',
            'Supplementary': 'gray'
        }
        
        colors = [category_colors.get(cat, 'blue') for cat in categories]
        
        # Pie Chart
        wedges, texts, autotexts = self.ax_harmonics.pie(counts, labels=categories, colors=colors, 
                                                        autopct='%1.0f', startangle=90)
        
        # Schrift-Größe anpassen
        for text in texts:
            text.set_fontsize(8)
        for autotext in autotexts:
            autotext.set_fontsize(8)
    
    def plot_configuration_efficiency(self, analysis):
        """Plotte Konfiguration-Effizienz"""
        self.ax_config.clear()
        self.ax_config.set_title('Konfiguration-Effizienz', fontsize=10)
        
        harmonic_metrics = analysis.get('harmonicMetrics', {})
        config_info = analysis.get('harmonicConfig', {})
        
        # Balken-Diagramm für Effizienz-Metriken
        metrics = [
            'Harmonien-Treffer',
            'Aktive Harmonien', 
            'Konfiguration-Effizienz',
            'Gesamt-Qualität'
        ]
        
        values = [
            harmonic_metrics.get('harmonic_matches', 0),
            config_info.get('activeHarmonics', 0),
            harmonic_metrics.get('config_efficiency', 0) * 10,  # Skaliert für Darstellung
            harmonic_metrics.get('harmonic_ratio', 0) * 100   # Prozent
        ]
        
        colors = ['green', 'blue', 'orange', 'red']
        bars = self.ax_config.bar(range(len(metrics)), values, color=colors, alpha=0.7)
        
        # Werte auf Balken
        for i, (bar, value) in enumerate(zip(bars, values)):
            height = bar.get_height()
            if i == 2:  # Konfiguration-Effizienz zurück-skalieren
                display_value = f'{value/10:.2f}'
            elif i == 3:  # Qualität als Prozent
                display_value = f'{value:.0f}%'
            else:
                display_value = f'{value:.0f}'
                
            self.ax_config.text(bar.get_x() + bar.get_width()/2, height + max(values)*0.01,
                               display_value, ha='center', va='bottom', fontsize=8)
        
        self.ax_config.set_xticks(range(len(metrics)))
        self.ax_config.set_xticklabels(metrics, rotation=45, ha='right', fontsize=8)
        self.ax_config.set_ylabel('Wert', fontsize=8)
        self.ax_config.tick_params(labelsize=8)
        self.ax_config.grid(True, alpha=0.3, axis='y')
    
    def display_text_results(self, analysis, source):
        """Zeige detaillierte Text-Ergebnisse"""
        self.results_text.delete(1.0, tk.END)
        
        text = "=== ξ-FFT HARMONISCHEN-ANALYSE BERICHT ===\n\n"
        
        # Konfiguration-Info
        config_info = analysis.get('harmonicConfig', {})
        text += f"🎼 HARMONISCHE KONFIGURATION:\n"
        text += f"   Preset: {config_info.get('preset', 'Unbekannt')}\n"
        text += f"   Aktive Harmonien: {config_info.get('activeHarmonics', 0)}/{config_info.get('totalHarmonics', 0)}\n"
        text += f"   Max. Phasen: {config_info.get('maxPhases', 0)}\n\n"
        
        # Performance-Metriken
        perf_metrics = analysis.get('performanceMetrics', {})
        text += f"⚡ PERFORMANCE-METRIKEN:\n"
        text += f"   Analysezeit: {perf_metrics.get('totalTime', 0):.3f}s\n"
        text += f"   Peaks/Sekunde: {perf_metrics.get('peaksPerSecond', 0):.1f}\n"
        text += f"   Getestete Harmonien: {perf_metrics.get('harmonicsTestedCount', 0)}\n"
        text += f"   Effizienz: {perf_metrics.get('efficiency', 0):.2f}\n\n"
        
        # Harmonische Metriken
        harmonic_metrics = analysis.get('harmonicMetrics', {})
        text += f"🎯 HARMONISCHE METRIKEN:\n"
        text += f"   Gesamt-Peaks: {harmonic_metrics.get('total_peaks', 0)}\n"
        text += f"   Harmonische Treffer: {harmonic_metrics.get('harmonic_matches', 0)}\n"
        text += f"   Harmonische Ratio: {harmonic_metrics.get('harmonic_ratio', 0):.1%}\n"
        text += f"   Qualität: {harmonic_metrics.get('quality', 'Unbekannt')}\n"
        text += f"   Konfiguration-Effizienz: {harmonic_metrics.get('config_efficiency', 0):.2f}\n\n"
        
        # Top Harmonische Peaks
        peaks = analysis.get('peaks', [])
        harmonic_peaks = [p for p in peaks if p.get('is_harmonic_match', False)]
        
        if harmonic_peaks:
            text += f"🎵 TOP HARMONISCHE PEAKS:\n"
            text += "-" * 60 + "\n"
            
            for i, peak in enumerate(harmonic_peaks[:10], 1):
                freq = peak['frequency']
                mag = peak['magnitude']
                name = peak.get('harmonic_name', 'Unknown')
                category = peak.get('harmonic_category', 'Unknown')
                phase = peak.get('phase', '?')
                
                # Kategorie-Symbol
                cat_symbol = {'Perfect': '🔴', 'Consonant': '🟠', 'Dissonant': '🟡', 
                             'Complex': '🟣', 'Microtone': '🔵', 'Beating': '🟢'}.get(category, '⚫')
                
                text += f"{i:2}. {cat_symbol} {freq:7.2f} Hz → {mag:6.3f} [{name}] (Phase {phase})\n"
        
        # ξ-Verhältnisse mit Harmonien-Bewertung
        xi_ratios = analysis.get('xiRatios', [])
        if xi_ratios:
            text += f"\n🔗 TOP ξ-VERHÄLTNISSE (Harmonische Qualität):\n"
            text += "-" * 60 + "\n"
            
            for i, ratio in enumerate(xi_ratios[:8], 1):
                xi_val = ratio['xiRatio']
                interval_name = ratio.get('intervalName', 'Unknown')
                harmonic_quality = ratio.get('harmonicQuality', {})
                quality_score = harmonic_quality.get('score', 0)
                
                # Qualitäts-Bewertung
                if quality_score >= 15:
                    quality_indicator = "🏆 Exzellent"
                elif quality_score >= 10:
                    quality_indicator = "⭐ Gut"
                elif quality_score >= 5:
                    quality_indicator = "✅ Mittel"
                else:
                    quality_indicator = "⚠️ Niedrig"
                
                text += f"{i}. ξ({ratio['freqHigh']:6.2f}/{ratio['freqLow']:6.2f}) = {xi_val:6.3f}\n"
                text += f"    [{interval_name}] {quality_indicator} (Score: {quality_score})\n"
        
        # Harmonische Empfehlungen
        text += f"\n💡 HARMONISCHE EMPFEHLUNGEN:\n"
        text += "-" * 40 + "\n"
        
        harmonic_ratio = harmonic_metrics.get('harmonic_ratio', 0)
        if harmonic_ratio > 0.8:
            text += "✅ Exzellente harmonische Struktur erkannt!\n"
            text += "   Konfiguration ist optimal für dieses Signal.\n"
        elif harmonic_ratio > 0.5:
            text += "👍 Gute harmonische Struktur erkannt.\n"
            text += "   Erwägen Sie erweiterte Harmonien für bessere Abdeckung.\n"
        else:
            text += "⚠️ Wenige harmonische Strukturen erkannt.\n"
            text += "   Empfehlungen:\n"
            text += "   • Probieren Sie das 'Complete' Preset\n"
            text += "   • Verwenden Sie f₀-Hinweis falls bekannt\n"
            text += "   • Prüfen Sie Threshold-Einstellung\n"
        
        # Konfiguration-Empfehlungen
        config_efficiency = harmonic_metrics.get('config_efficiency', 0)
        if config_efficiency < 0.3:
            text += "   • Zu viele Harmonien aktiviert - probieren Sie 'Standard' Preset\n"
        elif config_efficiency > 0.8:
            text += "   • Sehr effiziente Konfiguration - perfekt abgestimmt!\n"
        
        self.results_text.insert(tk.END, text)
    
    def handle_analysis_error(self, error_msg, source):
        """Handle Analyse-Fehler"""
        if source == "generator":
            self.gen_status_var.set(f"❌ Harmonien-Analyse fehlgeschlagen")
            self.gen_progress_var.set(0)
        else:
            self.file_status_var.set(f"❌ Harmonien-Analyse fehlgeschlagen")
            self.file_progress_var.set(0)
        
        self.status_var.set("❌ Analyse-Fehler aufgetreten")
        messagebox.showerror("Harmonien-Analyse Fehler", f"Analyse fehlgeschlagen:\n{error_msg}")

# ===== MAIN FUNCTION =====
def main():
    """Hauptfunktion für ξ-FFT mit Harmonischen-Auswahl"""
    
    print("🎼 ξ-FFT mit Harmonischen-Auswahl v2.1")
    print("=" * 60)
    print("🎵 Neue Features:")
    print("   • Konfigurierbare Harmonische Auswahl")
    print("   • 7 Harmonien-Presets (Minimal bis Komplett)")
    print("   • Kategorien-basierte Harmonien-Filter")
    print("   • Performance-Optimierung durch selektive Analyse")
    print("   • Individuelle Harmonien-Aktivierung")
    print("   • Erweiterte Harmonische Metriken")
    print("   • Echtzeit Konfiguration-Effizienz")
    print("=" * 60)
    
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
        # Erstelle App
        app = HarmonicSelectionXiFFTApp(root)
        
        print("✅ GUI mit Harmonischen-Auswahl bereit")
        print("\n🎼 HARMONISCHE FEATURES:")
        print("• 24 konfigurierbare Harmonien")
        print("• Intelligente Preset-Auswahl")
        print("• Phase-basierte Analyse-Strategien")
        print("• Echtzeit Performance-Schätzung")
        print("• Erweiterte Harmonische Metriken")
        print("• Adaptive Threshold-Strategien")
        
        # GUI starten
        root.mainloop()
        
    except Exception as e:
        print(f"💥 Kritischer Fehler: {e}")
        messagebox.showerror("Kritischer Fehler", f"Anwendung kann nicht gestartet werden:\n{str(e)}")
        sys.exit(1)
    
    print("👋 ξ-FFT mit Harmonischen-Auswahl beendet")
    print("🎼 Konfigurierbare Harmonien waren aktiv")

if __name__ == "__main__":
    main()