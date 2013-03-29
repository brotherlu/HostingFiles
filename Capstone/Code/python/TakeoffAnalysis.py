import math as M
import matplotlib.pylab as plt

"""
Function definitions
"""

def ToDist(Vto,a):
	return Vto**2/(2*a)	 

todist=[]									#Takeoff distance
chord=[]									#Chord length

# Define values 
rho=0.002378								#density (slugs/ft^3) 
g=32.20 									#gravity acceleration (ft/s^2) 
Fc=0.03 									#coefficient of rolling friction 
T=20										#static thrust (lb) 
z=1 										#height difference between wings (ft) 
Clmax=2.25 									#maximum lift coefficient 
Cf=0.0059
b1=8 										#wingspan first wing (ft) 
b2=8 										#wingspan second wing (ft) 
e1=.7 										#wing efficiency first wing (rect.) 
e2=.7 										#wing efficiency second wing (rect.) 
c1=0.5 										#Chord length first wing (ft) 
c2=0.5 										#Chord length second wing (ft) 
W=55 										#weight (pounds) 
alpha=0 									#angle of attack (degrees) 
alphamax=14

startdist=13.083-b1-8/12 					#distance between LE of forward wing and TE of aft wing 

# Begin While loop 
while (c1<=2.0):
    S1=b1*c1   							#Area (ft^2) first wing 
    S2=b2*c2 								#Area (ft^2) second wing 
    AR1=b1**2/S1								#aspect ratio first wing 
    AR2=b2**2/S2 							#aspect ratio second wing 
    y=startdist-c1-c2						#distance between TE of forward wing and LE of aft wing (ft) 
     
    # Solve for Fuselage Drag
    lF=49/12 									#length(ft) 
    dF=6*M.sqrt(2)/12 							#diameter (ft) 
    Swet=1300 									#Wetted area (ft^2) 
    FR=lF/dF 									#fineness ratio 
    FF=1+60/FR**3+.0025*FR 						#Fineness Factor 
    cdF=FF*Cf*Swet/(1440) 						#Drag coefficient due to fuselage 
     
    # Solve for Wing Drag 
    L=1.2
    R=1.05
    tc=.13 
    FF=(1+L*tc+100*tc**4)*R
    cdW=FF*Cf*4 								#Additional *2 for second wing 
     
    # Additional Drags and solve for Cdmin (taken from Nicolai paper) 
    cdLG=0.0042
    cdE=0.002
    cdVT=0.00039
    cdTB=0.00009 
    cdmin=cdTB+cdVT+cdE+cdLG+cdW+cdF 			#Minimum drag 
    
    # Solve for lift and drag coefficient of first wing 
    cla1=1.09+0.0933*alpha 						#coeff. of lift (infinite) 
    alpha_ind1=2*cla1/(M.pi*AR1)*(180/M.pi) 		#induced angle of attack 
    cdi1=2*cla1**2/(M.pi*e1*AR1) 					#induced drag coefficient 
    alpha_eff1=alpha-alpha_ind1 				#effective angle of attack 
    cl1=1.09+0.0933*alpha_eff1 					#coeff. of lift (finite) 
    cd1=2*cl1**2/(M.pi*e1*AR1) 					#coefficient of drag 
     
    # Solve for maximum lift on first wing 
    clamax1=1.09+0.0933*alphamax; 
    alphamax_ind1=2*clamax1/(M.pi*AR1)*(180/M.pi)
    alphamax_eff1=alphamax-alphamax_ind1
    clmax1=1.09+0.0933*alphamax_eff1
     
    # Solve for downwash angle on second wing 
    eps2=(cl1/(2*M.pi*AR1)*(((1+2*y/b1)/((1+2*y/b1)**2+(2*z/b1)**2))+((1-2*y/b1)**2)/((1-2*y/b1)**2+(2*z/b1)**2)))*180/M.pi
     
    # Solve for lift and drag on second wing (same analysis as first) 
    cla2=1.09+0.0933*alpha
    alpha_ind2=2*cla2/(M.pi*AR2)*(180/M.pi)
    cdi2=2*cla2**2/(M.pi*e2*AR2)
    alpha_eff2=alpha-eps2-alpha_ind2
    cl2=1.09+0.0933*alpha_eff2
    cd2=2*cl2**2/(M.pi*e2*AR2)
     
    # Solve for maximum lift on aft wing 
    clamax2=1.09+0.0933*alphamax
    alphamax_ind2=2*clamax2/(M.pi*AR2)*(180/M.pi)
    alphamax_eff2=alphamax-alphamax_ind2
    clmax2=1.09+0.0933*alphamax_eff2
     
    # Solve for Take-off Velocity 
    Vto=(2*W/((S1*clmax1+S2*clmax2)*0.8*rho))**.5
     
    # Solve for Mean Acceleration 
    D=0.5*(cd1+cdmin)*rho*(.7*Vto)**2*S1+0.5*(cd2+cdmin)*rho*(.7*Vto)**2*S2
    L=0.5*cl1*rho*(.7*Vto)**2*S2+0.5*cl2*rho*(.7*Vto)**2*S2
    a=(g/W)*(T-D-(Fc*(W-L)))
    	 
    # Increment chord lengths 
    c1=c1+0.01
    c2=c2+0.01
    
    todist.append(ToDist(Vto,a))
    chord.append(c1)
    #end while loop

Cmin = chord[todist.index(min(todist))]

Label = 'Minimum Point ('+str(Cmin)+','+str(min(todist))+')'

plt.plot(chord,todist)
plt.plot(Cmin,min(todist),'ok')
plt.annotate(Label,xy=(Cmin,min(todist)),xycoords='data',xytext=(-80,80),textcoords='offset points',arrowprops=dict(arrowstyle="->",
                                connectionstyle="arc3,rad=.2"))
plt.grid(True)
plt.title("Take-off Distance vs Chord length")
plt.xlabel("Chord Length (ft)")
plt.ylabel("Take-off Distance (ft)")

print(min(todist)),
print(","),
print(Cmin)

plt.show()