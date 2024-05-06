with open('ex1.txt', 'w', encoding='UTF-8') as file:
    for i in range(10):
        name = input(f"{i + 1}º nome: ")

        if i == 9:
            file.write(f"{name}")
            break

        file.write(f"{name}\n")