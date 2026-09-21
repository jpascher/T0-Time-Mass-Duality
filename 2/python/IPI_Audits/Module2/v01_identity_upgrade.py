#!/usr/bin/env python3
"""
v01 — The commutator law is an EXACT IDENTITY, not an inequality.

NB01 §4 states:   S^2 <= 4 + ||[A0,A1]||*||[B0,B1]||
NB02 §5 / NB03 state:  S^2  = 4 + ||[A0,A1]||*||[B0,B1]||

The second is the correct one, it holds in EVERY dimension, and it has a
one-line proof. This script gives the proof and the numerical confirmation.

Self-contained: numpy only.
"""
import numpy as np

nrm  = lambda M: np.linalg.norm(M, 2)
comm = lambda a, b: a @ b - b @ a

def rand_pm1(rng, d):
    """Random Hermitian involution (+-1 observable) of dimension d."""
    M = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    M = M + M.conj().T
    w, V = np.linalg.eigh(M)
    s = np.sign(w); s[s == 0] = 1.0
    return (V * s) @ V.conj().T

def chsh_norm(a0, a1, b0, b1):
    d = a0.shape[0]; Id = np.eye(d, dtype=complex); K = np.kron
    A0, A1, B0, B1 = K(a0, Id), K(a1, Id), K(Id, b0), K(Id, b1)
    return nrm(A0 @ B0 - A0 @ B1 + A1 @ B0 + A1 @ B1)

print(__doc__)
print("=" * 72)
print("PROOF (three lines)")
print("=" * 72)
print("""
  1. A0 is Hermitian with A0^2 = I, hence A0 = A0^{-1}. Therefore

         A0 [A0,A1] A0 = A0(A0A1 - A1A0)A0 = A1A0 - A0A1 = -[A0,A1].

     So [A0,A1] is conjugate to its own negative => the spectrum of the
     Hermitian operator i[A0,A1] is symmetric about 0, with extremes +-c_A,
     c_A = ||[A0,A1]||.  Same for B.

  2. [A0,A1] and [B0,B1] act on different tensor factors, so they commute
     and are simultaneously diagonalisable. The spectrum of the product
     [A0,A1][B0,B1] = -(i[A0,A1])(i[B0,B1]) is therefore {+- c_A c_B},
     symmetric, and it ATTAINS +c_A c_B.

  3. B^2 = 4I + [A0,A1][B0,B1] (Landau).  B is Hermitian, so ||B||^2 = ||B^2||,
     and the largest eigenvalue of 4I + (something attaining +c_A c_B) is
     exactly 4 + c_A c_B.  Hence

         S^2 = 4 + ||[A0,A1]|| * ||[B0,B1]||       EXACTLY, in every dimension.

  The Tsirelson bound is then the single corollary c_A, c_B <= 2.
""")

print("=" * 72)
print("NUMERICAL CONFIRMATION — random +-1 observables, several dimensions")
print("=" * 72)
rng = np.random.default_rng(2718)
print(f"  {'dim':>4} | {'trials':>7} | {'max |S^2 - (4+cA*cB)|':>24}")
print("  " + "-" * 44)
for d in (2, 3, 4, 6, 8):
    worst = 0.0
    for _ in range(3000):
        a0, a1, b0, b1 = (rand_pm1(rng, d) for _ in range(4))
        S   = chsh_norm(a0, a1, b0, b1)
        rhs = 4 + nrm(comm(a0, a1)) * nrm(comm(b0, b1))
        worst = max(worst, abs(S**2 - rhs))
    print(f"  {d:>4} | {3000:>7} | {worst:>24.3e}")

print("""
  Equality, not inequality, and not only at optimal settings. The '<=' in
  NB01 section 4 should be '='; the identity is the stronger statement and
  it is yours.
""")
