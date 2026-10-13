#!/usr/bin/env python3
"""
pruef_393a_nulltest_grammatik.py — Dok. 393, Abschnitt Nulltest.
Wie viel harmonische Struktur tragen die Messwerte selbst,
und wie viel bringt die FFGFT-Vorgabe?

Exakte symbolische Suche (die vollständige Form der symbolischen Regression)
über eine Ausdrucks-Grammatik, jeweils mit Monte-Carlo-Nulltest.

Grammatik:  x = c · d^(1/k) · ξ^(m/n) · π^s
  c = p/q   teilerfremd, p,q ≤ 200, Primfaktoren aus P
  d^(1/k)   d ≤ 30 aus P, k ∈ {2,3}, keine vollständige k-te Potenz (oder fehlt)
  ξ^(m/n)   ξ = 1/7500, n ∈ {1,2,3,6}, |m/n| ≤ 4.5
  π^s       s ∈ {-1,0,1}
Komplexität (Bit) = log2 p + log2 q + [log2 d + log2 k] + [1 + log2|m| + log2 n] + [1 falls s≠0]

Test A (mit Vorgabe): FFGFT-Formel aus Dok. 387 fest. p = Anteil zufälliger
  Zielwerte (log-gleichverteilt, ±1 Dekade um den Messwert), die ein Ausdruck
  derselben oder geringerer Komplexität mindestens so genau trifft.
Test B (ohne Vorgabe): blinde Suche nach dem besten Ausdruck je Komplexitätsstufe,
  p über dieselbe Suche an Zufallszielen, Bonferroni über die Stufen.
Kontrollen: andere Primzahlmengen; Positivkontrolle Balmer-Linien (Wasserstoff,
  Luftwellenlängen NIST), Negativkontrolle reine Zufallsziele.
"""
import numpy as np
from math import gcd, log2, log
from itertools import product

XI = 1 / 7500
RNG = np.random.default_rng(20261012)
NMC = 20000

def pf(n):
    s, d = set(), 2
    while d * d <= n:
        while n % d == 0:
            s.add(d); n //= d
        d += 1
    if n > 1: s.add(n)
    return s

def is_kth_power(d, k):
    r = round(d ** (1 / k))
    return any((r + e) ** k == d for e in (-1, 0, 1))

def build_grammar(P, maxpq=200, maxd=30, rational_only=False):
    sm = [n for n in range(1, maxpq + 1) if pf(n) <= P]
    cs = [(p, q) for p in sm for q in sm if gcd(p, q) == 1]
    c_log = np.array([log(p / q) for p, q in cs])
    c_bit = np.array([log2(p) + log2(q) for p, q in cs])
    if rational_only:
        return c_log, c_bit.astype(np.float32)
    ds = [(1, 1)] + [(d, k) for d in range(2, maxd + 1) if pf(d) <= P for k in (2, 3)
                     if not is_kth_power(d, k)]
    d_log = np.array([log(d) / k for d, k in ds])
    d_bit = np.array([0.0 if d == 1 else log2(d) + log2(k) for d, k in ds])
    xs = {}
    for n in (1, 2, 3, 6):
        for m in range(-27, 28):
            if abs(m / n) <= 4.5 and gcd(abs(m), n) == 1 or m == 0:
                fr = m / n
                b = 0.0 if m == 0 else 1 + log2(abs(m)) + log2(n)
                if fr not in xs or b < xs[fr]: xs[fr] = b
    x_log = np.array([fr * log(XI) for fr in xs]); x_bit = np.array(list(xs.values()))
    s_log = np.array([-log(np.pi), 0.0, log(np.pi)]); s_bit = np.array([1.0, 0.0, 1.0])
    # Kombinieren (äußeres Produkt) – getrennt nach ξ/π, um Speicher zu sparen
    cd_log = (c_log[:, None] + d_log[None, :]).ravel()
    cd_bit = (c_bit[:, None] + d_bit[None, :]).ravel()
    xs_log = (x_log[:, None] + s_log[None, :]).ravel()
    xs_bit = (x_bit[:, None] + s_bit[None, :]).ravel()
    L = (cd_log[:, None] + xs_log[None, :]).ravel()
    B = (cd_bit[:, None] + xs_bit[None, :]).ravel().astype(np.float32)
    return L, B

