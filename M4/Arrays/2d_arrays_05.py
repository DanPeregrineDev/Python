import numpy

def replaceNegatives(arr):

    for l in range(arr.shape[0]):
        for c in range(arr.shape[1]):
            if arr[l, c] < 0:
                arr[l, c] = 0

    return arr

m = numpy.array([[1, -2, 4], [4, -11, -9], [7, -32, -3]])

print(replaceNegatives(m))