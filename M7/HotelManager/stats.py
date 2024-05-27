import pickle, termcolor

ROOMS_FILE = './data/rooms.dat'
STATS_FILE = './data/stats.dat'

def main():
    occupancyRate()
    mostPopularRoomType()

    # Load stats file

    with open(STATS_FILE, 'rb') as file:
        try:
            stats = pickle.load(file)

        except:
            termcolor.cprint("ERRO ao carregar ficheiro das estatísticas", "red")

    print("=" * 60)
    print("Estatísticas")
    print("=" * 60)

    print(f"Numero total de quartos: {termcolor.colored(f"{stats['totalNumberOfRooms']}", "light_blue")}")
    print(f"Lucro: {termcolor.colored(f"{stats['totalProfit']} €", "light_green")}")
    print(f"Taxa de ocupação: {termcolor.colored(f"{stats['occupancyRate'] :.2f} %", "light_blue")}")
    print(f"Tipo de quarto mais popular: {termcolor.colored(f"{stats['mostPopularRoomType']}", "light_blue")}")

    print("=" * 60)
    print("Enter para voltar")

    t = input()

    return


def occupancyRate():
    # Load rooms file

    with open(ROOMS_FILE, 'rb') as file:
        try:
            rooms = pickle.load(file)

        except:
            termcolor.cprint("ERRO ao carregar ficheiro dos quartos", "red")

    # Load stats file

    with open(STATS_FILE, 'rb') as file:
        try:
            stats = pickle.load(file)

        except:
            termcolor.cprint("ERRO ao carregar ficheiro das estatísticas", "red")

    totalRooms = len(rooms)

    t = 0
    for room in rooms:
        if room['status'] == 'ocupado':
            t += 1

    occupiedRooms = t

    occupancyRate = (occupiedRooms / totalRooms) * 100

    stats['occupancyRate'] = occupancyRate

    # Save changes to stats file

    with open(STATS_FILE, 'wb') as file:
        try:
            pickle.dump(stats, file)

        except:
            termcolor.cprint("ERRO ao guardar alterações", "red")


def mostPopularRoomType():
    # Load rooms file

    with open(ROOMS_FILE, 'rb') as file:
        try:
            rooms = pickle.load(file)

        except:
            termcolor.cprint("ERRO ao carregar ficheiro dos quartos", "red")

    # Load stats file

    with open(STATS_FILE, 'rb') as file:
        try:
            stats = pickle.load(file)

        except:
            termcolor.cprint("ERRO ao carregar ficheiro das estatísticas", "red")

    roomTypesCount = {
        'singleRoom': 0,
        'doubleRoom': 0,
        'tripleRoom': 0,
        'quadripleRoom': 0,
        'suite': 0
    }

    for room in rooms:
        if room['status'] == 'ocupado':
            roomTypesCount[room['roomType']] += 1

    mostPopularRoomType = None
    t = 0

    for roomType, count in roomTypesCount.items():
        if count > t:
            t = count
            mostPopularRoomType = roomType

    stats['mostPopularRoomType'] = mostPopularRoomType

    # Save changes

    with open(STATS_FILE, 'wb') as file:
        try:
            pickle.dump(stats, file)

        except:
            termcolor.cprint("ERRO ao guardar alterações", "red")