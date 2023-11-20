Vagas = 100
Mesas = 20

UserInput = 1 # 1 porque nao pode ser 0

while 1 and UserInput != 0:
    Selection = int(input("1 se entraram pessoas ou 2 se sairam pessoas ou 0 para fechar o programa: "))
    if Mesas <= 0:
        print("Já não existem mais mesas disponiveis")
    if Selection == 1:
        UserInput = int(input("Quantas Pessoas Entraram: "))
        Vagas = Vagas - UserInput
        Mesas = Mesas - 1
        print("Existem", Vagas, "vagas", "e existem", Mesas, "mesas disponiniveis")
    if Selection == 2:
        UserInput = int(input("Quantas Pessoas Sairam: "))
        Vagas = Vagas + UserInput
        Mesas = Mesas + 1
        print("Existem", Vagas, "vagas", "e existem", Mesas, "mesas disponiniveis")
    if Selection == 0:
        break