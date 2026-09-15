#!/usr/bin/env python3
"""
polar_h10_atemfrequenz_scan.py — Reproduzierbare Analyse aller Polar H10 Aufnahmen
Dok. 360, Johann Pascher, 10. September 2026

Aufnahmen (Metronom: Klick = Wechsel):
  PolarH10_Spontan_HR.jsonl     — liegend, spontane Atmung (HR-only, RMSSD=36.3ms)
  PolarH10_4min_A1_ECG.jsonl    — sitzend, 8 bpm → 4/min (Aufn.1)
  PolarH10_4min_A2_ECG.jsonl    — sitzend, 8 bpm → 4/min (Aufn.2)
  PolarH10_6min_ECG.jsonl       — sitzend, 12 bpm → 6/min
  PolarH10_5min_A1_ECG.jsonl    — sitzend, 10 bpm → 5/min (2 Artefakte)
  PolarH10_5min_A2_ECG.jsonl    — sitzend, 10 bpm → 5/min (sauber)
  PolarH10_2min_A1_ECG.jsonl    — sitzend, 4 bpm  → 2/min (2 Artefakte)
  PolarH10_2min_A2_ECG.jsonl    — sitzend, 4 bpm  → 2/min (sauber)

Reproduziert Tab. 4 aus Dok. 360.
"""

import os, sys, json
import numpy as np
from scipy import signal
from scipy.interpolate import interp1d

sys.path.insert(0, os.path.dirname(__file__))
from galois_hrv_preprocess import (
    galois_project, galois_depth, arnold_tongue_width,
    HRV_BANDS, RES_LIMIT, _prime_factors
)

BASE = os.path.dirname(__file__)

AUFNAHMEN = [
    ("4/min A1",  "PolarH10_4min_A1_ECG.jsonl",   4.0),
    ("4/min A2",  "PolarH10_4min_A2_ECG.jsonl",   4.0),
    ("6/min",     "PolarH10_6min_ECG.jsonl",      6.0),
    ("5/min A1",  "PolarH10_5min_A1_ECG.jsonl",   5.0),
    ("5/min A2",  "PolarH10_5min_A2_ECG.jsonl",   5.0),
    ("2/min A1",  "PolarH10_2min_A1_ECG.jsonl",   2.0),
    ("2/min A2",  "PolarH10_2min_A2_ECG.jsonl",   2.0),
]

def load_ecg(fname):
    with open(fname) as f:
        lines = [json.loads(l) for l in f if l.strip()]
    return np.array([d['voltage'] for obj in lines
                     for d in obj.get('data',[])], float)

def detect_rpeaks(voltages, fs=130.0):
    b,a = signal.butter(3,[5/(fs/2),40/(fs/2)],btype='band')
    ef = signal.filtfilt(b,a,voltages)
    esq = ef**2
    ema = np.convolve(esq,np.ones(int(0.15*fs))/int(0.15*fs),mode='same')
    peaks,_ = signal.find_peaks(ema,height=np.percentile(ema,90),
                                 distance=int(0.3*fs))
    rr = np.diff(peaks)/fs*1000
    rr = rr[(rr>300)&(rr<1500)]
    med = np.median(rr)
    rr_clean = rr[(rr>0.70*med)&(rr<1.30*med)]
    n_art = len(rr)-len(rr_clean)
    return rr_clean, n_art, ema, peaks

def welch_lf_hf(rr, fs=4.0):
    t = np.cumsum(rr)/1000.0
    tg = np.arange(t[0],t[-1],1/fs)
    rg = interp1d(t,rr,kind='cubic',bounds_error=False,
                  fill_value='extrapolate')(tg)
    nperseg = min(int(3*60*fs),len(rg))
    f,p = signal.welch(rg,fs=fs,nperseg=nperseg,nfft=nperseg*8)
    def pk(flo,fhi):
        m=(f>=flo)&(f<fhi)
        if not m.any(): return None,0.0
        i=np.argmax(p[m]); fm=f[m]; pm=p[m]
        if 0<i<len(fm)-1:
            a,b,c=pm[i-1],pm[i],pm[i+1]
            d=0.5*(a-c)/(a-2*b+c) if (a-2*b+c)!=0 else 0
            return float(fm[i]+d*(fm[1]-fm[0])),float(np.trapezoid(pm,fm))
        return float(fm[i]),float(np.trapezoid(pm,fm))
    return pk(*HRV_BANDS['LF']), pk(*HRV_BANDS['HF'])

def atem_freq(ema, peaks, fs=130.0, fs_rr=4.0):
    r_amps = ema[peaks]
    t_r = peaks/fs
    tg = np.arange(t_r[0],t_r[-1],1/fs_rr)
    ag = interp1d(t_r,r_amps,kind='cubic',
                  bounds_error=False,fill_value='extrapolate')(tg)
    nperseg = min(int(3*60*fs_rr),len(ag))
    f,p = signal.welch(ag,fs=fs_rr,nperseg=nperseg,nfft=nperseg*8)
    m=(f>=0.02)&(f<=0.20)
    return float(f[m][np.argmax(p[m])]) if m.any() else None

print("Atemfrequenz-Scan — Polar H10 — Johann Pascher, 10.9.2026")
print("="*72)
print(f"{'Aufnahme':<12} {'Atem/min':>9} {'LF Hz':>7} {'RMSSD':>7} "
      f"{'Artefakte':>10} {'LF/HF':>7} {'p/q':>7} {'k':>3}")
print("-"*72)

for label, fname, atem_soll in AUFNAHMEN:
    fpath = os.path.join(BASE, fname)
    if not os.path.exists(fpath):
        print(f"{label:<12} Datei nicht gefunden: {fname}")
        continue
    v = load_ecg(fpath)
    rr, n_art, ema, peaks = detect_rpeaks(v)
    if len(rr) < 20:
        print(f"{label:<12} zu wenig RR-Intervalle"); continue

    rmssd = np.sqrt(np.mean(np.diff(rr)**2))
    (lf_p, lf_pow), (hf_p, hf_pow) = welch_lf_hf(rr)
    f_atem = atem_freq(ema, peaks)

    lf_hf = lf_pow/hf_pow if hf_pow > 0 else None
    galois_str = "—"
    k_str = "—"
    if lf_hf:
        _, frac, dist, in_grid = galois_project(lf_hf)
        k = galois_depth(frac)
        galois_str = str(frac)
        k_str = str(k)

    atem_str = f"{f_atem*60:.1f}" if f_atem else "—"
    lf_str = f"{lf_p:.3f}" if lf_p else "—"
    lfhf_str = f"{lf_hf:.3f}" if lf_hf else "—"

    print(f"{label:<12} {atem_str:>9} {lf_str:>7} {rmssd:>7.1f} "
          f"{n_art:>10} {lfhf_str:>7} {galois_str:>7} {k_str:>3}")

print("-"*72)
print(f"\nArtefakt-Filterung: Median ±30%")
print(f"Auflösungsgrenze:   Δf/f ≥ {RES_LIMIT*100:.2f}% (FFGFT Dok.343)")
print(f"Galois-Raster:      Primfaktoren ⊆ {{2,3,5,7,11,13}} (Dok.358)")
