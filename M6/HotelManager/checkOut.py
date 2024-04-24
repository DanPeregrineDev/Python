import utils
import config

def checkOutMenu(rooms):
    print("=" * 60)
    
    roomNumber = utils.askNumber("Número do quarto: ")

    for room in rooms:
        if room['roomNumber'] == roomNumber:
            roomType = room['roomType']
            print(f"Valor a pagar: {config.hotelPrices[f'{roomType}'] * room['nights']}€")
            
            room['status'] = 'disponível'
            room['cleaned'] = 'Não'
            room['ocupants'] = None
            room['nights'] = None
            room['checkInDate'] = None
            room['checkOutDate'] = None

