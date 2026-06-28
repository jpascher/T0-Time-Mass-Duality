"""
Is the 3 (+) 3' doubling already the first golden recursion -- and are recursion directions
empty in the compact picture? Yes. The Fibonacci/inflation operator M=[[1,1],[1,0]] has two
eigendirections: phi (expanding -> the physical '3', crystallographic core, masses) and -1/phi
(contracting -> the internal '3', the cut-and-project window). Physical content lives only in
the expanding/crystallographic branch; the contracting internal branch and all higher recursion
levels carry NO new mass content -> 'empty'. numpy only.
"""
import numpy as np
phi=(1+5**0.5)/2
M=np.array([[1,1],[1,0]],float)
ev,U=np.linalg.eig(M)
order=np.argsort(ev)            # -1/phi first, phi second
print("Fibonacci recursion operator M=[[1,1],[1,0]]:")
for e in ev: 
    lbl="phi  (expanding -> physical '3', crystallographic, MASSES)" if e>0 else "-1/phi (contracting -> internal '3'', the window, EMPTY)"
    print(f"   eigenvalue {e:+.5f}  -> {lbl}")
print(f"   check: phi={phi:.5f}, -1/phi={-1/phi:.5f}\n")

# iterate on a generic seed; track physical (phi) vs internal (-1/phi) components
v_phi   = U[:,np.argmax(ev)]; v_int = U[:,np.argmin(ev)]
x=np.array([1.0,0.3])
print("iterate M^n on a generic vector -- physical grows, internal vanishes:")
for n in [0,1,2,4,8]:
    y=np.linalg.matrix_power(M,n)@x
    cph=abs(np.dot(y,v_phi)); cin=abs(np.dot(y,v_int))
    print(f"   n={n:>2}: |physical(phi)|={cph:9.3f}   |internal(3')| ~ (1/phi)^n -> {cin:.4f}")
print("\n=> The 3 (+) 3' doubling IS the recursion's eigenstructure (one application of M).")
print("   3  = expanding physical branch = the crystallographic core where masses sit.")
print("   3' = contracting internal branch = the window: it carries no physical positions,")
print("        and under iteration it -> 0. That is why it is empty.")
print("   General: the seed (crystallographic '3') holds the masses; everything the golden")
print("   recursion generates from it -- the conjugate 3' and the phi^n tower -- is empty of")
print("   NEW mass content (it carries self-similar structure, not new sharp levels).")
print("   So 'recursion directions are empty in the compact picture' = '3' is empty' =")
print("   'masses need the crystallographic core' -- one statement.")
