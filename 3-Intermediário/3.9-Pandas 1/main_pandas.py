#!/usr/bin/python3

import pandas as pd

data = {
    'Nome': ['Alice', 'Bob', 'João'],
    'Idade': [25, 30, 35],
    'Cidade': ['São Paulo', 'Canela', 'Gramado']
}

print("Dicionário criado: ")
print(data)

df = pd.DataFrame(data)
print(df)

