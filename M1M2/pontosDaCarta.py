print("1 - Infração muito gráve")
print("2 - Infração gráve")
print("3 - Infração leve")

Pontos = 12

MG = 6
G = 4
L = 1

PrimeiraVez = True

while True:
    Selection = int(input("Selecione a opção: "))
    if Selection == 1:
        Pontos = Pontos - MG
        PrimeiraVez = False
    if Selection == 2:
        Pontos = Pontos - G
        PrimeiraVez = False
    if Selection == 3 and PrimeiraVez == False:
        Pontos = Pontos - 1
    print(Pontos)