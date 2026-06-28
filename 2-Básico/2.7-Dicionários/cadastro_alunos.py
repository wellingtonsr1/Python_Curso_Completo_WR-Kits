#!/usr/bin/python3

# ==========================================================
# IMPORTAÇÃO DE MÓDULOS
# ==========================================================
import os

# =========================================================
# VARIÁVEL GLOBAL DO SISTEMA
# =========================================================

# Lista principal responsável por armazenar todos os alunos
# cadastrados no sistema.
alunos = []
MEDIA_MINIMA = 7.0

# =========================================================
# FUNÇÕES DO SISTEMA
# =========================================================

# Verifica se o nom informado já existe.
def existe_aluno(nome):
    #return any(aluno['nome'].lower() == nome.lower() for aluno in alunos)

    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower():
            return True
        
    return False

# Limpa a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Realiza o cadastro de um novo aluno.
def adicionar_aluno():  
    while True:
        # Limpa a tela a cada chamada da função
        limpar_tela()

        # Cria um novo dicionário para cada aluno cadastrado.
        # Isso evita sobrescrever registros anteriores.
        info_aluno = {}

        # Exibe o cabeçalho da funcionalidade
        print("\n" + "=" * 40)
        print("              CADASTRAR")
        print("=" * 40)
        print("    *** Digite 'q' pra sair... ***\n")

        # Entrada do nome do aluno
        nome = input("Informe o nome do aluno: ").strip()

        # Faz uma checagem se o nome informado já existe.
        if not existe_aluno(nome):
            # Permite sair do cadastro
            if nome.lower() == 'q': break

            # Entrada das notas convertidas para número decimal
            nota_1 = float(input("Informe a primeira nota: "))
            nota_2 = float(input("Informe a segunda nota: "))
            nota_3 = float(input("Informe a terceira nota: "))
            nota_4 = float(input("Informe a quarta nota: "))

            # Faz o cálculo da média
            media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

            # Faz a verificação, com base na média, se o aluno está aprovado ou não
            status = 'Aprovado' if  media >= MEDIA_MINIMA else 'Reprovado'

            # Armazena os dados do aluno no dicionário
            info_aluno = {
                'nome': nome,
                'nota_1': nota_1,
                'nota_2': nota_2,
                'nota_3': nota_3,
                'nota_4': nota_4,
                'media': media,
                'status': status
            }

            # Adiciona o aluno na lista principal
            alunos.append(info_aluno)

        else:
            print(f"[{nome}] já está cadastardo.")
            input("\nPressione ENTER para voltar ao menu.")

 
#  Exibe todos os alunos cadastrados no sistema.
def listar_alunos():
    # Limpa a tela a cada chamada da função
    limpar_tela()

    # Exibe o cabeçalho da funcionalidade
    print("\n" + "=" * 40)
    print("             LISTA DE ALUNOS")
    print("=" * 40)

    # Verifica se existem alunos cadastrados
    if not alunos:
        print("    * Nenhum cadastro encontrado. *")
    else:
        # Percorre cada aluno armazenado na lista
        for aluno in alunos:
            print(f"\nAluno...: {aluno['nome']}")
            print(f"Nota 1..: {aluno['nota_1']}")
            print(f"Nota 2..: {aluno['nota_2']}")
            print(f"Nota 3..: {aluno['nota_3']}")
            print(f"Nota 4..: {aluno['nota_4']}")
            print(f"Média...: {aluno['media']}")
            print(f"Situação: {aluno['status']}")
            print("-" * 40)

    input("\nPressione ENTER para voltar ao menu.")

