#!/usr/bin/python3

# Lista que armazenará as tarefas.
# Cada tarefa será uma lista no formato:
# [descricao_da_tarefa, concluida]
#
# Exemplo:
# [
#     ["Estudar Python", False],
#     ["Fazer exercícios", True]
# ]
lista_tarefas = []

# Loop principal do programa
while True:
    print("\n* Controle de tarefas *")
    print("=======================")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Pesquisar tarefa")
    print("4. Remover tarefa")
    print("5. Alterar tarefa")
    print("6. Sair")

    # Leitura da opção escolhida pelo usuário
    opcao = input("\nEscolha uma opção: ")

    # Adicionar tarefa
    if opcao == '1': 

        # Permite adicionar várias tarefas seguidas
        while True:
            tarefa = input("Digite a tarefa (q para sair): ")

            # Sai do cadastro de tarefas
            if tarefa == 'q' or tarefa == 'Q': break

            # Adiciona a tarefa com status False
            # False = não concluída
            lista_tarefas.append([tarefa, False])
    
    # Lista tarefas
    elif opcao == '2':
        print("----------------------")
        print("*      Tarefas       *")
        print("----------------------")
        print("Status:        Tarefa:")
        print("-------        -------")

        # Percorre todas as tarefas cadastradas
        for tarefa in lista_tarefas:
            # Operador ternário:
            # Se tarefa[1] for True, mostra ✓
            # Caso contrário, mostra ✗
            status = "✓" if tarefa[1] else "✗"
            print(f"  {status}\t\t{tarefa[0]}")

        print("----------------------\n")

    # Pesquisar tarefa
    elif opcao == '3':
        # Variável para indicar se a tarefa foi encontrada
        encontrada = False

        # Solicita a tarefa que será pesquisada
        tarefa_pesquisa = input("\nDigite a tarefa que deseja pesquisar: ")

        # Percorre a lista procurando a tarefa
        for tarefa in lista_tarefas:
            # tarefa[0] contém a descrição da tarefa
            if tarefa_pesquisa == tarefa[0]:
                encontrada = True
                break

        # Exibe os dados da tarefa encontrada
        if encontrada:
            status = "✓" if tarefa[1] else "✗"
            print("\nStatus:        Tarefa:")
            print("-------        -------")
            print(f"  {status}\t\t{tarefa[0]}")
        else:
            print("\nTarefa não encotrada.")
        
    # Remover tarefa
    # Alterar tarefa
    # Sair do programa
    elif opcao == '6':
        print("\nSaindo do programa.")
        break
    
    # Caso seja informada uma opção não listada no menu
    else:
        print("Opção inválida!")



#lista_tarefas[0][1] = True
#print(lista_tarefas)


# Exemplo de acesso a uma tarefa:
#
# lista_tarefas[0]     -> primeira tarefa
# lista_tarefas[0][0]  -> descrição da primeira tarefa
# lista_tarefas[0][1]  -> status da primeira tarefa
#
# Exemplo:
#
# lista_tarefas = [
#     ["Estudar Python", False]
# ]
#
# lista_tarefas[0][0] -> "Estudar Python"
# lista_tarefas[0][1] -> False
    
