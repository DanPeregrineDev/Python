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
            adicionar()
        if op == 2:
            listar()
        if op == 3:
            editar()
        if op == 4:
            apagar()

def adicionar():
    nome = utils.lerTexto("Nome do livro: ", 3)

    autor = utils.lerTexto("Nome do autor: ", 3)

    ano = utils.lerNumero("Ano de edição: ")

    editora = utils.lerTexto("Editora: ", 3)

    id = 1
    if len(livros) > 0:
        id = livros[len(livros) - 1]['id'] + 1

    novo = {
        'id': id,
        'nome': nome,
        'autor': autor,
        'ano': ano,
        'editora': editora,
        'estado': 'disponivel',
        'leitor': None,
        'nEmprestimos': 0
    }

    livros.append(novo)
    print(f"Livro adicionado com sucesso. Tem {len(livros)} livros.")


def listar():
    print("#" * 40)
    print("Lista de livros")
    print("#" * 40)
    for livro in livros:
        print(f"Id: {livro['id']} | Nome: {livro['nome']} | Autor: {livro['autor']} | Ano: {livro['ano']} | Estado: {livro['estado']}")
        print("-" * 40)

def getLivro(id):
    "Pesquisa o dicionario com o id fornecido e devolve o livro ou None"

    for livro in livros:
        if livro['id'] == id:
            return livro
    return None


def editar():
    pass


def apagar():
    pass