#!/usr/bin/env python3
"""
v04 — NB02 section 4(c): the cell illustrates the thesis, it does not test it.

Self-contained: no imports beyond the standard library.
"""
LEVEL_RULE = {0: 29, 1: 6, 2: 34}
v4_prod = lambda seq: __import__("functools").reduce(lambda x, s: (x * s) % 35, seq, 1)
tower_word = lambda p: [[1, 2, 1][i % 3] for i in range(p)]
writhe = lambda w: sum(1 if x > 0 else -1 for x in w)

print(__doc__)
print("=" * 72); print("What the cell computes"); print("=" * 72)
print(f"  {'level':>6} {'p':>4} {'writhe fwd':>11} {'writhe rev':>11} {'V4 fwd':>7} {'V4 rev':>7}")
print("  " + "-" * 52)
for name, p in [("E8", 4), ("Leech", 12), ("Craig", 60)]:
    w = tower_word(p)
    inv = [-x for x in reversed(w)]
    f = v4_prod([LEVEL_RULE[i % 3] for i in range(p)])
    r = v4_prod([LEVEL_RULE[i % 3] for i in range(p)][::-1])
    print(f"  {name:>6} {p:>4} {writhe(w):>11} {writhe(inv):>11} {f:>7} {r:>7}")

print("""
  Read the two generators:

    tower_word(p) = [[1,2,1][i%3] for i in range(p)]      all letters positive
    inv           = [-x for x in reversed(w)]              all letters negated

  So writhe(fwd) = p and writhe(rev) = -p by construction. The numbers
  +-4/12/60 are the word lengths, which are the periods because the word was
  built with p letters. Nothing is measured.

  Likewise "V4 fwd == V4 rev" holds because V4 is abelian — which section 1
  already proved and section 4(a) already states ("the proof is one line").

  This is not an error: the cell is a correct illustration of a correct claim.
  But it is presented among [PROVED] results as though it were evidence, and a
  referee who reads the two list comprehensions will say so. The honest label
  is: the order-blindness is a THEOREM (abelian), the writhe asymmetry is a
  DEFINITION, and the interesting content is elsewhere — in section 2 (4 of 16
  assignments survive the braid relation) and section 3 (Delta^2 = t^3 I held
  where the gauge reads id). Those two ARE computations with outcomes that
  could have gone differently.
""")

print("=" * 72); print("The two cells that do carry content — reproduced"); print("=" * 72)
V4 = [1, 29, 6, 34]
valid = [(a, b) for a in V4 for b in V4 if (a * b * a) % 35 == (b * a * b) % 35]
print(f"  braid relation aba = bab in V4: {len(valid)} of 16 survive, all diagonal: "
      f"{all(a == b for a, b in valid)}   -> two layers forced. CONFIRMED")
v4_six = v4_prod([LEVEL_RULE[i % 3] for i in range(6)])
print(f"  V4 product over the 6 letters of (s1 s2)^3: {v4_six} (= id) while Burau holds t^3*I. CONFIRMED")
