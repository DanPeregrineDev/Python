UserInput = int(input("Escreva um numero: "))

def tabuada():
    global UserInput
    for i in range(1, 11):
        r = i * UserInput
        print(f"{UserInput} x {i} = {r}")
    UserInput = 0

tabuada()