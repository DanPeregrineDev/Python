import numpy as np

def readData():
    nums = np.empty(5, 'i')

    for i in range(len(nums)):
        nums[i] = int(input("N: "))

    return nums

array = readData()

print(array)