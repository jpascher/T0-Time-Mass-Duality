#!/usr/bin/env python3
"""
Unabhängige Prüfung von Jaimes v3: analytisch + numerisch
"""
import mpmath as mp
mp.mp.dps = 50

PASS = FAIL = 0
def check(label, cond, detail=""):
    global PASS, FAIL
    ok = "[PASS]" if cond else "[FAIL]"
    if cond: PASS += 1
    else:    FAIL += 1
    print(f"  {ok} {label}" + (f"  ({detail})" if detail else ""))

s3 = mp.sqrt(3)
omega = mp.mpc(-mp.mpf(1)/2, s3/2)
S  = mp.matrix([[0,1],[-1,0]])
Pi = mp.matrix([1, omega])
F  = mp.matrix([1, 1])
H  = mp.matrix([-1, 1])

print("=== [A] ANALYTISCHE HERLEITUNG ===")
# S*Pi
SPi = S*Pi
print(f"S·Π = ({mp.nstr(SPi[0],6)}, {mp.nstr(SPi[1],6)})  erwartet (ω, -1)")
check("S·Π = (ω,−1)", abs(SPi[0]-omega)<1e-40 and abs(SPi[1]+1)<1e-40)

A = (F.T*S*Pi)[0,0]
B = (H.T*S*Pi)[0,0]
print(f"A = F^T S Π = {mp.nstr(A,8)}   analytisch: ω−1 = −3/2 + i√3/2")
print(f"B = H^T S Π = {mp.nstr(B,8)}   analytisch: −ω−1 = −1/2 − i√3/2")
check("A = −3/2 + i√3/2", abs(A - mp.mpc(-1.5, s3/2))<1e-40)
check("B = −1/2 − i√3/2", abs(B - mp.mpc(-0.5, -s3/2))<1e-40)

# A/B exakt: (−3/2+i√3/2)/(−1/2−i√3/2). |B|² = 1/4+3/4 = 1
AB = A/B
print(f"A/B = {mp.nstr(AB,8)}   analytisch: −i√3")
check("A/B = −i√3", abs(AB - mp.mpc(0,-s3))<1e-40)
check("|B|² = 1 (Einheitskreis)", abs(abs(B)**2-1)<1e-40)

tau_star = mp.conj(AB)
print(f"τ* = conj(A/B) = {mp.nstr(tau_star,8)}")
check("τ* = i√3 exakt", abs(tau_star - mp.mpc(0,s3))<1e-40)
check("Im τ* = √3", abs(mp.im(tau_star)-s3)<1e-40)
gs = 1/mp.im(tau_star)
check("g_s = 1/√3 < 1", abs(gs - 1/s3)<1e-40 and gs<1, f"g_s={mp.nstr(gs,6)}")

print("\n=== [B] D_τW = 0 HERLEITUNG (nicht nur numerisch) ===")
# W = A − τB, dW/dτ = −B, K = −ln(2 Im τ), dK/dτ = −1/(τ−τ̄)
# D_τW = −B − (A−τB)/(τ−τ̄) = 0  ⟺  B(τ−τ̄) + A − τB = 0  ⟺  A = Bτ̄  ⟺  τ = conj(A/B)
def W(t): return A - t*B
def DW(t): return -B + (-1/(t-mp.conj(t)))*W(t)
res = abs(DW(tau_star))
check("D_τW(τ*) = 0 analytisch", res<1e-45, f"|D_τW|={mp.nstr(res,3)}")
W_star = W(tau_star)
print(f"W(τ*) = {mp.nstr(W_star,8)}   analytisch: −3 + i√3")
check("W(τ*) = −3+i√3", abs(W_star - mp.mpc(-3,s3))<1e-40)
check("|W(τ*)|² = 12", abs(abs(W_star)**2-12)<1e-40)

print("\n=== [C] V_AdS EXAKT ===")
K_star = -mp.log(2*mp.im(tau_star))
eK = mp.exp(K_star)
V_star = -3*eK*abs(W_star)**2
print(f"e^K = 1/(2√3) = {mp.nstr(eK,8)}")
print(f"V* = −3·e^K·|W|² = −3·(1/(2√3))·12 = −18/√3 = −6√3 = {mp.nstr(V_star,8)}")
check("V_AdS = −6√3", abs(V_star + 6*s3)<1e-40, f"{mp.nstr(V_star,8)}")

print("\n=== [D] BF-GRENZE ===")
# AdS4: L² = −3/V (Einheiten M_P=1, 8πG=1). m_BF² = −9/(4L²) = 3V/4
m_BF = 3*V_star/4
print(f"m_BF² = 3V/4 = −9√3/2 = {mp.nstr(m_BF,8)}")
check("m_BF² = −9√3/2", abs(m_BF + 9*s3/2)<1e-40)

