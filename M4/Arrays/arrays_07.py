"""
    Criar 2 arrays com 5 pos q o utiliz vai dar e mostrar a soma
"""

import numpy as np

ARRAY_MAX = 5

array1 = np.empty(ARRAY_MAX, dtype='i')
array2 = np.empty(ARRAY_MAX, dtype='i')
results = np.empty(ARRAY_MAX, dtype='i')

for i in range(ARRAY_MAX):
    array1[i] = int(input("Escreva um numero: "))

print("Agora para o vetor 2")

for i in range(ARRAY_MAX):
    array2[i] = int(input("Escreva um numero: "))

for i in range(ARRAY_MAX):
    results[i] = array1[i] + array2[i]

print(results)