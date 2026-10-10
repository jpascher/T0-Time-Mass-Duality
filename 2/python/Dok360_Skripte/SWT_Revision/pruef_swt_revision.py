#!/usr/bin/env python3
"""
pruef_swt_revision.py — Prüfskript zur Revision von SWT #12080 (Okt. 2026)
Rechnet alle in der Revision neu verwendeten Zahlen nach:
  R1  Rasterdichte / Zufallstrefferquote (Nullmodell)       [A: grid null, B12]
  R2  Einheiteninvarianz Verhältnisse vs. Bandgrenzen        [B10, A: band limits]
  R3  Auflösungs-Ungleichung und Mindestdauer                [A: 1.33%, B11]
  R4  Reanalyse Polar H10 (Detektor, Zeitachse, Peaks)       [A: Table 1, M2]
  R5  Test-Retest und Gleitfenster-LF/HF vs. Nullrate        [A, B12]
  R6  Fallzahl prospektives Protokoll                        [B13]
Aufruf (aus diesem Ordner): python3 pruef_swt_revision.py   [optional: Pfad zu Dok360_Skripte]
Benötigt: numpy, scipy, neurokit2 (pip install neurokit2)
"""
import sys, os, io, json, contextlib, numpy as np
from math import gcd, pi, sqrt
from fractions import Fraction
from scipy import signal, stats
from scipy.interpolate import interp1d
HERE = os.path.dirname(os.path.abspath(__file__))
D = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(HERE); sys.path.insert(0, D)
with contextlib.redirect_stdout(io.StringIO()):
    import polar_h10_atemfrequenz_scan as S
from galois_hrv_preprocess import GALOIS_FLOATS, GALOIS_GRID, galois_project
import neurokit2 as nk
OUT, ASSERT = {}, []
def check(name, cond): ASSERT.append((name, bool(cond)))
def smooth(n, P=(2,3,5,7,11,13)):
    for p in P:
        while n % p == 0: n //= p
    return n == 1
XI = 4/30000; RES = 100*XI

# ---------------- R1 Nullmodell ----------------
def grid(qmax, hi=4.0, P=(2,3,5,7,11,13)):
    return np.array(sorted({p/q for q in range(1,qmax+1) for p in range(1,int(hi*q)+1)
                            if gcd(p,q)==1 and smooth(p,P) and smooth(q,P)}))
G60 = GALOIS_FLOATS; G11 = grid(11)
rng = np.random.default_rng(12080)
x = np.exp(rng.uniform(np.log(1.0), np.log(4.0), 200_000))   # log-uniform LF/HF in [1,4]
def cov(G, xs, tol):
    i = np.clip(np.searchsorted(G, xs), 1, len(G)-1)
    d = np.minimum(abs(xs/G[i-1]-1), abs(xs/G[i]-1)); return float((d <= tol).mean())
tols = {"1.33%":RES, "0.14%":0.0014, "0.06%":0.0006, "0.02%":0.0002}
OUT["R1"] = {"n_G60": len(G60), "n_G11": len(G11),
             "cov_G60": {k: cov(G60,x,t) for k,t in tols.items()},
             "cov_G11": {k: cov(G11,x,t) for k,t in tols.items()}}
check("R1a q<=60-Raster hat 901 Elemente", len(G60)==901)
check("R1b q<=60 @1.33% deckt >99% ab (Kriterium nicht diskriminativ)", OUT["R1"]["cov_G60"]["1.33%"]>0.99)
check("R1c q<=60 @0.06% Zufallsquote >30%", OUT["R1"]["cov_G60"]["0.06%"]>0.30)
# Fantasia-Kriterium: nächstes q<=60-Element ist 5-smooth, LF/HF in [0.4,4.5]
G60f = [Fraction(g) for g in GALOIS_GRID]
xf = np.exp(rng.uniform(np.log(0.4), np.log(4.4), 50_000))
idx = np.array([np.argmin(abs(GALOIS_FLOATS - v)) for v in xf[:20000]])
fs5 = np.array([smooth(G60f[i].numerator,(2,3,5)) and smooth(G60f[i].denominator,(2,3,5)) for i in idx])
OUT["R1"]["fantasia_5limit_null"] = float(fs5.mean())
check("R1d Fantasia 4/10 liegt im Nullbereich (binom p>0.05)",
      stats.binomtest(4,10,fs5.mean(),alternative='greater').pvalue > 0.05)
