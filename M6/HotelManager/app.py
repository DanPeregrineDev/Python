import utils
import config

rooms = []

def mainMenu():
    populateRooms()

    while True:
        utils.showMenu("Menu", ["Check-in", "Check-out", "Configure", "Exit"])

        option = utils.askOption(4)

        if option == 1:
            pass
        if option == 2:
            pass
        if option == 3:
            config.configMenu()
        if option == 4:
            break


def populateRooms():
    # Calculate total of rooms

    totalRooms = 0
    for i in config.availableRooms.values():
        totalRooms = totalRooms + i

    # Number of floors is defined by the number of suites
    nFloors = config.availableRooms['suite']

    # Rooms per floor
    singleRoomPerFloor = config.availableRooms['singleRoom'] // nFloors
    doubleRoomPerFloor = config.availableRooms['doubleRoom'] // nFloors
    tripleRoomPerFloor = config.availableRooms['tripleRoom'] // nFloors
    quadripleRoomPerFloor = config.availableRooms['quadripleRoom'] // nFloors
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
                'roomType': roomType
            }

            rooms.append(room)

if __name__ == "__main__":
    mainMenu()