QClasse = int(input("Em que classe está? : "))
QuantasHoras = int(input("Quantas horas trabalhou? : "))

# Validation

if QClasse < 1 or QClasse > 2:
    print("A classe está invalida!")
    exit()
if QuantasHoras < 0:
    print("O numero de horas é invalido!")
    exit()

# Calculation

if QClasse == 1:
    PHoraExtra = 120
    if QuantasHoras > 40:
        HorasExtra = QuantasHoras - 40
        print("O seu salario é:", 4000 + (PHoraExtra * HorasExtra)) 
    else:
        print("O seu salario é:", QuantasHoras * 100)
if QClasse == 2:
    PHoraExtra = 240
    if QuantasHoras > 40:
        HorasExtra = QuantasHoras - 40
        print("O seu salario é:", 9600 + (HorasExtra * HorasExtra))
    else:
        print("O seu salario é:", QuantasHoras * 200)

input("Clike no ENTER para fechar o programa ")
exit()