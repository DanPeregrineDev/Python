# Funcao que le um inteiro do utiizador

def lerNumero(titulo):
    temp = input(titulo)

    while not temp.isnumeric():
        temp = input(titulo)

    return int(temp)

# Funcao para mostrar um menu

def mostrarMenu(titulo, opcoes):
    print("="*40)

    print(titulo)
    
    print("-"*40)
    
    for i in range(len(opcoes)):
        print(f"{i+1} - {opcoes[i]}")

    print("="*40)