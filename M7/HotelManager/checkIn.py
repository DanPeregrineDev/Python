import datetime, termcolor, pickle
import utils

CONFIG_FILE = './data/config.dat'
ROOMS_FILE = './data/rooms.dat'
STATS_FILE = './data/stats.dat'

def main():
    option = utils.showMenu("Check-In", ["1 Pessoa", "2 Pessoas", "3 Pessoas", "4 Pessoas", "Suite", "Voltar"])

    if option == 1:
        assignRoom(1)
    elif option == 2:
        assignRoom(2)
    elif option == 3:
        assignRoom(3)
    elif option == 4:
        assignRoom(4)
    elif option == 5:
        assignRoom(5)
    elif option == 6:
        return


def assignRoom(roomType):
    # Load config file

    with open(CONFIG_FILE, 'rb') as configFile:
        try:
            availableRooms = pickle.load(configFile)
            roomPrices = pickle.load(configFile)
            otherConfigurations = pickle.load(configFile)

        except:
            termcolor.cprint("ERRO ao carregar ficheiro das configurações", "red")

    # Load rooms file

    with open(ROOMS_FILE, 'rb') as roomsFile:
        try:
            rooms = pickle.load(roomsFile)
        
        except:
            termcolor.cprint("ERRO ao carregar ficheiro dos quartos", "red")

    occupants = []

    nights = utils.intInput("Quantas noites?: ")

    while nights > otherConfigurations['maxNights']:
        termcolor.cprint("Numero de noites exedeu o máximo!", "light_yellow")
        nights = utils.intInput("Numero de noites: ")

    checkOutDate = datetime.datetime.now() + datetime.timedelta(days=nights)

    found = False

    for room in rooms:
        if room['roomType'] == 'singleRoom' and room['status'] == 'disponível' and roomType == 1:
            occupants = input("Nome do ocupante: ")

            room['status'] = 'ocupado'
            room['cleaned'] = 'ocupado'
            room['occupants'] = occupants
            room['nights'] = nights
            room['checkInDate'] = datetime.datetime.now().strftime("%H:%M / %d/%m/%Y")
            room['checkOutDate'] = checkOutDate.strftime("%H:%M / %d/%m/%Y")

            termcolor.cprint(f"CheckIn concluído no quarto {room['roomNumber']}", 'light_green')

            found = True

            break
            
        elif room['roomType'] == 'doubleRoom' and room['status'] == 'disponível' and roomType == 2:
            for i in range(2):
                t = input(f"Nome do {i + 1}º ocupante: ")
                occupants.append(t)

            print(occupants)

            room['status'] = 'ocupado'
            room['cleaned'] = 'ocupado'
            room['occupants'] = occupants
            room['nights'] = nights
            room['checkInDate'] = datetime.datetime.now().strftime("%H:%M / %d/%m/%Y")
            room['checkOutDate'] = checkOutDate.strftime("%H:%M / %d/%m/%Y")

            termcolor.cprint(f"CheckIn concluído no quarto {room['roomNumber']}", 'light_green')

            found = True

            break

        elif room['roomType'] == 'tripleRoom' and room['status'] == 'disponível' and roomType == 3:
            for i in range(3):
                t = input(f"Nome do {i + 1}º ocupante: ")
                
                occupants.append(t)

            room['status'] = 'ocupado'
            room['cleaned'] = 'ocupado'
            room['occupants'] = occupants
            room['nights'] = nights
            room['checkInDate'] = datetime.datetime.now().strftime("%H:%M / %d/%m/%Y")
            room['checkOutDate'] = checkOutDate.strftime("%H:%M / %d/%m/%Y")

            termcolor.cprint(f"CheckIn concluído no quarto {room['roomNumber']}", 'light_green')

            found = True

            break

        elif room['roomType'] == 'quadripleRoom' and room['status'] == 'disponível' and roomType == 4:
            for i in range(4):
                t = input(f"Nome do {i + 1}º ocupante: ")
                
                occupants.append(t)

            room['status'] = 'ocupado'
            room['cleaned'] = 'ocupado'
            room['occupants'] = occupants
            room['nights'] = nights
            room['checkInDate'] = datetime.datetime.now().strftime("%H:%M / %d/%m/%Y")
            room['checkOutDate'] = checkOutDate.strftime("%H:%M / %d/%m/%Y")

            termcolor.cprint(f"CheckIn concluído no quarto {room['roomNumber']}", 'light_green')

            found = True

            break

        elif room['roomType'] == 'suite' and room['status'] == 'disponível' and roomType == 5:
            noccupants = utils.intInput("Quantos ocupantes?: ")

            for i in range(noccupants):
                t = input(f"Nome do {i + 1}º ocupante: ")
                
                occupants.append(t)

            room['status'] = 'ocupado'
            room['cleaned'] = 'ocupado'
            room['occupants'] = occupants
            room['nights'] = nights
            room['checkInDate'] = datetime.datetime.now().strftime("%H:%M / %d/%m/%Y")
            room['checkOutDate'] = checkOutDate.strftime("%H:%M / %d/%m/%Y")

            termcolor.cprint(f"CheckIn concluído no quarto {room['roomNumber']}", 'light_green')

            found = True

            break

    if found == False:
        termcolor.cprint("Nenhum quarto disponível", 'red')

    # Save changes to rooms file

    with open(ROOMS_FILE, 'wb') as file:
        try:
            pickle.dump(rooms, file)

        except:
            termcolor.cprint("ERRO ao guardar alterações", "red")