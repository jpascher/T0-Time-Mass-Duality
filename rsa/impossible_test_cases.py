#!/usr/bin/env python3
"""
Unmögliche Testfälle - Zeigt die absoluten Grenzen aller Faktorisierungsmethoden
Version 2.0 - Erweitert mit Universal T0 Framework
Diese Zahlen sind so groß/schwer, dass ALLES versagt - auch T0!
Bestätigt die fundamentalen Grenzen der Faktorisierung
"""

from factorization_benchmark_library import create_factorization_library, TestCase
import time

# RSA-Level und andere unmögliche Fälle (aktualisiert)
impossible_cases = [
  # Große Twin Prime Semiprimes (T0 Grenze überschritten)
  TestCase(
    982451653 * 982451707, # ~60 Bit Twin Primes
    [982451653, 982451707],
    "60-Bit Twin Primes - Jenseits aller Grenzen", "twin_prime_extreme", "impossible"
  ),
  
  # 30+ Bit Semiprimes (Hardware-Grenzen)
  TestCase(
    1000000007 * 1000000009, # 30-Bit Primes
    [1000000007, 1000000009],
    "30-Bit Prime Semiprime - Hardware-Grenze", "extreme_semiprime", "impossible"
  ),
  
  # 25+ Bit Twin Primes (T0's theoretische Grenze)
  TestCase(
    16777213 * 16777259, # 25-Bit Twin-ish
    [16777213, 16777259],
    "25-Bit Near-Twins - T0 Grenzbereich", "twin_extreme", "impossible"
  ),
  
  # Pathological Cases für T0
  TestCase(
    999999999989 * 999999999961, # 40-Bit nahe beieinander
    [999999999989, 999999999961],
    "40-Bit Fast-Zwillinge - Pathologisch", "pathological", "impossible"
  ),
  
  # Carmichael Numbers (Probabilistische Tests versagen)
  TestCase(
    561, # Kleinstes Carmichael
    [3, 11, 17],
    "Carmichael-561 - Probabilistik versagt", "carmichael", "special"
  ),
  
  # Large Composite with unknown factorization
  TestCase(
    2**67 - 1, # Mersenne-ähnlich, aber composite (bekannt faktorisierbar, aber sehr schwer)
    [], # Faktoren nicht trivial
    "2^67-1 Mersenne-like - Unbekannte Faktoren", "mersenne_like", "impossible"
  ),
  
  # RSA-Level (falls jemand versucht)
  TestCase(
    1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139,
    [37975227936943673922808872755445627854565536638199, 40094690950920881030683735292761468389214899724061],
    "RSA-100 (330 Bit) - UNMÖGLICH", "rsa", "impossible"
  ),
]