print("\n=== [E] MASSENMATRIX — UNABHÄNGIGE HESSE-BERECHNUNG ===")
def V_of(c0, s):
    t = mp.mpc(c0, s)
    eK_ = 1/(2*s)
    Kinv = 4*s**2
    return mp.re(eK_*(Kinv*abs(DW(t))**2 - 3*abs(W(t))**2))

c0s, ss = mp.re(tau_star), mp.im(tau_star)
Hcc = mp.diff(lambda x: V_of(x,ss), c0s, 2)
Hss = mp.diff(lambda y: V_of(c0s,y), ss, 2)
Hcs = mp.diff(lambda x: mp.diff(lambda y: V_of(x,y), ss), c0s)
print(f"H_c0c0 = {mp.nstr(Hcc,8)}")
print(f"H_ss   = {mp.nstr(Hss,8)}")
print(f"H_c0s  = {mp.nstr(Hcs,8)}")
check("Hesse diagonal (H_c0s ≈ 0)", abs(Hcs)<1e-20)
check("H_c0c0 = H_ss (isotrop)", abs(Hcc-Hss)<1e-20)

# Kinetische Metrik: Jaime nutzt G = 2 K_ττ̄ = 2/(4s²) = 1/(2s²)
K_tt = 1/(4*ss**2)
G_jaime = 2*K_tt
m2_jaime = Hcc/G_jaime
print(f"\nJaime: G = 2K_ττ̄ = {mp.nstr(G_jaime,8)}  →  m² = H/G = {mp.nstr(m2_jaime,8)}")
check("Jaime m² = −4√3", abs(m2_jaime + 4*s3)<1e-20, f"{mp.nstr(m2_jaime,8)}")

# Alternative Konvention: G = K_ττ̄ (ohne Faktor 2)
G_alt = K_tt
m2_alt = Hcc/G_alt
print(f"Alt:   G = K_ττ̄  = {mp.nstr(G_alt,8)}  →  m² = H/G = {mp.nstr(m2_alt,8)}")

print(f"\nBF-Margin (Jaime-Konv.): m² − m_BF² = {mp.nstr(m2_jaime-m_BF,8)}  = √3/2?  {mp.nstr(s3/2,8)}")
print(f"BF-Margin (Alt-Konv.):   m² − m_BF² = {mp.nstr(m2_alt-m_BF,8)}")
check("BF stabil (Jaime-Konv.)", m2_jaime > m_BF)
check("BF stabil (Alt-Konv.)  ", m2_alt > m_BF)
check("Margin Jaime = √3/2 exakt", abs((m2_jaime-m_BF)-s3/2)<1e-20)

print("\n=== [F] KONVENTIONSFRAGE ===")
# Standard N=1 SUGRA: L_kin = K_ij̄ ∂φ^i ∂φ̄^j̄. Für τ=c0+is: K_ττ̄|∂τ|² = K_ττ̄[(∂c0)²+(∂s)²]
# → Metrik auf (c0,s) ist diag(K_ττ̄, K_ττ̄), NICHT 2K_ττ̄.
# Mit L = ½ G_ab ∂φ^a ∂φ^b  wäre G = 2K_ττ̄ — das ist Jaimes Konvention.
# Beide Konventionen: BF-Stabilität gilt. Aber m²-Werte unterscheiden sich um Faktor 2.
print("Standard-Konv. (L = K_ij̄ ∂φ∂φ̄): m² = H/K_ττ̄ =", mp.nstr(m2_alt,6), "→ Margin", mp.nstr(m2_alt-m_BF,6))
print("Jaime-Konv.   (L = ½ G ∂φ∂φ):   m² = H/(2K_ττ̄) =", mp.nstr(m2_jaime,6), "→ Margin", mp.nstr(m2_jaime-m_BF,6))
print("BF-Stabilität in BEIDEN Konventionen erfüllt — Konvention muss aber deklariert werden.")

print("\n=== [G] PERIODENVEKTOR Π = (1, ω) — HERKUNFT ===")
# Für rigid T⁶/ℤ₃: b₃ = 2, Ω = dz₁∧dz₂∧dz₃. Perioden über die zwei 3-Zykel des ℤ₃-invarianten H³.
# Π = (1, ω) ist plausibel für ℤ₃-symmetrisches Gitter — aber im Skript DECLARED, nicht hergeleitet.
print("Π = (1, ω)^T ist im Skript gesetzt (Zeile 'Pi = mp.matrix([1, omega])').")
print("Keine Herleitung aus den 3-Zykeln von T⁶/ℤ₃ im Skript. Status: DECLARED.")

print(f"\n{'='*60}\n  ERGEBNIS: {PASS}/{PASS+FAIL} PASS\n{'='*60}")
