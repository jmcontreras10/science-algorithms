#   Author: jmcontreras10
#   Using concepts learned in IBIO2240: scientific programming 

from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
import sys

##
#   It defines a function that finds the Ci coeficients using the 
#   Inputs: 
#       X,Y values
def CoefValues(Xi, Yi):
    #   It defines the matrix size
    N = np.size(Xi)
    #   It defines the Matrix
    A = np.zeros([N,N])
    #   It defines the b Vector
    b = np.zeros([N,1])
    #   It iterates over the matrix
    for i in range(N):
        for j in range(N):
            #   It fill the correspond value in the Matrix
            #   Using Xi[i]**(N - j -1)
            A[i, j] = Xi[i]**(N - j -1)
        b[i] = Yi[i]
    #   It solves the System
    Ci = np.linalg.solve(A,b)
    return Ci

##
#   It defines a function that finds the nre points having in mind the finded coeficients
#   Inputs: 
#       Cin: Coeficients
#       Xin: The points to find the Yis
def YkValues(Cin, Xin):
    N = np.size(Cin)
    M = np.size(Xin)
    Yout = np.zeros(M)
    for i in range(M):
        for j in range(N):
            Yout[i] += (Cin[j]*(Xin[i]**(N-j-1)))
    return Yout


if len(sys.argv) > 1:
    if sys.argv[1] == '-t1':
        #   It defines the (X,Y) Known points
        Xi = np.array([13,16,17,23,28,33])
        Yi = np.array([30,92,21,159,94,236])
        
        Cis = CoefValues(Xi, Yi)
        
        X = np.arange(Xi[0],Xi[-1],0.01)
        Y = YkValues(Cis, X)
        
        plt.figure()
        plt.plot(Xi, Yi, 'or')
        plt.plot(Xi, Yi, '--',color='0.5')
        plt.plot(X,Y,'b')
        plt.xlim([0.0,37.0])
        plt.grid(1)
        plt.show()
        
    if sys.argv[1] == '-t2':
        #   It defines the (X,Y) original Known points
        Xi = np.array([13,16,17,23,28,33])
        Yi = np.array([30,92,21,159,94,236])
        
        #   It defines the (X) new points
        Xk = np.array([15,19,21,25,27,32])
        
        Cis = CoefValues(Xi, Yi)
        
        X = np.arange(Xi[0],Xi[-1],0.01)
        Y = YkValues(Cis, X)
        
        Yk = YkValues(Cis, Xk)
        
        plt.figure()
        plt.plot(Xi, Yi, 'or')
        plt.plot(Xi, Yi, '--',color='0.5')
        plt.plot(Xk, Yk, 'sg')
        plt.plot(X,Y,'b')
        plt.xlim([0.0,37.0])
        plt.grid(1)
        plt.show()