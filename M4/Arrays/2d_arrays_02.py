import numpy
import random

FORMA = (2, 2)

n1 = numpy.zeros(FORMA, 'i')
n2 = numpy.zeros(FORMA, 'i')
n3 = numpy.zeros(FORMA, 'i')

def preenche(matriz):
    for l in range(matriz.shape[0]):
        for c in range(matriz.shape[1]):
            t = random.randint(1, 100)
            matriz[c] = t
    return matriz

n1 = preenche(n1)
n2 = preenche(n2)

def soma(n1, n2, n3):
    for l in range(n3.shape[0]):
        for c in range(n3.shape[1]):
            n3[l, c] = n1[l, c] + n2[l, c]
    return n3

n3 = soma(n1, n2, n3)
print(n3)