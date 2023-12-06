def AISelection():
    import random
    Selection = random.randint(1, 3)
    return Selection

def Result(UserInput):
    AI = AISelection()
    User = UserInput

    # If user is rock
    if User == 1 and AI == 1:
        return "Pedra - EMPATE!"
    if User == 1 and AI == 2:
        return "Papel - PERDESTE!"
    if User == 1 and AI == 3:
        return "Tesoura - GANHASTE!"

    # If user is Paper
    if User == 2 and AI == 1:
        return "Pedra - GANHASTE!"
    if User == 2 and AI == 2:
        return "Papel - EMPATE!"
    if User == 2 and AI == 3:
        return "Tesoura - PERDESTE!"

    # If user is Scisours
    if User == 3 and AI == 1:
        return "Pedra - PERDESTE!"
    if User == 3 and AI == 2:
        return "Papel - GANHASTE!"
    if User == 3 and AI == 3:
        return "Tesoura - EMPATE!"

    # AI Error

    if AI > 3 or AI < 1:
        return "AI ERROR"

def main():
    while True:
        print("Pedra, Papel ou Tesoura")
        print("1 - Pedra")
        print("2 - Papel")
        print("3 - Tesoura")
        Selection = int(input(""))
        print(Result(Selection))

if __name__ == "__main__":
    main()