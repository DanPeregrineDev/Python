import numpy as np

ARRAY_MAX = 1000

nums = np.zeros(ARRAY_MAX, dtype='i')

for pos in range(ARRAY_MAX):
    nums[pos] = pos + 1

for i in range(ARRAY_MAX - 1, - 1, -1):
    print(nums[i])