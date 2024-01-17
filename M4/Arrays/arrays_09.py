import numpy as np

array_1 = np.array([1, 2, 3, 4])
array_2 = np.array([5, 6, 7, 8])
array_3 = np.empty(8, 'i')

for pos in range(len(array_1)):
    array_3[pos] = array_1[pos]
    array_3[pos + 4] = array_2[pos]

print(array_3)