# Programa para sugerir a loja onde um cabaz de produtos é mais barato
# O utilizador insere um cabaz de produtos a comprar
# Se não existirem todos os produtos a comprar deve informar o utilizador

precos = {
    "Pingo Doce": {"Arroz": 1.18, "Maçã": 2.85, "Leite": 0.82, "Frango": 4.98, "Café": 22.9, "Água5l": 1.29, "Azeite": 9.90, "Sal grosso": 0.25, "Açucar": 7.30, "Salmão": 12.99},
    "Auchan": {"Frango":2.34,"Arroz":1.05,"Maçã":1.59,"Leite":0.80,"Azeite":12.68,"Água5l":1.05,"Água6l":0.84,"Sal grosso":2.29,"Salmão":24.93,"Açucar":1.79,"Café":6.59},
    "Continente": {"Arroz":1.83,"Maçã":1.99,"Leite":0.82,"Frango":1.25,"Café":6.59,"Água5l":1.05,"Água6l":0.84}
}

compras = {}

def lerCompras(compras):
    
    while True:

        print("")
        produto = input("Escreva o nome do produto (Deixe em branco para terminar): ").capitalize()

        if produto == "":
            break

        quantidade = int(input("Escreva a quantidade do produto: "))

        while quantidade < 0:
            print("")
            print("A quantidade não pode ser menor que 1!")
            quantidade = int(input("Escreva a quantidade do produto: "))

        for i in precos.values():
            for j in i.keys():
                if j == produto:
                    if produto in compras:
                        compras[produto] += quantidade
                        lerCompras(compras)
                    else:
                        compras[produto] = quantidade
                        lerCompras(compras)
                    

        print("")
        print("Produto não encontrado!")


    return compras


def maisBarato(produtos):
    
    totalPingoDoce = 0
    totalAuchan = 0
    totalContinente = 0

    supermercadoPos = 0

    for produto in produtos.keys():
        for i in precos.values():
            supermercadoPos += 1
            for chave, valor in i.items():
                if chave == produto:

                    if supermercadoPos == 1:
                        totalPingoDoce += valor

                    elif supermercadoPos == 2:
                        totalAuchan += valor

                    elif supermercadoPos == 3:
                        totalContinente += valor

    lojaMaisBarata = None
    if totalPingoDoce > lojaMaisBarata:
        lojaMaisBarata = totalPingoDoce

    print(produtos)
    print(totalPingoDoce, totalAuchan, totalContinente)


maisBarato(lerCompras(compras))