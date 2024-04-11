"""
Leitores
"""

import utils

leitores = []

exemploLeitores = [
    {'id': 1, 'nome': 'Pessoa1', 'email': 'nsei@yes.com'}
]

def menuLeitores():
    while True:
        utils.mostrarMenu("Menu leitores", ["Adicionar", "Listar", "Editar", "Apagar", "Voltar"])
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


