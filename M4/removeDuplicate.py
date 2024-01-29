import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
fArr = np.zeros(10, 'i')

def remDuplicate(array):
    for i in range(len(array)):
        if i in array:
            continue
        fArr = array[i]

print(remDuplicate(arr))
