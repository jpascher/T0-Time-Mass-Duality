#!/usr/bin/env python3
"""
v02 — NB04 section 4b: item 4 is item 2 restated, and the recursion is a choice.

The claim under test is "zero free parameters — the whole spine is forced".
Items 1, 3 and 5 of that chain are confirmed here. Items 2 and 4 are not
independent, and item 2 is not derived from item 1.

Self-contained: sympy only.
"""
import sympy as sp
from sympy import isprime, integer_nthroot, n_order

print(__doc__)
print("=" * 72); print("ITEM 1 — the seed is forced.  CONFIRMED"); print("=" * 72)
sols = []
for k in range(1, 200):
    r, ok = integer_nthroot(2**(k + 1), 2)
    if ok and isprime(r - 1) and isprime(r + 1):
        sols.append((k, r - 1, r + 1))
print(f"  sigma(2^k) = 2^(k+1)-1 = p(p+2) requires 2^(k+1) = (p+1)^2.")
print(f"  Solutions with p, p+2 prime, k < 200: {sols}")
print("  Together with the mod-3 argument this is a theorem, not a scan. Confirmed.\n")

print("=" * 72); print("ITEMS 2 & 4 — not two facts.  ONE fact, stated twice."); print("=" * 72)
p = sp.symbols("p")
lhs = (p**3 - p + 1) - 1          # d' = p'^2 - 1, using the recursion
rhs = p * (p**2 - 1)              # p * d
print(f"  recursion:      p'^2 = p^3 - p + 1")
print(f"  subtract 1:     p'^2 - 1 = p^3 - p = p(p^2 - 1)")
print(f"  i.e.            d'      = p * d")
print(f"  sympy check ((p^3-p+1)-1) - p(p^2-1) = {sp.simplify(lhs - rhs)}")
print("""
  So the recursion IS the statement "each storey holds p copies of the last".
  NB04 item 4 ("the nesting multiplicities are the seed itself — the pair
  (3,5) reappearing as geometry") is therefore item 2 written backwards. The
  multiplicity does not reappear; it was put in when the recursion was chosen.
""")

print("=" * 72); print("Is the recursion derived from the seed?  Counter-test."); print("=" * 72)
print("  Generalise to d' = m*d, i.e. p' = sqrt(m*(p^2-1) + 1), same start p = 3:\n")
print(f"  {'m':>3} | tower")
print("  " + "-" * 40)
for m in range(2, 13):
    q, tower = 3, [3]
    for _ in range(5):
        n = m * (q * q - 1) + 1
        r, ok = integer_nthroot(n, 2)
        if not ok:
            break
        q = r; tower.append(q)
    print(f"  {m:>3} | {tower}")
print("""
  m = p gives 3 -> 5 -> 11; m = 6 gives 3 -> 7 -> 17. Both terminate, both are
  "forced" once m is fixed. Nothing in item 1 selects m = p. That is a
  structural choice, and it is the one the whole spine rests on.

  This does not make the spine wrong. It makes "zero free parameters" the
  wrong description of it: the parameters are zero, the structural choice is
  one, and stating it that way is unattackable where the present phrasing is
  not.
""")

print("=" * 72); print("ITEMS 3 & 5 — CONFIRMED"); print("=" * 72)
print("  ord_h(2):", {h: int(n_order(2, h)) for h in (15, 35, 143)})
tors = sorted(x for x in range(1, 35) if sp.gcd(x, 35) == 1 and (x * x) % 35 == 1)
print("  2-torsion of (Z/35Z)*:", tors, "-> V4 unique. Confirmed.")
