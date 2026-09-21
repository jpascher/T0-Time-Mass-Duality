#!/usr/bin/env python3
"""
v03 — NB03 section 3: the 84 is forced, the 24+60 split is a flag choice,
      and the sigma29 identification is asserted rather than derived.

Self-contained: numpy + itertools.
"""
import itertools
import numpy as np

roots = []
for i, j in itertools.combinations(range(8), 2):
    for si in (1, -1):
        for sj in (1, -1):
            v = np.zeros(8); v[i] = si; v[j] = sj; roots.append(v)
for s in itertools.product([0.5, -0.5], repeat=8):
    if np.prod([1 if x > 0 else -1 for x in s]) > 0:
        roots.append(np.array(s))
R = np.array(roots)

print(__doc__)
print("=" * 72); print("The 84 is real and forced — but not by sigma29"); print("=" * 72)
print(f"  roots {len(R)}, D8 {int((np.abs(R).max(axis=1) == 1).sum())}, "
      f"S+ {int((np.abs(R).max(axis=1) != 1).sum())}")
counts = [int((R[:, i] == 0).sum()) for i in range(8)]
print(f"  fixed set of the sign flip of axis i, for i = 0..7: {counts}")
print("""
  Every one of the eight coordinate reflections fixes 84 roots, all of D8 type
  (no half-integer root has a zero coordinate). So "84" follows from E8 plus
  "a coordinate reflection" alone. The identification of that reflection with
  sigma29 in (Z/35Z)* is an additional assertion; NB03 states it in a [PROVED]
  section without deriving it. It is the one step in that section that carries
  the framework, and it should carry a tag.
""")

print("=" * 72); print("The 24 + 60 split depends on which axes are 'inner'"); print("=" * 72)
fixed = R[:, 7] == 0
print(f"  {'inner axes':>11} | {'split of 84':>16}")
print("  " + "-" * 32)
for k in range(2, 8):
    inner = int((fixed & (np.abs(R[:, k:7]).sum(axis=1) == 0)).sum())
    mark = "   <- NB03's choice" if k == 4 else ""
    print(f"  {'first ' + str(k):>11} | {inner:>6} + {84 - inner:<7}{mark}")
print("""
  With 3 inner axes the seam is 12 + 72, with 5 it is 40 + 44. The number 24 is
  genuine — it is the D4 root system sitting inside the slice — but the
  DECOMPOSITION 84 = 24 + 60 is a choice of flag, not a consequence of the
  geometry. "84 = 24 + 60 is geometry, not numerology" is half true: the 84 is
  geometry, the split is a convention. Naming the convention costs nothing and
  removes the only handle a hostile reader has on that section.
""")
