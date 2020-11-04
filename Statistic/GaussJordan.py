#   Author: jmcontreras10
#   Using concepts learned in IBIO2240: scientific programming 

import numpy as np
import sys

##
#   Rows exchange function, excanging the pivot row position with the maximum row position (current column pivot)
def exchangeMax(Au, pivotPos,N):
    #   Find the max in the pivot's row
    max = np.abs(Au[pivotPos, pivotPos])   
    rowPos = pivotPos
    #   It titerates over the Au to find the max
    for i in range(pivotPos + 1,N):
        if np.abs(Au[i, pivotPos + 1]) > max:
            max = np.abs(Au[i, pivotPos + 1])
            rowPos = i
    #   It exchanges the rows if these are different
    if rowPos != pivotPos:
        aux = 1.0 * Au[rowPos, :]
        Au[rowPos, :] = 1.0 * Au[pivotPos, :]
        Au[pivotPos,:] = 1.0 * aux
    return Au

##
#   GaussJordan method solver of system of lineal ecuations
#   This algorithm implements the pivots strategy to avoid the zero pivots error
#   Inputs:
#       A: Variable Matrix [NxN]
#       b: Constants array [Nx1]
def gaussJordanSolve(A,b):
    
    #   Au, augmented matrix building. COncatenated by Axis 1
    Au =  np.concatenate([A,b],axis=1)
    #   N as the original matrix side size 
    N = np.size(Au, 0)
    #   M as augmented matrix larger side size
    M = np.size(Au, 1)
    
    for k in range(N):
        #   It gets Au[k][k] as the pivot
        pivot = Au[k,k]
        
        #   Watch if the pivot is zero
        if pivot == 0:
            Au = exchangeMax(Au, k, N)
            
        #   Divide over Au[k][k] to get 1
        Au[k,:] = Au[k,:] / pivot
        
        #   Now iteratively it go over all elements in the row
        for i in range(0, N):
            #   It skips if the iteration is on the pivot row
            if  i == k:
                continue
            #   It iterates over all columns at right of the pivor including self
            Au[i, :] = Au[i,:] - ( Au[i, k] * Au[k,:] )    
                     
            #for j in range(k,M):
            #    Au[i,j] = Au[i,j] - ( factor * Au[k,j])
    
    #   It have now the triangular matrix
    #   Now it substitute using back-sustitution
    #   It creates a Solution vector as zeros
    x = np.zeros([N,1])
    #   It iterates over the rows matrix in reverse
    for i in range(N-1, -1, -1):
        #   It stores the sum of befor solutions
        befsum = 0
        #   It iterates over the row columns
        for j in range(i + 1, N):
            #   It still sum the values into the row sum
            befsum += Au[i,j]*x[j,0]
        #   It gets that solution xi
        x[i,0] = ( 1.0 / Au[i,i] ) * ( Au[i, M-1 ] -befsum )
    
    #   Finally it returns the solution array
    return x

#   Test
if len(sys.argv) > 1:
    if sys.argv[1] == '-t':
        #   Here it test the algorithm
        A = np.random.rand(3, 3)
        b = np.random.rand(3, 1)
        print('Using this random values:')
        print('A:')
        print(A)
        print('b:')
        print(b)
        print('Using this gauss Algorithm, the solution is:')
        print(gaussJordanSolve(A,b))
        print('And using the linalg.solve is')
        print(np.linalg.solve(A,b))