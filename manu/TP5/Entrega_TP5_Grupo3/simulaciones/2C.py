from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import math

fc=1000
fs=100*10**3
fig, ax = plt.subplots(constrained_layout=True)

sys_digital1 = signal.TransferFunction([28.14,-56.28,28.14], [36.64,-54.8,21.64], dt=1/fs)
sys_analogico = signal.TransferFunction([7.03*10**(-10),0,0], [7.03*10**(-10),3.75*10**(-5), 1])

wa, maga,phasea = sys_analogico.bode()
wd1, magd1,phased1 = signal.dbode(sys_digital1)

ax.semilogx(wa/(2*math.pi), maga,color='b',label='Analógico')
ax.semilogx(wd1/(2*math.pi), magd1,color='r',label='Digital ')

ax2.grid(True, which='both', axis='x', color='xkcd:light grey')

ax.set_title('Función de Transferencia')
ax.set_xlabel('Frecuencia (Hz)')
ax.set_ylabel('Ganancia (dB)')
ax.grid(True, which='both', axis='x', color='xkcd:light grey')
plt.legend()
ax2 = ax.twinx()

ax2.semilogx(wa/(2*math.pi), phasea,color='b',linestyle='dashed')
ax2.semilogx(wd1/(2*math.pi), phased1,color='r',linestyle='dashed')
ax2.set_ylabel('Fase (radians)')


