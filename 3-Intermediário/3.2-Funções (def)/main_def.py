#!/usr/bin/python3

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 1, 1, 3, 3]

def conta_diferentes(lista):
    return len(set(lista))

conta_diferentes = lambda lista: len(set(lista))

print(f"Sem usar lambda: {conta_diferentes(numeros)}")
print(f"Usando lambda  : {conta_diferentes(numeros)}")