OUT["R1"]["fantasia_binom_p"] = stats.binomtest(4,10,fs5.mean(),alternative='greater').pvalue

# ---------------- R2 Einheiten ----------------
bands_hz = [Fraction(1,25), Fraction(3,20), Fraction(2,5)]
def is5(fr): return smooth(fr.numerator,(2,3,5)) and smooth(fr.denominator,(2,3,5))
OUT["R2"] = {"Hz": [is5(b) for b in bands_hz],
             "cpm(x60)": [is5(b*60) for b in bands_hz],
             "mHz(x1000)": [is5(b*1000) for b in bands_hz],
             "period_s": [is5(1/b) for b in bands_hz],
             "rad/s(x2pi)": "irrational -> not classifiable",
             "share_2dec_5smooth": sum(is5(Fraction(k,100)) for k in range(1,100))/99,
             "share_1sigdigit_5smooth": sum(smooth(d,(2,3,5)) for d in range(1,10))/9}
check("R2a Bandgrenzen 5-smooth in Hz, cpm, mHz, Periode", all(OUT["R2"]["Hz"]+OUT["R2"]["cpm(x60)"]+OUT["R2"]["mHz(x1000)"]+OUT["R2"]["period_s"]))
check("R2b 8/9 aller einstelligen Rundwerte sind 5-smooth", abs(OUT["R2"]["share_1sigdigit_5smooth"]-8/9)<1e-9)
r = 2.515; check("R2c Verhältnis einheitenfrei: (r*60)/(60) == r", abs((r*0.1*60)/(0.1*60)-r)<1e-12)

# ---------------- R3 Auflösung ----------------
fLF = 0.10
OUT["R3"] = {"T_min_s_at_0.1Hz": 1/(RES*fLF), "T_min_min": 1/(RES*fLF)/60,
             "T_min_min_at_0.083Hz": 1/(RES*1/12)/60,
             "rel_res_5min_record": (1/300)/fLF, "rel_res_180s_seg": (1/180)/fLF,
             "rel_res_64s_seg": (1/64)/fLF, "Qc": pi/sqrt(6*RES)}
check("R3a T_min = 1/(0.0133*0.1 Hz) = 12.5 min (Ungleichung: Delta f <= 0.0133 f)", abs(OUT["R3"]["T_min_min"]-12.5)<0.01)
check("R3b 5-min-Aufnahme: Delta f/f = 3.3% > 1.33%", OUT["R3"]["rel_res_5min_record"]>RES)

# ---------------- R4 Reanalyse ----------------
FS = 130
def beats_nk(v):
    c = nk.ecg_clean(v, sampling_rate=FS, method="neurokit")
    _, info = nk.ecg_peaks(c, sampling_rate=FS, method="neurokit", correct_artifacts=False)
    return np.asarray(info["ECG_R_Peaks"])/FS
def spectrum(tb, rr, seg=None, fs=4.0):
    tg = np.arange(tb[0], tb[-1], 1/fs); rg = interp1d(tb, rr, kind="cubic")(tg)
    n = len(rg) if seg is None else min(int(seg*fs), len(rg))
    return signal.welch(rg, fs=fs, window="hann", nperseg=n, noverlap=n//2,
                        nfft=max(16384, n), detrend="linear")
