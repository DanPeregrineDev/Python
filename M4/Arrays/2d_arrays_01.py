import numpy
import random

arr = numpy.zeros((3, 3), 'i')

def preenche(matriz):
    for l in range(matriz.shape[0]):
        for c in range(matriz.shape[1]):
            t = random.randint(1, 100)
            matriz[c] = t
    return matriz

print(preenche(arr))