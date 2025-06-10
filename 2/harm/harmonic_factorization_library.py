"""
Harmonic Factorization Library
==============================

Eine revolutionäre verhältnisbasierte Faktorisierungsbibliothek basierend auf 
musikalischen Harmonien. Entwickelt für systematische Tests und Forschung.

Author: Harmonic Mathematics Research
Version: 1.0.0

Installation:
    Speichere als harmonic_lib.py und importiere:
    
    from harmonic_lib import HarmonicFactorizer, TestSuite, HarmonicAnalyzer

Beispiel-Verwendung:
    
    # Einfache Faktorisierung
    factorizer = HarmonicFactorizer()
    result = factorizer.factorize(221)
    
    # Systematische Tests
    suite = TestSuite()
    suite.run_comprehensive_test()
    
    # Wissenschaftliche Analyse
    analyzer = HarmonicAnalyzer()
    analyzer.analyze_range(1000, 10000)
"""

import time
import random
import math
import statistics
from fractions import Fraction
from typing import Dict, List, Tuple, Optional, Union
from dataclasses import dataclass
from collections import defaultdict
import json

@dataclass
class FactorizationResult:
    """Ergebnis einer Faktorisierung"""
    success: bool
    number: int
    factors: Optional[Tuple[int, int]] = None
    harmonic_name: Optional[str] = None
    ratio: Optional[Fraction] = None
    target_ratio: Optional[Fraction] = None
    exact: bool = False
    deviation_percent: float = 0.0
    time_ms: float = 0.0
    method: str = 'none'

@dataclass
class HarmonicInterval:
    """Harmonisches Intervall"""
    ratio: Fraction
    name: str
    category: str = 'standard'
    
    def __str__(self):
        return f"{self.name} ({self.ratio})"

