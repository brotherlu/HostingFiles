# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 12:17:30 2012

@Title: Aircraft Optimization Algorithams

@author: Brunel
"""

import math as M
#import numpy as np
#import matplotlib.pylab as plt

"""
Plane Parameters (Change This)
"""

AR = 4.48                #Aspect Ratio
SweepLE = 0             #Leading Edge Sweep [deg]
TR = 1                #Taper Ratio
S = 12              #Lifting Surface Area [ft^2] Error under 9
b = 54/12                   # Wingspan [ft]
Wto = 11                #Takeoff Weight [lb]
PropThrust = 4.48      #Propeller Thrust [lbf]


"""
Required Functions for Solution
"""

def sweep(SweepLE,TR,AR):
	return M.atan(M.tan(SweepLE)-((1-TR)/AR*(1+TR)))

def cl3d(SweepQuarter,Cl2d):
	return 0.9*Cl2d*M.cos(SweepQuarter)

def clto(Cl3d):
	return Cl3d*0.8

def vto(Wto,S,RhoTO,Clmaxto):
	return ((2*Wto)/(S*RhoTO*Clmaxto))**0.5

def sexp(S,Sfuselage):
	return S - Sfuselage

#Mean Aerodynamic Chord ?
def cm(S,b):					# b is wingspan
	return S/b

def cdo(Cfe,S,Sexposed):
	return Cfe*(Sexposed/S)

def k(AReff,e):
	return 1/(M.pi*AReff*e)

def cdi(K,Clmin):
	return K*(Clmin**2)

def cdto(CDo,CDi):
	return CDo + CDi

def lto(RhoTO,S,Clmin,Vto):
	return 0.5*RhoTO*S*Clmin*(0.7*Vto)**2

def dto1(RhoTO,S,CDto,Vto):
	return 0.5*RhoTO*S*CDto*(0.7*Vto)**2

def amean(G,Wto,PropThrust,Dto,Fc,Lto):
	return (G/Wto)*(PropThrust-Dto-Fc*(Wto-Lto))

def sg(Vto,Amean):
	return (0.7*(Vto**2))/(2*Amean)

def vclimb(PropThrust,Dto,Wto,Vto):
	return ((PropThrust - Dto)/Wto)*Vto

def mach(Vto):
	return (Vto)/1126

def beta2(Mach):
	return 1-(Mach**2)

def calalfa(AReff,Beta2,AirfoilE,SweepMaxt,Sexposed,S,F):
	return ((2*M.pi*(AReff))/(2+((4 +(((AReff)**2*Beta2)/AirfoilE**2)*(1 +(M.tan(SweepMaxt)**2/Beta2)))**0.5)))*(Sexposed/S)*F

def clcruise(CLalfa,AoA):
	return CLalfa*AoA

def vcruise(RhoCruise,CLcruise,Wto,S):
	return ((2/(RhoCruise*CLcruise))*(Wto/S))**0.5

def tr(G,LoadF,Vcruise):
	return ((G*((LoadF**2)-1)**0.5)/Vcruise)*57.3

"""
Processing Steps
"""

#flight parameters
RhoTO = 0.00227
RhoCruise = 0.002176
G = 32.2

#Airplane Parameter
Cfe = 0.0055
Fc = 0.03

#Surface Area of fuselage only obtained through XFLR5 [ft^2]
Sfuselage = 10.4
Cl2d = 1.68
SweepMaxt = 0
AoA = 10
AReff = 1.2*AR
SweepQuarter = sweep(SweepLE,TR,AR)
Cl3d = cl3d(SweepQuarter,Cl2d)
Clmaxto = clto(Cl3d)
Clmin = 0.5368

#Take off Velocity
Vto = vto(Wto,S,RhoTO,Clmaxto)

#Exposed Surface
Sexposed = sexp(S,Sfuselage)
Cmac = cm(S,b)

#Calculation of Take Off Drag Coeff
e = 1.78*(1-(0.045*(AR**0.68)))-0.64
K = k(AReff,e)
CDo = cdo(Cfe,S,Sexposed)
CDi = cdi(K,Clmin)
CDto = cdto(CDo,CDi)

#Calculation of Mean Take off Acceleration
Lto = lto(RhoTO,S,Clmin,Vto)
Dto = dto1(RhoTO,S,CDto,Vto)
Amean = amean(G,Wto,PropThrust,Dto,Fc,Lto)

#Calculation of Take Off Distance
SG = sg(Vto,Amean)

# Climb Rate
VClimb = vclimb(PropThrust,Dto,Wto,Vto)

#Calculation of Wing Lift Slope & Cruise Lift Coefficient
Mach = mach(Vto)
Beta2 = beta2(Mach)
F = 0.98
AirfoilE = 0.95 # based on Raymer
CLalfa = calalfa(AReff,Beta2,AirfoilE,SweepMaxt,Sexposed,S,F)
CLcruise = clcruise(CLalfa,AoA)

#Claculation of Cruise Velocity, Thrust & Lift

print(Wto),
print(RhoCruise),
print(CLalfa)

Vcruise = vcruise(Wto,RhoCruise,CLcruise,S)

#Turn Rate
LoadF = 1.3 #Assume a load factor based on Raymers
TurnRate = tr(G,LoadF,Vcruise)

"""
Output
"""

#print("Takeoff Velocity [ft/s]:\t"),
print(Vto)
#print("Lift Force at Takeoff [lbf]:\t"),
print(Lto)
#print("Takeoff Drag [lbf]:\t\t"),
print(Dto)
#print("Mean Acceleration [ft/s^2]:\t"),
print(Amean)
#print("Takeoff Distance [ft]:\t\t"),
print(SG)
#print("Climb Velocity [ft/s]:\t\t"),
print(VClimb)
#print("Coeff of Lift at Cruise [lbf]:\t"),
print(CLcruise)
#print("Velocity at Cruise [ft/s]:\t"),
print(Vcruise)
#print("Turn Rate [deg/s]:\t\t"),
print(TurnRate)
#print("Exposed Surface Area [ft^2]:\t"),
print(Sexposed)


"""
End
"""