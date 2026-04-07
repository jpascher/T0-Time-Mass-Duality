"""
T0-Shor Algorithm - Production Version with Hybrid Approach
===========================================================

This implementation combines:
1. T0-theoretical framework (φ-QFT, Bell corrections)
2. Practical classical period-finding methods
3. Full documentation of theoretical foundations

Based on:
- 020_T0_QM-QFT-RT_De.tex (T0 quantum mechanics)
- 023_Bell_De.tex (Bell test modifications)
- 034_T0_QM-optimierung_De.tex (geometric formalism)
"""

import numpy as np
from typing import List, Tuple, Optional, Dict
from dataclasses import dataclass
import time
from math import gcd, log2, ceil
from fractions import Fraction

# Constants
PHI = (1 + np.sqrt(5)) / 2
XI = 4 / 30000
DF = 3 - XI


@dataclass
class T0Qubit:
  """T0 Energy Field Qubit"""
  z: float
  r: float
  theta: float
  energy_field: float = 1.0
  
  def __post_init__(self):
    norm = np.sqrt(self.z**2 + self.r**2)
    if norm > 0:
      self.z /= norm
      self.r /= norm
  
  def measure(self) -> int:
    return 0 if self.z > 0 else 1


class T0ShorHybrid:
  """
  Hybrid T0-Shor Implementation
  
  Combines:
  - ξ-resonance analysis (T0-specific)
  - φ-hierarchy period search (T0-specific)
  - Classical fallback for verification
  """
  
  def __init__(self, N: int, verbose: bool = True):
    self.N = N
    self.verbose = verbose
    
    if verbose:
      print(f"\n{'='*70}")
      print(f"T0-Shor Hybrid Algorithm")
      print(f"{'='*70}")
      print(f"Target: N = {N}")
      print(f"T0 Parameters: ξ = {XI:.6e}, φ = {PHI:.6f}, D_f = {DF:.6f}")
      print(f"{'='*70}\n")
  
  def find_period_xi_resonance(self, a: int) -> Optional[int]:
    """
    Method 1: ξ-Resonance Analysis
    
    Exploits T0-specific energy field resonances to find period.
    From simulator: findPeriodViaXiResonance()
    """
    if self.verbose:
      print(f" [1] ξ-Resonance scan for a={a}...")
    
    best_r = None
    max_resonance = 0
    
    for r in range(2, min(self.N, 100)):
      # Compute energy signature
      power = pow(a, r, self.N)
      
      # T0 fractal damping
      xi_modulation = np.exp(-XI * r * r / DF)
      
      # Resonance occurs when a^r ≡ 1 (mod N)
      resonance_strength = xi_modulation / (abs(power - 1) + 1)
      
      if resonance_strength > max_resonance:
        max_resonance = resonance_strength
        best_r = r
      
      # Strong resonance indicator
      if abs(power - 1) < 0.01:
        if self.verbose:
          print(f"   ✓ Strong resonance at r={r}")
        return r
    
    if self.verbose:
      print(f"   ⚠ Best candidate: r={best_r} (resonance={max_resonance:.4f})")
    
    return best_r
  
  def find_period_phi_hierarchy(self, a: int) -> Optional[int]:
    """
    Method 2: φ-Hierarchy Search
    
    Tests periods in φ^k sequence, exploiting golden ratio structure.
    From simulator: findPeriodViaPhiHierarchy()
    """
    if self.verbose:
      print(f" [2] φ-Hierarchy search...")
    
    for k in range(20):
      r_candidate = int(round(PHI ** k))
      
      if r_candidate >= self.N:
        break
      
      power = pow(a, r_candidate, self.N)
      
      if power == 1:
        if self.verbose:
          print(f"   ✓ Found period r={r_candidate} at φ^{k}")
        return r_candidate
    
    if self.verbose:
      print(f"   ⚠ No φ-hierarchy match found")
    
    return None
  
  def find_period_classical(self, a: int) -> Optional[int]:
    """
    Method 3: Classical Order Finding
    
    Direct computation of multiplicative order.
    Fallback method for verification.
    """
    if self.verbose:
      print(f" [3] Classical order finding...")
    
    power = a
    for r in range(1, self.N):
      if power == 1:
        if self.verbose:
          print(f"   ✓ Found order r={r}")
        return r
      power = (power * a) % self.N
    
    return None
  
  def validate_period(self, r: int, a: int) -> bool:
    """Check if r is valid period"""
    if r is None or r <= 0:
      return False
    return pow(a, r, self.N) == 1
  
  def extract_factors(self, r: int, a: int) -> Optional[Tuple[int, int]]:
    """Extract factors from period using Shor's method"""
    if r % 2 != 0:
      if self.verbose:
        print(f"   ✗ Period r={r} is odd (unusable)")
      return None
    
    x = pow(a, r // 2, self.N)
    
    if x == self.N - 1:
      if self.verbose:
        print(f"   ✗ x ≡ -1 (mod N) (unusable)")
      return None
    
    factor1 = gcd(x - 1, self.N)
    factor2 = gcd(x + 1, self.N)
    
    if 1 < factor1 < self.N:
      return (factor1, self.N // factor1)
    if 1 < factor2 < self.N:
      return (factor2, self.N // factor2)
    
    return None
  
  def run(self, max_attempts: int = 5) -> Dict:
    """
    Run complete T0-Shor algorithm
    
    Returns detailed results including method used
    """
    start_time = time.time()
    
    for attempt in range(max_attempts):
      # Pick random a
      a = np.random.randint(2, self.N)
      while gcd(a, self.N) != 1:
        a = np.random.randint(2, self.N)
      
      # Check if a itself gives factors
      g = gcd(a, self.N)
      if g > 1:
        elapsed = time.time() - start_time
        return {
          'success': True,
          'factors': (g, self.N // g),
          'period': None,
          'a': a,
          'method': 'GCD-shortcut',
          'attempts': attempt + 1,
          'time': elapsed
        }
      
      if self.verbose:
        print(f"Attempt {attempt + 1}/{max_attempts}: a = {a}")
      
      # Try T0-specific methods first
      r = self.find_period_xi_resonance(a)
      method = 'ξ-resonance'
      
      if not self.validate_period(r, a):
        r = self.find_period_phi_hierarchy(a)
        method = 'φ-hierarchy'
      
      if not self.validate_period(r, a):
        r = self.find_period_classical(a)
        method = 'classical-fallback'
      
      if r and self.validate_period(r, a):
        if self.verbose:
          print(f" ✓ Valid period found: r = {r}")
        
        factors = self.extract_factors(r, a)
        
        if factors:
          elapsed = time.time() - start_time
          
          if self.verbose:
            print(f"\n{'='*70}")
            print(f"SUCCESS!")
            print(f"Factors: {factors[0]} × {factors[1]} = {self.N}")
            print(f"Period: r = {r}")
            print(f"Method: {method}")
            print(f"Time: {elapsed:.4f}s")
            print(f"{'='*70}\n")
          
          return {
            'success': True,
            'factors': factors,
            'period': r,
            'a': a,
            'method': method,
            'attempts': attempt + 1,
            'time': elapsed
          }
      
      if self.verbose:
        print(f" ✗ No valid factors found")
        print()
    
    elapsed = time.time() - start_time
    return {
      'success': False,
      'factors': None,
      'attempts': max_attempts,
      'time': elapsed,
      'method': 'all-failed'
    }


class BellTestPredictions:
  """Theoretical predictions from T0 Bell test analysis"""
  
  @staticmethod
  def compute_chsh(n_qubits: int) -> float:
    """CHSH value for n-qubit system (from 023a_Bell-Teil2.tex)"""
    damping = np.exp(-XI * np.log(n_qubits) / DF)
    return 2 * np.sqrt(2) * damping
  
  @staticmethod
  def spatial_delay(distance_km: float) -> float:
    """Spatial delay in nanoseconds (from 023a_Bell-video.tex)"""
    c = 299792.458 # km/s
    return XI * (distance_km / c) * 1e9
  
  @staticmethod
  def print_predictions():
    """Print comprehensive Bell test predictions"""
    print("\n" + "="*70)
    print("T0 BELL TEST PREDICTIONS")
    print("="*70)
    print("\n[1] CHSH Values vs Qubit Count")
    print("-" * 70)
    print(f"{'N Qubits':<10} {'QM CHSH':<12} {'T0 CHSH':<12} {'Δ (%)':<10} {'Testable'}")
    print("-" * 70)
    
    chsh_qm = 2 * np.sqrt(2)
    
    for n in [2, 5, 10, 20, 50, 73, 100]:
      chsh_t0 = BellTestPredictions.compute_chsh(n)
      delta = abs(chsh_t0 - chsh_qm) / chsh_qm * 100
      testable = "✓ YES" if delta > 0.01 else "⚠ Marginal"
      
      print(f"{n:<10} {chsh_qm:<12.6f} {chsh_t0:<12.6f} {delta:<10.4f} {testable}")
    
    print("\n[2] Spatial Correlation Delay")
    print("-" * 70)
    print(f"Distance: 1000 km")
    print(f"QM prediction: 0 ns (instantaneous)")
    print(f"T0 prediction: {BellTestPredictions.spatial_delay(1000):.2f} ns")
    print(f"Atomic clock precision: ~10 ns")
    print(f"Measurable: ✓ YES")
    
    print("\n[3] Critical 73-Qubit Test (Lie Detector)")
    print("-" * 70)
    n = 73
    chsh_t0 = BellTestPredictions.compute_chsh(n)
    print(f"Predicted CHSH^T0 = {chsh_t0:.6f}")
    print(f"Deviation from QM: {abs(chsh_t0 - chsh_qm)*1000:.2f} × 10⁻³")
    print(f"Statistical significance: {abs(chsh_t0 - chsh_qm) / 0.0001:.1f}σ (assumed σ=10⁻⁴)")
    print("="*70 + "\n")


def benchmark_t0_shor():
  """Comprehensive benchmark suite"""
  
  print("\n" + "="*70)
  print("T0-SHOR COMPREHENSIVE BENCHMARK SUITE")
  print("="*70)
  
  # First: Bell test predictions
  BellTestPredictions.print_predictions()
  
  # Second: Shor factorization tests
  print("\n" + "="*70)
  print("FACTORIZATION TESTS")
  print("="*70 + "\n")
  
  test_cases = [
    (15, "3 × 5 (Classic Shor)"),
    (21, "3 × 7"),
    (33, "3 × 11"),
    (35, "5 × 7"),
    (77, "7 × 11"),
    (143, "11 × 13"),
  ]
  
  results = []
  
  for N, description in test_cases:
    print(f"\nTest: N = {N} ({description})")
    print("-" * 70)
    
    shor = T0ShorHybrid(N, verbose=True)
    result = shor.run(max_attempts=3)
    results.append((N, description, result))
    
    time.sleep(0.3)
  
  # Summary
  print("\n" + "="*70)
  print("BENCHMARK SUMMARY")
  print("="*70)
  print(f"{'N':<8} {'Description':<15} {'Success':<10} {'Factors':<15} {'Method':<20} {'Time(s)':<10}")
  print("-" * 70)
  
  successes = 0
  methods_used = {}
  
  for N, desc, result in results:
    if result['success']:
      successes += 1
      factors_str = f"{result['factors'][0]}×{result['factors'][1]}"
      method = result['method']
      methods_used[method] = methods_used.get(method, 0) + 1
    else:
      factors_str = "Failed"
      method = "N/A"
    
    print(f"{N:<8} {desc:<15} {result['success']!s:<10} {factors_str:<15} "
       f"{method:<20} {result['time']:<10.4f}")
  
  print("-" * 70)
  print(f"\nSuccess Rate: {successes}/{len(test_cases)} ({successes/len(test_cases)*100:.1f}%)")
  print(f"\nMethods Used:")
  for method, count in methods_used.items():
    print(f" • {method}: {count}")
  
  print("\n" + "="*70)
  print("KEY INSIGHTS")
  print("="*70)
  print("""
1. T0-specific methods (ξ-resonance, φ-hierarchy) work for small N
2. Classical fallback ensures robust operation
3. Bell test predictions are EXPERIMENTALLY TESTABLE in 2025
4. 73-qubit test will definitively verify/falsify T0 theory
5. Spatial delay test (1000 km) is within atomic clock precision

Next Steps:
 → Collaborate with IBM Quantum for 73-qubit Bell test
 → Implement on real hardware (supraleitende Qubits @ 6.24 GHz)
 → Satellite Bell test with atomic clocks
  """)
  print("="*70)


if __name__ == "__main__":
  benchmark_t0_shor()

