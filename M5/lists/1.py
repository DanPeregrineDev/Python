lista = [1, 2, 3, 4, "Joaquim"]

print(lista)

lista2 = lista

lista2[1] = 100

print(lista, lista2)

#copy

lista3 = lista[:]
lista3[1] = 99

print(lista3)