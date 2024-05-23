import pickle, termcolor, os
import utils, app

CONFIG_FILE = './data/config.dat'
ROOM_FILE = './data/rooms.dat'

def main():
    option = utils.showMenu("Configurações", ["Alterar quantidade de quartos", "Mudar preço dos quartos", "Alterar valor do desconto", "Mudar máximo de noites", "Voltar"])

    if option == 1:
        changeRoomQuantity()
    elif option == 2:
        changeRoomPrices()
    elif option == 3:
        changeDiscountValue()
    elif option == 4:
        changeMaxNights()
    elif option == 5:
        return


def changeRoomQuantity():
    with open(CONFIG_FILE, 'rb') as file:
        for i in range(3):

            if i == 0:
                availableRooms = pickle.load(file)
            elif i == 1:
                roomPrices = pickle.load(file)
            elif i == 2:
                otherConfigurations = pickle.load(file)

    termcolor.cprint(f"Ao alterar os valores ira apagar todos os ocupantes. (Deixe vazio para não alterar)", "light_yellow")
    
    for room, ammount in availableRooms.items():

        print(f"Mudar quantidade de {termcolor.colored(f"'{room}'", "light_blue")} | quantidade atual: {termcolor.colored(f"{ammount}", "light_blue")}")

        newValue = utils.intInput("> ")

        if newValue == None:
            continue

        try:
            availableRooms[room] = newValue

        except Exception as error:
            termcolor.cprint(f"Ocurreu um erro ao atualizar quantidade: {error}", "red")

    # Update the Config file if there was no error

    if 'error' not in locals():
        with open(CONFIG_FILE, 'wb') as file:
            for i in range(3):
                
                if i == 0:
                    pickle.dump(availableRooms, file)
                elif i == 1:
                    pickle.dump(roomPrices, file)
                elif i == 2:
                    pickle.dump(otherConfigurations, file)

        termcolor.cprint("Quantidades atualizadas com sucesso", "light_green")

    # Update the rooms

    os.remove(ROOM_FILE)
    app.initialize()


def changeRoomPrices():
    with open(CONFIG_FILE, 'rb') as file:
        for i in range(3):
            
            if i == 0:
                availableRooms = pickle.load(file)
            elif i == 1:
                roomPrices = pickle.load(file)
            elif i == 2:
                otherConfigurations = pickle.load(file)

    for room, price in roomPrices.items():
        print(f"Mudar preço de {termcolor.colored(f"'{room}'", "light_blue")} | Valor atual: {termcolor.colored(f"{price}", "light_blue")}")

        newPrice = utils.intInput("> ")

        if newPrice == None:
            continue

        try:
            roomPrices[room] = newPrice

        except Exception as error:
            termcolor.cprint(f"Ocurreu um erro ao alterar o preço do quarto: {error}", "red")

    # Update config file if there was no error

    if 'error' not in locals():
        with open(CONFIG_FILE, 'wb') as file:
            for i in range(3):
                
                if i == 0:
                    pickle.dump(availableRooms, file)
                elif i == 1:
                    pickle.dump(roomPrices, file)
                elif i == 2:
                    pickle.dump(otherConfigurations, file)

        termcolor.cprint("Preços atualizados com sucesso", "light_green")


def changeDiscountValue():
    with open(CONFIG_FILE, 'rb') as file:
        for i in range(3):
                
            if i == 0:
                availableRooms = pickle.load(file)
            elif i == 1:
                roomPrices = pickle.load(file)
            elif i == 2:
                otherConfigurations = pickle.load(file)

    print(f"Alterar valor do desconto | Atual {termcolor.colored(f"{otherConfigurations['discount']} %", "light_blue")}")

    newValue = utils.intInput("> ")

    if newValue == None:
        return

    while newValue > 100:
        termcolor.cprint("Desconto invalido", "red")
        newValue = utils.intInput("> ")

    otherConfigurations['discount'] = newValue

    with open(CONFIG_FILE, 'wb') as file:
        for i in range(3):
                
            if i == 0:
                pickle.dump(availableRooms, file)
            elif i == 1:
                pickle.dump(roomPrices, file)
            elif i == 2:
                pickle.dump(otherConfigurations, file)


def changeMaxNights():
    with open(CONFIG_FILE, 'rb') as file:
        for i in range(3):
                
            if i == 0:
                availableRooms = pickle.load(file)
            elif i == 1:
                roomPrices = pickle.load(file)
            elif i == 2:
                otherConfigurations = pickle.load(file)

    print(f"Alterar máximo de noites | Atual {termcolor.colored(f"{otherConfigurations['maxNights']}", "light_blue")} noites")

    newValue = utils.intInput("> ")

    if newValue == None:
        return

    otherConfigurations['maxNights'] = newValue

    with open(CONFIG_FILE, 'wb') as file:
        for i in range(3):
                
            if i == 0:
                pickle.dump(availableRooms, file)
            elif i == 1:
                pickle.dump(roomPrices, file)
            elif i == 2:
                pickle.dump(otherConfigurations, file)