import utils
import app
import datetime

# installed package required
import termcolor

def checkOutMenu(rooms, discount):
    print("=" * 60)
    
    roomNumber = utils.askNumber("Número do quarto (deixe vazio para cancelar): ")

    if roomNumber is None:
        return

    extraDate = 0

    for room in rooms:
        if room['roomNumber'] == roomNumber:
            checkOutDate_str = room['checkOutDate'].split(" / ")[1]
            checkOutDate = datetime.datetime.strptime(checkOutDate_str, '%d/%m/%Y')
            if checkOutDate < datetime.datetime.now():
                extraDate = int((datetime.datetime.now() - checkOutDate).days)
                termcolor.cprint("CheckOut atrasado. Sem direito a desconto", "red")

            roomType = room['roomType']

            if extraDate >= 1:
                print(f"Valor a pagar: {app.hotelPrices[roomType] * (room['nights'] + extraDate)}€")

            print(f"Valor a pagar: {app.hotelPrices[roomType] * room['nights'] - (discount / 100) * app.hotelPrices[roomType] * room['nights']}€")

            if discount > 0 and extraDate == 0:
                termcolor.cprint(f"Desconto de {discount}% aplicado", 'blue')
            
            room['status'] = 'disponível'
            room['cleaned'] = 'Não'
            room['occupants'] = None
            room['nights'] = None
            room['checkInDate'] = None
            room['checkOutDate'] = None

            termcolor.cprint("CheckOut sucedido", "green")
