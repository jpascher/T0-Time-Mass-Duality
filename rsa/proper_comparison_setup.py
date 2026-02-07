#!/usr/bin/env python3
"""
🔬 KORREKTER WISSENSCHAFTLICHER VERGLEICH
Da die v0-Library defekt ist, analysieren wir INNERHALB der v3-Library:
ALTE vs NEUE ξ-Strategien
"""

import importlib.util
import time

def load_working_library():
  """Lade die funktionierende v3-Library"""
  try:
    spec = importlib.util.spec_from_file_location(r"working_lib", r"factorization_benchmark_library.py"
    )
    lib = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(lib)
    return lib
  except Exception as e:
    print(f"❌ Fehler beim Laden: {e}")
    return None

def scientific_xi_comparison():
  """
  WISSENSCHAFTLICH KORREKTER VERGLEICH:
  Alte ξ-Werte vs Neue ξ-Werte INNERHALB der funktionierenden Library
  """
  
  print("🔬 WISSENSCHAFTLICH KORREKTER ξ-VERGLEICH")
  print("=" * 60)
  print("Da v0-Library defekt ist: Vergleiche ALTE vs NEUE ξ-Strategien")
  print("innerhalb der funktionierenden v3-Library")
  print()
  
  lib = load_working_library()
  if not lib:
    return
  
  factory = lib.create_factorization_library()
  
  # Test Cases
  test_cases = [
    (143, [11, 13], "Twin Prime 11×13"),
    (221, [13, 17], "Twin Prime 13×17"), 
    (323, [17, 19], "Twin Prime 17×19"),
    (35, [5, 7], "Einfacher Twin Prime 5×7"),
    (77, [7, 11], "Twin Prime 7×11"),
    (2491, [47, 53], "Medium Cousin Prime"),
    (1729, [7, 13, 19], "Ramanujan Zahl"),
  ]
  
  print("🎯 VERGLEICH: ALTE ξ-WERTE vs OPTIMIERTE ξ-WERTE")
  print("-" * 50)
  
  improvements = 0
  total_cases = 0
  
  for n, expected_factors, description in test_cases:
    print(f"\n📊 N={n} ({description})")
    print("-" * 30)
    
    # TEST 1: t0_classic (alte ξ-Werte: ξ=1/100000)
    try:
      start_time = time.time()
      old_result = factory.factorize(n, "t0_classic", timeout=3.0)
      old_time = time.time() - start_time
      old_success = old_result.success
      old_xi = old_result.method_specific.get('xi_value', 'N/A') if old_result.method_specific else 'N/A'
      old_resonance = old_result.method_specific.get('resonance_score', 0) if old_result.method_specific else 0
    except:
      old_success = False
      old_time = 3.0
      old_xi = 'ERROR'
      old_resonance = 0
    
    # TEST 2: t0_adaptive (neue optimierte ξ-Werte)
    try:
      start_time = time.time()
      new_result = factory.factorize(n, "t0_adaptive", timeout=3.0)
      new_time = time.time() - start_time
      new_success = new_result.success
      new_xi = new_result.method_specific.get('xi_value', 'N/A') if new_result.method_specific else 'N/A'
      new_resonance = new_result.method_specific.get('resonance_score', 0) if new_result.method_specific else 0
      new_strategy = new_result.method_specific.get('xi_strategy', 'N/A') if new_result.method_specific else 'N/A'
    except:
      new_success = False
      new_time = 3.0
      new_xi = 'ERROR'
      new_resonance = 0
      new_strategy = 'ERROR'
    
    # Analyse
    old_status = "✅" if old_success else "❌"
    new_status = "✅" if new_success else "❌"
    
    print(f"ALTE ξ-Strategie (classic): {old_status} {old_time:.4f}s ξ={old_xi} R={old_resonance:.6f}")
    print(f"NEUE ξ-Strategie (adaptive): {new_status} {new_time:.4f}s ξ={new_xi} R={new_resonance:.6f} ({new_strategy})")
    
    # Bewertung
    total_cases += 1
    if new_success and not old_success:
      print("🚀 VERBESSERUNG: Neue ξ-Optimierung löst unlösbaren Fall!")
      improvements += 1
    elif new_success and old_success:
      speedup = old_time / new_time if new_time > 0 else 1
      resonance_improvement = new_resonance / old_resonance if old_resonance > 0 else float('inf')
      print(f"📈 OPTIMIERUNG: {speedup:.2f}x Speedup, {resonance_improvement:.2f}x bessere Resonanz")
      if speedup > 1.2 or resonance_improvement > 2:
        improvements += 1
    elif old_success and not new_success:
      print("⚠️ REGRESSION: Alte Version war besser")
    else:
      print("❌ BEIDE versagen bei diesem Fall")
  
  print(f"\n🏆 WISSENSCHAFTLICHES FAZIT")
  print("=" * 30)
  print(f"Testfälle: {total_cases}")
  print(f"Verbesserungen durch ξ-Optimierung: {improvements}")
  print(f"Verbesserungsrate: {(improvements/total_cases)*100:.1f}%")
  
  if improvements >= total_cases * 0.7:
    print("✅ ξ-OPTIMIERUNG WISSENSCHAFTLICH BESTÄTIGT!")
  elif improvements >= total_cases * 0.5:
    print("⚡ ξ-OPTIMIERUNG ZEIGT DEUTLICHE VERBESSERUNGEN")
  else:
    print("⚠️ ξ-OPTIMIERUNG EFFEKT UNKLAR - Mehr Tests nötig")

