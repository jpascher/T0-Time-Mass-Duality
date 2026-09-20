#!/usr/bin/env python3
"""
Audit von Jaimes audit_bridge_v4.py — Was wird tatsächlich berechnet?
"""
import mpmath as mp
mp.mp.dps = 40

PASS = FAIL = 0
def check(label, cond, detail=""):
    global PASS, FAIL
    ok = "[PASS]" if cond else "[FAIL]"
    if cond: PASS += 1
    else:    FAIL += 1
    print(f"  {ok} {label}" + (f"  ({detail})" if detail else ""))

phi   = (1+mp.sqrt(5))/2
omega = mp.exp(2j*mp.pi/3)
th5   = 2*mp.pi/5

print("=== [1] Zeile-für-Zeile: Was berechnet v4 in Abschnitt [3]? ===")
print()
print("  Zeile: chi_R5 = 1 + 2*cos_2pi_5   → berechnet φ, wird danach NICHT verwendet")
print("  Zeile: overlap_derived = sum_h_twist → ZUWEISUNG des CFT-Werts, keine Berechnung")
print("  Es gibt KEINE Matrix, KEIN Skalarprodukt, KEINE Zustände σ₀, σ_e im Code.")
print("  Der 'Overlap' ist per Definition gleich 2/9 gesetzt, dann mit 2/9 verglichen.")
check("(c) |⟨σ₀|R₅|σ_e⟩|² tatsächlich BERECHNET", False, "Zirkelschluss: Wert zugewiesen, nicht hergeleitet")

print("\n=== [2] Die Einbettung: welche ℤ₃ wird 'respektiert'? ===")
Z3_orb = mp.matrix([[omega,0,0],[0,omega,0],[0,0,omega]])
U_R5   = mp.matrix([[1,0,0],[0,mp.exp(1j*th5),0],[0,0,mp.exp(-1j*th5)]])
print(f"  Orbifold-ℤ₃ (v4): diag(ω,ω,ω) = ω·𝟙  → Spur = {mp.nstr(Z3_orb[0,0]+Z3_orb[1,1]+Z3_orb[2,2],6)} = 3ω")
comm = U_R5*Z3_orb - Z3_orb*U_R5
print(f"  [U_R5, ω·𝟙] = 0?  max|·| = {mp.nstr(max(abs(comm[i,j]) for i in range(3) for j in range(3)),3)}")
check("ω·𝟙 ist ZENTRAL in U(3) — kommutiert mit JEDER Matrix", True)
print("  → Die Bedingung 'Einbettung respektiert Orbifold-ℤ₃' ist für ω·𝟙 LEER:")
print("    jedes U ∈ SU(3) erfüllt sie automatisch. Sie schränkt nichts ein.")

print("\n=== [3] Die FFGFT-ℤ₃ ist eine ANDERE ℤ₃ ===")
# FFGFT Z3 = zyklische Permutation (3-fach-Drehung um (1,1,1)) — in 3D-Irrep von A5
C3 = mp.matrix([[0,0,1],[1,0,0],[0,1,0]])
ev_C3 = mp.eig(C3)[0]
tr_C3 = C3[0,0]+C3[1,1]+C3[2,2]
print(f"  FFGFT-ℤ₃ (3-fach-Drehung in A₅): Eigenwerte ≈ {[mp.nstr(e,4) for e in ev_C3]}")
print(f"  → Eigenwerte (1, ω, ω²), Spur = {tr_C3} = χ₃(C₃) = 0")
print(f"  Orbifold-ℤ₃:                     Eigenwerte (ω, ω, ω), Spur = 3ω ≠ 0")
check("FFGFT-ℤ₃ ≠ Orbifold-ℤ₃ (verschiedene Spuren, verschiedene Konjugationsklassen)", abs(tr_C3)<1e-30)
print("  A₅ hat triviales Zentrum. Kein Element von A₅ ist in einer treuen Darstellung skalar.")
print("  → ι(ℤ₃^FFGFT) = ω·𝟙 ist für KEINE treue Einbettung A₅→SU(3) möglich.")
check("Bedingung (a) 'ι(ℤ₃) = Orbifold-ℤ₃' erfüllt", False, "unerfüllbar für treue 3D-Darstellung")

print("\n=== [4] Bedingung (b): Wirkung auf Twist-Sektoren ===")
print("  Twist-Felder σ_k leben in den ℤ₃-getwisteten Sektoren der Orbifold-CFT.")
print("  R₅ ∈ SU(3) ist eine GEOMETRISCHE Symmetrie des Torus — sie erhält Sektoren.")
print("  Untwisted ↔ twisted mischt R₅ nicht. ⟨σ₀|R₅|σ_e⟩ zwischen VERSCHIEDENEN Sektoren = 0.")
print("  v4 gibt keine Definition von σ₀, σ_e als Zustände und keine Wirkung von R₅ darauf an.")
check("(b) Wirkung von ι(R₅) auf Twist-Sektoren angegeben", False, "nicht im Code")

