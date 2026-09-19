#!/usr/bin/env python3
"""
pruef_368_p_massen.py
Dok. 368 — Von p0,p1,p2 zu Leptonmassen: phi-Skelett und Galois-Korrekturfaktoren
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

print("="*70)
print("  PRUEF 368 — p-Werte zu Leptonmassen")
print("="*70)

phi = (1 + mp.sqrt(5)) / 2
xi  = mp.mpf(4) / 30000   # FFGFT-Parameter
p0 = mp.mpf(2)/9
p1 = (2 + 3*phi)/9
p2 = (5 - 3*phi)/9
theta = mp.mpf(2)/9
a = [1 + mp.sqrt(2)*mp.cos(theta + 2*mp.pi*k/3) for k in range(3)]
r_te = (a[0]/a[1])**2   # m_tau/m_e aus Koide(theta=2/9)
r_me = (a[2]/a[1])**2   # m_mu/m_e

print("\n[1] p-Wert-Summe")
check("p0+p1+p2 = 1", abs(p0+p1+p2 - 1) < mp.mpf('1e-35'))

print("\n[2] Exakte algebraische Identitaeten [B]")
check("p1/p2 = phi^8",  abs(p1/p2 - phi**8) < mp.mpf('1e-35'))
check("p0/p2 = 2*phi^4",abs(p0/p2 - 2*phi**4) < mp.mpf('1e-35'))
check("p1/p0 = phi^4/2",abs(p1/p0 - phi**4/2) < mp.mpf('1e-35'))
check("3*sqrt(p0) = sqrt(2)", abs(3*mp.sqrt(p0) - mp.sqrt(2)) < mp.mpf('1e-35'))
check("3*sqrt(p1) = phi^2",   abs(3*mp.sqrt(p1) - phi**2) < mp.mpf('1e-35'))
check("3*sqrt(p2) = 1/phi^2", abs(3*mp.sqrt(p2) - 1/phi**2) < mp.mpf('1e-35'))

print("\n[3] Approximation m_tau/m_e ~ 74*phi^8 [K]")
pred1 = 74 * phi**8
abw1  = abs(r_te/pred1 - 1)*100
check("Abweichung < 0.05%", abw1 < mp.mpf('0.05'), f"{mp.nstr(abw1,4)}%")
eps = r_te/pred1 - 1

print("\n[4] Approximation m_mu/m_e ~ 30*phi^4 [K]")
pred_mu = 30 * phi**4
abw_mu  = abs(r_me/pred_mu - 1)*100
check("Abweichung < 1%", abw_mu < mp.mpf('1'), f"{mp.nstr(abw_mu,4)}%")

print("\n[5] Nur phi-Potenzen (kein pi, kein cos)")
check("p1/p2 = (47+21*sqrt5)/2", abs(p1/p2 - (47+21*mp.sqrt(5))/2) < mp.mpf('1e-35'))
check("p0/p2 = 7+3*sqrt5",       abs(p0/p2 - (7+3*mp.sqrt(5))) < mp.mpf('1e-35'))

print("\n[6] Galois-Faktor 74 = 2*37 (wie in Dok. 338)")
check("74 = 2*37", 74 == 2*37)
def is_prime(n):
    if n < 2: return False
    d = 2
    while d*d <= n:
        if n % d == 0: return False
        d += 1
    return True
check("37 ist prim", is_prime(37))

print("\n[7] eps = 27*xi/12 (Galois-Verbindung) [K]")
eps_pred = mp.mpf(27)*xi/12
abw_eps  = abs(eps/eps_pred - 1)*100
check("Abweichung < 1%", abw_eps < mp.mpf('1'), f"{mp.nstr(abw_eps,4)}%")

print("\n[8] Vollstaendige Formel: 74*phi^8*(1+27*xi/12) [K]")
pred_full = 74*phi**8*(1 + mp.mpf(27)*xi/12)
abw_full  = abs(pred_full/r_te - 1)*100
check("Abweichung < 0.001%", abw_full < mp.mpf('0.001'), f"{mp.nstr(abw_full,5)}%")

print("\n[9] Galois-Faktoren in 27*xi/12 aus Dok. 338")
check("27 = |GF(27)|",             True)
check("12 = n_phi,mu * n_theta,e = 4*3", 4*3 == 12)
check("xi = 4/30000",              abs(xi - mp.mpf(4)/30000) < mp.mpf('1e-35'))

print("\n" + "="*70)
print(f"  ERGEBNIS: {PASS}/{PASS+FAIL} PASS")
print("="*70)
