from multiprocessing import Pool
import time

def string_proof(x):
     print(x)
     time.sleep(3)

# Implementation 1: Run in serial
# time: 30 secs
def implementation_1():
     string_proof("Hello")
     string_proof("Hello")
     string_proof("Hello")
     string_proof("World")
     string_proof("World")
     string_proof("World")

# Implementation 2: Run in a process pool
# time: 10 secs
def implementation_2():
    p = Pool(3)
    p.map(string_proof,["Hello","Hello","Hello","World","World","World"])

# Implementation 3: Run using an MPI pool


#CALL COMMAND
implementation_2()
