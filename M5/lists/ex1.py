lista = []

userInput = input("Escreva os numeros (ex: 1 2 3 4 5): ")
lista = userInput.split(" ")

for i in range(len(lista)):
    lista[i] = int(lista[i])

soma = 0

for i in lista:
    print(i)
    soma += i

media = soma / len(lista)

print("")
print(media)