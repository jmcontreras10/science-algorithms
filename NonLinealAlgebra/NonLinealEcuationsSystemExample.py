#   Author: jmcontreras10
#   Using concepts learned in IBIO2240: scientific programming 

#   This Excercice is Wrong!!

from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
import sys


##
#   Gives the values to build the linear regression ecuation
#   Inputs:
def alculateRoots2x2(x1i0, x2i0, A, f1, f2, TolX, TolY):
    #   It defines the number of iterations
    x1 = 0
    x2 = 0
    iter = 0
    while 1:
        #   Lets sum in iters
        iter += 1
        #   set the b Vector
        b = np.zeros([2,1])
        b[0] = -f1(x1i0, x2i0)
        b[1] = -f2(x1i0, x2i0)
        #   It calculates the DeltaX
        #   Using Gauss-Jordan
        delta_X = np.linalg.solve(A, b)
        #   It calculates the root x**i = x**(i-1) + Delta_X
        x1 = np.float(x1i0 + delta_X[0])
        x2 = np.float(x2i0 + delta_X[1])
        #   Evaluates the criteriums
        if np.abs(x1 - x1i0) <= TolX and np.abs(x2 - x2i0) <= TolX:
            break
        if np.abs(f1(x1,x2)) <= TolY and np.abs(f2(x1,x2)) <= TolY:
            break
        #   It updates x1i0 and x2i0
        x1i0 = x1
        x2i0 = x2
        
    print('Root x1: ',x1)
    print('Root x2: ',x2)
    print('Number of Iters: ',iter)


#   Test
if len(sys.argv) > 1:
    if sys.argv[1] == '-t':
        #   It defines the function f1
        f1 = lambda x1, x2: x1**2+x2-3
        
        #   It defines the function f2
        f2 = lambda x1, x2: (x1-2)**2+(x2+3)**2-4
        
        #   Let's plot to look for two good points
        delta = 0.1
        #   x1
        x1 = np.arange(-5.0,5.0,delta)
        #   x2
        x2 = np.arange(-5.0,5.0,delta)
        
        #   It gets the combination matrix of all elements
        X1, X2 = np.meshgrid(x1, x2)
        
        plt.figure()
        #   Plot UwU
        plt.subplot(2,1,1)
        
        C1 = plt.contour(X1, X2, f1(X1,X2),colors = 'b')
        plt.clabel(C1, fontsize=10)
        
        
        C2 = plt.contour(X1, X2, f2(X1,X2),colors = 'r')
        plt.clabel(C2, fontsize=10)
        
        plt.xlabel('x1')
        plt.ylabel('x2')
        
        plt.subplot(2,1,2)
        
        C1 = plt.contour(X1, X2, f1(X1,X2),[0.0], colors = 'b')
        plt.clabel(C1, fontsize=10)
        
        
        C2 = plt.contour(X1, X2, f2(X1,X2),[0.0], colors = 'r')
        plt.clabel(C2, fontsize=10)
        
        plt.xlabel('x1')
        plt.ylabel('x2')
        plt.show()
        
        #   Now it defines Jacobian Matrix
        def Jaco(x1,x2):
            A = np.zeros([2,2])
            A[0,0] = 2.0*x1
            A[0,1] = 1.0
            A[1,0] = 2*(x1-2)
            A[1,1] = 2*(x2+3)
            return A
        
        #   It defines the initial points
        x1i0 = 1.8
        x2i0 = -1.5
        #   It defines the tolerance values
        TolX = 10**-5
        TolY = 10**-10

        alculateRoots2x2(x1i0,x2i0, Jaco(x1i0, x2i0), f1, f2, TolX, TolY)

