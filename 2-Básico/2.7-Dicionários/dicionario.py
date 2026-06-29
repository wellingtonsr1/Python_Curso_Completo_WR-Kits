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


def soma(a, b, c):
    d = a + b + c
    e = d/ 3

    return d, e

r1, r2 = soma(10, 20, 30)
print(f"Soma: {r1} Média: {r2}")



def calcular_media_bimestre(n1, n2, n3, n4):
    
    # Calcula a média do bimestre atual.
    media = round((n1 + n2 + n3 + n4) / 4, 2)

    # Acumula a média do bimestre para cálculo da média final.
    #somatorio_medias += media

    # Calcula a média final considerando os quatro bimestres.
    #media_final = round(somatorio_medias / 4, 2)

    return media

# Realiza o cadastro de um novo aluno.
def adicionar_aluno():  
    while True:
        # Limpa a tela a cada chamada da função
        limpar_tela()

        # Exibe o cabeçalho da funcionalidade
        exibir_titutlo("CADASTRAR")

        print("    *** Digite 'q' pra sair... ***\n")

        # Entrada do nome do aluno
        nome = input("Informe o nome do aluno........: ").strip()

        # Faz uma checagem se o nome informado já existe.
        if not existe_aluno(nome):
            # Permite sair do cadastro
            if nome.lower() == 'q': break

            # Cria a estrutura inicial do aluno.
            # O dicionário 'bimestres' receberá posteriormente as notas
            # e médias de cada período letivo.
            aluno = {
                'nome': nome,
                'bimestres': {}
            }

            # Variável acumuladora utilizada para somar as médias dos quatro
            # bimestres e calcular a média final do aluno.
            somatorio_medias = 0

            # Percorre os quatro bimestres do ano letivo.
            for idx in range(4):
                #Solicita as quatro notas referentes ao bimestre atual.
                # Os valores são convertidos para float para permitir cálculos.
                nota_1 = float(input(f"\nInforme a primeira nota do B{idx + 1}..: "))
                nota_2 = float(input(f"Informe a segunda nota do B{idx + 1}...: "))
                nota_3 = float(input(f"Informe a terceira nota do B{idx + 1}..: "))
                nota_4 = float(input(f"Informe a quarta nota do B{idx + 1}....: "))

                # Calcula a média do bimestre atual.
                media = calcular_media_bimestre(nota_1, nota_2, nota_3, nota_4)

                # Acumula a média do bimestre para cálculo da média final.
                somatorio_medias += media

                # Adiciona o bimestre e suas respectivas notas ao dicionário do aluno.
                # A chave é criada dinamicamente (b1, b2, b3, b4).
                aluno['bimestres'][f"b{idx + 1}"] = {
                    'nota_1': nota_1,
                    'nota_2': nota_2,
                    'nota_3': nota_3,
                    'nota_4': nota_4,
                    'media': media
                }
            
            # Calcula a média final considerando os quatro bimestres.
            media_final = round(somatorio_medias / 4, 2)

            # Armazena a média final no cadastro do aluno.
            aluno['media_final'] = media_final

            # Define automaticamente a situação do aluno com base na média mínima.
            aluno['status'] = 'Aprovado' if  media_final >= MEDIA_MINIMA else 'Reprovado'

            # Adiciona o aluno completo à lista principal de alunos cadastrados.
            alunos.append(aluno)

            # Exibe mensagem de confirmação do cadastro.
            print(f"\nAluno [{nome}] cadastrado com sucesso!")

        else:
            print(f"[{nome}] já está cadastrado.")
        
        # Aguarda confirmação antes de retornar ao menu.
        input("\nPressione ENTER para voltar ao menu.")