def alternative_comparison():
  """Alternative: Vergleiche T0 vs Klassische Methoden"""
  
  print(f"\n\n🔬 ALTERNATIVE: T0 vs KLASSISCHE METHODEN")
  print("=" * 50)
  print("Vergleiche optimierte T0-Methoden mit bewährten klassischen Algorithmen")
  
  lib = load_working_library()
  if not lib:
    return
  
  factory = lib.create_factorization_library()
  
  test_cases = [
    (143, [11, 13], "Twin Prime 11×13"),
    (221, [13, 17], "Twin Prime 13×17"), 
    (323, [17, 19], "Twin Prime 17×19"),
    (2491, [47, 53], "Medium Cousin Prime"),
  ]
  
  methods = {
    'trial_division': 'Klassisch: Trial Division',
    'fermat': 'Klassisch: Fermat',
    'pollard_rho': 'Klassisch: Pollard Rho',
    't0_adaptive': 'Revolutionär: T0-Adaptive'
  }
  
  for n, expected_factors, description in test_cases:
    print(f"\n📊 N={n} ({description})")
    print("-" * 30)
    
    results = {}
    for method, label in methods.items():
      try:
        start_time = time.time()
        result = factory.factorize(n, method, timeout=2.0)
        elapsed = time.time() - start_time
        success = result.success
        
        status = "✅" if success else "❌"
        results[method] = {'success': success, 'time': elapsed}
        print(f"{label:>25}: {status} {elapsed:.4f}s")
        
      except Exception as e:
        print(f"{label:>25}: ❌ ERROR")
        results[method] = {'success': False, 'time': 2.0}
    
    # Bewertung
    t0_success = results.get('t0_adaptive', {}).get('success', False)
    classical_successes = [results[m]['success'] for m in ['trial_division', 'fermat', 'pollard_rho'] if m in results]
    
    if t0_success and not any(classical_successes):
      print("🚀 T0 EINZIGARTIG: Nur T0 löst diesen Fall!")
    elif t0_success and any(classical_successes):
      t0_time = results['t0_adaptive']['time']
      best_classical_time = min([results[m]['time'] for m in ['trial_division', 'fermat', 'pollard_rho'] if m in results and results[m]['success']], default=float('inf'))
      if best_classical_time < float('inf'):
        if t0_time < best_classical_time:
          print(f"⚡ T0 SCHNELLER: {best_classical_time/t0_time:.2f}x vs beste klassische Methode")
        else:
          print(f"🐌 Klassisch schneller: {t0_time/best_classical_time:.2f}x")

def main():
  """Hauptfunktion"""
  print("🎯 WISSENSCHAFTLICH KORREKTER VERGLEICH")
  print("Da v0-Library defekt ist, führen wir korrekte Vergleiche durch:")
  print()
  
  # Hauptvergleich: Alte vs neue ξ-Strategien
  scientific_xi_comparison()
  
  # Zusätzlicher Vergleich: T0 vs Klassische Methoden
  alternative_comparison()
  
  print(f"\n💡 ZUSAMMENFASSUNG:")
  print("Dieser Vergleich ist wissenschaftlich korrekt, weil er:")
  print("1. Funktionsfähige Algorithmen vergleicht (nicht defekt vs funktionierend)")
  print("2. Spezifische ξ-Optimierungen isoliert testet")
  print("3. T0 vs etablierte Methoden objektiv bewertet")

if __name__ == "__main__":
  main()

