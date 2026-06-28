#!/usr/bin/python3

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

# Realiza o cadastro de um novo aluno.
def adicionar_aluno():  
    while True:
        # Cria um novo dicionário para cada aluno cadastrado.
        # Isso evita sobrescrever registros anteriores.
        cadastro_aluno = {}

        print("\n" + "=" * 40)
        print("              CADASTRAR")
        print("=" * 40)
        print("    *** Digite 'q' pra sair... ***\n")

        # Entrada do nome do aluno
        nome = input("Informe o nome do aluno: ").strip()

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
        cadastro_aluno = {
            'nome': nome,
            'nota_1': nota_1,
            'nota_2': nota_2,
            'nota_3': nota_3,
            'nota_4': nota_4,
            'media': media,
            'status': status
        }

        # Adiciona o aluno na lista principal
        alunos.append(cadastro_aluno)
 
#  Exibe todos os alunos cadastrados no sistema.
def listar_alunos():
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

    input("\nPressione ENTER para voltar ao menu")

# Pesquisa um aluno pelo nome informado pelo usuário.
def pesquisar_aluno():   
    print("\n" + "=" * 40)
    print("             PESQUISAR ALUNO")
    print("=" * 40)

    # Recebe o nome do aluno a ser procurado
    busca_aluno = input("Infome o aluno que deseja pesquisar: ").strip()
    
    if not alunos:
        print("    * Nenhum cadastro encontrado. *")
    else:
        encontrado = False

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

    input("\nPressione ENTER para voltar ao menu")

# Remove um aluno cadastrado.
def remover_aluno():
    print("\n" + "=" * 40)
    print("             REMOVER ALUNO")
    print("=" * 40)
    
    aluno_remover = input("Infome o aluno que deseja pesquisar: ").strip()

    encontrado = False

    for aluno in alunos:
        if aluno['nome'] == aluno_remover:
            alunos.remove(aluno)
            print(f"\n* Aluno '{aluno['nome']}' removido com sucesso! *")
            encontrado = True
            break
    
    if not encontrado:
        print("\n      * Aluno não encontrado. *")

    input("\nPressione ENTER para voltar ao menu")

# Permite alterar informações de um aluno.
def alterar_aluno():
    print("\n" + "=" * 40)
    print("             ALTERAR ALUNO")
    print("=" * 40)
    
    aluno_alterar = input("Infome o aluno que deseja alterar: ").strip()

    for aluno in alunos:
        if aluno['nome'] == aluno_alterar:
            n_nome = input(f"Informe o novo nome do aluno [{aluno['nome']}]: ").split()
            n_nota_1 = float(input(f"Infome a nova nota 1 [{aluno['nota_1']}]: "))
            n_nota_2 = float(input(f"Infome a nova nota 2 [{aluno['nota_2']}]: "))
            n_nota_3 = float(input(f"Infome a nova nota 3 [{aluno['nota_3']}]: "))
            n_nota_4 = float(input(f"Infome a nova nota 4 [{aluno['nota_4']}]: "))
    
            # Faz o cálculo da média
            media = (n_nota_1 + n_nota_2 + n_nota_3 + n_nota_4) / 4

            # Faz a verificação, com base na média, se o aluno está aprovado ou não
            status = 'Aprovado' if  media >= MEDIA_MINIMA else 'Reprovado'

            aluno = {
                'nome': n_nome,
                'nota_1': n_nota_1,
                'nota_2': n_nota_2,
                'nota_3': n_nota_3,
                'nota_4': n_nota_4,
                'media': media,
                'status': status
            }
        
    alunos.append(aluno)


# Exibe alunos que atingiram média mínima.
def exibir_alunos_aprovados():
    print("\n" + "=" * 40)
    print("             EXIBIR APROVADOS")
    print("=" * 40)
    
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

        if not encontrado:
            print("\n    * Nenhum aluno aprovado encontrado")

    input("\nPressione ENTER para voltar ao menu")  

# =========================================================
# MENU PRINCIPAL (INTERFACE DO USUÁRIO)
# =========================================================
while True:
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
        input("\nPressione ENTER para voltar ao menu") 
