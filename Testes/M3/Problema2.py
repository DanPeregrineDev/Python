def signo(day, month):

    # -----VALIDATION-----

    if day < 1 or day > 31 or month < 1 or month > 12:
        return "Data incorreta"
    
    # -----Aquário-----

    if day >= 21 and month == 1 or day <= 19 and month == 2:
        return "Aquário"

    # -----Peixes-----

    if day >= 20 and month == 2 or day <= 20 and month == 3:
        return "Peixes"

    # -----Áries-----

    if day >= 21 and month == 3 or day <= 20 and month == 4:
        return "Áries"
    
    # -----Touro-----

    if day >= 21 and month == 4 or day <= 20 and month == 5:
        return "Touro"
    
    # -----Gémeos-----

    if day >= 21 and month == 5 or day <= 20 and month == 6:
        return "Gémeos"
    
    # -----Câncer-----

    if day >= 21 and month == 6 or day <= 21 and month == 7:
        return "Câncer"
    
    # -----Leão-----

    if day >= 22 and month == 7 or day <= 22 and month == 8:
        return "Leão"
    
    # -----Virgem-----

    if day >= 23 and month == 8 or day <= 22 and month == 9:
        return "Virgem"
    
    # -----Libra-----

    if day >= 23 and month == 9 or day <= 22 and month == 10:
        return "Libra"
    
    # -----Escorpião-----

    if day >= 23 and month == 10 or day <= 21 and month == 11:
        return "Escorpião"
    
    # -----Sagitário-----

    if day >= 22 and month == 11 or day <= 21 and month == 12:
        return "Sagitário"
    
    # -----Capricórnio-----

    if day >= 22 and month == 12 or day <= 20 and month == 1:
        return "Capricórnio"

def main():
    day = int(input("Dia: "))
    month = int(input("Mês: "))
    print(signo(day, month))

if __name__ == "__main__":
    main()
