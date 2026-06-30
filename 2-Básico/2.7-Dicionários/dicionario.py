#!/usr/bin/python3

# # # Dicionário em Python
# # info = {
# #     'nome': 'João',
# #     'sobrenome': 'Silva',
# #     'idade': 30,
# #     'cidade': 'São Paulo'
# # }

# # print("\nDicionário Completo:")
# # print("--------------------")
# # print(info)  # Imprime o dicionário completo

# # # Acessando os valores do dicionário usando as chaves
# # print("\nInformações do Dicionário:")
# # print("---------------------------")
# # print("Nome     : ", info['nome'])  # Acessando o valor associado à chave 'nome'
# # print("Sobrenome: ", info['sobrenome'])  # Acessando o valor associado à chave 'sobrenome'
# # print("Idade    : ", info['idade'])  # Acessando o valor associado à chave 'idade'
# # print("Cidade   : ", info['cidade'])  # Acessando o valor associado à chave 'cidade'

# # print("\n") # Imprime uma linha em branco para melhor formatação.

# nome = input("Informe o nome: ")
# sobrenome = input("Informe o sobrenome: ")
# idade = input("Informe a idade: ")
# cidade = input("Informe a cidade: ")

# info = {
#     'nome': nome,
#     'sobrenome': sobrenome,
#     'idade': idade,
#     'cidade': cidade
# }

# print(f"Antes: {info}")

# # #Assim, trata também espaços: Entrada: "     " não deve ser considerado um nome válido.

# # Recebe os dados
# n_nome = input("Informe o novo nome: ").strip()
# n_sobrenome = input("Informe o novo sobrenome: ").strip()
# n_idade = input("Informe a nova idade: ").strip()
# n_cidade = input("Informe a nova cidade: ").strip()

# # Atualiza, caso não for vazio.
# if n_nome: info['nome'] = n_nome
# if n_sobrenome: info['nome'] = n_sobrenome
# if n_idade: info['idade'] = n_idade
# if n_cidade: info['cidade'] = n_cidade

# # Exibe os novos dados em uma única linha.
# print(f"Depois: {info}")

# # Exibe os novos dados em várias linhas.
# print(f"Nome: {info['nome']}")
# print(f"Sobrenome: {info['sobrenome']}")
# print(f"Idade: {info['idade']}")
# print(f"Cidade: {info['cidade']}")

# # print(bool(""))
# # print(bool("joão"))

# # o 'pop' remove e retorna quem foi removido.
# removido = info.pop('nome')

# print(f"{removido} foi removido com sucesso!")

# # o 'del' apenas remove sem retornar quem foi removido.
# del info['idade']

# print(info)

# # adicionando mais um elemento ao dicionário
# info['pais'] = 'Brasil'

# print(info)

lista = [{'a': 1, 'b': 2, 'c':3}, {'a': 10, 'B': 2, 'C': 3}]

#print(lista[0]['a'])

# for dic in lista:
#     if dic['a'] == 1:
#         lista.remove(dic)
# print(lista)

# def busca(num_1):
#     for num in lista:
#         if num['a'] == num_1:
#             return True
            

#     return False

# print(busca(1))

# aluno = {
#     "nome": "Teste",
#     "bimestres": {
#         "B1": {
#             "n1": 1,
#             "n2": 2,
#             "n3": 3,
#             "n4": 4
#         },
#         "B2": {
#             "n1": 1,
#             "n2": 2,
#             "n3": 3,
#             "n4": 4
#         },
#         "B3": {
#             "n1": 1,
#             "n2": 2,
#             "n3": 3,
#             "n4": 4
#         },
#         "B4": {
#             "n1": 1,
#             "n2": 2,
#             "n3": 3,
#             "n4": 4
#         }
#     }
# }


# print(aluno['bimestres']['B1'])


# def soma(a, b, c):
#     d = a + b + c
#     e = d/ 3

#     return d, e

# r1, r2 = soma(10, 20, 30)
# print(f"Soma: {r1} Média: {r2}")


