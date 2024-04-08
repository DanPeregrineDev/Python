# Funcao que le um inteiro do utiizador

def lerNumero(titulo):
    temp = input(titulo)

    while not temp.isnumeric():
        print("Escreva um numero")
        temp = input(titulo)

    return int(temp)

# Funcao para ler texto

def lerTexto(titulo, minChar):
    temp = input(titulo)

    while len(temp) < minChar:
        print(f"Minimo de {minChar} caracteres")
        temp = input(titulo)

    return temp

# Funcao para mostrar um menu

def mostrarMenu(titulo, opcoes):
    print("="*40)

    print(titulo)
    
    print("-"*40)
    
    for i in range(len(opcoes)):
        print(f"{i+1} - {opcoes[i]}")

    print("="*40)
