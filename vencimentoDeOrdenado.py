import datetime

# Variables

SalaryPerDay = float(input("Quanto ganha por dia: "))
DateStarted = input("Quando é que comessou a trabalhar (ex: 2000-12-31): ")
DateEnded = input("Quando é que acabou de trabalhar (ex: 2000-12-31): ")

# Validation

while DateStarted > DateEnded:
    print("Dados invalidos")
    DateStarted = input("Quando é que comessou a trabalhar (ano-mes-dia): ")
    DateEnded = input("Quando é que acabou de trabalhar (ano-mes-dia): ")

while SalaryPerDay < 1:
    print("Salario muito baixo")
    SalaryPerDay = float(input("Quanto ganha por dia: "))

# Process

DateStarted_obj = datetime.datetime.strptime(DateStarted, "%Y-%m-%d")
DateEnded_obj = datetime.datetime.strptime(DateEnded, "%Y-%m-%d")

Diferenca = DateEnded_obj - DateStarted_obj

Result = Diferenca.days

QuantoRecebeu = Result * SalaryPerDay

# Output

print(f"Já recebeu {QuantoRecebeu}€")