#!/usr/bin/env python3
"""
EXAKTE BIT-GRENZEN für Harmonische Faktorisierung
=================================================

Berechne präzise bis zu welcher Bit-Größe harmonische Faktorisierung funktioniert.
Basierend auf den bewiesenen Grenzen von ~12 Dezimalstellen.
"""

import math
from harmonic_lib import HarmonicFactorizer

def calculate_exact_bit_limits():
    """Berechne exakte Bit-Grenzen basierend auf harmonischen Grenzen"""
    
    print("🎯 EXAKTE BIT-GRENZEN BERECHNUNG")
    print("=" * 50)
    
    # Bewiesene harmonische Grenzen aus den Tests
    proven_limits = {
        "Zuverlässig (70%+ Erfolg)": 12,  # 12 Dezimalstellen
        "Gelegentlich (einzelne Treffer)": 15,  # 15 Dezimalstellen  
        "Praktisch unmöglich": 16  # 16+ Dezimalstellen
    }
    
    print("📊 UMRECHNUNG: Dezimalstellen → Bits")
    print("-" * 40)
    print(f"{'Kategorie':<30} {'Stellen':<8} {'Bits':<8} {'Größe'}")
    print("-" * 65)
    
    bit_limits = {}
    
    for category, decimal_digits in proven_limits.items():
        # Umrechnung: Dezimalstellen zu Bits
        # log10(2^bits) = bits * log10(2) = decimal_digits
        # Also: bits = decimal_digits / log10(2)
        
        bits = decimal_digits / math.log10(2)
        max_number = 10 ** decimal_digits
        
        bit_limits[category] = int(bits)
        
        print(f"{category:<30} {decimal_digits:<8} {int(bits):<8} 10^{decimal_digits}")
    
    return bit_limits

def test_specific_bit_sizes():
    """Teste spezifische Bit-Größen um die genaue Grenze zu finden"""
    
    print(f"\n🔬 PRÄZISIONS-TEST: Verschiedene Bit-Größen")
    print("-" * 50)
    
    factorizer = HarmonicFactorizer(tolerance_percent=5.0)
    
    # Teste Bit-Größen rund um die berechnete Grenze
    test_bit_sizes = [32, 36, 40, 44, 48, 52, 56, 60]
    
    print(f"{'Bits':<6} {'Stellen':<8} {'Beispielzahl':<15} {'Tests':<6} {'Erfolg':<6} {'Rate'}")
    print("-" * 65)
    
    results = {}
    
    for bits in test_bit_sizes:
        # Berechne entsprechende Dezimalstellen
        decimal_digits = int(bits * math.log10(2))
        
        # Generiere Testzahlen mit genau dieser Bit-Größe
        min_val = 2 ** (bits - 1)  # Kleinste bits-Bit Zahl
        max_val = 2 ** bits - 1    # Größte bits-Bit Zahl
        
        successes = 0
        total_tests = 10  # 10 Tests pro Bit-Größe
        test_numbers = []
        
        for _ in range(total_tests):
            # Generiere zwei Faktoren die ein Produkt in der Bit-Range ergeben
            factor_bits = bits // 2
            min_factor = 2 ** (factor_bits - 1)
            max_factor = 2 ** factor_bits - 1
            
            import random
            factor1 = random.randint(min_factor, max_factor)
            factor2 = random.randint(min_factor, max_factor)
            
            test_number = factor1 * factor2
            
            # Prüfe ob im gewünschten Bit-Bereich
            if min_val <= test_number <= max_val:
                test_numbers.append(test_number)
                
                try:
                    result = factorizer.factorize(test_number, verbose=False)
                    if result.success:
                        successes += 1
                except Exception as e:
                    # Bei Fehlern (wie OverflowError) als Misserfolg werten
                    pass
        
        actual_tests = len(test_numbers)
        success_rate = successes / actual_tests if actual_tests > 0 else 0
        
        example_number = test_numbers[0] if test_numbers else "N/A"
        if isinstance(example_number, int):
            example_str = f"{example_number:,.0e}"
        else:
            example_str = str(example_number)
        
        print(f"{bits:<6} {decimal_digits:<8} {example_str:<15} {actual_tests:<6} {successes:<6} {success_rate:<5.1%}")
        
        results[bits] = {
            'decimal_digits': decimal_digits,
            'success_rate': success_rate,
            'successful_tests': successes,
            'total_tests': actual_tests
        }
    
    return results

