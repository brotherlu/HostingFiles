"""
Measuring the arduino leads to finding that we can achieve 20
values per second.10 is good enough for on-the-fly analysis

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

font = {'family':'default',
        'size':16}


matplotlib.rc('font',**font)

def kalmangain(V,Err):
	return V / ( V + Err )

def updateEstimate(E,KG,D):
	return E + KG * ( D - E )

def updateVariance(V,KG):
	return ( 1 - KG ) * V

def kalmanFilter(Err,D):
	global E
	global V
	global Estimates
	global Variances
	for d in D:
		KG = kalmangain(V,Err)
		E = updateEstimate(E,KG,d)
		Estimates.append(E)
		V = updateVariance(V,KG)
		Variances.append(V)

Data = np.random.random_integers(500,600,30)

#Data = Data / 100.

E=550.
V=1.
Err=.5 # LV-EZ1 noise in inches

Estimates=[]
Variances=[]

kalmanFilter(Err,Data)

mean = np.mean(Data)

print("Mean: " + str(mean))
print("Kalman Estimate: " + str(E))
print("Kalman Variance: " + str(V))

plt.subplot(211)
plt.title("Estimate")
plt.plot(Estimates,label='Estimates')
plt.plot(Data,'ko',label='Raw Data')
plt.axhline(550,linestyle = '--',label='Mean')
plt.legend()
plt.subplot(212)
plt.title("Variance")
plt.plot(Variances)
plt.show()