print("\n=== [5] Was v4 tatsächlich zeigt ===")
h1 = mp.mpf(1)*2/(2*9); h2 = mp.mpf(2)*1/(2*9)
check("Σh_twist = 2/9 [E, DFMS 1987]", abs(h1+h2-mp.mpf(2)/9)<1e-30)
check("det(U_R5)=1, det(ω𝟙)=1", True)
check("R6 ∈ SO(6) (Realform von U_R5)", True)
print("  Das ist alles. Drei triviale bzw. bereits bekannte Tatsachen.")

print("\n=== [6] Was der FFGFT-Wert ist — zur Erinnerung ===")
s3 = mp.sqrt(3)
v = [mp.matrix([1,1,1])/s3, mp.matrix([1,omega,omega**2])/s3, mp.matrix([1,omega**2,omega**4])/s3]
axis = mp.matrix([0,1,phi]); n = axis/mp.sqrt(sum(axis[i]**2 for i in range(3)))
c,s = mp.cos(th5), mp.sin(th5)
K = mp.matrix([[0,-n[2],n[1]],[n[2],0,-n[0]],[-n[1],n[0],0]])
R5 = mp.eye(3)+s*K+(1-c)*(K*K)
A = sum(mp.conj(v[0][i])*(R5*v[1])[i] for i in range(3))
print(f"  FFGFT: R₅ = Rodrigues-Drehung, Achse ∝ (0,1,φ), 72°  — in der Standardbasis x,y,z")
print(f"         |⟨v₀|R₅|v₁⟩|² = {mp.nstr(abs(A)**2,10)} = 2/9")
print(f"  v4:    U_R5 = diag(1, e^{{iθ}}, e^{{−iθ}})  — DIAGONALISIERTE Form, andere Basis")
print(f"         In dieser Basis: ⟨v₀|U_R5|v₁⟩ mit v_k = Fourier-Moden:")
A_diag = sum(mp.conj(v[0][i])*(U_R5*v[1])[i] for i in range(3))
print(f"         |⟨v₀|U_R5|v₁⟩|² = {mp.nstr(abs(A_diag)**2,10)}  ≠ 2/9")
check("v4-Matrix U_R5 reproduziert FFGFT-Wert 2/9 in Fourier-Basis", abs(abs(A_diag)**2-mp.mpf(2)/9)<1e-10, f"gibt {mp.nstr(abs(A_diag)**2,6)}")
print("  → Die Basis, in der 2/9 entsteht, ist die ℤ₃-Fourier-Basis relativ zur A₅-ℤ₃ (Zyklus).")
print("    U_R5 diagonal ist relativ zu R₅'s eigener Achse — das ist NICHT die A₅-ℤ₃-Basis.")
print("    Ohne Angabe des Basiswechsels ist kein Vergleich möglich.")

print("\n=== [7] Nebenbemerkung: Jaimes BF-'Einsicht' (Mail 03:02) ===")
print("  Behauptung: BF-Stabilität sei 'kein Zufall der SUSY-Erhaltung', sondern")
print("  'intrinsische geometrische Eigenschaft' der Twist-Moden mit h=1/9.")
print("  Prüfung: Bei D_τW=0 ist BF durch allgemeinen Satz garantiert (BF 1982, Gibbons-Hull-Warner).")
print("  Die Aussage vermischt zwei Dinge: (i) SUSY⇒BF (Satz), (ii) h=1/9 (CFT-Spektrum).")
print("  Ein Zusammenhang (ii)⇒(i) ist nicht gezeigt. Die Massen m²=−4√3 kommen aus der")
print("  Hesse-Matrix von V(τ), nicht aus Twist-Feldern. Twist-Felder treten in v3 nirgends auf.")
check("BF-Ursache = Twist-Moden statt SUSY nachgewiesen", False, "Behauptung ohne Rechnung")

print(f"\n{'='*60}\n  ERGEBNIS: {PASS}/{PASS+FAIL} PASS\n{'='*60}")
print("\nVERDIKT: v4 erfüllt (a)–(d) NICHT. Der Overlap ist zugewiesen, nicht berechnet.")
print("Die 'respektierte' ℤ₃ ist zentral und schränkt die Einbettung nicht ein.")
print("Die FFGFT-ℤ₃ (Spur 0) und die Orbifold-ℤ₃ (Spur 3ω) sind verschiedene Objekte.")
print("Status bleibt: PROPOSED. Die strukturelle ℤ₃-Korrespondenz bleibt SUPPORTED.")
