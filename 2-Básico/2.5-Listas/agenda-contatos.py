#!/usr/bin/python3

# Definir a agenda de contatos como uma lista vazia
# Cada contato será representado como uma sublista contendo o nome, telefone e email
lista_contatos = [[], [], []]

while True:
    print("\n*** Agenda de Contatos ***")
    print("==========================")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Pesquisar contato")
    print("4. Remover contato")
    print("5. Alterar contato")
    print("6. Sair")
    opcao = input("\nEscolha uma opção: ")

    # Adicionar contato na agenda
    if opcao == '1': 
        print("Adicionando contato na agenda.")
        print("-------------------------------")
        while True:
            print("Digite as informações do contato: (ou 'q' para sair)")
            nome = input("Nome: ")
            if nome == 'q' or nome == 'Q': break # Verificar se o usuário deseja sair do loop
            telefone = input("Telefone: ")
            email = input("Email: ")

            lista_contatos[0].append(nome)      # Nome
            lista_contatos[1].append(telefone)  # Telefone
            lista_contatos[2].append(email)     # Email

    # Listar os contatos
    elif opcao == '2':  
        print("\nContatos na agenda:")
        print("-------------------------------")
        for i in range(len(lista_contatos[0])):
            print(f"Nome: {lista_contatos[0][i]}, Telefone: {lista_contatos[1][i]}, Email: {lista_contatos[2][i]}")
        print("-------------------------------")

    # Pesquisar contato na agenda
    elif opcao == '3': 
        print("Pesquisar contato na agenda.")
        print("-------------------------------")
        nome_pesquisa = input("Digite o nome do contato que deseja pesquisar: ")
        if nome_pesquisa in lista_contatos[0]:
            index = lista_contatos[0].index(nome_pesquisa)
            print(f"\nContato encontrado: Nome: {lista_contatos[0][index]}, Telefone: {lista_contatos[1][index]}, Email: {lista_contatos[2][index]}")
        else:
            print("Contato não encontrado.")
            
    # Remover contato da agenda
    elif opcao == '4': 
        print("\nRemover contato da agenda.")
        print("-------------------------------")
        nome_remover = input("Digite o nome do contato que deseja remover: ")
        if nome_remover in lista_contatos[0]:
            index = lista_contatos[0].index(nome_remover)
            del lista_contatos[0][index]  # Remover nome
            del lista_contatos[1][index]  # Remover telefone
            del lista_contatos[2][index]  # Remover email
            print("Contato removido com sucesso.\n")
        else:
            print("\nContato não encontrado.")


    # Alterar contato da agenda

    # Sair do programa
    elif opcao == '6':
        print("\nSaindo do programa.")
        break
