#!/usr/bin/python3 

"""
Sistema de Produtos

Este programa permite cadastrar e listar produtos utilizando
uma lista de tuplas.

Estrutura utilizada:

produtos = [
    (código, nome, categoria, preço)
]

Cada produto é armazenado como uma tupla, pois seus dados
são tratados como um registro fixo.
"""

# Lista principal que armazenará todos os produtos cadastrados.
# Cada item da lista será uma tupla contendo:
# (código do produto, nome, categoria, preço)
produtos = []

# Laço principal do programa.
# O sistema continuará executando até que o usuário escolha a opção de saída.
while True:
    # Exibe o menu principal do sistema.
    print("========== Sistema de Produtos ==========")
    print("-----------------------------------------")

    print("\n1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Sair")

    # Recebe a opção escolhida pelo usuário.
    opcao = input("\nEscola uma opção: ")

    if opcao == "1":
        # Solicita os dados do novo produto.
        cod_produto = input("\nCódigo do produto: ")
        nome_produto = input("Nome do produto: ")
        categoria_produto = input("Categoria do produto: ")
        preco_produto = input("Preço do produto: ")

        # Cria uma tupla contendo os dados do produto.
        #
        # Exemplo:
        # ("001", "Notebook", "Informática", "3500")
        #
        # A tupla representa um registro de produto.
        produto = (cod_produto, nome_produto, categoria_produto, preco_produto)

        # Adiciona a tupla criada dentro da lista de produtos.
        produtos.append(produto)

    # -------------------------------------------------
    # OPÇÃO 2 - LISTAR PRODUTOS
    # -------------------------------------------------
    elif opcao == "2":
        # Verifica se existe pelo menos um produto cadastrado.
        if len(produtos) != 0:
            # Percorre a lista de produtos.
            # Cada elemento retornado será uma tupla.
            for produto in produtos:
                print("\n*** Produtos ***")
                print("-----------------")

                # Acessa os valores da tupla através dos índices:
                #
                # produto[0] -> código
                # produto[1] -> nome
                # produto[2] -> categoria
                # produto[3] -> preço
                print(f"\nCódigo    : {produto[0]}")
                print(f"Nome      : {produto[1]}")
                print(f"Cateegoria: {produto[2]}")
                print(f"Preço     : {produto[3]}\n")

        # Caso a lista esteja vazia.
        else:
            print("\nNão há produto cadastrado.\n")

    # -------------------------------------------------
    # OPÇÃO 3 - SAIR DO SISTEMA
    # -------------------------------------------------
    elif opcao == "3":
        print("Saindo do programa...\n")

        # Encerra o laço while.
        break
    
    # -------------------------------------------------
    # OPÇÃO INVÁLIDA
    # -------------------------------------------------
    else:
        print("\nOpção inválida")
    