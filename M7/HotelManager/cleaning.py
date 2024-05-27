import pickle, termcolor
import utils, list

ROOMS_FILE = './data/rooms.dat'

def main():
    print("=" * 60)
    print("Quartos por limpar:")

    list.listToCleanRooms()

    markAsCleaned = utils.intInput("Numero do quarto para marcar como limpo (deixe vazio para cancelar): ")

    if markAsCleaned == None:
        return
    
    with open(ROOMS_FILE, 'rb') as file:
        try:
            rooms = pickle.load(file)

        except:
            termcolor.cprint("ERRO ao carregar ficheiro dos quartos", "red")

    for room in rooms:
        if room['roomNumber'] == markAsCleaned:
            room['cleaned'] = 'Sim'

            termcolor.cprint("Limpo com sucesso!", 'light_green')

    # Save changes

    with open(ROOMS_FILE, 'wb') as file:
        try:
            pickle.dump(rooms, file)

        except:
            termcolor.cprint("ERRO ao guardar alterações", "red")