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
        if op == 2:
            devolver()
        if op == 3:
            livrosEmprestados()
        if op == 4:
            leitoresComLivros()


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
    dataDevolucao = dataEmprestimo + datetime.timedelta(days=7)

    print(f"Tem de devolver o livro até {dataDevolucao.strftime("%d/%m/%Y")}")

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



def devolver():
    """Funcao para devolver o livro"""

    livros.listar()
    idLivro = utils.lerNumero("ID do livro: ")
    livro = livros.getLivro(idLivro)
    
    while livro is None:
        livros.listar()
        idLivro = utils.lerNumero("ID do livro: ")
        livro = livros.getLivro(idLivro)

    if livro['estado'] == "disponivel":
        print("Livro encontra-se disponivel")
        return
    
    for emprestimo in emprestimos:
        if emprestimo['livro'] == livro and emprestimo['estado'] == 'emprestado':
            if emprestimo['data_devolucao'] > datetime.datetime.now():
                print("Livro devolvido dentro do prazo")
            else:
                print("Livro devolvido fora do prazo")
            
            emprestimo['estado'] = 'concluido'
            livro['estado'] = 'disponivel'
            
            livro['leitor'] = None
            
            return

    print("OS DADOS DA APLICACAO ESTAO CORROMPIDOS")


def livrosEmprestados():
    for livro in livros.livros:
        if livro['estado'] == 'emprestado':
            print("-" * 40)
            print(f"Id: {livro['id']} | Nome: {livro['nome']} | Autor: {livro['autor']} | Ano: {livro['ano']} | Estado: {livro['estado']}")



def leitoresComLivros():
    for livro in livros.livros:
        if livro['estado'] == 'emprestado':
            print(livro['leitor'])