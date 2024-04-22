import utils
import config
import app
import datetime

def checkInMenu():
    utils.showMenu("Check-In", ["1 Pessoa", "2 Pessoas", "3 Pessoas", "4 Pessoas", "Suite", "Voltar"])

    option = utils.askOption(6)

    if option == 1:
        assignRoom(1)
    if option == 2:
        assignRoom(2)
    if option == 3:
        assignRoom(3)
    if option == 4:
        assignRoom(4)
    if option == 5:
        assignRoom(5)
    if option == 6:
        app.mainMenu()


def assignRoom(roomType):
    """
        roomType - 1 = singleRoom | 2 = doubleRoom...etc | for suites use 5
        function will return room number
    """
    tenant = input("O nome inteiro do inquilino: ")
    noites = utils.askNumber("Quantas noites?: ")
    
    rooms = app.rooms

    for room in rooms:
        if room['roomType'] == 'singleRoom' and roomType == 1:
            room['status'] = 'ocupied'
            room['tenant'] = tenant
            return room['roomNumber']
        if room['roomType'] == 'doubleRoom' and roomType == 2:
            room['status'] = 'ocupied'
            room['tenant'] = tenant
            return room['roomNumber']
        if room['roomType'] == 'tripleRoom' and roomType == 3:
            room['status'] = 'ocupied'
            room['tenant'] = tenant
            return room['roomNumber']
        if room['roomType'] == 'quadripleRoom' and roomType == 4:
            room['status'] = 'ocupied'
            room['tenant'] = tenant
            return room['roomNumber']
        if room['roomType'] == 'suite' and roomType == 5:
            room['status'] = 'ocupied'
            room['tenant'] = tenant
            return room['roomNumber']
