#!/usr/bin/python3

# Conjuntos (set)

print("\nConjuntos (set)")
print("--------------------")

print("Frutas 1")
frutas1 = {"maçã", "banana", "banana", "laranja"}
print(frutas1)

print("\nAdicionando um elemento ao conjunto frutas1:")
frutas1.add("uva")
print(frutas1)

print("\nRemovendo um elemento do conjunto frutas1:")
frutas1.remove("banana")
print(frutas1)

print("\nFrutas 2")
frutas2 = {"banana", "uva", "abacaxi", "abacaxi"}
print(frutas2)

print("\nUnião de frutas1 e frutas2:")
frutas_uniao = frutas1.union(frutas2)
print(frutas_uniao)


print("\n") # Quebra de linha para melhor visualização



