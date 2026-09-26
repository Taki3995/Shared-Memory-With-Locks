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
    # Declaración de variables globales compartidas por el inicializador
    global shared_space
    global shared_matrix
    global matA
    global matB

    # coord es la fila i de la Matriz A que se va a multiplicar con la Matriz B
    i = coord
    
    # Total de columnas B 
    b_cols = matB.shape[1]
    
    # Total elementos de la fila i de A (columnas de A)
    a_cols = matA.shape[1]
    
    accu = 0 # Candado de acceso. Dummy.
    with shared_space.get_lock():
        accu += 1 
        
    # Inicio de la ecuación matemática (Sin usar locks ya que cada proceso vaa escribir en una fila diferente de la matriz compartida)
    for j in range(b_cols):
        temp_sum = 0.0
        
        for k in range(a_cols):
            temp_sum += matA[i, k] * matB[k, j]
            
        # Asignar la sumatoria completa a la celda específica de la memoria compartida
        shared_matrix[i, j] = temp_sum
        


#This cell should be the last one
#This avoids the execution of this script when it is invoked directly.
if __name__ == "__main__":
    print("This is not an executable library")

