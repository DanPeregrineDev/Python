"""
Emprestimos
"""

import datetime
import utils
import leitores
import livros

enprestimos = []

def menuEmprestimos():
    while True:
        utils.mostrarMenu("Menu empréstimos", ["Emprestar", "Devolver", "Livros emprestados", "Leitores com livros", "Voltar"])
        op = utils.lerNumero("")

        if op == 5:
            break
        if op == 1:
            emprestar()


def emprestar():
    """Funcao para registar o emprestimo de um livro"""

    livros.listar()
    idLivro = utils.lerNumero("ID do livro: ")
    livro = livros.getLivro(idLivro)
    
    while livro is None:
        livros.listar()
        idLivro = utils.lerNumero("ID do livro: ")
        livro = livros.getLivro(idLivro)

    if livro['estado'] != "disponivel":
        print("Livro indesponível")
        return

    leitores.listar()
    idLeitor = utils.lerNumero("ID do leitor: ")

    