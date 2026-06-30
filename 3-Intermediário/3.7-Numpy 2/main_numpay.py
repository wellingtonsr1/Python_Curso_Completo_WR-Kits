#!/usr/bin/python3

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([11, 12, 13, 14, 15])

print("Numpy Broadcasting")
soma_broadcasting = arr1 + arr2
print(soma_broadcasting)

print("Slicing avançado")
arr3 = np.array([
     [0, 1, 2, 0, 1, 2], 
     [3, 4, 5, 0, 1, 2], 
     [9, 10, 11, 0, 1, 2],
     [0, 1, 2, 0, 1, 2], 
     [3, 4, 5, 0, 1, 2], 
     [9, 10, 11, 0, 1, 2]
])


print("\nArray Original")
print(arr3)

print("\nLinhas ímpares: ")
print(arr3[1::2,:])

print("\nLinhas Pares: ")
print(arr3[0::2,:])

print("\nColunas ímpares: ")
print(arr3[:,1::2])

print("\nColunas Pares: ")
print(arr3[:,0::2])

print("\nCriando um array iniciado com zeros: ")
arr4 = np.zeros((3, 4))
print(arr4)

print("\nCriando um array iniciado com zeros: ")
arr4 = np.ones(shape=(3, 3, 4), dtype=np.int16)
print(arr4)

print(arr4.dtype.name)