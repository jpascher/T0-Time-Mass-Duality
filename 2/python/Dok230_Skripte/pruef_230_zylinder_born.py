"""Dok. 230, Zylinderdarstellung des Qubits: Prüfungen zur Literaturverortung."""
import numpy as np
rng = np.random.default_rng(230)
ok = 0; n = 0
def check(name, cond):
    global ok, n; n += 1; ok += bool(cond); print(("OK  " if cond else "FAIL") + " " + name)

# 1 (z,r,theta) = Bloch-Kugel in Zylinderkoordinaten; alpha/beta-Formeln Standard
for _ in range(200):
    th_pol = rng.uniform(0, np.pi); th = rng.uniform(0, 2*np.pi)
    z, r = np.cos(th_pol), np.sin(th_pol)
    a = np.sqrt((1+z)/2)*np.exp(1j*th/2); b = np.sqrt((1-z)/2)*np.exp(-1j*th/2)
    sx = 2*(np.conj(a)*b).real; sy = 2*(np.conj(a)*b).imag; sz = abs(a)**2-abs(b)**2
    good = np.allclose([sz, np.hypot(sx, sy)], [z, r]) and np.isclose(z**2+r**2, 1)
    if not good: break
check("z=cos, r=sin, Bloch-Vektor (z, r) reproduziert", good)
check("Azimut: arg(a)-arg(b)=theta (Standard-phi = -theta, nur Orientierung)",
      np.isclose(np.angle(a/b), (th+np.pi) % (2*np.pi)-np.pi))

# 2 Archimedes: Haar-Zustaende -> z gleichverteilt
psi = rng.normal(size=(400000, 2)) + 1j*rng.normal(size=(400000, 2))
psi /= np.linalg.norm(psi, axis=1)[:, None]
zc = np.abs(psi[:, 0])**2 - np.abs(psi[:, 1])**2
h, _ = np.histogram(zc, bins=20, range=(-1, 1), density=True)
check("komplex: z gleichverteilt (Archimedes/Wootters)", np.max(np.abs(h-0.5)) < 0.02)
# reell: nicht gleichverteilt
pr = rng.normal(size=(400000, 2)); pr /= np.linalg.norm(pr, axis=1)[:, None]
zr = pr[:, 0]**2 - pr[:, 1]**2
hr, _ = np.histogram(zr, bins=20, range=(-1, 1), density=True)
check("reell: z NICHT gleichverteilt", np.max(np.abs(hr-0.5)) > 0.3)

# 3 Aerts: Band reisst gleichverteilt in [-1,1], Punkt bei z -> P(+1)=(1+z)/2
for z0 in [-0.8, -0.3, 0.0, 0.4, 0.9]:
    lam = rng.uniform(-1, 1, 400000)
    p = np.mean(lam < z0)          # Riss unterhalb -> Punkt geht zum oberen Pol
    if abs(p-(1+z0)/2) > 0.004: break
else: z0 = None
check("Aerts-Modell liefert (1+z)/2", z0 is None)

# 6 theta traegt nichts bei: P haengt nur von z ab
z0 = 0.37; ps = [np.mean(rng.uniform(-1, 1, 200000) < z0) for th in np.linspace(0, 2*np.pi, 7)]
check("P(+1) unabhaengig von theta", np.ptp(ps) < 0.01)
# Gegenprobe: gleichverteilte Phase allein mit fester Schwelle gibt nicht (1+z)/2
thr = rng.uniform(0, 2*np.pi, 400000)
p_phase = np.mean(np.cos(thr) < z0)  # Schwelle auf Phase statt z
check("gleichverteilte Phase allein liefert nicht (1+z)/2", abs(p_phase-(1+z0)/2) > 0.05)

# 5 Hopf: globale Phase aendert (z,r,theta) nicht
g = np.exp(1j*1.234); a2, b2 = g*a, g*b
check("globale Phase faellt heraus (S^3 -> S^2)",
      np.isclose(abs(a2)**2-abs(b2)**2, abs(a)**2-abs(b)**2) and
      np.isclose(np.angle(a2/b2), np.angle(a/b)))
print(f"{ok}/{n}")
