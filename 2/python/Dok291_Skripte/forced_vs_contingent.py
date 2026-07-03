#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Erzwungen wie c, oder kontingent? -- Zahlen zum Photon/2/9-Kontrast.

Testet Johanns Intuition direkt: ist 2/9 ein RAND/Saettigungs-Wert (parameterfrei
erzwungen, wie v=c) oder ein INNERES Extremum, das an einem freien Parameter delta
haengt (kontingent)?

Funktional wie in symmetriebrechung_2_9.py:
  a_k = 1 + sqrt2 cos(phi_k) + delta cos(2 phi_k + chi),  phi_k = theta + 2pi k/3
  e3(theta) = prod_k a_k   (der einzige theta-Traeger)

numpy-only, seed 20780458.
"""
import numpy as np
np.random.seed(20780458)
r = np.sqrt(2.0); TWO_PI = 2*np.pi; TH29 = 2/9
TH = np.linspace(1e-4, TWO_PI/3 - 1e-4, 200001)

def e3(theta, delta, chi):
    k = np.arange(3)[:,None]; phi = theta[None,:] + TWO_PI*k/3
    return np.prod(1 + r*np.cos(phi) + delta*np.cos(2*phi+chi), axis=0)

def theta_star(delta, chi):
    y = e3(TH, delta, chi); dy = np.diff(y)
    sc = np.where(np.diff(np.sign(dy))!=0)[0]+1
    inner = [TH[i] for i in sc if 2e-3 < TH[i] < TWO_PI/3-2e-3]
    if not inner: return None
    return min(inner, key=lambda t: abs(t-TH29))

print("="*70)
print("(1) Q(theta): der symmetrische Koide-Invariant ist theta-BLIND")
print("="*70)
for th in [0.0, TH29, 0.3, 0.5, 0.9]:
    a = 1 + r*np.cos(th + TWO_PI*np.arange(3)/3)   # signierte Wurzeln sqrt(m_k)=a_k
    Q = (a**2).sum() / (a.sum()**2)                # Koide-Q, vorzeichenrichtig
    print(f"   theta={th:.4f}:  Q = sum(a^2)/(sum a)^2 = {Q:.6f}   (sum a = {a.sum():.4f})")
print("   -> Q = 2/3 EXAKT fuer ALLE theta (Phasenzweig, r=sqrt2). Q-Grenzen sind 1/3, 1;")
print("      2/9 liegt an keiner Q-Grenze. Im symmetrischen Betrags-Invariant ist 2/9 unsichtbar.")

print()
print("="*70)
print("(2) theta*(delta): das Extremum WANDERT stetig mit dem freien delta")
print("="*70)
for chi,lab in [(0.0,'chi=0'), (np.pi/2,'chi=pi/2')]:
    print(f"\n   {lab}:")
    print(f"     {'delta':>7} | {'theta*':>9} | {'theta*-2/9':>11}")
    hit=None
    for delta in [0.10,0.20,0.24,0.30,0.40,0.52,0.60,0.80,1.00]:
        ts = theta_star(delta,chi)
        if ts is None:
            print(f"     {delta:7.2f} | {'--':>9} |"); continue
        print(f"     {delta:7.2f} | {ts:9.5f} | {ts-TH29:+11.5f}")
    # feine Suche: bei welchem delta genau 2/9?
    ds = np.linspace(0.05,1.2,400)
    tss = np.array([theta_star(d,chi) or np.nan for d in ds])
    good = ~np.isnan(tss)
    k = np.nanargmin(np.abs(tss-TH29))
    # Sensitivitaet dtheta*/ddelta um 2/9
    sl = np.gradient(tss[good], ds[good])
    print(f"     -> theta*=2/9 bei delta={ds[good][np.nanargmin(np.abs(tss[good]-TH29))]:.3f};"
          f"  Steigung dtheta*/ddelta ~ {np.nanmedian(sl):+.3f} (Median ueber Gitter; nicht 0 -> 2/9 wird gezogen)")
    # lokale Steigung bei delta* und delta-Fenster im theta-Raum (Basin = naechstes Orbit-Glied)
    dstar = ds[good][np.nanargmin(np.abs(tss[good]-TH29))]
    i0 = np.argmin(np.abs(ds-dstar))
    sl_loc = np.gradient(tss, ds)[i0]
    basin_lo, basin_hi = 1/6, 1/3   # Mittelpunkte zu 1/9 und 4/9 im theta-Raum
    print(f"     -> lokale Steigung bei delta*~{dstar:.2f}: {sl_loc:+.3f};"
          f"  theta-Basin [1/6,1/3] Breite {basin_hi-basin_lo:.4f}"
          f"  -> delta-Fenster ~ {(basin_hi-basin_lo)/sl_loc:.3f} (weich, nicht feinabgestimmt)")
    print(f"     -> erreichter theta*-Bereich: [{np.nanmin(tss[good]):.4f}, {np.nanmax(tss[good]):.4f}]"
          f" rad -- 2/9={TH29:.4f} liegt INNEN, unausgezeichnet.")

# Spiegel-Zweig chi=3pi/2 (=-i, ebenfalls schief-adjungiert): erreicht 2/9 NICHT
TH_f = np.linspace(1e-4, TWO_PI/3 - 1e-4, 200001)
ph = TH_f[None,:] + TWO_PI*np.arange(3)[:,None]/3
y = np.prod(1 + r*np.cos(ph) + 0.24*np.cos(2*ph+1.5*np.pi), axis=0)
dy = np.diff(y); sc = np.where(np.diff(np.sign(dy))!=0)[0]+1
inner = [t for t in TH_f[sc] if 2e-3 < t < TWO_PI/3-2e-3]
print(f"\n   Spiegel-Zweig chi=3pi/2 (e^(-i pi/2)=-i), delta=0.24: innere Extrema = "
      f"{np.round(inner,3)} -- kein Extremum nahe 2/9={TH29:.4f}."
      f" Die +i/-i-Zweigwahl ist eine Orientierungswahl; nur +i erreicht den Orbit-Bereich.")

print()
print("="*70)
print("(3) Kontrast c: parameterfreier RAND, keine Kurve, kein Modul")
print("="*70)
print("   Kausalgrenze v<=c; masselos m=0 SAETTIGT die Grenze -> v=c exakt.")
print("   Es gibt kein 'c*(parameter)': c ist ein Punkt, festgelegt durch die")
print("   Lorentz-Signatur (Kegelrand), nicht Extremum eines Funktionals.")
print("   dc/d(irgendwas) existiert nicht -- im Gegensatz zu dtheta*/ddelta != 0.")
print()
print("FAZIT (Zahlen): 2/9 ist ein INNERES Extremum, das ein freier Parameter delta")
print("herbeizieht (dtheta*/ddelta != 0), unsichtbar im symmetrischen Q. c ist ein")
print("parameterfreier RAND. Verschiedener Typ -- 2/9 statisch NICHT erzwungen wie c.")
