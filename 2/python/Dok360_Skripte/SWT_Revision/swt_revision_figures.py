#!/usr/bin/env python3
"""swt_revision_figures.py — Abbildungen 1–3 der SWT-Revision #12080 (Okt. 2026).
Vorher pruef_swt_revision.py ausführen (liest pruef_swt_revision_ergebnis.json).
Aufruf (aus diesem Ordner): python3 swt_revision_figures.py"""
import sys,os,io,json,contextlib,numpy as np, neurokit2 as nk
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy import signal
from scipy.interpolate import interp1d
HERE=os.path.dirname(os.path.abspath(__file__))
D=sys.argv[1] if len(sys.argv)>1 else os.path.dirname(HERE); sys.path.insert(0,D); os.chdir(HERE)
with contextlib.redirect_stdout(io.StringIO()):
    import polar_h10_atemfrequenz_scan as S
from galois_hrv_preprocess import GALOIS_FLOATS
B,O,A,GR,INK,MUT='#2a78d6','#eb6834','#1baf7a','#8a8a85','#1f1f1e','#6b6b66'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,'axes.edgecolor':MUT,'axes.labelcolor':INK,
  'xtick.color':MUT,'ytick.color':MUT,'axes.spines.top':False,'axes.spines.right':False,'axes.grid':True,
  'grid.color':'#e6e6e2','grid.linewidth':0.6,'lines.linewidth':1.6,'figure.dpi':200})
FS=130
def nkbeats(v):
    c=nk.ecg_clean(v,sampling_rate=FS); _,i=nk.ecg_peaks(c,sampling_rate=FS,correct_artifacts=False)
    return np.asarray(i['ECG_R_Peaks'])
def spec(t,rr,fs=4):
    tg=np.arange(t[0],t[-1],1/fs); rg=interp1d(t,rr,kind='cubic')(tg)
    return signal.welch(rg,fs=fs,window='hann',nperseg=len(rg),nfft=16384,detrend='linear')
# ---- Fig 1 ----
v=S.load_ecg(os.path.join(D,'PolarH10_5min_A2_ECG.jsonl'))
rr_old,_,_,pk_old=S.detect_rpeaks(v); pk_new=nkbeats(v)
fig,ax=plt.subplots(2,1,figsize=(6.5,4.6),gridspec_kw={'height_ratios':[1,1.1]})
t0,t1=60,90; s=slice(t0*FS,t1*FS); tt=np.arange(len(v))/FS
ax[0].plot(tt[s],v[s]/1000,color=GR,lw=0.7)
m=(pk_new>=t0*FS)&(pk_new<t1*FS); ax[0].plot(pk_new[m]/FS,v[pk_new[m]]/1000+0.25,'v',color=B,ms=5,label=f'Validated detector ({len(pk_new)} beats in record)')
m=(pk_old>=t0*FS)&(pk_old<t1*FS); ax[0].plot(pk_old[m]/FS,v[pk_old[m]]/1000+0.55,'x',color=O,ms=5,mew=1.5,label=f'Original detector ({len(pk_old)} beats in record)')
ax[0].set_xlabel('Time (s)'); ax[0].set_ylabel('ECG (mV)'); ax[0].set_ylim(-1.75,1.55); ax[0].legend(loc='upper center',fontsize=7.5,frameon=False,ncol=2,bbox_to_anchor=(0.5,1.0))
ax[0].set_title('a  ECG excerpt, 5 breaths/min (recording 2)',loc='left',fontsize=9,color=INK)
tn=pk_new[1:]/FS; rn=np.diff(pk_new)/FS*1000
ax[1].plot(tn/60,rn,color=B,lw=1.2,label='Corrected: beat times, true time axis')
med=np.median(rr_old); ro=rr_old; to=np.cumsum(ro)/60000
ax[1].plot(to,ro,color=O,lw=1.2,label='Original: retained RR concatenated (axis compressed)')
ax[1].set_xlabel('Time (min)'); ax[1].set_ylabel('RR interval (ms)'); ax[1].legend(fontsize=7.5,frameon=False,loc='upper right')
ax[1].set_title('b  Tachogram',loc='left',fontsize=9,color=INK)
fig.tight_layout(); fig.savefig('Fig1_detection.png'); plt.close(fig)
# ---- Fig 2 ----
recs=[('Spontaneous (supine, 21.9 min)',None,None),('4 breaths/min','PolarH10_4min_A1_ECG.jsonl',4/60),
      ('5 breaths/min (rec. 2)','PolarH10_5min_A2_ECG.jsonl',5/60),('6 breaths/min','PolarH10_6min_ECG.jsonl',6/60)]
