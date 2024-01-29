"""
Crie um programa para sortear os números do euro milhões.
Devemos sortear 5 números entre 1 e 50 e mais 2 números entre 1 e 12.
Os números sorteados não se podem repetir.
Devemos mostrar os números por ordem crescente.
"""

import numpy as np
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                t = arr[j]
                arr[j]=arr[j + 1]
                arr[j + 1]=t
    return arr

numeros = np.zeros(5, 'i')
estrelas = np.zeros(2, 'i')

i = 0
while i < 5:
    x = random.randint(1, 50)

    if x in numeros:
        continue
    numeros[i] = x
    i += 1

i = 0
while i < 2:
    x = random.randint(1, 12)

    if x in estrelas:
        continue
    estrelas[i] = x
    i += 1

bubble_sort(numeros)
bubble_sort(estrelas)
print(numeros, estrelas)