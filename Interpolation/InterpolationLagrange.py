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
def LagrangeValues(Xi, Yi, Xk):
    #   Yks definition
    Yk = np.zeros(np.size(Xk))
    #   It iterates
    for k in range(np.size(Xk)):
        for i in range(np.size(Yi)):
            multaux = 1
            for j in range(np.size(Yi)):
                if i == j:
                    continue
                #   Mult
                multaux *= ((Xk[k] - Xi[j])/(Xi[i]-Xi[j]))
                
            #   SUM
            Yk[k] += Yi[i]*multaux
    return Yk


if len(sys.argv) > 1:
    if sys.argv[1] == '-t1':
        #   It defines the (X,Y) Known points
        Xi = np.array([13,16,17,23,28,33])
        Yi = np.array([30,92,21,159,94,236])
        
        #   It defines the (X) new points
        Xk = np.array([15,19,21,25,27,32])
        
        Yk = LagrangeValues(Xi, Yi, Xk)
        CiPoly = np.polyfit(Xi, Yi, np.size(Xi)-1)
        YkPoly = np.polyval(CiPoly, Xk)
        
        X = np.arange(Xi[0],Xi[-1],0.01)
        Y = LagrangeValues(Xi, Yi, X)
        
        plt.figure()
        plt.plot(Xi, Yi, 'or')
        plt.plot(Xi, Yi, '--',color='0.5')
        plt.plot(X,Y,'b')
        plt.plot(Xk, Yk, 'sg')
        plt.xlim([0.0,37.0])
        plt.grid(1)
        plt.show()
        
    if sys.argv[1] == '-t2':
        print('Nothing to show')