import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
H0,Om,OL=67.4,0.315,0.685; tH=9.778/(H0/100.0)   # Hubble time 14.51 Gyr
age=lambda z:(2/3)/np.sqrt(OL)*tH*np.arcsinh(np.sqrt(OL/Om)*(1+z)**-1.5)
t0=age(0.0)                                        # 13.80 Gyr
z=np.logspace(-1,np.log10(1300),600)
lb_LCDM=t0-age(z)                                  # LCDM look-back (assumes expansion+Lambda)
tau_static=tH*np.log(1+z)                          # generic static benchmark (tired-light): no a(t)

fig,ax=plt.subplots(figsize=(11,6.4)); fig.patch.set_facecolor("white")
ax.plot(z,lb_LCDM,color="#c0392b",lw=2.6,label="$\\Lambda$CDM look-back time  (assumes expansion + $\\Lambda$)")
ax.plot(z,tau_static,color="#2c3e50",lw=2.0,ls="--",
        label="generic STATIC benchmark $\\tau=\\ln(1+z)/H_0$  (no expansion; illustrative, not FFGFT)")
ax.axhline(t0,color="#999",ls=":",lw=1.2)
ax.text(0.11,t0+0.3,"$\\Lambda$CDM age ceiling = Big Bang (13.8 Gyr) — exists only WITH expansion",fontsize=8.5,color="#777")

# markers
for zz,lab,col in [(1.86,"cosmic noon\n$z\\approx1.9$","#888"),
                   (875,"FFGFT $z_*\\approx875$\n(Dok 267)","#27ae60"),
                   (1100,"$\\Lambda$CDM $z_*\\approx1100$","#8e44ad")]:
    ax.axvline(zz,color=col,ls="-",lw=1.0,alpha=0.7)
    ax.text(zz*1.02,1.0,lab,fontsize=8.5,color=col,rotation=90,va="bottom")

ax.set_xscale("log"); ax.set_xlim(0.1,1300); ax.set_ylim(0,20)
ax.set_xlabel("redshift  $z$   (model-independent observable)",fontsize=12)
ax.set_ylabel("inferred time  (Gyr)",fontsize=12)
ax.set_title("Redshift $\\to$ time is MODEL-DEPENDENT\n"
             "the SFRD age-axis is a $\\Lambda$CDM construct — FFGFT (no $a(t)$) only maps onto it",fontsize=12)
ax.legend(loc="upper left",fontsize=9); ax.grid(alpha=0.25,which="both")
ax.annotate("same observed $z$,\ndifferent inferred time",xy=(3,tau_static[np.argmin(abs(z-3))]),
            xytext=(0.18,15),fontsize=9,color="#444",
            arrowprops=dict(arrowstyle="->",color="#444"))
fig.tight_layout(); fig.savefig("z_time_mapping.png",dpi=180,bbox_inches="tight")
print("LCDM lookback@z=1.9 = %.1f Gyr ; static@z=1.9 = %.1f Gyr"%(t0-age(1.86),tH*np.log(2.86)))
print("LCDM age ceiling t0 = %.2f Gyr ; static has NO ceiling (no Big Bang)"%t0)
print("written z_time_mapping.png")