class Grammar:
    def __init__(self, P, rational_only=False):
        self.P = P
        L, B = build_grammar(P, rational_only=rational_only)
        o = np.argsort(B, kind='stable')
        self.L, self.B = L[o], B[o]
        self.cache = {}
    def sub(self, cmax):
        key = round(float(cmax), 3)
        if key not in self.cache:
            n = np.searchsorted(self.B, cmax + 1e-6, side='right')
            self.cache[key] = np.sort(self.L[:n])
        return self.cache[key]
    @staticmethod
    def nearest(sorted_logs, t):
        i = np.searchsorted(sorted_logs, t)
        i0 = np.clip(i - 1, 0, len(sorted_logs) - 1); i1 = np.clip(i, 0, len(sorted_logs) - 1)
        return np.minimum(np.abs(sorted_logs[i0] - t), np.abs(sorted_logs[i1] - t))
    def p_fixed(self, x, dev, cmax):
        """Anteil Zufallsziele (±1 Dekade), die ein Ausdruck mit Komplexität ≤ cmax
        mindestens so genau trifft wie |dev|."""
        S = self.sub(cmax)
        t = log(x) + RNG.uniform(-log(10), log(10), NMC)
        return float(np.mean(self.nearest(S, t) <= log(1 + abs(dev))))
    def blind(self, x, levels, sigma=0.0):
        """Beste Treffergenauigkeit je Komplexitätsstufe und p-Wert (Bonferroni).
        Treffer unterhalb der Messunsicherheit sigma zählen nur als sigma."""
        best = []
        for c in levels:
            S = self.sub(c)
            d = max(float(np.expm1(self.nearest(S, np.array([log(x)]))[0])), sigma)
            p = self.p_fixed(x, d, c)
            best.append((c, d, p))
        cmin, dmin, pmin = min(best, key=lambda r: r[2])
        return cmin, dmin, min(1.0, pmin * len(levels)), best

# ----------------------------------------------------------------- Daten
# FFGFT-Grundform nach Dok. 387 (Formel, Komplexität), Messwerte CODATA 2022 / PDG 2024
def bits(p=1, q=1, d=1, k=1, m=0, n=1, s=0):
    b = log2(p) + log2(q)
    if d > 1: b += log2(d) + log2(k)
    if m: b += 1 + log2(abs(m)) + log2(n)
    if s: b += 1
    return b

ITEMS = [
 # Name, Messwert, FFGFT-Wert, Komplexität der FFGFT-Formel, rel. Messunsicherheit (Dok. 387)
 ("m_mu/m_e",        206.7682830,          120 * 3 ** 0.5,                  bits(p=120, d=3, k=2), 2e-8),
 ("m_tau/m_mu",      1776.86 / 105.6583755, 125 / 144 * XI ** (-1 / 3),     bits(p=125, q=144, m=-1, n=3), 7e-5),
 ("dm2_atm/dm2_sol", 2.501e-3 / 7.53e-5,   120 / (11 / 3),                  bits(p=360, q=11), 2.6e-2),
 ("sin2_theta13",    0.0220,               (25 * XI) ** (2 / 3),            bits(p=5, d=5, k=3, m=2, n=3), 3e-2),
 ("M_W/M_Z",         80.3692 / 91.1876,    (7 / 9) ** 0.5,                  bits(q=3, d=7, k=2), 1.7e-4),
 ("m_h/M_Z",         125.20 / 91.1876,     11 / 8,                          bits(p=11, q=8), 9e-4),
 ("m_t/M_Z",         172.57 / 91.1876,     (11 / 8) ** 2,                   bits(p=121, q=64), 1.7e-3),
 ("lambda_CKM",      0.22501,              XI ** (1 / 6),                   bits(m=1, n=6), 3e-3),
 ("v/E_P",           246.21965 / 1.220890e19, XI ** 4 / (5 * np.pi),        bits(q=5, m=4, s=1), 1e-5),
]
# Positivkontrolle: Balmer-Linien, Luftwellenlängen in nm (NIST); exakt 27/20, 28/25, 200/189
BALMER = [("H_alpha/H_beta", 656.279 / 486.135), ("H_beta/H_gamma", 486.135 / 434.047),
          ("H_gamma/H_delta", 434.047 / 410.174)]
LEVELS = [4, 6, 8, 10, 12, 14, 16, 18]

PSETS = {
 "FFGFT {2,3,5,7,11,13}":   {2, 3, 5, 7, 11, 13},
 "Kontrolle {2,3,5,7,17,19}": {2, 3, 5, 7, 17, 19},
 "Kontrolle {2,3,5,13,17,23}": {2, 3, 5, 13, 17, 23},
 "nur {2,3,5,7}":            {2, 3, 5, 7},
}

def fisher(ps):
    from math import exp, factorial
    ps = [max(p, 1 / NMC) for p in ps]
    X = -2 * sum(log(p) for p in ps); k = len(ps)
    # Chi²-Verteilung mit 2k Freiheitsgraden, geschlossene Form
    s = sum((X / 2) ** i / factorial(i) for i in range(k))
    return exp(-X / 2) * s

