# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 09:28:47 2012

@author: quade7
"""
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pylab as plt
#from matplotlib.widgets import Slider,Button

fig = plt.figure()
ax = Axes3D(fig)

def hermite(xi,mi,xf,mf,t):
    h1 = 2*t**3 - 3*t**2 + 1
    h2 = t**3 - 2*t**2 + t
    h3 = -2*t**3 + 3*t**2
    h4 = t**3 - t**2
    return h1*xi+h2*mi+h3*xf+h4*mf

def hermiteDt(xi,mi,xf,mf,t):
    h1 = 6*t**2 - 6*t
    h2 = 3*t**2 - 4*t + 1
    h3 = -6*t**2 + 6*t
    h4 = 3*t**2 - 2*t
    return h1*xi+h2*mi+h3*xf+h4*mf

xi=20
mxi=20
xf=10
mxf=-40

yi=40
myi=20
yf=20
myf=-40

steps = np.r_[0:1:150j]
pSteps=[0.1,0.3,0.5,0.7,0.9]


Hx=[]
Hy=[]

Hxp=[]
Hyp=[]

Hxdt=[]
Hydt=[]

for i in steps:
    hx=hermite(xi,mxi,xf,mxf,i)
    hy=hermite(yi,myi,yf,myf,i)
    Hx.append(hx)
    Hy.append(hy)
    Hxdt.append(hermiteDt(xi,mxi,xf,mxf,i))
    Hydt.append(hermiteDt(yi,myi,yf,myf,i))

for i in pSteps:
    hx=hermite(xi,mxi,xf,mxf,i)
    hy=hermite(yi,myi,yf,myf,i)
    Hxp.append(hx)
    Hyp.append(hy)

#ax.plot(Hx,Hy)

plt.subplot(321)
plt.plot(steps,Hx)

plt.subplot(322)
plt.plot(steps,Hxdt)

plt.subplot(323)
plt.plot(steps,Hy)

plt.subplot(324)
plt.plot(steps,Hydt)

plt.subplot(325)
plt.plot(Hx,Hy)
plt.plot(Hxp,Hyp,'ok')

plt.show()