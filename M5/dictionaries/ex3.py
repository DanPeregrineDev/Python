"""
    Jogo de dados em Python. Crie um programa onde 4 jogadores joguem um jogo de dados.
    Cada jogador lança o dado 6 vezes e o programa deve guardar os resultados num dicionário
    em que o nome do jogador é a chave. No final o programa deve indicar quem ganhou o jogo que
    corresponde ao jogador com o total de valores mais elevado. O valor do lançamento do dado deve
    ser simulado com a library random.
"""

import random

def lancarDado():
    a = [0, 0, 0, 0, 0, 0]
    for i in range(6):
        a[i] = random.randint(1, 6)

    return a

def somarResultado(jogador):
    soma = 0
    for i in jogador:
        soma = soma + i
    
    return soma

resultados = {'Jogador1': 0, 'Jogador2': 0, 'Jogador3': 0, 'Jogador4': 0}

resultados['Jogador1'] = lancarDado()
resultados['Jogador2'] = lancarDado()
resultados['Jogador3'] = lancarDado()
resultados['Jogador4'] = lancarDado()

print(f"O Jogador 1 lançou os dados e calharam os seguintes numeros: {resultados['Jogador1']}")
print(f"O Jogador 2 lançou os dados e calharam os seguintes numeros: {resultados['Jogador2']}")
print(f"O Jogador 3 lançou os dados e calharam os seguintes numeros: {resultados['Jogador3']}")
print(f"O Jogador 4 lançou os dados e calharam os seguintes numeros: {resultados['Jogador4']}")

t1 = somarResultado(resultados['Jogador1'])
t2 = somarResultado(resultados['Jogador2'])
t3 = somarResultado(resultados['Jogador3'])
t4 = somarResultado(resultados['Jogador4'])

print("")
if t2 > t1 and t2 > t3 and t2 > t4:
    print(f"O jogador 2 ganhou com uma pontuação de {t2}")
elif t3 > t1 and t3 > t2 and t3 > t4:
    print(f"O jogador 3 ganhou com uma pontuação de {t3}")
elif t4 > t1 and t4 > t2 and t4 > t3:
    print(f"O jogador 4 ganhou com uma pontuação de {t4}")
else:
    print(f"O jogador 1 ganhou com uma pontuação de {t1}")