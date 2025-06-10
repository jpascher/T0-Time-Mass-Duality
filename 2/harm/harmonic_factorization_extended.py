#!/usr/bin/env python3
"""
Erweiterte Harmonische Faktorisierung mit Serientests
====================================================

Basierend auf der harmonic_factorization_library.py mit zusätzlichen
Testfunktionen und verbesserter Benutzerinteraktion.

Verwendung:
    python harmonic_extended.py
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

# Import der ursprünglichen Klassen (falls verfügbar)
try:
    from harmonic_lib import HarmonicFactorizer, TestSuite, HarmonicAnalyzer, FactorizationResult
    print("✅ Originale harmonic_lib importiert")
except ImportError:
    print("⚠️  harmonic_lib nicht gefunden - verwende lokale Implementierung")
    
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
        """Vereinfachte lokale Version"""
        
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
        
        def __init__(self, tolerance_percent: float = 5.0):
            self.tolerance = Fraction(int(tolerance_percent * 100), 10000)
            self.harmonics = self.STANDARD_HARMONICS.copy()
            self.stats = {
                'total_factorizations': 0,
                'successful_factorizations': 0,
                'exact_matches': 0,
                'total_time_ms': 0.0,
                'harmonic_distribution': defaultdict(int)
            }
        
        def factorize(self, n: int, verbose: bool = False) -> FactorizationResult:
            start_time = time.perf_counter()
            self.stats['total_factorizations'] += 1
            
            # Teste exakte harmonische Verhältnisse
            exact_result = self._test_exact_harmonics(n, verbose)
            if exact_result:
                end_time = time.perf_counter()
                exact_result.time_ms = (end_time - start_time) * 1000
                exact_result.method = 'exact'
                self._update_stats(exact_result)
                return exact_result
            
            # Teste mit Toleranz
            tolerance_result = self._test_with_tolerance(n, verbose)
            end_time = time.perf_counter()
            
            if tolerance_result:
                tolerance_result.time_ms = (end_time - start_time) * 1000
                tolerance_result.method = 'tolerance'
                self._update_stats(tolerance_result)
                return tolerance_result
            
            return FactorizationResult(
                success=False,
                number=n,
                time_ms=(end_time - start_time) * 1000,
                method='none'
            )
        
        def _test_exact_harmonics(self, n: int, verbose: bool) -> Optional[FactorizationResult]:
            for harmonic in self.harmonics:
                ratio = harmonic.ratio
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
            max_factor = min(int(math.sqrt(n)) + 1, 100000)
            
            for test_a in range(2, max_factor):
                if n % test_a == 0:
                    test_b = n // test_a
                    test_ratio = Fraction(max(test_a, test_b), min(test_a, test_b))
                    
                    for harmonic in self.harmonics:
                        target_ratio = harmonic.ratio
                        
                        if target_ratio > 0:
                            deviation = abs(test_ratio - target_ratio) / target_ratio
                            
                            if deviation <= self.tolerance:
                                deviation_percent = float(deviation * 100)
                                
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
            if result.success:
                self.stats['successful_factorizations'] += 1
                if result.exact:
                    self.stats['exact_matches'] += 1
                self.stats['harmonic_distribution'][result.harmonic_name] += 1
            self.stats['total_time_ms'] += result.time_ms


class ExtendedTestSuite:
    """
    Erweiterte Testsuite mit interaktiven Serientests
    """
    
    def __init__(self, factorizer: Optional[HarmonicFactorizer] = None):
        self.factorizer = factorizer or HarmonicFactorizer()
        self.results = []
        self.session_stats = {
            'tests_run': 0,
            'total_success': 0,
            'total_exact': 0,
            'total_time': 0.0
        }
    
    def interactive_menu(self):
        """Interaktives Hauptmenü"""
        while True:
            self._print_header()
            self._print_menu()
            
            try:
                choice = input("\n🎯 Ihre Wahl: ").strip()
                
                if choice == '1':
                    self.single_test()
                elif choice == '2':
                    self.prime_product_series()
                elif choice == '3':
                    self.harmonic_construction_series()
                elif choice == '4':
                    self.range_test_series()
                elif choice == '5':
                    self.performance_comparison()
                elif choice == '6':
                    self.golden_ratio_search()
                elif choice == '7':
                    self.custom_test_series()
                elif choice == '8':
                    self.show_session_stats()
                elif choice == '9':
                    self.export_results()
                elif choice == '0':
                    print("\n👋 Auf Wiedersehen!")
                    break
                else:
                    print("❌ Ungültige Auswahl!")
                
                input("\n📝 Drücken Sie Enter um fortzufahren...")
                
            except KeyboardInterrupt:
                print("\n\n👋 Programm beendet.")
                break
            except Exception as e:
                print(f"❌ Fehler: {e}")
    
    def _print_header(self):
        """Drucke Programm-Header"""
        print("\n" + "="*70)
        print("🎵 HARMONISCHE FAKTORISIERUNG - Erweiterte Testsuite")
        print("="*70)
        print(f"📊 Session: {self.session_stats['tests_run']} Tests | "
              f"Erfolg: {self._get_success_rate():.1f}% | "
              f"Exakt: {self._get_exact_rate():.1f}%")
        print("="*70)
    
    def _print_menu(self):
        """Drucke Hauptmenü"""
        print("\n🎯 TESTOPTIONEN:")
        print("1️⃣  Einzeltest - Eine Zahl testen")
        print("2️⃣  Primzahl-Produkte Serie - Zufällige Primzahl-Kombinationen")
        print("3️⃣  Harmonische Konstruktion - Konstruierte harmonische Zahlen")
        print("4️⃣  Bereichstest - Systematischer Zahlenbereich")
        print("5️⃣  Performance-Vergleich - Harmonisch vs. Klassisch")
        print("6️⃣  Goldener Schnitt - Suche φ-ähnliche Verhältnisse")
        print("7️⃣  Custom Serie - Benutzerdefinierte Tests")
        print("8️⃣  Session Statistiken - Aktuelle Ergebnisse")
        print("9️⃣  Export - Ergebnisse speichern")
        print("0️⃣  Beenden")
    
    def single_test(self):
        """Einzelner Faktorisierungstest"""
        print("\n🔢 EINZELTEST")
        print("-" * 40)
        
        try:
            number = int(input("Zahl eingeben: "))
            if number < 4:
                print("❌ Zahl muss ≥ 4 sein!")
                return
            
            tolerance = float(input("Toleranz in % (Standard: 5.0): ") or "5.0")
            self.factorizer.tolerance = Fraction(int(tolerance * 100), 10000)
            
            print(f"\n🎼 Teste {number:,} mit {tolerance}% Toleranz...")
            
            result = self.factorizer.factorize(number, verbose=True)
            self._process_single_result(result)
            
        except ValueError:
            print("❌ Ungültige Eingabe!")
    
    def prime_product_series(self):
        """Serie von Primzahl-Produkten"""
        print("\n🔢 PRIMZAHL-PRODUKTE SERIE")
        print("-" * 40)
        
        try:
            count = int(input("Anzahl Tests (Standard: 20): ") or "20")
            max_prime = int(input("Max. Primzahl (Standard: 1000): ") or "1000")
            
            print(f"\n🎲 Generiere {count} Primzahl-Produkte bis {max_prime:,}...")
            
            primes = self._generate_primes(max_prime)
            results = []
            
            for i in range(count):
                if len(primes) < 2:
                    print("❌ Nicht genug Primzahlen!")
                    break
                
                p1, p2 = random.sample(primes, 2)
                number = p1 * p2
                
                print(f"Test {i+1:2d}/{count}: {number:8,} = {p1} × {p2}", end=" → ")
                
                result = self.factorizer.factorize(number)
                results.append(result)
                
                if result.success:
                    status = "EXAKT" if result.exact else f"{result.deviation_percent:.1f}%"
                    print(f"✅ {result.harmonic_name} ({status})")
                else:
                    print("❌ Nicht harmonisch")
            
            self._analyze_series_results("Primzahl-Produkte", results)
            
        except ValueError:
            print("❌ Ungültige Eingabe!")
    
    def harmonic_construction_series(self):
        """Serie konstruierter harmonischer Zahlen"""
        print("\n🎼 HARMONISCHE KONSTRUKTION")
        print("-" * 40)
        
        try:
            max_k = int(input("Max. Multiplikator k (Standard: 10): ") or "10")
            
            print(f"\n🏗️  Konstruiere harmonische Zahlen für k=1 bis {max_k}...")
            
            results = []
            
            for harmonic in self.factorizer.harmonics:
                print(f"\n🎵 {harmonic.name}:")
                
                for k in range(1, max_k + 1):
                    a = k * harmonic.ratio.numerator
                    b = k * harmonic.ratio.denominator
                    number = a * b
                    
                    result = self.factorizer.factorize(number)
                    results.append(result)
                    
                    status = "✅ EXAKT" if result.exact else "❌ FEHLER"
                    print(f"  k={k:2d}: {number:8,} = {a:3d} × {b:3d} → {status}")
            
            self._analyze_series_results("Harmonische Konstruktion", results)
            
        except ValueError:
            print("❌ Ungültige Eingabe!")
    
    def range_test_series(self):
        """Systematischer Bereichstest"""
        print("\n📊 BEREICHSTEST")
        print("-" * 40)
        
        try:
            start = int(input("Start (Standard: 100): ") or "100")
            end = int(input("Ende (Standard: 500): ") or "500")
            step = int(input("Schritt (Standard: 5): ") or "5")
            
            print(f"\n🔍 Teste Bereich {start:,} bis {end:,} (Schritt {step})...")
            
            results = []
            tested = 0
            
            for n in range(start, end + 1, step):
                if self._is_composite(n):
                    tested += 1
                    result = self.factorizer.factorize(n)
                    results.append(result)
                    
                    if result.success:
                        status = "EXAKT" if result.exact else f"{result.deviation_percent:.1f}%"
                        print(f"{n:6,}: {result.factors[0]:3d} × {result.factors[1]:3d} → "
                              f"✅ {result.harmonic_name} ({status})")
                    elif tested % 10 == 0:  # Zeige nur jeden 10. Fehler
                        print(f"{n:6,}: ❌ Nicht harmonisch")
            
            self._analyze_series_results(f"Bereich {start}-{end}", results)
            
        except ValueError:
            print("❌ Ungültige Eingabe!")
    
    def performance_comparison(self):
        """Performance-Vergleich mit klassischer Faktorisierung"""
        print("\n⚡ PERFORMANCE-VERGLEICH")
        print("-" * 40)
        
        try:
            count = int(input("Anzahl Tests (Standard: 50): ") or "50")
            max_number = int(input("Max. Zahl (Standard: 100000): ") or "100000")
            
            print(f"\n🏁 Vergleiche Harmonisch vs. Klassisch für {count} Zahlen...")
            
            # Generiere Testzahlen
            test_numbers = []
            while len(test_numbers) < count:
                n = random.randint(100, max_number)
                if self._is_composite(n):
                    test_numbers.append(n)
            
            harmonic_times = []
            classical_times = []
            successes = 0
            
            print(f"\n{'Zahl':<8} {'Harmonisch':<12} {'Klassisch':<12} {'Speedup':<8} {'Status'}")
            print("-" * 60)
            
            for i, n in enumerate(test_numbers):
                # Harmonische Methode
                start_time = time.perf_counter()
                result = self.factorizer.factorize(n)
                harmonic_time = (time.perf_counter() - start_time) * 1000
                harmonic_times.append(harmonic_time)
                
                if result.success:
                    successes += 1
                
                # Klassische Methode
                classical_time = self._classical_factorize_time(n)
                classical_times.append(classical_time)
                
                speedup = classical_time / harmonic_time if harmonic_time > 0 else float('inf')
                status = "✅" if result.success else "❌"
                
                if i < 10 or result.success:  # Zeige erste 10 oder Erfolge
                    print(f"{n:<8,} {harmonic_time:<10.2f}ms {classical_time:<10.2f}ms "
                          f"{speedup:<6.1f}x {status}")
            
            # Zusammenfassung
            avg_harmonic = statistics.mean(harmonic_times)
            avg_classical = statistics.mean(classical_times)
            avg_speedup = avg_classical / avg_harmonic
            success_rate = successes / count
            
            print("\n📈 PERFORMANCE ZUSAMMENFASSUNG:")
            print(f"Harmonisch: {avg_harmonic:.2f}ms ⌀")
            print(f"Klassisch:  {avg_classical:.2f}ms ⌀")
            print(f"Speedup:    {avg_speedup:.1f}x")
            print(f"Erfolgsquote: {success_rate:.1%}")
            
        except ValueError:
            print("❌ Ungültige Eingabe!")
    
    def golden_ratio_search(self):
        """Suche nach Zahlen mit goldenen Schnitt-ähnlichen Verhältnissen"""
        print("\n🔍 GOLDENER SCHNITT SUCHE")
        print("-" * 40)
        
        try:
            max_n = int(input("Max. Zahl (Standard: 10000): ") or "10000")
            tolerance = float(input("Toleranz in % (Standard: 1.0): ") or "1.0") / 100
            
            golden_ratio = (1 + math.sqrt(5)) / 2  # φ ≈ 1.618
            print(f"\n🌟 Suche Verhältnisse nahe φ = {golden_ratio:.6f} bis {max_n:,}...")
            
            candidates = []
            
            for n in range(4, max_n + 1):
                if self._is_composite(n):
                    factors = self._find_factors(n)
                    if factors:
                        ratio = max(factors) / min(factors)
                        deviation = abs(ratio - golden_ratio) / golden_ratio
                        
                        if deviation < tolerance:
                            candidates.append((n, factors, ratio, deviation))
                
                if n % 1000 == 0:
                    print(f"  Geprüft bis {n:,}...")
            
            # Sortiere nach Abweichung
            candidates.sort(key=lambda x: x[3])
            
            print(f"\n🎯 {len(candidates)} Goldene-Schnitt Kandidaten gefunden:")
            print(f"{'Zahl':<8} {'Faktoren':<12} {'Verhältnis':<12} {'Abweichung'}")
            print("-" * 50)
            
            for n, factors, ratio, deviation in candidates[:20]:
                print(f"{n:<8,} {factors[0]:3d} × {factors[1]:<3d}    "
                      f"{ratio:.6f}    {deviation*100:.3f}%")
            
        except ValueError:
            print("❌ Ungültige Eingabe!")
    
    def custom_test_series(self):
        """Benutzerdefinierte Testserie"""
        print("\n🎯 CUSTOM TESTSERIE")
        print("-" * 40)
        
        try:
            print("Zahlen eingeben (durch Leerzeichen getrennt):")
            numbers_input = input("Zahlen: ")
            
            numbers = [int(x) for x in numbers_input.split()]
            if not numbers:
                print("❌ Keine Zahlen eingegeben!")
                return
            
            tolerance = float(input("Toleranz in % (Standard: 5.0): ") or "5.0")
            self.factorizer.tolerance = Fraction(int(tolerance * 100), 10000)
            
            print(f"\n🎼 Teste {len(numbers)} benutzerdefinierte Zahlen...")
            
            results = []
            
            for number in numbers:
                if number < 4:
                    print(f"{number:8,}: ❌ Zu klein (< 4)")
                    continue
                
                result = self.factorizer.factorize(number)
                results.append(result)
                
                if result.success:
                    status = "EXAKT" if result.exact else f"{result.deviation_percent:.1f}%"
                    print(f"{number:8,}: {result.factors[0]:3d} × {result.factors[1]:3d} → "
                          f"✅ {result.harmonic_name} ({status})")
                else:
                    print(f"{number:8,}: ❌ Keine harmonischen Faktoren")
            
            self._analyze_series_results("Custom Serie", results)
            
        except ValueError:
            print("❌ Ungültige Eingabe!")
    
    def show_session_stats(self):
        """Zeige Session-Statistiken"""
        print("\n📈 SESSION STATISTIKEN")
        print("-" * 40)
        
        stats = self.factorizer.stats
        
        if stats['total_factorizations'] == 0:
            print("📊 Noch keine Tests durchgeführt!")
            return
        
        success_rate = stats['successful_factorizations'] / stats['total_factorizations'] * 100
        exact_rate = stats['exact_matches'] / stats['total_factorizations'] * 100
        avg_time = stats['total_time_ms'] / stats['total_factorizations']
        
        print(f"🔢 Gesamt Tests:      {stats['total_factorizations']:,}")
        print(f"✅ Erfolgreiche:     {stats['successful_factorizations']:,} ({success_rate:.1f}%)")
        print(f"🎯 Exakte Treffer:   {stats['exact_matches']:,} ({exact_rate:.1f}%)")
        print(f"⏱️  Durchschnittszeit: {avg_time:.2f}ms")
        
        if stats['harmonic_distribution']:
            print("\n🎵 Harmonische Verteilung:")
            sorted_harmonics = sorted(stats['harmonic_distribution'].items(), 
                                    key=lambda x: x[1], reverse=True)
            for harmonic, count in sorted_harmonics[:10]:
                percentage = count / stats['successful_factorizations'] * 100
                print(f"  {harmonic:<20}: {count:3d} ({percentage:.1f}%)")
    
    def export_results(self):
        """Exportiere Ergebnisse"""
        print("\n💾 EXPORT ERGEBNISSE")
        print("-" * 40)
        
        filename = input("Dateiname (Standard: harmonic_results.json): ") or "harmonic_results.json"
        
        try:
            export_data = {
                'session_stats': self.session_stats,
                'factorizer_stats': self.factorizer.stats,
                'harmonics_used': [
                    {
                        'name': h.name,
                        'ratio': f"{h.ratio.numerator}:{h.ratio.denominator}",
                        'decimal': float(h.ratio),
                        'category': h.category
                    }
                    for h in self.factorizer.harmonics
                ],
                'export_timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
            }
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, indent=2, ensure_ascii=False, default=str)
            
            print(f"✅ Ergebnisse gespeichert in: {filename}")
            
        except Exception as e:
            print(f"❌ Export-Fehler: {e}")
    
    def _process_single_result(self, result: FactorizationResult):
        """Verarbeite Einzeltest-Ergebnis"""
        self.session_stats['tests_run'] += 1
        self.session_stats['total_time'] += result.time_ms
        
        if result.success:
            self.session_stats['total_success'] += 1
            if result.exact:
                self.session_stats['total_exact'] += 1
            
            print(f"\n✅ ERFOLG: {result.factors[0]} × {result.factors[1]} = {result.number:,}")
            print(f"🎼 Harmonie: {result.harmonic_name}")
            print(f"📐 Verhältnis: {float(result.ratio):.6f}")
            
            if result.exact:
                print("🎯 EXAKTE ÜBEREINSTIMMUNG!")
            else:
                print(f"📊 Abweichung: {result.deviation_percent:.3f}%")
            
            print(f"⏱️  Zeit: {result.time_ms:.2f}ms")
        else:
            print(f"\n❌ FEHLSCHLAG: Keine harmonischen Faktoren für {result.number:,}")
            print(f"⏱️  Zeit: {result.time_ms:.2f}ms")
    
    def _analyze_series_results(self, test_name: str, results: List[FactorizationResult]):
        """Analysiere Serie von Ergebnissen"""
        if not results:
            return
        
        # Update Session Stats
        self.session_stats['tests_run'] += len(results)
        successful = [r for r in results if r.success]
        exact = [r for r in results if r.exact]
        
        self.session_stats['total_success'] += len(successful)
        self.session_stats['total_exact'] += len(exact)
        self.session_stats['total_time'] += sum(r.time_ms for r in results)
        
        # Analyse
        success_rate = len(successful) / len(results) * 100
        exact_rate = len(exact) / len(results) * 100
        avg_time = statistics.mean([r.time_ms for r in results])
        
        print(f"\n📊 SERIE ANALYSE: {test_name}")
        print("-" * 50)
        print(f"🔢 Gesamt Tests:    {len(results):,}")
        print(f"✅ Erfolgreiche:   {len(successful):,} ({success_rate:.1f}%)")
        print(f"🎯 Exakte Treffer: {len(exact):,} ({exact_rate:.1f}%)")
        print(f"⏱️  Ø Zeit:         {avg_time:.2f}ms")
        
        if successful:
            avg_deviation = statistics.mean([r.deviation_percent for r in successful if not r.exact])
            if avg_deviation > 0:
                print(f"📈 Ø Abweichung:   {avg_deviation:.2f}%")
            
            # Harmonische Verteilung
            harmonic_dist = defaultdict(int)
            for r in successful:
                harmonic_dist[r.harmonic_name] += 1
            
            if len(harmonic_dist) > 0:
                print("\n🎵 Top Harmonien:")
                sorted_harmonics = sorted(harmonic_dist.items(), key=lambda x: x[1], reverse=True)
                for harmonic, count in sorted_harmonics[:5]:
                    percentage = count / len(successful) * 100
                    print(f"  {harmonic:<20}: {count:2d} ({percentage:.1f}%)")
    
    def _generate_primes(self, max_n: int) -> List[int]:
        """Generiere Primzahlen bis max_n"""
        sieve = [True] * (max_n + 1)
        sieve[0] = sieve[1] = False
        
        for i in range(2, int(math.sqrt(max_n)) + 1):
            if sieve[i]:
                for j in range(i*i, max_n + 1, i):
                    sieve[j] = False
        
        return [i for i in range(2, max_n + 1) if sieve[i]]
    
    def _is_composite(self, n: int) -> bool:
        """Prüfe ob Zahl zusammengesetzt ist"""
        if n < 4:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return True
        return False
    
    def _find_factors(self, n: int) -> Optional[Tuple[int, int]]:
        """Finde Faktoren einer Zahl"""
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return (i, n // i)
        return None
    
    def _classical_factorize_time(self, n: int) -> float:
        """Miss Zeit für klassische Faktorisierung"""
        start_time = time.perf_counter()
        
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                break
        
        return (time.perf_counter() - start_time) * 1000
    
    def _get_success_rate(self) -> float:
        """Berechne aktuelle Erfolgsquote"""
        if self.session_stats['tests_run'] == 0:
            return 0.0
        return self.session_stats['total_success'] / self.session_stats['tests_run'] * 100
    
    def _get_exact_rate(self) -> float:
        """Berechne aktuelle Exakt-Quote"""
        if self.session_stats['tests_run'] == 0:
            return 0.0
        return self.session_stats['total_exact'] / self.session_stats['tests_run'] * 100


def main():
    """Hauptfunktion"""
    print("🎵 HARMONISCHE FAKTORISIERUNG - Erweiterte Testsuite")
    print("=" * 60)
    print("Basierend auf der harmonischen Faktorisierungsbibliothek")
    print("Verwendet musikalische Intervalle zur effizienten Faktorisierung")
    print("=" * 60)
    
    # Initialisiere Faktorizierer
    factorizer = HarmonicFactorizer(tolerance_percent=5.0)
    
    # Starte interaktive Testsuite
    test_suite = ExtendedTestSuite(factorizer)
    test_suite.interactive_menu()


if __name__ == "__main__":
    main()