def bp(f,p,a,b): m=(f>=a)&(f<b); return float(np.trapezoid(p[m],f[m]))
def pk(f,p,a,b): m=(f>=a)&(f<b); return float(f[m][np.argmax(p[m])])
def clean_rr(t):
    rr = np.diff(t)*1000; tb = t[1:]; ok = np.abs(rr/np.median(rr)-1) <= 0.30
    d = np.diff(rr); okd = ok[1:] & ok[:-1]
    return tb[ok], rr[ok], int((~ok).sum()), float(np.sqrt(np.mean(d[okd]**2)))
rows = []
for lab, fn, fset in S.AUFNAHMEN:
    v = S.load_ecg(os.path.join(D, fn)); T = len(v)/FS
    rr_old, nart_old, _, pk_old = S.detect_rpeaks(v)
    t = beats_nk(v); tb, rr, nart, rmssd = clean_rr(t)
    f, p = spectrum(tb, rr)
    lf, hf = bp(f,p,.04,.15), bp(f,p,.15,.40)
    _, frac, dist, _ = galois_project(lf/hf)
    rows.append(dict(label=lab, file=fn, f_set=fset/60, T_ecg_min=T/60,
        old_beats=int(len(pk_old)), old_rr_span_min=float(np.sum(rr_old)/60000),
        nk_beats=int(len(t)), artefacts=nart, rmssd=rmssd, mean_hr=float(60000/np.mean(rr)),
        f_dom=pk(f,p,.02,.40), f_LFpk=pk(f,p,.04,.15), f_HFpk=pk(f,p,.15,.40),
        lf=lf, hf=hf, lfhf=lf/hf, galois=str(frac), dist_pct=dist*100,
        md5=__import__("hashlib").md5(open(os.path.join(D,fn),"rb").read()).hexdigest()))
OUT["R4"] = rows
dup = rows[0]["md5"] == rows[1]["md5"]; OUT["R4_duplicate_4min"] = dup
check("R4a 4/min A1 und A2 byte-identisch (nur eine 4/min-Aufnahme)", dup)
miss = [1 - r["old_beats"]/r["nk_beats"] for r in rows]
OUT["R4_old_missed_fraction"] = [min(miss), max(miss)]
check("R4b Originaldetektor verpasst >30% der Schläge in jeder Aufnahme", min(miss) > 0.30)
comp = [r["old_rr_span_min"]/r["T_ecg_min"] for r in rows]
OUT["R4_old_timeaxis_factor"] = [min(comp), max(comp)]
check("R4c Originalpipeline staucht Zeitachse auf <70%", max(comp) < 0.70)
for r in rows:
    if r["label"] == "4/min A2": continue          # Duplikat von A1
    if r["f_set"] >= 4/60:
        check(f"R4d {r['label']}: dominanter Peak = Metronomfrequenz (±1/T)", abs(r["f_dom"]-r["f_set"]) <= 1/(r["T_ecg_min"]*60))
    if r["f_set"] >= 4/60 and 2*r["f_set"] >= 0.15:   # 2. Harmonische liegt im HF-Band
        check(f"R4e {r['label']}: HF-Peak = 2. Harmonische der Atmung (±2/T)", abs(r["f_HFpk"]-2*r["f_set"]) <= 2/(r["T_ecg_min"]*60))
# spontaneous (device RR, contiguous)
L = [json.loads(l) for l in open(os.path.join(D,"PolarH10_Spontan_HR.jsonl")) if l.strip()]
rrs = np.array([x for o in L for d in o["data"] for x in d.get("rrsMs",[])], float)
ts = np.cumsum(rrs)/1000; tb, rr, nart, rmssd = clean_rr(np.concatenate([[0.0], ts]))
rmssd_raw = float(np.sqrt(np.mean(np.diff(rrs)**2)))
sp = {"n_rr": len(rrs), "T_min": ts[-1]/60, "artefacts": nart, "rmssd_clean": rmssd,
      "rmssd_raw": rmssd_raw, "max_rr": float(rrs.max()), "mean_hr": float(60000/np.mean(rr))}
