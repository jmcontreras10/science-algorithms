#   Author: jmcontreras10
#   Using concepts learned in IBIO2240: scientific programming 

import numpy as np
import matplotlib.pyplot as plt
import sys

from GaussJordan import gaussJordanSolve

##
#   Gives the values to build the linear regression ecuation
#   Inputs:
#       xVals: Values of X Axis
#       yVals: values of Y Axis
def getLinealRegretionValues(xVals, yVals):
    #   It calculates the mean of X and Y
    xMean = np.mean(xVals)
    yMean = np.mean(yVals)
    #   It creates the A matrix
    A = np.array([[1, xMean],[xMean, np.mean(xVals ** 2)]])
    #   It creates the b Vector
    b = np.array([[yMean],[np.mean(xVals*yVals)]])
    #   It calculates using gaussJordan
    x = gaussJordanSolve(A,b)

    return({
        'C0':x[0],
        'C1':x[1]
    })


#   Test
if len(sys.argv) > 1:
    if sys.argv[1] == '-t':
        #   Getting random points
        xVals = np.linspace(0,100,15)
        yVals = np.random.uniform(100,150,15)
        print(xVals,yVals)
        #   Plotting the points
        plt.figure()
        plt.plot(xVals, yVals, '-s')
        #   Getting the line of reg
        vals = getLinealRegretionValues(xVals,yVals)
        yLine = vals['C1'] * xVals + vals['C0']
        #   Plotting line
        plt.plot(xVals,yLine,'-or')
        plt.grid(1)
        plt.show()