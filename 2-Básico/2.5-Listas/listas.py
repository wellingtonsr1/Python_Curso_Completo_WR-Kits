#!/usr/bin/python3

#!/usr/bin/python3

# print("✓")
# print("✗")

#lista = [1, 2, 3, 4, 5, 8]
#lista2 = [7, 8]
lista_teste = [['teste 1', False], ['teste 2', True]]

for lista in lista_teste:
    if lista[0] == 'b' and lista[1] == False:
        lista[1] = True
#         index = lista_teste.index(lista)
#         break
# print(index)
# lista_teste.pop(index)
#print(lista_teste)
#print(lista_teste)

nome = "teste 1"
novo_nome = 'wellington'
for item_lista in lista_teste:
    if nome == item_lista[0]:
        index = lista_teste.index(item_lista)
        lista_teste[index][0] = novo_nome
        break

print(f"Nome atual: {nome}")      
print(lista_teste)







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