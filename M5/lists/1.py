lista = [1, 2, 3, 4, "Joaquim"]

print(lista)

lista2 = lista

lista2[1] = 100

print(lista, lista2)

#copy

lista3 = lista[:]
lista3[1] = 99

print(lista3)

# list all elements

for i in lista:
    print(i)

# add elements
    
lista.append(555)
lista.insert(0, 88) # pos 0

# union lists

lista.extend(lista3)

print(lista)