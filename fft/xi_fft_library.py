"""
ξ-FFT: Spektralanalyse durch Frequenz-Verhältnisse
Einfache, robuste Alternative zur traditionellen FFT-Analyse

Verwendung:
    from xi_fft import XiFFT, XiAnomalyDetector, XiStreamProcessor
    
    # Einfache Analyse
    xi_fft = XiFFT(sample_rate=1000)
    result = xi_fft.analyze(signal)
    print(f"Dominantes ξ: {result['dominant_xi']['xi_ratio']}")
"""

import math
from typing import List, Dict, Tuple, Optional

class XiFFT:
    """Hauptklasse für ξ-FFT Analyse"""
    
    def __init__(self, sample_rate: int, threshold: float = 0.05):
        """
        Initialisiere ξ-FFT Analyzer
        
        Args:
            sample_rate: Abtastrate in Hz
            threshold: Minimum-Amplitude für Peak-Erkennung
        """
        self.sample_rate = sample_rate
        self.threshold = threshold
        self.peaks = []
        self.xi_ratios = []
    
    def analyze(self, signal: List[float], freq_range: Tuple[int, int] = (10, 500)) -> Dict:
        """
        Analysiere Signal und berechne ξ-Verhältnisse
        
        Args:
            signal: Eingangssignal als Liste
            freq_range: Frequenzbereich (min_freq, max_freq)
            
        Returns:
            Dict mit peaks, xi_ratios, dominant_xi, etc.
        """
        self.peaks = self._find_spectral_peaks(signal, freq_range)
        self.xi_ratios = self._calculate_xi_ratios(self.peaks)
        
        return {
            'peaks': self.peaks,
            'xi_ratios': self.xi_ratios,
            'dominant_xi': self.xi_ratios[0] if self.xi_ratios else None,
            'peak_count': len(self.peaks),
            'complexity': len(self.xi_ratios)
        }
    
    def _find_spectral_peaks(self, signal: List[float], freq_range: Tuple[int, int]) -> List[Dict]:
        """Finde spektrale Peaks mittels DFT"""
        peaks = []
        min_freq, max_freq = freq_range
        step_size = max(1, (max_freq - min_freq) // 100)
        
        for freq in range(min_freq, max_freq + 1, step_size):
            magnitude = self._calculate_magnitude(signal, freq)
            
            if magnitude > self.threshold:
                peaks.append({
                    'frequency': freq,
                    'magnitude': round(magnitude, 4)
                })
        
        return sorted(peaks, key=lambda x: x['magnitude'], reverse=True)
    
    def _calculate_magnitude(self, signal: List[float], frequency: float) -> float:
        """DFT für spezifische Frequenz"""
        N = len(signal)
        real = imag = 0.0
        
        for n in range(N):
            angle = -2 * math.pi * frequency * n / self.sample_rate
            real += signal[n] * math.cos(angle)
            imag += signal[n] * math.sin(angle)
        
        return math.sqrt(real * real + imag * imag) * 2 / N
    
    def _calculate_xi_ratios(self, peaks: List[Dict]) -> List[Dict]:
        """Berechne alle ξ-Verhältnisse zwischen Peaks"""
        ratios = []
        
        for i in range(len(peaks)):
            for j in range(i + 1, len(peaks)):
                f1, f2 = peaks[i]['frequency'], peaks[j]['frequency']
                xi = max(f1, f2) / min(f1, f2)
                
                ratios.append({
                    'freq_high': max(f1, f2),
                    'freq_low': min(f1, f2),
                    'xi_ratio': round(xi, 3),
                    'significance': round(peaks[i]['magnitude'] * peaks[j]['magnitude'], 6)
                })
        
        return sorted(ratios, key=lambda x: x['significance'], reverse=True)

class XiAnomalyDetector:
    """Anomalie-Erkennung basierend auf ξ-Verhältnissen"""
    
    def __init__(self, expected_ratios: List[Dict], tolerance: float = 0.2):
        """
        Initialisiere Anomalie-Detektor
        
        Args:
            expected_ratios: Liste erwarteter ξ-Verhältnisse 
                           [{'name': 'Motor/Lager', 'value': 2.5}, ...]
            tolerance: Toleranz für Abweichungen
        """
        self.expected_ratios = expected_ratios
        self.tolerance = tolerance
    
    def detect(self, xi_ratios: List[Dict]) -> Dict:
        """
        Erkenne Abweichungen von erwarteten ξ-Verhältnissen
        
        Args:
            xi_ratios: Berechnete ξ-Verhältnisse aus XiFFT.analyze()
            
        Returns:
            Dict mit anomalies, matches, health_score
        """
        anomalies = []
        matches = []
        
        for expected in self.expected_ratios:
            best_match = None
            min_deviation = float('inf')
            
            for actual in xi_ratios:
                deviation = abs(actual['xi_ratio'] - expected['value'])
                if deviation < min_deviation:
                    min_deviation = deviation
                    best_match = actual
            
            if min_deviation < self.tolerance:
                matches.append({
                    'expected': expected,
                    'actual': best_match,
                    'deviation': round(min_deviation, 3),
                    'status': 'normal'
                })
            else:
                anomalies.append({
                    'expected': expected,
                    'deviation': round(min_deviation, 3),
                    'status': 'anomaly'
                })
        
        return {
            'anomalies': anomalies,
            'matches': matches,
            'anomaly_count': len(anomalies),
            'health_score': len(matches) / len(self.expected_ratios) if self.expected_ratios else 0
        }

class XiStreamProcessor:
    """Echtzeit-Verarbeitung von Datenströmen"""
    
    def __init__(self, sample_rate: int, buffer_size: int = 1024):
        """
        Initialisiere Stream-Processor
        
        Args:
            sample_rate: Abtastrate in Hz
            buffer_size: Größe des Analyse-Buffers
        """
        self.sample_rate = sample_rate
        self.buffer_size = buffer_size
        self.buffer = []
        self.xi_fft = XiFFT(sample_rate)
        self.history = []
    
    def process_sample(self, sample: float) -> Optional[Dict]:
        """
        Füge Sample hinzu und analysiere bei vollem Buffer
        
        Args:
            sample: Einzelner Messwert
            
        Returns:
            Analyse-Ergebnis wenn Buffer voll, sonst None
        """
        self.buffer.append(sample)
        
        if len(self.buffer) >= self.buffer_size:
            result = self.xi_fft.analyze(self.buffer)
            
            self.history.append(result)
            if len(self.history) > 100:
                self.history.pop(0)
            
            # Overlap für kontinuierliche Analyse
            overlap = self.buffer_size // 4
            self.buffer = self.buffer[-overlap:]
            
            return result
        
        return None
    
    def get_trend_analysis(self) -> Dict:
        """Analysiere Trends der ξ-Verhältnisse"""
        if len(self.history) < 5:
            return {'status': 'insufficient_data'}
        
        recent_xi = []
        for h in self.history[-10:]:
            if h['dominant_xi']:
                recent_xi.append(h['dominant_xi']['xi_ratio'])
        
        if not recent_xi:
            return {'status': 'no_dominant_xi'}
        
        mean_xi = sum(recent_xi) / len(recent_xi)
        variance = sum((x - mean_xi) ** 2 for x in recent_xi) / len(recent_xi)
        std_xi = math.sqrt(variance)
        
        return {
            'mean_xi': round(mean_xi, 3),
            'std_xi': round(std_xi, 3),
            'trend': 'stable' if std_xi < 0.1 else 'unstable',
            'latest_xi': recent_xi[-1],
            'sample_count': len(recent_xi)
        }

# Hilfsfunktionen
def create_test_signal(freqs: List[float], amplitudes: List[float], 
                      duration: float = 2.0, sample_rate: int = 1000) -> List[float]:
    """
    Erstelle Testsignal mit gegebenen Frequenzen
    
    Args:
        freqs: Liste der Frequenzen in Hz
        amplitudes: Liste der Amplituden
        duration: Signallänge in Sekunden
        sample_rate: Abtastrate in Hz
        
    Returns:
        Signal als Liste
    """
    if len(freqs) != len(amplitudes):
        raise ValueError("Frequenzen und Amplituden müssen gleiche Länge haben")
    
    n_samples = int(duration * sample_rate)
    signal = [0.0] * n_samples
    
    for i in range(n_samples):
        t = i / sample_rate
        for freq, amp in zip(freqs, amplitudes):
            signal[i] += amp * math.sin(2 * math.pi * freq * t)
    
    return signal

def quick_analysis(signal: List[float], sample_rate: int, 
                  freq_range: Tuple[int, int] = (10, 500)) -> None:
    """
    Schnelle Analyse mit Konsolen-Ausgabe
    
    Args:
        signal: Eingangssignal
        sample_rate: Abtastrate in Hz
        freq_range: Frequenzbereich (min, max)
    """
    xi_fft = XiFFT(sample_rate)
    result = xi_fft.analyze(signal, freq_range)
    
    print("=== ξ-FFT Analyse ===")
    print(f"Peaks gefunden: {result['peak_count']}")
    print(f"ξ-Verhältnisse: {result['complexity']}")
    
    print("\nTop Frequenzen:")
    for i, peak in enumerate(result['peaks'][:5], 1):
        print(f"{i}. {peak['frequency']} Hz: {peak['magnitude']:.3f}")
    
    print("\nTop ξ-Verhältnisse:")
    for i, ratio in enumerate(result['xi_ratios'][:5], 1):
        print(f"{i}. ξ({ratio['freq_high']}/{ratio['freq_low']}) = {ratio['xi_ratio']}")

def machine_monitoring_example():
    """Beispiel für Maschinenüberwachung"""
    
    # Erstelle realistische Maschinenvibration
    # Motor: 60Hz, Lager: 150Hz, Getriebe: 240Hz
    machine_signal = create_test_signal(
        freqs=[60, 150, 240],
        amplitudes=[1.0, 0.4, 0.2],
        duration=2.0,
        sample_rate=1000
    )
    
    # Füge leichtes Rauschen hinzu
    import random
    for i in range(len(machine_signal)):
        machine_signal[i] += random.uniform(-0.02, 0.02)
    
    # Definiere erwartete ξ-Verhältnisse für gesunde Maschine
    expected_ratios = [
        {'name': 'Lager/Motor', 'value': 2.5},      # 150/60 = 2.5
        {'name': 'Getriebe/Motor', 'value': 4.0},   # 240/60 = 4.0
        {'name': 'Getriebe/Lager', 'value': 1.6}    # 240/150 = 1.6
    ]
    
    # Setup
    xi_fft = XiFFT(sample_rate=1000, threshold=0.1)
    detector = XiAnomalyDetector(expected_ratios, tolerance=0.3)
    
    # Analysiere
    result = xi_fft.analyze(machine_signal, freq_range=(10, 300))
    anomaly_report = detector.detect(result['xi_ratios'])
    
    print("=== Maschinenüberwachung ===")
    print(f"Gesundheits-Score: {anomaly_report['health_score']:.2f}")
    print(f"Anomalien gefunden: {anomaly_report['anomaly_count']}")
    
    print("\nMatches:")
    for match in anomaly_report['matches']:
        print(f"✅ {match['expected']['name']}: "
              f"Erwartet {match['expected']['value']:.1f}, "
              f"Gefunden {match['actual']['xi_ratio']:.2f}")
    
    if anomaly_report['anomalies']:
        print("\nAnomalien:")
        for anomaly in anomaly_report['anomalies']:
            print(f"❌ {anomaly['expected']['name']}: "
                  f"Abweichung {anomaly['deviation']:.2f}")

def realtime_monitoring_example():
    """Beispiel für Echtzeit-Monitoring"""
    
    # Setup Stream-Processor
    stream_processor = XiStreamProcessor(sample_rate=1000, buffer_size=512)
    
    # Simuliere kontinuierlichen Datenstrom
    print("=== Echtzeit-Monitoring ===")
    print("Simuliere Datenstream...")
    
    # Erstelle längeres Signal mit sich ändernden Eigenschaften
    base_signal = create_test_signal([50, 120, 200], [1.0, 0.6, 0.3], 
                                   duration=10.0, sample_rate=1000)
    
    analysis_count = 0
    for i, sample in enumerate(base_signal):
        result = stream_processor.process_sample(sample)
        
        if result:
            analysis_count += 1
            dominant_xi = result['dominant_xi']
            
            if dominant_xi and analysis_count % 5 == 0:  # Jeden 5. Durchgang
                print(f"Segment {analysis_count}: "
                      f"ξ = {dominant_xi['xi_ratio']:.2f} "
                      f"({dominant_xi['freq_high']}/{dominant_xi['freq_low']} Hz)")
            
            # Trend-Analyse alle 10 Segmente
            if analysis_count % 10 == 0:
                trend = stream_processor.get_trend_analysis()
                if trend.get('mean_xi'):
                    print(f"  → Trend: {trend['trend']}, "
                          f"Mean ξ: {trend['mean_xi']:.2f} ± {trend['std_xi']:.2f}")

# Beispiel-Nutzung
if __name__ == "__main__":
    print("ξ-FFT Bibliothek - Demonstrationen\n")
    
    # 1. Einfache Analyse
    print("1. Einfache Signalanalyse:")
    test_signal = create_test_signal([50, 120, 180], [1.0, 0.7, 0.4])
    quick_analysis(test_signal, sample_rate=1000)
    print()
    
    # 2. Maschinenüberwachung
    print("2. Maschinenüberwachung:")
    machine_monitoring_example()
    print()
    
    # 3. Echtzeit-Monitoring
    print("3. Echtzeit-Monitoring:")
    realtime_monitoring_example()
