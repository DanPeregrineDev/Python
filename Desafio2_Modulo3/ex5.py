def primeirosMultiplos(n, m):
    for i in range(1, n + 1):
        print(i * m)

def main():
    n = int(input("Valor de n: "))
    m = int(input("Valor de m: "))

    primeirosMultiplos(n, m)

if __name__ == "__main__":
    main()