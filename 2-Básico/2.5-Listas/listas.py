#!/usr/bin/python3

#!/usr/bin/python3

# print("✓")
# print("✗")

#lista = [1, 2, 3, 4, 5, 8]
#lista2 = [7, 8]
lista_teste = [['b', False], ['a', True]]

for lista in lista_teste:
    if lista[0] == 'b' and lista[1] == False:
        lista[1] = True
#         index = lista_teste.index(lista)
#         break
# print(index)
# lista_teste.pop(index)
#print(lista_teste)
print(len(lista_teste[-1]))
print(len(lista_teste))
#print(len(lista_teste[-1]) == len(lista_teste))
if (len(lista_teste[-1])) == len(lista_teste):
    print("ok")
# for index in range(len(lista)):
#     print(lista[index])

# #print(f"Tamanho: {len(lista)}")

# lista.extend(lista2)
# print(lista)

# lista.insert(2, 32)
# print(lista)

# lista.pop(2)
# print(lista)

# del lista[3]
# print(lista)

# lista.remove(8)
# print(lista)

# #lista.clear()
# #print(lista)

# #print(lista[-1])

# print(lista[len(lista)-1])

# print("Sim") if 53 in lista else print("Não")
# print("Sim") if 53 not in lista else print("Não")