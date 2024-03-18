lista = [1,2,3,4,5]

def rotate(lista, n):
    for i in range(n):
        pos = lista[0]
        lista.remove(pos)
        lista.insert(len(lista),pos)

rotate(lista, 2)
print(lista)