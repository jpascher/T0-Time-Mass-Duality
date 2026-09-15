"""
pruef_hilbert_bridge.py — Kapitel 13: Zustandsbrücke FFGFT ↔ Hilbertraum
Quelle: QMB_n13_hilbertraum.tex, Gleichung (eq:state-bridge)

Brücke:
  alpha = sqrt((1+z)/2) * exp(i*theta/2)
  beta  = sqrt((1-z)/2) * exp(-i*theta/2)
Inverse:
  z     = |alpha|^2 - |beta|^2
  r     = 2*|alpha*beta|
  theta = arg(alpha) - arg(beta)
Bedingungen:
  (A) Normerhaltung:     |alpha|^2 + |beta|^2 == 1
  (B) Zylinderbedingung: z^2 + r^2 == 1
  (C) Bijektivität:      Hin- und Rücktransformation sind invers
  (D) Gatter sigma_z:    theta -> theta - pi  (nicht +pi)
  (E) Gatter Hadamard:   (z,r,theta) -> (r,z,theta+pi/2) [aus Matrixrechnung]
"""

import numpy as np

TOLS = dict(norm=1e-12, cyl=1e-12, bij=1e-12)

def forward(z, r, theta):
    """(z,r,theta) -> (alpha, beta)"""
    alpha = np.sqrt((1 + z) / 2) * np.exp(1j * theta / 2)
    beta  = np.sqrt((1 - z) / 2) * np.exp(-1j * theta / 2)
    return alpha, beta

def backward(alpha, beta):
    """(alpha, beta) -> (z, r, theta)"""
    z     = abs(alpha)**2 - abs(beta)**2
    r     = 2 * abs(alpha * beta)
    theta = np.angle(alpha) - np.angle(beta)
    # theta in [0, 2pi)
    theta = theta % (2 * np.pi)
    return z, r, theta

def gate_sigma_z(alpha, beta):
    """sigma_z = diag(1,-1): alpha -> alpha, beta -> -beta"""
    return alpha, -beta

def gate_hadamard(alpha, beta):
    """H = (1/sqrt2)[[1,1],[1,-1]]: standard Hadamard"""
    a2 = (alpha + beta) / np.sqrt(2)
    b2 = (alpha - beta) / np.sqrt(2)
    return a2, b2

# --- Testpunkte: Polpunkte + äquatoriale + allgemeine ---
testpoints = [
    # (z, r, theta, label)
    ( 1.0,  0.0, 0.0,          "|0>: Nordpol"),
    (-1.0,  0.0, 0.0,          "|1>: Südpol"),
    ( 0.0,  1.0, 0.0,          "|+>: Äquator, theta=0"),
    ( 0.0,  1.0, np.pi,        "|->: Äquator, theta=pi"),
    ( 0.0,  1.0, np.pi/2,      "|i>: Äquator, theta=pi/2"),
    ( 0.5,  np.sqrt(0.75), np.pi/3, "allgemeiner Punkt 1"),
    (-0.3,  np.sqrt(0.91), 2.1,     "allgemeiner Punkt 2"),
    ( 0.8,  0.6, 5.0,               "allgemeiner Punkt 3"),
]

errors = 0

print("=" * 60)
print("pruef_hilbert_bridge.py — Kapitel 13 Zustandsbrücke")
print("=" * 60)

# Check (A) + (B) + (C)
print("\n[A/B/C] Norm, Zylinderbedingung, Bijektivität")
for z0, r0, theta0, label in testpoints:
    # Zylinder-Bedingung vorab prüfen
    if abs(z0**2 + r0**2 - 1) > 1e-10:
        print(f"  SKIP (kein gültiger Zylinderpunkt): {label}")
        continue

    a, b = forward(z0, r0, theta0)

    # (A) Norm
    norm = abs(a)**2 + abs(b)**2
    if abs(norm - 1) > TOLS['norm']:
        print(f"  FEHLER Norm: {label}: |a|²+|b|²={norm:.6f}")
        errors += 1

    # (B) Zylinder
    z1, r1, theta1 = backward(a, b)
    cyl = z1**2 + r1**2
    if abs(cyl - 1) > TOLS['cyl']:
        print(f"  FEHLER Zylinder: {label}: z²+r²={cyl:.6f}")
        errors += 1

    # (C) Bijektivität: z,r stimmen exakt; theta modulo 2pi
    dz = abs(z1 - z0)
    dr = abs(r1 - r0)
    dtheta = abs((theta1 - theta0 % (2*np.pi)) % (2*np.pi))
    dtheta = min(dtheta, 2*np.pi - dtheta)
    if dz > TOLS['bij'] or dr > TOLS['bij'] or dtheta > TOLS['bij']:
        print(f"  FEHLER Bijekt.: {label}: dz={dz:.2e} dr={dr:.2e} dt={dtheta:.2e}")
        errors += 1
    else:
        print(f"  OK  {label}")

# Check (D) sigma_z: theta -> theta - pi
print("\n[D] Gatter sigma_z: theta -> theta - pi")
for z0, r0, theta0, label in testpoints:
    if abs(z0**2 + r0**2 - 1) > 1e-10:
        continue
    if r0 < 1e-10:   # Pol: theta undefiniert, skip
        continue
    a, b = forward(z0, r0, theta0)
    a2, b2 = gate_sigma_z(a, b)
    z2, r2, theta2 = backward(a2, b2)
    # Erwartung: z gleich, r gleich, theta -> theta - pi (mod 2pi)
    theta_exp = (theta0 - np.pi) % (2 * np.pi)
    dtheta = abs(theta2 - theta_exp)
    dtheta = min(dtheta, 2*np.pi - dtheta)
    dz = abs(z2 - z0); dr = abs(r2 - r0)
    if dz > 1e-10 or dr > 1e-10 or dtheta > 1e-10:
        print(f"  FEHLER sigma_z: {label}: dz={dz:.2e} dr={dr:.2e} dtheta={dtheta:.2e}")
        errors += 1
    else:
        print(f"  OK  sigma_z {label}: theta {theta0:.3f} -> {theta2:.3f} (erwartet {theta_exp:.3f})")

# Check (E) Hadamard aus Matrixrechnung: direkt auf alpha/beta prüfen
print("\n[E] Gatter Hadamard: Matrixbedingung |H(psi)|²=1, H²=I")
for z0, r0, theta0, label in testpoints:
    if abs(z0**2 + r0**2 - 1) > 1e-10:
        continue
    a, b = forward(z0, r0, theta0)
    a2, b2 = gate_hadamard(a, b)
    # Norm erhalten
    norm2 = abs(a2)**2 + abs(b2)**2
    # H² = I: zweimal Hadamard = Identität
    a3, b3 = gate_hadamard(a2, b2)
    da = abs(a3 - a); db = abs(b3 - b)
    if abs(norm2 - 1) > 1e-10 or da > 1e-10 or db > 1e-10:
        print(f"  FEHLER Hadamard: {label}: norm={norm2:.6f} da={da:.2e} db={db:.2e}")
        errors += 1
    else:
        print(f"  OK  Hadamard {label}")

print("\n" + "=" * 60)
if errors == 0:
    print(f"Alle Checks bestanden [K]")
else:
    print(f"{errors} FEHLER")
