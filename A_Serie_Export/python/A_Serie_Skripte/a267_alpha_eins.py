"""A267: alpha=1 Setzung, Umrechnungstabelle, 137-Leiter."""
import math
alpha = 1/137.036
m_e = 0.511  # MeV, nat. Einheiten c=hbar=1

print("=== A267: alpha=1 Setzung ===")
# e = sqrt(4*pi*alpha)
e_phys = math.sqrt(4*math.pi*alpha)
e_a1   = math.sqrt(4*math.pi)
print(f"e(phys) = {e_phys:.6f}, e(alpha=1) = {e_a1:.6f}")
print(f"e(alpha=1)/e(phys) = {e_a1/e_phys:.6f} = 1/sqrt(alpha) = {1/math.sqrt(alpha):.6f}")
assert abs(e_a1/e_phys - 1/math.sqrt(alpha)) < 1e-10

# Umrechnungstabelle (alle Groessen in nat. Einheiten, r in MeV^-1, E in MeV)
# Coulomb: V = alpha/r,  r=1/m_e -> V = alpha*m_e
# bei alpha=1: V_a1 = m_e
# Rueckfaktor: V/V_a1 = alpha
checks = [
    ("Coulomb V",      alpha*m_e,          m_e,           1),
    ("r_e",            alpha/m_e,          1/m_e,         1),
    ("lambda_C",       1/m_e,              1/m_e,         0),
    ("a_0",            1/(alpha*m_e),      1/m_e,        -1),
    ("Rydberg",        0.5*alpha**2*m_e,   0.5*m_e,       2),
]
print("\nUmrechnungstabelle:")
for name, val, val_a1, n in checks:
    ratio = val/val_a1
    exp   = alpha**n
    ok = abs(ratio-exp)/max(abs(exp),1e-30) < 1e-8
    print(f"  alpha^{n:+d}  {name:12s}: {ratio:.4e} vs {exp:.4e} {'v' if ok else 'X'}")
    assert ok, name

# 137-Leiter
r_e = alpha/m_e; lC = 1/m_e; a0 = 1/(alpha*m_e)
assert abs(r_e/lC - alpha) < 1e-10
assert abs(a0/lC - 1/alpha) < 1e-6
print(f"\n137-Leiter: r_e:lambda_C:a_0 = alpha:1:1/alpha v")

print("\nAlle Checks bestanden.")
