#   Author: jmcontreras10
#   Using concepts learned in IBIO2240: scientific programming 

from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interpol
import sys


if len(sys.argv) > 1:
    if sys.argv[1] == '-t1':
        #   It defines the (X,Y) Known points
        Xi = np.array([13,16,17,23])
        Yi = np.array([30,92,21,159])
        f1Nat = interpol.CubicSpline(Xi, Yi, bc_type='natural')
        f1Nak = interpol.CubicSpline(Xi, Yi, bc_type='not-a-knot')
        f1Clam = interpol.CubicSpline(Xi, Yi, bc_type='clamped')
        
        Xp = np.arange(Xi[0],Xi[-1]-0.001,0.001)
        
        plt.figure()
        plt.plot(Xi, Yi, 'or')
        plt.plot(Xi, Yi, '--',color='0.5')
        plt.plot(Xp, f1Nat(Xp), '--b')
        plt.plot(Xp,f1Nak(Xp),'--m')
        plt.plot(Xp,f1Clam(Xp),'--g')
        plt.xlim([10.0,25.0])
        plt.ylim([-200.0,180.0])
        plt.grid(1)
        plt.show()
        
    if sys.argv[1] == '-t2':
        print('Nothing to show')