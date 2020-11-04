#   Author: jmcontreras10
#   Using concepts learned in IBIO2240: scientific programming 

import numpy as np
import matplotlib.pyplot as plt
import sys


##
#   Bisection Method find the solution root in which f(root) = val
#   Inputs:
#       fx: Function to find root
#       root: Root to find a solution
#       Tx: Tolerance in x
#       Tf: Tolerance in f
def bisectionMethod(fx, val, x0, x1):
    #   It defines the tolerances
    Tx = 10**-5
    Tf = Tx
    #   It defines the final root
    root = x1
    #   It iterates while true :V
    iter = 0
    while 1:
        #   It sums one iteration
        iter += 1
        #   It calculates the current root using:
        x2 = (x0 + x1)/2.0  
        
        #   It evaluates the tolernce criterium on x
        if np.abs(x2 - root) <= Tx:
            break
        #   It evaluates the tolernce criterium on y
        if np.abs(fx(x2)) <= Tf:
            break
        #   It updates the interval depending on current root result
        if fx(x2)*fx(x0) < 0:
            x1 = x2
        else:
            x0 = x2
        
        root = x2
        
    return root, iter


##
#   Fake Position Method find the solution root in which f(root) = val
#   Inputs:
#       fx: Function to find root
#       root: Root to find a solution
#       Tx: Tolerance in x
#       Tf: Tolerance in f
def fakePosMethod(fx, val, x0, x1):
    #   It defines the tolerances
    Tx = 10**-5
    Tf = Tx
    #   It defines the final root
    root = x1
    #   It iterates while true :V
    iter = 0
    while 1:
        #   It sums one iteration
        iter += 1
        #   It calculates the current root using:
        x2 = x1 - ((fx(x1)*(x1-x0))/(fx(x1)-fx(x0)))
        
        #   It evaluates the tolernce criterium on x
        if np.abs(x2 - root) <= Tx:
            break
        #   It evaluates the tolernce criterium on y
        if np.abs(fx(x2)) <= Tf:
            break
        #   It updates the interval depending on current root result
        if fx(x2)*fx(x0) < 0:
            x1 = x2
        else:
            x0 = x2
        
        root = x2
        
    return root, iter


##
#   Fixed Point Method find the solution root in which f(root) = val
#   Inputs:
#       fx: Function to find root
#       gx: Function to available
#       root: Root to find a solution
#       Tx: Tolerance in x
#       Tf: Tolerance in f
def fixedPointMethod(fx, gx, val, x0, x1):
    #   It defines the tolerances
    Tx = 10**-5
    Tf = Tx
    #   It defines the final root
    root = x1
    #   It iterates while true :V
    iter = 0
    while 1:
        #   It sums one iteration
        iter += 1
        #   It calculates the current root using:
        x2 = gx(x1)
        
        #   It evaluates the tolernce criterium on x
        if np.abs(x2 - root) <= Tx:
            break
        #   It evaluates the tolernce criterium on y
        if np.abs(fx(x2)) <= Tf:
            break
        #   It updates the intervals
        x1 = x2
        root = x2
        
    return root, iter


##
#   Newton Method find the solution root in which f(root) = val
#   Inputs:
#       fx: Function to find root
#       fdx: Derivative of function to find root 
#       root: Root to find a solution
#       Tx: Tolerance in x
#       Tf: Tolerance in f
def newtonMethod(fx, fdx, val, x0, x1):
    #   It defines the tolerances
    Tx = 10**-5
    Tf = Tx
    #   It defines the final root
    root = x1
    #   It iterates while true :V
    iter = 0
    while 1:
        #   It sums one iteration
        iter += 1
        #   It calculates the current root using:
        x2 = x1 - (fx(x1) / fdx(x1))    
        
        #   It evaluates the tolernce criterium on x
        if np.abs(x2 - root) <= Tx:
            break
        #   It evaluates the tolernce criterium on y
        if np.abs(fx(x2)) <= Tf:
            break
        #   It updates the intervals
        x1 = x2
        root = x2
        
    return root, iter


#   Test
if len(sys.argv) > 1:
    if sys.argv[1] == '-t':
        #   Here it test the algorithm
        fx = lambda x: -(np.sqrt(3.0*x)**(2.0/5.0)) + (x**3.0)*np.cos(3.0*x)+4.0*(x**2)-7
        #   Arrange of points
        x = np.arange(0.0,2.0,0.001)
        #   Let's plot
        plt.figure()
        plt.plot(x, fx(x), color='navy')
        plt.grid(1)
        
        print('Using the Bisection method:')
        val = 0
        x0 = 1.0
        x1 = 2.0
        root, iter = bisectionMethod(fx, val, x0, x1)
        print('The root is {:.5f}, and it was using {:d} iterations.'.format(root,iter))
        plt.plot(root, 0, 'ro')
        plt.annotate("Bisection", (root, 0))
        plt.grid(1)
        
        
        print('Using the Fake Pos method:')
        val = 0
        x0 = 1.0
        x1 = 2.0
        root, iter = fakePosMethod(fx, val, x0, x1)
        print('The root is {:.5f}, and it was using {:d} iterations.'.format(root,iter))
        plt.plot(root, 0, 'bo')
        plt.annotate("Fake pos", (root, 0))
        plt.grid(1)
        
        print('Using the fixed point method:')
        val = 0
        x0 = 1.0
        x1 = 2.0
        gx = lambda x: ((1.0/4.0)*(np.sqrt(3*x)**(2.0/5.0)-(x**3.0)*np.cos(3.0*x)+7))**0.5
        root, iter = fixedPointMethod(fx, gx, val, x0, x1)
        print('The root is {:.5f}, and it was using {:d} iterations.'.format(root,iter))
        plt.annotate("Fixed Point", (root, 0))
        plt.plot(root, 0, 'go')
        plt.grid(1)
        
        print('Using the Newton method:')
        val = 0
        x0 = 1.0
        x1 = 2.0
        fdx = lambda x: -((3.0**(1.0/5.0))/5.0)*(x**(-4.0/5.0))-3.0*(x**3.0)*np.sin(3.0*x)+3*(x**2)*np.cos(3*x)+8*x
        root, iter = newtonMethod(fx, fdx, val, x0, x1)
        print('The root is {:.5f}, and it was using {:d} iterations.'.format(root,iter))
        plt.annotate("Newton", (root, 0))
        plt.plot(root, 0, 'yo')
        plt.grid(1)
        
        
        plt.show()