import numpy as np
# ---------------------------------------------------------------------------
# Warum omega = xi^1 * E0 (eine fraktale Potenz) und nicht xi^2 ?
# Mechanismus: der Nullmode der Connection-Laplace wird durch die fraktale
# Korrektur g = eta(1 + xi*f) angehoben. Stoerungstheorie 1. Ordnung:
#     delta-lambda_0 = xi * <0|f|0> = xi * Mittelwert(f).
# -> Mittelwert(f) != 0  (Dimensions-DEFIZIT D_f=3-xi)  => xi^1
# -> Mittelwert(f) == 0  (volumen-erhaltende Welligkeit) => xi^2 (2. Ordnung)
# ---------------------------------------------------------------------------
N = 64
# Ring-Laplace L0 (T^1-Proxy fuer T^4): exakter Nullmode v0 = const, lambda=0
idx = np.arange(N)
L0 = 2*np.eye(N) - np.eye(N)[np.roll(idx,1)] - np.eye(N)[np.roll(idx,-1)]
w0 = np.linalg.eigvalsh(L0); 
print("L0 niedrigste Eigenwerte:", np.round(w0[:3],6), " (Nullmode vorhanden)")

def lift(f, xis):
    """niedrigster Eigenwert von L0 + xi*diag(f), als Funktion von xi"""
    V = np.diag(f - 0.0)          # fraktale Potential-Korrektur (diagonal)
    out=[]
    for xi in xis:
        lam = np.linalg.eigvalsh(L0 + xi*V).min()
        out.append(lam - 0.0)
    return np.array(out)

xis = np.array([4/30000 * t for t in (1,2,4,8,16,32)])   # um den FFGFT-Wert herum

# Fall A: Dimensions-DEFIZIT -> Mittelwert(f) != 0  (hier f ~ 1, leicht moduliert)
fA = 1.0 + 0.1*np.cos(2*np.pi*idx/N);  fA_mean = fA.mean()
# Fall B: volumen-erhaltende Welligkeit -> Mittelwert(f) = 0
fB = np.cos(2*np.pi*idx/N);            fB_mean = fB.mean()

for name, f in [("A  Dimensions-Defizit (mean!=0)", fA), ("B  Welligkeit (mean=0)", fB)]:
    lam = np.abs(lift(f, xis))
    # log-log-Steigung = effektive xi-Potenz
    p = np.polyfit(np.log(xis), np.log(lam), 1)[0]
    print("\nFall %s :  mean(f)=%.4f" % (name, f.mean()))
    print("   lambda0(xi) =", np.array2string(lam, formatter={'float_kind':lambda z:'%.3e'%z}))
    print("   -> effektive xi-Potenz p = %.3f" % p)

print("\n==> Ergebnis: die fraktale Korrektur hebt den Nullmode an;")
print("    die POTENZ ist 1, genau dann wenn die Korrektur nicht-verschwindenden")
print("    Torus-Mittelwert hat. D_f = 3 - xi ist ein Dimensions-DEFIZIT (nicht")
print("    volumen-erhaltend) -> Mittelwert != 0 -> xi^1. Also omega ~ xi * E0.")
print("    Offen bleibt nur der O(1)-Koeffizient (kinematisch 1/2, Dok 047) und")
print("    die Bestaetigung, dass der kinetische Zustand dieser gehobene Mode ist.")