alunos = [
    {
        "nome": "Ana Silva",
        "bimestres": {
            "b1": {"nota_1": 8.0, "nota_2": 7.5, "nota_3": 9.0, "nota_4": 8.5, "media": 8.25},
            "b2": {"nota_1": 7.0, "nota_2": 8.0, "nota_3": 8.5, "nota_4": 9.0, "media": 8.13},
            "b3": {"nota_1": 9.0, "nota_2": 9.5, "nota_3": 10.0, "nota_4": 8.5, "media": 9.25},
            "b4": {"nota_1": 8.0, "nota_2": 8.5, "nota_3": 9.0, "nota_4": 9.5, "media": 8.75}
        },
        "media_final": 8.60,
        "status": "Aprovado"
    },
    {
        "nome": "Bruno Santos",
        "bimestres": {
            "b1": {"nota_1": 4.0, "nota_2": 5.0, "nota_3": 3.5, "nota_4": 4.5, "media": 4.25},
            "b2": {"nota_1": 3.0, "nota_2": 4.0, "nota_3": 5.0, "nota_4": 3.5, "media": 3.88},
            "b3": {"nota_1": 5.0, "nota_2": 4.5, "nota_3": 4.0, "nota_4": 5.5, "media": 4.75},
            "b4": {"nota_1": 2.0, "nota_2": 3.0, "nota_3": 4.0, "nota_4": 3.0, "media": 3.00}
        },
        "media_final": 3.97,
        "status": "Reprovado"
    },
    {
        "nome": "Carlos Oliveira",
        "bimestres": {
            "b1": {"nota_1": 6.0, "nota_2": 6.5, "nota_3": 7.0, "nota_4": 6.0, "media": 6.38},
            "b2": {"nota_1": 5.5, "nota_2": 6.0, "nota_3": 7.0, "nota_4": 6.5, "media": 6.25},
            "b3": {"nota_1": 7.0, "nota_2": 7.5, "nota_3": 6.5, "nota_4": 8.0, "media": 7.25},
            "b4": {"nota_1": 6.0, "nota_2": 6.5, "nota_3": 7.0, "nota_4": 7.5, "media": 6.75}
        },
        "media_final": 6.66,
        "status": "Aprovado"
    }
]


def exibir_detalhes_aluno(lista_alunos, nome=None, status=None):
    alunos_exibir = lista_alunos
   
    if nome:
        #alunos_exibir = []
        # alunos_exibir = [
        #     aluno for aluno in lista_alunos 
        #     if aluno['nome'].lower() == nome.strip().lower()
        # ]
        for aluno in lista_alunos:
            if aluno['nome'].lower() == nome.strip().lower():
                alunos.append(aluno)
    elif status:
        alunos_exibir = []
        # alunos_exibir = [
        #     aluno for aluno in lista_alunos 
        #     if aluno['status'].lower() == "Aprovado".lower()
        # ]
        for aluno in lista_alunos:
            if aluno['status'].lower() == "Aprovado".lower():
                alunos.append(aluno)

    #Percorre cada aluno armazenado na lista
    for aluno in alunos_exibir:
        print(f"\nAluno...: {aluno['nome']}")
        for i in range(4):
            print(f"\n ** {i + 1}º Bimestre **")
            # Exibe as 4 notas do bimestre atual em uma única linha para economizar espaço
            notas_str = ""
            for j in range(4):
                nota = aluno['bimestres'][f'b{i + 1}'][f'nota_{j + 1}']
                notas_str += f"N{j + 1}: {nota:.1f}  | "
                media = f"{aluno['bimestres'][f'b{i + 1}']['media']}"
        
            print(f"    Notas: {notas_str} Média Parcial: {media}")

        print(f"\nMédia Final..: {aluno['media_final']}")
        print(f"Situação.....: {aluno['status']}")
        print("-" * 25)


nome = "Carlos Oliveira"
aprovado = False
alunos

exibir_detalhes_aluno(alunos, "Carlos Oliveira", None)
