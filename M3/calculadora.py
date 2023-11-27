# Functions

def Soma(P1, P2):
    R = P1 + P2

def Subtracao(P1, P2):
    R = P1 - P2

def Multiplicacao(P1, P2):
    R = P1 * P2

def Divisao(P1, P2):
    R = P1 / P2

def Menu():
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Fechar")
    Selecao = int(input("Selecione a opção: "))
    return Selecao

# Process, Validation and Output

while True:
    Selecao = Menu()

    # Validation

    while Selecao < 0 or Selecao > 4:
        print("Seleção inválida")
        Selecao = int(input("Selecione a opção: "))

    # Process and Output

    if Selecao == 1:
        V1 = int(input("Primeiro valor: "))
        V2 = int(input("Segundo valor: "))
        print("")
        print(f"O resultado é: {Soma(V1, V2)}")
        print("")

    elif Selecao == 2:
        V1 = int(input("Primeiro valor: "))
        V2 = int(input("Segundo valor: "))
        print("")
        print(f"O resultado é {Subtracao(V1, V2)}")
        print("")

    elif Selecao == 3:
        V1 = int(input("Primeiro valor: "))
        V2 = int(input("Segundo valor: "))
        print("")
        print(f"O resultado é {Multiplicacao(V1, V2)}")
        print("")

    elif Selecao == 4:
        V1 = int(input("Primeiro valor: "))
        V2 = int(input("Segundo valor: "))
        print("")
        print(f"O resultado é {Divisao(V1, V2)}")
        print("")

    elif Selecao == 0:
        print("A terminar...")
        break