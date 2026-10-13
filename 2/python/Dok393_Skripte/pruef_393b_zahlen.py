#!/usr/bin/env python3
"""
pruef_393b_zahlen.py — Dok. 393: alle übrigen Zahlen im Text.
Farey-Höhe, Mittelung, Balmer-Verhältnisse, Lernschranken aus Dok. 359,
Born-Häufigkeit, Stellenzahl der Gewichte.
"""
from fractions import Fraction
from math import pi, sqrt, log, log10, ceil, gcd
ok = tot = 0
def check(name, cond, detail=""):
    global ok, tot
    tot += 1; ok += bool(cond)
    print(f"[{'OK ' if cond else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

XI = Fraction(1, 7500)
# Z1/Z2: Farey-Höhe Q_c = pi/sqrt(6 eps) (Dok. 343 G', Dok. 359 Satz B)
q1 = pi / sqrt(6 * 0.0105); q2 = pi / sqrt(6 * 100 * float(XI))
check("Z1 Q_c bei 1,05 % ≈ 12,5", abs(q1 - 12.5) < 0.05, f"{q1:.2f}")
check("Z2 Q_c bei 100ξ = 1,33 % ≈ 11,1", abs(q2 - 11.1) < 0.05, f"{q2:.2f}")

# Z3: Mittelung — 100-fache Messzahl senkt Rauschen auf 1/10
check("Z3 Rauschen ∝ 1/√N: N×100 → Faktor 10", abs(1 / sqrt(100) - 0.1) < 1e-12)

# Z4–Z6: Balmer (Luftwellenlängen NIST, nm) gegen exakte Brüche
lam = {3: 656.279, 4: 486.135, 5: 434.047, 6: 410.174}
def ratio(a, b):   # λ_a/λ_b = (1/4-1/b²)/(1/4-1/a²)
    return (Fraction(1, 4) - Fraction(1, b * b)) / (Fraction(1, 4) - Fraction(1, a * a))
for (a, b), exp in (((3, 4), Fraction(27, 20)), ((4, 5), Fraction(28, 25)), ((5, 6), Fraction(200, 189))):
    r = ratio(a, b); m = lam[a] / lam[b]
    check(f"Z{3 + a - 2} Balmer λ{a}/λ{b} = {exp} exakt, Messung auf 1e-5",
          r == exp and abs(m / float(r) - 1) < 1e-5, f"{m:.6f} vs {float(r):.6f}")

# Z7–Z9: Lernschranken (Dok. 359 Satz D)
dom = [(p, q) for p in range(1, 101) for q in range(1, 101) if gcd(p, q) == 1]
eps = delta = 0.05
m_free = ceil((len(dom) * log(2) + log(1 / delta)) / eps)
m_struct = ceil((25 * log(2) + log(1 / delta)) / eps)
check("Z7 Raster 6087 Brüche", len(dom) == 6087)
check("Z8 ohne Strukturannahme ≈ 84 000 Beispiele", 84000 <= m_free <= 85000, str(m_free))
check("Z9 mit Primfaktor-Struktur ≤ 407 Beispiele", m_struct == 407)

# Z10: Born-Häufigkeit 2/9 — Streuung bei N Ereignissen, Trennung von 1/5
p = 2 / 9; gap = p - 1 / 5
N = ceil((3 * sqrt(p * (1 - p)) / gap) ** 2)
check("Z10 2/9 gegen 1/5 auf 3σ trennbar ab rund 3200 Ereignissen", 3100 <= N <= 3200, str(N))

# Z11: Stellenzahl der Gewichte
d16 = log10(2 ** 11); dbf = log10(2 ** 8)
check("Z11 16-Bit-Gewicht: 2,4 (bfloat16) bis 3,3 (float16) Dezimalstellen",
      abs(dbf - 2.41) < 0.01 and abs(d16 - 3.31) < 0.01, f"{dbf:.2f} / {d16:.2f}")

print(f"\n{ok}/{tot} Prüfungen bestanden")
raise SystemExit(0 if ok == tot else 1)
