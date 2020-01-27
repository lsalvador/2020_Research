from mpi4py import MPIPoolExecutor
from multiprocessing import Pool
import time

def time_proof(x):
     time.sleep(5)

# Implementation 1: Run in serial
# time: 30 secs
def implementation_1():
     time_proof(1)
     time_proof(2)
     time_proof(3)
     time_proof(4)
     time_proof(5)
     time_proof(6)

# Implementation 2: Run in a process pool
# time: 10 secs
def implementation_2():
    p = Pool(3)
    p.map(time_proof,[1,2,3,4,5,6])

# Implementation 3: Run using an MPI pool
def implementation_3():
    with MPIPoolExecutor(max_workers=3) as executor:
        futures = executor.map(time_proof,[1,2,3,4,5,6])

#CALL COMMAND
implementation_3()
