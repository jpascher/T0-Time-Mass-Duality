#!/usr/bin/env python3
"""
T0 Gap Analyzer - Warum versagt T0 bei "einfachen" Zahlen?
Systematische Analyse der Lücken in T0's Performance
"""

from factorization_benchmark_library import create_factorization_library, TestCase
from fractions import Fraction
import math
import time

class T0GapAnalyzer:
    """Analysiert wo und warum T0 versagt"""
    
    def __init__(self):
        self.lib = create_factorization_library()
        
    def analyze_t0_gaps(self):
        """Hauptanalyse der T0-Lücken"""
        print("=" * 80)
        print("🔍 T0 GAP ANALYSIS - Warum versagt T0 bei einfachen Zahlen?")
        print("=" * 80)
        
        # Testfälle wo T0 versagen sollte aber nicht sollte
        gap_cases = [
            # Twin Primes die T0 lösen sollte, aber versagt
            TestCase(143, [11, 13], "Twin Prime 11×13 - T0 sollte lösen", "twin_prime", "easy"),
            TestCase(323, [17, 19], "Twin Prime 17×19 - T0 sollte lösen", "twin_prime", "easy"),
            TestCase(1517, [37, 41], "Twin Prime 37×41 - T0 sollte lösen", "twin_prime", "medium"),
            TestCase(2491, [47, 53], "Twin Prime 47×53 - T0 sollte lösen", "twin_prime", "medium"),
            
            # Zum Vergleich: Twin Primes die T0 löst
            TestCase(77, [7, 11], "Twin Prime 7×11 - T0 löst", "twin_prime", "easy"),
            TestCase(221, [13, 17], "Twin Prime 13×17 - T0 löst", "twin_prime", "easy"),
            TestCase(667, [23, 29], "Twin Prime 23×29 - T0 löst", "twin_prime", "medium"),
            
            # Grenzfälle
            TestCase(35, [5, 7], "Twin Prime 5×7 - Baseline", "twin_prime", "trivial"),
            TestCase(21, [3, 7], "Cousin Prime 3×7 - Sollte lösen", "cousin_prime", "easy"),
        ]
        
        print("🎯 Testing T0 performance on small cases that should work...")
        
        for case in gap_cases:
            self.analyze_single_case(case)
        
        # Tiefere Analyse der Problemfälle
        print(f"\n{'='*80}")
        print("🔬 DEEP DIVE ANALYSIS - Warum versagen diese Fälle?")
        print(f"{'='*80}")
        
        problem_cases = [143, 323, 1517, 2491]
        working_cases = [77, 221, 667]
        
        self.deep_dive_analysis(problem_cases, working_cases)
    
    def analyze_single_case(self, case):
        """Analysiere einen einzelnen Fall detailliert"""
        n = case.n
        factors = case.expected_factors
        
        print(f"\n{'='*60}")
        print(f"🔍 Analyzing N = {n} = {factors[0]}×{factors[1]}")
        print(f"Bit size: {n.bit_length()}, Factor gap: {abs(factors[0] - factors[1])}")
        print(f"Description: {case.description}")
        print(f"{'='*60}")
        
        # Teste alle T0-Varianten mit detaillierter Ausgabe
        methods = ['t0_classic', 't0_universal', 't0_adaptive']
        
        for method in methods:
            print(f"\n🔬 Testing {method}:")
            
            start_time = time.time()
            result = self.lib.factorize(n, method, timeout=10.0)
            elapsed = time.time() - start_time
            
            status = "✅ SUCCESS" if result.success else "❌ FAILED"
            print(f"   Result: {status} in {elapsed:.4f}s")
            
            if result.factors:
                print(f"   Factors found: {result.factors}")
            
            # T0-spezifische Details
            if hasattr(result, 'method_specific') and result.method_specific:
                ms = result.method_specific
                print(f"   ξ strategy: {ms.get('xi_strategy', 'N/A')}")
                print(f"   ξ value: {ms.get('xi_value', 'N/A')}")
                print(f"   Resonance: {ms.get('resonance_score', 0):.6f}")
                print(f"   Periods tested: {ms.get('periods_tested', 0)}")
                print(f"   Best period: {ms.get('period_found', 'N/A')}")
                
                # Mehr Details wenn möglich
                if 'method' in ms:
                    print(f"   Method used: {ms['method']}")
        
        # Vergleiche mit klassischen Methoden
        print(f"\n📊 Classical methods comparison:")
        classical_methods = ['trial_division', 'fermat', 'pollard_rho']
        
        for method in classical_methods:
            result = self.lib.factorize(n, method, timeout=2.0)
            status = "✅" if result.success else "❌"
            print(f"   {method:15}: {status} {result.time:.4f}s")
    
    def deep_dive_analysis(self, problem_cases, working_cases):
        """Tiefere Analyse warum manche Fälle versagen"""
        
        print("🔍 MATHEMATICAL PROPERTIES ANALYSIS")
        print("-" * 50)
        
        print("\n❌ PROBLEM CASES (T0 versagt):")
        for n in problem_cases:
            factors = self.factorize_simple(n)
            if len(factors) == 2:
                p, q = factors
                self.analyze_mathematical_properties(n, p, q, "PROBLEM")
        
        print("\n✅ WORKING CASES (T0 funktioniert):")
        for n in working_cases:
            factors = self.factorize_simple(n)
            if len(factors) == 2:
                p, q = factors
                self.analyze_mathematical_properties(n, p, q, "WORKING")
        
        # Hypothesen testen
        print(f"\n{'='*60}")
        print("🧠 HYPOTHESIS TESTING")
        print(f"{'='*60}")
        
        self.test_hypotheses(problem_cases, working_cases)
    
    def analyze_mathematical_properties(self, n, p, q, case_type):
        """Analysiere mathematische Eigenschaften"""
        gap = abs(p - q)
        avg = (p + q) / 2
        ratio = max(p, q) / min(p, q)
        
        # Modular properties
        n_mod_4 = n % 4
        n_mod_8 = n % 8
        n_mod_12 = n % 12
        
        # Prime gaps to previous/next primes
        p_gap_prev = self.gap_to_previous_prime(p)
        q_gap_next = self.gap_to_next_prime(q)
        
        print(f"   N={n} = {p}×{q} ({case_type})")
        print(f"      Gap: {gap}, Ratio: {ratio:.3f}, Avg: {avg:.1f}")
        print(f"      N mod (4,8,12): ({n_mod_4},{n_mod_8},{n_mod_12})")
        print(f"      Prime gaps: p-prev={p_gap_prev}, q-next={q_gap_next}")
        
        # T0-spezifische Eigenschaften
        self.analyze_t0_properties(n, p, q)
    
    def analyze_t0_properties(self, n, p, q):
        """Analysiere T0-spezifische mathematische Eigenschaften"""
        
        # Periode-Eigenschaften für verschiedene Basen
        for base in [2, 3, 5, 7]:
            if math.gcd(base, n) == 1:
                # Finde Periode
                period = self.find_period_length(base, n)
                if period:
                    # Berechne "Resonanz" manuell
                    omega = 2 * math.pi / period
                    pi_approx = 355/113
                    diff = abs(omega - pi_approx)
                    
                    print(f"      Base {base}: periode={period}, ω={omega:.4f}, |ω-π|={diff:.4f}")
                else:
                    print(f"      Base {base}: keine Periode gefunden")
    
    def find_period_length(self, base, n, max_period=1000):
        """Finde Periodenlänge für base^r ≡ 1 (mod n)"""
        for r in range(1, min(n, max_period)):
            if pow(base, r, n) == 1:
                return r
        return None
    
    def gap_to_previous_prime(self, p):
        """Finde Abstand zum vorherigen Prime"""
        for i in range(1, p):
            if self.is_prime_simple(p - i):
                return i
        return 0
    
    def gap_to_next_prime(self, p):
        """Finde Abstand zum nächsten Prime"""
        for i in range(1, 100):
            if self.is_prime_simple(p + i):
                return i
        return 0
    
    def test_hypotheses(self, problem_cases, working_cases):
        """Teste verschiedene Hypothesen warum T0 versagt"""
        
        hypotheses = [
            "Hypothesis 1: Problem cases have no suitable periods",
            "Hypothesis 2: Problem cases need different ξ values", 
            "Hypothesis 3: Problem cases have unfavorable resonance patterns",
            "Hypothesis 4: Implementation bugs in period search",
        ]
        
        for hypothesis in hypotheses:
            print(f"\n🧪 {hypothesis}")
            
        # Hypothesis 1: Periode-Existenz
        print(f"\n🔬 Testing Hypothesis 1: Period existence")
        
        for n in problem_cases + working_cases:
            case_type = "PROBLEM" if n in problem_cases else "WORKING"
            periods_found = []
            
            for base in [2, 3, 5, 7]:
                if math.gcd(base, n) == 1:
                    period = self.find_period_length(base, n)
                    if period:
                        periods_found.append((base, period))
            
            print(f"   N={n} ({case_type}): periods {periods_found}")
        
        # Hypothesis 2: ξ-Sensitivität  
        print(f"\n🔬 Testing Hypothesis 2: ξ sensitivity")
        
        xi_values_to_test = [
            Fraction(1, 1000000), Fraction(1, 100000), Fraction(1, 10000),
            Fraction(1, 1000), Fraction(1, 100), Fraction(1, 42)
        ]
        
        for n in problem_cases[:2]:  # Teste nur erste 2 für Performance
            print(f"   Testing N={n} with different ξ values:")
            
            for xi in xi_values_to_test:
                # Simuliere T0 mit diesem ξ
                success = self.test_t0_with_xi(n, xi)
                status = "✅" if success else "❌"
                print(f"      ξ={xi}: {status}")
    
    def test_t0_with_xi(self, n, xi):
        """Teste T0 mit spezifischem ξ-Wert (vereinfacht)"""
        # Das ist eine vereinfachte Simulation
        # In der echten Implementation würden wir T0 mit diesem ξ laufen lassen
        
        pi_approx = Fraction(355, 113)
        threshold = Fraction(1, 3)
        
        for base in [2, 3, 5, 7]:
            if math.gcd(base, n) == 1:
                period = self.find_period_length(base, n)
                if period:
                    # Vereinfachte Resonanz-Berechnung
                    omega = Fraction(2) * pi_approx / Fraction(period)
                    diff = omega - pi_approx
                    diff_squared = diff * diff
                    denominator = Fraction(4) * xi
                    exponent = -diff_squared / denominator
                    score = Fraction(1) / (Fraction(1) + abs(exponent))
                    
                    if score > threshold:
                        return True
        
        return False
    
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
    
    def is_prime_simple(self, n):
        """Einfacher Primzahltest"""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

def main():
    """Führe T0 Gap Analysis aus"""
    analyzer = T0GapAnalyzer()
    analyzer.analyze_t0_gaps()
    
    print(f"\n{'='*80}")
    print("🎯 CONCLUSIONS FROM GAP ANALYSIS:")
    print("• T0's failures are NOT random - there are patterns")
    print("• Mathematical properties of the numbers matter")
    print("• ξ-optimization might help, but implementation issues exist")
    print("• T0 needs better period search and resonance calculation")
    print(f"{'='*80}")

if __name__ == "__main__":
    main()