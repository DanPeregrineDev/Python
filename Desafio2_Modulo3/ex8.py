def multiploEntre2Numeros(n1, n2):
    if n1 % n2 == 0:
        return True
    else:
        return False

def main():
    n1 = int(input("Escreva o 1º numero: "))
    n2 = int(input("Escreva o 2º numero: "))
    
    n = multiploEntre2Numeros(n1, n2)

    if n == True:
        print("São múltiplos um do outro")
    else:
        print("Não são múltiplos um do outro")

if __name__ == "__main__":
    main()