for seg in (None, 300):
    f, p = spectrum(tb, rr, seg=seg); lf, hf = bp(f,p,.04,.15), bp(f,p,.15,.40)
    _, frac, dist, _ = galois_project(lf/hf)
    sp[f"seg_{seg}"] = dict(f_LFpk=pk(f,p,.04,.15), f_HFpk=pk(f,p,.15,.40), lfhf=lf/hf, galois=str(frac), dist_pct=dist*100)
OUT["R4_spont"] = sp
check("R4f Spontan: ein verpasster Schlag verdoppelt RMSSD nahezu", rmssd_raw/rmssd > 1.8)

# ---------------- R5 Test-Retest, Gleitfenster ----------------
a1 = [r for r in rows if r["label"]=="5/min A1"][0]["lfhf"]; a2 = [r for r in rows if r["label"]=="5/min A2"][0]["lfhf"]
OUT["R5_retest_5min"] = {"A1": a1, "A2": a2, "rel_diff": abs(a1-a2)/((a1+a2)/2)}
check("R5a Test-Retest 5/min: Differenz >20% (>> 0.02%)", OUT["R5_retest_5min"]["rel_diff"] > 0.20)
win, step = 300, 60; vals = []
tg = np.arange(tb[0], tb[-1], 0.25); rg = interp1d(tb, rr, kind="cubic")(tg)
for s0 in np.arange(tb[0], tb[-1]-win, step):
    m = (tg>=s0)&(tg<s0+win); f,p = signal.welch(rg[m], fs=4, window="hann", nperseg=m.sum(), nfft=16384, detrend="linear")
    vals.append(bp(f,p,.04,.15)/bp(f,p,.15,.40))
vals = np.array(vals); d60 = np.array([galois_project(v)[2] for v in vals])
OUT["R5_sliding"] = {"n_win": len(vals), "lfhf_min": float(vals.min()), "lfhf_max": float(vals.max()),
    "cv": float(vals.std(ddof=1)/vals.mean()), "hit_0.06": float((d60<=0.0006).mean()),
    "hit_1.33": float((d60<=RES).mean())}
check("R5b Gleitfenster-LF/HF streut >20% (CV)", OUT["R5_sliding"]["cv"] > 0.20)
inr = (vals >= 1.0) & (vals <= 4.0); k = int((d60[inr] <= 0.0006).sum()); n = int(inr.sum())
ci = stats.binomtest(k, n).proportion_ci(method="wilson")
OUT["R5_sliding"].update({"n_in_1_4": n, "hits_in_1_4_0.06": k, "rate_in_1_4": k/n,
    "ci95": [float(ci.low), float(ci.high)], "binom_p_vs_null": float(stats.binomtest(k, n, OUT["R1"]["cov_G60"]["0.06%"]).pvalue)})
check("R5c Gleitfenster in [1,4]: Trefferquote mit Nullrate vereinbar (p>0.05)", OUT["R5_sliding"]["binom_p_vs_null"] > 0.05)

# ---------------- R6 Fallzahl ----------------
def n_paired(dz, alpha=0.05, power=0.80):
    for n in range(3, 500):
        df = n-1; tc = stats.t.ppf(1-alpha/2, df); nc = dz*np.sqrt(n)
        if 1 - stats.nct.cdf(tc, df, nc) + stats.nct.cdf(-tc, df, nc) >= power: return n
OUT["R6"] = {f"dz={dz}": n_paired(dz) for dz in (0.5, 0.6, 0.8)}
OUT["R6"]["planned_n_with_20pct_dropout"] = int(np.ceil(OUT["R6"]["dz=0.6"]/0.8))
check("R6a n(dz=0.6, 80%, alpha .05 zweiseitig) = 24", OUT["R6"]["dz=0.6"] == 24)

json.dump(OUT, open(os.path.join(HERE, "pruef_swt_revision_ergebnis.json"),"w"), indent=1, default=str)
print(json.dumps(OUT["R6"]))
print()
for n, c in ASSERT: print(("OK  " if c else "FAIL"), n)
print(f"\n{sum(c for _,c in ASSERT)}/{len(ASSERT)} Assertions bestanden")
