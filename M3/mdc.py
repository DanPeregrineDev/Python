def mdc(n1, n2):
    menor = 0
    if n1 < n2:
        menor = n1
    elif n2 < n1:
        menor = n2
    for i in range(menor, 0, -1):
        if n1 % i and n2 % i == 0:
            return i
    print("Não existe minimo divisor comum")

def main():
    N1 = int(input("Escreva um numero: "))
    N2 = int(input("Escreva outro numero: "))
    print(mdc(N1, N2))

if __name__ == "__main__":
    main()