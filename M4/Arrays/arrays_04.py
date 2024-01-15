import numpy as np

VECTOR_MAX = 10

numbers = np.empty(VECTOR_MAX, dtype="f") # f - Floats

for i  in range(VECTOR_MAX):
    numbers[i] = int(input("Type a number: "))

biggestPosition = 0
biggest = numbers[0]

for p in range(VECTOR_MAX):
    if numbers[p] > biggest:
        biggest = numbers[p]
        biggestPosition = p

print(f"Biggest number: {biggest} in position {biggestPosition + 1}")

smallestPosition = 0
smallest = numbers[0]

for p in range(VECTOR_MAX):
    if numbers[p] < smallest:
        smallest = numbers[p]
        smallestPosition = p

print(f"Smallest number: {smallest} in position {smallestPosition + 1}")
