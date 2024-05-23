# Python
import os, pickle, termcolor

# Local
import utils, checkIn, checkOut, list, cleaning, config

ROOMS_FILE = './data/rooms.dat'
CONFIG_FILE = './data/config.dat'

def main():
    initialize()

    while True:
        option = utils.showMenu("Main Menu", ["Check-In", "Check-Out", "Listar quartos", "Limpezas", "Configurar", "Sair"])

        if option == 1:
            checkIn.main()
        elif option == 2:
            checkOut.main()
        elif option == 3:
            list.main()
        elif option == 4:
            cleaning.main()
        elif option == 5:
            config.main()
        elif option == 6:
            print("A fechar...")
            break


def initialize():
    # CONFIG file

    if os.path.exists(CONFIG_FILE) == False:
        termcolor.cprint("Ficheiro de configurações não encontrado", "light_yellow")
        termcolor.cprint("A criar configuração...", "light_green")

        availableRooms = {
            'singleRoom': utils.intInput("Numero de quartos para 1 pessoa: "),
            'doubleRoom': utils.intInput("Numero de quartos para 2 pessoas: "),
            'tripleRoom': utils.intInput("Numero de quartos para 3 pessoas: "),
            'quadripleRoom': utils.intInput("Numero de quartos para 4 pessoas: "),
            'suite': utils.intInput("Numero de suites (Será o mesmo numero de andares): ")
        }

        print("")

        roomPrices = {
            'singleRoom': utils.intInput("Preço do quarto para 1 pessoa: "),
            'doubleRoom': utils.intInput("Preço do quarto para 2 pessoas: "),
            'tripleRoom': utils.intInput("Preço do quarto para 3 pessoas: "),
            'quadripleRoom': utils.intInput("Preço do quarto para 4 pessoas: "),
            'suite': utils.intInput("Preço de uma suite: ")
        }

        print("")

        otherConfigurations = {
            'maxNights': utils.intInput("Numero máximo de noites: "),
            'discount': 0
        }

        with open(CONFIG_FILE, 'wb') as file:
            try:
                pickle.dump(availableRooms, file)           # Available Rooms
                pickle.dump(roomPrices, file)               # Room Prices
                pickle.dump(otherConfigurations, file)      # Other Configurations

                termcolor.cprint("Criado ficheiro de configurações com sucesso", "light_green")

            except:
                termcolor.cprint("ERRO ao criar ficheiro de configurações!")

    # ROOMS file

    if os.path.exists(ROOMS_FILE) == False:
        rooms = []

        with open(CONFIG_FILE, 'rb') as configFile:
            try:
                availableRooms = pickle.load(configFile)
            
            except:
                termcolor.cprint("ERRO ao ler ficheiro de configurações!")

        # Calculate the number of rooms

        nOfRooms = 0
        for i in availableRooms.values():
            nOfRooms = nOfRooms + i

        # Number of floors is defined by the number of suites

        nOfFloors = availableRooms['suite']

        # Rooms per floor

        singleRoomsPerFloor = availableRooms['singleRoom'] / nOfFloors
        doubleRoomsPerFloor = availableRooms['doubleRoom'] / nOfFloors
        tripleRoomsPerFloor = availableRooms['tripleRoom'] / nOfFloors
        quadripleRoomsPerFloor = availableRooms['quadripleRoom'] / nOfFloors
        suitesPerFloor = nOfFloors

        roomsPerFloor = int(singleRoomsPerFloor + doubleRoomsPerFloor + tripleRoomsPerFloor + quadripleRoomsPerFloor + suitesPerFloor)

        # Populate rooms

        for floor in range(1, nOfFloors + 1):
            for roomNumber in range(1, roomsPerFloor + 1):
                if roomNumber <= singleRoomsPerFloor:
                    roomType = 'singleRoom'

                elif roomNumber <= singleRoomsPerFloor + doubleRoomsPerFloor:
                    roomType = 'doubleRoom'

                elif roomNumber <= singleRoomsPerFloor + doubleRoomsPerFloor + tripleRoomsPerFloor:
                    roomType = 'tripleRoom'

                elif roomNumber <= singleRoomsPerFloor + doubleRoomsPerFloor + tripleRoomsPerFloor + quadripleRoomsPerFloor:
                    roomType = 'quadripleRoom'
                else:
                    roomType = 'suite'

                # If room number below 10 it would look like 19 for room number 9 floor 1. So we need to add an extra 0
                if roomNumber < 10:
                    roomNumber = "0" + f"{roomNumber}"
            
                room = {
                    'roomNumber': int(f"{floor}{roomNumber}"),
                    'floor': floor,
                    'roomType': roomType,
                    'status': 'disponível',
                    'cleaned': 'Sim',
                    'occupants': None,
                    'nights': None,
                    'checkInDate': None,
                    'checkOutDate': None
                }

                rooms.append(room)

        # Save the rooms to the file

        with open(ROOMS_FILE, 'wb') as file:
            try:
                pickle.dump(rooms, file)
            
            except:
                termcolor.cprint("ERRO ao criar ficheiro dos quartos", "red")

if __name__ == "__main__":
    main()