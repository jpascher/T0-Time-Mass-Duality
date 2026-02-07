#!/usr/bin/env python3
"""
Automatischer ξ-Parameter Optimizer für T0-Framework
Systematische Erforschung optimaler ξ-Werte für verschiedene Zahlentypen
"""

from fractions import Fraction
from math import gcd, sqrt, log
import time
import csv
import json
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from collections import defaultdict
import statistics

@dataclass
class TestResult:
  """Einzelnes Testergebnis"""
  n: int
  xi_value: str
  xi_decimal: float
  category: str
  success: bool
  factors: Optional[List[int]]
  resonance_score: float
  time_taken: float
  periods_tested: int
  best_period: Optional[int]

class XiOptimizedT0:
  """T0 mit konfigurierbaren ξ-Werten"""
  
  def __init__(self, xi_fraction: Fraction):
    self.xi_fraction = xi_fraction
    self.pi_fraction = Fraction(355, 113)
    self.threshold = Fraction(1, 3)
    
  def factorize(self, N: int, max_periods: int = 1000) -> Dict:
    """Faktorisiere mit aktuellen ξ-Werten"""
    start_time = time.time()
    
    # Triviale Faktoren prüfen
    for basis in [2, 3, 5, 7]:
      if gcd(basis, N) > 1:
        factor = gcd(basis, N)
        return {
          'success': True,
          'factors': [factor, N // factor],
          'resonance_score': 1.0,
          'periods_tested': 0,
          'best_period': None,
          'time': time.time() - start_time
        }
    
    # Periode suchen
    for basis in [2, 3, 5, 7]:
      result = self._find_period(basis, N, max_periods)
      if result['period']:
        factors = self._extract_factors(basis, result['period'], N)
        if factors:
          return {
            'success': True,
            'factors': factors,
            'resonance_score': result['best_resonance'],
            'periods_tested': result['periods_tested'],
            'best_period': result['period'],
            'time': time.time() - start_time
          }
    
    return {
      'success': False,
      'factors': None,
      'resonance_score': 0.0,
      'periods_tested': max_periods * 4,
      'best_period': None,
      'time': time.time() - start_time
    }
  
  def _find_period(self, a: int, N: int, max_periods: int) -> Dict:
    """Finde beste Periode mit Resonanz-Bewertung"""
    best_resonance = Fraction(0, 1)
    best_period = None
    periods_tested = 0
    
    for r in range(2, min(N, max_periods)):
      periods_tested += 1
      if pow(a, r, N) == 1:
        resonance = self._calculate_resonance(r)
        
        if resonance > best_resonance:
          best_resonance = resonance
          best_period = r
        
        if resonance > self.threshold:
          return {
            'period': r,
            'best_resonance': float(best_resonance),
            'periods_tested': periods_tested
          }
    
    return {
      'period': best_period,
      'best_resonance': float(best_resonance),
      'periods_tested': periods_tested
    }
  
  def _calculate_resonance(self, r: int) -> Fraction:
    """Berechne Resonanz-Score"""
    omega = Fraction(2, 1) * self.pi_fraction / Fraction(r, 1)
    diff = omega - self.pi_fraction
    diff_squared = diff * diff
    denominator = Fraction(4, 1) * self.xi_fraction
    exponent = -diff_squared / denominator
    score = Fraction(1, 1) / (Fraction(1, 1) + abs(exponent))
    return score
  
  def _extract_factors(self, a: int, period: int, N: int) -> Optional[List[int]]:
    """Extrahiere Faktoren aus Periode"""
    if period % 2 != 0:
      return None
    
    x = pow(a, period // 2, N)
    if x == N - 1:
      return None
    
    f1 = gcd(x - 1, N)
    f2 = gcd(x + 1, N)
    
    for f in [f1, f2]:
      if 1 < f < N:
        return [f, N // f]
    
    return None

class AutomaticXiOptimizer:
  """Automatischer ξ-Optimizer"""
  
  def __init__(self):
    self.results = []
    
  def generate_xi_candidates(self, focus_type="comprehensive") -> List[Fraction]:
    """Generiere ξ-Kandidaten basierend auf Fokus"""
    candidates = []
    
    if focus_type == "comprehensive":
      # Umfassende Suche
      # Standard Potenzen
      for exp in range(2, 9):
        candidates.append(Fraction(1, 10**exp))
      
      # Fibonacci-ähnlich
      fibonacci = [13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
      for f in fibonacci:
        candidates.append(Fraction(1, f))
      
      # Primzahlen
      primes = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
      for p in primes:
        candidates.append(Fraction(1, p))
        candidates.append(Fraction(1, p * 10))
      
      # Mathematische Konstanten
      candidates.extend([
        Fraction(1, 314), Fraction(1, 3141), Fraction(1, 31415), # π
        Fraction(1, 1618), Fraction(1, 16180), # φ
        Fraction(1, 2718), Fraction(1, 27182), # e
      ])
      
    elif focus_type == "quick":
      # Schnelle Suche - nur vielversprechende Werte
      candidates = [
        Fraction(1, 100), Fraction(1, 500), Fraction(1, 1000),
        Fraction(1, 5000), Fraction(1, 10000), Fraction(1, 50000), Fraction(1, 100000),
        Fraction(1, 314), Fraction(1, 1618), Fraction(1, 2718),
        Fraction(1, 144), Fraction(1, 233), Fraction(1, 377)
      ]
    
    # Entferne Duplikate und sortiere
    unique_candidates = list(set(candidates))
    unique_candidates.sort(reverse=True)
    return unique_candidates
  
  def categorize_number(self, n: int) -> str:
    """Kategorisiere Zahl nach Typ"""
    factors = self._simple_factorize(n)
    
    if len(factors) != 2:
      return "composite"
    
    p, q = factors
    if not (self._is_prime(p) and self._is_prime(q)):
      return "composite_factors"
    
    diff = abs(p - q)
    if diff == 2:
      return "twin_prime"
    elif diff <= 6:
      return "cousin_prime"
    elif diff <= 12:
      return "near_twin_prime"
    elif diff <= 30:
      return "close_prime"
    else:
      return "distant_prime"
  
  def generate_test_numbers(self, category: str = "all") -> List[int]:
    """Generiere Testzahlen für verschiedene Kategorien"""
    
    if category == "twin_prime":
      return [15, 21, 35, 77, 91, 143, 187, 221, 323, 437, 667, 899, 1147, 1517, 1763, 2021, 2491, 3127, 3599, 4087]
    
    elif category == "cousin_prime":
      return [21, 39, 87, 111, 159, 183, 267, 291, 319, 447, 471, 559, 583, 687, 711, 831, 879, 1011, 1079, 1191]
    
    elif category == "near_twin":
      return [65, 85, 115, 155, 205, 235, 295, 335, 365, 445, 515, 545, 635, 695, 745, 865, 905, 965, 1015, 1105]
    
    elif category == "composite":
      return [55, 75, 105, 165, 195, 225, 255, 285, 315, 345, 375, 405, 465, 495, 525, 555, 585, 615, 645, 675]
    
    elif category == "mixed":
      # Gemischte schwierige Fälle
      return [
        # Twin primes
        15, 35, 77, 143, 221,
        # Cousin primes 
        21, 87, 159, 267, 319,
        # Near twins
        65, 115, 205, 295, 365,
        # Composite
        55, 105, 195, 255, 315,
        # Spezielle Fälle
        1729, 2047, 4181 # Carmichael, Mersenne-related
      ]
    
    else: # "all"
      all_numbers = []
      for cat in ["twin_prime", "cousin_prime", "near_twin", "composite"]:
        all_numbers.extend(self.generate_test_numbers(cat)[:10]) # Erste 10 jeder Kategorie
      return sorted(list(set(all_numbers)))
  
  def run_comprehensive_test(self, test_numbers: List[int] = None, xi_focus: str = "quick") -> Dict:
    """Führe umfassenden Test durch"""
    
    if test_numbers is None:
      test_numbers = self.generate_test_numbers("mixed")
    
    xi_candidates = self.generate_xi_candidates(xi_focus)
    
    print(f"🔬 Starte automatische ξ-Optimierung")
    print(f"  Testzahlen: {len(test_numbers)}")
    print(f"  ξ-Kandidaten: {len(xi_candidates)}")
    print(f"  Gesamt Tests: {len(test_numbers) * len(xi_candidates)}")
    print()
    
    total_tests = len(test_numbers) * len(xi_candidates)
    current_test = 0
    
    for xi in xi_candidates:
      xi_str = str(xi)
      xi_decimal = float(xi)
      
      print(f"Testing ξ = {xi_str} ({xi_decimal:.2e})")
      
      t0 = XiOptimizedT0(xi)
      
      for n in test_numbers:
        current_test += 1
        category = self.categorize_number(n)
        
        # Teste Faktorisierung
        result_dict = t0.factorize(n, max_periods=500)
        
        result = TestResult(
          n=n,
          xi_value=xi_str,
          xi_decimal=xi_decimal,
          category=category,
          success=result_dict['success'],
          factors=result_dict['factors'],
          resonance_score=result_dict['resonance_score'],
          time_taken=result_dict['time'],
          periods_tested=result_dict['periods_tested'],
          best_period=result_dict['best_period']
        )
        
        self.results.append(result)
        
        # Progress Update
        if current_test % 20 == 0:
          progress = (current_test / total_tests) * 100
          print(f" Progress: {progress:.1f}% ({current_test}/{total_tests})")
    
    print(f"\n✅ Tests abgeschlossen: {len(self.results)} Ergebnisse")
    return self.analyze_results()
  
  def analyze_results(self) -> Dict:
    """Analysiere alle Testergebnisse"""
    if not self.results:
      return {}
    
    print("\n📊 Analysiere Ergebnisse...")
    
    # Gruppiere nach Kategorien
    by_category = defaultdict(list)
    for result in self.results:
      by_category[result.category].append(result)
    
    # Gruppiere nach ξ-Werten
    by_xi = defaultdict(list)
    for result in self.results:
      by_xi[result.xi_value].append(result)
    
    analysis = {
      'total_tests': len(self.results),
      'categories': {},
      'xi_performance': {},
      'best_xi_overall': None,
      'best_xi_per_category': {},
      'recommendations': []
    }
    
    # Analysiere jede Kategorie
    for category, results in by_category.items():
      total = len(results)
      successes = sum(1 for r in results if r.success)
      success_rate = (successes / total) * 100 if total > 0 else 0
      
      # Finde bestes ξ für diese Kategorie
      category_by_xi = defaultdict(list)
      for result in results:
        category_by_xi[result.xi_value].append(result)
      
      best_xi_for_category = None
      best_score = 0
      
      for xi_val, xi_results in category_by_xi.items():
        xi_successes = sum(1 for r in xi_results if r.success)
        xi_success_rate = (xi_successes / len(xi_results)) * 100
        avg_resonance = statistics.mean([r.resonance_score for r in xi_results])
        
        # Composite Score: Erfolgsrate wichtiger als Resonanz
        composite_score = xi_success_rate * 0.8 + avg_resonance * 20
        
        if composite_score > best_score:
          best_score = composite_score
          best_xi_for_category = {
            'xi': xi_val,
            'success_rate': xi_success_rate,
            'avg_resonance': avg_resonance,
            'score': composite_score
          }
      
      analysis['categories'][category] = {
        'total_tests': total,
        'successes': successes,
        'success_rate': success_rate,
        'best_xi': best_xi_for_category
      }
      
      analysis['best_xi_per_category'][category] = best_xi_for_category
    
    # Analysiere ξ-Performance
    for xi_val, results in by_xi.items():
      total = len(results)
      successes = sum(1 for r in results if r.success)
      success_rate = (successes / total) * 100 if total > 0 else 0
      avg_time = statistics.mean([r.time_taken for r in results])
      avg_resonance = statistics.mean([r.resonance_score for r in results])
      
      analysis['xi_performance'][xi_val] = {
        'total_tests': total,
        'successes': successes,
        'success_rate': success_rate,
        'avg_time': avg_time,
        'avg_resonance': avg_resonance
      }
    
    # Finde overall bestes ξ
    best_overall_xi = None
    best_overall_score = 0
    
    for xi_val, performance in analysis['xi_performance'].items():
      if performance['total_tests'] >= 5: # Mindestens 5 Tests
        score = performance['success_rate'] * 0.9 + performance['avg_resonance'] * 10
        if score > best_overall_score:
          best_overall_score = score
          best_overall_xi = {
            'xi': xi_val,
            'success_rate': performance['success_rate'],
            'avg_resonance': performance['avg_resonance'],
            'score': score
          }
    
    analysis['best_xi_overall'] = best_overall_xi
    
    # Generiere Empfehlungen
    analysis['recommendations'] = self._generate_recommendations(analysis)
    
    return analysis
  
  def _generate_recommendations(self, analysis: Dict) -> List[str]:
    """Generiere Empfehlungen basierend auf Analyse"""
    recommendations = []
    
    if analysis['best_xi_overall']:
      best = analysis['best_xi_overall']
      recommendations.append(
        f"🏆 Overall bestes ξ: {best['xi']} "
        f"(Erfolgsrate: {best['success_rate']:.1f}%)"
      )
    
    for category, best_xi in analysis['best_xi_per_category'].items():
      if best_xi and best_xi['success_rate'] > 50:
        recommendations.append(
          f"📈 {category}: ξ = {best_xi['xi']} "
          f"({best_xi['success_rate']:.1f}% Erfolg)"
        )
    
    # Finde ξ-Werte die bei mehreren Kategorien gut funktionieren
    xi_category_performance = defaultdict(list)
    for category, data in analysis['categories'].items():
      if data['best_xi']:
        xi_category_performance[data['best_xi']['xi']].append(
          (category, data['best_xi']['success_rate'])
        )
    
    for xi_val, category_performances in xi_category_performance.items():
      if len(category_performances) >= 3: # Gut bei mindestens 3 Kategorien
        avg_success = statistics.mean([perf[1] for perf in category_performances])
        if avg_success > 60:
          categories = ", ".join([perf[0] for perf in category_performances])
          recommendations.append(
            f"🌟 Universelles ξ: {xi_val} funktioniert gut bei: {categories}"
          )
    
    return recommendations
  
  def print_report(self, analysis: Dict):
    """Drucke ausführlichen Report"""
    print("\n" + "="*60)
    print("🔬 ξ-PARAMETER OPTIMIERUNG - ERGEBNISSE")
    print("="*60)
    
    if analysis['best_xi_overall']:
      best = analysis['best_xi_overall']
      print(f"\n🏆 OVERALL BESTES ξ:")
      print(f"  ξ = {best['xi']}")
      print(f"  Erfolgsrate: {best['success_rate']:.1f}%")
      print(f"  Ø Resonanz: {best['avg_resonance']:.6f}")
    
    print(f"\n📊 KATEGORIE-PERFORMANCE:")
    for category, data in analysis['categories'].items():
      print(f"\n{category.upper().replace('_', ' ')}:")
      print(f"  Gesamt-Erfolgsrate: {data['success_rate']:.1f}%")
      print(f"  Tests: {data['total_tests']}")
      if data['best_xi']:
        print(f"  Bestes ξ: {data['best_xi']['xi']} ({data['best_xi']['success_rate']:.1f}%)")
    
    print(f"\n💡 EMPFEHLUNGEN:")
    for i, rec in enumerate(analysis['recommendations'], 1):
      print(f"  {i}. {rec}")
    
    print(f"\n📈 TOP ξ-WERTE (nach Erfolgsrate):")
    sorted_xi = sorted(
      analysis['xi_performance'].items(),
      key=lambda x: x[1]['success_rate'],
      reverse=True
    )
    
    for i, (xi_val, performance) in enumerate(sorted_xi[:10], 1):
      if performance['total_tests'] >= 3:
        print(f"  {i:2d}. ξ={xi_val:>12} → {performance['success_rate']:5.1f}% "
           f"({performance['successes']}/{performance['total_tests']} Tests)")
  
  def save_results(self, filename: str = "xi_optimization_results.csv"):
    """Speichere Ergebnisse als CSV"""
    with open(filename, 'w', newline='') as csvfile:
      fieldnames = ['n', 'xi_value', 'xi_decimal', 'category', 'success', 
             'factors', 'resonance_score', 'time_taken', 'periods_tested']
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      
      writer.writeheader()
      for result in self.results:
        writer.writerow({
          'n': result.n,
          'xi_value': result.xi_value,
          'xi_decimal': result.xi_decimal,
          'category': result.category,
          'success': result.success,
          'factors': str(result.factors) if result.factors else None,
          'resonance_score': result.resonance_score,
          'time_taken': result.time_taken,
          'periods_tested': result.periods_tested
        })
    
    print(f"\n💾 Ergebnisse gespeichert: {filename}")
  
  def _simple_factorize(self, n: int) -> List[int]:
    """Einfache Faktorisierung"""
    factors = []
    d = 2
    while d * d <= n:
      while n % d == 0:
        factors.append(d)
        n //= d
      d += 1
    if n > 1:
      factors.append(n)
    return factors
  
  def _is_prime(self, n: int) -> bool:
    """Primzahltest"""
    if n < 2:
      return False
    if n == 2:
      return True
    if n % 2 == 0:
      return False
    for i in range(3, int(sqrt(n)) + 1, 2):
      if n % i == 0:
        return False
    return True

def main():
  """Hauptprogramm für automatische ξ-Optimierung"""
  
  optimizer = AutomaticXiOptimizer()
  
  print("🚀 Automatische ξ-Parameter Optimierung gestartet")
  print("="*50)
  
  # Schnelle Analyse mit wichtigsten Werten
  analysis = optimizer.run_comprehensive_test(
    test_numbers=None, # Verwendet standard mixed set
    xi_focus="quick"  # Schnelle Suche
  )
  
  # Drucke Report
  optimizer.print_report(analysis)
  
  # Speichere Ergebnisse
  optimizer.save_results()
  
  return optimizer, analysis

if __name__ == "__main__":
  optimizer, analysis = main()
