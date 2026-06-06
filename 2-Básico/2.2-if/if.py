#!/usr/bin/python3

import os

os.system('clear')
idade = int(input("Digite sua idade: "))


if idade < 18:
    print("Você é menor de idade.")
elif idade >= 18 and idade < 21:
    print("Você é maior de idade.")
elif idade == 21:   
    print("Você tem exatamente 21 anos.")
elif idade > 21 and idade <= 60:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")