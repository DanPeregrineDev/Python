import utils
import app
import datetime

# installed package required
import termcolor

def checkInMenu(rooms, maxNights):
    utils.showMenu("Check-In", ["1 Pessoa", "2 Pessoas", "3 Pessoas", "4 Pessoas", "Suite", "Voltar"])

    option = utils.askOption(6)

    if option == 1:
        assignRoom(1, rooms, maxNights)
    if option == 2:
        assignRoom(2, rooms, maxNights)
    if option == 3:
        assignRoom(3, rooms, maxNights)
    if option == 4:
        assignRoom(4, rooms, maxNights)
    if option == 5:
        assignRoom(5, rooms, maxNights)
    if option == 6:
        app.mainMenu()


def assignRoom(roomType, rooms, maxNights):
    """
        roomType - 1 = singleRoom | 2 = doubleRoom...etc | for suites use 5
        function will return room number
    """
    ocupantes = []

    nights = utils.askNumber("Quantas noites? (deixe vazio para sair): ")

    if nights == None:
        app.mainMenu()

    while nights > maxNights:
        print("Numero máximo de noites exedido!")
        nights = utils.askNumber("Quantas noites? (deixe vazio para sair): ")

    checkOutDate = datetime.datetime.now() + datetime.timedelta(days=nights)

    for room in rooms:
        if room['roomType'] == 'singleRoom' and room['status'] == 'disponível' and roomType == 1:
            ocupante = input("Nome do ocupante: ")

            room['status'] = 'ocupado'
            room['cleaned'] = 'ocupado'
            room['occupants'] = ocupante
            room['nights'] = nights
            room['checkInDate'] = datetime.datetime.now().strftime("%H:%M / %d/%m/%Y")
            room['checkOutDate'] = checkOutDate.strftime("%H:%M / %d/%m/%Y")

            termcolor.cprint("CheckIn sucedido", 'green')
            
            return room['roomNumber']
        if room['roomType'] == 'doubleRoom' and room['status'] == 'disponível' and roomType == 2:
            for i in range(2):
                t = input(f"Nome do {i + 1}º ocupante: ")
                
                ocupantes.append(t)

            room['status'] = 'ocupado'
            room['cleaned'] = 'ocupado'
            room['occupants'] = ocupantes
            room['nights'] = nights
            room['checkInDate'] = datetime.datetime.now().strftime("%H:%M / %d/%m/%Y")
            room['checkOutDate'] = checkOutDate.strftime("%H:%M / %d/%m/%Y")

            termcolor.cprint("CheckIn sucedido", 'green')

            return room['roomNumber']
        if room['roomType'] == 'tripleRoom' and room['status'] == 'disponível' and roomType == 3:
            for i in range(3):
                t = input(f"Nome do {i + 1}º ocupante: ")
                
                ocupantes.append(t)

            room['status'] = 'ocupado'
            room['cleaned'] = 'ocupado'
            room['occupants'] = ocupantes
            room['nights'] = nights
            room['checkInDate'] = datetime.datetime.now().strftime("%H:%M / %d/%m/%Y")
            room['checkOutDate'] = checkOutDate.strftime("%H:%M / %d/%m/%Y")

            termcolor.cprint("CheckIn sucedido", 'green')

            return room['roomNumber']
        if room['roomType'] == 'quadripleRoom' and room['status'] == 'disponível' and roomType == 4:
            for i in range(4):
                t = input(f"Nome do {i + 1}º ocupante: ")
                
                ocupantes.append(t)

            room['status'] = 'ocupado'
            room['cleaned'] = 'ocupado'
            room['occupants'] = ocupantes
            room['nights'] = nights
            room['checkInDate'] = datetime.datetime.now().strftime("%H:%M / %d/%m/%Y")
            room['checkOutDate'] = checkOutDate.strftime("%H:%M / %d/%m/%Y")

            termcolor.cprint("CheckIn sucedido", 'green')

            return room['roomNumber']
        if room['roomType'] == 'suite' and room['status'] == 'disponível' and roomType == 5:
            noccupants = utils.askNumber("Quantos ocupantes?: ")

            for i in range(noccupants):
                t = input(f"Nome do {i + 1}º ocupante: ")
                
                ocupantes.append(t)

            room['status'] = 'ocupado'
            room['cleaned'] = 'ocupado'
            room['occupants'] = ocupantes
            room['nights'] = nights
            room['checkInDate'] = datetime.datetime.now().strftime("%H:%M / %d/%m/%Y")
            room['checkOutDate'] = checkOutDate.strftime("%H:%M / %d/%m/%Y")

            termcolor.cprint("CheckIn sucedido", 'green')

            return room['roomNumber']
        
    termcolor.cprint("Nenhum quarto disponível", 'red')
    app.mainMenu()