if __name__ == "__main__":
    G = {name: Grammar(P) for name, P in PSETS.items()}
    R = {name: Grammar(P, rational_only=True) for name, P in PSETS.items()}
    g0 = G["FFGFT {2,3,5,7,11,13}"]; r0 = R["FFGFT {2,3,5,7,11,13}"]
    print(f"Grammatikgröße voll: {len(g0.L):,} Ausdrücke, nur Brüche: {len(r0.L):,}\n")

    print("TEST A — FFGFT-Formel als feste Vorgabe (Dok. 387), volle Grammatik bis zur Formel-Komplexität")
    print(f"{'Größe':18s}{'Abw.':>9s}{'Mess.':>9s}{'Bit':>6s}{'p':>8s}")
    pA = []
    for name, x, f, c, sg in ITEMS:
        dev = f / x - 1
        p = g0.p_fixed(x, max(abs(dev), sg), c)
        pA.append(p)
        print(f"{name:18s}{dev*100:+8.3f}%{sg*100:8.4f}%{c:6.1f}{p:8.3f}")
    print(f"Fisher kombiniert: p = {fisher(pA):.3g}\n")
    RES = {"pA": pA, "fisherA": fisher(pA)}

    for label, GG in (("volle Grammatik", G), ("nur Brüche p/q (harmonisches Raster)", R)):
        print(f"TEST B — blinde Suche ohne Vorgabe, {label}")
        for gname, g in GG.items():
            pB = [g.blind(x, LEVELS, sg)[2] for name, x, f, c, sg in ITEMS]
            RES[(label, gname)] = min(pB)
            print(f"  {gname:30s} kleinster p = {min(pB):.3f}   Fisher = {fisher(pB):.3g}")
        print()

    print("Detail TEST B, FFGFT-Primzahlen, volle Grammatik:")
    for name, x, f, c, sg in ITEMS:
        cb, db, pb, _ = g0.blind(x, LEVELS, sg)
        print(f"  {name:18s} bester Treffer {db*100:.4f}% bei ≤{cb} Bit, p = {pb:.3f}")
    print()

    print("POSITIVKONTROLLE — Balmer-Linien, Messunsicherheit 1e-5")
    for label, g in (("volle Grammatik", g0), ("nur Brüche", r0)):
        pP = []
        for name, x in BALMER:
            cb, db, pb, _ = g.blind(x, LEVELS, 1e-5)
            pP.append(pb)
            print(f"  [{label}] {name:16s} Treffer {db*100:.5f}% bei ≤{cb} Bit, p = {pb:.4f}")
        print(f"  [{label}] Fisher kombiniert: p = {fisher(pP):.3g}")
        RES[("balmer", label)] = fisher(pP)
    print()

    print("NEGATIVKONTROLLE — 9 reine Zufallsziele, blind gesucht (Unsicherheit 1e-3)")
    for label, g in (("volle Grammatik", g0), ("nur Brüche", r0)):
        pN = []
        for i in range(9):
            x = float(np.exp(RNG.uniform(log(0.01), log(300))))
            pN.append(g.blind(x, LEVELS, 1e-3)[2])
        print(f"  [{label}] p-Werte: {', '.join(f'{p:.2f}' for p in pN)}   Fisher = {fisher(pN):.3g}")
    print()

    print("1/alpha = 3700/27 (Dok. 338)")
    a = 137.035999177; d = 3700 / 27 / a - 1
    t = log(a) + RNG.uniform(-log(1.01), log(1.01), NMC)
    fr = np.array(sorted({log(p / q) for q in range(1, 28) for p in range(int(130 * q), int(145 * q) + 1)}))
    pa = float(np.mean(Grammar.nearest(fr, t) <= abs(d)))
    print(f"  Abweichung {d*1e6:+.2f} ppm; Anteil Zufallszahlen, die ein Bruch p/q mit q ≤ 27 "
          f"ebenso genau trifft: p = {pa:.3f}")
    RES["alpha"] = pa

    # ---------------- Prüfungen der im Dok. 393 genannten Aussagen
    ok = tot = 0
    def check(name, cond):
        return name, bool(cond)
    checks = [
     check("A1 Test A kombiniert nicht signifikant (Fisher > 0,2)", RES["fisherA"] > 0.2),
     check("A2 v/E_P kleinster Einzelwert in Test A (p < 0,05)", RES["pA"][8] < 0.05 and min(RES["pA"]) == RES["pA"][8]),
     check("A3 Leptonverhältnisse in Test A p = 1", RES["pA"][0] > 0.99 and RES["pA"][1] > 0.99),
     check("B1 blinde Suche, volle Grammatik: keine Primzahlmenge unter p = 0,3",
           all(v > 0.3 for k, v in RES.items() if isinstance(k, tuple) and k[0] == "volle Grammatik")),
     check("B2 blinde Suche, nur Brüche: keine Primzahlmenge unter p = 0,3",
           all(v > 0.3 for k, v in RES.items() if isinstance(k, tuple) and k[0].startswith("nur Brüche p/q"))),
     check("P1 Balmer, nur Brüche: kombiniert p < 0,01", RES[("balmer", "nur Brüche")] < 0.01),
     check("P2 Balmer, volle Grammatik: kombiniert p > 0,1", RES[("balmer", "volle Grammatik")] > 0.1),
     check("Q1 1/alpha = 3700/27: Zufallstrefferquote zwischen 0,3 und 0,7", 0.3 < RES["alpha"] < 0.7),
    ]
    print()
    for n, c in checks:
        tot += 1; ok += c
        print(f"[{'OK ' if c else 'FAIL'}] {n}")
    print(f"\n{ok}/{tot} Prüfungen bestanden")
    raise SystemExit(0 if ok == tot else 1)
