"""
Trabalho Modelo - Modulo 6
--------------------------
Um programa para ajudar a gerir os livros e emprestimos de uma biblioteca
Requesitos:
    Gestao de livros (CRUD)
    Gestao de leitores (CRUD)
    Emprestimos/devoluções
    Estatisticas (top livro, top mes, top leitores)
"""

import utils
import livros
import leitores
import emprestimos

DEBUG = True

def menuPrincipal():
    while True:
        utils.mostrarMenu("Menu Principal", ["Livros", "Leitores", "Empréstimos e devoluções", "Estatisticas", "Sair"])
        op = utils.lerNumero("")

        if op == 5:
            break
        elif op == 1:
            livros.menuLivros()
        elif op == 2:
            leitores.menuLeitores()
        elif op == 3:
            emprestimos.menuEmprestimos()
        elif op == 4:
            pass


def main():
    if DEBUG:
        livros.configurar()
        leitores.configurar()
    menuPrincipal()

if __name__ == "__main__":
    main()