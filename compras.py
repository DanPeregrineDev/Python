Budget = float(input("Qual é o orçamento?: "))
WheightCanCarry = float(input("Quanto é o peso que pode levar?"))
CurrentlyCarrying = 0
while True:
    Price = float(input("Qual é o preço do produto?: "))
    Wheigh = float(input("Qual é o peso do produto?: "))
    CurrentlyCarrying = CurrentlyCarrying - Wheigh
    if CurrentlyCarrying < 0:
        print("Já não pode levar mais nada")
        break
    Budget = Budget - Price
    if Budget < 0:
        print("Já não tem dinheiro suficiente para comprar mais")
        break
    print(Budget)
    print(Wheigh)