import utils
import config
import checkIn
import checkOut

rooms = []

def mainMenu():

    while True:
        utils.showMenu("Menu", ["Check-in", "Check-out", "Listar Quartos", "Configure", "Exit"])

        option = utils.askOption(5)

        if option == 1:
            checkIn.checkInMenu(rooms)
        if option == 2:
            checkOut.checkOutMenu(rooms)
        if option == 3:
            listMenu()
        if option == 4:
            config.configMenu()
        if option == 5:
            break


def populateRooms():
    # Calculate total of rooms

    totalRooms = 0
    for i in config.availableRooms.values():
        totalRooms = totalRooms + i

    # Number of floors is defined by the number of suites
    nFloors = config.availableRooms['suite']

    # Rooms per floor
    singleRoomPerFloor = config.availableRooms['singleRoom'] / nFloors
    doubleRoomPerFloor = config.availableRooms['doubleRoom'] / nFloors
    tripleRoomPerFloor = config.availableRooms['tripleRoom'] / nFloors
    quadripleRoomPerFloor = config.availableRooms['quadripleRoom'] / nFloors
    suitesPerFloor = nFloors

    roomsPerFloor = int(singleRoomPerFloor + doubleRoomPerFloor + tripleRoomPerFloor + quadripleRoomPerFloor + suitesPerFloor)

    # Populate Floors
    for floor in range(1, nFloors + 1):
        for roomNumber in range(1, roomsPerFloor + 1):
            if roomNumber <= singleRoomPerFloor:
                roomType = 'singleRoom'
            elif roomNumber <= singleRoomPerFloor + doubleRoomPerFloor:
                roomType = 'doubleRoom'
            elif roomNumber <= singleRoomPerFloor + doubleRoomPerFloor + tripleRoomPerFloor:
                roomType = 'tripleRoom'
            elif roomNumber <= singleRoomPerFloor + doubleRoomPerFloor + tripleRoomPerFloor + quadripleRoomPerFloor:
                roomType = 'quadripleRoom'
            else:
                roomType = 'suite'

            if roomNumber < 10:
                roomNumber = "0" + f"{roomNumber}"
            
            room = {
                'roomNumber': int(f"{floor}{roomNumber}"),
                'floor': floor,
                'roomType': roomType,
                'status': 'disponível',
                'cleaned': 'Sim',
                'ocupants': None,
                'checkInDate': None,
                'checkOutDate': None
            }

            rooms.append(room)


def listMenu():
    while True:
        utils.showMenu("Listar", ["Listar todos os quartos", "Listar quartos disponíveis", "Listar quartos ocupados", "Listar quartos por limpar", "Voltar"])

        option = utils.askOption(5)

        if option == 1:
            listAllRooms()
        if option == 2:
            listEmptyRooms()
        if option == 3:
            listOcupiedRooms()
        if option == 4:
            listToCleanRooms()
        if option == 5:
            mainMenu()


def listAllRooms():
    print("=" * 60)

    for room in rooms:
        print(f"Numero: {room['roomNumber']} | Andar: {room['floor']} | Tipo: {room['roomType']} | Estado: {room['status']} | Limpo?: {room['cleaned']} | Ocupante(s): {room['ocupants']} | Data de entrada: {room['checkInDate']} | Data de Saída {room['checkOutDate']}")
        print("-" * 60)


def listEmptyRooms():
    print("=" * 60)

    for room in rooms:
        if room['status'] == 'disponível':
            print(f"Numero: {room['roomNumber']} | Andar: {room['floor']} | Tipo: {room['roomType']} | Estado: {room['status']} | Limpo?: {room['cleaned']} | Ocupante(s): {room['ocupants']} | Data de entrada: {room['checkInDate']} | Data de Saída {room['checkOutDate']}")
            print("-" * 60)


def listOcupiedRooms():
    print("=" * 60)

    for room in rooms:
        if room['status'] == 'ocupado':
            print(f"Numero: {room['roomNumber']} | Andar: {room['floor']} | Tipo: {room['roomType']} | Estado: {room['status']} | Limpo?: {room['cleaned']} | Ocupante(s): {room['ocupants']} | Data de entrada: {room['checkInDate']} | Data de Saída {room['checkOutDate']}")
            print("-" * 60)


def listToCleanRooms():
    print("=" * 60)

    for room in rooms:
        if room['cleaned'] == 'Não':
            print(f"Numero: {room['roomNumber']} | Andar: {room['floor']} | Tipo: {room['roomType']} | Limpo?: {room['cleaned']}")
            print("-" * 60)

if __name__ == "__main__":
    populateRooms()
    mainMenu()