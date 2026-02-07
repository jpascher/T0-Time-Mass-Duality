#!/usr/bin/env python3
"""
🔬 T0 UNIQUENESS TEST
Systematische Suche nach Cases wo NUR T0 erfolgreich ist
"""

import importlib.util
import time
import math

def load_library():
  """Lade T0-Library"""
  try:
    spec = importlib.util.spec_from_file_location(r"t0_lib", r"factorization_benchmark_library.py"
    )
    lib = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(lib)
    return lib.create_factorization_library()
  except Exception as e:
    print(f"❌ Library-Fehler: {e}")
    return None

def test_single_case(factory, n, description, expected_factors=None, timeout=2.0):
  """Teste einen einzelnen Fall mit allen Methoden"""
  
  methods = {
    'trial_division': 'Trial Division',
    'fermat': 'Fermat', 
    'pollard_rho': 'Pollard Rho',
    'pollard_p_minus_1': 'Pollard p-1',
    't0_adaptive': 'T0-Adaptive'
  }
  
  results = {}
  
  print(f"\n🧪 N={n} ({description})")
  if expected_factors:
    print(f"  Erwartete Faktoren: {expected_factors}")
  print("-" * 40)
  
  for method, label in methods.items():
    try:
      start_time = time.time()
      result = factory.factorize(n, method, timeout=timeout)
      elapsed = time.time() - start_time
      
      success = result.success
      factors = result.factors if success else None
      
      # Verifiziere Faktoren
      if success and factors:
        product = 1
        for f in factors:
          product *= f
        if product != n:
          success = False
          factors = None
      
      results[method] = {
        'success': success,
        'time': elapsed,
        'factors': factors
      }
      
      status = "✅" if success else "❌"
      time_str = f"{elapsed:.4f}s"
      factors_str = f" → {factors}" if factors else ""
      
      # T0-Details
      if method == 't0_adaptive' and success and hasattr(result, 'method_specific') and result.method_specific:
        xi_val = result.method_specific.get('xi_value', 'N/A')
        resonance = result.method_specific.get('resonance_score', 0)
        strategy = result.method_specific.get('xi_strategy', 'N/A')
        factors_str += f" [ξ={xi_val}, R={resonance:.4f}, {strategy}]"
      
      print(f" {label:>15}: {status} {time_str}{factors_str}")
      
    except Exception as e:
      print(f" {label:>15}: ❌ ERROR: {str(e)[:30]}")
      results[method] = {'success': False, 'time': timeout, 'factors': None}
  
  return results

def analyze_result(results, n, description):
  """Analysiere ob T0 einzigartig ist"""
  
  classical_methods = ['trial_division', 'fermat', 'pollard_rho', 'pollard_p_minus_1']
  
  t0_success = results.get('t0_adaptive', {}).get('success', False)
  classical_successes = [results.get(m, {}).get('success', False) for m in classical_methods]
  classical_success_count = sum(classical_successes)
  
  if t0_success and classical_success_count == 0:
    print("🚀 T0 EINZIGARTIG! Nur T0 löst diesen Fall!")
    return "t0_unique"
  elif not t0_success and classical_success_count > 0:
    print("❌ T0 versagt, Klassische erfolgreich")
    return "classical_better"
  elif t0_success and classical_success_count > 0:
    # Beide erfolgreich - Geschwindigkeitsvergleich
    t0_time = results['t0_adaptive']['time']
    successful_classical_times = [results[m]['time'] for m in classical_methods 
                  if results.get(m, {}).get('success', False)]
    best_classical_time = min(successful_classical_times) if successful_classical_times else float('inf')
    
    if t0_time < best_classical_time * 0.8:
      print(f"⚡ T0 SCHNELLER: {best_classical_time/t0_time:.2f}x")
      return "t0_faster"
    elif best_classical_time < t0_time * 0.8:
      print(f"🐌 Klassisch schneller: {t0_time/best_classical_time:.2f}x")
      return "classical_faster"
    else:
      print("🤝 Ähnliche Performance")
      return "tie"
  else:
    print("💥 ALLE versagen")
    return "all_fail"

