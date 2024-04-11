
def lerNumero(titulo):
    # Funcao que le um inteiro do utiizador
    
    temp = input(titulo)

    while not temp.isnumeric():
        print("Escreva um numero")
        temp = input(titulo)

    return int(temp)


def lerTexto(titulo, minChar=None):
    # Funcao para ler texto
    
    temp = input(titulo)

    while minChar is not None and len(temp) < minChar:
        print(f"Minimo de {minChar} caracteres")
        temp = input(titulo)

    return temp


def mostrarMenu(titulo, opcoes):
    # Funcao para mostrar um menu
    
    print("="*40)

    print(titulo)
    
    print("-"*40)
    
    for i in range(len(opcoes)):
        print(f"{i+1} - {opcoes[i]}")

    print("="*40)


def validarEmail(email):
    # Validar email
    
    arroba = 0
    pontos = 0

    for i in email:
        if i == "@":
            arroba += 1
        if i == ".":
            pontos += 1
    
    if arroba == 1 and pontos > 1:
        return True
    return False


def lerEmail(texto):
    #Ler email
    
    temp = input(texto)

    arroba = 0
    pontos = 0

    for i in temp:
        if i == "@":
            arroba += 1
        if i == ".":
            pontos += 1

    if arroba == 1 and pontos > 0:
        return temp
    print("Email Invalido")
    lerEmail(texto)