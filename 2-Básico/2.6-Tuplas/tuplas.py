#!/usr/bin/python3 

# Tuplas são semelhantes às listas, mas são imutáveis, ou seja, não podem ser modificadas após a criação.

# Criando uma tupla
from sympy import var


tupla = (1, 2, 3, 4, 5)

print("\n--- Tupla ---")
print(tupla)

print("\n--- Tipo de dado ---")
print(type(tupla))

print("\n--- Acessando elementos ---")
print("Primeiro elemento:", tupla[0])   # Acessa o primeiro elemento
print("Terceiro elemento:", tupla[2])   # Acessa o terceiro elemento
print("Último elemento  :", tupla[-1])  # Acessa o último elemento
print("Fatia (1:4)      :", tupla[1:4]) # Acessa uma fatia da tupla
print("O valor 3 está na tupla?", 3 in tupla)  # Verifica se o valor 3 está na tupla
print("O valor 3 não está na tupla?", 3 not in tupla)  # Verifica se o valor 3 não está na tupla

lista = [1, 2, 3, 4, 5]
print("\n--- Lista ---")
print(lista)

print("\n--- Convertendo lista para tupla ---")
tupla_convertida = tuple(lista)
print(tupla_convertida)

print("\n")


