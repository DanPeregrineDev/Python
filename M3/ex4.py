def tabuada(n):
    for i in range(1, 11):
        r = n * i
        print(f"{n} x {i} = {r}")


UserInput = int(input("Escreva o numero: "))
tabuada(UserInput)