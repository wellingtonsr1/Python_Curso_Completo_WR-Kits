#!/usr/bin/python3

import pandas as pd

data = {
    'Nome': [
        'Alice',
        'Bob',
        'João',
        'Maria',
        'Carlos',
        'Ana',
        'Pedro',
        'Juliana',
        'Fernando',
        'Camila'
    ],
    
    'Idade': [
        25,
        30,
        35,
        28,
        42,
        31,
        22,
        27,
        50,
        24
    ],
    
    'Cidade': [
        'São Paulo',
        'Canela',
        'Gramado',
        'Rio de Janeiro',
        'Belo Horizonte',
        'Curitiba',
        'Recife',
        'Salvador',
        'Porto Alegre',
        'João Pessoa'
    ],
    
    'Profissão': [
        'Analista de Dados',
        'Engenheiro',
        'Professor',
        'Médica',
        'Administrador',
        'Designer',
        'Desenvolvedor',
        'Advogada',
        'Consultor',
        'Arquiteta'
    ],
    
    'Salário': [
        4500,
        7500,
        5200,
        9000,
        6800,
        4000,
        3500,
        6200,
        10000,
        5500
    ],
    
    'Status': [
        'Ativo',
        'Ativo',
        'Ativo',
        'Ativo',
        'Inativo',
        'Ativo',
        'Ativo',
        'Ativo',
        'Inativo',
        'Ativo'
    ]
}

print("Dicionário criado: ")
print(data)

df = pd.DataFrame(data)
print(df)

print("Obtendo Idade")
print(df['Idade'])

print("Retornando linha 1")
print(df.iloc[1])

print("Editando idade de Bob")
df.loc[1, 'Idade'] = 31
print(df)


print("Filtrar maiores de 30")
print(df[df['Idade'] > 30])