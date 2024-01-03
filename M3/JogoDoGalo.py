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
    print("")
    print(f"{a1}|{a2}|{a3}")
    print(f"{b1}|{b2}|{b3}")
    print(f"{c1}|{c2}|{c3}")
    print("")

def Player1():
    global A1, A2, A3, B1, B2, B3, C1, C2, C3
    pInput = input("Jogador 1! Escreva as cordenadas de onde quer marcar: ").upper()
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
    return True

def Player2():
    global A1, A2, A3, B1, B2, B3, C1, C2, C3
    pInput = input("Jogador 2! Escreva as cordenadas de onde quer marcar: ").upper()
    while pInput != "A1" and pInput != "A2" and pInput != "A3" and pInput != "B1" and pInput != "B2" and pInput != "B3" and pInput != "C1" and pInput != "C2" and pInput != "C3":
        print("Cordenada invalida!")
        pInput = input("Escreva as cordenadas de onde quer marcar: ").upper()
    if pInput == "A1":
        A1 = "O"
    elif pInput == "A2":
        A2 = "O"
    elif pInput == "A3":
        A3 = "O"
    elif pInput == "B1":
        B1 = "O"
    elif pInput == "B2":
        B2 = "O"
    elif pInput == "B3":
        B3 = "O"
    elif pInput == "C1":
        C1 = "O"
    elif pInput == "C2":
        C2 = "O"
    elif pInput == "C3":
        C3 = "O"
    PrintTable(A1, A2, A3, B1, B2, B3, C1, C2, C3)
    return True

def DidUserWon():
    global A1, A2, A3, B1, B2, B3, C1, C2, C3

    # X
    if A1 == "X" and A2 == "X" and A3 == "X":
        return True
    if B1 == "X" and B2 == "X" and B3 == "X":
        return True
    if C1 == "X" and C2 == "X" and C3 == "X":
        return True
    if A1 == "X" and B1 == "X" and C1 == "X":
        return True
    if A2 == "X" and B2 == "X" and C2 == "X":
        return True
    if A3 == "X" and B3 == "X" and C3 == "X":
        return True
    if A1 == "X" and B2 == "X" and C3 == "X":
        return True
    if A3 == "X" and B2 == "X" and C1 == "X":
        return True

    # O
    if A1 == "O" and A2 == "O" and A3 == "O":
        return True
    if B1 == "O" and B2 == "O" and B3 == "O":
        return True
    if C1 == "O" and C2 == "O" and C3 == "O":
        return True
    if A1 == "O" and B1 == "O" and C1 == "O":
        return True
    if A2 == "O" and B2 == "O" and C2 == "O":
        return True
    if A3 == "O" and B3 == "O" and C3 == "O":
        return True
    if A1 == "O" and B2 == "O" and C3 == "O":
        return True
    if A3 == "O" and B2 == "O" and C1 == "O":
        return True

def main():
    global EndGame
    while not EndGame:
        p1 = Player1()
        if p1 and not EndGame:
            Player2()
        didUserWon = DidUserWon()
        if didUserWon:
            print("Parabens! Ganhaste")
            exit()

if __name__ == "__main__":
    main()