# -*- coding: utf-8 -*-
"""
Created on Wed Nov 07 13:02:37 2012

@author: Brunel
"""

import numpy as np
import matplotlib.pylab as plt

Data = np.random.random_integers(500,600,20)

def RA():
    global E
    global Data
    Average=0
    count = len(Data)
    for i in Data:
        Average+=i
    E = (E+average)/2

E = 550

plt.plot(Data,'ok')
plt.axhline(550,'--')
plt.show()