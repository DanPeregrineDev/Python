import numpy as np

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid  # Target found
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1  # Target not found

# Example usage
arr = np.array([1, 3, 5, 7, 9, 11, 15, 18])
target = 5
result = binary_search(arr, target)

print(f"Index of {target}: {result}")