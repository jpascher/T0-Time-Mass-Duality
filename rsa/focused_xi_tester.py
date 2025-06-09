#!/usr/bin/env python3
"""
Fokussierter ξ-Tester für problematische Zahlen
Gezieltes Testing für Zahlen die mit Standard-ξ versagen
"""

from fractions import Fraction
from math import gcd, sqrt
import time
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass 
class FocusedTestResult:
    """Ergebnis eines fokussierten Tests"""
    n: int
    factors_expected: List[int]
    xi_tested: str
    xi_decimal: float
    success: bool
    factors_found: Optional[List[int]]
    resonance_score: float
    time_taken: float
    improvement_over_standard: Optional[float]

class FocusedXiTester:
    """Tester für spezifische problematische Zahlen"""
    
    def __init__(self):
        self.standard_xi = Fraction(1, 100000)
        self.results = []
    
    def get_problematic_numbers(self) -> Dict[str, List[Dict]]:
        """Definiere problematische Zahlen verschiedener Kategorien"""
        return {
            "cousin_primes": [
                {"n": 21, "factors": [3, 7], "diff": 4},
                {"n": 39, "factors": [3, 13], "diff": 10}, 
                {"n": 87, "factors": [3, 29], "diff": 26},
                {"n": 111, "factors": [3, 37], "diff": 34},
                {"n": 159, "factors": [3, 53], "diff": 50},
                {"n": 183, "factors": [3, 61], "diff": 58},
                {"n": 267, "factors": [3, 89], "diff": 86},
                {"n": 291, "factors": [3, 97], "diff": 94},
            ],
            
            "near_twins": [
                {"n": 65, "factors": [5, 13], "diff": 8},
                {"n": 85, "factors": [5, 17], "diff": 12},
                {"n": 115, "factors": [5, 23], "diff": 18},
                {"n": 155, "factors": [5, 31], "diff": 26},
                {"n": 205, "factors": [5, 41], "diff": 36},
                {"n": 235, "factors": [5, 47], "diff": 42},
                {"n": 295, "factors": [5, 59], "diff": 54},
            ],
            
            "distant_primes": [
                {"n": 69, "factors": [3, 23], "diff": 20},
                {"n": 93, "factors": [3, 31], "diff": 28},
                {"n": 123, "factors": [3, 41], "diff": 38},
                {"n": 141, "factors": [3, 47], "diff": 44},
                {"n": 177, "factors": [3, 59], "diff": 56},
                {"n": 201, "factors": [3, 67], "diff": 64},
            ],
            
            "composite_factors": [
                {"n": 55, "factors": [5, 11], "diff": 6},  # 5 ist nicht prim
                {"n": 75, "factors": [3, 25], "diff": 22}, # 25 ist nicht prim
                {"n": 105, "factors": [3, 35], "diff": 32}, # 35 ist nicht prim
                {"n": 165, "factors": [3, 55], "diff": 52}, # 55 ist nicht prim
            ],
            
            "medium_size": [
                {"n": 1643, "factors": [31, 53], "diff": 22},
                {"n": 2491, "factors": [47, 53], "diff": 6}, 
                {"n": 3599, "factors": [59, 61], "diff": 2},  # Twin aber größer
                {"n": 4087, "factors": [61, 67], "diff": 6},
                {"n": 5183, "factors": [71, 73], "diff": 2},  # Twin aber größer
            ],
            
            "special_cases": [
                {"n": 1729, "factors": [7, 13, 19], "diff": None},  # Ramanujan
                {"n": 2047, "factors": [23, 89], "diff": 66},        # Mersenne-related
                {"n": 4181, "factors": [59, 71], "diff": 12},        # Fibonacci-related
            ]
        }
    
    def generate_xi_candidates_for_category(self, category: str) -> List[Fraction]:
        """Generiere ξ-Kandidaten spezifisch für Kategorie"""
        
        base_candidates = [
            # Standard-Bereich erweitern
            Fraction(1, 50000), Fraction(1, 25000), Fraction(1, 10000), 
            Fraction(1, 5000), Fraction(1, 2500), Fraction(1, 1000),
        ]
        
        if category == "cousin_primes":
            # Cousin Primes haben Abstand 4-6, brauchen vermutlich toleranteres ξ
            base_candidates.extend([
                Fraction(1, 500), Fraction(1, 314), Fraction(1, 250),
                Fraction(1, 144), Fraction(1, 89), Fraction(1, 55)
            ])
            
        elif category == "near_twins":
            # Near twins haben größere Abstände, brauchen noch toleranteres ξ
            base_candidates.extend([
                Fraction(1, 377), Fraction(1, 233), Fraction(1, 144),
                Fraction(1, 89), Fraction(1, 55), Fraction(1, 34)
            ])
            
        elif category == "distant_primes":
            # Große Abstände, sehr tolerantes ξ
            base_candidates.extend([
                Fraction(1, 100), Fraction(1, 89), Fraction(1, 55),
                Fraction(1, 34), Fraction(1, 21), Fraction(1, 13)
            ])
            
        elif category == "composite_factors":
            # Composite Faktoren, experimentelle ξ-Werte
            base_candidates.extend([
                Fraction(1, 271), Fraction(1, 1618), Fraction(1, 2718),  # e, φ, e×1000
                Fraction(1, 42), Fraction(1, 73), Fraction(1, 137)       # Spezielle Zahlen
            ])
            
        elif category == "medium_size":
            # Größere Zahlen, ggf. kleinere ξ-Werte
            base_candidates.extend([
                Fraction(1, 200000), Fraction(1, 500000), Fraction(1, 1000000),
                Fraction(1, 314159), Fraction(1, 271828)  # π×100000, e×100000
            ])
            
        elif category == "special_cases":
            # Spezielle Fälle, alle möglichen ξ-Werte
            base_candidates.extend([
                Fraction(1, 1729), Fraction(1, 2047), Fraction(1, 4181),  # Nach den Zahlen selbst
                Fraction(1, 42), Fraction(1, 137), Fraction(1, 1618)      # Physik/Math Konstanten
            ])
        
        # Entferne Duplikate und sortiere
        unique_candidates = list(set(base_candidates))
        unique_candidates.sort(reverse=True)
        return unique_candidates
    
    def test_category_comprehensive(self, category: str) -> Dict:
        """Teste eine Kategorie umfassend"""
        problematic_numbers = self.get_problematic_numbers()
        
        if category not in problematic_numbers:
            print(f"❌ Unbekannte Kategorie: {category}")
            return {}
        
        test_cases = problematic_numbers[category]
        xi_candidates = self.generate_xi_candidates_for_category(category)
        
        print(f"\n🔍 Fokussierter Test: {category}")
        print(f"   Testzahlen: {len(test_cases)}")
        print(f"   ξ-Kandidaten: {len(xi_candidates)}")
        print(f"   Gesamt Tests: {len(test_cases) * len(xi_candidates)}")
        
        category_results = []
        
        # Erst Standard-ξ testen für Baseline
        print(f"\n📏 Baseline mit Standard ξ = {self.standard_xi}")
        standard_results = {}
        for test_case in test_cases:
            n = test_case["n"]
            expected_factors = test_case["factors"]
            
            t0_standard = self._create_t0_instance(self.standard_xi)
            result = t0_standard.factorize(n, max_periods=500)
            standard_results[n] = result
            
            status = "✅" if result['success'] else "❌"
            print(f"   N={n}: {status} (Resonanz: {result['resonance_score']:.6f})")
        
        # Jetzt alternative ξ-Werte testen
        print(f"\n🔬 Teste alternative ξ-Werte...")
        
        best_improvements = []
        
        for xi in xi_candidates:
            xi_str = str(xi)
            xi_decimal = float(xi)
            
            print(f"   Testing ξ = {xi_str} ({xi_decimal:.2e})")
            
            t0_instance = self._create_t0_instance(xi)
            xi_improvements = 0
            
            for test_case in test_cases:
                n = test_case["n"] 
                expected_factors = test_case["factors"]
                
                result = t0_instance.factorize(n, max_periods=500)
                standard_result = standard_results[n]
                
                # Berechne Verbesserung
                improvement = None
                if result['success'] and not standard_result['success']:
                    improvement = float('inf')  # Von Fehler zu Erfolg
                elif result['success'] and standard_result['success']:
                    if result['resonance_score'] > standard_result['resonance_score']:
                        improvement = result['resonance_score'] / standard_result['resonance_score']
                    else:
                        improvement = result['resonance_score'] / standard_result['resonance_score']
                elif not result['success'] and not standard_result['success']:
                    if result['resonance_score'] > standard_result['resonance_score']:
                        improvement = result['resonance_score'] / standard_result['resonance_score']
                
                focused_result = FocusedTestResult(
                    n=n,
                    factors_expected=expected_factors,
                    xi_tested=xi_str,
                    xi_decimal=xi_decimal,
                    success=result['success'],
                    factors_found=result['factors'],
                    resonance_score=result['resonance_score'],
                    time_taken=result['time'],
                    improvement_over_standard=improvement
                )
                
                category_results.append(focused_result)
                
                if result['success'] and not standard_result['success']:
                    xi_improvements += 1
                    print(f"     N={n}: ✅ VERBESSERUNG! (war ❌)")
                elif result['success'] and result['resonance_score'] > standard_result['resonance_score'] * 1.1:
                    print(f"     N={n}: ✅ Bessere Resonanz ({result['resonance_score']:.6f} vs {standard_result['resonance_score']:.6f})")
            
            if xi_improvements > 0:
                best_improvements.append((xi_str, xi_improvements, xi_decimal))
                print(f"   → {xi_improvements} Verbesserungen gefunden!")
        
        # Analysiere Ergebnisse für diese Kategorie
        analysis = self._analyze_category_results(category, category_results, best_improvements)
        
        return analysis
    
    def test_all_categories(self) -> Dict:
        """Teste alle problematischen Kategorien"""
        all_results = {}
        
        print("🚀 COMPREHENSIVE FOKUSSIERTER TEST ALLER KATEGORIEN")
        print("="*60)
        
        categories = list(self.get_problematic_numbers().keys())
        
        for i, category in enumerate(categories, 1):
            print(f"\n[{i}/{len(categories)}] Testing {category}...")
            category_analysis = self.test_category_comprehensive(category)
            all_results[category] = category_analysis
            
            # Kurze Zusammenfassung
            if category_analysis.get('best_xi'):
                best = category_analysis['best_xi']
                print(f"   🏆 Bestes ξ für {category}: {best['xi']} ({best['improvements']} Verbesserungen)")
        
        # Gesamtanalyse
        overall_analysis = self._analyze_all_categories(all_results)
        
        return {
            'categories': all_results,
            'overall': overall_analysis
        }
    
    def _create_t0_instance(self, xi_fraction: Fraction):
        """Erstelle T0-Instance mit ξ-Wert"""
        from automatic_xi_optimizer import XiOptimizedT0
        return XiOptimizedT0(xi_fraction)
    
    def _analyze_category_results(self, category: str, results: List[FocusedTestResult], improvements: List[tuple]) -> Dict:
        """Analysiere Ergebnisse einer Kategorie"""
        
        total_tests = len(results)
        successful_tests = len([r for r in results if r.success])
        
        # Gruppiere nach ξ-Werten
        by_xi = {}
        for result in results:
            if result.xi_tested not in by_xi:
                by_xi[result.xi_tested] = []
            by_xi[result.xi_tested].append(result)
        
        # Finde bestes ξ
        best_xi = None
        best_score = 0
        
        for xi_val, xi_results in by_xi.items():
            successes = len([r for r in xi_results if r.success])
            success_rate = (successes / len(xi_results)) * 100
            avg_resonance = sum(r.resonance_score for r in xi_results) / len(xi_results)
            improvements_count = len([r for r in xi_results if r.improvement_over_standard and r.improvement_over_standard > 1.0])
            
            # Score basierend auf Verbesserungen
            score = success_rate * 0.5 + avg_resonance * 25 + improvements_count * 10
            
            if score > best_score:
                best_score = score
                best_xi = {
                    'xi': xi_val,
                    'success_rate': success_rate,
                    'avg_resonance': avg_resonance,
                    'improvements': improvements_count,
                    'score': score
                }
        
        return {
            'category': category,
            'total_tests': total_tests,
            'successful_tests': successful_tests,
            'success_rate': (successful_tests / total_tests) * 100,
            'best_xi': best_xi,
            'xi_performance': {xi: {'successes': len([r for r in results if r.success]), 
                                   'total': len(results),
                                   'avg_resonance': sum(r.resonance_score for r in results) / len(results)}
                              for xi, results in by_xi.items()},
            'top_improvements': sorted(improvements, key=lambda x: x[1], reverse=True)[:3]
        }
    
    def _analyze_all_categories(self, all_results: Dict) -> Dict:
        """Analysiere Ergebnisse aller Kategorien"""
        
        # Sammle alle besten ξ-Werte
        all_best_xi = []
        for category, analysis in all_results.items():
            if analysis.get('best_xi'):
                all_best_xi.append((category, analysis['best_xi']))
        
        # Finde ξ-Werte die bei mehreren Kategorien gut sind
        xi_category_count = {}
        for category, best_xi in all_best_xi:
            xi_val = best_xi['xi']
            if xi_val not in xi_category_count:
                xi_category_count[xi_val] = []
            xi_category_count[xi_val].append((category, best_xi['improvements']))
        
        # Universal ξ-Werte
        universal_xi = []
        for xi_val, category_performances in xi_category_count.items():
            if len(category_performances) >= 2:  # Gut bei mindestens 2 Kategorien
                total_improvements = sum(perf[1] for perf in category_performances)
                categories = [perf[0] for perf in category_performances]
                universal_xi.append({
                    'xi': xi_val,
                    'categories': categories,
                    'total_improvements': total_improvements
                })
        
        # Sortiere nach Total Improvements
        universal_xi.sort(key=lambda x: x['total_improvements'], reverse=True)
        
        return {
            'total_categories': len(all_results),
            'categories_with_improvements': len([r for r in all_results.values() if r.get('best_xi', {}).get('improvements', 0) > 0]),
            'universal_xi': universal_xi[:5],  # Top 5
            'category_summaries': {cat: {'best_xi': analysis.get('best_xi', {}).get('xi'), 
                                        'improvements': analysis.get('best_xi', {}).get('improvements', 0)}
                                  for cat, analysis in all_results.items()}
        }
    
    def print_comprehensive_report(self, results: Dict):
        """Drucke umfassenden Report"""
        print("\n" + "="*70)
        print("🎯 FOKUSSIERTER ξ-TEST - COMPREHENSIVE REPORT")
        print("="*70)
        
        overall = results['overall']
        categories = results['categories']
        
        print(f"\n📊 OVERVIEW:")
        print(f"   Kategorien getestet: {overall['total_categories']}")
        print(f"   Kategorien mit Verbesserungen: {overall['categories_with_improvements']}")
        
        if overall['universal_xi']:
            print(f"\n🌟 UNIVERSELLE ξ-WERTE:")
            for i, universal in enumerate(overall['universal_xi'], 1):
                categories_str = ", ".join(universal['categories'])
                print(f"   {i}. ξ = {universal['xi']}")
                print(f"      Kategorien: {categories_str}")
                print(f"      Gesamt Verbesserungen: {universal['total_improvements']}")
        
        print(f"\n📈 KATEGORIE-DETAILS:")
        for category, analysis in categories.items():
            print(f"\n{category.upper().replace('_', ' ')}:")
            if analysis.get('best_xi'):
                best = analysis['best_xi']
                print(f"   🏆 Bestes ξ: {best['xi']}")
                print(f"   Erfolgsrate: {best['success_rate']:.1f}%")
                print(f"   Verbesserungen: {best['improvements']}")
                print(f"   Ø Resonanz: {best['avg_resonance']:.6f}")
            else:
                print(f"   ❌ Keine signifikanten Verbesserungen gefunden")
        
        print(f"\n💡 EMPFEHLUNGEN:")
        
        # Top Empfehlungen
        if overall['universal_xi']:
            top_universal = overall['universal_xi'][0]
            print(f"   1. 🌟 Universell: ξ = {top_universal['xi']} für {', '.join(top_universal['categories'])}")
        
        # Kategorie-spezifische Empfehlungen
        for category, analysis in categories.items():
            if analysis.get('best_xi') and analysis['best_xi']['improvements'] > 0:
                best = analysis['best_xi']
                print(f"   • {category}: ξ = {best['xi']} ({best['improvements']} Verbesserungen)")

def main():
    """Hauptprogramm für fokussierte Tests"""
    
    tester = FocusedXiTester()
    
    print("🎯 FOKUSSIERTER ξ-TESTER GESTARTET")
    print("="*50)
    print("Teste problematische Zahlen mit alternativen ξ-Werten")
    
    # Führe umfassende Tests durch
    results = tester.test_all_categories()
    
    # Drucke Report
    tester.print_comprehensive_report(results)
    
    return tester, results

if __name__ == "__main__":
    tester, results = main()