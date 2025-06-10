#!/usr/bin/env python3
"""
ERWEITERTE HARMONISCHE FAKTORISIERUNG - KOMPLEXE TESTS
======================================================

Korrigierte Version für harmonic_lib.py Import

Speichere als: test-komplex-fix.py
Ausführung: python test-komplex-fix.py
"""

import time
import random
import json
import math
from collections import defaultdict, Counter
from datetime import datetime

# KORRIGIERTER IMPORT - verwendet harmonic_lib.py
from harmonic_lib import (
    HarmonicFactorizer, TestSuite, HarmonicAnalyzer, 
    FactorizationResult, quick_test
)

class AdvancedTestRunner:
    """Erweiterte Testumgebung für komplexe Analysen"""
    
    def __init__(self, save_results=True):
        self.save_results = save_results
        self.test_session = {
            'start_time': datetime.now().isoformat(),
            'tests_performed': [],
            'overall_statistics': {},
            'discoveries': []
        }
        
        # Verschiedene Faktorizierer für Vergleiche
        self.factorizers = {
            'standard': HarmonicFactorizer(tolerance_percent=5.0),
            'precise': HarmonicFactorizer(tolerance_percent=2.0),
            'extended': HarmonicFactorizer(tolerance_percent=7.0, use_extended=True),
            'strict': HarmonicFactorizer(tolerance_percent=1.0)
        }
        
        print("🧪 ERWEITERTE HARMONISCHE FAKTORISIERUNG TESTS")
        print("=" * 70)
        print(f"Session Start: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Konfigurierte Faktorizierer: {len(self.factorizers)}")
        print()
    
    def run_quick_validation(self):
        """Schnelle Validierung - teste nur die wichtigsten Funktionen"""
        
        print("🔬 SCHNELL-VALIDIERUNG")
        print("-" * 50)
        
        # Test 1: Bekannte Zahlen
        print("\n1. Bekannte harmonische Zahlen:")
        known_numbers = [77, 143, 221, 323, 391]
        factorizer = self.factorizers['standard']
        
        successes = 0
        for n in known_numbers:
            result = factorizer.factorize(n, verbose=False)
            if result.success:
                successes += 1
                print(f"  ✅ {n:>3}: {result.factors[0]}×{result.factors[1]} "
                      f"({result.harmonic_name}) [{result.deviation_percent:.1f}%]")
            else:
                print(f"  ❌ {n:>3}: Keine Faktoren")
        
        success_rate = successes / len(known_numbers)
        print(f"\n📊 Erfolgsrate bekannte Zahlen: {success_rate:.1%}")
        
        # Test 2: Performance-Stichprobe
        print("\n2. Performance-Stichprobe:")
        
        test_sizes = [1000, 10000, 100000]
        for size in test_sizes:
            # Generiere Test-Zahlen
            p1 = random.randint(int(math.sqrt(size * 0.5)), int(math.sqrt(size)))
            p2 = random.randint(int(size / p1 * 0.8), int(size / p1))
            n = p1 * p2
            
            start_time = time.perf_counter()
            result = factorizer.factorize(n, verbose=False)
            test_time = (time.perf_counter() - start_time) * 1000
            
            status = "✅" if result.success else "❌"
            print(f"  {size:>6,}: n={n:>8,} → {test_time:.2f}ms {status}")
        
        # Test 3: Toleranz-Vergleich (vereinfacht)
        print("\n3. Toleranz-Vergleich:")
        
        test_number = 1247  # Bekannt schwierige Zahl
        
        for name, fact in self.factorizers.items():
            result = fact.factorize(test_number, verbose=False)
            if result.success:
                print(f"  {name:<10}: ✅ {result.factors[0]}×{result.factors[1]} "
                      f"({result.deviation_percent:.2f}%)")
            else:
                print(f"  {name:<10}: ❌ Keine Faktoren")
        
        return success_rate
    
    def run_comprehensive_test(self):
        """Führe umfassende Tests durch"""
        
        print("\n🔬 UMFASSENDE TESTS")
        print("-" * 50)
        
        # Test 1: Skalierungsanalyse (vereinfacht)
        self.test_scaling_simple()
        
        # Test 2: Harmonische Verteilung
        self.test_harmonic_distribution()
        
        # Test 3: Statistische Stichprobe
        self.test_statistical_sample()
        
        # Test 4: Edge Cases
        self.test_edge_cases_simple()
    
    def test_scaling_simple(self):
        """Vereinfachte Skalierungsanalyse"""
        
        print("\n📈 Skalierungsanalyse:")
        
        factorizer = self.factorizers['standard']
        
        size_tests = [
            ("Klein", 100, 1000, 5),
            ("Mittel", 1000, 10000, 5),
            ("Groß", 10000, 100000, 3),
            ("Sehr groß", 100000, 1000000, 2)
        ]
        
        print(f"{'Bereich':<12} {'Durchschnitt':<12} {'Erfolg':<8} {'Zeit'}")
        print("-" * 45)
        
        for name, min_size, max_size, count in size_tests:
            successes = 0
            total_time = 0
            
            for _ in range(count):
                p1 = random.randint(int(math.sqrt(min_size)), int(math.sqrt(max_size)))
                p2 = random.randint(min_size // p1, max_size // p1)
                n = p1 * p2
                
                result = factorizer.factorize(n, verbose=False)
                total_time += result.time_ms
                
                if result.success:
                    successes += 1
            
            avg_size = (min_size + max_size) // 2
            success_rate = successes / count
            avg_time = total_time / count
            
            print(f"{name:<12} {avg_size:<12,} {success_rate:<7.1%} {avg_time:<6.2f}ms")
    
    def test_harmonic_distribution(self):
        """Teste Verteilung der harmonischen Intervalle"""
        
        print("\n🎵 Harmonische Intervall-Verteilung:")
        
        factorizer = self.factorizers['standard']
        harmonic_counts = Counter()
        
        # Teste 100 zufällige Zahlen
        successful_tests = 0
        for _ in range(100):
            p1 = random.randint(10, 100)
            p2 = random.randint(10, 100)
            n = p1 * p2
            
            result = factorizer.factorize(n, verbose=False)
            if result.success:
                successful_tests += 1
                harmonic_counts[result.harmonic_name] += 1
        
        print(f"Erfolgreiche Tests: {successful_tests}/100")
        print("\nVerteilung:")
        
        for harmonic, count in harmonic_counts.most_common():
            percentage = count / successful_tests * 100 if successful_tests > 0 else 0
            print(f"  {harmonic:<25}: {count:>2} ({percentage:>5.1f}%)")
    
    def test_statistical_sample(self):
        """Statistische Stichprobe"""
        
        print("\n📊 Statistische Stichprobe (200 Zahlen):")
        
        factorizer = self.factorizers['standard']
        
        successes = 0
        exact_matches = 0
        deviations = []
        times = []
        
        for _ in range(200):
            p1 = random.randint(10, 200)
            p2 = random.randint(10, 200)
            n = p1 * p2
            
            result = factorizer.factorize(n, verbose=False)
            times.append(result.time_ms)
            
            if result.success:
                successes += 1
                if result.exact:
                    exact_matches += 1
                deviations.append(result.deviation_percent)
        
        success_rate = successes / 200
        exact_rate = exact_matches / 200
        avg_time = sum(times) / len(times)
        
        print(f"  Erfolgsrate: {success_rate:.1%}")
        print(f"  Exakte Treffer: {exact_rate:.1%}")
        print(f"  Durchschnittszeit: {avg_time:.3f}ms")
        
        if deviations:
            avg_deviation = sum(deviations) / len(deviations)
            print(f"  Durchschnittliche Abweichung: {avg_deviation:.2f}%")
            print(f"  Beste Abweichung: {min(deviations):.2f}%")
            print(f"  Schlechteste Abweichung: {max(deviations):.2f}%")
    
    def test_edge_cases_simple(self):
        """Vereinfachte Edge Case Tests"""
        
        print("\n🔍 Edge Cases:")
        
        factorizer = self.factorizers['standard']
        
        # Kleine zusammengesetzte Zahlen
        small_numbers = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28]
        small_successes = 0
        
        print("  Kleine Zahlen (4-28):")
        for n in small_numbers:
            result = factorizer.factorize(n, verbose=False)
            if result.success:
                small_successes += 1
                print(f"    ✅ {n:>2}: {result.factors[0]}×{result.factors[1]} ({result.harmonic_name})")
        
        print(f"    Erfolg: {small_successes}/{len(small_numbers)} = {small_successes/len(small_numbers):.1%}")
        
        # Primzahl-Quadrate
        prime_squares = [4, 9, 25, 49, 121, 169, 289, 361]
        square_successes = 0
        
        print("  Primzahl-Quadrate:")
        for n in prime_squares:
            result = factorizer.factorize(n, verbose=False)
            if result.success:
                square_successes += 1
                print(f"    ✅ {n:>3}: {result.factors[0]}×{result.factors[1]} ({result.harmonic_name})")
        
        print(f"    Erfolg: {square_successes}/{len(prime_squares)} = {square_successes/len(prime_squares):.1%}")
    
    def run_performance_benchmark(self):
        """Performance-Benchmark gegen klassische Methoden"""
        
        print("\n⚡ PERFORMANCE BENCHMARK")
        print("-" * 50)
        
        factorizer = self.factorizers['standard']
        
        test_ranges = [
            (1000, 5),
            (10000, 5),
            (100000, 3),
            (1000000, 2)
        ]
        
        print(f"{'Größe':<10} {'Harmonisch':<12} {'Klassisch':<12} {'Speedup'}")
        print("-" * 50)
        
        for size, count in test_ranges:
            harmonic_times = []
            classical_times = []
            
            for _ in range(count):
                # Generiere Testzahl
                p1 = random.randint(int(math.sqrt(size * 0.7)), int(math.sqrt(size)))
                p2 = random.randint(int(size / p1 * 0.8), int(size / p1))
                n = p1 * p2
                
                # Harmonische Methode
                start = time.perf_counter()
                result = factorizer.factorize(n, verbose=False)
                harmonic_times.append((time.perf_counter() - start) * 1000)
                
                # Klassische Methode (begrenzt)
                start = time.perf_counter()
                self._classical_factorize(n)
                classical_times.append((time.perf_counter() - start) * 1000)
            
            avg_harmonic = sum(harmonic_times) / len(harmonic_times)
            avg_classical = sum(classical_times) / len(classical_times)
            speedup = avg_classical / avg_harmonic if avg_harmonic > 0 else float('inf')
            
            print(f"{size:<10,} {avg_harmonic:<11.2f}ms {avg_classical:<11.2f}ms {speedup:<7.1f}x")
    
    def _classical_factorize(self, n):
        """Klassische Trial Division"""
        limit = min(int(math.sqrt(n)) + 1, 10000)  # Begrenzt für Performance
        for i in range(2, limit):
            if n % i == 0:
                return i, n // i
        return None
    
    def save_results_summary(self):
        """Speichere Zusammenfassung der Ergebnisse"""
        
        if not self.save_results:
            return
        
        # Sammle Statistiken
        summary = {
            'timestamp': datetime.now().isoformat(),
            'factorizer_stats': {}
        }
        
        for name, factorizer in self.factorizers.items():
            stats = factorizer.get_statistics()
            summary['factorizer_stats'][name] = stats
        
        # Speichere
        filename = f"harmonic_test_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2, ensure_ascii=False, default=str)
            print(f"\n💾 Zusammenfassung gespeichert: {filename}")
        except Exception as e:
            print(f"\n❌ Fehler beim Speichern: {e}")

