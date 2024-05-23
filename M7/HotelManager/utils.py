# Utilities

def showMenu(title, options):
    """
        title - Title of the menu |
        options - An array of the options. Ex: ["Add", "Subtract", "Multiply"]

        Returns option
    """

    print("=" * 60)
    print(title)
    print("-" * 60)
    
    for option in range(len(options)):
        print(f"{option + 1} - {options[option]}")
    
    print("=" * 60)

    option = int(input("> "))

    while option < 1 or option > len(options):
        print("Opção é inválida")
        option = int(input(""))

    return option


def intInput(text, min = 1):
    userInput = input(text)

    if userInput == "":
        return None
    
    while userInput.isdigit() == False:
        print("Valor inválido")
        userInput = input(text)

    userInput = int(userInput)

    while userInput < min:
        print("Valor inválido")
        userInput = input(text)


    return int(userInput)