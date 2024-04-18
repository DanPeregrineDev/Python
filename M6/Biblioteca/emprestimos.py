"""
Emprestimos
"""

import datetime
import utils
import leitores
import livros

emprestimos = []

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
    leitor = leitores.getLeitor(idLeitor)

    while leitor is None:
        leitores.listar()
        idLeitor = utils.lerNumero("ID do leitor: ")
        leitor = leitores.getLeitor(idLeitor)

    print(f"Emprestimo do livro {livro['nome']} ao leitor {leitor['nome']}")

    dataEmprestimo = datetime.datetime.now()
    dataDevolucao = (dataEmprestimo + datetime.timedelta(days=7)).strftime("%d/%m/%Y")

    print(f"Tem de devolver o livro até {dataDevolucao}")

    novo = {
        'livro': livro,
        'leitor': leitor,
        'data_emprestimo': dataEmprestimo,
        'data_devolucao': dataDevolucao,
        'estado': 'emprestado'
    }

    livro['estado'] = 'emprestado'
    livro['leitor'] = leitor

    emprestimos.append(novo)

    print("Emprestimo feito com sucesso")