# Schritt 3: Lomb-Scargle (ohne Resampling), Atemreferenz aus RESP-Kanal, DFA
import numpy as np
from scipy import signal
from scipy.signal import lombscargle
tz=np.trapezoid
rr=np.loadtxt('rr01.csv'); rr=rr[(rr>300)&(rr<2000)]
t=np.cumsum(rr)/1000; t-=t[0]; x=rr-rr.mean()
f=np.linspace(0.003,0.5,5000); P=lombscargle(t,x,2*np.pi*f,normalize=True)
pk={}
for n,(lo,hi) in {"VLF":(.003,.04),"LF":(.04,.15),"HF":(.15,.4)}.items():
    m=(f>=lo)&(f<hi); pk[n]=f[m][np.argmax(P[m])]; print(f"  {n}: Peak {pk[n]:.4f} Hz")
print(f"  HF/LF = {pk['HF']/pk['LF']:.3f}  (5/2 = 2.500)")
try:
    import wfdb
    r=wfdb.rdrecord('bidmc01'); resp=np.nan_to_num(r.p_signal[:,0]); fs=r.fs
    fr,pr=signal.welch(signal.detrend(resp),fs=fs,nperseg=4096); m=(fr>0.1)&(fr<0.6)
    print(f"  Atemfrequenz (RESP-Kanal): {fr[m][np.argmax(pr[m])]:.3f} Hz  -> HF-Peak = Atmung")
except Exception as e: print("  (RESP-Kanal nicht verfuegbar:",e,")")
def dfa(x,scales):
    y=np.cumsum(x-x.mean()); F=[]
    for s in scales:
        n=len(y)//s; segs=y[:n*s].reshape(n,s); t_=np.arange(s)
        res=[seg-np.polyval(np.polyfit(t_,seg,1),t_) for seg in segs]
        F.append(np.sqrt(np.mean(np.concatenate(res)**2)))
    return np.array(F)
s1=np.arange(4,17); s2=np.arange(16,65)
print(f"  DFA alpha1 = {np.polyfit(np.log(s1),np.log(dfa(rr,s1)),1)[0]:.3f}, alpha2 = {np.polyfit(np.log(s2),np.log(dfa(rr,s2)),1)[0]:.3f}  (gesund ~1.0, weiss 0.5)")
