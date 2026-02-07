#!/usr/bin/env python3
"""
T0 Period Structure Analyzer - Systematische Analyse des Perioden-Problems
Untersucht warum T0 bei bestimmten Zahlen versagt trotz Periodenfindung
Version 1.0 - Fokus auf gerade vs ungerade Perioden
"""

import math
from fractions import Fraction
from typing import List, Dict, Tuple, Optional

class T0PeriodAnalyzer:
  """Analysiert Perioden-Strukturen und T0's Limitationen"""
  
  def __init__(self):
    self.bases = [2, 3, 5, 7, 11, 13, 17, 19] # Erweiterte Basis-Liste
    
  def gcd(self, a: int, b: int) -> int:
    """Greatest Common Divisor"""
    while b:
      a, b = b, a % b
    return a
  
  def find_order(self, a: int, n: int, max_order: int = 1000) -> Optional[int]:
    """Finde Ordnung von a modulo n (kleinste r mit a^r ≡ 1 mod n)"""
    if self.gcd(a, n) != 1:
      return None
      
    current = a % n
    for r in range(1, min(max_order, n)):
      if current == 1:
        return r
      current = (current * a) % n
    return None
  
  def can_extract_factors(self, a: int, r: int, n: int) -> Tuple[bool, List[int], str]:
    """
    Prüfe ob aus Periode r Faktoren extrahiert werden können
    Returns: (success, factors, method_used)
    """
    factors = []
    method = "none"
    
    # Standard T0-Methode: r muss gerade sein
    if r % 2 == 0:
      x = pow(a, r // 2, n)
      if x != n - 1: # x ≠ -1 (mod n)
        f1 = self.gcd(x - 1, n)
        f2 = self.gcd(x + 1, n)
        
        for f in [f1, f2]:
          if 1 < f < n:
            factors = [f, n // f]
            method = "even_period_standard"
            return True, factors, method
    
    # Alternative Methode für ungerade Perioden: Verwende 2r
    if r % 2 == 1:
      # Versuche 2r als neue Periode
      double_r = 2 * r
      if pow(a, double_r, n) == 1:
        x = pow(a, r, n) # a^r mod n
        if x != 1 and x != n - 1:
          f1 = self.gcd(x - 1, n)
          f2 = self.gcd(x + 1, n)
          
          for f in [f1, f2]:
            if 1 < f < n:
              factors = [f, n // f]
              method = "odd_period_doubled"
              return True, factors, method
    
    # Erweiterte Methode: Teiler von r verwenden
    if r > 1:
      for divisor in self._get_divisors(r):
        if divisor > 1 and divisor < r:
          x = pow(a, divisor, n)
          if x != 1:
            f1 = self.gcd(x - 1, n)
            if 1 < f1 < n:
              factors = [f1, n // f1]
              method = f"period_divisor_{divisor}"
              return True, factors, method
    
    return False, [], method
  
  def _get_divisors(self, n: int) -> List[int]:
    """Finde alle Teiler von n"""
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
      if n % i == 0:
        divisors.append(i)
        if i != n // i:
          divisors.append(n // i)
    return sorted(divisors)
  
  def analyze_number(self, n: int, expected_factors: List[int]) -> Dict:
    """Vollständige Analyse einer Zahl"""
    print(f"\n{'='*60}")
    print(f"🔬 ANALYZING N = {n}")
    print(f"Expected factors: {expected_factors}")
    print(f"Product check: {expected_factors[0] * expected_factors[1] == n}")
    print(f"{'='*60}")
    
    analysis = {
      'n': n,
      'expected_factors': expected_factors,
      'basis_results': {},
      'successful_extractions': [],
      'failed_extractions': [],
      'period_statistics': {
        'even_periods': [],
        'odd_periods': [],
        'total_periods_found': 0
      }
    }
    
    successful_methods = set()
    
    for base in self.bases:
      if self.gcd(base, n) != 1:
        print(f" Base {base}: Skipped (gcd({base}, {n}) ≠ 1)")
        continue
        
      order = self.find_order(base, n)
      if order is None:
        print(f" Base {base}: No order found (>1000)")
        continue
      
      # Klassifiziere Periode
      if order % 2 == 0:
        analysis['period_statistics']['even_periods'].append(order)
      else:
        analysis['period_statistics']['odd_periods'].append(order)
      
      analysis['period_statistics']['total_periods_found'] += 1
      
      # Versuche Faktor-Extraktion
      success, factors, method = self.can_extract_factors(base, order, n)
      
      result = {
        'base': base,
        'order': order,
        'period_parity': 'even' if order % 2 == 0 else 'odd',
        'extraction_success': success,
        'extracted_factors': factors,
        'method_used': method
      }
      
      analysis['basis_results'][base] = result
      
      if success:
        analysis['successful_extractions'].append(result)
        successful_methods.add(method)
        print(f" Base {base}: ✅ r={order} ({result['period_parity']}) → {factors} via {method}")
      else:
        analysis['failed_extractions'].append(result)
        print(f" Base {base}: ❌ r={order} ({result['period_parity']}) → extraction failed")
    
    # Zusammenfassung
    print(f"\n📊 SUMMARY:")
    print(f" Total periods found: {analysis['period_statistics']['total_periods_found']}")
    print(f" Even periods: {len(analysis['period_statistics']['even_periods'])} → {analysis['period_statistics']['even_periods']}")
    print(f" Odd periods: {len(analysis['period_statistics']['odd_periods'])} → {analysis['period_statistics']['odd_periods']}")
    print(f" Successful extractions: {len(analysis['successful_extractions'])}")
    print(f" Methods that worked: {successful_methods}")
    
    # Bestimme warum T0 versagt oder funktioniert
    if analysis['successful_extractions']:
      print(f" 🎯 T0 SHOULD WORK: {len(analysis['successful_extractions'])} extraction methods available")
    else:
      print(f" ❌ T0 FAILS: No extraction methods work")
      
      # Analysiere Failure-Gründe
      even_periods = len(analysis['period_statistics']['even_periods'])
      odd_periods = len(analysis['period_statistics']['odd_periods'])
      
      if even_periods == 0 and odd_periods > 0:
        print(f"   Reason: Only odd periods available → Standard T0 can't use them")
      elif even_periods > 0:
        print(f"   Reason: Even periods available but extraction fails → Implementation issue")
      else:
        print(f"   Reason: No suitable periods found")
    
    analysis['conclusion'] = self._generate_conclusion(analysis)
    return analysis
  
  def _generate_conclusion(self, analysis: Dict) -> str:
    """Generiere Schlussfolgerung basierend auf Analyse"""
    if analysis['successful_extractions']:
      return "SUCCESS_POSSIBLE"
    elif len(analysis['period_statistics']['even_periods']) == 0:
      return "ONLY_ODD_PERIODS"
    elif len(analysis['period_statistics']['even_periods']) > 0:
      return "EVEN_PERIODS_BUT_EXTRACTION_FAILS"
    else:
      return "NO_PERIODS_FOUND"
  
  def run_systematic_analysis(self):
    """Führe systematische Analyse auf Problem- und Working-Cases aus"""
    print("🔬 T0 PERIOD STRUCTURE ANALYSIS")
    print("=" * 80)
    print("Investigating why T0 fails on seemingly easy cases")
    print("Focus: Period parity and extraction methods")
    print("=" * 80)
    
    # Test Cases aus Ihren Ergebnissen
    test_cases = [
      # Working Cases (sollten funktionieren)
      (221, [13, 17], "Working Case - Twin Prime"),
      (667, [23, 29], "Working Case - Twin Prime"),
      (77, [7, 11], "Working Case - Twin Prime"),
      (21, [3, 7], "Working Case - Cousin Prime"),
      
      # Problem Cases (versagen aktuell)
      (143, [11, 13], "Problem Case - Twin Prime"),
      (323, [17, 19], "Problem Case - Twin Prime"),
      (1517, [37, 41], "Problem Case - Twin Prime"),
      (2491, [47, 53], "Problem Case - Twin Prime"),
      
      # Zusätzliche Test Cases
      (35, [5, 7], "Additional - Twin Prime"),
      (87, [3, 29], "Additional - Cousin Prime"),
    ]
    
    results = []
    working_cases = []
    problem_cases = []
    
    for n, factors, description in test_cases:
      analysis = self.analyze_number(n, factors)
      results.append(analysis)
      
      if "Working" in description:
        working_cases.append(analysis)
      elif "Problem" in description:
        problem_cases.append(analysis)
    
    # Vergleichende Analyse
    self._compare_cases(working_cases, problem_cases)
    
    return results
  
  def _compare_cases(self, working_cases: List[Dict], problem_cases: List[Dict]):
    """Vergleiche Working vs Problem Cases"""
    print(f"\n{'='*80}")
    print("🎯 COMPARATIVE ANALYSIS: Working vs Problem Cases")
    print(f"{'='*80}")
    
    print(f"\n📊 WORKING CASES PATTERNS:")
    working_conclusions = [case['conclusion'] for case in working_cases]
    working_even_periods = sum(len(case['period_statistics']['even_periods']) for case in working_cases)
    working_odd_periods = sum(len(case['period_statistics']['odd_periods']) for case in working_cases)
    working_successes = sum(len(case['successful_extractions']) for case in working_cases)
    
    print(f" Cases: {len(working_cases)}")
    print(f" Total even periods found: {working_even_periods}")
    print(f" Total odd periods found: {working_odd_periods}")
    print(f" Total successful extractions: {working_successes}")
    print(f" Conclusions: {set(working_conclusions)}")
    
    print(f"\n📊 PROBLEM CASES PATTERNS:")
    problem_conclusions = [case['conclusion'] for case in problem_cases]
    problem_even_periods = sum(len(case['period_statistics']['even_periods']) for case in problem_cases)
    problem_odd_periods = sum(len(case['period_statistics']['odd_periods']) for case in problem_cases)
    problem_successes = sum(len(case['successful_extractions']) for case in problem_cases)
    
    print(f" Cases: {len(problem_cases)}")
    print(f" Total even periods found: {problem_even_periods}")
    print(f" Total odd periods found: {problem_odd_periods}")
    print(f" Total successful extractions: {problem_successes}")
    print(f" Conclusions: {set(problem_conclusions)}")
    
    print(f"\n🎯 KEY DIFFERENCES:")
    print(f" Even periods ratio - Working: {working_even_periods/len(working_cases):.1f}, Problem: {problem_even_periods/len(problem_cases):.1f}")
    print(f" Success ratio - Working: {working_successes/len(working_cases):.1f}, Problem: {problem_successes/len(problem_cases):.1f}")
    
    # Hypothesen testen
    print(f"\n🧠 HYPOTHESIS TESTING:")
    
    # H1: Problem cases haben nur ungerade Perioden
    only_odd_problem_cases = sum(1 for case in problem_cases if case['conclusion'] == 'ONLY_ODD_PERIODS')
    print(f" H1 - Problem cases with only odd periods: {only_odd_problem_cases}/{len(problem_cases)} ({100*only_odd_problem_cases/len(problem_cases):.0f}%)")
    
    # H2: Working cases haben mehr gerade Perioden
    avg_even_working = working_even_periods / len(working_cases) if working_cases else 0
    avg_even_problem = problem_even_periods / len(problem_cases) if problem_cases else 0
    print(f" H2 - Average even periods: Working={avg_even_working:.1f}, Problem={avg_even_problem:.1f}")
    
    # H3: Extraction-Methoden Unterschiede
    working_methods = set()
    for case in working_cases:
      for extraction in case['successful_extractions']:
        working_methods.add(extraction['method_used'])
    print(f" H3 - Methods that work on working cases: {working_methods}")
  
  def test_improved_extraction(self):
    """Teste verbesserte Extraktions-Methoden für ungerade Perioden"""
    print(f"\n{'='*80}")
    print("🚀 TESTING IMPROVED EXTRACTION METHODS")
    print(f"{'='*80}")
    
    # Teste auf bekannten Problem Cases
    problem_cases = [143, 323, 1517]
    
    for n in problem_cases:
      print(f"\n🔬 Testing improved methods on N={n}")
      
      # Standard-Faktorisierung zum Vergleich
      factors = self._simple_factorize(n)
      print(f"  Actual factors: {factors}")
      
      # Finde alle Perioden
      periods_found = {}
      for base in [2, 3, 5, 7]:
        if self.gcd(base, n) == 1:
          order = self.find_order(base, n)
          if order:
            periods_found[base] = order
      
      print(f"  Periods found: {periods_found}")
      
      # Teste erweiterte Extraction-Methoden
      for base, period in periods_found.items():
        success, extracted_factors, method = self.can_extract_factors(base, period, n)
        if success:
          print(f"  ✅ Base {base}, period {period}: {extracted_factors} via {method}")
        else:
          print(f"  ❌ Base {base}, period {period}: extraction failed")
          
          # Debug warum es fehlschlägt
          if period % 2 == 1:
            print(f"   Reason: Odd period ({period}) - standard T0 can't handle")
          else:
            x = pow(base, period // 2, n)
            print(f"   Debug: x = {base}^{period//2} ≡ {x} (mod {n})")
            print(f"   Debug: x-1 = {x-1}, gcd({x-1}, {n}) = {self.gcd(x-1, n)}")
            print(f"   Debug: x+1 = {x+1}, gcd({x+1}, {n}) = {self.gcd(x+1, n)}")
  
  def _simple_factorize(self, n: int) -> List[int]:
    """Einfache Faktorisierung für Vergleich"""
    factors = []
    d = 2
    temp_n = n
    while d * d <= temp_n:
      while temp_n % d == 0:
        factors.append(d)
        temp_n //= d
      d += 1
    if temp_n > 1:
      factors.append(temp_n)
    return factors

def main():
  """Hauptfunktion"""
  analyzer = T0PeriodAnalyzer()
  
  # Führe systematische Analyse aus
  results = analyzer.run_systematic_analysis()
  
  # Teste verbesserte Extraction-Methoden
  analyzer.test_improved_extraction()
  
  print(f"\n{'='*80}")
  print("💡 CONCLUSIONS AND NEXT STEPS")
  print(f"{'='*80}")
  print("1. Analyze the period patterns between working and problem cases")
  print("2. Investigate why standard extraction fails on even periods")
  print("3. Develop alternative extraction methods for odd periods")
  print("4. Test if expanded basis set [2,3,5,7,11,13,17,19] helps")
  print("5. Consider hybrid approaches combining multiple extraction methods")

if __name__ == "__main__":
  main()

