"""
Leitores
"""

import utils

leitores = []

exemploLeitores = [
    {'id': 1, 'nome': 'Pessoa1', 'email': 'nsei@yes.com'},
    {'id': 2, 'nome': 'Jose', 'email': 'jose@gmail.com'},
    {'id': 3, 'nome': 'Miguel', 'email': 'miguel@gmail.com'}
]

def configurar():
    leitores.extend(exemploLeitores)


def menuLeitores():
    while True:
        utils.mostrarMenu("Menu leitores", ["Adicionar", "Listar", "Editar", "Apagar", "Voltar"])
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
    nome = utils.lerTexto("Nome do leitor: ", 3)

    email = utils.lerEmail("Email do leitor: ")

    id = 1
    if len(leitores) > 0:
        id = leitores[len(leitores) - 1]['id'] + 1
    
    novo = {
        'id': id,
        'nome': nome,
        'email': email
    }

    leitores.append(novo)
    print(f"Leitor adicionado com sucesso")


def listar():
    print("#" * 40)
    print("Lista de leitores")
    print("#" * 40)
    for leitor in leitores:
        print(f"Id: {leitor['id']} | Nome: {leitor['nome']} | Email: {leitor['email']}")
        print("-" * 40)


def editar():
    pass


def apagar():
    listar()
    
    id = int(input("ID: "))

    leitores.pop(id - 1)

    print("Apagado com sucesso")