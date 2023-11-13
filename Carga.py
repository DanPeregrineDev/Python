Carga = 0
Limite = 10000

while True:
    print("1 - Carregar")
    print("2 - Descarregar")
    print("3 - Sair")
    print("Carga:", Carga)
    Selection = int(input(""))

    if Selection == 1:
        ParaCarregar = int(input("Quantos Kg para carregar: "))

        while ParaCarregar < 0 or ParaCarregar > Limite:
            ParaCarregar = int(input("Numero invalido, volte a escrever: "))

        if Carga + ParaCarregar > Limite:
            print("Ultrapaçou o limite de carga")
        elif Carga + ParaCarregar < Limite:
            Carga = Carga + ParaCarregar
    
    elif Selection == 2:
        ParaDescarregar = int(input("Quantos Kg para descarregar: "))

        while ParaDescarregar < 0:
            ParaDescarregar = int(input("Numero invalido, volte a escrever: "))

        while Carga < ParaDescarregar:
            ParaDescarregar = int(input("Numero para descarregar é superior a carga, volte a escrever: "))

        Carga = Carga - ParaDescarregar
        
    elif Selection == 3:
        break