def PrintTable(A1, A2, A3, B1, B2, B3, C1, C2, C3):
    print(f"{A1}|{A2}|{A3}")
    print(f"{B1}|{B2}|{B3}")
    print(f"{C1}|{C2}|{C3}")

def PlayerInput(isPlayerTurn):
    if isPlayerTurn:
        pInput = input("Escreva as cordenadas de onde quer marcar: ").upper()
        while pInput != "A1" or pInput != "A2" or pInput != "A3" or pInput != "B1" or pInput != "B2" or pInput != "B3" or pInput != "C1" or pInput != "C2" or pInput != "C3":
            print("Cordenada invalida!")
            pInput = input("Escreva as cordenadas de onde quer marcar: ").upper()

def main():
    PrintTable(" ", " ", " ", " ", " ", " ", " ", " ", " ")
    PlayerInput(True)

if __name__ == "__main__":
    main()