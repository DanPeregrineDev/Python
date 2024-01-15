import numpy as np

ARRAY_MAX = 5

array1 = np.empty(ARRAY_MAX, dtype='i')
array2 = np.empty(ARRAY_MAX, dtype='i')

results = np.empty(ARRAY_MAX, dtype='i')

def readData(nums):
    for pos in range(len(nums)):
        nums[ pos ] = int(input("Escreva um numero: "))

def calculateData(nums):
    add = 0
    for x in nums:
        add = add + 1
    return add

readData(array1)
print("Agora para o vetor 2")
readData(array2)

result = calculateData(array1) + calculateData(array2)

print(results)