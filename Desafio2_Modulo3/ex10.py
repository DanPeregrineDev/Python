def fatorial(n):
    if n < 1:
        print("Erro: o parametro 'n' não pode ser negativo ou nulo")
        return
    r = 1
    for i in range(1, n + 1):
        r *= i
    print(r)

def main():
    for i in range(1, 11):
        if fatorial(i) != None:
            print(fatorial(i))

if __name__ == "__main__":
    main()