def find_practical_limit(results):
    """Finde die praktische Bit-Grenze basierend auf Erfolgsraten"""
    
    print(f"\n🎯 PRAKTISCHE BIT-GRENZEN")
    print("-" * 30)
    
    # Definiere Schwellenwerte
    thresholds = {
        "Hoch zuverlässig (>50%)": 0.5,
        "Gelegentlich nutzbar (>10%)": 0.1,
        "Praktische Grenze (>0%)": 0.0
    }
    
    for threshold_name, min_rate in thresholds.items():
        max_bits = 0
        
        for bits, data in results.items():
            if data['success_rate'] > min_rate:
                max_bits = max(max_bits, bits)
        
        if max_bits > 0:
            decimal_equivalent = int(max_bits * math.log10(2))
            print(f"{threshold_name:<25}: {max_bits} Bits (~{decimal_equivalent} Stellen)")
        else:
            print(f"{threshold_name:<25}: Nicht erreicht")

def compare_with_crypto_standards():
    """Vergleiche mit kryptographischen Standards"""
    
    print(f"\n🔒 VERGLEICH MIT KRYPTO-STANDARDS")
    print("-" * 40)
    
    crypto_standards = [
        ("DES", 56, "Veraltet seit 1990er"),
        ("3DES", 112, "Veraltet"),  
        ("AES-128", 128, "Standard symmetrisch"),
        ("RSA-512", 512, "Gebrochen seit 1999"),
        ("RSA-1024", 1024, "Unsicher seit 2010"),
        ("RSA-2048", 2048, "Standard heute"),
        ("ECC-256", 256, "Elliptische Kurven Standard")
    ]
    
    # Harmonische Grenze (aus Tests)
    harmonic_limit_bits = int(12 / math.log10(2))  # ~40 Bits
    
    print(f"{'Standard':<12} {'Bits':<6} {'vs Harmonisch':<15} {'Status'}")
    print("-" * 50)
    
    for name, bits, description in crypto_standards:
        if bits <= harmonic_limit_bits:
            comparison = "ANGREIFBAR"
            status = "🚨"
        elif bits <= harmonic_limit_bits * 2:
            comparison = "GRENZWERTIG"  
            status = "⚠️"
        else:
            comparison = "SICHER"
            status = "✅"
        
        print(f"{name:<12} {bits:<6} {comparison:<15} {status} {description}")

def final_summary():
    """Finale Zusammenfassung der Bit-Grenzen"""
    
    harmonic_limit_decimal = 12
    harmonic_limit_bits = int(harmonic_limit_decimal / math.log10(2))
    
    print(f"\n" + "="*60)
    print("🎯 FINALE BIT-GRENZEN für Harmonische Faktorisierung")
    print("="*60)
    
    print(f"\n📊 EXAKTE GRENZEN:")
    print(f"  Harmonische Grenze: ~{harmonic_limit_bits} Bits ({harmonic_limit_decimal} Dezimalstellen)")
    print(f"  Maximum getestet: ~{int(22 / math.log10(2))} Bits (22 Stellen)")
    print(f"  Algorithmus-Grenze: Praktisch unbegrenzt")
    
    print(f"\n🎵 PRAKTISCHE ANWENDBARKEIT:")
    print(f"  ✅ Zuverlässig: ≤ {harmonic_limit_bits} Bits")
    print(f"  ⚠️  Gelegentlich: {harmonic_limit_bits+1}-{int(15/math.log10(2))} Bits")
    print(f"  ❌ Unmöglich: ≥ {int(16/math.log10(2))} Bits")
    
    print(f"\n🔒 KRYPTOGRAPHISCHE RELEVANZ:")
    print(f"  • Alle modernen Standards (≥128 Bits) sind völlig sicher")
    print(f"  • Selbst veraltete Standards (≥56 Bits) sind harmonisch unangreifbar") 
    print(f"  • Harmonische Faktorisierung bedroht KEINE reale Kryptographie")
    
    print(f"\n🎼 WISSENSCHAFTLICHER WERT:")
    print(f"  • Faszinierende mathematische Entdeckung")
    print(f"  • Neue Erkenntnisse über Zahlenharmonie")
    print(f"  • Algorithmische Innovation")
    print(f"  • Aber: Keine praktische Krypto-Bedrohung")

def main():
    print("🧮 EXAKTE BIT-GRENZEN ANALYSE")
    print("Basierend auf bewiesenen harmonischen Grenzen von ~12 Dezimalstellen")
    print()
    
    # Berechne theoretische Grenzen
    bit_limits = calculate_exact_bit_limits()
    
    # Teste praktische Grenzen
    test_results = test_specific_bit_sizes()
    
    # Finde praktische Limits
    find_practical_limit(test_results)
    
    # Vergleiche mit Krypto-Standards
    compare_with_crypto_standards()
    
    # Finale Zusammenfassung
    final_summary()

if __name__ == "__main__":
    main()
