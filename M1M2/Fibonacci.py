# Variables

UserInput = int(input("Escreva um numero: "))

N1 = 0
N2 = 1

# Process and Output

for i in range(UserInput):
    N3 = N1 + N2
    print(N3)
    N1 = N2
    N2 = N3