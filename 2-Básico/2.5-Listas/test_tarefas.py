#!/usr/bin/python3

import unittest


class TesteControleTarefas(unittest.TestCase):

    def setUp(self):
        """
        Executado antes de cada teste.
        Cria uma lista de tarefas de exemplo.
        """
        self.lista_tarefas = [
            ["Estudar Python", False],
            ["Fazer exercícios", True]
        ]

    def test_adicionar_tarefa(self):
        self.lista_tarefas.append(["Ler livro", False])

        self.assertEqual(len(self.lista_tarefas), 3)
        self.assertIn(["Ler livro", False], self.lista_tarefas)

    def test_pesquisar_tarefa_existente(self):
        encontrada = False

        for tarefa in self.lista_tarefas:
            if tarefa[0] == "Estudar Python":
                encontrada = True
                break

        self.assertTrue(encontrada)

    def test_pesquisar_tarefa_inexistente(self):
        encontrada = False

        for tarefa in self.lista_tarefas:
            if tarefa[0] == "Nadar":
                encontrada = True
                break

        self.assertFalse(encontrada)

    def test_remover_tarefa(self):
        for tarefa in self.lista_tarefas:
            if tarefa[0] == "Estudar Python":
                self.lista_tarefas.remove(tarefa)
                break

        self.assertNotIn(
            ["Estudar Python", False],
            self.lista_tarefas
        )

    def test_concluir_tarefa(self):
        for tarefa in self.lista_tarefas:
            if tarefa[0] == "Estudar Python":
                tarefa[1] = True
                break
            

        self.assertTrue(self.lista_tarefas[0][1])

    def test_tarefa_ja_concluida(self):
        for tarefa in self.lista_tarefas:
            if tarefa[0] == "Fazer exercícios":
                self.assertTrue(tarefa[1])

    def test_lista_vazia(self):
        lista = []

        self.assertEqual(len(lista), 0)

    def test_quantidade_tarefas(self):
        self.assertEqual(len(self.lista_tarefas), 2)


if __name__ == "__main__":
    unittest.main()