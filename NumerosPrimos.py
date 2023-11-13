UserInput = int(input("Escreva um numero: "))

# Input Validation

if UserInput < 0:
    print("Valor invalido")

# Operation

if UserInput == 2:
    print("É primo")
    exit()

np = 0

for i in range(2, UserInput):
    if UserInput % i == 0:
        np = np + 1
        break

if np >= 1:
    print("Não é primo")

if np == 0:
    print("É primo")