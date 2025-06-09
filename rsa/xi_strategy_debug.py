#!/usr/bin/env python3
"""
ξ-Strategy Debug - Das wahre Problem ist die falsche ξ-Strategie-Auswahl!
N=21 funktioniert mit universal ξ=1/100
N=143 versagt mit twin_prime_classic ξ=1/100000
"""

import time
from fractions import Fraction
from factorization_benchmark_library import UniversalT0Algorithm

def debug_xi_strategy_selection():
    """Debug die ξ-Strategie-Auswahl"""
    print("🎯 ξ-STRATEGY SELECTION DEBUG")
    print("=" * 60)
    
    t0 = UniversalT0Algorithm()
    
    # Test Cases
    test_cases = [
        (21, [3, 7], "Working Case"),
        (77, [7, 11], "Working Case"),
        (143, [11, 13], "Problem Case"),
        (323, [17, 19], "Problem Case"),
    ]
    
    print("Analyzing how T0 selects ξ-strategy for each case...")
    
    for n, expected_factors, case_type in test_cases:
        print(f"\n🔬 {case_type}: N={n} (factors: {expected_factors})")
        
        # Manuelle Kategorisierung (wie T0 es macht)
        category = t0._categorize_number(n)
        selected_strategy = t0._select_xi_strategy(n)
        xi_value = t0.xi_profiles[selected_strategy]
        
        print(f"   Categorized as: {category}")
        print(f"   Selected strategy: {selected_strategy}")
        print(f"   ξ value: {xi_value} = {float(xi_value):.6f}")
        
        # Teste Faktorisierung
        result = t0.factorize(n, timeout=2.0)
        success = result.get('factors') is not None
        actual_strategy = result.get('method_specific', {}).get('xi_strategy', 'unknown')
        actual_xi = result.get('method_specific', {}).get('xi_value', 'unknown')
        
        print(f"   Actual strategy used: {actual_strategy}")
        print(f"   Actual ξ used: {actual_xi}")
        print(f"   Result: {'✅ SUCCESS' if success else '❌ FAILED'}")
        
        # Analyse warum diese Strategie gewählt wurde
        bit_size = n.bit_length()
        print(f"   Bit size: {bit_size}")
        
        if n in [1729, 2047, 4181]:
            print(f"   → Special case detected")
        elif n > 10000:
            print(f"   → Large number path")
        elif n > 1000:
            print(f"   → Medium size path")
        elif bit_size > 25:
            print(f"   → High bit size path")
        elif category == 'twin_prime' and n < 500:
            print(f"   → Small twin prime path")
        else:
            print(f"   → Universal path (should use ξ=1/100)")

def test_force_xi_strategies():
    """Teste alle ξ-Strategien auf Problem Cases"""
    print(f"\n{'='*60}")
    print("🚀 FORCE ξ-STRATEGY TEST")
    print("=" * 60)
    print("Testing all ξ-strategies on problem cases to find what works...")
    
    t0 = UniversalT0Algorithm()
    
    problem_cases = [143, 323]
    strategies = ['universal', 'medium_size', 'special_cases', 'large_numbers', 'twin_prime_classic']
    
    for n in problem_cases:
        print(f"\n🔬 Testing N={n}:")
        
        for strategy in strategies:
            # Force strategy durch temporäre Änderung
            original_profiles = t0.xi_profiles.copy()
            
            # Alle Strategien auf getestete Strategie setzen
            xi_value = original_profiles[strategy]
            forced_profiles = {key: xi_value for key in original_profiles.keys()}
            t0.xi_profiles = forced_profiles
            
            try:
                result = t0.factorize(n, timeout=2.0)
                success = result.get('factors') is not None
                factors = result.get('factors', None)
                resonance = result.get('method_specific', {}).get('resonance_score', 0)
                
                status = "✅" if success else "❌"
                factors_str = str(factors) if factors else "None"
                
                print(f"   {strategy:18}: {status} {factors_str} (R={resonance:.6f})")
                
            finally:
                # Restore original profiles
                t0.xi_profiles = original_profiles

def debug_categorization_logic():
    """Debug die Kategorisierung-Logic"""
    print(f"\n{'='*60}")
    print("🔍 CATEGORIZATION LOGIC DEBUG")
    print("=" * 60)
    
    t0 = UniversalT0Algorithm()
    
    test_numbers = [21, 77, 143, 221, 323, 667]
    
    for n in test_numbers:
        print(f"\n📊 N={n}:")
        
        # Schritt-für-Schritt Kategorisierung
        factors = t0._simple_factorize(n)
        print(f"   Simple factorization: {factors}")
        
        if len(factors) == 2:
            p, q = factors
            is_p_prime = t0._is_prime(p)
            is_q_prime = t0._is_prime(q)
            print(f"   {p} is prime: {is_p_prime}")
            print(f"   {q} is prime: {is_q_prime}")
            
            if is_p_prime and is_q_prime:
                diff = abs(p - q)
                print(f"   Factor difference: {diff}")
                
                if diff == 2:
                    category = 'twin_prime'
                elif diff <= 6:
                    category = 'cousin_prime'
                elif diff <= 12:
                    category = 'near_twin_prime'
                else:
                    category = 'distant_prime'
                    
                print(f"   → Category: {category}")
            else:
                print(f"   → Category: composite_factors")
        else:
            print(f"   → Category: composite")
        
        # Vergleiche mit tatsächlicher Kategorisierung
        actual_category = t0._categorize_number(n)
        print(f"   Actual category: {actual_category}")

def find_optimal_xi_for_problem_cases():
    """Finde optimale ξ-Werte für Problem Cases"""
    print(f"\n{'='*60}")
    print("🎯 OPTIMAL ξ SEARCH")
    print("=" * 60)
    
    t0 = UniversalT0Algorithm()
    
    # Teste verschiedene ξ-Werte
    xi_candidates = [
        Fraction(1, 10),
        Fraction(1, 50),
        Fraction(1, 100),      # Universal
        Fraction(1, 500),
        Fraction(1, 1000),     # Medium
        Fraction(1, 5000),
        Fraction(1, 10000),
        Fraction(1, 50000),
        Fraction(1, 100000),   # Classic
    ]
    
    problem_case = 143
    print(f"Testing optimal ξ for N={problem_case}:")
    
    for xi in xi_candidates:
        # Force diesen ξ-Wert
        original_profiles = t0.xi_profiles.copy()
        forced_profiles = {key: xi for key in original_profiles.keys()}
        t0.xi_profiles = forced_profiles
        
        try:
            result = t0.factorize(problem_case, timeout=2.0)
            success = result.get('factors') is not None
            factors = result.get('factors', None)
            resonance = result.get('method_specific', {}).get('resonance_score', 0)
            
            status = "✅" if success else "❌"
            factors_str = str(factors) if factors else "None"
            
            print(f"   ξ = {xi} = {float(xi):.6f}: {status} {factors_str} (R={resonance:.6f})")
            
        finally:
            t0.xi_profiles = original_profiles

if __name__ == "__main__":
    # 1. Debug ξ-Strategy Selection
    debug_xi_strategy_selection()
    
    # 2. Force Test alle Strategien
    test_force_xi_strategies()
    
    # 3. Debug Kategorisierung
    debug_categorization_logic()
    
    # 4. Optimal ξ Search
    find_optimal_xi_for_problem_cases()
    
    print(f"\n💡 CONCLUSIONS:")
    print("• Check if problem cases are mis-categorized")
    print("• Check if wrong ξ-strategy is selected")
    print("• Find which ξ-values actually work")
    print("• Fix the strategy selection logic")
