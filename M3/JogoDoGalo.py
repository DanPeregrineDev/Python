A1 = " "
A2 = " "
A3 = " "
B1 = " "
B2 = " "
B3 = " "
C1 = " "
C2 = " "
C3 = " "

EndGame = False

def PrintTable(a1, a2, a3, b1, b2, b3, c1, c2, c3):
    print(f"{a1}|{a2}|{a3}")
    print(f"{b1}|{b2}|{b3}")
    print(f"{c1}|{c2}|{c3}")

def game():
    global A1, A2, A3, B1, B2, B3, C1, C2, C3
    PrintTable(A1, A2, A3, B1, B2, B3, C1, C2, C3)
    pInput = input("Escreva as cordenadas de onde quer marcar: ").upper()
    while pInput != "A1" and pInput != "A2" and pInput != "A3" and pInput != "B1" and pInput != "B2" and pInput != "B3" and pInput != "C1" and pInput != "C2" and pInput != "C3":
        print("Cordenada invalida!")
        pInput = input("Escreva as cordenadas de onde quer marcar: ").upper()
    if pInput == "A1":
        A1 = "X"
    elif pInput == "A2":
        A2 = "X"
    elif pInput == "A3":
        A3 = "X"
    elif pInput == "B1":
        B1 = "X"
    elif pInput == "B2":
        B2 = "X"
    elif pInput == "B3":
        B3 = "X"
    elif pInput == "C1":
        C1 = "X"
    elif pInput == "C2":
        C2 = "X"
    elif pInput == "C3":
        C3 = "X"
    PrintTable(A1, A2, A3, B1, B2, B3, C1, C2, C3)

def main():
    global EndGame
    while not EndGame:
        game()

if __name__ == "__main__":
    main()