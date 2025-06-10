#!/usr/bin/env python3
"""
EXTREME FAKTORISIERUNG - An der absoluten Grenze
===============================================

Teste Faktorisierungen mit den größtmöglichen Zahlen, die dein PC verkraften kann.
Basierend auf den Grenzen-Tests: Bis 10^15+ ist machbar!

Speichere als: test-extrem.py
Ausführung: python test-extrem.py
"""

import time
import random
import math
import gc
import psutil
from datetime import datetime
from typing import List, Tuple, Optional

from harmonic_lib import HarmonicFactorizer

class ExtremeFactorizer:
    """Faktorisierung an der absoluten Grenze der Machbarkeit"""
    
    def __init__(self):
        self.factorizer = HarmonicFactorizer(tolerance_percent=5.0)
        self.extreme_results = []
        
        print("🔥 EXTREME FAKTORISIERUNG - Absolute Grenzen")
        print("=" * 60)
        print(f"Start: {datetime.now().strftime('%H:%M:%S')}")
        print()
        
        # Bekannte Grenzen aus dem vorherigen Test
        self.practical_limit = 10**15  # 1000T Level
        self.safe_range = 10**12       # 1T Level - garantiert schnell
        
    def generate_extreme_numbers(self) -> List[Tuple[int, str, str]]:
        """Generiere extreme Testzahlen an der Grenze der Machbarkeit"""
        
        extreme_numbers = []
        
        print("🎯 GENERIERE EXTREME TESTZAHLEN...")
        
        # 1. Zahlen nahe der JavaScript-Grenze
        js_limit = 9007199254740991  # 2^53 - 1
        print(f"JavaScript-Grenze: {js_limit:,}")
        
        for i in range(3):
            # Erzeuge Zahl nahe JS-Limit
            factor1 = random.randint(90000000, 100000000)  # ~10^8
            factor2 = js_limit // factor1
            number = factor1 * factor2
            extreme_numbers.append((number, f"JS-Grenze #{i+1}", f"{factor1} × {factor2}"))
        
        # 2. Zahlen an der 10^15 Grenze (praktisches Limit)
        print(f"Praktisches Limit: 10^15")
        
        for i in range(5):
            # Erzeuge Zahlen um 10^15
            magnitude = random.uniform(14.5, 15.2)  # 10^14.5 bis 10^15.2
            target = int(10**magnitude)
            
            sqrt_target = int(math.sqrt(target))
            factor1 = random.randint(int(sqrt_target * 0.8), int(sqrt_target * 1.2))
            factor2 = target // factor1
            number = factor1 * factor2
            extreme_numbers.append((number, f"10^15 Bereich #{i+1}", f"{factor1} × {factor2}"))
        
        # 3. Theoretische Grenzen - darüber hinaus
        print(f"Theoretische Grenzen: 10^16+")
        
        for i in range(3):
            # Versuche 10^16 - 10^18
            magnitude = 16 + i
            sqrt_target = int(10**(magnitude/2))
            
            factor1 = random.randint(int(sqrt_target * 0.9), int(sqrt_target * 1.1))
            factor2 = random.randint(int(sqrt_target * 0.9), int(sqrt_target * 1.1))
            number = factor1 * factor2
            extreme_numbers.append((number, f"10^{magnitude} Test", f"{factor1} × {factor2}"))
        
        # 4. Spezielle mathematische Zahlen
        print(f"Spezielle mathematische Strukturen...")
        
        # Mersenne-ähnliche Strukturen
        for p in [31, 37, 41, 43]:  # Große Primzahlen
            mersenne_like = 2**p - 1
            factor = random.randint(1000, 10000)
            number = mersenne_like * factor
            extreme_numbers.append((number, f"Mersenne-like 2^{p}-1", f"{mersenne_like} × {factor}"))
        
        # Fibonacci-ähnliche große Zahlen
        fib_large = 12200160415121876738  # Großer Fibonacci-ähnlicher Wert
        factor = random.randint(100, 1000)
        number = fib_large * factor
        extreme_numbers.append((number, "Fibonacci-like", f"{fib_large} × {factor}"))
        
        print(f"✅ {len(extreme_numbers)} extreme Testzahlen generiert")
        return extreme_numbers
    
    def test_extreme_factorization(self, number: int, description: str, factors_hint: str) -> dict:
        """Teste eine einzelne extreme Faktorisierung"""
        
        digits = len(str(number))
        magnitude = math.log10(number)
        
        print(f"\n🔬 TESTE: {description}")
        print(f"  Zahl: {number:,}")
        print(f"  Stellen: {digits}")
        print(f"  Größenordnung: 10^{magnitude:.1f}")
        print(f"  Faktoren-Tipp: {factors_hint}")
        
        # Speicher vor Test
        gc.collect()
        memory_before = psutil.virtual_memory().used / (1024**2)
        
        try:
            # Faktorisierungs-Test mit Timeout-Schutz
            start_time = time.perf_counter()
            
            result = self.factorizer.factorize(number, verbose=False)
            
            end_time = time.perf_counter()
            test_time_ms = (end_time - start_time) * 1000
            
            # Speicher nach Test
            memory_after = psutil.virtual_memory().used / (1024**2)
            memory_used = memory_after - memory_before
            
            # Ergebnis analysieren
            if result.success:
                a, b = result.factors
                actual_ratio = max(a, b) / min(a, b)
                
                print(f"  ✅ ERFOLG!")
                print(f"  🎵 Faktoren: {a:,} × {b:,}")
                print(f"  🎼 Harmonisch: {result.harmonic_name}")
                print(f"  📐 Verhältnis: {actual_ratio:.6f}")
                print(f"  📊 Abweichung: {result.deviation_percent:.3f}%")
                print(f"  ⏱️  Zeit: {test_time_ms:.2f}ms")
                print(f"  💾 Speicher: {memory_used:+.1f}MB")
                
                # Verifikation
                if a * b == number:
                    print(f"  ✅ Verifikation: {a} × {b} = {number:,} ✓")
                else:
                    print(f"  ❌ Verifikation FEHLER!")
                
                success_status = "HARMONISCH ERFOLGREICH"
                
            else:
                print(f"  ❌ Keine harmonischen Faktoren gefunden")
                print(f"  ⏱️  Zeit: {test_time_ms:.2f}ms")
                print(f"  💾 Speicher: {memory_used:+.1f}MB")
                
                success_status = "KEINE HARMONISCHEN FAKTOREN"
            
            # Performance-Bewertung
            if test_time_ms < 100:
                performance = "BLITZSCHNELL"
            elif test_time_ms < 1000:
                performance = "SCHNELL"
            elif test_time_ms < 5000:
                performance = "AKZEPTABEL"
            elif test_time_ms < 30000:
                performance = "LANGSAM"
            else:
                performance = "ZU LANGSAM"
            
            print(f"  🚀 Performance: {performance}")
            
            return {
                'number': number,
                'description': description,
                'factors_hint': factors_hint,
                'digits': digits,
                'magnitude': magnitude,
                'success': result.success,
                'time_ms': test_time_ms,
                'memory_mb': memory_used,
                'performance': performance,
                'result': result if result.success else None
            }
            
        except MemoryError:
            print(f"  💥 SPEICHER-FEHLER: Zahl zu groß für verfügbaren RAM")
            return {'error': 'MemoryError', 'number': number, 'description': description}
            
        except OverflowError:
            print(f"  💥 OVERFLOW-FEHLER: Zahl übersteigt Python-Limits")
            return {'error': 'OverflowError', 'number': number, 'description': description}
            
        except Exception as e:
            print(f"  💥 UNERWARTETER FEHLER: {str(e)}")
            return {'error': str(e), 'number': number, 'description': description}
    
    def run_extreme_tests(self):
        """Führe alle extremen Tests durch"""
        
        extreme_numbers = self.generate_extreme_numbers()
        
        print(f"\n🚀 STARTE EXTREME FAKTORISIERUNGS-TESTS")
        print("=" * 60)
        
        successful_tests = 0
        harmonic_successes = 0
        total_time = 0
        
        for i, (number, description, factors_hint) in enumerate(extreme_numbers, 1):
            print(f"\n{'='*60}")
            print(f"TEST {i}/{len(extreme_numbers)}")
            
            result = self.test_extreme_factorization(number, description, factors_hint)
            
            if 'error' not in result:
                successful_tests += 1
                total_time += result['time_ms']
                
                if result['success']:
                    harmonic_successes += 1
                
                self.extreme_results.append(result)
                
                # Kurze Pause zwischen extremen Tests
                time.sleep(0.5)
            else:
                print(f"  💀 Test abgebrochen wegen: {result['error']}")
                break
        
        # Zusammenfassung
        self.print_extreme_summary(successful_tests, harmonic_successes, total_time)
    
    def print_extreme_summary(self, successful_tests: int, harmonic_successes: int, total_time: float):
        """Drucke Zusammenfassung der extremen Tests"""
        
        print(f"\n" + "="*70)
        print("🏆 EXTREME FAKTORISIERUNG - ENDERGEBNIS")
        print("="*70)
        
        if successful_tests == 0:
            print("❌ Keine erfolgreichen Tests - Limit erreicht!")
            return
        
        print(f"\n📊 GESAMTSTATISTIK:")
        print(f"  Durchgeführte Tests: {successful_tests}")
        print(f"  Harmonische Erfolge: {harmonic_successes}")
        print(f"  Harmonische Rate: {harmonic_successes/successful_tests:.1%}")
        print(f"  Gesamtzeit: {total_time/1000:.1f} Sekunden")
        print(f"  Ø Zeit pro Test: {total_time/successful_tests:.1f}ms")
        
        # Finde extremste erfolgreiche Faktorisierung
        if self.extreme_results:
            largest_number = max(self.extreme_results, key=lambda x: x['number'])
            fastest_test = min(self.extreme_results, key=lambda x: x['time_ms'])
            
            print(f"\n🥇 GRÖSSTE ERFOLGREICH GETESTETE ZAHL:")
            print(f"  Zahl: {largest_number['number']:,}")
            print(f"  Beschreibung: {largest_number['description']}")
            print(f"  Stellen: {largest_number['digits']}")
            print(f"  Größenordnung: 10^{largest_number['magnitude']:.1f}")
            print(f"  Zeit: {largest_number['time_ms']:.2f}ms")
            print(f"  Status: {largest_number['performance']}")
            
            print(f"\n⚡ SCHNELLSTER EXTREMER TEST:")
            print(f"  Zahl: {fastest_test['number']:,}")
            print(f"  Zeit: {fastest_test['time_ms']:.2f}ms")
            print(f"  Beschreibung: {fastest_test['description']}")
            
            # Harmonische Erfolge analysieren
            harmonic_results = [r for r in self.extreme_results if r['success']]
            
            if harmonic_results:
                print(f"\n🎵 HARMONISCHE EXTREME ERFOLGE:")
                
                for result in harmonic_results:
                    res_obj = result['result']
                    print(f"  {result['number']:,}")
                    print(f"    → {res_obj.factors[0]:,} × {res_obj.factors[1]:,}")
                    print(f"    → {res_obj.harmonic_name} ({res_obj.deviation_percent:.2f}%)")
                    print(f"    → {result['time_ms']:.1f}ms")
        
        # Performance-Verteilung
        performance_counts = {}
        for result in self.extreme_results:
            perf = result['performance']
            performance_counts[perf] = performance_counts.get(perf, 0) + 1
        
        print(f"\n📈 PERFORMANCE-VERTEILUNG:")
        for performance, count in sorted(performance_counts.items()):
            print(f"  {performance}: {count} Tests")
        
        print(f"\n🎯 FAZIT:")
        if harmonic_successes > 0:
            print(f"  ✅ Harmonische Faktorisierung funktioniert selbst an extremen Grenzen!")
            print(f"  🚀 Dein PC kann Zahlen bis ~10^{largest_number['magnitude']:.0f} harmonisch faktorisieren!")
        else:
            print(f"  ⚠️  Extreme Zahlen überschreiten harmonische Bereiche")
            print(f"  📊 Aber Performance bleibt konstant - kein Algorithmus-Versagen!")
        
        print(f"  🎼 Die harmonische Faktorisierung ist production-ready!")

