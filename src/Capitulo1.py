
import cmath as c
import math 
import numpy as np

def suma(a,b): 
    return a+b

def div(a,b):
    return a/b

a= suma(1,8)
b=div(1+3j,5+8j)
print(b)
print(c.polar(a))
print(c.phase(a)) 

print(dir(c))
print(c.rect(1,0))


#Programming Drill 2.1.1
#Write three functions that perform the addition, inverse,
#and scalar multiplication operations for Cn, i.e., write a function that accepts the ap
#propriate input for each of the operations and outputs the vector

# When n=1, the matrices Cm×n = Cm×1 = Cm,Thus, we can think of vectors as special types of matrices.
def matrix_sum(v,w): 
    if(len(v)==len(w)):
        return v+w
    else:
        return print("diferent vector len")

def matrix_inverse(v):
    return v*(-1)

def matrix_escalar_multiplication(escalar,matrix):
    return escalar*matrix

a= np.array([(1+2j,4+5j, 2+1j),(4-3j,9+2j,1+3j),(1,1,1)])
b=np.array([(1,0,0),(0,1,0),(0,0, 1)])

print(matrix_sum(a,b))
print(matrix_inverse(b))
print(matrix_escalar_multiplication(3,b) )


print(a.shape)
print(b.shape)

# Programming Drill 2.2.2 Write a function that accepts two complex matrices of the
# appropriate size. The function should do matrix multiplication and return the result

def matrix_multiplication(Ma_A, Ma_B): 
    (n,m)=Ma_A.shape
    (p,k)=Ma_B.shape
    if(m!=p):
        return "error en los tamaños de las matrices"
    Mult=np.empty((n,k), dtype=Ma_A.dtype) #creo un elemento de numpy vacio de tamaño (n,k)
    for fila_a in range(n):  #lo ultimo que vario es la fila de A , 
        for columna_b in range(k):   
            valor=0          #reinicio el valor de los elementos puntuales 
            for elemento in range(m):
                valor+= Ma_A[fila_a,elemento]*Ma_B[elemento,columna_b]
        Mult[fila_a,columna_b]=valor
    return Mult


def matrix_multiplication_eficiente(Ma_A, Ma_B):
    (n,m)=Ma_A.shape
    (p,k)=Ma_B.shape
    if(m!=p):
        return "error en los tamaños de las matrices"
    return (Ma_A @ Ma_B)
    

#Pued ha

print(matrix_multiplication(a,b))


#ProgrammingDrill2.4.1 Write a function that accepts two complex vectors of lengt n 
# and calculates their inner product.
def inner_product(v, w):
    if(len(v)==len(w)):
        return np.inner(v, w)
    else: #hacer que esta funcion tambien sirva para el prducto interno de matrices
        return print("diferent vector len")         
    

print("Producto interno:",inner_product([1,1,1],[1,1,1]))



# ProgrammingDrill2.4.2 Write a function that alculates the norm of a given complex vector.
def norma_vector(v):
    return np.linalg.norm(v)
   

print("a nrma",norma_vector([2]))


#Programming Drill 2.4.3 Write a function that calculates the distance of two given complex vectors.
def distancia_vectores(v,w):
    new_vec=v-w
    return math.sqrt(inner_product(new_vec,new_vec))
    
c=np.array([1,1])
d=np.array([1,1])


print("la dist",distancia_vectores(c,d))

#Programming Drill 2.6.1 Write a function that accepts a square matrix and tells if it is hermitian.
def is_hermitian(Ma):
    filas, columnas = Ma.shape
    if filas != columnas:
        return "No es cuadrada"
    Ma_adj = np.conjugate(Ma).T
    if np.allclose(Ma, Ma_adj):
        return True
    else:
        return False

#Programming Drill 2.6.2 Write a function that accepts a square matrix and tells if it is unitary.
def is_unitary(Ma):
     filas, columnas = Ma.shape
     if filas != columnas:
        return "No es cuadrada"
     Ma_adj = np.conjugate(Ma).T
     result= matrix_multiplication_eficiente(Ma,Ma_adj)
     identidad=np.eye(filas)
     if np.array_equal(result, identidad):
         return True
     else: return False
