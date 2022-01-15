from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import math

fc=1000
fs=100*10**3
fig, ax = plt.subplots(constrained_layout=True)

sys_digital1 = signal.TransferFunction([39478417.60,78956835.20,39478417.60], [41816631592.86, -79921043164.79,38262325242.34], dt=1/fs)
sys_analogico = signal.TransferFunction([(2*np.pi*fc)**2], [1, 2*np.pi*fc*np.sqrt(2), (2*np.pi*fc)**2])


wa, maga,phasea = sys_analogico.bode()
wd1, magd1,phased1 = signal.dbode(sys_digital1)

ax.semilogx(wa/(2*math.pi), maga,color='b',label='Analógico')
ax.semilogx(wd1/(2*math.pi), magd1,color='r',label='Digital ')


ax.set_title('2A')
ax.set_xlabel('Frecuencia (Hz)')
ax.set_ylabel('Ganancia (dB)')
ax.grid(True, which='both', axis='x', color='xkcd:light grey')
plt.legend()
ax2 = ax.twinx()
ax2.grid(True, which='both', axis='x', color='xkcd:light grey')

ax2.semilogx(wa/(2*math.pi), phasea,color='b',linestyle='dashed')
ax2.semilogx(wd1/(2*math.pi), phased1,color='r',linestyle='dashed')
ax2.set_ylabel('Fase (radians)')


