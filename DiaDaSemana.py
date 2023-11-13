import datetime

# Variables

Year = int(input("Ano em que nasceu: "))
Month = int(input("Mês em que nasceu: "))
Day = int(input("Dia em que nasceu: "))

date = datetime.date(Year, Month, Day)

# Output

print(date.weekday())
print(date.strftime("%A"))