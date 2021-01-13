# matmul

## Matrix multiplication algorithms accelerated with jit and cuda

* `matmulnumba.py` - numba accelerated matrix multiplication
* `matmulcuda.py` - cuda accelerated matrix multiplication
* `speedup.pdf` - plot of speedup of cuda code vs. numba code

## Dockerfile

In order build the Docker image, execute the commands:
  * `export MATMUL_ROOT=<path-to-matmul-repo>`
  * `cd <path-to-matmul-repo>`
  * `docker build --tag matmul:matmul .`

To launch the Docker container, execute the commands: 
 * `chmod 777 run.sh`
 * `./run.sh`
