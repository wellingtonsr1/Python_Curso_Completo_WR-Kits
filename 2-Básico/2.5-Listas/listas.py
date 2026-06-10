#!/usr/bin/python3

#!/usr/bin/python3

# print("✓")
# print("✗")

lista = [1, 2, 3, 4, 5, 8]
lista2 = [7, 8]

for index in range(len(lista)):
    print(lista[index])

#print(f"Tamanho: {len(lista)}")

lista.extend(lista2)
print(lista)

lista.insert(2, 32)
print(lista)

lista.pop(2)
print(lista)

del lista[3]
print(lista)

lista.remove(8)
print(lista)

#lista.clear()
#print(lista)

#print(lista[-1])

print(lista[len(lista)-1])

print("Sim") if 53 in lista else print("Não")
print("Sim") if 53 not in lista else print("Não")