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
    print("5. Editar tarefa")
    print("6. Marcar tarefa como concluída")
    print("0. Sair")

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
        if len(lista_tarefas) != 0:
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
        # Executado quando não existem tarefas cadastradas.
        else:
            print("\nA lista está vazia.")

    # Pesquisar tarefa
    elif opcao == '3':
        if len(lista_tarefas) != 0:
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
                print("\nTarefa não encontrada.")
        # Executado quando não existem tarefas cadastradas.
        else:
            print("\nA lista está vazia.")

    # Remover tarefa
    elif opcao == '4':
        # Verifica se existe pelo menos uma tarefa cadastrada.
        # len(lista_tarefas) retorna a quantidade de tarefas na lista.
        if len(lista_tarefas) != 0:
            print("\n* Remover tarefa *")
            print("------------------")

            # Solicita ao usuário tarefa que será removida.
            tarefa_remover = input("Digite a tarefa que deseja remover: ")

            # Percorre a lista procurando a tarefa
            for tarefa in lista_tarefas:
                # tarefa[0] contém a descrição da tarefa
                # Compara a descrição atual com a informada pelo usuário.
                if tarefa[0] == tarefa_remover:
                    # Remove a sublista completa da lista de tarefas.
                    lista_tarefas.remove(tarefa)
                    print("\nTarefa removida com sucesso!")
                    break
        # Executado quando não existem tarefas cadastradas.
        else:
            print("\nA lista está vazia.")     

    # Editar tarefa
    elif opcao == '5':
        print("\nEm produção...")

    # Marca como concluída
    elif opcao == '6':
        # Verifica se existe pelo menos uma tarefa cadastrada.
        # len(lista_tarefas) retorna a quantidade de tarefas na lista.
        if len(lista_tarefas) != 0:
            print("\n* Concuir tarefa *")
            print("------------------")
            tarefa_concluir = input("Digite a tarefa que deseja concluir: ")
        # Executado quando não existem tarefas cadastradas.
        else:
            print("\nA lista está vazia.") 

    # Sair do programa
    elif opcao == '0':
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
    
