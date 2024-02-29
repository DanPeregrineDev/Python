"""
    Faça um programa que tenha uma função notas()
    que recebe várias notas de um aluno e retorna um dicionário
    com as seguintes informações:
    - Número de notas;
    - A melhor nota;
    - A pior nota;
    - A média das notas;
    - A situação: APROVADO se média maior ou igual a 10 e REPROVADO nos restantes casos.
"""

def notas(notas):
    dicionario = {}

    dicionario['Numero de notas'] = len(notas)
    dicionario['Melhor nota'] = max(notas)
    dicionario['Pior nota'] = min(notas)
    dicionario['Media das notas'] = sum(notas) / len(notas)

    if dicionario['Media das notas'] >= 10:
        dicionario['Situacao'] = "APROVADO"
    elif dicionario['Media das notas'] < 10:
        dicionario['Situacao'] = "REPROVADO"

    return dicionario

print(notas([1, 10, 12, 4, 9, 14]))