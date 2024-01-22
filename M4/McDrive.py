import numpy as np

def Menu():
    print("1 - Entrada")
    print("2 - Saida")
    print("3 - Estado da Fila")
    print("4 - Terminar")
    print("")
    selection = int(input(""))
    
    while selection > 4 or selection < 1:
        print("Seleção invalida!")

        print("1 - Entrada")
        print("2 - Saida")
        print("3 - Estado da Fila")
        print("4 - Terminar")
        print("")
        selection = int(input(""))

    return selection

def Entrada(fila, nElementos):
    if isFull(fila, nElementos) == True:
        print("A fila esta cheia")

    matricula = input("Qual a matricula?: ")
    fila[nElementos] = matricula
    nElementos += 1
    return nElementos

def Saida(fila, nElementos):
    if nElementos == 0:
        print("A fila esta vazia!")
        return nElementos
    elementoRetirado = fila[0]
    print(f"Sai o {elementoRetirado}")
    for i in range(nElementos - 2):
        fila[i] = fila[i + 1]
    nElementos -= 1

    return nElementos

def MostrarEstado(fila, nElementos):
    if nElementos == 0:
        print("Fila vazia")
        return
    for i in range(nElementos):
        print(fila[i])

def isFull(fila, nElementos):
    if len(fila) == nElementos:
        return True
    return False

def main():
    Fila = np.empty(10, 'U8')
    nElementos = 0
    
    while True:
        selection = Menu()
        if selection == 1:
            nElementos = Entrada(Fila, nElementos)
        elif selection == 2:
            nElementos = Saida(Fila, nElementos)
        elif selection == 3:
            MostrarEstado(Fila, nElementos)

if __name__ == "__main__":
    main()