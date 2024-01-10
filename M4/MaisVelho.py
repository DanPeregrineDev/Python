"""
    Ler o nome e idade de 5 pessoas e mostrar o mais velho
"""

import numpy as np

N_PEOPLE = 5

Nomes = np.empty(5, 'U20')
Idades = np.empty(5, 'i')

currentPerson = 0

oldestPerson = Idades[0]

for i in range(N_PEOPLE):
    Nomes[currentPerson] = input(f"Nome da {i}º pessoa: ")
    Idades[currentPerson] = int(input(f"Idade da {i}º pessoa: "))

    if Idades[i] > oldestPerson:
        oldestPerson = 