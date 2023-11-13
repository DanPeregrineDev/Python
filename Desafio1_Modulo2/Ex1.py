# Daniel Madeira
# Exercicio 1

contar = 0
n = 1

print("Escreva 5 numeros superiores a 10 e inferiores a 100")

for i in range(0, 5):
        
        n = int(input(""))
        
        while n < 10 or n > 100:
            n = int(input("O numero que intruduziu está invalido, escreva novamente: "))

print("")

while contar < 5:

    if n > 10 or n < 100:
        contar = contar + 1
    print(contar)