# Daniel Madeira

import numpy


def perguntarJogos(jogos):

    # Perguntar quantos jogos durante a temporada

    nJogosJogados = int(input("Quantos jogos durante a temporada?: "))

    # Ciclo para percorrer o vetor "jogos" e preencher com os dados necessarios

    for l in range(nJogosJogados):
        local = input(f"Escreva o local do {l + 1}º jogo: ").capitalize()
        golos = int(input(f"Escreva a quantidade de golos do {l + 1}º jogo: "))
        while golos < 0:
            print("Valor não pode ser negativo")
            golos = int(input(f"Escreva a quantidade de golos do {l + 1}º jogo: "))

        # Aplicar os dados obtidos para o vetor

        jogos[l, 0] = local
        jogos[l, 1] = golos

    # Devolver a quantidade de jogos jogados

    return nJogosJogados


def maxGolos(jogos, nJogosJogados):

    # Percorrer o vetor à procura do maior numero de golos marcados

    maxGolos = 0
    maxGolosPos = 0

    for l in range(nJogosJogados):
        if jogos[l, 1] > maxGolos:

            # Atualizar o valor de maxGolos para o numero maximo encontrado de golos

            maxGolos = jogos[l, 1]
            maxGolosPos = l + 1

    dados = (maxGolos, maxGolosPos)

    return dados


def pJogadosEmCasa(jogos, nJogosJogados):
    
    nJogadosEmCasa = 0

    for l in range(nJogosJogados):
        if jogos[l, 0] == "Viseu":
            nJogadosEmCasa += 1

    p = (nJogadosEmCasa / nJogosJogados) * 100

    return p


def totalDeGolos(jogos, nJogosJogados):

    nTotal = 0

    for l in range(nJogosJogados):
        nTotal += jogos[l, 1]

    return nTotal


def main():

    # Cria um array de 2 dimenções para guardar a informação dos jogos

    MAX_JOGOS = 100
    jogos = numpy.zeros((MAX_JOGOS, 2), 'O')

    # Perguntar os jogos

    nJogosJogados = perguntarJogos(jogos)

    # Procurar o numero maximo de golos marcados num jogo

    dadosMaxGolos = maxGolos(jogos, nJogosJogados)

    maximoGolos, jornada = dadosMaxGolos

    # Calcular a percentagem de jogos jogados em casa

    percentagem = pJogadosEmCasa(jogos, nJogosJogados)

    # Calcular o total de golos marcados

    totalGolos = totalDeGolos(jogos, nJogosJogados)

    # Mostrar os dados

    print(f"O recorde de golos num jogo foi de {maximoGolos} golos, obtido na {jornada}ªjornada. {int(percentagem)}% dos jogos da temporada foram em casa. A equipa marcou {totalGolos} golos na totalidade.")

if __name__ == "__main__":
    main()