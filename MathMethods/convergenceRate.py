#   Author: jmcontreras10
#   Using concepts learned in IBIO2240: scientific programming 

import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
import sys


##
#   Calculates convergence of bisection method
#   Inputs:
#       fx: Function to find root
#       root: Root to find a solution
#       x0: x0 point
#       x1: x1 point
def convergenceRateBisection(fx, val, x0, x1):
    #   It defines the tolerances
    Tx = 10**-5
    Tf = Tx
    #   It defines the final root
    root = x1
    #   It iterates while true :V
    iter = 0
    #   It will stores the iterations root as its appears
    xr_iter = np.array([])
    while 1:
        #   It sums one iteration
        iter += 1
        #   It calculates the current root using:
        x2 = (x0 + x1)/2.0
        #   Add the root to the array
        xr_iter = np.append(xr_iter, x2)
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
        
    return root, iter, xr_iter

#   Test
if len(sys.argv) > 1:
    if sys.argv[1] == '-t':
        #   Here it test the algorithm
        fx = lambda x: -(np.sqrt(3.0*x)**(2.0/5.0)) + (x**3.0)*np.cos(3.0*x)+4.0*(x**2)-7
        
        print('Using the Bisection method:')
        val = 0
        x0 = 1.0
        x1 = 2.0
        root, iter, xr_iter = convergenceRateBisection(fx, val, x0, x1)
        print(xr_iter)
        print('The root is {:.5f}, and it was using {:d} iterations.'.format(root,iter))
        #   It calculates the 'true' root value
        xroot_true = opt.fsolve(fx, x1)
        #   It calculates the error stimation in each iteration
        eps_array = np.abs(xr_iter - xroot_true)
        #   For each iteration, it calculates the convergence rate
        r_array = (np.log10(eps_array[1:np.size(eps_array) - 1]/
                            eps_array[2:np.size(eps_array)])/
                   np.log10(eps_array[0:np.size(eps_array) - 2]/
                            eps_array[1:np.size(eps_array) - 1]))
        #   Rate
        print(r_array[-2:])
        #   Arange
        iter_array = np.arange(1.0, np.size(r_array) + 1)
        #   Let's plot
        plt.figure()
        plt.plot(iter_array, r_array)
        plt.plot(iter_array, r_array, 'or')
        plt.grid(1)
        
        plt.show()