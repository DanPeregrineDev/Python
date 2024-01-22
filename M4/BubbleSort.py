import numpy as np

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                t = arr[j]
                arr[j]=arr[j + 1]
                arr[j + 1]=t

vetor = np.array([1, 24, 6, 1, 77, 56])
bubble_sort(vetor)
print(vetor)