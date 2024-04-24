# Hotel Configuration

import app
import utils

availableRooms = {'singleRoom': 20, 'doubleRoom': 40, 'tripleRoom': 20, 'quadripleRoom': 15, 'suite': 5}
hotelPrices = {'singleRoom': 100, 'doubleRoom': 150, 'tripleRoom': 200, 'quadripleRoom': 250, 'suite': 400} # Per night
discount = 0 # 0%
currency = "€"

def configMenu():
    while True:
        utils.showMenu("Configuration Menu", ["Alterar quantidade de quartos", "Mudar Preços", "Alterar valor do desconto", "Mudar moeda", "Voltar"])

        option = utils.askOption(5)

        if option == 1:
            changeRoomQuantity()
        if option == 2:
            changePrices()
        if option == 3:
            changeDiscout()
        if option == 4:
            app.mainMenu()


def changeRoomQuantity():
    for room, ammount in availableRooms.items():
        print(f"Mudar quantidade de {room} | quantidade atual: {ammount}")

        newQuantity = utils.askNumber()

        if newQuantity == None:
            continue

        availableRooms[room] = newQuantity

    print("Valores autalizados: ")
    print(availableRooms)

    app.populateRooms()


def changePrices():
    for room, price in hotelPrices.items():
        print(f"Mudar preço de {room} | valor atual: {price}")

        newPrice = utils.askNumber()

        if newPrice == None:
            continue

        hotelPrices[room] = newPrice

    print("Valores atualizados: ")
    print(hotelPrices)


def changeDiscout():
    global discount

    print(f"Mudar percentagem do desconto | Atual: {discount}%")

    newDiscount = utils.askNumber()

    if newDiscount == None:
        configMenu()

    discount = newDiscount

    print("Desconto alterado com sucesso")

    configMenu()


def listPrices():
    for room, price in hotelPrices.items():
        print(f"{room} - {price}€")