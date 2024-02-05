import numpy

original = numpy.array([1, 2], [3, 4], [5, 6])

FORMA = (original.shape[1], original.shape[0])

transposta = numpy.empty(FORMA)

for l in range(original.shape[0]):
    for c in range(original.shape[1]):
        transposta[c, l] = original[l, c]

print(transposta)