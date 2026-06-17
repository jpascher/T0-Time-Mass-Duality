import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
# ---- LCDM (expansion + Lambda) ----
H0L,Om,OL=67.4,0.315,0.685; tHL=9.778/(H0L/100.0)
age=lambda z:(2/3)/np.sqrt(OL)*tHL*np.arcsinh(np.sqrt(OL/Om)*(1+z)**-1.5)
t0=age(0.0)
# ---- FFGFT / T0 (static, no expansion): 1+z = exp(xi x) = exp(H0 x/c) ; light-travel time = ln(1+z)/H0 ----
H0T=66.2; tHT=9.778/(H0T/100.0)          # 14.77 Gyr
tau_ffgft=lambda z: tHT*np.log(1+z)
z=np.logspace(-1,np.log10(1300),700)
lb_LCDM=t0-age(z); tau_F=tau_ffgft(z)

fig,ax=plt.subplots(figsize=(11.5,6.6)); fig.patch.set_facecolor("white")
ax.plot(z,lb_LCDM,color="#c0392b",lw=2.6,label="$\\Lambda$CDM look-back time  (expansion + $\\Lambda$, $H_0=67.4$)")
ax.plot(z,tau_F,color="#1f77b4",lw=2.6,
        label="FFGFT / T0  $1+z=e^{\\xi x}$ $\\Rightarrow$ light-travel time $=\\ln(1+z)/H_0$  (static, $H_0=66.2$)")
ax.axhline(t0,color="#999",ls=":",lw=1.2)
ax.text(0.105,t0+0.3,"$\\Lambda$CDM age ceiling = Big Bang (13.8 Gyr) — exists ONLY with expansion",fontsize=8.5,color="#777")
ax.text(0.105,18.6,"FFGFT: static, NO Big Bang, NO finite age $\\Rightarrow$ light-travel time grows as $\\ln(1+z)$, unbounded",
        fontsize=8.5,color="#1f77b4")
for zz,lab,col in [(1.86,"cosmic noon $z\\approx1.9$","#888"),
                   (875,"FFGFT $z_*\\approx875$ (Dok 267)","#1f77b4"),
                   (1100,"$\\Lambda$CDM $z_*\\approx1100$","#8e44ad")]:
    ax.axvline(zz,color=col,ls="-",lw=1.0,alpha=0.65)
    ax.text(zz*1.03,0.4,lab,fontsize=8.4,color=col,rotation=90,va="bottom")
# divergence callout at cosmic noon
zc=1.86; yL=t0-age(zc); yF=tau_ffgft(zc)
ax.annotate("",xy=(zc,yF),xytext=(zc,yL),arrowprops=dict(arrowstyle="<->",color="#444"))
ax.text(zc*1.15,(yL+yF)/2,f"same $z$:\n$\\Lambda$CDM {yL:.1f} vs FFGFT {yF:.1f} Gyr",fontsize=8.5,color="#444")
ax.set_xscale("log"); ax.set_xlim(0.1,1300); ax.set_ylim(0,20)
ax.set_xlabel("redshift  $z$   (the only model-independent quantity)",fontsize=12)
ax.set_ylabel("inferred light-travel / look-back time  (Gyr)",fontsize=12)
ax.set_title("Redshift $\\to$ time: $\\Lambda$CDM (expansion) vs FFGFT (static, $z=\\xi x$)\n"
             "the SFRD '0–14 Gyr' axis exists only in $\\Lambda$CDM; FFGFT has distance/light-travel, no cosmic age",
             fontsize=11.5)
ax.legend(loc="upper left",fontsize=9); ax.grid(alpha=0.25,which="both")
fig.tight_layout(); fig.savefig("z_time_ffgft.png",dpi=180,bbox_inches="tight")
print("cosmic noon z=1.9:  LCDM lookback=%.1f Gyr | FFGFT travel=%.1f Gyr"%(t0-age(1.86),tau_ffgft(1.86)))
print("z*=875 FFGFT travel=%.0f Gyr | LCDM lookback@1100=%.2f Gyr (ceiling %.1f)"%(tau_ffgft(875),t0-age(1100),t0))
print("written z_time_ffgft.png")