class HarmonicFactorizer:
    """
    Kernklasse für harmonische Faktorisierung
    
    Verwendet musikalische Verhältnisse zur effizienten Faktorisierung
    zusammengesetzter Zahlen ohne Rundungsfehler.
    """
    
    # Standard harmonische Intervalle
    STANDARD_HARMONICS = [
        HarmonicInterval(Fraction(9, 8), "große Sekunde 9:8", "sekunde"),
        HarmonicInterval(Fraction(6, 5), "kleine Terz 6:5", "terz"),
        HarmonicInterval(Fraction(5, 4), "große Terz 5:4", "terz"),
        HarmonicInterval(Fraction(4, 3), "Quarte 4:3", "quarte"),
        HarmonicInterval(Fraction(3, 2), "Quinte 3:2", "quinte"),
        HarmonicInterval(Fraction(8, 5), "kleine Sexte 8:5", "sexte"),
        HarmonicInterval(Fraction(5, 3), "große Sexte 5:3", "sexte"),
        HarmonicInterval(Fraction(16, 9), "kleine Septime 16:9", "septime"),
        HarmonicInterval(Fraction(15, 8), "große Septime 15:8", "septime")
    ]
    
    # Erweiterte harmonische Verhältnisse für Forschung
    EXTENDED_HARMONICS = [
        HarmonicInterval(Fraction(10, 9), "kleine Sekunde 10:9", "sekunde"),
        HarmonicInterval(Fraction(7, 6), "natürliche kleine Terz 7:6", "terz"),
        HarmonicInterval(Fraction(9, 7), "natürliche große Terz 9:7", "terz"),
        HarmonicInterval(Fraction(11, 8), "übermäßige Quarte 11:8", "tritonus"),
        HarmonicInterval(Fraction(16, 11), "verminderte Quinte 16:11", "tritonus"),
        HarmonicInterval(Fraction(7, 4), "natürliche kleine Septime 7:4", "septime"),
        HarmonicInterval(Fraction(17, 16), "17. Oberton 17:16", "mikrotonal"),
        HarmonicInterval(Fraction(19, 16), "19. Oberton 19:16", "mikrotonal")
    ]
    
    def __init__(self, tolerance_percent: float = 5.0, use_extended: bool = False):
        """
        Initialisierung des Faktorizierers
        
        Args:
            tolerance_percent: Toleranz in Prozent für "nahe" harmonische Verhältnisse
            use_extended: Verwende erweiterte harmonische Verhältnisse
        """
        self.tolerance = Fraction(int(tolerance_percent * 100), 10000)
        self.harmonics = self.STANDARD_HARMONICS.copy()
        
        if use_extended:
            self.harmonics.extend(self.EXTENDED_HARMONICS)
        
        # Statistiken
        self.stats = {
            'total_factorizations': 0,
            'successful_factorizations': 0,
            'exact_matches': 0,
            'total_time_ms': 0.0,
            'harmonic_distribution': defaultdict(int)
        }
    
    def factorize(self, n: int, verbose: bool = False) -> FactorizationResult:
        """
        Hauptmethode: Faktorisierung einer Zahl n
        
        Args:
            n: Zu faktorisierende Zahl
            verbose: Detaillierte Ausgabe
            
        Returns:
            FactorizationResult mit allen Details
        """
        start_time = time.perf_counter()
        self.stats['total_factorizations'] += 1
        
        if verbose:
            print(f"\n🎵 Harmonische Faktorisierung von {n:,}")
            print("=" * 50)
        
        # 1. Teste exakte harmonische Verhältnisse
        exact_result = self._test_exact_harmonics(n, verbose)
        if exact_result:
            end_time = time.perf_counter()
            exact_result.time_ms = (end_time - start_time) * 1000
            exact_result.method = 'exact'
            self._update_stats(exact_result)
            return exact_result
        
        # 2. Teste mit Toleranz
        tolerance_result = self._test_with_tolerance(n, verbose)
        end_time = time.perf_counter()
        
        if tolerance_result:
            tolerance_result.time_ms = (end_time - start_time) * 1000
            tolerance_result.method = 'tolerance'
            self._update_stats(tolerance_result)
            return tolerance_result
        
        # 3. Keine harmonischen Faktoren gefunden
        result = FactorizationResult(
            success=False,
            number=n,
            time_ms=(end_time - start_time) * 1000,
            method='none'
        )
        
        if verbose:
            print("❌ Keine harmonischen Faktoren gefunden")
        
        return result
    
    def _test_exact_harmonics(self, n: int, verbose: bool) -> Optional[FactorizationResult]:
        """Teste exakte harmonische Verhältnisse"""
        
        for harmonic in self.harmonics:
            ratio = harmonic.ratio
            
            if verbose:
                print(f"\nTeste {harmonic}:")
            
            # Exakte Bruchrechnung: n = a * b, wobei a:b = ratio
            one_plus_ratio = ratio + 1
            
            numerator_a = n * ratio.numerator * one_plus_ratio.denominator
            denominator_a = ratio.denominator * one_plus_ratio.numerator
            
            numerator_b = n * one_plus_ratio.denominator  
            denominator_b = one_plus_ratio.numerator
            
            if (numerator_a % denominator_a == 0 and 
                numerator_b % denominator_b == 0):
                
                a = numerator_a // denominator_a
                b = numerator_b // denominator_b
                
                if a > 1 and b > 1 and a * b == n:
                    actual_ratio = Fraction(max(a, b), min(a, b))
                    
                    if verbose:
                        print(f"  ✅ EXAKT: {a} × {b} = {n}")
                        print(f"  🎯 Verhältnis: {max(a,b)}:{min(a,b)} = {actual_ratio}")
                    
                    return FactorizationResult(
                        success=True,
                        number=n,
                        factors=(a, b),
                        harmonic_name=harmonic.name,
                        ratio=actual_ratio,
                        target_ratio=ratio,
                        exact=True,
                        deviation_percent=0.0
                    )
        
        return None
    
    def _test_with_tolerance(self, n: int, verbose: bool) -> Optional[FactorizationResult]:
        """Teste mit Toleranz"""
        
        if verbose:
            print(f"\n🔍 Suche mit {float(self.tolerance * 100):.2f}% Toleranz...")
        
        # Performance-Optimierung für große Zahlen
        max_factor = min(int(math.sqrt(n)) + 1, 100000)
        
        for test_a in range(2, max_factor):
            if n % test_a == 0:
                test_b = n // test_a
                test_ratio = Fraction(max(test_a, test_b), min(test_a, test_b))
                
                # Prüfe gegen alle harmonischen Verhältnisse
                for harmonic in self.harmonics:
                    target_ratio = harmonic.ratio
                    
                    if target_ratio > 0:
                        deviation = abs(test_ratio - target_ratio) / target_ratio
                        
                        if deviation <= self.tolerance:
                            deviation_percent = float(deviation * 100)
                            
                            if verbose:
                                print(f"  ✅ NAH: {test_a} × {test_b} = {n}")
                                print(f"  🎼 {harmonic.name} (Abweichung: {deviation_percent:.2f}%)")
                                print(f"  📐 Verhältnis: {test_ratio} ≈ {target_ratio}")
                            
                            return FactorizationResult(
                                success=True,
                                number=n,
                                factors=(test_a, test_b),
                                harmonic_name=harmonic.name,
                                ratio=test_ratio,
                                target_ratio=target_ratio,
                                exact=False,
                                deviation_percent=deviation_percent
                            )
        
        return None
    
    def _update_stats(self, result: FactorizationResult):
        """Aktualisiere interne Statistiken"""
        if result.success:
            self.stats['successful_factorizations'] += 1
            if result.exact:
                self.stats['exact_matches'] += 1
            self.stats['harmonic_distribution'][result.harmonic_name] += 1
        
        self.stats['total_time_ms'] += result.time_ms
    
    def get_statistics(self) -> Dict:
        """Gebe aktuelle Statistiken zurück"""
        total = self.stats['total_factorizations']
        if total == 0:
            return {'error': 'Keine Faktorisierungen durchgeführt'}
        
        return {
            'total_factorizations': total,
            'success_rate': self.stats['successful_factorizations'] / total,
            'exact_rate': self.stats['exact_matches'] / total,
            'average_time_ms': self.stats['total_time_ms'] / total,
            'harmonic_distribution': dict(self.stats['harmonic_distribution']),
            'most_common_harmonic': max(self.stats['harmonic_distribution'].items(), 
                                      key=lambda x: x[1], default=('none', 0))[0]
        }
    
    def reset_statistics(self):
        """Setze Statistiken zurück"""
        self.stats = {
            'total_factorizations': 0,
            'successful_factorizations': 0,
            'exact_matches': 0,
            'total_time_ms': 0.0,
            'harmonic_distribution': defaultdict(int)
        }

