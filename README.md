# matmul

## Matrix multiplication algorithms accelerated with jit and cuda

* `matmulnumba.py` - numba accelerated matrix multiplication
* `matmulcuda.py` - cuda accelerated matrix multiplication
* `speedup.pdf` - plot of speedup of cuda code vs. numba code

## Dockerfile

In order to setup and run the Dockerfile, execute the following steps:
  * `export MATMUL_ROOT=<path-to-matmul-repo>`
  * `cd <path-to-matmul-repo>`
  * `chmod 777 run.sh`
  * `chmod 777 run_matmulcuda.sh`
  * `chmod 777 run_matmulnumba.sh`
  * `docker build --tag matmul:matmul .`

