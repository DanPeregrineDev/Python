APagarPorDia = 10
APagarPorKM = 0.60 # 0,60€

QuantosDiasPassaram = int(input("Quantos Dias Já pagou: "))
QuantosKMAndou = float(input("Quantos KMs Andou: "))

# Validate Input
if QuantosDiasPassaram < 1:
    print("É preciso ter passado mais de 1 dia!")
    exit() # End program
if QuantosKMAndou < 0:
    print("Valor apresentado é invalido!")
    exit() # End program

# Calculations

TotalAPagar = (APagarPorDia * QuantosDiasPassaram) + (APagarPorKM * QuantosKMAndou)
iva = TotalAPagar * 0.23
ValorFinal = TotalAPagar + iva

print("O valor a pagar é", ValorFinal)