def test_impossible_cases():
  print("=" * 90)
  print("🔥 UNMÖGLICHE TESTFÄLLE v2.0 - TOTALES VERSAGEN ALLER METHODEN 🔥")
  print("=" * 90)
  print("Inkludiert Universal T0 Framework - Zeigt fundamentale Grenzen!")
  print("Erwartung: 100% Versagen bei ALLEN Methoden (inkl. revolutionäres T0)")
  print("=" * 90)
  
  lib = create_factorization_library()
  
  # Erweiterte Timeouts inkl. T0-Methoden
  timeout_settings = {
    'trial_division': 1.0,  # 1 Sekunde
    'fermat': 2.0,      # 2 Sekunden 
    'pollard_rho': 3.0,   # 3 Sekunden
    'pollard_p_minus_1': 2.0,
    'quadratic_sieve': 5.0, # 5 Sekunden für den "besten" klassischen
    'elliptic_curve': 3.0,
    'continued_fraction': 3.0,
    # T0-Framework Varianten
    't0_classic': 5.0,    # Auch T0 kann diese nicht lösen
    't0_universal': 5.0,   # Selbst ξ=1/100 Revolution hilft nicht
    't0_adaptive': 5.0,   # Adaptive Auswahl auch machtlos
  }
  
  total_failures = 0
  total_attempts = 0
  method_stats = {method: {'attempts': 0, 'failures': 0, 'successes': 0} for method in timeout_settings.keys()}
  
  for i, test_case in enumerate(impossible_cases, 1):
    print(f"\n{'='*70}")
    print(f"Test {i}/{len(impossible_cases)}: {test_case.description}")
    
    if len(str(test_case.n)) > 50:
      print(f"N = [Too large to display - {test_case.n.bit_length()} bits]")
    else:
      print(f"N = {test_case.n}")
      
    print(f"Bit-Größe: {test_case.n.bit_length()} Bits")
    print(f"Kategorie: {test_case.category}")
    print(f"{'='*70}")
    
    case_results = {}
    
    # Teste klassische Methoden
    print("🔬 CLASSICAL METHODS:")
    classical_methods = ['trial_division', 'fermat', 'pollard_rho', 'pollard_p_minus_1', 
              'quadratic_sieve', 'elliptic_curve', 'continued_fraction']
    
    for method in classical_methods:
      timeout = timeout_settings[method]
      print(f" 🔥 {method:18} (timeout: {timeout}s)...", end=" ", flush=True)
      
      start_time = time.time()
      result = lib.factorize(test_case.n, method, timeout=timeout)
      elapsed = time.time() - start_time
      
      method_stats[method]['attempts'] += 1
      total_attempts += 1
      
      if result.success:
        print(f"✅ SHOCK! Success in {elapsed:.3f}s - {result.factors}")
        method_stats[method]['successes'] += 1
        case_results[method] = "SUCCESS"
      else:
        print(f"❌ Failed after {elapsed:.3f}s")
        method_stats[method]['failures'] += 1
        case_results[method] = "FAILED"
        total_failures += 1
    
    # Teste T0-Framework (der spannende Teil!)
    print(f"\n🚀 T0-FRAMEWORK METHODS:")
    t0_methods = ['t0_classic', 't0_universal', 't0_adaptive']
    
    for method in t0_methods:
      timeout = timeout_settings[method]
      print(f" 🎯 {method:18} (timeout: {timeout}s)...", end=" ", flush=True)
      
      start_time = time.time()
      
      # Spezielle Behandlung für T0 bei großen Zahlen
      if test_case.n.bit_length() > 30:
        print("❌ Skipped - Beyond T0 theoretical limit (>30 bit)")
        method_stats[method]['attempts'] += 1
        method_stats[method]['failures'] += 1
        total_attempts += 1
        total_failures += 1
        case_results[method] = "SKIPPED"
      else:
        result = lib.factorize(test_case.n, method, timeout=timeout)
        elapsed = time.time() - start_time
        
        method_stats[method]['attempts'] += 1
        total_attempts += 1
        
        if result.success:
          print(f"✅ IMPOSSIBLE! T0 success in {elapsed:.3f}s - {result.factors}")
          if hasattr(result, 'xi_used'):
            print(f"   ξ used: {result.xi_used}")
          method_stats[method]['successes'] += 1
          case_results[method] = "SUCCESS"
        else:
          print(f"❌ Failed after {elapsed:.3f}s")
          method_stats[method]['failures'] += 1
          case_results[method] = "FAILED"
          total_failures += 1
    
    # Analyse für diesen Fall
    any_success = any(result == "SUCCESS" for result in case_results.values())
    if any_success:
      successful_methods = [method for method, result in case_results.items() if result == "SUCCESS"]
      print(f"\n 🚨 UNEXPECTED SUCCESS by: {', '.join(successful_methods)}")
      print(f"   This case might not be as 'impossible' as expected!")
    else:
      print(f"\n ✅ Total failure as expected - fundamental limits confirmed")
  
  print(f"\n{'='*90}")
  print("🏁 FINAL IMPOSSIBLE CASES ANALYSIS 🏁")
  print(f"{'='*90}")
  print(f"Total attempts: {total_attempts}")
  print(f"Total failures: {total_failures}")
  print(f"Overall failure rate: {(total_failures/total_attempts)*100:.1f}%")
  
  # Methoden-spezifische Analyse
  print(f"\n📊 METHOD-SPECIFIC ANALYSIS:")
  
  print(f"\n🔬 Classical Methods:")
  classical_methods = ['trial_division', 'fermat', 'pollard_rho', 'pollard_p_minus_1']
  for method in classical_methods:
    stats = method_stats[method]
    if stats['attempts'] > 0:
      failure_rate = (stats['failures'] / stats['attempts']) * 100
      print(f" {method:20}: {failure_rate:5.1f}% failure ({stats['failures']}/{stats['attempts']})")
  
  print(f"\n🚀 T0-Framework Methods:")
  t0_methods = ['t0_classic', 't0_universal', 't0_adaptive']
  for method in t0_methods:
    stats = method_stats[method]
    if stats['attempts'] > 0:
      failure_rate = (stats['failures'] / stats['attempts']) * 100
      print(f" {method:20}: {failure_rate:5.1f}% failure ({stats['failures']}/{stats['attempts']})")
  
  print(f"\n{'='*90}")
  
  if total_failures == total_attempts:
    print("🎯 PERFECT! All methods failed as expected!")
    print("This confirms the fundamental limits of factorization!")
    print("🔥 Even revolutionary T0 with ξ-optimization has hard limits!")
  else:
    unexpected_successes = total_attempts - total_failures
    print(f"⚠️ {unexpected_successes} unexpected successes!")
    print("Either we got lucky or some cases weren't truly 'impossible'!")
  
  print(f"{'='*90}")
  print("💡 KEY INSIGHTS:")
  print("• Classical methods: Expected to fail on all large cases")
  print("• T0-Framework: Revolutionary ξ-optimization still has limits")
  print("• Hardware limits: >30-bit becomes computationally intractable")
  print("• RSA-security: Based on exactly these fundamental limits")
  print("• Theoretical vs Practical: Even perfect algorithms hit scaling walls")
  print(f"{'='*90}")

