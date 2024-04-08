"""
Livros
"""

import utils

livros = []

exemploLivros = [
    {'id': 1, 'nome': 'Livro1', 'autor': 'boogabooga', 'ano': 2000, 'editora': 'nsei', 'estado': 'disponivel', 'leitor': None, 'nEmprestimos': 0},
    {'id': 2, 'nome': 'Livro2', 'autor': 'oooo', 'ano': 2001, 'editora': 'nsei', 'estado': 'disponivel', 'leitor': None, 'nEmprestimos': 0},
    {'id': 3, 'nome': 'Livro3', 'autor': 'joe', 'ano': 1924, 'editora': 'nsei', 'estado': 'disponivel', 'leitor': None, 'nEmprestimos': 0}
]

def configurar():
    livros.extend(exemploLivros)

def menuLivros():
    while True:
        utils.mostrarMenu("Menu livros", ["Adicionar", "Listar", "Editar", "Apagar", "Voltar"])
        op = utils.lerNumero("")

        if op == 5:
            break
        if op == 1:
            pass
        if op == 2:
            pass
        if op == 3:
            pass
        if op == 4:
            pass