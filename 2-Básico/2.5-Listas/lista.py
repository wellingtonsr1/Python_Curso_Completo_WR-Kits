#!/usr/bin/python3

# Listas em Python
lista = [1, 2, 3, 4, 5]
lista2 = [7, 8, 9, 10, 11, 12, 40, 54, 67, 89, 90]

print("------------------------------------------------------")
print("Imprimindo cada elemento da lista:")
print("------------------------------------------------------")
for numero in lista:
    print(numero)
print("------------------------------------------------------")
print("Imprimindo a lista completa:")
print("------------------------------------------------------")
print(lista)

print("\n--------------------------------------------------------")
print("Imprimindo o índice e o valor de cada elemento da lista:")
print("--------------------------------------------------------")
for indice in range(len(lista)):
    print(f"Índice: {indice}, Valor: {lista[indice]}")

lista.append(6)  # Adiciona o número 6 ao final da lista
print("\n------------------------------------------------------")
print("Lista após adicionar o número 6:")
print("------------------------------------------------------")
print(lista)

lista.extend(lista2)  # Adiciona os elementos de lista2 ao final de lista
print("\n------------------------------------------------------")
print("Lista após adicionar os elementos de lista2:")
print("------------------------------------------------------")
print(lista)

lista.insert(2, 10)  # Insere o número 10 na posição de índice 2
print("\n------------------------------------------------------")
print("Lista após inserir o número 10 na posição de índice 2:")
print("------------------------------------------------------")
print(lista)

lista.pop(2)  # Remove o elemento na posição de índice 2
print("\n------------------------------------------------------")
print("Lista após remover o elemento na posição de índice 2:")
print("------------------------------------------------------")
print(lista)

lista.remove(7)  # Remove o número 7 da lista
print("\n------------------------------------------------------")
print("Lista após remover o número 7:")
print("------------------------------------------------------")
print(lista)

lista.clear()  # Remove todos os elementos da lista
print("\n------------------------------------------------------")
print("Lista após limpar todos os elementos:")
print("------------------------------------------------------")
print(lista)

ultimo_elemento = lista2[-1]  # Acessa o último elemento da lista2 usando índice negativo
print("\n------------------------------------------------------")
print("Último elemento da lista2 usando índice negativo:")
print("------------------------------------------------------")
print(ultimo_elemento)

print("\n------------------------------------------------------")
print("Elementos da lista2 de índice 6 a 9:")
print("------------------------------------------------------")
print(lista2[6:9]) # Imprime os elementos da lista2 do índice 6 ao 8 (o índice 9 é exclusivo)

print("\n------------------------------------------------------")
print("O número 0 está na lista2?")
print("------------------------------------------------------")
print(0 in lista2) # Verifica se o número 0 está presente na lista2

print("\n------------------------------------------------------")
print("O número 0 não está na lista2?")
print("------------------------------------------------------")
print(0 not in lista2) # Verifica se o número 0 não está presente na lista2


# Imprime uma linha em branco para separar a saída
print("\n")