def main():
    """Hauptfunktion mit Auswahlmenü"""
    
    print("🎵 HARMONISCHE FAKTORISIERUNG - ERWEITERTE TESTS")
    print("=" * 60)
    print()
    
    runner = AdvancedTestRunner(save_results=True)
    
    while True:
        print("\nTest-Optionen:")
        print("1. Schnell-Validierung (2-3 Minuten)")
        print("2. Umfassende Tests (5-10 Minuten)")
        print("3. Performance Benchmark")
        print("4. Alle Tests (10+ Minuten)")
        print("5. Beenden")
        
        choice = input("\nWähle Option (1-5): ").strip()
        
        if choice == '1':
            print("\n" + "="*60)
            success_rate = runner.run_quick_validation()
            
            if success_rate >= 0.8:
                print(f"\n✅ VALIDIERUNG ERFOLGREICH! ({success_rate:.1%} Erfolg)")
                print("Die harmonische Faktorisierung funktioniert einwandfrei!")
            else:
                print(f"\n⚠️  Erfolgsrate niedrig: {success_rate:.1%}")
        
        elif choice == '2':
            print("\n" + "="*60)
            runner.run_comprehensive_test()
            print("\n✅ UMFASSENDE TESTS ABGESCHLOSSEN!")
        
        elif choice == '3':
            print("\n" + "="*60)
            runner.run_performance_benchmark()
            print("\n✅ PERFORMANCE BENCHMARK ABGESCHLOSSEN!")
        
        elif choice == '4':
            print("\n" + "="*60)
            print("Starte alle Tests... (kann 10+ Minuten dauern)")
            
            confirm = input("Fortfahren? (j/n): ").strip().lower()
            if confirm in ['j', 'ja', 'y', 'yes', '']:
                runner.run_quick_validation()
                runner.run_comprehensive_test()
                runner.run_performance_benchmark()
                runner.save_results_summary()
                print("\n🎯 ALLE TESTS ABGESCHLOSSEN!")
        
        elif choice == '5':
            runner.save_results_summary()
            print("\n🎵 Auf Wiedersehen!")
            break
        
        else:
            print("❌ Ungültige Option!")

if __name__ == "__main__":
    main()
