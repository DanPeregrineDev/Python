import numpy
import random

arr = numpy.zeroes((3, 3), 'i')

for l in range(2):
    for c in range(2):
        t = random.randint(1, 100)
        arr[c] = t

print(arr)