fig,axs=plt.subplots(2,2,figsize=(6.5,4.4),sharex=True)
for a,(lab,fn,fr) in zip(axs.flat,recs):
    if fn is None:
        L=[json.loads(l) for l in open(os.path.join(D,'PolarH10_Spontan_HR.jsonl')) if l.strip()]
        rr=np.array([x for o in L for d in o['data'] for x in d.get('rrsMs',[])],float); t=np.cumsum(rr)/1000
        ok=np.abs(rr/np.median(rr)-1)<=0.3; t,rr=t[ok],rr[ok]
    else:
        p=nkbeats(S.load_ecg(os.path.join(D,fn)))/FS; t=p[1:]; rr=np.diff(p)*1000
    f,P=spec(t,rr); m=f<=0.42
    a.axvspan(0.04,0.15,color='#eef4fc',zorder=0); a.axvspan(0.15,0.40,color='#fdf0ea',zorder=0)
    a.plot(f[m],P[m]/1000,color=B,lw=1.4)
    if fr:
        for k,ls in ((1,'--'),(2,':')): a.axvline(k*fr,color=INK,ls=ls,lw=0.9)
    a.set_title(lab,loc='left',fontsize=8.5,color=INK); a.set_xlim(0,0.42)
    if fr is None:
        a.set_ylim(0,50)
for a in axs[1]: a.set_xlabel('Frequency (Hz)')
for a in axs[:,0]: a.set_ylabel('PSD (×10³ ms²/Hz)')
axs[0,0].text(0.095,0.92,'LF',transform=axs[0,0].get_xaxis_transform(),ha='center',color=MUT,fontsize=8)
axs[0,0].text(0.275,0.92,'HF',transform=axs[0,0].get_xaxis_transform(),ha='center',color=MUT,fontsize=8)
fig.text(0.5,0.005,'Dashed: metronome breathing frequency $f_R$;  dotted: $2f_R$',ha='center',fontsize=7.5,color=MUT)
fig.tight_layout(rect=(0,0.03,1,1)); fig.savefig('Fig2_spectra.png'); plt.close(fig)
# ---- Fig 3 ----
from math import gcd
def sm(n):
    for q in (2,3,5,7,11,13):
        while n%q==0:n//=q
    return n==1
G11=np.array(sorted({p/q for q in range(1,12) for p in range(1,4*q+1) if gcd(p,q)==1 and sm(p) and sm(q)}))
rng=np.random.default_rng(1); x=np.exp(rng.uniform(0,np.log(4),100000))
def dist(G,xs):
    i=np.clip(np.searchsorted(G,xs),1,len(G)-1); return np.minimum(abs(xs/G[i-1]-1),abs(xs/G[i]-1))
tol=np.logspace(-4.3,-1.5,200)
d60=np.sort(dist(GALOIS_FLOATS,x)); d11=np.sort(dist(G11,x))
fig,ax=plt.subplots(figsize=(6.5,3.4))
ax.plot(tol*100,np.searchsorted(d60,tol)/len(x),color=B,label='Original grid G(60), 901 elements')
ax.plot(tol*100,np.searchsorted(d11,tol)/len(x),color=A,label='Farey-limited grid G(11), 133 elements')
ax.axvline(1.333,color=INK,ls='--',lw=0.9); ax.text(1.333*1.06,0.05,'100ξ = 1.33 %',fontsize=7.5,color=INK)
R=json.load(open('pruef_swt_revision_ergebnis.json'))
obs=[r['dist_pct'] for r in R['R4'] if r['label'] in ('5/min A1','5/min A2')]+[R['R4_spont']['seg_None']['dist_pct']]
for o in obs: ax.plot(o,np.searchsorted(d60,o/100)/len(x),'o',color=O,ms=6,mec='white',mew=1)
ax.plot([],[],'o',color=O,label='Observed LF/HF distances (re-analysis)')
ax.set_xscale('log'); ax.set_xlabel('Tolerance |r/g − 1| (%)'); ax.set_ylabel('P(random LF/HF is a "hit")')
ax.set_ylim(0,1.02); ax.legend(fontsize=7.5,frameon=False,loc='upper left')
fig.tight_layout(); fig.savefig('Fig3_null.png'); plt.close(fig)
print('ok', obs)
