# Schritt 1: R-Zacken aus BIDMC-01 (ECG-Kanal II), RR-Intervalle -> rr01.csv
# Quelle: https://physionet.org/files/bidmc/1.0.0/bidmc01.dat / .hea  (Pimentel et al. 2017, CC-BY)
import wfdb, numpy as np
from scipy import signal
from scipy.signal import find_peaks
r = wfdb.rdrecord('bidmc01')                # braucht bidmc01.dat + bidmc01.hea im Ordner
ecg = np.nan_to_num(r.p_signal[:, 4]); fs = r.fs   # Kanal 4 = Ableitung II, fs = 125 Hz
b, a = signal.butter(3, [5/(fs/2), 20/(fs/2)], 'band')
y = signal.filtfilt(b, a, ecg)
pk, _ = find_peaks(y, distance=int(0.4*fs), height=np.percentile(y, 95)*0.5)
rr = np.diff(pk)/fs*1000
print(f"{len(pk)} R-Zacken, HR {60000/np.median(rr):.0f} bpm, SDNN {rr.std():.1f} ms")
np.savetxt('rr01.csv', rr, delimiter=',')
