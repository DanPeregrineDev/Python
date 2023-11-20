UserInput = int(input("Escreva um numero: "))

# Operation

for i in range(UserInput, 0, -1):
    if UserInput % i == 0:
        print(i)