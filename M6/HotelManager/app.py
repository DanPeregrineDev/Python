import utils
import checkIn
import checkOut

# installed package required
import termcolor

availableRooms = {'singleRoom': 20, 'doubleRoom': 40, 'tripleRoom': 20, 'quadripleRoom': 15, 'suite': 5}
hotelPrices = {'singleRoom': 100, 'doubleRoom': 150, 'tripleRoom': 200, 'quadripleRoom': 250, 'suite': 400} # Per night
maxNights = 15 # 15 default
discount = 0 # 0%

rooms = []

def mainMenu():

    while True:
        utils.showMenu("Menu", ["Check-in", "Check-out", "Listar Quartos", "Limpezas", "Configurar", "Exit"])

        option = utils.askOption(6)

        if option == 1:
            checkIn.checkInMenu(rooms, maxNights)
        if option == 2:
            listOcupiedRooms()
            checkOut.checkOutMenu(rooms, discount)
        if option == 3:
            listMenu()
        if option == 4:
            limpezas()
        if option == 5:
            configMenu()
        if option == 6:
            return


def populateRooms():
    # Calculate total of rooms

    totalRooms = 0
    for i in availableRooms.values():
        totalRooms = totalRooms + i

    # Number of floors is defined by the number of suites
    nFloors = availableRooms['suite']

    # Rooms per floor
    singleRoomPerFloor = availableRooms['singleRoom'] / nFloors
    doubleRoomPerFloor = availableRooms['doubleRoom'] / nFloors
    tripleRoomPerFloor = availableRooms['tripleRoom'] / nFloors
    quadripleRoomPerFloor = availableRooms['quadripleRoom'] / nFloors
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
                'nights': None,
                'checkInDate': None,
                'checkOutDate': None
            }

            rooms.append(room)


# LIST MENU


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
        print(f"Numero: {room['roomNumber']} | Andar: {room['floor']} | Tipo: {room['roomType']} | Estado: {room['status']} | Limpo?: {room['cleaned']} | Ocupante(s): {room['ocupants']} \nNoites: {room['nights']} | Data de entrada: {room['checkInDate']} | Data de Saída: {room['checkOutDate']}")
        print("-" * 60)


def listEmptyRooms():
    print("=" * 60)

    for room in rooms:
        if room['status'] == 'disponível':
            print(f"Numero: {room['roomNumber']} | Andar: {room['floor']} | Tipo: {room['roomType']} | Estado: {room['status']} | Limpo?: {room['cleaned']} | Ocupante(s): {room['ocupants']} \nNoites: {room['nights']} | Data de entrada: {room['checkInDate']} | Data de Saída: {room['checkOutDate']}")
            print("-" * 60)


def listOcupiedRooms():
    print("=" * 60)

    for room in rooms:
        if room['status'] == 'ocupado':
            print(f"Numero: {room['roomNumber']} | Andar: {room['floor']} | Tipo: {room['roomType']} | Estado: {room['status']} | Limpo?: {room['cleaned']} | Ocupante(s): {room['ocupants']} \nNoites: {room['nights']} | Data de entrada: {room['checkInDate']} | Data de Saída: {room['checkOutDate']}")
            print("-" * 60)


def listToCleanRooms():
    print("=" * 60)

    for room in rooms:
        if room['cleaned'] == 'Não':
            print(f"Numero: {room['roomNumber']} | Andar: {room['floor']} | Tipo: {room['roomType']} | Limpo?: {room['cleaned']}")
            print("-" * 60)


def limpezas():
    print("=" * 60)
    print("Quartos para limpar:")

    listToCleanRooms()

    markAsCleaned = utils.askNumber("Numero do quarto para marcar como limpo (deixe vazio para cancelar): ")

    if markAsCleaned == None:
        mainMenu()

    for room in rooms:
        if room['roomNumber'] == markAsCleaned:
            room['cleaned'] = 'Sim'

            print("Limpo com sucesso!")


# CONFIG MENU


def configMenu():
    while True:
        utils.showMenu("Configuration Menu", ["Alterar quantidade de quartos", "Mudar Preços", "Alterar valor do desconto", "Mudar máximo de noites", "Voltar"])

        option = utils.askOption(5)

        if option == 1:
            changeRoomQuantity()
        if option == 2:
            changePrices()
        if option == 3:
            changeDiscout()
        if option == 4:
            changeMaxNights()
        if option == 5:
            mainMenu()


def changeRoomQuantity():
    rooms.clear()

    for room, ammount in availableRooms.items():
        print(f"Mudar quantidade de {room} | quantidade atual: {ammount}")

        newQuantity = utils.askNumber()

        if newQuantity == None:
            continue

        availableRooms[room] = newQuantity

    print("Valores autalizados: ")
    print(availableRooms)

    populateRooms()


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
        return

    discount = newDiscount

    termcolor.cprint("Desconto alterado com sucesso", "green")

    return

def changeMaxNights():
    global maxNights

    print(f"Mudar máximo de noites | Atual: {maxNights}")

    newMaxNights = utils.askNumber()

    if newMaxNights is None:
        return

    maxNights = newMaxNights

    termcolor.cprint("Máximo de noites alterado com sucesso", "green")

    return


if __name__ == "__main__":
    populateRooms()
    mainMenu()