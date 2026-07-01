#!/usr/bin/python3


import numpy
import numpy as np

arr1 = numpy.arange(10)
print(arr1)

arr3 = numpy.arange(0, 1.2, 0.1, dtype=float)
print(arr3)

print("\nAlterando forma de 1x10 para 2x5")
arr4 = np.reshape(arr1, (2, 5), 'C')
print(arr4)

print("\nAlterando forma de 1x10 para 2x5 no mmodo Fortran")
arr5 = np.reshape(arr1, (2, 5), 'F')
print(arr5)