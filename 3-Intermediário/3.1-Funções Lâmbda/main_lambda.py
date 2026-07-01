#!/usr/bin/python3

# quadrado = lambda x: x ** 2
# # quadrado = lambda x: {x ** 2}
# print(quadrado(5))


# par_ou_impar = lambda x: x % 2 == 0
# print(par_ou_impar(32))


dicionario = {
    'a': 5,
    'b': 10,
    'c': 15,
    'd': 20
}

filtra_pares = lambda dic: {
    chave: valor for chave, valor in dic.items() if valor % 2 == 0
}
print(filtra_pares(dicionario))