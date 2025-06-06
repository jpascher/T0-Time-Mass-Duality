# ========================================
# T0-FRAMEWORK COLAB TEST - KOMPLETTER CODE
# Alles in einer Zelle - einfach ausführen!
# ========================================

import time
import math
from datetime import datetime
import gc

# ========================================
# PURE QUANTUM T0 IMPLEMENTATION
# ========================================

class PureQuantumT0:
    def __init__(self, N):
        self.N = N
        self.bits = math.ceil(math.log2(N))
    
    def mod_pow(self, base, exp, mod):
        result = 1
        base = base % mod
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod
            exp = exp >> 1
            base = (base * base) % mod
        return result
    
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def factor(self):
        a = 2
        max_period = min(self.N, 2000)  # Begrenzt für Colab
        
        # Periodensuche
        for r in range(1, max_period):
            if self.mod_pow(a, r, self.N) == 1:
                if r % 2 == 0:
                    mid = self.mod_pow(a, r // 2, self.N)
                    c1 = self.gcd(mid - 1, self.N)
                    c2 = self.gcd(mid + 1, self.N)
                    
                    for c in [c1, c2]:
                        if 1 < c < self.N and self.N % c == 0:
                            return [c, self.N // c]
        return []

# ========================================
# TRIAL DIVISION BASELINE
# ========================================

def trial_division(n):
    if n < 2:
        return []
    if n % 2 == 0:
        return [2, n // 2]
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return [i, n // i]
    
    return [n]  # Primzahl

# ========================================
# TEST FUNKTIONEN
# ========================================

def test_pure_quantum():
    """Test Pure Quantum Algorithmus"""
    print("📊 PURE T0-QUANTUM ALGORITHMUS")
    print("-" * 35)
    
    test_numbers = [77, 143, 323, 1247, 9991, 65537, 322031]
    results = []
    
    for N in test_numbers:
        start = time.time()
        solver = PureQuantumT0(N)
        factors = solver.factor()
        elapsed = time.time() - start
        
        success = len(factors) >= 2 and factors[0] * factors[1] == N
        
        status = "✅" if success else "❌"
        factors_str = f"{factors[0]} × {factors[1]}" if success else "Keine"
        
        print(f"{N:>8} ({solver.bits:2d} bits): {status} {elapsed:6.3f}s - {factors_str}")
        
        results.append({
            'N': N,
            'bits': solver.bits,
            'success': success,
            'time': elapsed,
            'factors': factors
        })
    
    success_count = sum(1 for r in results if r['success'])
    print(f"\nPure Quantum Erfolgsrate: {success_count}/{len(results)} ({success_count/len(results)*100:.1f}%)")
    
    return results

def test_trial_division():
    """Test Trial Division als Baseline"""
    print("\n📊 TRIAL DIVISION BASELINE")
    print("-" * 30)
    
    test_numbers = [77, 323, 1247, 9991, 65537, 322031, 4294967311]
    results = []
    
    for N in test_numbers:
        start = time.time()
        factors = trial_division(N)
        elapsed = time.time() - start
        
        success = len(factors) >= 2 and factors[0] * factors[1] == N
        bits = math.ceil(math.log2(N))
        
        status = "✅" if success else "❌"
        factors_str = f"{factors[0]} × {factors[1]}" if success else f"Primzahl: {factors[0]}"
        
        print(f"{N:>11} ({bits:2d} bits): {status} {elapsed:6.3f}s - {factors_str}")
        
        results.append({
            'N': N,
            'bits': bits,
            'success': success,
            'time': elapsed,
            'factors': factors
        })
    
    success_count = sum(1 for r in results if r['success'])
    print(f"\nTrial Division Erfolgsrate: {success_count}/{len(results)} ({success_count/len(results)*100:.1f}%)")
    
    return results

def test_hybrid_if_available():
    """Test Hybrid T0-Framework falls verfügbar"""
    print("\n📊 HYBRID T0-FRAMEWORK (falls verfügbar)")
    print("-" * 40)
    
    # Prüfe ob T0FrameworkSimulator verfügbar ist
    try:
        if 'T0FrameworkSimulator' in globals():
            test_numbers = [77, 323, 1247, 9991]
            results = []
            
            for N in test_numbers:
                try:
                    start = time.time()
                    simulator = T0FrameworkSimulator(N)
                    factors = simulator.shor_t0_framework()
                    elapsed = time.time() - start
                    
                    success = False
                    if factors:
                        if len(factors) == 1:
                            success = (factors[0] == N)
                        elif len(factors) >= 2:
                            success = (factors[0] * factors[1] == N)
                    
                    status = "✅" if success else "❌"
                    factors_str = " × ".join(map(str, factors[:2])) if factors else "Keine"
                    
                    print(f"{N:>8}: {status} {elapsed:6.3f}s - {factors_str}")
                    
                    results.append({
                        'N': N,
                        'success': success,
                        'time': elapsed,
                        'factors': factors
                    })
                    
                except Exception as e:
                    print(f"{N:>8}: ❌ ERROR - {type(e).__name__}")
                    results.append({'N': N, 'success': False, 'error': str(e)})
            
            success_count = sum(1 for r in results if r['success'])
            print(f"\nHybrid T0 Erfolgsrate: {success_count}/{len(results)} ({success_count/len(results)*100:.1f}%)")
            
            return results
        else:
            print("❌ T0FrameworkSimulator nicht verfügbar")
            print("💡 Laden Sie zuerst den T0-Simulator Code")
            return None
    except Exception as e:
        print(f"❌ Hybrid-Test Fehler: {e}")
        return None

def analyze_boundaries():
    """Analysiere Grenzwerte"""
    print("\n📊 GRENZWERT-ANALYSE")
    print("-" * 25)
    
    # Pure Quantum Grenzen
    print("Teste Pure Quantum Grenzen:")
    pure_limit = 0
    
    for bits in range(10, 20):
        N = (2**(bits-1)) + 1
        
        success = False
        for r in range(1, min(N, 500)):
            if pow(2, r, N) == 1 and r % 2 == 0:
                mid = pow(2, r // 2, N)
                
                def gcd(a, b):
                    while b:
                        a, b = b, a % b
                    return a
                
                c = gcd(mid - 1, N)
                if 1 < c < N:
                    success = True
                    break
        
        if success:
            pure_limit = bits
            print(f"  {bits} bits: ✅")
        else:
            print(f"  {bits} bits: ❌ (Grenze erreicht)")
            break
    
    print(f"\nPure Quantum Grenze: ~{pure_limit} bits")
    
    # Trial Division Zeit-Grenzen
    print("\nTeste Trial Division Zeit-Grenzen:")
    trial_limit = 0
    
    for bits in range(20, 35):
        N = (2**(bits-1)) + 1
        
        start = time.time()
        limit = min(int(math.sqrt(N)) + 1, 1000000)
        
        found = False
        for i in range(3, limit, 2):
            if N % i == 0:
                found = True
                break
        
        elapsed = time.time() - start
        
        if elapsed < 1.0:
            trial_limit = bits
            print(f"  {bits} bits: ✅ ({elapsed:.3f}s)")
        else:
            print(f"  {bits} bits: ❌ ({elapsed:.3f}s, zu langsam)")
            break
    
    print(f"\nTrial Division Grenze: ~{trial_limit} bits (1s Limit)")
    
    return {
        'pure_quantum_limit': pure_limit,
        'trial_division_limit': trial_limit
    }

def save_results(pure_results, trial_results, hybrid_results, boundary_results):
    """Speichere alle Ergebnisse"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Hardware Info
    try:
        import torch
        if torch.cuda.is_available():
            gpu_name = torch.cuda.get_device_name(0)
            hardware = f"GPU: {gpu_name}"
        else:
            hardware = "CPU"
    except:
        hardware = "CPU"
    
    try:
        import psutil
        memory = f"{psutil.virtual_memory().total / (1024**3):.1f} GB"
    except:
        memory = "Unbekannt"
    
    # TXT-Datei erstellen
    filename = f"t0_colab_results_{timestamp}.txt"
    
    try:
        with open(filename, 'w') as f:
            f.write("T0-Framework Colab Test Ergebnisse\n")
            f.write("=" * 40 + "\n")
            f.write(f"Datum: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Hardware: {hardware}\n")
            f.write(f"RAM: {memory}\n\n")
            
            # Pure Quantum Ergebnisse
            f.write("PURE QUANTUM ERGEBNISSE:\n")
            f.write("-" * 25 + "\n")
            for r in pure_results:
                f.write(f"N={r['N']} ({r['bits']} bits): ")
                f.write(f"{'SUCCESS' if r['success'] else 'FAILED'} ")
                f.write(f"({r['time']:.3f}s)")
                if r['factors']:
                    f.write(f" - {' × '.join(map(str, r['factors']))}")
                f.write("\n")
            
            # Trial Division Ergebnisse
            f.write("\nTRIAL DIVISION ERGEBNISSE:\n")
            f.write("-" * 28 + "\n")
            for r in trial_results:
                f.write(f"N={r['N']} ({r['bits']} bits): ")
                f.write(f"{'SUCCESS' if r['success'] else 'FAILED'} ")
                f.write(f"({r['time']:.3f}s)")
                if r['factors']:
                    f.write(f" - {' × '.join(map(str, r['factors']))}")
                f.write("\n")
            
            # Hybrid Ergebnisse (falls verfügbar)
            if hybrid_results:
                f.write("\nHYBRID T0 ERGEBNISSE:\n")
                f.write("-" * 20 + "\n")
                for r in hybrid_results:
                    f.write(f"N={r['N']}: ")
                    f.write(f"{'SUCCESS' if r['success'] else 'FAILED'}")
                    if 'time' in r:
                        f.write(f" ({r['time']:.3f}s)")
                    if 'factors' in r and r['factors']:
                        f.write(f" - {' × '.join(map(str, r['factors']))}")
                    f.write("\n")
            
            # Grenzwerte
            f.write("\nGRENZWERT-ANALYSE:\n")
            f.write("-" * 20 + "\n")
            f.write(f"Pure Quantum Grenze: ~{boundary_results['pure_quantum_limit']} bits\n")
            f.write(f"Trial Division Grenze: ~{boundary_results['trial_division_limit']} bits\n")
        
        print(f"\n✅ Ergebnisse gespeichert: {filename}")
        print("📁 Datei im Colab-Dateibrowser verfügbar")
        print("💡 Rechtsklick → Download zum Herunterladen")
        
    except Exception as e:
        print(f"❌ Speichern fehlgeschlagen: {e}")

# ========================================
# HAUPTFUNKTION
# ========================================

def run_complete_t0_test():
    """Führe alle T0-Tests durch"""
    print("🚀 T0-FRAMEWORK COLAB TEST SUITE")
    print("=" * 40)
    print(f"Start: {datetime.now().strftime('%H:%M:%S')}")
    
    # Hardware Info
    try:
        import torch
        if torch.cuda.is_available():
            gpu_name = torch.cuda.get_device_name(0)
            gpu_memory = torch.cuda.get_device_properties(0).total_memory / (1024**3)
            print(f"🎮 GPU: {gpu_name} ({gpu_memory:.1f} GB)")
        else:
            print("💻 Hardware: CPU only")
    except:
        print("💻 Hardware: CPU only")
    
    try:
        import psutil
        memory_gb = psutil.virtual_memory().total / (1024**3)
        print(f"🧠 RAM: {memory_gb:.1f} GB")
    except:
        print("🧠 RAM: Unbekannt")
    
    print()
    
    # Führe alle Tests durch
    pure_results = test_pure_quantum()
    trial_results = test_trial_division()
    hybrid_results = test_hybrid_if_available()
    boundary_results = analyze_boundaries()
    
    # Zusammenfassung
    print("\n" + "=" * 50)
    print("GESAMTZUSAMMENFASSUNG")
    print("=" * 50)
    
    # Pure Quantum
    pure_success = sum(1 for r in pure_results if r['success'])
    pure_avg_time = sum(r['time'] for r in pure_results) / len(pure_results)
    print(f"Pure Quantum: {pure_success}/{len(pure_results)} ({pure_success/len(pure_results)*100:.1f}%), ⌀{pure_avg_time:.3f}s")
    
    # Trial Division
    trial_success = sum(1 for r in trial_results if r['success'])
    trial_avg_time = sum(r['time'] for r in trial_results) / len(trial_results)
    print(f"Trial Division: {trial_success}/{len(trial_results)} ({trial_success/len(trial_results)*100:.1f}%), ⌀{trial_avg_time:.3f}s")
    
    # Hybrid (falls verfügbar)
    if hybrid_results:
        hybrid_success = sum(1 for r in hybrid_results if r['success'])
        hybrid_avg_time = sum(r.get('time', 0) for r in hybrid_results) / len(hybrid_results)
        print(f"Hybrid T0: {hybrid_success}/{len(hybrid_results)} ({hybrid_success/len(hybrid_results)*100:.1f}%), ⌀{hybrid_avg_time:.3f}s")
    else:
        print("Hybrid T0: Nicht verfügbar")
    
    # Grenzwerte
    print(f"\nGrenzwerte:")
    print(f"  Pure Quantum: ~{boundary_results['pure_quantum_limit']} bits")
    print(f"  Trial Division: ~{boundary_results['trial_division_limit']} bits")
    
    # Speichere Ergebnisse
    save_results(pure_results, trial_results, hybrid_results, boundary_results)
    
    print(f"\n🎯 Test abgeschlossen: {datetime.now().strftime('%H:%M:%S')}")
    
    return {
        'pure_quantum': pure_results,
        'trial_division': trial_results,
        'hybrid': hybrid_results,
        'boundaries': boundary_results
    }

# ========================================
# AUTO-START FÜR COLAB
# ========================================

print("🔬 T0-Framework Colab Test Suite geladen!")
print("📊 Starten mit: run_complete_t0_test()")
print()

# Automatischer Start falls in Colab
try:
    import google.colab
    print("🚀 Google Colab erkannt - starte automatisch in 3 Sekunden...")
    
    for i in range(3, 0, -1):
        print(f"Start in {i}...")
        time.sleep(1)
    
    # Automatischer Start
    results = run_complete_t0_test()
    
except ImportError:
    print("💻 Lokale Umgebung - manueller Start nötig")
    print("Verwenden Sie: run_complete_t0_test()")
except Exception as e:
    print(f"⚠️ Auto-Start Fehler: {e}")
    print("Manueller Start: run_complete_t0_test()")