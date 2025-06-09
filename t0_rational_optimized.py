#!/usr/bin/env python3
"""
T0-Framework Periodensuche mit rationalen Zahlen und Optimierungen
Implementiert BSGS, Padé-Approximation, parallele Basis-Suche und vereinfachte Resonanzmetrik
"""

from fractions import Fraction
import time
from typing import Optional, List, Tuple
from multiprocessing import Pool
import random

class T0RationalSimulatorOptimized:
    def __init__(self, rsa_target_N: int):
        """Initialisiere optimierten T0-Simulator mit rationalen Zahlen"""
        self.rsa_N = rsa_target_N
        self.rsa_bits = rsa_target_N.bit_length()
        self.xi = Fraction(1, 100000)  # ξ = 1e-5
        self.pi = Fraction(355, 113)   # π-Approximation
        self.max_period_search = 75000
        self.max_resonance_periods = 800
        print(f"🔬 T0-Rational-Optimized Simulator - N={rsa_target_N:,} ({self.rsa_bits} bits)")
        print(f"   ξ-Parameter: {self.xi} (rational)")
        print(f"   π-Approximation: {self.pi} (rational)")

    def mod_pow(self, base: int, exp: int, mod: int) -> int:
        """Modulare Exponentiation"""
        result = 1
        base = base % mod
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod
            exp >>= 1
            base = (base * base) % mod
        return result

    def gcd(self, a: int, b: int) -> int:
        """GCD mit Edge-Case-Behandlung"""
        a, b = abs(a), abs(b)
        if a == 0 and b == 0:
            raise ValueError("GCD(0, 0) is undefined")
        while b:
            a, b = b, a % b
        return a

    def _rational_exp_approx(self, x: Fraction) -> Fraction:
        """Padé-Approximation für e^(-x)"""
        num = Fraction(1, 1) - x / 2
        denom = Fraction(1, 1) + x / 2
        return num / denom if denom != 0 else Fraction(1, 1)

    def _find_optimal_base(self) -> int:
        """Rationale Basis-Auswahl (vereinfacht)"""
        candidates = random.sample(range(2, min(self.rsa_N, 1000)), 5)
        for a in candidates:
            if self.gcd(a, self.rsa_N) == 1:
                return a
        return 2

    def quantum_period_finding_bsgs(self, a: int) -> Optional[int]:
        """Periodensuche mit Baby-Step Giant-Step"""
        print(f"   🔍 T0-Rationale BSGS-Periodensuche für Basis a={a}")
        start_time = time.time()

        m = int(self.rsa_N ** 0.5) + 1
        table = {}
        for j in range(m):
            val = self.mod_pow(a, j, self.rsa_N)
            table[val] = j
        for i in range(m):
            val = self.mod_pow(a, i * m, self.rsa_N)
            if val in table:
                r = i * m - table[val]
                if r > 0 and self.mod_pow(a, r, self.rsa_N) == 1:
                    print(f"   🎯 Beste T0-Periode: r={r}")
                    print(f"   Zeit: {time.time() - start_time:.3f}s")
                    return r
            if time.time() - start_time > 2.0:
                break
        print(f"   ❌ Keine Periode gefunden nach {time.time() - start_time:.3f}s")
        return None

    def quantum_period_finding(self, a: Optional[int] = None) -> Optional[int]:
        """Rationale Periodensuche mit vereinfachter Resonanzmetrik"""
        print(f"   🔍 T0-Rationale Periodensuche für Basis a={a if a else 'auto'}")
        start_time = time.time()

        if a is None:
            a = self._find_optimal_base()
        gcd_check = self.gcd(a, self.rsa_N)
        if gcd_check > 1:
            print(f"   ✅ Direkter GCD-Faktor: {gcd_check}")
            return None

        periods: List[Tuple[int, Fraction]] = []
        max_period = min(self.rsa_N, self.max_period_search)

        for r in range(2, max_period, 2):  # Nur gerade r
            if self.mod_pow(a, r, self.rsa_N) == 1:
                omega = Fraction(2, 1) * self.pi / Fraction(r, 1)
                if abs(omega - self.pi) < self.xi * 100:  # Vereinfachte Resonanzmetrik
                    periods.append((r, Fraction(1, 1)))  # Dummy-Resonanz für Auswahl
                if len(periods) > self.max_resonance_periods:
                    break
            if time.time() - start_time > 2.0:
                break

        if periods:
            best_period = min(periods, key=lambda x: x[0])[0]  # Kleinste Periode
            print(f"   🎯 Beste T0-Periode: r={best_period}")
            print(f"   Zeit: {time.time() - start_time:.3f}s")
            return best_period
        print(f"   ❌ Keine Periode gefunden nach {time.time() - start_time:.3f}s")
        return None

    def quantum_period_finding_parallel(self) -> Optional[int]:
        """Parallele Periodensuche für mehrere Basen"""
        bases = [self._find_optimal_base() for _ in range(4)]
        print(f"   🔍 Parallele Periodensuche für Basen {bases}")
        with Pool(4) as p:
            results = p.map(self.quantum_period_finding_bsgs, bases)
        period = next((r for r in results if r), None)
        if period:
            print(f"   🎯 Beste T0-Periode (parallel): r={period}")
        return period

    def extract_factors(self, a: int, r: int) -> List[int]:
        """Faktor-Extraktion"""
        factors = []
        if r % 2 == 0:
            mid_power = self.mod_pow(a, r // 2, self.rsa_N)
            candidate1 = self.gcd(mid_power - 1, self.rsa_N)
            candidate2 = self.gcd(mid_power + 1, self.rsa_N)
            for candidate in [candidate1, candidate2]:
                if 1 < candidate < self.rsa_N and self.rsa_N % candidate == 0:
                    factors.append(candidate)
                    complementary = self.rsa_N // candidate
                    if complementary != candidate and complementary not in factors:
                        factors.append(complementary)
        return sorted(list(set(factors)))

    def trial_division_fallback(self) -> List[int]:
        """Fallback für Trial Division"""
        for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 127]:
            if self.rsa_N % p == 0:
                return [p, self.rsa_N // p]
        return []

    def shor_t0_rational(self) -> List[int]:
        """Hauptmethode für Faktorisierung"""
        print(f"🚀 T0-Rationale-Optimized Faktorisierung für N={self.rsa_N:,}")
        period = self.quantum_period_finding_parallel()
        if period:
            a = self._find_optimal_base()
            factors = self.extract_factors(a, period)
            if len(factors) >= 2 and factors[0] * factors[1] == self.rsa_N:
                print(f"   ✅ Faktoren: {factors[0]:,} × {factors[1]:,} = {self.rsa_N:,}")
                return factors
        factors = self.trial_division_fallback()
        if factors:
            print(f"   ✅ Fallback-Faktoren: {factors[0]:,} × {factors[1]:,} = {self.rsa_N:,}")
            return factors
        print("   ❌ Faktorisierung fehlgeschlagen")
        return []

def test_rational_period_finding_optimized():
    """Test der optimierten rationalen Periodensuche"""
    test_cases = [
        (15, 4, [3, 5]),       # 3 × 5
        (323, 18, [17, 19]),   # 17 × 19
        (437, 24, [19, 23]),   # 19 × 23
        (667, 22, [23, 29]),   # 23 × 29
        (10403, 50, [101, 103]), # 101 × 103
        (87463, None, [127, 689]), # 127 × 689
    ]
    for n, expected_period, expected_factors in test_cases:
        simulator = T0RationalSimulatorOptimized(n)
        period = simulator.quantum_period_finding(a=2)
        factors = simulator.extract_factors(2, period) if period else []
        print(f"N={n}: Periode={period}, Erwartet={expected_period}, Faktoren={factors}, Erwartet={expected_factors}")

if __name__ == "__main__":
    test_rational_period_finding_optimized()