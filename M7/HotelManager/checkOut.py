import pickle, termcolor, datetime
import utils, list

CONFIG_FILE = './data/config.dat'
ROOMS_FILE = './data/rooms.dat'
STATS_FILE = './data/stats.dat'

def main():
    print("Quartos ocupados:")
    list.listOcupiedRooms()

    roomNumber = utils.intInput("Numero do quarto (Deixe vazio para cancelar): ")

    if roomNumber == None:
        return
    
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

    # Load stats file

    with open(STATS_FILE, 'rb') as statsFile:
        try:
            stats = pickle.load(statsFile)

        except:
            termcolor.cprint("ERRO ao carregar ficheiro das estatísticas", "red")
    
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

            stats['totalProfit'] += roomPrices[roomType] * room['nights'] - (otherConfigurations['discount'] / 100) * roomPrices[roomType] * room['nights']

            if otherConfigurations['discount'] > 0 and extraDate == 0:
                termcolor.cprint(f"Desconto de {otherConfigurations['discount']}% aplicado", 'blue')
            
            stats['totalNumberOfCustomers'] -= len(room['occupants'])
            
            room['status'] = 'disponível'
            room['cleaned'] = 'Não'
            room['occupants'] = None
            room['nights'] = None
            room['checkInDate'] = None
            room['checkOutDate'] = None

            termcolor.cprint("CheckOut concluido", "green")

    # Save changes to rooms file

    with open(ROOMS_FILE, 'wb') as file:
        try:
            pickle.dump(rooms, file)
        
        except:
            termcolor.cprint("ERRO ao guardar alterações", "red")
            return # so it doesn't break the stats

    # Save changes to stats file

    with open(STATS_FILE, 'wb') as file:
        try:
            pickle.dump(stats, file)
        
        except:
            termcolor.cprint("ERRO ao guardar alterações", "red")
