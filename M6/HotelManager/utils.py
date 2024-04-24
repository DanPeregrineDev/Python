# Utilities

def showMenu(title, options):
    """
        title - Title of the menu |
        options - An array of the options. Ex: ["Add", "Subtract", "Multiply"]
    """

    print("=" * 60)

    print(title)

    print("-" * 60)

    for option in range(len(options)):
        print(f"{option + 1} - {options[option]}")

    print("=" * 60)


def askOption(nOptions = 1000):
    """nOptions - Number of options"""
    while True:

        userInput = input("")

        if not userInput.isdigit():
            print("Opção inválida")
            continue

        userInput = int(userInput)

        while userInput < 0 or userInput > nOptions:
            userInput = int(input(f"Opção inválida. Deve ser entre 0 e {nOptions}: "))

        return userInput


def askNumber(text = "", negative = False, maxNumber = None):
    """
        text - input's text |
        negative - if the number can be negative |
        maxNumber - max number value
    """

    userInput = input(text)

    if userInput == "":
        return None
    
    userInput = int(userInput)

    while userInput < 0 and negative is False:
        print("Não pode ser menor que 0")
        userInput = int(input(text))
    
    while maxNumber != None and userInput > maxNumber:
        print(f"Não pode ser maior que {maxNumber}")
        userInput = int(input(text))


    return userInput