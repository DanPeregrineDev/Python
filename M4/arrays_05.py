import numpy as np

VECTOR_MAX = 10

numbers = np.empty(VECTOR_MAX, 'f')

for i in range(VECTOR_MAX):
    numbers[i] = float(input(f"Type a number for the position {i + 1}: "))

biggest = numbers[0]
pos_biggest = 0

for pos in range(VECTOR_MAX):
    if numbers[pos] > biggest:
        biggest = numbers[pos]
        pos_biggest = pos

print(f"The biggest is {biggest} with the position of {pos_biggest + 1}")

largests = np.empty(VECTOR_MAX, 'f')
n = 0

for pos in range(VECTOR_MAX):
    if numbers[pos] == biggest:
        largests[n] = pos
        n = n + 1

for i in range(n):
    print(f"Position {largests[i]}")