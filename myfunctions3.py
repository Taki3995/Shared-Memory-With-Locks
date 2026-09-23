#!/usr/bin/env python
# coding: utf-8

# # My Functions Library
# 
#
import numpy as np
from multiprocessing.sharedctypes import Value, Array, RawArray
import multiprocessing as mp


# In[ ]:




from multiprocessing.sharedctypes import Value, Array, RawArray
from multiprocessing import Process, Lock
import ctypes



# In[ ]:


#This function just creates a numpy array structure of type unsigned int8, using the memory from our global r/w shared memory
def tonumpyarray(mp_arr: Array):
    #mp_arr is a shared memory array with lock
    
    return np.frombuffer(mp_arr.get_obj(),dtype=np.uint8)

def tonumpyarrayF(mp_arr: Array):
    #mp_arr is a shared memory array with lock
    
    return np.frombuffer(mp_arr.get_obj(),dtype=np.float64)
    
#this function creates an instance of the Value data type and initializes it to 0
def dot_init(g_A):
    global A 
    A = g_A #We create a variable of type "double"           
    
    
def shared_dot_1(V):
    #This code is wrong!
    for f in V:
        A.value += f[0]*f[1]
    
def shared_dot_2(V):
    #This code is wrong!
    with A.get_lock():
        for f in V:
            A.value += f[0]*f[1]
    
def shared_dot_3(V):
    #This code is wrong!
    a=0
    for f in V:
        a += f[0]*f[1]
    with A.get_lock():
        A.value += a
    
shared_space = None
shared_matrix = None
matA = None
matB = None

def init_sharedarray(matA_in : np.ndarray,
                     matB_in : np.ndarray,
                     shared_array: Array ):
    global shared_space
    global shared_matrix
    global matA
    global matB

    matA = matA_in
    matB = matB_in

    a_rows, a_cols = matA.shape
    b_rows, b_cols = matB.shape
    
    shared_space = shared_array
    shared_matrix = tonumpyarrayF(shared_space).reshape((a_rows,b_cols))

def matmulP(coord) -> None:
    # The parameter coord can vary depending on your approach to solve the matrix multiplication:
    # can be of type tuple, if you pass the coordinates of the cell to calculate (fine granularity)
    # or can be a simple integer if your approach is the row to calculate sequentially (medium granularity)

    # Access the global variables
    # Because both use the same computers memory space, they will have the same values. 
    # the difference is the acces to the propetary methods in each one data object instance-
    # shared_space is an instance of the Array object with the methods defined for shared memory
    # shared_matrix is an instance of np.array object (the second way to view the memory space) 
    # has all the methods that belong to np.ndarray objects
    
    global shared_space
    global shared_matrix

    accu = 0 #dummy variable, you can use or not, depending on the algorithm you decide to implement
    # The use of the get_lock() method is mandatory. You should carefully analyse where it can be placed
    # so as to minimise its impact on the overall execution of the program. In your conclusions,
    #  you may then discuss whether its use is actually necessary for the implementation you have developed.

    with shared_space.get_lock():
        accu += 1 #this is a dummy line, just to be able to load the library at the beginning
        # In this section, you have to program the parallel code to implement the global matrix multiplication
        # and store the result in the shared memory variable.
        


#This cell should be the last one
#This avoids the execution of this script when it is invoked directly.
if __name__ == "__main__":
    print("This is not an executable library")

