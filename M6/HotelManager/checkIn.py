import utils
import app
import datetime

# installed package required
import termcolor

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

    nights = utils.askNumber("Quantas noites? (deixe vazio para sair): ")

    if nights == None:
        app.mainMenu()

    while nights > app.maxNights:
        print("Numero máximo de noites exedido!")
        nights = utils.askNumber("Quantas noites? (deixe vazio para sair): ")

    checkOutDate = datetime.datetime.now() + datetime.timedelta(days=nights)

    for room in rooms:
        if room['roomType'] == 'singleRoom' and room['status'] == 'disponível' and roomType == 1:
            ocupante = input("Nome do ocupante: ")

            room['status'] = 'ocupado'
            room['cleaned'] = 'ocupado'
            room['ocupants'] = ocupante
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
            room['ocupants'] = ocupantes
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
            room['ocupants'] = ocupantes
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
            room['ocupants'] = ocupantes
            room['nights'] = nights
            room['checkInDate'] = datetime.datetime.now().strftime("%H:%M / %d/%m/%Y")
            room['checkOutDate'] = checkOutDate.strftime("%H:%M / %d/%m/%Y")

            termcolor.cprint("CheckIn sucedido", 'green')

            return room['roomNumber']
        if room['roomType'] == 'suite' and room['status'] == 'disponível' and roomType == 5:
            nOcupants = utils.askNumber("Quantos ocupantes?: ")

            for i in range(nOcupants):
                t = input(f"Nome do {i + 1}º ocupante: ")
                
                ocupantes.append(t)

            room['status'] = 'ocupado'
            room['cleaned'] = 'ocupado'
            room['ocupants'] = ocupantes
            room['nights'] = nights
            room['checkInDate'] = datetime.datetime.now().strftime("%H:%M / %d/%m/%Y")
            room['checkOutDate'] = checkOutDate.strftime("%H:%M / %d/%m/%Y")

            termcolor.cprint("CheckIn sucedido", 'green')

            return room['roomNumber']
        
    termcolor.cprint("Nenhum quarto disponível", 'red')
    app.mainMenu()