class TestSuite:
    """
    Umfassende Testsuite für systematische Evaluierung
    """
    
    def __init__(self, factorizer: Optional[HarmonicFactorizer] = None):
        self.factorizer = factorizer or HarmonicFactorizer()
        self.results = []
    
    def run_range_test(self, start: int, end: int, step: int = 1) -> Dict:
        """
        Teste alle Zahlen in einem Bereich
        
        Args:
            start: Startwert
            end: Endwert
            step: Schrittweite
            
        Returns:
            Zusammenfassung der Ergebnisse
        """
        print(f"🔬 Range Test: {start:,} bis {end:,} (Schritt: {step})")
        print("=" * 60)
        
        results = []
        start_time = time.perf_counter()
        
        for n in range(start, end + 1, step):
            # Nur zusammengesetzte Zahlen testen
            if self._is_composite(n):
                result = self.factorizer.factorize(n)
                results.append(result)
                
                if result.success:
                    print(f"{n:>8,}: {result.factors[0]} × {result.factors[1]} "
                          f"({result.harmonic_name}) [{result.time_ms:.2f}ms]")
        
        end_time = time.perf_counter()
        
        return self._analyze_results(results, end_time - start_time)
    
    def run_prime_product_test(self, count: int = 100, max_prime: int = 1000) -> Dict:
        """
        Teste Produkte von Primzahlen
        
        Args:
            count: Anzahl zu testender Zahlen
            max_prime: Maximale Primzahl
            
        Returns:
            Zusammenfassung der Ergebnisse
        """
        print(f"🔬 Prime Product Test: {count} Zahlen, Primzahlen bis {max_prime:,}")
        print("=" * 60)
        
        primes = self._generate_primes(max_prime)
        results = []
        
        for _ in range(count):
            p1, p2 = random.sample(primes, 2)
            n = p1 * p2
            
            result = self.factorizer.factorize(n)
            results.append(result)
            
            if result.success:
                print(f"{n:>8,}: {p1} × {p2} "
                      f"({result.harmonic_name}, {result.deviation_percent:.2f}%) "
                      f"[{result.time_ms:.2f}ms]")
        
        return self._analyze_results(results)
    
    def run_harmonic_construction_test(self, max_k: int = 10) -> Dict:
        """
        Teste konstruierte harmonische Zahlen
        
        Args:
            max_k: Maximaler Multiplikationsfaktor
            
        Returns:
            Zusammenfassung der Ergebnisse
        """
        print(f"🔬 Harmonic Construction Test: k=1 bis {max_k}")
        print("=" * 60)
        
        results = []
        
        for harmonic in self.factorizer.harmonics:
            ratio = harmonic.ratio
            print(f"\n{harmonic.name}:")
            
            for k in range(1, max_k + 1):
                a = k * ratio.numerator
                b = k * ratio.denominator
                n = a * b
                
                result = self.factorizer.factorize(n)
                results.append(result)
                
                status = "✅ EXAKT" if result.exact else "❌ FEHLER"
                print(f"  k={k}: {n:,} = {a} × {b} → {status}")
        
        return self._analyze_results(results)
    
    def run_performance_benchmark(self, sizes: List[int] = None) -> Dict:
        """
        Performance-Benchmark gegen klassische Faktorisierung
        
        Args:
            sizes: Liste von Zahlengrößen zum Testen
            
        Returns:
            Performance-Vergleich
        """
        if sizes is None:
            sizes = [1000, 10000, 100000, 1000000, 10000000]
        
        print(f"🏁 Performance Benchmark")
        print("=" * 70)
        print(f"{'Größe':<12} {'Harmonisch':<12} {'Klassisch':<12} {'Speedup':<10} {'Erfolgsrate'}")
        print("-" * 70)
        
        benchmark_results = []
        
        for size in sizes:
            # Generiere Testzahlen
            test_numbers = self._generate_composite_numbers(10, size//10, size)
            
            # Harmonische Tests
            harmonic_times = []
            classical_times = []
            successes = 0
            
            for n in test_numbers:
                # Harmonische Methode
                result = self.factorizer.factorize(n)
                harmonic_times.append(result.time_ms)
                if result.success:
                    successes += 1
                
                # Klassische Methode
                classical_time = self._classical_factorize_time(n)
                classical_times.append(classical_time)
            
            avg_harmonic = statistics.mean(harmonic_times)
            avg_classical = statistics.mean(classical_times)
            speedup = avg_classical / avg_harmonic if avg_harmonic > 0 else float('inf')
            success_rate = successes / len(test_numbers)
            
            print(f"{size:<12,} {avg_harmonic:<10.2f}ms {avg_classical:<10.2f}ms "
                  f"{speedup:<8.1f}x {success_rate:<8.1%}")
            
            benchmark_results.append({
                'size': size,
                'harmonic_time': avg_harmonic,
                'classical_time': avg_classical,
                'speedup': speedup,
                'success_rate': success_rate
            })
        
        return benchmark_results
    
    def run_comprehensive_test(self) -> Dict:
        """
        Umfassender Test aller Funktionen
        
        Returns:
            Vollständige Testergebnisse
        """
        print("🧪 UMFASSENDER HARMONIC FACTORIZATION TEST")
        print("=" * 80)
        
        # Verschiedene Testphasen
        tests = {}
        
        print("\n1. Range Test (100-500)")
        tests['range'] = self.run_range_test(100, 500, 5)
        
        print("\n\n2. Prime Product Test")
        tests['prime_products'] = self.run_prime_product_test(50, 100)
        
        print("\n\n3. Harmonic Construction Test")
        tests['harmonic_construction'] = self.run_harmonic_construction_test(5)
        
        print("\n\n4. Performance Benchmark")
        tests['performance'] = self.run_performance_benchmark([1000, 10000, 100000])
        
        # Gesamtstatistiken
        print("\n\n📊 GESAMTSTATISTIKEN")
        print("=" * 40)
        overall_stats = self.factorizer.get_statistics()
        
        for key, value in overall_stats.items():
            if isinstance(value, float):
                print(f"{key}: {value:.3f}")
            elif isinstance(value, dict):
                print(f"{key}: {len(value)} Einträge")
            else:
                print(f"{key}: {value}")
        
        return {
            'tests': tests,
            'overall_statistics': overall_stats,
            'factorizer_config': {
                'tolerance': float(self.factorizer.tolerance),
                'harmonic_count': len(self.factorizer.harmonics)
            }
        }
    
    def _is_composite(self, n: int) -> bool:
        """Prüfe ob Zahl zusammengesetzt ist"""
        if n < 4:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return True
        return False
    
    def _generate_primes(self, max_n: int) -> List[int]:
        """Generiere Primzahlen bis max_n mit Sieb des Eratosthenes"""
        sieve = [True] * (max_n + 1)
        sieve[0] = sieve[1] = False
        
        for i in range(2, int(math.sqrt(max_n)) + 1):
            if sieve[i]:
                for j in range(i*i, max_n + 1, i):
                    sieve[j] = False
        
        return [i for i in range(2, max_n + 1) if sieve[i]]
    
    def _generate_composite_numbers(self, count: int, min_val: int, max_val: int) -> List[int]:
        """Generiere zusammengesetzte Zahlen"""
        numbers = []
        while len(numbers) < count:
            n = random.randint(min_val, max_val)
            if self._is_composite(n):
                numbers.append(n)
        return numbers
    
    def _classical_factorize_time(self, n: int) -> float:
        """Miss Zeit für klassische Faktorisierung"""
        start_time = time.perf_counter()
        
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                break
        
        return (time.perf_counter() - start_time) * 1000
    
    def _analyze_results(self, results: List[FactorizationResult], total_time: float = 0) -> Dict:
        """Analysiere Testergebnisse"""
        if not results:
            return {'error': 'Keine Ergebnisse'}
        
        successful = [r for r in results if r.success]
        exact = [r for r in results if r.exact]
        
        analysis = {
            'total_tests': len(results),
            'successful': len(successful),
            'exact_matches': len(exact),
            'success_rate': len(successful) / len(results),
            'exact_rate': len(exact) / len(results) if results else 0,
            'average_time_ms': statistics.mean([r.time_ms for r in results]),
            'total_time': total_time
        }
        
        if successful:
            analysis['average_deviation'] = statistics.mean([r.deviation_percent for r in successful])
            analysis['harmonic_distribution'] = {}
            
            for result in successful:
                harmonic = result.harmonic_name
                if harmonic not in analysis['harmonic_distribution']:
                    analysis['harmonic_distribution'][harmonic] = 0
                analysis['harmonic_distribution'][harmonic] += 1
        
        return analysis

class HarmonicAnalyzer:
    """
    Wissenschaftliche Analyse-Tools für harmonische Strukturen
    """
    
    def __init__(self, factorizer: Optional[HarmonicFactorizer] = None):
        self.factorizer = factorizer or HarmonicFactorizer()
    
    def analyze_range(self, start: int, end: int, output_file: str = None) -> Dict:
        """
        Analysiere harmonische Strukturen in einem Zahlenbereich
        
        Args:
            start: Startwert
            end: Endwert  
            output_file: Optional JSON-Ausgabedatei
            
        Returns:
            Detaillierte Analyse
        """
        print(f"📊 Harmonische Analyse: {start:,} - {end:,}")
        print("=" * 50)
        
        analysis = {
            'range': {'start': start, 'end': end},
            'harmonic_patterns': defaultdict(list),
            'ratio_distribution': defaultdict(int),
            'deviation_analysis': [],
            'performance_metrics': {}
        }
        
        start_time = time.perf_counter()
        tested_count = 0
        
        for n in range(start, end + 1):
            if self._is_composite(n):
                result = self.factorizer.factorize(n)
                tested_count += 1
                
                if result.success:
                    # Sammle harmonische Muster
                    pattern = {
                        'number': n,
                        'factors': result.factors,
                        'harmonic': result.harmonic_name,
                        'ratio': float(result.ratio),
                        'deviation': result.deviation_percent,
                        'exact': result.exact
                    }
                    
                    analysis['harmonic_patterns'][result.harmonic_name].append(pattern)
                    analysis['ratio_distribution'][str(result.ratio)] += 1
                    analysis['deviation_analysis'].append(result.deviation_percent)
        
        end_time = time.perf_counter()
        
        # Performance-Metriken
        analysis['performance_metrics'] = {
            'total_time_seconds': end_time - start_time,
            'tested_numbers': tested_count,
            'numbers_per_second': tested_count / (end_time - start_time),
            'success_rate': len([p for patterns in analysis['harmonic_patterns'].values() 
                               for p in patterns]) / tested_count if tested_count > 0 else 0
        }
        
        # Statistische Auswertung
        if analysis['deviation_analysis']:
            analysis['deviation_statistics'] = {
                'mean': statistics.mean(analysis['deviation_analysis']),
                'median': statistics.median(analysis['deviation_analysis']),
                'stdev': statistics.stdev(analysis['deviation_analysis']) if len(analysis['deviation_analysis']) > 1 else 0,
                'min': min(analysis['deviation_analysis']),
                'max': max(analysis['deviation_analysis'])
            }
        
        # Ausgabe in Datei
        if output_file:
            with open(output_file, 'w') as f:
                json.dump(analysis, f, indent=2, default=str)
            print(f"💾 Analyse gespeichert in: {output_file}")
        
        return analysis
    
    def find_golden_ratio_candidates(self, max_n: int = 10000) -> List[Tuple[int, float]]:
        """
        Suche nach Zahlen mit Faktoren nahe dem goldenen Schnitt
        
        Args:
            max_n: Maximale zu testende Zahl
            
        Returns:
            Liste von (Zahl, Abweichung) Tupeln
        """
        golden_ratio = (1 + math.sqrt(5)) / 2  # φ ≈ 1.618
        candidates = []
        
        print(f"🔍 Suche goldenen Schnitt Kandidaten bis {max_n:,}")
        
        for n in range(4, max_n + 1):
            if self._is_composite(n):
                # Finde alle Faktorpaare
                for i in range(2, int(math.sqrt(n)) + 1):
                    if n % i == 0:
                        a, b = i, n // i
                        ratio = max(a, b) / min(a, b)
                        deviation = abs(ratio - golden_ratio) / golden_ratio
                        
                        if deviation < 0.01:  # 1% Toleranz
                            candidates.append((n, deviation * 100))
                        break
        
        candidates.sort(key=lambda x: x[1])  # Sortiere nach Abweichung
        
        print(f"Gefunden: {len(candidates)} Kandidaten")
        for n, dev in candidates[:10]:  # Zeige beste 10
            factors = next((i, n//i) for i in range(2, int(math.sqrt(n))+1) if n % i == 0)
            ratio = max(factors) / min(factors)
            print(f"  {n:>6}: {factors[0]} × {factors[1]} → {ratio:.6f} (Abw: {dev:.3f}%)")
        
        return candidates
    
    def _is_composite(self, n: int) -> bool:
        """Hilfsmethode: Prüfe ob Zahl zusammengesetzt ist"""
        if n < 4:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return True
        return False

# Convenience-Funktionen für einfache Verwendung
def factorize(n: int, tolerance: float = 5.0) -> FactorizationResult:
    """Einfache Faktorisierungs-Funktion"""
    factorizer = HarmonicFactorizer(tolerance)
    return factorizer.factorize(n)

def quick_test(numbers: List[int]) -> None:
    """Schneller Test mehrerer Zahlen"""
    factorizer = HarmonicFactorizer()
    
    print("🎵 QUICK TEST")
    print("-" * 40)
    
    for n in numbers:
        result = factorizer.factorize(n)
        if result.success:
            status = "EXAKT" if result.exact else f"{result.deviation_percent:.1f}%"
            print(f"{n:>8,}: {result.factors[0]} × {result.factors[1]} "
                  f"({result.harmonic_name}) [{status}]")
        else:
            print(f"{n:>8,}: Keine harmonischen Faktoren")

def comprehensive_analysis(start: int, end: int) -> Dict:
    """Umfassende Analyse eines Zahlenbereichs"""
    analyzer = HarmonicAnalyzer()
    return analyzer.analyze_range(start, end)

# Version und Metadaten
__version__ = "1.0.0"
__author__ = "Harmonic Mathematics Research"
__description__ = "Revolutionary ratio-based factorization using musical harmonics"

if __name__ == "__main__":
    # Beispiel-Verwendung bei direkter Ausführung
    print("🎵 Harmonic Factorization Library")
    print(f"Version {__version__}")
    print("=" * 50)
    
    # Schneller Test
    test_numbers = [77, 143, 221, 323, 391, 1247]
    quick_test(test_numbers)
    
    # Umfassender Test
    suite = TestSuite()
    suite.run_comprehensive_test()
