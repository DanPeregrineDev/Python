def showMenu(title, options):
    """
        title = "Menu"
        options = ["Option1", "Option2"]

        function also asks for a option and returs it.
    """

    print("=" * 60)
    print(title)
    print("-" * 60)

    for option in range(len(options)):
        print(f"{option + 1} - {options[option]}")

    print("=" * 60)

    option = int(input(""))

    while option < 1 or option > len(options):
        print("Opção inválida")
        option = int(input(""))

    return option


#aasdef