import datetime

# Variables

CurrentYear = datetime.now().year
CurrentMonth = datetime.now().month
CurrentDay = datetime.now().day
BornInYear = int(input("Em que ano nasceu: "))
BornInMonth = int(input("Em que mês nasceu: "))
BornInDay = int(input("Em que dia nasceu: "))

# Validation

while BornInYear > CurrentYear:
    print("Ano em que nasceu está invalido")
    BornIn = int(input("Em que ano nasceu: "))

while BornInMonth > 12 or BornInMonth < 1:
    print("O mês está invalido")
    BornInMonth = int(input("Em que mês nasceu: "))

while BornInDay > 31 or BornInDay < 1:
    print("O dia está invalido")
    BornInDay = int(input("Em que dia nasceu: "))

# Process

YearsOld = CurrentYear - BornInYear
MonthsOld = CurrentMonth - BornInMonth
DaysOld = CurrentDay - BornInDay

if CurrentMonth < BornInMonth or CurrentMonth == BornInMonth or BornInDay > CurrentDay:
    YearsOld -= 1

# Output

print(f"Tem {YearsOld} anos, {MonthsOld} mêses e {DaysOld} dias")