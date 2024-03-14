import random

lista = []

for i in range(10):
    palavra = ""
    for i in range(random.randint(3, 10)):
        palavra += chr(random.randint(97, 122))
    lista.append(palavra)

print(lista)