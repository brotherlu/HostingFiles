"""
Hermite Curve Generator
"""
def hermite(xi,mi,xf,mf,t):
    h1 = 2*t**3 - 3*t**2 + 1
    h2 = t**3 - 2*t**2 + t
    h3 = -2*t**3 + 3*t**2
    h4 = t**3 - t**2
    return h1*xi+h2*mi+h3*xf+h4*mf

"""
360 Degree Wrapper
"""
def wrap360(angle):
	if angle > 36000 : -=36000
	if angle < 0 : +=36000
	return angle

"""
BankLeft 90 Subroutine
"""

def BankLeft90(length="Short"):
	currentHeading = cs.yaw
	while wrap360(cs.yaw) != wrap360(currentHeading-90):
		Script.SendRC(1,1200,True)

	Script.SendRC(1,Script.GetParam('RC1_TRIM'),True)

#for distance 

	if length=="NoDelay" : return True
	if length=="Short" : Script.Sleep(5000)
	if length=="Long" : Script.Sleep(10000)

	return True

"""
Nudge Control Surface Subroutine
"""
def NudgeCS(channel=3,direction=1):

	CH=[0,cs.ch1out,cs.ch2out,cs.ch3out,cs.ch4out]

	Script.SendRC(2,CH[channel]+(direction*100),True)
	Script.Sleep(200)
	Script.SendRC(2,CH[channel]+(-1*direction*100),True)

	return True

"""
Takeoff Subroutine
"""
# Save current State
RunwayBearing=cs.yaw
HomeLoc=[cs.lat,cs.lng,cs.alt]

#go through Throttle steps
SpeedSteps=[1000,1200,1400,1600,1800,2000]

for i in SpeedSteps:
	Script.SendRC(3,i,True)
	Script.Sleep(300)

Script.SendRC(2,Script.GetParam("RC2_TRIM")+300,True)

Script.ChangeMode(Stablizie) # Handoff to next Phase

"""
Waypoint Subroutine
"""

Script.ChangeMode(AUTO)

BankLeft90("Short") # first left bank
BankLeft90("Short") # second left bank
BankLeft90("Short") # third left bank
BankLeft90("Long") # fourth left bank

BankLeft90("Short") # third left bank
BankLeft90("Long") # second left bank
BankLeft90("Short") # third left bank
BankLeft90("Long") # fourth left bank

BankLeft90("Short") # first left bank
BankLeft90("Long") # second left bank
BankLeft90("Short") # third left bank
BankLeft90("NoDelay") # Just bank and release

Script.ChangeMode(Stablizie) # Handoff to next Phase

"""
AutoLanding Subroutine
"""

Script.SendRC(3,Script.GetParam("RC3_MIN"),True) #Throttle to minimum

# Now gliding

NudgeCS(2,-1)
Script.Sleep(500)
NudgeCS(2,-1)
Script.Sleep(500)
NudgeCS(2,-1)
Script.Sleep(500)
