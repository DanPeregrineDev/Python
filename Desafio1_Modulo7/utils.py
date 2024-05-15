def showmenu(title, options):
    """
        Title - Menu's title
        Options - A list of options ex: ["Option1", "Option2"]

        Function returns the option
    """

    print("=" * 60)
    print(title)
    print("-" * 60)
    
    for option in range(len(options)):
        print(f"{option + 1} - {options[option]}")
    
    print("=" * 60)

    option = int(input("> "))

    while option < 1 or option > len(options):
        print("Invalid option")
        option = int(input(""))

    return option