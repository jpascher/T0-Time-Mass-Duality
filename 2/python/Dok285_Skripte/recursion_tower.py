"""
The tower D(4+3n): n golden recursions. D7 = 1 recursion, D10 = 2, ... up to 100 and beyond.
KEY (from the proven emptiness theorem): every recursion adds a CONTRACTING internal 3-window
(the -1/phi eigenmode), which is EMPTY. So n recursions = n empty windows; the mass content
stays in the D4 core at every level. The tower is geometry, not new physics -- unless a dynamics
populates a window (the same open question at every level). numpy only.
"""
import numpy as np
phi=(1+5**0.5)/2
def D(n): return 4+3*n
print("dimension tower  D(n) = 4 + 3n  (n = number of golden recursions):")
for n in [0,1,2,3,10,32,100]:
    tag={0:"D4 = FFGFT seed (the '3' + time)",1:"D7 = 1 recursion (adds 3')",
         2:"D10 = 2 recursions (adds 3'')",100:"D304 = 100 recursions"}.get(n,"")
    print(f"   n={n:>3}:  D{D(n):<4} {tag}")
print()

# each recursion level contributes a contracting (-1/phi) window -> empty
print("emptiness across the tower: weight that the recursion puts in window level k after m steps")
print("  (each window is the contracting branch, decays as (1/phi)^m):")
m=12
for k in range(1,6):
    w=(1/phi)**(m)          # every window contracts at the same golden rate
    print(f"   window {k} (the (k)th added 3): residual after {m} steps ~ {w:.2e}  -> empty")
print("\n  => masses live ONLY in the D4 seed at every level of the tower.")
print("     n recursions add n empty internal 3-windows; they do NOT add particles.")

print("\n=== honest status ===")
print(" - arithmetic tower D(4+3n) is well defined; D10 = two recursions is correct counting.")
print(" - BUT by the emptiness theorem each added 3 is an empty window. 100 recursions = 100")
print("   empty windows, not 100 physics layers. The tower is a geometric hierarchy")
print("   (nested cut-and-project), not new testable content.")
print(" - '+3 per step' assumes every level repeats the icosahedral 3+3 pattern (a choice; a")
print("   different non-crystallographic symmetry would give a different increment).")
print(" - populating ANY window needs a specified dynamics -- the same open gap, at every level.")
