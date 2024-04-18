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
        utils.mostrarMenu("Menu livros", ["Adicionar", "Listar", "Editar", "Apagar", "Pequisar", "Voltar"])
        op = utils.lerNumero("")

        if op == 6:
            break
        if op == 1:
            adicionar()
        if op == 2:
            listar()
        if op == 3:
            editar()
        if op == 4:
            apagar()
        if op == 5:
            pesquisar()

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
    """Pesquisa o dicionario com o id fornecido e devolve o livro ou None"""

    for livro in livros:
        if livro['id'] == id:
            return livro
    return None


def editar():
    id = utils.lerNumero("Qual o ID do livro que quer editar?: ")
    livro = getLivro(id)

    if livro is None:
        print("Não existe nenhum livro com o ID indicado")
        return

    print(livro)
    print("-" * 40)

    paraNaoEditar = ["id", "nEmprestimos", "leitor"]

    for campo, valor in livro.items():
        if campo in paraNaoEditar:
            continue

        print(valor)

        if campo == "ano":
            novo = utils.lerNumero(f"Novo {campo} ou enter para não alterar: ")
        else:
            novo = utils.lerTexto(f"Novo {campo} ou enter para não alterar: ")

        if novo != "":
            livro[campo] = novo


def apagar():
    id = utils.lerNumero("Qual o ID do livro para apagar?: ")

    livro = getLivro(id)

    if livro is None:
        print("Não existe o livro com o ID indicado")

    if livro['estado'] != "disponivel" or livro['estado'] != "disponível":
        print("So pode apagar o livro em que o estado é disponível")
        return
    
    op = print(f"Quer remover o livro {livro['nome']}? S/N: ")

    if op != "S" or op == "s":
        return
    
    livros.remove(livro)

    print("Livro removido com sucesso")


def pesquisar():
    utils.mostrarMenu("Escolha oque deseja pesquisar", ["Pelo nome", "Pelo autor", "Voltar"])
    op = input("")

    if op == 1:
        campo = "nome"

    if op == 2:
        campo = "autor"

    if op == 3:
        return
    
    pesquisa = utils.lerTexto(f"{campo} a pesquisar: ")

    for livro in livros:
        if pesquisa in livro[campo]:
            print(livro)
