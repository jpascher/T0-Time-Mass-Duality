#!/usr/bin/env python3
# Rotverschiebungs-Drift (Sandage-Loeb): diskriminiert sie FFGFT von LCDM --
# oder verlaeuft auch das in Entartung? numpy-only, seed 20780458.
import numpy as np
np.random.seed(20780458)

c   = 2.998e8                     # m/s
H0  = 67.4*1000/3.0857e22         # 1/s (Planck 67.4 km/s/Mpc)
Om, OL = 0.315, 0.685
yr  = 3.156e7
def E(z): return np.sqrt(Om*(1+z)**3 + OL)

print("== 1) LCDM-Drift: zdot=(1+z)H0 - H(z);  Dv = c*zdot*Dt/(1+z) ==")
for T in (20, 25):
    Dt = T*yr
    print(f"  Beobachtungsdauer {T} Jahre  (c*H0*Dt = {100*c*H0*Dt:.1f} cm/s):")
    for z in (0.5, 1.0, 2.0, 3.0, 4.0, 5.0):
        red = 1 - E(z)/(1+z)              # zdot/((1+z)H0)
        dv  = c*H0*Dt*red
        print(f"    z={z:3.1f}:  zdot/(1+z) = {red:+.3f} H0   ->  Dv = {100*dv:+7.2f} cm/s")
# Nulldurchgang
zz = np.linspace(0.01, 5, 200001)
i0 = np.argmin(np.abs(1 - E(zz)/(1+zz)))
print(f"  Vorzeichenwechsel (LCDM-Signatur): z0 = {zz[i0]:.3f}")

print("\n== 2) FFGFT strikt statisch: 1+z=e^(xi*x), x fest -> zdot = 0, Dv = 0 exakt ==")

print("\n== 3) Messbarkeit (ELT/ANDES, Groessenordnung sigma ~ 2 cm/s Gesamtkampagne) ==")
sig = 0.02
for z in (2.0, 3.0, 4.0):
    dv = c*H0*25*yr*(1 - E(z)/(1+z))
    print(f"  z={z}: |LCDM - FFGFT(0)| = {100*abs(dv):.1f} cm/s  ->  {abs(dv)/sig:.1f} sigma")

print("\n== 4) ENTARTUNGSKANAL A: saekulare FFGFT-Evolution ==")
print("  Wenn die Phase xi*x (oder xi_eff) saekular driftet mit Rate s = d(xi x)/dt,")
print("  dann zdot/(1+z) = s. Erforderliche Rate, um LCDM zu imitieren:")
for z in (0.5, 2.0, 4.0):
    s = H0*(1 - E(z)/(1+z))
    print(f"    z={z}: s = {s/H0:+.3f} H0 = {s*yr:+.2e} /Jahr")
print(f"  Natuerliche FFGFT-Rate: c/R_H = H0 exakt (R_H = c/H0) = {H0*yr:.2e} /Jahr")
print("  -> Eine saekulare Evolution bei ~10-40% der EIGENEN Naturskala reicht.")
print("     Die Entartung ist nicht zufaellig: beide Modelle teilen die Skala R_H/H0.")

print("\n== 5) FORM-Test gegen Kanal A: konstante Rate vs. LCDM-Formkurve ==")
print("  Konstantes s: zdot/(1+z) z-UNABHAENGIG (kein Vorzeichenwechsel).")
print("  LCDM: Vorzeichenwechsel bei z0=1.92 (positiv darunter, negativ darueber).")
Dt = 25*yr
lo, hi = 0.5, 4.0
d_l = c*H0*Dt*(1-E(lo)/(1+lo)); d_h = c*H0*Dt*(1-E(hi)/(1+hi))
print(f"  Zwei-Band-Kontrast Dv(z={lo})-Dv(z={hi}):")
print(f"    LCDM:              {100*(d_l-d_h):+.1f} cm/s")
print(f"    FFGFT statisch:      +0.0 cm/s")
print(f"    FFGFT + konst. s:    +0.0 cm/s  (Kontrast eliminiert JEDEN konstanten Kanal)")
print(f"    Signifikanz Kontrast (sigma~{100*sig*np.sqrt(2):.1f} cm/s): {abs(d_l-d_h)/(sig*np.sqrt(2)):.1f} sigma")
print("  ABER: das Niedrig-z-Band (+5 cm/s bei z=0.5) braucht andere Traeger")
print("  (Ly-alpha erst ab z>1.7 vom Boden; darunter Masern/Uhren -> haerter).")

print("\n== 6) SYSTEMATIK gleicher Groessenordnung: galaktische Beschleunigung ==")
a_gal = (2.35e5)**2/2.5e20         # v_c^2/R0, m/s^2
for T in (20,25):
    print(f"  Sonnensystem-Beschleunigung -> saekulare Doppler-Drift ueber {T} J: "
          f"{100*a_gal*T*yr:.1f} cm/s (DIPOL am Himmel, korrigierbar via Richtungsmuster,")
print("  aber gleiche Groessenordnung wie das Signal -- kein 'sauberer' Test ohne diese Subtraktion.)")
print("  Pekuliare Beschleunigungen der Ly-alpha-Woelkchen: Literaturabschaetzung <~0.1 cm/s/Dekade,")
print("  subdominant, aber quellenabhaengig.")

print("\n== FAZIT ==")
print("  (a) Amplituden-Test allein: NICHT entartungsfest -- eine saekulare FFGFT-")
print("      Evolution an der eigenen R_H-Skala imitiert LCDM in der Groesse,")
print("      und die Dipol-Systematik liegt in derselben Ordnung.")
print("  (b) FORM-Test (Vorzeichenwechsel bei z=1.92 / Zwei-Band-Kontrast ~17 cm/s):")
print("      eliminiert jeden z-KONSTANTEN Entartungskanal; nur ein fein")
print("      z-abhaengig konstruierter Kanal koennte ihn imitieren (Occam, kein Beweis).")
print("  (c) Bedingung auf FFGFT-Seite: der Korpus muesste sich VORAB auf strikte")
print("      Statik (zdot=0) festlegen -- sonst ist der Test per Konstruktion entartet.")
print("  (d) Zeithorizont ~2 Jahrzehnte ELT; kein kurzfristiger Diskriminator.")
