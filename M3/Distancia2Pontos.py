import math


def distancia(x1, y1, x2, y2):
    C1 = x2 - x1
    C2 = y2 - y1
    r = math.sqrt(C1 ** 2 + C2 ** 2)
    return r

def main():
    X1 = int(input("Escreva a cordenada X1: "))
    Y1 = int(input("Escreva a cordenada Y1: "))
    X2 = int(input("Escreva a cordenada X2: "))
    Y2 = int(input("Escreva a cordenada Y2: "))
    print(distancia(X1, Y1, X2, Y2))

if __name__ == "__main__":
    main()