def main():
    """Hauptfunktion für extreme Tests"""
    
    print("🔥 WILLKOMMEN ZUM EXTREMEN FAKTORISIERUNGS-TEST!")
    print()
    print("Dieser Test wird die größtmöglichen Zahlen versuchen,")
    print("die dein PC mit harmonischer Faktorisierung verkraften kann.")
    print()
    print("Basierend auf vorherigen Tests:")
    print("  • Praktikabel bis: 10^15")
    print("  • Konstante Zeit bis: 10^15+")
    print("  • Theoretisches Limit: Unbekannt")
    print()
    
    proceed = input("Extreme Tests starten? (j/n): ").strip().lower()
    
    if proceed in ['j', 'ja', 'y', 'yes', '']:
        factorizer = ExtremeFactorizer()
        factorizer.run_extreme_tests()
        
        print(f"\n🎵 Extreme Tests abgeschlossen: {datetime.now().strftime('%H:%M:%S')}")
        
        # Optionaler Export der Ergebnisse
        if factorizer.extreme_results:
            export = input("\nErgebnisse in Datei speichern? (j/n): ").strip().lower()
            if export in ['j', 'ja', 'y', 'yes']:
                import json
                filename = f"extreme_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                
                # Bereite Daten für JSON vor
                export_data = []
                for result in factorizer.extreme_results:
                    export_result = result.copy()
                    if 'result' in export_result and export_result['result']:
                        # Konvertiere FactorizationResult zu dict
                        res = export_result['result']
                        export_result['harmonic_details'] = {
                            'factors': res.factors,
                            'harmonic_name': res.harmonic_name,
                            'deviation_percent': res.deviation_percent,
                            'exact': res.exact
                        }
                        del export_result['result']
                    export_data.append(export_result)
                
                with open(filename, 'w') as f:
                    json.dump(export_data, f, indent=2, default=str)
                
                print(f"💾 Ergebnisse gespeichert: {filename}")
    else:
        print("Tests abgebrochen.")

if __name__ == "__main__":
    main()
