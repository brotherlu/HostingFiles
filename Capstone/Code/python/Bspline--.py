import numpy as np
import matplotlib.pyplot as plt

def bspline(U,dataPoints,order):
	bsplineBasis(u,dataPoints.size,order)



def bsplineBasis(u,numPoints,order):

	global knot
	global basisFunctions

	for j in range(order-1):
		for i in range(len(knot)-order-2):
			if j == 0:
				if knot[i] <= u and u <= knot[i+1]:
					basisFunctions[i][j]=1
				else:
					basisFunctions[i][j]=0
			else:
				temp1 = (( u - knot[i] ) / ( knot[i+j] - knot[i] )) * basisFunctions[i][j-1]
				temp2 = (( knot[i+j+1] - u ) / ( knot[i+j+1] - knot[i+1] )) * basisFunctions[i+1][j-1]
				basisFunctions[i][j] = temp1 + temp2


def bsplineKnot(numPoints,order):

	global knot

	for i in range(numPoints+order):
		if i < order:
			knot.append(0)
		elif i<=numPoints and i>=order:
			knot.append(i-order+1)
		elif i>numPoints:
			knot.append(numPoints-order+2)


#u=n-k+2


"""
Input for b-spline curve

points array, order k ... usually 4 for smooth curves
"""

order = 4
dataPoints=np.random.random_integers(500,600,10)
basisFunctions=np.zeros( (4,4) )
knot=[]

bsplineKnot(dataPoints.size,order)

print(len(knot))

for i in range(dataPoints.size-order+2):
	bsplineBasis(i,dataPoints.size,order)

print(knot)

print(dataPoints)

print(basisFunctions);
