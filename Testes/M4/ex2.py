# Daniel Madeira

import numpy

def homogeneidade(saltos, atletas):
    menor = 300
    maior = 0

    for i in range(atletas):
        if saltos[i] > maior:
            maior = saltos[i]
    for i in range(atletas):
        if saltos[i] < menor:
            if saltos[i] != 0:
                menor = saltos[i]

    dif = maior - menor

    if dif < 50:
        a = "Inconstante"
    elif dif >= 50:
        a = "Constante"

    return a

def main():
    MAX_SALTOS = 100
    saltos = numpy.zeros(MAX_SALTOS, 'i')

    atletas = int(input("Numero de atletas que concorreram: "))

    nulos = 0
    
    for i in range(atletas):
        saltos[i] = int(input(f"Salto do {i + 1}º Atleta (Ex: 170): "))
        if saltos[i] == 0:
            nulos += 1

    mApuramento = int(input("Marca de apuramento: "))

    # Apurados

    apurados = " "

    for i in range(atletas):
        if saltos[i] > mApuramento:
            apurados += f"Nº{i + 1} "

    print(f"N de saltos nulos: {nulos}. \n Atletas apurados para a Final: {apurados}. \n Prova {homogeneidade(saltos, atletas)}")

if __name__ == "__main__":
    main()