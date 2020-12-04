#   Author: jmcontreras10
#   Using concepts learned in IBIO2240: scientific programming 

import numpy as np
import matplotlib.pyplot as plt
import sys

##
#   It defines a function that calculates euler values back
#   Inputs: 
#       F:  Function
#       h:  step
#       Yo: Initial Y
#       T0: Initial time
#       Tf: Final time
def EulerToBack(F, h, T0, Tf, Y0):
    #   Calculating all numbers in the result - dependent variable
    T = np.arange(T0, Tf + h,h)
    #   Independent variable
    YEulerBack = np.zeros(len(T))
    #   Initial Y
    YEulerBack[0] = Y0
    #   Iteration
    for iter in range(1,len(T)):
        #   Using the formula y(t) = h*F(t0,y0) + y(t0)
        YEulerBack[iter] = F(T[iter], YEulerBack[iter-1], h)
    #   It returns (X,Y)Value tuples to graph
    return T, YEulerBack

##
#   It defines a function that calculates euler values front
#   Inputs: 
#       F:  Function
#       h:  step
#       Yo: Initial Y
#       T0: Initial time
#       Tf: Final time
def EulerToFront(F, h, T0, Tf, Y0):
    #   Calculating all numbers in the result - dependent variable
    T = np.arange(T0, Tf + h,h)
    #   Independent variable
    YEulerFor = np.zeros(len(T))
    #   Initial Y
    YEulerFor[0] = Y0
    #   Iteration
    for iter in range(1,len(T)):
        #   Using the formula y(t) = h*F(t0,y0) + y(t0)
        YEulerFor[iter] = YEulerFor[iter -1 ] + h * F(T[iter-1],YEulerFor[iter -1 ])
    #   It returns (X,Y)Value tuples to graph
    return T, YEulerFor


##
#   It defines a function that calculates euler values Modificated
#   Inputs: 
#       F:  Function Mod
#       F1: Function
#       h:  step
#       Yo: Initial Y
#       T0: Initial time
#       Tf: Final time
def EulerToMod(F,F1, h, T0, Tf, Y0):
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
#   It defines a function that calculates euler values RK2
#   Inputs: 
#       F:  Function
#       h:  step
#       Yo: Initial Y
#       T0: Initial time
#       Tf: Final time
def EulerToRK2(F, h, T0, Tf, Y0):
    #   Calculating all numbers in the result - dependent variable
    T = np.arange(T0, Tf + h,h)
    #   Independent variable
    YEulerRK2 = np.zeros(len(T))
    #   Initial Y
    YEulerRK2[0] = Y0
    #   Iteration
    for iter in range(1,len(T)):
        #   Using the formula
        k1 = F(T[iter-1], YEulerRK2[iter-1])
        k2 = F(T[iter-1] + h , YEulerRK2[iter - 1] + k1 * h)
        YEulerRK2[iter] = YEulerRK2[iter - 1] + (h / 2.0) * (k1 + k2)
    #   It returns (X,Y)Value tuples to graph
    return T, YEulerRK2

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
        
    if sys.argv[1] == '-t':
        #   It defines the function
        Fb = lambda t,y,h: y / (1 - h*(0.49 - ((0.00245*np.exp(0.49*t))/(0.49+0.005*(np.exp(0.49*t)-1)))))
        Ff = lambda t,y: (0.49 - ((0.00245*np.exp(0.49*t))/(0.49+0.005*(np.exp(0.49*t)-1)))) * y
        Fm = lambda t,h: (1 - (h / 2.0) * (0.49 - ((0.00245*np.exp(0.49*t))/(0.49+0.005*(np.exp(0.49*t)-1)))))
        
        #   It defines an h value
        h = 0.01
        #   It defines Yi, Ti and Tf
        Y0 = 0.01
        T0 = 0.0
        Tf = 30.0
        
        T, YEulerBack = EulerToBack(Fb, h, T0, Tf, Y0)
        T, YEulerFor = EulerToFront(Ff, h, T0, Tf, Y0)
        T, YEulerMod = EulerToMod(Fm,Ff, h, T0, Tf, Y0)
        T, YRK2 = EulerToRK2(Ff, h, T0, Tf, Y0)
            
        plt.figure()
    
        plt.plot(T,YAnalitic(T),'b')
        plt.plot(T,YEulerBack,'r')
        plt.plot(T,YEulerFor,'g')
        plt.plot(T,YEulerMod,'m')
        plt.plot(T,YRK2,'orange')
        plt.xlabel('t',fontsize=15)
        plt.ylabel('y(t)',fontsize=15)
        plt.legend(['Analitic','EulerBack','EulerFor','EulerMod','EulerRK2'],fontsize=12)
        plt.grid(1)
        plt.show()
            

        
        