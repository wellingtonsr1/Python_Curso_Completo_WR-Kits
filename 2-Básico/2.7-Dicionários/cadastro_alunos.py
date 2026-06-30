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

# Calcula a média do bimestre atual.
def calcular_media_bimestre(n1, n2, n3, n4): 
    media = round((n1 + n2 + n3 + n4) / 4, 2)

    return media

# Exibe o cabeçalho da funcionalidade
def exibir_titutlo(texto):
    print("\n" + "=" * 40)
    print(f"             {texto}")
    print("=" * 40)

# Exibe as informações do Aluno
def exibir_detalhes_aluno(lista_alunos, nome=None, status=None):
    alunos = lista_alunos

    if nome:
        alunos = [
            aluno for aluno in lista_alunos 
            if aluno['nome'].lower() == nome.strip().lower()
        ]
    elif status:
        alunos = [
            aluno for aluno in lista_alunos 
            if aluno['status'].lower() == "Aprovado".lower()
        ]

    # Verifica se nenhum aluno foi encontrado
    if not alunos:
        print("\n      * Aluno não encontrado. *")
        return
    
    #Percorre cada aluno armazenado na lista
    for aluno in alunos:
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


#  Exibe todos os alunos cadastrados no sistema.
def listar_alunos():
    # Limpa a tela a cada chamada da função
    limpar_tela()

    # Exibe o cabeçalho da funcionalidade
    exibir_titutlo("LISTA DE ALUNOS")

    # # Verifica se existem alunos cadastrados
    if not alunos:
        print("    * Nenhum cadastro encontrado. *")
    else:
        exibir_detalhes_aluno(alunos, None, None)

    input("\nPressione ENTER para voltar ao menu.")

# Pesquisa um aluno pelo nome informado pelo usuário.
def pesquisar_aluno(): 
    # Limpa a tela a cada chamada da função 
    limpar_tela()

    # Exibe o cabeçalho da funcionalidade
    exibir_titutlo("PESQUISAR ALUNO")

    # Verifica se existem alunos cadastrados
    if not alunos:
        print("\n    * Nenhum cadastro encontrado. *")   
    else:
        # # Recebe o nome do aluno a ser procurado
        busca_aluno = input("Infome o aluno que deseja pesquisar: ").strip()
        
        exibir_detalhes_aluno(alunos, busca_aluno, None)
        
    input("\nPressione ENTER para voltar ao menu.")

# Remove um aluno cadastrado.
def remover_aluno():
    # Limpa a tela a cada chamada da função
    limpar_tela()

    # Exibe o cabeçalho da funcionalidade
    exibir_titutlo("REMOVER ALUNO")
    
    # Verifica se existem alunos cadastrados
    if not alunos:
        print("\n    * Nenhum cadastro encontrado. *")
    else:
        # Solicita o nome do aluno que será removido
        aluno_remover = input("Infome o aluno que deseja remover: ").strip()

        # Variável de controle para verificar se o aluno foi encontrado
        encontrado = False

        # Percorre a lista de alunos procurando pelo nome informado
        for aluno in alunos:
            # Verifica se o aluno atual corresponde ao aluno pesquisado
            if aluno['nome'].lower() == aluno_remover.lower():
                # Remove o dicionário do aluno encontrado da lista
                alunos.remove(aluno)

                # Exibe mensagem confirmando a exclusão
                print(f"\n* Aluno [{aluno['nome']}] removido com sucesso! *")

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
    exibir_titutlo("ALTERAR ALUNO")

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
    exibir_titutlo("EXIBIR APROVADOS")

    # Verifica se existem alunos cadastrados
    if not alunos:
        print("    * Nenhum cadastro encontrado. *")
    else:
        exibir_detalhes_aluno(alunos, None, True)

    # Aguarda o usuário pressionar ENTER antes de retornar ao menu
    input("\nPressione ENTER para voltar ao menu.")  

# Função principal
def main():
    # =========================================================
    # MENU PRINCIPAL (INTERFACE DO USUÁRIO)
    # =========================================================
    while True:
        # Limpa a tela a cada chamada da função
        limpar_tela()

        # Exibe o cabeçalho da funcionalidade
        exibir_titutlo("SISTEMA DE CADASTRO DE ALUNOS")

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

# Função que inicia o programa 
if __name__ == "__main__":
    main()