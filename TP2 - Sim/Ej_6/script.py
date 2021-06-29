# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
from splane import pzmap, grpDelay, bodePlot, convert2SOS
from scipy import signal

# Esta es una liberia tomada de la comunidad [https://stackoverflow.com/questions/35304245/multiply-scipy-lti-transfer-functions?newreg=b12c460c179042b09ad75c2fb4297bc9]
from ltisys import *

e = .096
a = np.roots([-256*e,0,-640*e,0,-560*e,0,-200*e,0,-25*e,0,1])

# Coeficientes Transferencias
q_1 = 2.59

k = 1

q_2 = 4.3
w_2 = 1.025

q_3 = 1.12
w_3 = 0.703

# Genero la función transferencia T1 en S
num_t1 = [1, 0]
den_t1 = [1, q_1]
T1 = ltimul(num_t1, den_t1);

# Genero la función transferencia T2 en S
num_t2 = [1, 0, 0]
den_t2 = [1, 1 / (q_2 * w_2), 1/ (w_2**2)]
T2 = ltimul(num_t2, den_t2);

# Genero la función transferencia T3 en S
num_t3 = [1, 0, 0]
den_t3 = [1, 1 / (q_3 * w_3), 1/ (w_3**2)]
T3 = ltimul(num_t3, den_t3);


T = T1 * T2 * T3
#pzmap(T, 1);
#fig, ax = bodePlot(T1.to_ss(), 2);
#fig, ax = bodePlot(T2.to_ss(), 2);
#fig, ax = bodePlot(T3.to_ss(), 2);
fig, ax = bodePlot(T.to_ss(), 2);
#ax[0].set_xlim(1e-1,1e1)
#ax[0].set_ylim(-100, 10)
#ax[1].set_xlim(1e-1,1e1)