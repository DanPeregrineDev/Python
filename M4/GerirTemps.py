"""
    Precisamos de um programa para gerir as temperaturas médias mensais de um ano.
    O programa dever ler as 12 temperaturas e depois mostrar o mês mais quente e mais frio.
    Opcional: calcular e mostrar a temperatura média do ano e quantos meses tiveram temperatura superior à média
"""

import numpy as np

MAX_ARRAY = 12 # 12 months

temperatures = np.empty(MAX_ARRAY, dtype='f')
months = np.array(["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"])

for pos in range(MAX_ARRAY):
    temperatures[pos] = int(input(f"Escreva a temperatura mês de {months[pos]}: "))

# Hottest
    
hottest = 0

for pos in range(MAX_ARRAY):
    if temperatures[pos] > hottest:
        hottest = temperatures[pos]

print(f"A temperatura mais quente é de {hottest} no mês de {months[pos]}")

# Coldest
        
coldest = 12

for pos in range(MAX_ARRAY):
    if temperatures[pos] < coldest:
        coldest = temperatures[pos]
        pos_month = pos

print(f"A temperatura mais fria é de {coldest} no mês de {months[pos]}")

# Median

Sum = 0

for pos in range(MAX_ARRAY):
    Sum = Sum + temperatures[pos]

print(f"A temperatura média do ano é {Sum / MAX_ARRAY}")