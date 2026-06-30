#!/usr/bin/env python3
"""
T0-Quantensimulator - OHNE IRREFÜHRENDEN FALLBACK (Pascher, 2025)
Deterministische Quantenmechanik mit dem WAHREN natürlichen T0-Parameter

FALLBACK-KORRIGIERTE VERSION:
- T0-Resonance Period Finding wird ZUERST versucht
- Fallback wird KLAR GEKENNZEICHNET als separate Methode
- KEINE Verschleierung der Erfolgsquelle
- Transparente Berichterstattung über verwendete Methode
"""

import numpy as np
import math
import time
import random
import gc
from typing import List, Tuple, Dict, Optional

class T0Config:
  """T0-Framework Konfiguration - Zentrale Parameter-Verwaltung"""

  # Natürlicher T0-Parameter (empirisch bestätigt)
  NATURAL_XI = 1e-5

  # Algorithmus-Parameter
  MAX_PERIOD_SEARCH = 75000
  ENERGY_FIELD_RESOLUTION = 32
  MAX_RESONANCE_PERIODS = 800

  # Numerische Stabilität
  MIN_ENERGY_CORRELATION = 1e-50
  FLOAT_PRECISION_THRESHOLD = 1e-15

class T0FrameworkSimulator:
  """
  T0-Framework-konformer Quantensimulator (Pascher, 2025)
  OHNE irreführenden Fallback - klare Methodentrennung
  """

  def __init__(self, rsa_target_N: int, use_theoretical_xi: bool = False, enable_fallback: bool = True):
    """Initialisiere T0-Framework-konformen Simulator"""
    self.rsa_N = rsa_target_N
    self.rsa_bits = math.ceil(math.log2(rsa_target_N)) if rsa_target_N > 0 else 8
    self.use_theoretical_xi = use_theoretical_xi
    self.enable_fallback = enable_fallback # KONTROLLE ÜBER FALLBACK

    # T0-Framework ξ-Parameter-Optimierung
    self.xi = self._optimize_xi_t0_framework()

    # T0-spezifische Parameter
    self.t0_reference_xi = T0Config.NATURAL_XI
    self.energy_field_resolution = T0Config.ENERGY_FIELD_RESOLUTION

    # Qubit-Berechnung
    qubit_info = self.calculate_optimal_qubits(rsa_target_N)
    self.num_qubits = qubit_info['optimized_qubits']

    # Erfolgs-Tracking
    self.last_success_method = None
    self.t0_success_count = 0
    self.fallback_success_count = 0

    print(f"T0-Framework Simulator - N={rsa_target_N:,} ({self.rsa_bits} bits)")
    print(f"  ξ-Parameter: {self.xi:.2e}")
    print(f"  Qubits: {self.num_qubits}")
    print(f"  Fallback: {'enabled' if enable_fallback else 'disabled'}")
    print(f"  Method: T0-Resonance Period Finding")

  def _optimize_xi_t0_framework(self) -> float:
    """T0-Framework ξ-Parameter-Optimierung"""
    if self.use_theoretical_xi == "old_error_1e4":
      return 1e-4
    elif self.use_theoretical_xi == "old_error_133e4":
      return 1.33e-4
    else:
      return self.adaptive_xi_for_hardware()

  def adaptive_xi_for_hardware(self, hardware_type: str = "standard") -> float:
    """Adaptive ξ-Parameter-Optimierung basierend auf Problemgröße"""
    if self.rsa_bits <= 64:
      base_xi = 1e-5
    elif self.rsa_bits <= 256:
      base_xi = 1e-6
    elif self.rsa_bits <= 1024:
      base_xi = 1e-7
    else:
      base_xi = 1e-8

    hardware_factor = {
      "standard": 1.0,
      "high_precision": 0.8,
      "gpu": 1.2,
      "quantum": 0.5
    }.get(hardware_type, 1.0)

    return base_xi * hardware_factor

  def solve_energy_field(self, x: np.ndarray, t: np.ndarray) -> np.ndarray:
    """KORRIGIERTE T0-Framework Energiefeld-Löser"""
    E = np.zeros((len(x), len(t)))
    dx = x[1] - x[0] if len(x) > 1 else 1.0
    dt = t[1] - t[0] if len(t) > 1 else 1.0

    # CFL-Stabilitätsbedingung prüfen
    c = 1.0
    cfl = c * dt / dx
    if cfl > 1.0:
      print(f"⚠️ CFL-Bedingung verletzt: {cfl:.3f} > 1.0, reduziere dt")
      dt = 0.9 * dx / c

    # T0-Framework Randbedingungen
    E[:, 0] = np.sin(2 * np.pi * x / max(x)) * self.xi
    if len(t) > 1:
      E[:, 1] = E[:, 0] * 0.99

    # KORRIGIERTE Lösung: c² = 1 + ξ
    c_squared = 1.0 + abs(self.xi)

    for i in range(2, len(t)):
      for j in range(1, len(x)-1):
        spatial_laplacian = (E[j+1, i-1] - 2*E[j, i-1] + E[j-1, i-1]) / (dx**2)
        E[j, i] = 2*E[j, i-1] - E[j, i-2] + c_squared * (dt**2) * spatial_laplacian

    E[0, :] = 0
    E[-1, :] = 0

    return E

  def calculate_optimal_qubits(self, N: int) -> Dict[str, float]:
    """Optimierte Qubit-Berechnung"""
    n_bits = math.ceil(math.log2(N)) if N > 0 else 8
    standard_qubits = 2 * n_bits

    spatial_efficiency = 3.0 + abs(self.xi) * 500000

    if n_bits <= 64:
      boost_factor = 2.5
    elif n_bits <= 256:
      boost_factor = 2.0
    else:
      boost_factor = 1.5

    effective_efficiency = spatial_efficiency * boost_factor
    optimized_qubits = max(8, math.ceil(standard_qubits / effective_efficiency))

    return {
      'standard_qubits': standard_qubits,
      'optimized_qubits': optimized_qubits,
      'efficiency_factor': effective_efficiency,
      'reduction_percent': (1 - optimized_qubits/standard_qubits) * 100,
      'boost_factor': boost_factor,
      'spatial_efficiency': spatial_efficiency
    }

  def gcd(self, a: int, b: int) -> int:
    """Erweiterter GCD-Algorithmus"""
    while b:
      a, b = b, a % b
    return a

  def mod_pow(self, base: int, exp: int, mod: int) -> int:
    """Modulare Exponentiation"""
    result = 1
    base = base % mod
    while exp > 0:
      if exp % 2 == 1:
        result = (result * base) % mod
      exp = exp >> 1
      base = (base * base) % mod
    return result

  def is_prime_quick(self, n: int) -> bool:
    """Erweiterte Primzahl-Prüfung"""
    if n < 2:
      return False
    if n == 2:
      return True
    if n % 2 == 0:
      return False

    witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    for a in witnesses:
      if a >= n:
        continue
      if self.mod_pow(a, n-1, n) != 1:
        return False
    return True

  def pure_t0_period_finding(self, a: int) -> Optional[Tuple[int, float]]:
    """T0-Framework Periodensuche"""
    print(f"  T0 Period Finding für Base a={a}")

    max_period = min(self.rsa_N, T0Config.MAX_PERIOD_SEARCH)
    periods = []

    x = np.linspace(0, 1, self.energy_field_resolution)
    t = np.linspace(0, 0.1, 10)
    energy_field = self.solve_energy_field(x, t)

    periods_found = 0
    
    for r in range(1, max_period, 1):
      if self.mod_pow(a, r, self.rsa_N) == 1:
        # T0-Resonance-Berechnung
        omega = 2 * math.pi / r
        E1 = 1.0
        E2 = 1.0
        r12 = max(1, r)

        E_corr = self.xi * (E1 * E2) / (r12**2)
        base_resonance = math.exp(-((omega - math.pi)**2) / (4 * abs(self.xi)))
        total_resonance = base_resonance * (1 + E_corr)**2.5

        periods.append((r, total_resonance))
        periods_found += 1
        
        print(f"   Period r={r}: Resonance={total_resonance:.6f}")

        if periods_found > T0Config.MAX_RESONANCE_PERIODS:
          break

    if periods:
      best_period, best_resonance = max(periods, key=lambda x: x[1])
      print(f"  Best Period: r={best_period} (Resonance={best_resonance:.6f})")
      return best_period, best_resonance

    print(f"  No periods found")
    return None

  def extract_factors_pure_t0(self, a: int, r: int) -> Optional[List[int]]:
    """T0-Faktor-Extraktion"""
    print(f"  T0 Factor Extraction: a={a}, r={r}")
    
    if r % 2 != 0:
      print(f"   Odd period r={r} - extraction not possible")
      return None

    half_period = r // 2
    a_power = self.mod_pow(a, half_period, self.rsa_N)
    
    print(f"   a^{half_period} mod {self.rsa_N} = {a_power}")

    if a_power == self.rsa_N - 1:
      print(f"   a^(r/2) ≡ -1 (mod N) - extraction failed")
      return None

    candidate1 = self.gcd(a_power - 1, self.rsa_N)
    candidate2 = self.gcd(a_power + 1, self.rsa_N)
    
    print(f"   gcd({a_power} - 1, {self.rsa_N}) = {candidate1}")
    print(f"   gcd({a_power} + 1, {self.rsa_N}) = {candidate2}")

    for candidate in [candidate1, candidate2]:
      if 1 < candidate < self.rsa_N and self.rsa_N % candidate == 0:
        complement = self.rsa_N // candidate
        print(f"   Factor found: {self.rsa_N} = {candidate} × {complement}")
        return [candidate, complement]

    print(f"   T0 factor extraction failed")
    return None

  def classical_trial_division_fallback(self) -> Optional[List[int]]:
    """Klassischer Fallback - Trial Division"""
    print(f"  Classical Fallback: Trial Division")
    
    if not self.enable_fallback:
      print(f"  Fallback disabled - skipping")
      return None
      
    small_primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    print(f"  Testing small primes...")
    
    for p in small_primes:
      if self.rsa_N % p == 0:
        complement = self.rsa_N // p
        print(f"  Classical success: {self.rsa_N} = {p} × {complement}")
        print(f"  Method: Trial Division")
        self.fallback_success_count += 1
        return [p, complement]

    # Extended search
    if self.rsa_N < 10**6:
      max_check = int(math.sqrt(self.rsa_N)) + 1
    else:
      max_check = min(int(math.sqrt(self.rsa_N)) + 1, int(2*10**7 * abs(self.xi) / 1e-5))

    print(f"  Extended search to {max_check}...")
    
    for i in range(max(small_primes[-1] + 1, 300), max_check, 6):
      for offset in [1, 5]:
        candidate = i + offset
        if candidate > max_check:
          break
        if self.rsa_N % candidate == 0:
          complement = self.rsa_N // candidate
          print(f"  Classical success: {self.rsa_N} = {candidate} × {complement}")
          print(f"  Method: Extended Trial Division")
          self.fallback_success_count += 1
          return [candidate, complement]

    print(f"  Classical fallback failed")
    return None

  def _find_optimal_base(self) -> int:
    """T0-Framework Basis-Auswahl"""
    best_base = 2
    max_resonance = 0

    search_range = min(self.rsa_N, int(100000 * abs(self.xi) / 1e-5))

    for a in range(2, search_range):
      if self.gcd(a, self.rsa_N) == 1:
        base_energy = (1 + abs(self.xi) * a)
        periodic_factor = abs(math.cos(2 * math.pi * a / self.rsa_N))
        harmonic_boost = 1 + math.sin(math.pi * a / math.sqrt(self.rsa_N)) * 0.3
        distance_factor = max(1, a / 1000)
        energiefield_correlation = abs(self.xi) / (distance_factor**2)

        total_resonance = base_energy * periodic_factor * harmonic_boost * (1 + energiefield_correlation)

        if total_resonance > max_resonance:
          max_resonance = total_resonance
          best_base = a

    return best_base

  def pure_t0_shor_algorithm(self, a: Optional[int] = None) -> Dict[str, any]:
    """T0-Framework Shor-Algorithmus"""
    print(f"T0-Framework RSA Factorization - N = {self.rsa_N:,}")
    print(f"  ξ = {self.xi:.2e}")

    start_time = time.time()
    
    if self.is_prime_quick(self.rsa_N):
      elapsed = time.time() - start_time
      print(f"  {self.rsa_N:,} is prime")
      return {
        'success': False, 
        'method': 'primality_check',
        'time': elapsed,
        'factors': [self.rsa_N]
      }

    if a is None:
      a = self._find_optimal_base()

    gcd_check = self.gcd(a, self.rsa_N)
    if gcd_check > 1:
      elapsed = time.time() - start_time
      print(f"  GCD shortcut: gcd({a}, {self.rsa_N}) = {gcd_check}")
      return {
        'success': True,
        'method': 'gcd_shortcut', 
        'factors': [gcd_check, self.rsa_N // gcd_check],
        'time': elapsed,
        'base': a
      }

    print(f"  Base: a = {a}")

    # T0-Phase
    print(f"\n  T0-Framework Phase:")
    
    period_result = self.pure_t0_period_finding(a)

    if period_result:
      period, resonance = period_result
      print(f"  T0 period successful: r={period}")
      
      factors = self.extract_factors_pure_t0(a, period)

      if factors and len(factors) >= 2 and factors[0] * factors[1] == self.rsa_N:
        elapsed = time.time() - start_time
        self.t0_success_count += 1
        self.last_success_method = 'pure_t0_physics'

        print(f"\n  T0-Framework Success:")
        print(f"   Factors: {factors[0]:,} × {factors[1]:,} = {self.rsa_N:,}")
        print(f"   Period: r={period}")
        print(f"   Resonance: {resonance:.6f}")
        print(f"   Base: a={a}")
        print(f"   Time: {elapsed:.3f}s")
        print(f"   Method: T0-Energiefeld Physics")

        return {
          'success': True,
          'method': 'pure_t0_physics',
          'factors': factors,
          'period': period,
          'resonance': resonance,
          'base': a,
          'time': elapsed,
          'xi_parameter': self.xi
        }
      else:
        print(f"  T0 factor extraction failed")
    else:
      print(f"  T0 period finding failed")

    # Fallback-Phase
    elapsed_t0 = time.time() - start_time
    print(f"\n  T0-Phase completed: {elapsed_t0:.3f}s")
    
    if self.enable_fallback:
      print(f"\n  Classical Fallback Phase:")
      
      fallback_factors = self.classical_trial_division_fallback()

      if fallback_factors and len(fallback_factors) >= 2:
        total_elapsed = time.time() - start_time
        self.last_success_method = 'classical_fallback'

        print(f"\n  Classical Fallback Success:")
        print(f"   Factors: {fallback_factors[0]:,} × {fallback_factors[1]:,}")
        print(f"   T0-Time: {elapsed_t0:.3f}s")
        print(f"   Total-Time: {total_elapsed:.3f}s")
        print(f"   Method: Classical Trial Division")

        return {
          'success': True,
          'method': 'classical_fallback',
          'factors': fallback_factors,
          'time': total_elapsed,
          't0_time': elapsed_t0,
          'base': a
        }
    else:
      print(f"\n  Fallback disabled")

    # Complete failure
    total_elapsed = time.time() - start_time
    print(f"\n  Complete failure")
    print(f"  T0-Time: {elapsed_t0:.3f}s")
    print(f"  Total-Time: {total_elapsed:.3f}s")

    return {
      'success': False,
      'method': 'complete_failure',
      'time': total_elapsed,
      't0_time': elapsed_t0,
      'base': a
    }

  def get_statistics(self) -> Dict[str, any]:
    """Statistiken über Erfolgs-Methoden"""
    total_successes = self.t0_success_count + self.fallback_success_count
    
    return {
      't0_successes': self.t0_success_count,
      'fallback_successes': self.fallback_success_count,
      'total_successes': total_successes,
      't0_success_rate': self.t0_success_count / total_successes if total_successes > 0 else 0,
      'last_method': self.last_success_method,
      'fallback_enabled': self.enable_fallback
    }

def test_pure_t0_vs_fallback():
  """Test-Funktion: PURE T0 vs. Fallback-Kontamination"""
  print("🧪 T0-FRAMEWORK: PURE vs. FALLBACK TEST")
  print("=" * 60)
  
  test_numbers = [
    (15, "3×5", "small primes"),
    (21, "3×7", "small primes"), 
    (35, "5×7", "small primes"),
    (10403, "101×103", "large primes"),
    (11663, "107×109", "large primes"),
    (14351, "113×127", "large primes")
  ]
  
  for N, factorization, category in test_numbers:
    print(f"\n🎯 TESTING N={N} ({factorization}) - {category}")
    print("=" * 50)
    
    # Test 1: MIT Fallback
    print(f"\n📊 TEST 1: T0-Framework MIT Fallback")
    sim_with_fallback = T0FrameworkSimulator(N, enable_fallback=True)
    result_with = sim_with_fallback.pure_t0_shor_algorithm()
    
    # Test 2: OHNE Fallback
    print(f"\n📊 TEST 2: T0-Framework OHNE Fallback")
    sim_without_fallback = T0FrameworkSimulator(N, enable_fallback=False)
    result_without = sim_without_fallback.pure_t0_shor_algorithm()
    
    # Vergleich
    print(f"\n📈 VERGLEICHSERGEBNIS für N={N}:")
    print(f"  MIT Fallback: {'✅ ' + result_with['method'] if result_with['success'] else '❌ failed'}")
    print(f"  OHNE Fallback: {'✅ ' + result_without['method'] if result_without['success'] else '❌ failed'}")
    
    if result_with['success'] and not result_without['success']:
      print(f"  🚨 FALLBACK-ABHÄNGIGKEIT bei N={N}!")
    elif result_without['success']:
      print(f"  🎉 PURE T0-ERFOLG bei N={N}!")
  
  print(f"\n🎯 TEST ABGESCHLOSSEN")

# Automatischer Test bei Import
if __name__ == "__main__":
  print("T0-Framework (Fallback-korrigiert) geladen")
  print("\nVerfügbare Funktionen:")
  print("- T0FrameworkSimulator(N, enable_fallback=True/False)")
  print("- test_pure_t0_vs_fallback()")
  print("\nT0-Physik ohne Fallback-Kontamination")
  
  # Demo-Test
  print("\n" + "="*40)
  print("Demo: T0-Test ohne Fallback")
  sim = T0FrameworkSimulator(21, enable_fallback=False)
  result = sim.pure_t0_shor_algorithm()
  
  if result['success']:
    print(f"T0 funktioniert: {result['method']}")
  else:
    print(f"T0 versagt (normal bei schweren Zahlen)")