# Pesquisa um aluno pelo nome informado pelo usuário.
def pesquisar_aluno(): 
    # Limpa a tela a cada chamada da função 
    limpar_tela()

    # Exibe o cabeçalho da funcionalidade
    print("\n" + "=" * 40)
    print("             PESQUISAR ALUNO")
    print("=" * 40)
    
    # Verifica se existem alunos cadastrados
    if not alunos:
        print("\n    * Nenhum cadastro encontrado. *")
    else:
        encontrado = False

        # Recebe o nome do aluno a ser procurado
        busca_aluno = input("Infome o aluno que deseja pesquisar: ").strip()

        # Percorre todos os alunos cadastrados
        for aluno in alunos:
            # Compara os nomes ignorando maiúsculas/minúsculas
            if aluno['nome'].lower() == busca_aluno.lower():
                print(f"\nAluno.....: {aluno['nome']}")
                print(f"Nota 1....: {aluno['nota_1']}")
                print(f"Nota 2....: {aluno['nota_2']}")
                print(f"Nota 3....: {aluno['nota_3']}")
                print(f"Nota 4....: {aluno['nota_4']}")
                print(f"Situação..: {aluno['status']}")

                encontrado = True

        # Caso nenhum aluno seja localizado
        if not encontrado:
            print("\n      * Aluno não encontrado. *")

    input("\nPressione ENTER para voltar ao menu.")

# Remove um aluno cadastrado.
def remover_aluno():
    # Limpa a tela a cada chamada da função
    limpar_tela()

    # Exibe o cabeçalho da funcionalidade
    print("\n" + "=" * 40)
    print("             REMOVER ALUNO")
    print("=" * 40)
    
    # Solicita o nome do aluno que será removido
    aluno_remover = input("Infome o aluno que deseja remover: ").strip()

     # Variável de controle para verificar se o aluno foi encontrado
    encontrado = False

    # Percorre a lista de alunos procurando pelo nome informado
    for aluno in alunos:
        # Verifica se o aluno atual corresponde ao aluno pesquisado
        if aluno['nome'] == aluno_remover:
            # Remove o dicionário do aluno encontrado da lista
            alunos.remove(aluno)

            # Exibe mensagem confirmando a exclusão
            print(f"\n* Aluno [ {aluno['nome']} ] removido com sucesso! *")

            # Indica que a remoção foi realizada
            encontrado = True

            # Encerra o laço após encontrar e remover o aluno
            break

    # Caso nenhum aluno tenha sido encontrado, informa o usuário
    if not encontrado:
        print("\n      * Aluno não encontrado. *")

    # Aguarda o usuário pressionar ENTER antes de retornar ao menu
    input("\nPressione ENTER para voltar ao menu.")

# Permite alterar informações de um aluno.
def alterar_aluno():
    # Limpa a tela a cada chamada da função
    limpar_tela()

    # Exibe o cabeçalho da funcionalidade
    print("\n" + "=" * 40)
    print("             ALTERAR ALUNO")
    print("=" * 40)
    
    # Verifica se existem alunos cadastrados
    if not alunos:
        print("\n    * Nenhum cadastro encontrado. *")
    else:
        encontrado = False

        # Solicita o nome do aluno que será alterado
        aluno_alterar = input("Infome o aluno que deseja alterar: ").strip()

        # Percorre a lista de alunos procurando o cadastro informado
        for aluno in alunos:
            # Verifica se o nome informado corresponde ao aluno cadastrado
            if aluno['nome'] == aluno_alterar:
                encontrado = True

                # Informa ao usuário que ENTER mantém o valor existente
                print("\n** [Tecle ENTER para manter o valor atual.] **")

                # Solicita os novos valores dos campos do aluno
                # Caso o campo seja deixado vazio, o valor atual será preservado
                entrada_n_nome = input(f"\nInforme o novo nome do aluno [{aluno['nome']}]: ")
                entrada_n_nota_1 = input(f"Infome a nova nota 1 [{aluno['nota_1']}]: ")
                entrada_n_nota_2 = input(f"Infome a nova nota 2 [{aluno['nota_2']}]: ")
                entrada_n_nota_3 = input(f"Infome a nova nota 3 [{aluno['nota_3']}]: ")
                entrada_n_nota_4 = input(f"Infome a nova nota 4 [{aluno['nota_4']}]: ")

                # Define os novos valores.
                # Se o usuário não informar um valor, mantém o dado atual.
                # No caso das notas, elas são convertida de str para float
                n_nome = entrada_n_nome if entrada_n_nome else aluno['nome']
                n_nota_1 = float(entrada_n_nota_1) if entrada_n_nota_1 else aluno['nota_1']
                n_nota_2 = float(entrada_n_nota_2) if entrada_n_nota_2 else aluno['nota_2']
                n_nota_3 = float(entrada_n_nota_3) if entrada_n_nota_3 else aluno['nota_3']
                n_nota_4 = float(entrada_n_nota_4) if entrada_n_nota_4 else aluno['nota_4']

                # Calcula novamente a média após a alteração das notas
                media = (n_nota_1 + n_nota_2 + n_nota_3 + n_nota_4) / 4

                # Atualiza a situação do aluno com base na média calculada
                status = 'Aprovado' if  media >= MEDIA_MINIMA else 'Reprovado'
                
                # Atualiza os dados do aluno no dicionário existente
                aluno["nome"] = n_nome
                aluno["nota_1"] = n_nota_1
                aluno["nota_2"] = n_nota_2
                aluno["nota_3"] = n_nota_3
                aluno["nota_4"] = n_nota_4
                aluno['media'] = media
                aluno['status'] = status

                # Informa, na tela, que o usuário foi removido
                print(f"\nCadastro do aluno [ {aluno['nome']} ] alterado com sucesso.")

    # Aguarda o usuário pressionar ENTER antes de retornar ao menu
    input("\nPressione ENTER para voltar ao menu.")

