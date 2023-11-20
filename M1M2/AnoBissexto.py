AnoAtual = int(input("Escreva o ano atual: "))

if (AnoAtual % 4 == 0 and AnoAtual % 100 != 0) or AnoAtual % 400 == 0:
    print("Ano é bissexto")
else:
    print("Ano não é bissexto")