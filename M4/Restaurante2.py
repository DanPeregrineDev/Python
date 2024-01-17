import numpy as np

print("Quantas mesas?")
quantasMesas = int(input(""))

mesas = np.empty(quantasMesas, 'i')

# Config mesas

for i in range(len(mesas)):
    lugares = int(input(f"Quantos lugares tem a mesa {i + 1}?: "))
    mesas[i] = lugares

while True:
    print("")
    print("1 - Entrada de clientes")
    print("2 - Saida de clientes")
    print("3 - Terminar progama")
    selection = int(input("Selecione a opção: "))

     # -----VALIDATION-----

    if selection < 1 or selection > 3:
        print("")
        print("Opção invalida!")
        print("")
        print("1 - Entrada de clientes")
        print("2 - Saida de clientes")
        print("3 - Terminar progama")
        selection = int(input("Selecione a opção: "))

    # -----1-----

    if selection == 1:
        print("")
        print(f"Lugares disponiveis: {mesas}")
        mesa = int(input("Selecione a mesa: ")) - 1

        while mesa > quantasMesas:
            print(f"A mesa {mesa} não existe")
            print(f"Lugares disponiveis: {mesas}")
            mesa = int(input("Selecione a mesa: ")) - 1

        print("Quantas pessoas entraram?")
        entradas = int(input(""))
        
        while entradas > mesas[mesa]:
            print("Não existe lugares suficientes")
            print("")
            print(f"Mesas: {mesas}")
            mesa = int(input("Selecione a mesa: ")) - 1
            print("Quantas pessoas entraram?")
            entradas = int(input(""))
        
        mesas[mesa] -= entradas

    # -----2-----
        
    if selection == 2:
        print("")
        print(f"Lugares disponiveis: {mesas}")
        mesa = int(input("Selecione a mesa: ")) - 1

        while mesa > quantasMesas:
            print(f"A mesa {mesa} não existe")
            print(f"Lugares disponiveis: {mesas}")
            mesa = int(input("Selecione a mesa: ")) - 1

        print("Quantas pessoas entraram?")
        saidas = int(input(""))

        while saidas > mesas[mesa]:
            print("Impossível sair mais pessoas do que lugares existem")
            print("")
            print("Quantas pessoas sairam?")
            saidas = int(input(""))

        mesas[mesa] += saidas

    # -----3-----
        
    if selection == 3:
        break