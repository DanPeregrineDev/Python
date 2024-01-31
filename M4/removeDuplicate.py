import numpy as np

def remDuplicate(nums):
    temp = np.zeros(len(nums))
    pos = 0

    for i in range(len(nums)):
        if nums[i] in temp:
            continue
        else:
            temp[pos] = nums[i]
            pos += 1

    return temp

nums_repetidos = np.array([1, 2, 2, 3, 3, 3, 4])
print(remDuplicate(nums_repetidos))