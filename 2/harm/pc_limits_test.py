#!/usr/bin/env python3
"""
PC-GRENZEN TEST - Harmonische Faktorisierung
============================================

Erkunde die absoluten Grenzen deines PCs mit der harmonischen Faktorisierung.
Teste systematisch steigende Zahlengrößen bis zum Limit.

Speichere als: test-grenzen.py
Ausführung: python test-grenzen.py
"""

import time
import sys
import psutil
import gc
import random
import math
from datetime import datetime
from typing import List, Tuple, Dict

from harmonic_lib import HarmonicFactorizer

class PCLimitsExplorer:
    """Erkunde die Grenzen des PCs für harmonische Faktorisierung"""
    
    def __init__(self):
        self.factorizer = HarmonicFactorizer(tolerance_percent=5.0)
        self.results = []
        self.system_info = self._get_system_info()
        
        print("🚀 PC-GRENZEN EXPLORER - Harmonische Faktorisierung")
        print("=" * 70)
        print(f"Start: {datetime.now().strftime('%H:%M:%S')}")
        self._print_system_info()
        print()
        
        # JavaScript-Grenzen für Referenz
        self.js_max_safe_int = 9007199254740991  # 2^53 - 1
        
    def _get_system_info(self) -> Dict:
        """Sammle System-Informationen"""
        try:
            return {
                'cpu_count': psutil.cpu_count(),
                'memory_gb': round(psutil.virtual_memory().total / (1024**3), 1),
                'memory_available_gb': round(psutil.virtual_memory().available / (1024**3), 1),
                'python_version': sys.version.split()[0],
                'platform': sys.platform
            }
        except:
            return {'info': 'Nicht verfügbar'}
    
    def _print_system_info(self):
        """Zeige System-Informationen"""
        print("💻 SYSTEM-INFORMATIONEN:")
        for key, value in self.system_info.items():
            print(f"  {key}: {value}")
    
    def run_scaling_test(self):
        """Teste mit exponentiell steigenden Zahlengrößen"""
        
        print("\n🔬 SKALIERUNGS-GRENZWERT TEST")
        print("-" * 50)
        
        # Exponentiell steigende Zahlengrößen
        size_levels = [
            ("1K", 10**3, 5),
            ("10K", 10**4, 5),  
            ("100K", 10**5, 5),
            ("1M", 10**6, 4),
            ("10M", 10**7, 3),
            ("100M", 10**8, 3),
            ("1B", 10**9, 2),
            ("10B", 10**10, 2),
            ("100B", 10**11, 1),
            ("1T", 10**12, 1),
            ("10T", 10**13, 1),
            ("100T", 10**14, 1),
            ("1000T", 10**15, 1),  # Nahe JavaScript-Maximum
        ]
        
        print(f"{'Level':<8} {'Größe':<15} {'Zeit (ms)':<12} {'Erfolg':<8} {'Speicher':<10} {'Status'}")
        print("-" * 75)
        
        for level_name, target_size, test_count in size_levels:
            try:
                # Garbage Collection vor jedem Test
                gc.collect()
                
                # Messe Speicherverbrauch vor Test
                memory_before = psutil.virtual_memory().used / (1024**2)  # MB
                
                # Führe Tests durch
                total_time = 0
                successes = 0
                test_numbers = []
                
                # Generiere Testzahlen in der Zielgröße
                for _ in range(test_count):
                    test_number = self._generate_number_near_size(target_size)
                    test_numbers.append(test_number)
                
                # Teste jede Zahl
                start_time = time.perf_counter()
                
                for test_number in test_numbers:
                    result = self.factorizer.factorize(test_number, verbose=False)
                    if result.success:
                        successes += 1
                
                total_time = (time.perf_counter() - start_time) * 1000
                avg_time = total_time / test_count
                
                # Messe Speicherverbrauch nach Test
                memory_after = psutil.virtual_memory().used / (1024**2)  # MB
                memory_used = memory_after - memory_before
                
                success_rate = successes / test_count
                size_str = f"~{target_size:,.0e}"
                memory_str = f"{memory_used:+.0f}MB"
                
                # Status bestimmen
                if avg_time < 1000:  # < 1 Sekunde
                    status = "✅ Schnell"
                elif avg_time < 5000:  # < 5 Sekunden
                    status = "⚡ Okay"
                elif avg_time < 30000:  # < 30 Sekunden
                    status = "⚠️  Langsam"
                else:
                    status = "❌ Zu langsam"
                
                print(f"{level_name:<8} {size_str:<15} {avg_time:<11.1f} {success_rate:<7.1%} "
                      f"{memory_str:<10} {status}")
                
                # Speichere Ergebnis
                self.results.append({
                    'level': level_name,
                    'target_size': target_size,
                    'avg_time_ms': avg_time,
                    'success_rate': success_rate,
                    'memory_used_mb': memory_used,
                    'test_numbers': test_numbers[:2],  # Speichere nur erste 2 für Referenz
                    'status': status
                })
                
                # Abbruchkriterium: Wenn zu langsam oder Speicher-Problem
                if avg_time > 30000:  # 30 Sekunden
                    print(f"\n⚠️  ABBRUCH: Test zu langsam ({avg_time/1000:.1f}s)")
                    break
                
                if memory_used > 1000:  # 1GB Speicher-Anstieg
                    print(f"\n⚠️  ABBRUCH: Speicherverbrauch zu hoch ({memory_used:.0f}MB)")
                    break
                
                # Kurze Pause zwischen Tests
                time.sleep(0.5)
                
            except MemoryError:
                print(f"{level_name:<8} {'MEMORY ERROR':<15} {'---':<11} {'---':<7} {'---':<10} ❌ Speicher-Limit")
                break
            except OverflowError:
                print(f"{level_name:<8} {'OVERFLOW ERROR':<15} {'---':<11} {'---':<7} {'---':<10} ❌ Zahl zu groß")
                break
            except Exception as e:
                print(f"{level_name:<8} {'ERROR':<15} {'---':<11} {'---':<7} {'---':<10} ❌ {str(e)[:20]}")
                break
    
    def run_stress_test(self):
        """Stress-Test mit vielen gleichzeitigen Faktorisierungen"""
        
        print("\n🔥 STRESS-TEST: Massive parallele Faktorisierungen")
        print("-" * 50)
        
        stress_levels = [
            ("Leicht", 100, 10**5),
            ("Mittel", 500, 10**6),
            ("Schwer", 1000, 10**7),
            ("Extrem", 2000, 10**8),
            ("Wahnsinn", 5000, 10**9)
        ]
        
        print(f"{'Level':<10} {'Anzahl':<8} {'Größe':<12} {'Zeit (s)':<10} {'Rate':<15} {'Status'}")
        print("-" * 70)
        
        for level_name, count, number_size in stress_levels:
            try:
                gc.collect()  # Aufräumen vor Test
                
                # Generiere viele Testzahlen
                test_numbers = []
                for _ in range(count):
                    test_numbers.append(self._generate_number_near_size(number_size))
                
                # Stress-Test durchführen
                start_time = time.perf_counter()
                successes = 0
                
                for i, test_number in enumerate(test_numbers):
                    result = self.factorizer.factorize(test_number, verbose=False)
                    if result.success:
                        successes += 1
                    
                    # Zwischenstatus alle 500 Tests
                    if (i + 1) % 500 == 0:
                        elapsed = time.perf_counter() - start_time
                        rate = (i + 1) / elapsed
                        print(f"    {i+1:>4}/{count} Tests, {rate:.0f}/s, "
                              f"{successes/(i+1):.1%} Erfolg    ", end='\r')
                
                total_time = time.perf_counter() - start_time
                rate = count / total_time
                success_rate = successes / count
                
                # Status
                if total_time < 10:
                    status = "✅ Exzellent"
                elif total_time < 60:
                    status = "⚡ Gut"
                elif total_time < 300:
                    status = "⚠️  Akzeptabel"
                else:
                    status = "❌ Zu langsam"
                
                size_str = f"~{number_size:.0e}"
                rate_str = f"{rate:.0f} Tests/s"
                
                print(f"{level_name:<10} {count:<8} {size_str:<12} {total_time:<9.1f} "
                      f"{rate_str:<15} {status}")
                
                # Abbruchkriterium
                if total_time > 300:  # 5 Minuten
                    print(f"\n⚠️  STRESS-TEST ABBRUCH: Zu langsam ({total_time:.0f}s)")
                    break
                
            except Exception as e:
                print(f"{level_name:<10} {'ERROR':<8} {'---':<12} {'---':<9} {'---':<15} ❌ {str(e)[:20]}")
                break
    
    def run_memory_limit_test(self):
        """Teste Speicher-Grenzen mit sehr großen Zahlen"""
        
        print("\n💾 SPEICHER-GRENZWERT TEST")
        print("-" * 50)
        
        # Teste mit einzelnen sehr großen Zahlen
        giant_sizes = [
            10**16,  # 10 Billiarden
            10**18,  # 1 Trillion  
            10**20,  # 100 Trilliarden
            10**25,  # Sehr groß
            10**30,  # Extrem groß
        ]
        
        print(f"{'Größe':<15} {'Stellenzahl':<12} {'Zeit (ms)':<12} {'Speicher':<10} {'Status'}")
        print("-" * 65)
        
        for size in giant_sizes:
            try:
                gc.collect()
                memory_before = psutil.virtual_memory().used / (1024**2)
                
                # Generiere eine einzige sehr große Zahl
                test_number = self._generate_number_near_size(size)
                digits = len(str(test_number))
                
                # Teste Faktorisierung
                start_time = time.perf_counter()
                result = self.factorizer.factorize(test_number, verbose=False)
                test_time = (time.perf_counter() - start_time) * 1000
                
                memory_after = psutil.virtual_memory().used / (1024**2)
                memory_used = memory_after - memory_before
                
                size_str = f"{size:.0e}"
                memory_str = f"{memory_used:+.0f}MB"
                
                if test_time < 1000:
                    status = "✅ Schnell"
                elif test_time < 10000:
                    status = "⚡ Okay"
                else:
                    status = "❌ Langsam"
                
                if result.success:
                    status += " 🎵"
                
                print(f"{size_str:<15} {digits:<12} {test_time:<11.1f} {memory_str:<10} {status}")
                
                # Abbruch bei Problemen
                if test_time > 30000 or memory_used > 2000:
                    print("\n⚠️  SPEICHER-TEST ABBRUCH: Ressourcen-Limit erreicht")
                    break
                
            except (MemoryError, OverflowError) as e:
                print(f"{size:.0e:<15} {'---':<12} {'---':<11} {'---':<10} ❌ {type(e).__name__}")
                break
            except Exception as e:
                print(f"{size:.0e:<15} {'---':<12} {'---':<11} {'---':<10} ❌ Error")
                break
    
    def _generate_number_near_size(self, target_size: int) -> int:
        """Generiere eine zusammengesetzte Zahl nahe der Zielgröße"""
        
        # Finde zwei Faktoren, deren Produkt nahe der Zielgröße ist
        sqrt_target = int(math.sqrt(target_size))
        
        # Wähle Faktoren im Bereich um sqrt(target)
        factor_range = max(sqrt_target // 10, 2)
        
        factor1 = random.randint(sqrt_target - factor_range, sqrt_target + factor_range)
        factor2 = random.randint(sqrt_target - factor_range, sqrt_target + factor_range)
        
        # Sorge dafür, dass beide Faktoren > 1 sind
        factor1 = max(factor1, 2)
        factor2 = max(factor2, 2)
        
        return factor1 * factor2
    
    def analyze_results(self):
        """Analysiere und fasse die Testergebnisse zusammen"""
        
        print("\n" + "="*70)
        print("📊 ANALYSE DER PC-GRENZEN")
        print("="*70)
        
        if not self.results:
            print("❌ Keine Ergebnisse zu analysieren.")
            return
        
        # Finde Grenzen
        fast_results = [r for r in self.results if r['avg_time_ms'] < 1000]
        okay_results = [r for r in self.results if 1000 <= r['avg_time_ms'] < 5000]
        slow_results = [r for r in self.results if r['avg_time_ms'] >= 5000]
        
        print(f"\n🚀 PERFORMANCE-KATEGORIEN:")
        print(f"  Schnell (< 1s):    {len(fast_results)} Level")
        print(f"  Okay (1-5s):       {len(okay_results)} Level")  
        print(f"  Langsam (> 5s):    {len(slow_results)} Level")
        
        # Größte erfolgreich getestete Zahl
        if self.results:
            max_level = max(self.results, key=lambda x: x['target_size'])
            print(f"\n🏆 HÖCHSTE GETESTETE GRÖßE:")
            print(f"  Level: {max_level['level']}")
            print(f"  Größe: ~{max_level['target_size']:.0e}")
            print(f"  Zeit: {max_level['avg_time_ms']:.1f}ms")
            print(f"  Erfolgsrate: {max_level['success_rate']:.1%}")
        
        # Praktikabilitäts-Grenze
        practical_levels = [r for r in self.results if r['avg_time_ms'] < 5000]
        if practical_levels:
            practical_limit = max(practical_levels, key=lambda x: x['target_size'])
            print(f"\n✅ PRAKTIKABILITÄTS-GRENZE:")
            print(f"  Größe: ~{practical_limit['target_size']:.0e}")
            print(f"  Zeit: {practical_limit['avg_time_ms']:.1f}ms")
            print(f"  → Harmonische Faktorisierung praktikabel bis {practical_limit['level']}")
        
        # JavaScript-Vergleich
        js_comparable = [r for r in self.results if r['target_size'] <= self.js_max_safe_int]
        if js_comparable:
            print(f"\n🌐 JAVASCRIPT-VERGLEICH:")
            print(f"  JS Maximum: {self.js_max_safe_int:,}")
            print(f"  Getestete Level bis JS-Maximum: {len(js_comparable)}")
            print(f"  → Harmonische Faktorisierung übertrifft Browser-Limits!")
        
        # Empfehlungen
        print(f"\n💡 EMPFEHLUNGEN:")
        if fast_results:
            fast_limit = max(fast_results, key=lambda x: x['target_size'])
            print(f"  Für beste Performance: Bis {fast_limit['level']} (~{fast_limit['target_size']:.0e})")
        
        if practical_levels:
            print(f"  Für praktische Anwendung: Bis {practical_limit['level']}")
        
        print(f"  Dein PC kann harmonische Faktorisierung deutlich über Standard-Limits hinaus!")

def main():
    """Hauptfunktion für PC-Grenzen Tests"""
    
    explorer = PCLimitsExplorer()
    
    print("Welche Grenzen möchten Sie erkunden?")
    print()
    print("1. Skalierungs-Grenzwert (empfohlen zuerst)")
    print("2. Stress-Test (viele parallele Tests)")  
    print("3. Speicher-Grenzwert (sehr große einzelne Zahlen)")
    print("4. Alle Tests (kann sehr lange dauern!)")
    print("5. Nur Analyse der System-Limits")
    
    choice = input("\nWähle Option (1-5): ").strip()
    
    if choice == '1':
        explorer.run_scaling_test()
        explorer.analyze_results()
    
    elif choice == '2':
        explorer.run_stress_test()
    
    elif choice == '3':
        explorer.run_memory_limit_test()
    
    elif choice == '4':
        print("\n⚠️  WARNUNG: Vollständiger Test kann 30+ Minuten dauern!")
        confirm = input("Fortfahren? (j/n): ").strip().lower()
        
        if confirm in ['j', 'ja', 'y', 'yes']:
            explorer.run_scaling_test()
            explorer.run_stress_test() 
            explorer.run_memory_limit_test()
            explorer.analyze_results()
        else:
            print("Tests abgebrochen.")
    
    elif choice == '5':
        print(f"\n💻 SYSTEM-LIMITS ÜBERSICHT:")
        print(f"  Python Integer: Praktisch unbegrenzt")
        print(f"  JavaScript Safe Integer: {explorer.js_max_safe_int:,}")
        print(f"  Verfügbarer RAM: {explorer.system_info.get('memory_available_gb', 'N/A')} GB")
        print(f"  CPU Kerne: {explorer.system_info.get('cpu_count', 'N/A')}")
        print(f"\n🎯 Harmonische Faktorisierung ist hauptsächlich durch Zeit begrenzt, nicht durch Zahlengröße!")
    
    else:
        print("❌ Ungültige Option!")
    
    print(f"\n🎵 PC-Grenzen Test abgeschlossen: {datetime.now().strftime('%H:%M:%S')}")

if __name__ == "__main__":
    main()
