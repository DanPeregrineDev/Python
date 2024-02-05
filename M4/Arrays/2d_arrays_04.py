import numpy

def diagonal(n):

    FORMA = (n, n)

    matriz = numpy.zeros(FORMA, 'i')

    for i in range(matriz.shape[0]):
        matriz[i, i] = 1

    return matriz

print(diagonal(30))