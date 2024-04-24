import utils
import config
import app
import datetime

def checkInMenu(rooms):
    utils.showMenu("Check-In", ["1 Pessoa", "2 Pessoas", "3 Pessoas", "4 Pessoas", "Suite", "Voltar"])

    option = utils.askOption(6)

    if option == 1:
        assignRoom(1, rooms)
    if option == 2:
        assignRoom(2, rooms)
    if option == 3:
        assignRoom(3, rooms)
    if option == 4:
        assignRoom(4, rooms)
    if option == 5:
        assignRoom(5, rooms)
    if option == 6:
        app.mainMenu()


def assignRoom(roomType, rooms):
    """
        roomType - 1 = singleRoom | 2 = doubleRoom...etc | for suites use 5
        function will return room number
    """
    ocupantes = []

    noites = utils.askNumber("Quantas noites?: ")

    checkOutDate = datetime.datetime.now() + datetime.timedelta(days=noites)

    for room in rooms:
        if room['roomType'] == 'singleRoom' and roomType == 1:
            ocupante = input("Nome do ocupante: ")

            room['status'] = 'ocupado'
            room['cleaned'] = 'ocupado'
            room['ocupants'] = ocupante
            room['checkInDate'] = datetime.datetime.now()
            room['checkOutDate'] = checkOutDate
            return room['roomNumber']
        if room['roomType'] == 'doubleRoom' and roomType == 2:
            for i in range(2):
                t = input(f"Nome do {i + 1}º ocupante")
                
                ocupantes.append(t)

            room['status'] = 'ocupado'
            room['cleaned'] = 'ocupado'
            room['ocupants'] = ocupantes
            room['checkInDate'] = datetime.datetime.now()
            room['checkOutDate'] = checkOutDate
            return room['roomNumber']
        if room['roomType'] == 'tripleRoom' and roomType == 3:
            for i in range(3):
                t = input(f"Nome do {i + 1}º ocupante")
                
                ocupantes.append(t)

            room['status'] = 'ocupado'
            room['cleaned'] = 'ocupado'
            room['ocupants'] = ocupantes
            room['checkInDate'] = datetime.datetime.now()
            room['checkOutDate'] = checkOutDate
            return room['roomNumber']
        if room['roomType'] == 'quadripleRoom' and roomType == 4:
            for i in range(4):
                t = input(f"Nome do {i + 1}º ocupante")
                
                ocupantes.append(t)

            room['status'] = 'ocupado'
            room['cleaned'] = 'ocupado'
            room['ocupants'] = ocupantes
            room['checkInDate'] = datetime.datetime.now()
            room['checkOutDate'] = checkOutDate
            return room['roomNumber']
        if room['roomType'] == 'suite' and roomType == 5:
            nOcupants = utils.askNumber("Quantos ocupantes?: ")

            for i in range(nOcupants):
                t = input(f"Nome do {i + 1}º ocupante")
                
                ocupantes.append(t)

            room['status'] = 'ocupado'
            room['cleaned'] = 'ocupado'
            room['ocupants'] = ocupantes
            room['checkInDate'] = datetime.datetime.now()
            room['checkOutDate'] = checkOutDate
            return room['roomNumber']
        else:
            print("Nenhum quarto disponível")
