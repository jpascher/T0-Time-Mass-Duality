# Schritt 2 (Welch, 8192-Punkte-Zero-Padding, parabolische Peakinterpolation)
# Testet: liegen die Peak-Verhaeltnisse VLF/LF/HF in 5-limit-Bruechen (Nenner<=12, +-15 Cent)?
import numpy as np
from scipy import signal
from scipy.interpolate import interp1d
from fractions import Fraction
from math import gcd
def pf(n):
    f={};p=2
    while p*p<=n:
        while n%p==0: f[p]=f.get(p,0)+1; n//=p
        p+=1
    if n>1: f[n]=f.get(n,0)+1
    return f
def gradus(p,q):
    g=gcd(p,q); return 1+sum((k-1)*m for k,m in pf((p//g)*(q//g)).items())
def five(p,q):
    g=gcd(p,q); return set(pf((p//g)*(q//g)))<={2,3,5}
rr=np.loadtxt('rr01.csv'); rr=rr[(rr>300)&(rr<2000)]
t=np.cumsum(rr)/1000; t-=t[0]; fs=4.0; ti=np.arange(0,t[-1],1/fs)
x=signal.detrend(interp1d(t,rr,kind='cubic')(ti))
freqs,psd=signal.welch(x,fs=fs,nperseg=len(x),nfft=8192)
pk={}
for n,(lo,hi) in {"VLF":(.003,.04),"LF":(.04,.15),"HF":(.15,.40)}.items():
    m=(freqs>=lo)&(freqs<hi); idx=np.where(m)[0][np.argmax(psd[m])]
    a,b,c=np.log(psd[idx-1:idx+2]+1e-30); d=0.5*(a-c)/(a-2*b+c)
    pk[n]=freqs[idx]+d*(freqs[1]-freqs[0])
print("Welch-Peaks:",{k:round(v,4) for k,v in pk.items()})
TOL=15; names=list(pk); hits=0
for i in range(3):
    for j in range(i+1,3):
        r=pk[names[j]]/pk[names[i]]; fr=Fraction(r).limit_denominator(12)
        c=1200*np.log2(r/float(fr)); ok=abs(c)<=TOL and five(fr.numerator,fr.denominator); hits+=ok
        print(f"  {names[j]}/{names[i]}: {r:.3f} ~ {fr} ({c:+.1f} Cent) Grad {gradus(fr.numerator,fr.denominator)} 5-limit: {'JA' if ok else 'NEIN'}")
print(f"Beobachtet: {hits}/3")
rng=np.random.default_rng(0); N=5000; nh=0
for _ in range(N):
    p={"VLF":rng.uniform(.003,.04),"LF":rng.uniform(.04,.15),"HF":rng.uniform(.15,.40)}; ok=True
    for i in range(3):
        for j in range(i+1,3):
            r=p[names[j]]/p[names[i]]; fr=Fraction(r).limit_denominator(12); c=1200*np.log2(r/float(fr))
            if not(abs(c)<=TOL and five(fr.numerator,fr.denominator)): ok=False
    nh+=ok
print(f"Nullmodell (zufaellige Peaks, gleiches Kriterium): alle 3 erfuellt in {100*nh/N:.1f}%")
