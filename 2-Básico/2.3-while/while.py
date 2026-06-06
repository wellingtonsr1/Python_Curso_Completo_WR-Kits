#!/usr/bin/python3

import random, os

os.system('clear')
numero_sorteado = random.randint(1, 100)

chute = 0

print("==================================================")
print("         Bem-vindo ao jogo de adivinhação!        ")
print("==================================================")

while chute != numero_sorteado:
    chute = int(input("Digite um número entre 1 e 100: "))
    
    if chute < numero_sorteado:
        print("Tente um número maior.")
    elif chute > numero_sorteado:
        print("Tente um número menor.")
    else:
        print("Parabéns! Você acertou o número sorteado!")