def generate_test_cases():
  """Generiere systematische Test-Cases"""
  
  test_cases = []
  
  # 1. Bekannte T0-Stärken
  print("📋 BEKANNTE T0-STÄRKEN:")
  known_good = [
    (143, [11, 13], "Twin Prime Gap=2"),
    (221, [13, 17], "Twin Prime Gap=4"),
    (323, [17, 19], "Twin Prime Gap=2"),
    (35, [5, 7], "Einfacher Twin Prime"),
    (77, [7, 11], "Twin Prime Gap=4"),
    (1729, [7, 13, 19], "Ramanujan Number"),
    (2491, [47, 53], "Medium Cousin Prime"),
  ]
  test_cases.extend(known_good)
  
  # 2. Spezielle mathematische Zahlen
  print("📋 SPEZIELLE MATHEMATISCHE ZAHLEN:")
  special_numbers = [
    (2047, [23, 89], "Mersenne-Related 2^11-1"),
    (4181, [59, 71], "Fibonacci F19"),
    (1189, [29, 41], "Lucas-Related"),
    (1363, [29, 47], "Prime Gap=18"),
    (1517, [37, 41], "Twin Prime Gap=4"),
  ]
  test_cases.extend(special_numbers)
  
  # 3. Systematische Twin Prime Progression
  print("📋 TWIN PRIME PROGRESSION:")
  twin_primes = [
    (15, [3, 5], "3×5 Gap=2"),
    (35, [5, 7], "5×7 Gap=2"), 
    (143, [11, 13], "11×13 Gap=2"),
    (323, [17, 19], "17×19 Gap=2"),
    (899, [29, 31], "29×31 Gap=2"),
    (1763, [41, 43], "41×43 Gap=2"),
    (2491, [47, 53], "47×53 Gap=6"), # Cousin, nicht Twin
    (3599, [59, 61], "59×61 Gap=2"),
    (5183, [71, 73], "71×73 Gap=2"),
  ]
  test_cases.extend(twin_primes)
  
  # 4. Edge Cases für klassische Methoden
  print("📋 EDGE CASES FÜR KLASSISCHE METHODEN:")
  edge_cases = [
    (667, [23, 29], "23×29 Gap=6"),
    (1073, [29, 37], "29×37 Gap=8"), 
    (1333, [31, 43], "31×43 Gap=12"),
    (1643, [31, 53], "31×53 Gap=22"),
    (2021, [43, 47], "43×47 Gap=4"),
    (2537, [43, 59], "43×59 Gap=16"),
  ]
  test_cases.extend(edge_cases)
  
  # 5. Generiere weitere Twin Primes
  print("📋 ZUSÄTZLICHE TWIN PRIMES:")
  additional_twins = []
  primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
  
  for i, p1 in enumerate(primes):
    for p2 in primes[i+1:i+5]: # Nächste 4 Primes
      if abs(p1 - p2) <= 6: # Gap <= 6
        n = p1 * p2
        if n not in [tc[0] for tc in test_cases]: # Nicht bereits in Liste
          additional_twins.append((n, [p1, p2], f"{p1}×{p2} Gap={abs(p1-p2)}"))
          if len(additional_twins) >= 10: # Limit
            break
    if len(additional_twins) >= 10:
      break
  
  test_cases.extend(additional_twins)
  
  return test_cases

def main():
  """Hauptprogramm"""
  
  print("🔬 T0 UNIQUENESS TEST")
  print("=" * 50)
  print("Systematische Suche nach T0's einzigartigen Fähigkeiten")
  print()
  
  # Lade Library
  factory = load_library()
  if not factory:
    print("❌ Kann Library nicht laden!")
    return
  
  # Generiere Test Cases
  test_cases = generate_test_cases()
  print(f"📊 {len(test_cases)} Test Cases generiert")
  
  # Führe Tests durch
  print(f"\n🧪 STARTE SYSTEMATISCHE TESTS")
  print("=" * 50)
  
  results_summary = {
    't0_unique': [],
    't0_faster': [],
    'classical_better': [],
    'classical_faster': [],
    'tie': [],
    'all_fail': []
  }
  
  for i, (n, expected_factors, description) in enumerate(test_cases):
    print(f"\n[{i+1}/{len(test_cases)}]", end="")
    results = test_single_case(factory, n, description, expected_factors)
    result_type = analyze_result(results, n, description)
    results_summary[result_type].append((n, description, results))
  
  # Zusammenfassung
  print(f"\n🏆 GESAMTERGEBNISSE")
  print("=" * 50)
  
  print(f"🚀 T0 EINZIGARTIGE ERFOLGE: {len(results_summary['t0_unique'])}")
  for n, desc, _ in results_summary['t0_unique']:
    print(f"  N={n}: {desc}")
  
  print(f"\n⚡ T0 SCHNELLER: {len(results_summary['t0_faster'])}")
  for n, desc, _ in results_summary['t0_faster']:
    print(f"  N={n}: {desc}")
  
  print(f"\n❌ T0 VERSAGT: {len(results_summary['classical_better'])}")
  for n, desc, _ in results_summary['classical_better'][:5]: # Erste 5
    print(f"  N={n}: {desc}")
  
  print(f"\n🐌 T0 LANGSAMER: {len(results_summary['classical_faster'])}")
  for n, desc, _ in results_summary['classical_faster'][:5]: # Erste 5 
    print(f"  N={n}: {desc}")
  
  print(f"\n🤝 GLEICHWERTIG: {len(results_summary['tie'])}")
  print(f"💥 ALLE VERSAGEN: {len(results_summary['all_fail'])}")
  
  # Fazit
  total_tests = len(test_cases)
  t0_advantage = len(results_summary['t0_unique']) + len(results_summary['t0_faster'])
  classical_advantage = len(results_summary['classical_better']) + len(results_summary['classical_faster'])
  
  print(f"\n🎯 ANTWORT AUF DIE FRAGE:")
  print("=" * 30)
  print(f"Total Tests: {total_tests}")
  print(f"T0 Vorteile: {t0_advantage} ({(t0_advantage/total_tests)*100:.1f}%)")
  print(f"Klassische Vorteile: {classical_advantage} ({(classical_advantage/total_tests)*100:.1f}%)")
  
  if len(results_summary['t0_unique']) > 0:
    print(f"\n✅ T0 HAT EINZIGARTIGE FÄHIGKEITEN!")
    print(f"  {len(results_summary['t0_unique'])} Cases die NUR T0 lösen kann")
    print("  T0's Nische: Spezielle Semiprimes mit Resonanz-Eigenschaften")
  else:
    print(f"\n⚠️ KEINE EINDEUTIGEN T0-VORTEILE")
    print("  T0 ist anders, aber nicht unbedingt überlegen")
  
  print(f"\n💡 T0's wahre Stärke liegt in:")
  print("  • Alternative mathematische Herangehensweise")
  print("  • Resonanz-basierte Faktorisierung") 
  print("  • Adaptive Intelligenz vs statische Algorithmen")

if __name__ == "__main__":
  main()

