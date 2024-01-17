import numpy as np

MAX_ARRAY = 5

array = np.array([1, 2, 3, 4, 5])
tempArray = np.empty(5, dtype='i')

index2 = len(array)-1
for i in range(len(array)):
    array[i] = array[index2]
    index2 = index2 - 1

array = tempArray
print(array)