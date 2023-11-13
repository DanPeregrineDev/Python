import random

print("Dificuldade 1 - 0 a 9")
print("Dificuldade 2 - 0 a 99")
print("Dificuldade 3 - 0 a 999")
Difficulty = int(input("Selecione a Dificuldade: "))

if Difficulty == 1:
    A = 10
elif Difficulty == 2:
    A = 100
elif Difficulty == 3:
    A = 1000

Lives = int(input("Quantas vidas quer ter (1 a 5): "))
UserInput = 0

# Validation

while Difficulty > 3 or Difficulty < 1:
    print("O numero da dificuldade está invalido")
    Difficulty = int(input("Selecione a Dificuldade (1 a 3): "))

while Lives > 5 or Lives < 1:
    if Lives > 5:
        print("Não pode ter mais que 5 vidas")
        Lives = int(input("Quantas vidas quer ter (1 a 5): "))
    elif Lives < 1:
        print("Não pode ter menos que 1 vida")
        Lives = int(input("Quantas vidas quer ter (1 a 5): "))

# Operation

RandomNumber = int(random.random() * A)

for i in range(Lives):

    if Lives == 1:
        print("Tem", Lives, "vida")
    elif Lives > 1:
        print("Tem", Lives, "vidas")

    if Difficulty == 1:
        UserInput = int(input("Tente adivinhar o numero (0 a 9): "))
    elif Difficulty == 2:
        UserInput = int(input("Tente adivinhar o numero (0 a 99): "))
    elif Difficulty == 3:
        UserInput = int(input("Tente adivinhar o numero (0 a 999): "))
    
    if UserInput != RandomNumber:
        print("Errou!")
        Lives = Lives - 1

        if UserInput > RandomNumber:
            if Lives > 1:
                print("Dica: O numero que escreveu é menor")
        elif UserInput < RandomNumber:
            if Lives > 1:
                print("Dica: O numero que escreveuu é maior")
    
    elif UserInput == RandomNumber:
        print("Parabens Asertou!")
        break

if Lives == 0:
    print("Ficou sem vidas :(")
    print("O numero era o:", RandomNumber)