#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dok 290 -- Hebel: die Masse-Information ist blind fuer den Misch-/Phasenkanal.

Ein Massenoperator M = U diag(m) U^dagger hat zwei unabhaengige Inhalte:
  - die Eigenwerte m (Massen)        -> Betragskanal, was Vopson/Landauer zaehlt
  - die Eigenvektoren U (Mischung)   -> Phasenkanal (PMNS-artig)
Jede Funktion der Eigenwerte allein (Summe = "Masse-Information", Koide Q) ist
gegenueber U INVARIANT. Zwei physikalisch verschiedene Operatoren (verschiedene
Mischung) haben damit identische Masse-Information.

numpy-only, seed 20780458.
"""
import numpy as np
np.random.seed(20780458)

def random_unitary(n):
    Z = (np.random.randn(n, n) + 1j*np.random.randn(n, n)) / np.sqrt(2)
    Q, R = np.linalg.qr(Z)
    return Q @ np.diag(np.exp(1j*np.angle(np.diag(R))))

def koide_Q(m):
    s = np.sqrt(m); return m.sum()/s.sum()**2

m = np.array([0.5, 1.5, 3.0])         # feste Massen (Eigenwerte)
print("feste Massen (Eigenwerte):", m)
print("Masse-Information-Proxy  Sum m =", f"{m.sum():.6f}")
print("Koide Q                       =", f"{koide_Q(m):.6f}")
print()
print("drei verschiedene Mischungen U bei IDENTISCHEN Massen:")
for k in range(3):
    U = random_unitary(3)
    M = U @ np.diag(m) @ U.conj().T
    ev = np.sort(np.linalg.eigvalsh(M))
    offdiag = np.sqrt(np.sum(np.abs(M - np.diag(np.diag(M)))**2))
    print(f"  U{k+1}: Eigenwerte={np.round(ev,6)}  Sum m={ev.sum():.6f}  Q={koide_Q(ev):.6f}"
          f"  ||M_offdiag||={offdiag:.3f}")
print()
print("-> Sum m und Q sind ueber alle Mischungen IDENTISCH (Betragskanal),")
print("   waehrend ||M_offdiag|| (die Mischung/Phase) stark variiert.")
print()

# entarteter Grenzfall: Massen gleich -> M = m*I fuer JEDES U
md = np.array([1.0, 1.0, 1.0])
U = random_unitary(3)
Md = U @ np.diag(md) @ U.conj().T
print("entartet (m gleich):  ||M - m*I|| =", f"{np.linalg.norm(Md - md[0]*np.eye(3)):.2e}")
print("-> bei Entartung verschwindet die Mischung AUS M; der Oszillations-/Phasen-")
print("   inhalt muss dann ausserhalb von M sitzen (Propagations-/Holonomie-Phase).")
print("   Das ist der Neutrino-Allpass-Fall: Betrag flach, Information in der Phase.")
