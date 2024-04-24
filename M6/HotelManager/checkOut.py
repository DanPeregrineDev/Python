import utils
import app
import config

def checkOutMenu(rooms):
    print("=" * 60)
    
    roomNumber = utils.askNumber("Número do quarto (deixe vazio para cancelar): ")

    if roomNumber == None:
        app.mainMenu()

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

