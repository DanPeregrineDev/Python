def primo(n):
    if n == 2:
        print("É primo")
        return True
    for i in range(2, n):
        if n % i == 0:
            print("Não é primo")
            return False
        elif n % i != 0:
            print("É primo")
            return True

UserInput = int(input("Escreva um numero: "))
primo(UserInput)