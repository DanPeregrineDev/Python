import numpy as np

VECTOR_MAX = 10

numbers = np.empty(VECTOR_MAX, dtype="f") # f - Floats

for i  in range(VECTOR_MAX):
    numbers[i] = int(input("Type a number: "))