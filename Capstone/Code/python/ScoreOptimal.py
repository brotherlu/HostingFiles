# -*- coding: utf-8 -*-
"""
Created on Thuf Sep 20 12:09:49 2012

@author: quade7
"""

"""
KEY
-----

WS      Written Report Score
TFS     Total Flight Score
RAC     Rated Aircraft Cost
SF      Size Factor

EWn     Empty Weight n-th Flight
XMAX    Longest possible dimension in direction of flight
YMAX    Longest possible dimension in Normal to direction of flight

"""


import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm

def FinalScore(WS,TFS,RAC):
    return WS * TFS / RAC

def TFS(M):
    Sum=0
    for val in M:
        Sum+=val
    return Sum

def RAC(EW,SF):
    return math.sqrt(EW * SF) / 10

def EW(EWn):
    Max=EWn[0]
    for val in EWn:
        Max = val if (Max < val) else Max
    return Max

def SizeFactor(XMAX,YMAX):
    return XMAX + 2 * YMAX

"""
Mission Scoreing

Mn      Mission-n Score

NOTE: MUST HAVE SUCCESSFUL LANDING TO GET SCORE
"""

"""
Mission 1 Short Take-off
"""

def M1(Laps,MaxLaps):
    return 2 * ( Laps / MaxLaps )

"""
Mission 2 Stealth Mission
"""

def M2(Store,MaxStore):
    return 4 * ( Store / MaxStore )

"""
Mission 3 Strike Mission
"""

def M3( FastestTime,TeamTime ):
    return 6 * ( FastestTime / TeamTime )

#"""
#Score Solver
#"""
#
#def Score():
#    SCORE=0
#    global MissionScores, EmptyWeight, WrittenPoints, XMAX, YMAX
#    print "Size Factor :", SizeFactor( XMAX , YMAX )
#    print "Empty Weight :",  EW( EmptyWeight )
#    print "RAC :", RAC( EW( EmptyWeight ), SizeFactor( XMAX , YMAX ) )
#    print "Total Flight Score: ",TFS( MissionScores )
#
#    SCORE = FinalScore( WrittenPoints, TFS( MissionScores ),RAC( EW( EmptyWeight ), SizeFactor( XMAX , YMAX ) ) )
#
#    print "Score Achieved: ", SCORE
#
#    return SCORE

"""
Value Definations
"""

fig = plt.figure()
ax = Axes3D(fig)

"""
Mission One
"""

#t = np.r_[40:100:200j]      #Speed rangeing from 40 to 90 ft/s
#u=[]                       # Empty array to hold the new values
#v = np.r_[2:6:200j]         #Number of laps aimed
#for i in t:
#    u.append(i*240/3800.)      #loop to calculate the speed
#
#a = np.zeros((len(u),v.size))  #empty loop to hold the scores
#
#for i in np.arange(len(u)):
#    for j in np.arange(v.size):
#        val = M1(u[i],v[j])
#        a[j,i] = val if val <=2 else 2
#
#t,u = np.meshgrid(t,u)         #Create a Meshgrid for the x,y plane
#
##Plot the surface
#ax.plot_surface(t,u,a,alpha=0.5,cmap=cm.jet)
#
##Plot the contours if desired
##ax.contour(t,u,a,zdir='x',offset=100) #plot the X contour
##ax.contour(t,u,a,zdir='y',offset=2)   #plot the y contour
#
##Set the x,y,z limits
#ax.set_xlim(40,100)
#ax.set_ylim(2,7)
#ax.set_zlim(0,2)
#
##Create the axis labels
#ax.set_xlabel("Speed ft/s")
#ax.set_ylabel("Laps Completed")
#ax.set_zlabel("Mission Score")

"""
Mission Two
"""

#Weight of Mini-Max is 1.3oz or 37grams

WE = np.r_[1:10:200j]
WP = np.r_[1:10:200j]

a = np.zeros((WE.size,WP.size))

for i in np.arange(WE.size):
    for j in np.arange(WP.size):
        val = M2(WE[i],WP[j])
        a[j,i] = val if val <=4 else 4

WE,WP = np.meshgrid(WE,WP)

ax.plot_surface(WE,WP,a,alpha=.5,cmap=cm.jet)
ax.contour(WE,WP,a,zdir='x',offset=10)
ax.contour(WE,WP,a,zdir='y',offset=10)
#ax.contour(WE,WP,a,zdir='z',offset=0)

ax.set_xlim(0,10)
ax.set_ylim(0,10)
ax.set_zlim(0,4)

ax.set_xlabel("Stored Rockets")
ax.set_ylabel("Max Stored Rockets")
ax.set_zlabel("Mission Score")

"""
Mission Three
"""
#
#mTime=np.r_[1:600:200j]
#aTime=np.r_[1:600:200j]
#
#a = np.zeros((mTime.size,aTime.size))
#
#for i in np.arange(mTime.size):
#    for j in np.arange(aTime.size):
#        val = M3(mTime[i],aTime[j])
#        a[j,i] = val if val <=6 else 6
#
#mTime,aTime = np.meshgrid(mTime,aTime)
#
#ax.plot_surface(mTime,aTime,a,alpha=.5,cmap=cm.jet)
#ax.contour(mTime,aTime,a,zdir='x',offset=600)
#ax.contour(mTime,aTime,a,zdir='y',offset=600)
##ax.contour(mTime,aTime,a,zdir='z',offset=10)
#
#ax.set_xlabel("Flight Time (s)")
#ax.set_ylabel("Best Flight Time (s)")
#ax.set_zlabel("Mission Score")
#
#ax.set_xlim(0,600)
#ax.set_ylim(0,600)
#ax.set_zlim(0,6)

"""
Total score Plots
"""

#EW = np.r_[2:15:200j]
#SF = np.r_[5:30:200j]
#
#Z = np.zeros((EW.size,SF.size))
#
#for i in np.arange(EW.size):
#    for j in np.arange(SF.size):
#        val = 6 / RAC(EW[i],SF[j])
#        Z[i,j] = val
#
#EW,SF = np.meshgrid(EW,SF)
#
#ax.plot_surface(EW,SF,Z,cmap=cm.jet,alpha=0.5)
#
#ax.contour(EW,SF,Z,zdir='x',offset=0)
#ax.contour(EW,SF,Z,zdir='y',offset=0)
#
#ax.set_xlabel("Empty Weight (lbs)")
#ax.set_ylabel("Size Factor (ft)")
#ax.set_zlabel("Total Score")
#
#ax.set_xlim(0,15)
#ax.set_ylim(0,30)

"""
Display the plot
"""

ax.view_init(30,-155) # set the viewing angle for the 3D plot

plt.show()          # Display the plot