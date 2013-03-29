# -*- coding: utf-8 -*-
"""
Created on Wed Nov 07 13:02:37 2012

@author: Brunel
"""

import numpy as np
import matplotlib.pylab as plt
import matplotlib

fonts = {'family':'default',
         'size':'16'}

matplotlib.rc('font',**fonts)

Data = np.random.random_integers(500,600,20)

def RA():
    global E
    global Data
    for i in np.arange(len(Data)):
        E=(E+Data[i])/2
        AV.append(E)

E = 550
AV=[]

RA()


print(AV)
plt.xlabel("Reading")
plt.ylabel("Value")
plt.title("Rolling Average")

plt.plot(Data,'ok',label="Raw Data")
plt.axhline(550,linestyle='--',label="Mean Value")
plt.plot(AV,label="Iterative Average")
plt.legend()
plt.show()