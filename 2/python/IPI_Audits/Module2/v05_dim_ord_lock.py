#!/usr/bin/env python3
"""
v05 — An unremarked coupling: dim = 2 * ord_h(2) at all three storeys,
      and it is contingent, not forced.

NB04 section 4b lists the dimensions (8/24/120) as item 2 and the tick periods
(4/12/60) as item 3, as two independent forced facts. They are locked at ratio
2 — but the lock is a property of 2 modulo h, not of the tower construction.

Self-contained: sympy only.
"""
from sympy import n_order, lcm, isprime

print(__doc__)
print("=" * 72); print("The coupling"); print("=" * 72)
print(f"  {'p':>4} {'h=p(p+2)':>10} {'d=p^2-1':>9} {'ord_h(2)':>9} {'d/ord':>6} "
      f"{'lambda(h)':>10} {'ord=lambda':>11}")
print("  " + "-" * 64)
for p in (3, 5, 11):
    h, d = p * (p + 2), p * p - 1
    o, lam = int(n_order(2, h)), int(lcm(p - 1, p + 1))
    print(f"  {p:>4} {h:>10} {d:>9} {o:>9} {d // o:>6} {lam:>10} {str(o == lam):>11}")

print("""
  For odd p, gcd(p-1, p+1) = 2, so lambda(h) = lcm(p-1, p+1) = (p^2-1)/2 = d/2.
  Hence ord_h(2) DIVIDES d/2 always. Equality — i.e. 2 having maximal order
  mod h — is what makes the periods come out as exactly half the dimensions.
  That is an extra condition, and it is not derived anywhere in the chain.
""")

print("=" * 72); print("Is it automatic for twin products?  No."); print("=" * 72)
print(f"  {'p':>5} {'ord_h(2)':>10} {'lambda(h)':>10} {'equal':>7}")
print("  " + "-" * 36)
hits = tot = 0
for p in range(3, 250):
    if isprime(p) and isprime(p + 2):
        h = p * (p + 2)
        o, lam = int(n_order(2, h)), int(lcm(p - 1, p + 1))
        tot += 1; hits += (o == lam)
        print(f"  {p:>5} {o:>10} {lam:>10} {str(o == lam):>7}"
              + ("   <- tower member" if p in (3, 5, 11) else ""))
print(f"\n  equality holds for {hits} of {tot} twin lower-members below 250.")
print("""
  So the elegant reading "dimensions 8/24/120, periods exactly half of them"
  is contingent: it holds at 3, 5, 11 and fails at 17, 29, 41, 71, ...

  Two honest options:
    (a) there is a reason 2 has maximal order at exactly the tower conductors
        — then it belongs in the chain as a sixth item, and it is a genuine
        result;
    (b) there is not — then items 2 and 3 must not be presented as mutually
        reinforcing, because their agreement is an accident of the number 2.

  Either way it is better found by you than by a referee.
""")