# Exibe alunos que atingiram média mínima.
def exibir_alunos_aprovados():
    # Limpa a tela a cada chamada da função
    limpar_tela()

    # Exibe o cabeçalho da funcionalidade
    print("\n" + "=" * 40)
    print("             EXIBIR APROVADOS")
    print("=" * 40)
    
    # Verifica se existem alunos cadastrados
    if not alunos:
        print("    * Nenhum cadastro encontrado. *")
    else:
        encontrado = False

        # Percorre todos os alunos cadastrados
        for aluno in alunos:
            if aluno['status'] == 'Aprovado':
                print(f"Aluno.....: {aluno['nome']}")
                print(f"Nota 1....: {aluno['nota_1']}")
                print(f"Nota 2....: {aluno['nota_2']}")
                print(f"Nota 3....: {aluno['nota_3']}")
                print(f"Nota 4....: {aluno['nota_4']}")
                print(f"Média.....: {aluno['media']}")
                print(f"Situação..: {aluno['status']}")
                print("-" * 40)

                encontrado = True

        # Exibe uma mensagem, na tela, informando que não há alunos aprovados.
        if not encontrado:
            print("\n    * Nenhum aluno aprovado encontrado")

    # Aguarda o usuário pressionar ENTER antes de retornar ao menu
    input("\nPressione ENTER para voltar ao menu.")  

# =========================================================
# MENU PRINCIPAL (INTERFACE DO USUÁRIO)
# =========================================================
while True:
    # Limpa a tela a cada chamada da função
    limpar_tela()

    # Exibe o cabeçalho da funcionalidade
    print("\n" + "=" * 40)
    print("      SISTEMA DE CADASTRO DE ALUNOS")
    print("=" * 40)

    print("\n[1] Adicionar aluno")
    print("[2] Listar alunos")
    print("[3] Pesquisar aluno")
    print("[4] Remover aluno")
    print("[5] Alterar aluno")
    print("[6] Exibir alunos aprovados")

    print("\n[0] Sair")
    print("=" * 40)

    opcao = input("\nEscolha uma opção: ")

    # Controle das opções escolhidas pelo usuário
    if opcao == '1':
        adicionar_aluno()

    elif opcao == '2':
        listar_alunos()
        
    elif opcao == '3':
        pesquisar_aluno()
        
    elif opcao == '4':
        remover_aluno()
        
    elif opcao == '5':
        alterar_aluno()
        
    elif opcao == '6':
        exibir_alunos_aprovados()

    elif opcao == '0':
        print("\nSaindo...")
        break
        
    else:
        print("\nOpção inválida! Tente novamente.") 

        # Aguarda o usuário pressionar ENTER antes de retornar ao menu
        input("\nPressione ENTER para voltar ao menu.") 
