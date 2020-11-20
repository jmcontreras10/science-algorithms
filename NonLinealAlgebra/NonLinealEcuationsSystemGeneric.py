#   Author: jmcontreras10
#   Using concepts learned in IBIO2240: scientific programming 

from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
import sys

def set_numpy_decimal_places(places, width=0):
    set_np = '{0:' + str(width) + '.' + str(places) + 'f}'
    np.set_printoptions(formatter={'float': lambda x: set_np.format(x)})


##
#   Gives the values to build the linear regression ecuation
#   Inputs:
def calculateRoots(xi0, A, fs, TolX, TolY):
    xi0 = xi0.reshape((np.size(xi0),1))
    x = np.zeros([len(fs),1])
    #   It defines the number of iterations
    iter = 0
    while 1:
        #   Lets sum in iters
        iter += 1
        #   set the b Vector
        b = np.zeros([len(fs),1])
        
        for i in range(np.size(b)):
            b[i] = -fs[i](xi0)
        #   It calculates the DeltaX
        #   Using Gauss-Jordan
        delta_X = np.linalg.solve(A, b)
        #   It calculates the root x**i = x**(i-1) + Delta_X
        x = xi0 + delta_X
        #   Evaluates the criteriums
        ready = True
        for i in range(np.size(xi0)):
            if np.abs(x[i] - xi0[i]) > TolX:
                ready = False
        if ready:
            break
            
        ready = True
        for i in range(np.size(xi0)):
            if np.abs(fs[i](x)) > TolY:
                ready = False
        if ready:
            break
            
        #   It updates x
        xi0 = x
    set_numpy_decimal_places(16)
    print('Root x: ',x)
    print('Number of Iters: ',iter)


#   Test
if len(sys.argv) > 1:
    if sys.argv[1] == '-t':
        #   It defines the function f1
        f1 = lambda x: 3.0*np.exp(-(x[0]**2.0))-5.0*(x[1]**(1.0/3.0))+6.0
        
        #   It defines the function f2
        f2 = lambda x: 3.0*x[0]+0.5*(x[1]**(1.0/4.0))-15.0
        
        #   It defines the function in array
        fs = [f1,f2]
        
        #   Let's plot to look for two good points
        delta = 0.1
        #   x1
        x1 = np.arange(0.1,6.0,delta)
        #   x2
        x2 = np.arange(0.1,6.0,delta)
        
        #   It gets the combination matrix of all elements
        X1, X2 = np.meshgrid(x1, x2)
        
        plt.figure()
        #   Plot UwU
        plt.subplot(2,1,1)
        
        C1 = plt.contour(X1, X2, f1([X1,X2]),colors = 'b')
        plt.clabel(C1, fontsize=10)
        
        
        C2 = plt.contour(X1, X2, f2([X1,X2]),colors = 'r')
        plt.clabel(C2, fontsize=10)
        
        plt.xlabel('x1')
        plt.ylabel('x2')
        
        plt.subplot(2,1,2)
        
        C1 = plt.contour(X1, X2, f1([X1,X2]),[0.0], colors = 'b')
        plt.clabel(C1, fontsize=10)
        
        
        C2 = plt.contour(X1, X2, f2([X1,X2]),[0.0], colors = 'r')
        plt.clabel(C2, fontsize=10)
        
        plt.xlabel('x1')
        plt.ylabel('x2')
        plt.show()
        
        #   Now it defines Jacobian Matrix
        def Jaco(x):
            A = np.zeros([np.size(x),np.size(x)])
            A[0,0] = -6.0*x[0]*np.exp(-(x[0]**2.0))
            A[0,1] = (-5.0/3.0)*x[1]**(-2.0/3.0)
            A[1,0] = 3.0
            A[1,1] = (1.0/8.0)*(x[1]**(-3.0/4.0))
            return A
        
        #   It defines the initial points
        xi0 = np.array([[5.0],[2.0]])
        #   It defines the tolerance values
        TolX = 10.0**-5
        TolY = 10.0**-5

        calculateRoots(xi0, Jaco(xi0), fs, TolX, TolY)