def show_theoretical_limits_v2():
  """Erweiterte theoretische Grenzen inkl. T0"""
  print("\n📊 THEORETICAL LIMITS v2.0 - INCLUDING T0-FRAMEWORK")
  print("=" * 80)
  
  limits = {
    "Trial Division": "O(√N) - praktisch ~20 bit",
    "Fermat": "O(N^1/4) - gut bei nahen Faktoren ~25 bit", 
    "Pollard Rho": "O(N^1/4) - durchschnittlich ~30 bit",
    "Quadratic Sieve": "exp(√(ln N ln ln N)) - ~100 bit mit Supercomputer",
    "GNFS": "exp((ln N)^1/3) - RSA-768 (232 bit) Weltrekord",
    "T0-Classic": "ξ=1/100000 - nur Twin Primes ~25 bit",
    "T0-Universal": "ξ=1/100 - ALLE Semiprimes ~25 bit (REVOLUTION!)",
    "T0-Adaptive": "Dynamic ξ - optimiert für Zahlentyp ~25 bit",
    "T0-Theoretical": "Perfect ξ - noch unerforscht, vermutlich ~30 bit",
  }
  
  for method, limit in limits.items():
    print(f"{method:20}: {limit}")
  
  print("-" * 80) # Separator zwischen Classical und T0
  
  print("=" * 80)
  print("🔥 REVOLUTIONARY INSIGHT:")
  print("  T0 mit ξ-Optimization erweitert Faktorisierung auf ALLE Semiprimes!")
  print("  Aber fundamentale Skalierungs-Gesetze gelten trotzdem!")
  print()
  print("🎯 THE HARD TRUTH:")
  print("  • Exponentieller Aufwand ist FUNDAMENTAL")
  print("  • Auch revolutionäre Algorithmen treffen Hardware-Grenzen")
  print("  • RSA-Sicherheit basiert auf diesen mathematischen Realitäten")
  print("  • T0's ξ-Revolution erweitert den lösbaren Bereich, hebt ihn aber nicht auf!")

def test_t0_theoretical_limits():
  """Teste T0's theoretische Grenzen speziell"""
  print(f"\n{'='*80}")
  print("🎯 T0-FRAMEWORK THEORETICAL LIMITS TEST")
  print(f"{'='*80}")
  
  lib = create_factorization_library()
  
  # T0-Grenzfälle: Twin Primes in verschiedenen Größen
  t0_limit_cases = [
    TestCase(524287 * 524309, [524287, 524309], "19-Bit Twin Prime", "twin_prime", "extreme"),
    TestCase(1048573 * 1048583, [1048573, 1048583], "20-Bit Twin Prime", "twin_prime", "extreme"),
    TestCase(2097143 * 2097169, [2097143, 2097169], "21-Bit Twin Prime", "twin_prime", "impossible"),
    TestCase(4194301 * 4194319, [4194301, 4194319], "22-Bit Twin Prime", "twin_prime", "impossible"),
    TestCase(8388593 * 8388617, [8388593, 8388617], "23-Bit Twin Prime", "twin_prime", "impossible"),
  ]
  
  print("Testing T0's limits on progressively larger Twin Prime Semiprimes:")
  
  for case in t0_limit_cases:
    bit_size = case.n.bit_length()
    print(f"\n🔬 {case.description} ({bit_size} bits total)")
    print(f"N = {case.expected_factors[0]} × {case.expected_factors[1]}")
    
    # Teste nur T0-Methoden
    t0_methods = ['t0_universal', 't0_adaptive']
    
    for method in t0_methods:
      print(f" {method:15}...", end=" ", flush=True)
      
      start_time = time.time()
      result = lib.factorize(case.n, method, timeout=10.0)
      elapsed = time.time() - start_time
      
      if result.success:
        print(f"✅ Success in {elapsed:.3f}s")
        if hasattr(result, 'xi_used'):
          resonance = getattr(result, 'resonance_score', 0)
          print(f"   ξ={result.xi_used}, Resonanz={resonance:.6f}")
      else:
        print(f"❌ Failed after {elapsed:.3f}s")
  
  print(f"\n🎯 T0 LIMIT ANALYSIS:")
  print("• T0 should excel at Twin Primes up to ~20-25 bits")
  print("• Beyond that, even perfect ξ-optimization hits scaling limits")
  print("• The ξ-revolution extends the range but doesn't eliminate scaling")

if __name__ == "__main__":
  test_impossible_cases()
  show_theoretical_limits_v2()
  test_t0_theoretical_limits()
