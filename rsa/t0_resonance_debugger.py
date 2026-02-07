#!/usr/bin/env python3
"""
T0 Resonance Debugger - Analysiert die wahren Gründe für T0's Versagen
"""

from fractions import Fraction
import math

class T0ResonanceDebugger:
  """Debuggt T0's Resonanz-Berechnung"""
  
  def __init__(self):
    self.pi_fraction = Fraction(355, 113)
    self.pi_decimal = float(self.pi_fraction)
    
  def debug_resonance_calculation(self):
    """Debugge Resonanz-Berechnung für Problem- und Working-Cases"""
    
    print("=" * 80)
    print("🔬 T0 RESONANCE DEBUGGING - Warum funktioniert die Resonanz nicht?")
    print("=" * 80)
    
    test_cases = [
      # Problem Cases
      (143, [11, 13], "PROBLEM"),
      (323, [17, 19], "PROBLEM"), 
      (1517, [37, 41], "PROBLEM"),
      (2491, [47, 53], "PROBLEM"),
      
      # Working Cases
      (77, [7, 11], "WORKING"),
      (221, [13, 17], "WORKING"),
      (667, [23, 29], "WORKING"),
    ]
    
    for n, factors, case_type in test_cases:
      print(f"\n{'='*60}")
      print(f"🔍 Debugging N = {n} = {factors[0]}×{factors[1]} ({case_type})")
      print(f"{'='*60}")
      
      self.debug_single_case(n, factors, case_type)
    
    self.analyze_patterns()
  
  def debug_single_case(self, n, factors, case_type):
    """Debugge einen einzelnen Fall detailliert"""
    
    print(f"📊 Basic Properties:")
    print(f"  N = {n}, Factors = {factors}")
    print(f"  N mod 4 = {n % 4}, N mod 8 = {n % 8}")
    print(f"  Factor gap = {abs(factors[0] - factors[1])}")
    
    # Teste alle Basen
    for base in [2, 3, 5, 7]:
      if math.gcd(base, n) == 1:
        print(f"\n🔬 Testing Base {base}:")
        self.debug_base_resonance(base, n, case_type)
      else:
        gcd_val = math.gcd(base, n)
        print(f"\n🔬 Base {base}: GCD = {gcd_val} (trivial factor!)")
  
  def debug_base_resonance(self, base, n, case_type):
    """Debugge Resonanz für eine spezifische Basis"""
    
    # Finde Periode
    period = self.find_period(base, n)
    
    if not period:
      print(f"  ❌ No period found for base {base}")
      return
    
    print(f"  📈 Period found: r = {period}")
    
    # Berechne verschiedene ξ-Werte
    xi_values = [
      Fraction(1, 1000000),
      Fraction(1, 100000),
      Fraction(1, 10000), 
      Fraction(1, 1000),
      Fraction(1, 100),
      Fraction(1, 42),
    ]
    
    print(f"  🧮 Resonance calculations:")
    
    for xi in xi_values:
      resonance = self.calculate_resonance(period, xi)
      threshold = Fraction(1, 3)
      
      status = "✅ PASS" if resonance > threshold else "❌ FAIL"
      
      print(f"   ξ={xi}: R={float(resonance):.6f} {status}")
    
    # Omega analysis
    omega = 2 * self.pi_decimal / period
    omega_pi_diff = abs(omega - self.pi_decimal)
    
    print(f"  🌊 Omega Analysis:")
    print(f"   ω = 2π/r = {omega:.6f}")
    print(f"   π = {self.pi_decimal:.6f}")
    print(f"   |ω - π| = {omega_pi_diff:.6f}")
    
    # Ist ω nah genug an π?
    if omega_pi_diff < 0.1:
      print(f"   🎯 ω is CLOSE to π!")
    elif omega_pi_diff < 1.0:
      print(f"   ⚠️ ω is MODERATE distance from π")
    else:
      print(f"   ❌ ω is FAR from π")
    
    # Teste alternative Resonanz-Kriterien
    self.test_alternative_criteria(period, n, case_type)
  
  def calculate_resonance(self, period, xi):
    """Berechne Resonanz mit spezifischem ξ"""
    omega = Fraction(2, 1) * self.pi_fraction / Fraction(period, 1)
    diff = omega - self.pi_fraction
    diff_squared = diff * diff
    denominator = Fraction(4, 1) * xi
    exponent = -diff_squared / denominator
    score = Fraction(1, 1) / (Fraction(1, 1) + abs(exponent))
    return score
  
  def test_alternative_criteria(self, period, n, case_type):
    """Teste alternative Resonanz-Kriterien"""
    
    print(f"  🧪 Alternative Criteria:")
    
    # Kriterium 1: Periode-Größe
    if period < 100:
      print(f"   Period size: {period} < 100 ✅ GOOD")
    else:
      print(f"   Period size: {period} ≥ 100 ❌ TOO LARGE")
    
    # Kriterium 2: Period divisors
    period_factors = self.factorize_simple(period)
    small_factors = [f for f in period_factors if f <= 10]
    
    if len(small_factors) >= 2:
      print(f"   Period factors: {period_factors} ✅ HAS SMALL FACTORS")
    else:
      print(f"   Period factors: {period_factors} ❌ NO SMALL FACTORS")
    
    # Kriterium 3: N mod period
    n_mod_period = n % period
    if n_mod_period < period // 4:
      print(f"   N mod period: {n_mod_period} ✅ SMALL REMAINDER")
    else:
      print(f"   N mod period: {n_mod_period} ❌ LARGE REMAINDER")
  
  def find_period(self, base, n, max_period=1000):
    """Finde Periode für base^r ≡ 1 (mod n)"""
    for r in range(1, min(n, max_period)):
      if pow(base, r, n) == 1:
        return r
    return None
  
  def factorize_simple(self, n):
    """Einfache Faktorisierung"""
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
  
  def analyze_patterns(self):
    """Analysiere Patterns zwischen Working und Problem Cases"""
    
    print(f"\n{'='*80}")
    print("🧠 PATTERN ANALYSIS - Was unterscheidet Working von Problem Cases?")
    print(f"{'='*80}")
    
    # Modulare Arithmetik Patterns
    print(f"\n📊 Modular Arithmetic Patterns:")
    
    working_cases = [(77, "N mod 4 = 1"), (221, "N mod 4 = 1"), (667, "N mod 4 = 3")]
    problem_cases = [(143, "N mod 4 = 3"), (323, "N mod 4 = 3"), (1517, "N mod 4 = 1"), (2491, "N mod 4 = 3")]
    
    print(f"  WORKING CASES:")
    for n, pattern in working_cases:
      print(f"   N={n}: {pattern}")
    
    print(f"  PROBLEM CASES:")
    for n, pattern in problem_cases:
      print(f"   N={n}: {pattern}")
    
    # Period Analysis
    print(f"\n📈 Period Size Analysis:")
    print("  (Hypothesis: Smaller periods = better resonance)")
    
    # GCD Analysis
    print(f"\n🔗 GCD Analysis:")
    print("  (Some T0 'successes' are actually trivial GCD finds)")
    
    working_gcd_cases = []
    working_period_cases = []
    
    for n in [77, 221, 667, 21, 35]:
      factors = self.factorize_simple(n)
      if len(factors) == 2:
        # Check if any base has GCD > 1
        has_trivial = False
        for base in [2, 3, 5, 7]:
          if math.gcd(base, n) > 1:
            has_trivial = True
            working_gcd_cases.append(n)
            break
        
        if not has_trivial:
          working_period_cases.append(n)
    
    print(f"  Working via GCD: {working_gcd_cases}")
    print(f"  Working via Periods: {working_period_cases}")
    
    print(f"\n🎯 KEY INSIGHTS:")
    print("  1. Many T0 'successes' are actually trivial GCD finds")
    print("  2. True period-based successes are rare")
    print("  3. ω ≈ π condition seems irrelevant")
    print("  4. Alternative resonance criteria needed")

def main():
  debugger = T0ResonanceDebugger()
  debugger.debug_resonance_calculation()
  
  print(f"\n{'='*80}")
  print("💡 REVOLUTIONARY HYPOTHESIS:")
  print("  T0's 'resonance' theory may be fundamentally flawed!")
  print("  The ω ≈ π condition doesn't correlate with success!")
  print("  T0 works via different mechanisms than documented!")
  print(f"{'='*80}")

if __name__ == "__main__":
  main()
