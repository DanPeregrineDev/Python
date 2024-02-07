carros = ("ford", "ferrari", "bmw", "vw", "ford")
print(carros.count("ford"))

def lerCarros():
    carro1 = input("Carro: ")
    carro2 = input("Carro: ")
    carro3 = input("Carro: ")

    meu_tuplo = (carro1, carro2, carro3)
    return meu_tuplo

print(lerCarros())