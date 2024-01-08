def multiplosInferioresA100(n):
    for i in range(1, 100):
            if n * i < 100:
                print(n * i)
            else:
                break

n = input(int("Escreva o numero: "))
multiplosInferioresA100(n)