"""
pruef_343e_dok186_check.py — Was aus Dok. 186 (FFGFT-Photonik) berechenbar ist,
geprüft gegen Dok. 328 (Kopplungsregime) und Dok. 343 (Auflösungsschwellen).
A  TFLN-Güte Q>10⁶: welche FFGFT-Skalen sind damit auflösbar?
B  "Einrasten" f_n = φ^-k f0 gegen Arnold-Zungen bei K_eff = 2πξ
C  50-GHz-Bandbreite als "Zugang zu Harmonischen von ξ": welche Stufe k?
D  Sweet-Spot-Leiter aus Dok. 034/162 (6,24 / 2,38 GHz): Konsistenz, Lage von 50 GHz
E  B-Meson: kann α = ξ eine 4σ-Abweichung erzeugen? Statistik-Test
F  Wicklungszahlen r_e = 4/3, r_μ = 16/5 (Dok. 338) gegen Fibonacci-Bedingung N ∈ {F_k}
"""
import math
xi = 4/30000; phi=(1+5**0.5)/2
print("="*66); print("A) TFLN-Auflösung 1/Q gegen FFGFT-Skalen"); print("="*66)
for Q in (1e4, 1e6, 1e7, 1e8):
    print(f"  Q={Q:.0e}: 1/Q={1/Q:.1e}   löst ξ={xi:.2e}: {1/Q<xi}   löst 100ξ: {1/Q<100*xi}   löst ξ²={xi*xi:.1e}: {1/Q<xi*xi}")
print(f"  Benötigt: Q > 1/ξ = {1/xi:.0f} für ξ;  Q > 1/ξ² = {1/xi**2:.1e} für ξ².  TFLN (Q>10⁶) löst ξ, nicht ξ² [B].")
f_opt = 3e8/1550e-9
print(f"  Bei 1550 nm (f={f_opt:.2e} Hz): Linienbreite Δf = f/Q = {f_opt/1e6:.0f} MHz bei Q=10⁶.")

print("\n"+"="*66); print("B) 'Einrasten' auf φ^-k gegen Arnold-Zungen (Dok. 328, K_eff=2πξ)"); print("="*66)
K=2*math.pi*xi
fib=[1,1,2,3,5,8,13,21,34,55]
print(f"  K_eff = {K:.3e}.  Zungenbreite ΔΩ(p/q) ≈ 2(K/2)^q/(qπ^(q-1)); Fibonacci-Näherungen von 1/φ:")
for i in range(1,8):
    p,q=fib[i],fib[i+1]
    w=2*(K/2)**q/(q*math.pi**(q-1)); dist=abs(1/phi-p/q)
    print(f"    p/q={p}/{q}: Abstand zu 1/φ={dist:.2e}, Zungenhalbbreite={w/2:.1e} → {'IN Zunge' if dist<w/2 else 'außerhalb'}")
print("  [B] 1/φ liegt außerhalb jeder Zunge — φ^-k-Verhältnisse sind stabil, WEIL sie nicht einrasten (KAM),")
print("      nicht weil sie einrasten. Dok. 186 nennt das 'Einrasten'; Dok. 328 [K] zeigt das Gegenteil.")
print("      Die Diskretheit N∈ℤ aus ∮∇φ = 2πN ist topologisch; 'Phase-Locking' ist die falsche Vokabel.")

print("\n"+"="*66); print("C) 50 GHz als Harmonische von f0 = 1/t0"); print("="*66)
tP=5.391e-44; t0=tP/7500; f0=1/t0
for f in (50e9, 6.24e9, 2.38e9):
    k_phi = math.log(f0/f)/math.log(phi); n_int=f0/f
    print(f"  f={f:.2e} Hz: f0/f = {n_int:.2e};  als φ^-k·f0: k = {k_phi:.1f};  als φ^-2n·f0: n = {k_phi/2:.1f}")
print(f"  [B] 50 GHz ist die ~{math.log(f0/50e9)/math.log(phi):.0f}. Goldene Subharmonische von f0 = {f0:.2e} Hz — keine ausgezeichnete Stufe.")

print("\n"+"="*66); print("D) Sweet-Spot-Leiter f_n = (E0/h)·ξ²·φ^-2n (Dok. 034/162)"); print("="*66)
r=6.24/2.38
print(f"  6,24/2,38 = {r:.3f};  φ² = {phi**2:.3f}  → Leiter intern konsistent: {abs(r-phi**2)/phi**2*100:.1f} % Abweichung [B]")
A = 6.24e9*phi**(2*14)
print(f"  Vorfaktor (E0/h)·ξ² = 6,24 GHz·φ^28 = {A:.3e} Hz  →  E0/h = {A/xi**2:.3e} Hz  →  E0 = {A/xi**2*6.626e-34/1.602e-19:.3e} eV")
print("  Leiter um 50 GHz:")
for n in (10,11,12,13,14,15):
    print(f"    n={n}: {A*phi**(-2*n)/1e9:8.2f} GHz")
print(f"  [B] 50 GHz liegt NICHT auf der Leiter (nächste Sprosse n=12: {A*phi**-24/1e9:.1f} GHz, {abs(50-A*phi**-24/1e9)/50*100:.0f} % daneben).")
print("      Die 50-GHz-Bandbreite aus Dok.186 und die Sweet-Spots aus Dok.162 sind nicht dieselbe Struktur.")

print("\n"+"="*66); print("E) B-Meson: α = ξ als Ursache einer 4σ-Abweichung?"); print("="*66)
delta = xi
for N in (1e4, 1e5, 1e6, 1e8, 1e9):
    sig = delta*math.sqrt(N)
    print(f"  N={N:.0e} Ereignisse: Signifikanz einer relativen Ratenänderung δ=ξ ≈ δ√N = {sig:.2f} σ")
Nreq=(4/delta)**2
print(f"  Für 4σ nötig: N ≈ (4/ξ)² = {Nreq:.1e} Ereignisse.  LHCb B→K*μμ: O(10³–10⁴) Ereignisse.")
print("  [B] Eine Ratenmodifikation der Größe α=ξ (0,013 %) kann bei realistischer Statistik KEINE 4σ-")
print("      Abweichung erzeugen; die beobachteten Anomalien liegen bei Prozenten, nicht bei 10⁻⁴.")
print("      Dok.186 setzt eine PHASE Δφ=ξ mit einer RATE gleich — das ist ein Kategorienfehler [S→X].")

print("\n"+"="*66); print("F) Wicklungszahlen gegen Fibonacci-Bedingung (Dok.186: N ∈ {F_k})"); print("="*66)
from fractions import Fraction
for name,r in (("r_e",Fraction(4,3)),("r_μ",Fraction(16,5))):
    num,den=r.numerator,r.denominator
    print(f"  {name} = {r}: Zähler {num} {'∈' if num in fib else '∉'} Fibonacci, Nenner {den} {'∈' if den in fib else '∉'} Fibonacci")
print("  Nach Dok. 342: die Nenner 3 und 5 sind Primzahlen der GF(3^k)-Hierarchie (k=1 Charakteristik, k=4),")
print("  die Zähler 4 = 2², 16 = 2⁴ Potenzen der Oktave. Das ist die Galois-Struktur, nicht Fibonacci.")
print("  [B] Die Fibonacci-Bedingung aus Dok.186 wird von den Wicklungszahlen aus Dok.338 nicht erfüllt (16 ∉ F).")
print("\nAlle Rechnungen ausgeführt.")
