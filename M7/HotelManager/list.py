import pickle, termcolor
import utils

ROOMS_FILE = './data/rooms.dat'

def main():
    option = utils.showMenu("Listar", ["Todos os quartos", "Listar quartos vazios", "Listar quartos ocupados", "Listar quartos para limpar", "Voltar"])

    if option == 1:
        listAllRooms()
    elif option == 2:
        listEmptyRooms()
    elif option == 3:
        listOcupiedRooms()
    elif option == 4:
        listToCleanRooms()
    elif option == 5:
        return


def listAllRooms():
    with open(ROOMS_FILE, 'rb') as roomsFile:
        try:
            rooms = pickle.load(roomsFile)
        
        except:
            termcolor.cprint("ERRO ao ler ficheiro dos quartos", "red")

    print("=" * 60)

    for room in rooms:
        print(f"Numero: {room['roomNumber']} | Andar: {room['floor']} | Tipo: {room['roomType']} | Estado: {room['status']} | Limpo?: {room['cleaned']} | Ocupante(s): {room['occupants']} \nNoites: {room['nights']} | Data de entrada: {room['checkInDate']} | Data de Saída: {room['checkOutDate']}")
        print("-" * 60)


def listEmptyRooms():
    with open(ROOMS_FILE, 'rb') as roomsFile:
        try:
            rooms = pickle.load(roomsFile)
        
        except:
            termcolor.cprint("ERRO ao ler ficheiro dos quartos", "red")

    print("=" * 60)

    for room in rooms:
        if room['status'] == 'disponível':
            print(f"Numero: {room['roomNumber']} | Andar: {room['floor']} | Tipo: {room['roomType']} | Estado: {room['status']} | Limpo?: {room['cleaned']} | Ocupante(s): {room['occupants']} \nNoites: {room['nights']} | Data de entrada: {room['checkInDate']} | Data de Saída: {room['checkOutDate']}")
            print("-" * 60)


def listOcupiedRooms():
    with open(ROOMS_FILE, 'rb') as roomsFile:
        try:
            rooms = pickle.load(roomsFile)
        
        except:
            termcolor.cprint("ERRO ao ler ficheiro dos quartos", "red")

    print("=" * 60)

    for room in rooms:
        if room['status'] == 'ocupado':
            print(f"Numero: {room['roomNumber']} | Andar: {room['floor']} | Tipo: {room['roomType']} | Estado: {room['status']} | Limpo?: {room['cleaned']} | Ocupante(s): {room['occupants']} \nNoites: {room['nights']} | Data de entrada: {room['checkInDate']} | Data de Saída: {room['checkOutDate']}")
            print("-" * 60)


def listToCleanRooms():
    with open(ROOMS_FILE, 'rb') as roomsFile:
        try:
            rooms = pickle.load(roomsFile)
        
        except:
            termcolor.cprint("ERRO ao ler ficheiro dos quartos", "red")

    print("=" * 60)

    for room in rooms:
        if room['cleaned'] == 'Não':
            print(f"Numero: {room['roomNumber']} | Andar: {room['floor']} | Tipo: {room['roomType']} | Limpo?: {room['cleaned']}")
            print("-" * 60)