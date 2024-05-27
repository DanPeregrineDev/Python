import pickle, termcolor, os
import utils, app

CONFIG_FILE = './data/config.dat'
ROOM_FILE = './data/rooms.dat'
STATS_FILE = './data/stats.dat'

def main():
    option = utils.showMenu("Configurações", ["Alterar quantidade de quartos", "Mudar preço dos quartos", "Alterar valor do desconto", "Mudar máximo de noites", "Apagar todos os dados", "Voltar"])

    if option == 1:
        changeRoomQuantity()
    elif option == 2:
        changeRoomPrices()
    elif option == 3:
        changeDiscountValue()
    elif option == 4:
        changeMaxNights()
    elif option == 5:
        removeAllData()
    elif option == 6:
        return


def changeRoomQuantity():
    with open(CONFIG_FILE, 'rb') as file:
        try:
            availableRooms = pickle.load(file)
            roomPrices = pickle.load(file)
            otherConfigurations = pickle.load(file)

        except:
            termcolor.cprint("ERRO ao ler ficheiro das configurações", "red")

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
            try:
                pickle.dump(availableRooms, file)
                pickle.dump(roomPrices, file)
                pickle.dump(otherConfigurations, file)

            except:
                termcolor.cprint("ERRO ao guardar alterações", "red")
                return

        termcolor.cprint("Quantidades atualizadas com sucesso", "light_green")

    # Update the rooms

    os.remove(ROOM_FILE)
    app.initialize()


def changeRoomPrices():
    with open(CONFIG_FILE, 'rb') as file:
        try:
            availableRooms = pickle.load(file)
            roomPrices = pickle.load(file)
            otherConfigurations = pickle.load(file)
        
        except:
            termcolor.cprint("ERRO ao ler ficheiro das configurações", "red")

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
            try:
                pickle.dump(availableRooms, file)
                pickle.dump(roomPrices, file)
                pickle.dump(otherConfigurations, file)

            except:
                termcolor.cprint("ERRO ao guardar alterações", "red")
                return

        termcolor.cprint("Preços atualizados com sucesso", "light_green")


def changeDiscountValue():
    with open(CONFIG_FILE, 'rb') as file:
        try:
            availableRooms = pickle.load(file)
            roomPrices = pickle.load(file)
            otherConfigurations = pickle.load(file)

        except:
            termcolor.cprint("ERRO ao carregar ficheiro das configurações", "red")

    print(f"Alterar valor do desconto | Atual {termcolor.colored(f"{otherConfigurations['discount']} %", "light_blue")}")

    newValue = utils.intInput("> ")

    if newValue == None:
        return

    while newValue > 100:
        termcolor.cprint("Desconto invalido", "red")
        newValue = utils.intInput("> ")

    otherConfigurations['discount'] = newValue

    with open(CONFIG_FILE, 'wb') as file:
        try:
            pickle.dump(availableRooms, file)
            pickle.dump(roomPrices, file)
            pickle.dump(otherConfigurations, file)

        except:
            termcolor.cprint("ERRO ao guardar alterações", "red")


def changeMaxNights():
    with open(CONFIG_FILE, 'rb') as file:
        try:
            availableRooms = pickle.load(file)
            roomPrices = pickle.load(file)
            otherConfigurations = pickle.load(file)

        except:
            termcolor.cprint("ERRO ao carregar ficheiro das configurações", "red")

    print(f"Alterar máximo de noites | Atual {termcolor.colored(f"{otherConfigurations['maxNights']}", "light_blue")} noites")

    newValue = utils.intInput("> ")

    if newValue == None:
        return

    otherConfigurations['maxNights'] = newValue

    with open(CONFIG_FILE, 'wb') as file:
        try:
            pickle.dump(availableRooms, file)
            pickle.dump(roomPrices, file)
            pickle.dump(otherConfigurations, file)

        except:
            termcolor.cprint("ERRO ao guardar alterações", "red")


def removeAllData():
    termcolor.cprint("Tem a certeza que deseja apagar todos os dados? (Y/N)", "red")

    option = utils.YesOrNo()

    if option == False:
        return
    
    elif option == True:
        os.remove(CONFIG_FILE)
        os.remove(ROOM_FILE)
        os.remove(STATS_FILE)

        print("Dados apagados com sucesso. Por favor volte a iniciar o programa")

        exit()