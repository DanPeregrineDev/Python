# Variables

CurrentMonth = int(input("Que numero do mês é hoje: "))
CurrentDay = int(input("Que dia é hoje: "))
MonthDays = 0
RemaningDays = 0

# Validation

while CurrentDay > 31 or CurrentDay < 1:
    print("O dia é invalido")
    CurrentDay = int(input("Que dia é hoje: "))

while CurrentMonth > 12 or CurrentMonth < 1:
    print("O mês é invalido")
    CurrentMonth = int(input("Que numero do mês é hoje: "))

while CurrentDay > 29 and CurrentMonth == 2:
    print("O dia é invalido porque 'Fevereiro' não tem mais de 29 dias.")
    CurrentDay = int(input("Que dia é hoje: "))

# Process

if CurrentMonth in (1, 3, 5, 7, 8, 10, 12):
    MonthDays = 31
    RemaningDays = MonthDays - CurrentDay

if CurrentMonth in (4, 6, 9, 11):
    MonthDays = 30
    RemaningDays = MonthDays - CurrentDay

if CurrentMonth == 2:
    MonthDays = 29
    RemaningDays = MonthDays - CurrentDay

# Output

print(f"Faltam {RemaningDays} dias para acabar o mês")