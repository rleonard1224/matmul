'''
Python script for jit-accelerated matrix multiplication
'''
# Import Python libaries
import numpy as np
import time 
from numba import jit, njit, prange
# Matrix multiplication method
# Calculate A[mxn] * B[nxp] = C[mxp]
@jit
def matmul(A, B, m, n, p):
    C = np.zeros((m,p))
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i,j] = C[i,j] + A[i,k]*B[k,j]
    return C
# Allocate matrices
N = 1000
A = np.ones((N,N))
B = np.ones((N,N))
m = A.shape[0]
n = A.shape[1]
p = B.shape[1]
# Calculate and time matrix product
start = time.time()
C = matmul(A,B,m,n,p)
end = time.time()
# Print timing
print("Time = {}".format(end - start))




