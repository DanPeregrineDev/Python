import pickle, termcolor, datetime
import utils, list

CONFIG_FILE = './data/config.dat'
ROOMS_FILE = './data/rooms.dat'

def main():
    print("Quartos ocupados:")
    list.listOcupiedRooms()

    roomNumber = utils.intInput("Numero do quarto (Deixe vazio para cancelar): ")

    if roomNumber == None:
        return
    
    with open(CONFIG_FILE, 'rb') as configFile:
        for i in range(3):
            if i == 1:
                roomPrices = pickle.load(configFile)
            elif i == 2:
                otherConfigurations = pickle.load(configFile)
    
    with open(ROOMS_FILE, 'rb') as roomsFile:
        rooms = pickle.load(roomsFile)
    
    extraDate = 0

    for room in rooms:
        if room['roomNumber'] == roomNumber:
            checkOutDate_str = room['checkOutDate'].split(" / ")[1]
            checkOutDate = datetime.datetime.strptime(checkOutDate_str, '%d/%m/%Y')

            if checkOutDate < datetime.datetime.now():
                extraDate = int((datetime.datetime.now() - checkOutDate).days)
                termcolor.cprint("CheckOut atrasado. Sem direito a desconto", "red")

            roomType = room['roomType']

            if extraDate >= 1:
                print(f"Valor a pagar: {roomPrices[roomType] * (room['nights'] + extraDate)}€")

            print(f"Valor a pagar: {roomPrices[roomType] * room['nights'] - (otherConfigurations['discount'] / 100) * roomPrices[roomType] * room['nights']}€")

            if otherConfigurations['discount'] > 0 and extraDate == 0:
                termcolor.cprint(f"Desconto de {otherConfigurations['discount']}% aplicado", 'blue')
            
            room['status'] = 'disponível'
            room['cleaned'] = 'Não'
            room['occupants'] = None
            room['nights'] = None
            room['checkInDate'] = None
            room['checkOutDate'] = None

            termcolor.cprint("CheckOut concluido", "green")

    # Save changes

    with open(ROOMS_FILE, 'wb') as file:
        pickle.dump(rooms, file)
