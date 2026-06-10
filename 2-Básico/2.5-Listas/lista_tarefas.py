#!/usr/bin/python3

lista_tarefas = []

while True:
    tarefa = input("Digite a tarefa (q para sair): ")
    if tarefa == 'q' or tarefa == 'Q': break
    lista_tarefas.append([tarefa, False])


lista_tarefas[0][1] = True
print(lista_tarefas)


for tarefa in lista_tarefas:
    # valor_se_verdadeiro if condicao else valor_se_falso
    status = "✓" if tarefa[1] else "✗"
    print(f"{status} {tarefa[0]}")
