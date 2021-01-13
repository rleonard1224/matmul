# matmul

## Matrix multiplication algorithms accelerated with jit and cuda

* `matmulcuda.py` - cuda accelerated matrix multiplication
* `matmulnumba.py` - numba accelerated matrix multiplication
* `speedup.pdf` - plot of speedup of cuda code vs. numba code

## Dockerfile

In order build the Docker image and change permissions on run scripts execute the commands:
  * `export MATMUL_ROOT=<path-to-matmul-repo>`
  * `cd <path-to-matmul-repo>`
  * `docker build --tag matmul:matmul .`
  * `chmod 777 run.sh`
  * `chmod 777 run_matmulcuda.sh`
  * `chmod 777 run_matmulnumba.sh`

To launch the Docker container execute the command:
  * `./run.sh`

To run matmulcuda.py while inside the Docker container execute the command:
  * `./run_matmulcuda.py`
  
To run matmulnumba.py while inside the Docker container execute the command:
  * `./runmatmulnumba.py`

