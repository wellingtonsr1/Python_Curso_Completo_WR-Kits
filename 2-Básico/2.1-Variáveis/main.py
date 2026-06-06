#!/usr/bin/python3

import string 
import sys


intVal = 42
floatVal = 3.14
bolVal = False
charVal = 'A'
stringVal = "Hello, World!"


print("Concatenando valores:", str(intVal) + " " + str(floatVal) + " " + str(bolVal) + " " + charVal + " " + stringVal   
)
print("Usando fstring      :", f"{intVal} {floatVal} {bolVal} {charVal} {stringVal}\n")

print("Tamanho do intVal   :", sys.getsizeof(intVal))
print("Tamanho do floatVal :", sys.getsizeof(floatVal))
print("Tamanho do bolVal   :", sys.getsizeof(bolVal))
print("Tamanho do charVal  :", sys.getsizeof(charVal))
print("Tamanho do stringVal:", sys.getsizeof(stringVal))
