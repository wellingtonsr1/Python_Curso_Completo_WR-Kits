#!/usr/bin/python3

# =========================================================
# VARIÁVEL GLOBAL DO SISTEMA
# =========================================================

# Lista principal responsável por armazenar todos os alunos
# cadastrados no sistema.
alunos = []

# =========================================================
# FUNÇÕES DO SISTEMA
# =========================================================

def adicionar_aluno():
    """
    Realiza o cadastro de um novo aluno.

    Processo:
        1. Solicita o nome do aluno.
        2. Solicita as quatro notas.
        3. Cria um dicionário contendo os dados.
        4. Adiciona o cadastro na lista global de alunos.

    O usuário pode digitar 'q' para sair do cadastro.
    """

    while True:
        # Cria um novo dicionário para cada aluno cadastrado.
        # Isso evita sobrescrever registros anteriores.
        cadastro_aluno = {}

        print("\n" + "=" * 40)
        print("              CADASTRAR")
        print("=" * 40)
        print("    *** Digite 'q' pra sair... ***\n")

        # Entrada do nome do aluno
        nome = input("Informe o nome do aluno: ")

        # Permite sair do cadastro
        if nome == 'q' or nome == 'Q': break

        # Entrada das notas convertidas para número decimal
        nota_1 = float(input("Informe a primeira nota: "))
        nota_2 = float(input("Informe a segunda nota: "))
        nota_3 = float(input("Informe a terceira nota: "))
        nota_4 = float(input("Informe a quarta nota: "))

        # Armazena os dados do aluno no dicionário
        cadastro_aluno['nome'] = nome
        cadastro_aluno['nota_1'] = nota_1
        cadastro_aluno['nota_2'] = nota_2
        cadastro_aluno['nota_3'] = nota_3
        cadastro_aluno['nota_4'] = nota_4

        # Adiciona o aluno na lista principal
        alunos.append(cadastro_aluno)
 

def listar_alunos():
    """
    Exibe todos os alunos cadastrados no sistema.

    Caso a lista esteja vazia, informa ao usuário
    que não existem registros.
    """

    print("\n" + "=" * 40)
    print("             LISTA DE ALUNOS")
    print("=" * 40)

    # Verifica se existem alunos cadastrados
    if not alunos:
        print("    * Nenhum cadastro encontrado. *")
    else:
        # Percorre cada aluno armazenado na lista
        for aluno in alunos:
            print(f"Aluno : {aluno['nome']}")
            print(f"Nota 1: {aluno['nota_1']}")
            print(f"Nota 2: {aluno['nota_2']}")
            print(f"Nota 3: {aluno['nota_3']}")
            print(f"Nota 4: {aluno['nota_4']}")
            
            print("-" * 40)

    input("\nPressione ENTER para voltar ao menu")

def pesquisar_aluno():
    """
    Pesquisa um aluno pelo nome informado pelo usuário.

    Funcionamento:
        - Percorre a lista de alunos.
        - Compara o nome pesquisado.
        - Exibe os dados caso encontre.
        - Informa caso o aluno não exista.

    A comparação ignora diferença entre letras
    maiúsculas e minúsculas.
    """
     
    print("\n" + "=" * 40)
    print("             PESQUISAR ALUNO")
    print("=" * 40)

    busca_aluno = input("Infome o aluno que deseja pesquisar: ")
    
    if not alunos:
        print("    * Nenhum cadastro encontrado. *")
    else:
        encontrado = False

        # Percorre todos os alunos cadastrados
        for aluno in alunos:
            # Compara os nomes ignorando maiúsculas/minúsculas
            if aluno['nome'].lower() == busca_aluno.lower():
                print(f"\nAluno : {aluno['nome']}")
                print(f"Nota 1: {aluno['nota_1']}")
                print(f"Nota 2: {aluno['nota_2']}")
                print(f"Nota 3: {aluno['nota_3']}")
                print(f"Nota 4: {aluno['nota_4']}")

                encontrado = True

        # Caso nenhum aluno seja localizado
        if not encontrado:
            print("\n      * Aluno não encontrado. *")

    input("\nPressione ENTER para voltar ao menu")

def remover_aluno():
    """
    Remove um aluno cadastrado.

    Função reservada para implementação futura.
    """

    print("\n" + "=" * 40)
    print("             REMOVER ALUNO")
    print("=" * 40)
    return 0

def alterar_aluno():
    """
    Permite alterar informações de um aluno.

    Função reservada para implementação futura.
    """

    print("\n" + "=" * 40)
    print("             ALTERAR ALUNO")
    print("=" * 40)
    return 0

def exibir_alunos_aprovados():
    """
    Exibe alunos que atingiram média mínima.

    Função reservada para implementação futura.
    """

    print("\n" + "=" * 40)
    print("             EXIBIR APROVADOS")
    print("=" * 40)
    return 0


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
        
    else:
        print("\nOpção inválida!")
        break