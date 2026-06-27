# # #!/usr/bin/python3

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

nome = input("Informe o nome: ")
sobrenome = input("Informe o sobrenome: ")
idade = input("Informe a idade: ")
cidade = input("Informe a cidade: ")

info = {
    'nome': nome,
    'sobrenome': sobrenome,
    'idade': idade,
    'cidade': cidade
}

print(f"Antes: {info}")

# #Assim, trata também espaços: Entrada: "     " não deve ser considerado um nome válido.

# Recebe os dados
n_nome = input("Informe o novo nome: ").strip()
n_sobrenome = input("Informe o novo sobrenome: ").strip()
n_idade = input("Informe a nova idade: ").strip()
n_cidade = input("Informe a nova cidade: ").strip()

# Atualiza, caso não for vazio.
if n_nome: info['nome'] = n_nome
if n_sobrenome: info['nome'] = n_sobrenome
if n_idade: info['idade'] = n_idade
if n_cidade: info['cidade'] = n_cidade

# Exibe os novos dados em uma linha.
print(f"Depois: {info}")

# Exibe os novos dados em várias linhas.
print(f"Nome: {info['nome']}")
print(f"Sobrenome: {info['sobrenome']}")
print(f"Idade: {info['idade']}")
print(f"Cidade: {info['cidade']}")

# print(bool(""))
# print(bool("joão"))

# o 'pop' remove e retorna quem foi removido.
removido = info.pop('nome')

print(f"{removido} foi removido com sucesso!")

# o 'del' apenas remove sem retornar quem foi removido.
del info['idade']

print(info)