# Daniel Madeira
# Exercicio 4

UserInput = input("")

Vogais = 0

for i in UserInput:
    if i in "aeiouAEIOU":
        Vogais = Vogais + 1

print(Vogais)