def Soma(P1, P2):
    R = P1 + P2
    print(f"O resultado é {R}")

def Subtracao(P1, P2):
    R = P1 - P2
    print(f"O resultado é {R}")

def Multiplicacao(P1, P2):
    R = P1 * P2
    print(f"O resultado é {R}")

def Divisao(P1, P2):
    R = P1 / P2
    print(f"O resultado é {R}")

print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
print("0 - Fechar")

# Variables

Selecao = int(input("Selecione a opção: "))

# Validation

while Selecao < 1 or Selecao > 4:
    print("Seleção inválida")
    Selecao = int(input("Selecione a opção: "))

while Selecao != 0:
    if Selecao == 1:
        V1 = int(input("Primeiro valor: "))
        V2 = int(input("Segundo valor: "))
        Soma(V1, V2)
    elif Selecao == 2:
        V1 = int(input("Primeiro valor: "))
        V2 = int(input("Segundo valor: "))
        Subtracao(V1, V2)
    elif Selecao == 3:
        V1 = int(input("Primeiro valor: "))
        V2 = int(input("Segundo valor: "))
        Multiplicacao(V1, V2)
    elif Selecao == 4:
        V1 = int(input("Primeiro valor: "))
        V2 = int(input("Segundo valor: "))
        Divisao(V1, V2)
print("A terminar...")