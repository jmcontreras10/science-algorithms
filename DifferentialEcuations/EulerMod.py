#   Author: jmcontreras10
#   Using concepts learned in IBIO2240: scientific programming 

import numpy as np
import matplotlib.pyplot as plt
import sys

##
#   It defines a function that calculates euler values
#   Inputs: 
#       F:  Function
#       h:  step
#       Yo: Initial Y
#       T0: Initial time
#       Tf: Final time
def EulerTo(F,F1, h, T0, Tf, Y0):
    #   Calculating all numbers in the result - dependent variable
    T = np.arange(T0, Tf + h,h)
    #   Independent variable
    YEulerMod = np.zeros(len(T))
    #   Initial Y
    YEulerMod[0] = Y0
    #   Iteration
    for iter in range(1,len(T)):
        #   Using the formula y(t) = h*F(t0,y0) + y(t0)
        YEulerMod[iter] = (YEulerMod[iter -1 ] + (h/2.0)*F1(T[iter-1],YEulerMod[iter-1]))/F(T[iter],h)
    #   It returns (X,Y)Value tuples to graph
    return T, YEulerMod

##
#   It evaluates the analytic solution using the formula and values
#   Inputs: 
#       t:  Current Time
def YAnalitic(t):
    #   Params for analytic solve
    a = 0.5
    b = 0.01
    So = 0.99
    Io = 1 - So
    N = So + Io
    return ((a*N-b)*Io*np.exp((a*N-b)*t))/((a*N-b)+a*Io*(np.exp((a*N-b)*t)-1))

if len(sys.argv) > 1:
    if sys.argv[1] == '-t1':
        #   It defines the function
        F = lambda t,h: (1 - (h / 2.0) * (0.49 - ((0.00245*np.exp(0.49*t))/(0.49+0.005*(np.exp(0.49*t)-1)))))
        Ff = lambda t,y: (0.49 - ((0.00245*np.exp(0.49*t))/(0.49+0.005*(np.exp(0.49*t)-1)))) * y
        
        #   It defines an h value - Step
        h = 0.01
        #   Initial quantity of Y
        Y0 = 0.01
        #   Initial Time
        T0 = 0.0
        #   Final Time
        Tf = 30.0
        
        T, YEulerFor = EulerTo(F,Ff, h, T0, Tf, Y0)
        
        plt.figure()
        
        plt.plot(T,YEulerFor,'r')
        plt.xlabel('t',fontsize=15)
        plt.ylabel('y(t)',fontsize=15)
        plt.grid(1)
        plt.show()
        
    if sys.argv[1] == '-t2':
        #   It defines the function
        F = lambda t,h: (1 - (h / 2.0) * (0.49 - ((0.00245*np.exp(0.49*t))/(0.49+0.005*(np.exp(0.49*t)-1)))))
        Ff = lambda t,y: (0.49 - ((0.00245*np.exp(0.49*t))/(0.49+0.005*(np.exp(0.49*t)-1)))) * y
        
        #   It defines an h value
        h = 0.01
        #   It defines Yi, Ti and Tf
        Y0 = 0.01
        T0 = 0.0
        Tf = 30.0
        
        T, YEulerMod = EulerTo(F,Ff, h, T0, Tf, Y0)
            
        plt.figure()
    
        plt.plot(T,YAnalitic(T),'b')
        plt.plot(T,YEulerMod,'r')
        plt.xlabel('t',fontsize=15)
        plt.ylabel('y(t)',fontsize=15)
        plt.legend(['Analitic','EulerMod'],fontsize=12)
        plt.grid(1)
        plt.show()
            

        
        