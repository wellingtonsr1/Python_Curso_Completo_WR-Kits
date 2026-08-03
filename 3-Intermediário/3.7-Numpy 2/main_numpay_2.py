#!/usr/bin/python3

# import numpy as np

# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([11, 12, 13, 14, 15])

# print("Numpy Broadcasting")
# soma_broadcasting = arr1 + arr2
# print(soma_broadcasting)

# print("Slicing avançado")
# arr3 = np.array([
#      [0, 1, 2, 0, 1, 2], 
#      [3, 4, 5, 0, 1, 2], 
#      [9, 10, 11, 0, 1, 2],
#      [0, 1, 2, 0, 1, 2], 
#      [3, 4, 5, 0, 1, 2], 
#      [9, 10, 11, 0, 1, 2]
# ])


# print("\nArray Original")
# print(arr3)

# print("\nLinhas ímpares: ")
# print(arr3[1::2,:])

# print("\nLinhas Pares: ")
# print(arr3[0::2,:])

# print("\nColunas ímpares: ")
# print(arr3[:,1::2])

# print("\nColunas Pares: ")
# print(arr3[:,0::2])

# print("\nCriando um array iniciado com zeros: ")
# arr4 = np.zeros((3, 4))
# print(arr4)

# print("\nCriando um array iniciado com zeros: ")
# arr4 = np.ones(shape=(3, 3, 4), dtype=np.int16)
# print(arr4)

# print(arr4.dtype.name)

# arr5 = np.random.randint(10, size=6)
# arr6 = np.random.randint(10, size=(3, 4))
# arr7 = np.random.randint(10, size=(3, 4, 5))

# print("\n *** arr5 ***")
# print(arr5)

# print("\n *** arr6 ***")
# print(arr6)

# print("\n *** arr7 ***")
# print(arr7)

# print("\nConvertendo tipo do array")
# arr7 = np.array(arr7, dtype=float)
# print(arr7)

import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)