#mpi4py practice
import mpi4py

print("""MPI stands for Message passing interface. An implementation of MPI such as MPICH"
or OpenMPI is used to create a platform to write parallel programs in a distributed
system such as a Linux cluster with distributed memory. Generally the platform
built allows programming in C using the MPI standard. So in order to run Parallel programs
in this environment in python, we need to make use of a module called MPI4py which means
"MPI for Python". This module provides standard functions to do tasks such as get
the rank of processors, send and receive messages/ data from various nodes in the clusters.
It allows the program to be parallely executed with messages being passed between nodes.
It is important that MPIch2 and MPI4py is installed in your system. So, if you haven't installed
MPI4Py, following are 2 guides to refer to for installing, building and testing
a sample program in MPI4PY.""")

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print(rank)
if rank == 0:
    data = {'a': 7, 'b': 3.14}
    comm.send(data, dest=1, tag=11)
elif rank == 1:
    data = comm.recv(source=0, tag=11)
