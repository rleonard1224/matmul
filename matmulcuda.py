'''
Python script containing cuda-accelerated matrix multiplication kernel
'''
# Import Python libraries
import numpy as np
import cupy as cp
import time 
# Define cuda kernel
class cuda_kernels():
    # Matrix multiplication method
    # Calculate a[mxn] * b[nxp] = c[mxp]
    def matmul_cuda():
        kernel = cp.RawKernel(r'''
        #include <cupy/complex.cuh>
        extern "C"{ 
            __global__ void matmul(const double *A, const double *B, double *C, int m, int n, int p) 
            {
                int bid = gridDim.y*blockIdx.x + blockIdx.y;
                int tid = blockDim.y*threadIdx.x + threadIdx.y;
                int nelements = m*p;
                if ((bid < nelements) && (tid < n))
                {
                    int arow = bid / p;
                    int bcolumn = bid % p;
                    atomicAdd(&C[bid], A[arow*n+tid]*B[bcolumn+tid*p]);
                }
            }
        }''', 'matmul')
        return kernel
# Allocate matrices on gpu
N = 1000
A = cp.ones((N,N))
B = cp.ones((N,N))
C = cp.zeros((A.shape[0],B.shape[1]),cp.double)
m = A.shape[0]; n = A.shape[1]; p = B.shape[1]
# Allocate gpu grid
blockx = 1024; blocky = 1024
threadx = 1024
kernel = cuda_kernels.matmul_cuda()
# Call and time the cuda kernel
start = time.time()
kernel((blockx,blocky), (threadx,), (A, B, C, m, n, p))
end = time.time()
# Print timing
print("Time = {}".format(end - start))
