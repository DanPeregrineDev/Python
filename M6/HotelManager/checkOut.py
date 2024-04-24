import utils
import app
import datetime

def checkOutMenu(rooms):
    print("=" * 60)
    
    roomNumber = utils.askNumber("Número do quarto: ")

    for room in rooms:
        if room['roomNumber'] == roomNumber:
            room['status'] = 'disponível'
            room['cleaned'] = 'Não'
            room['ocupants'] = None
            room['checkInDate'] = None
            room['checkOutDate'] = None