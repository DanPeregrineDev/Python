import numpy as np

# Vai ler 10 numeros do utilizador e mostra-os

numbers = np.empty(10)

for i in range(10):
    numbers[i] = int(input(f"Escreva o {i + 1} numero: "))

print(numbers)

# Mostrar valores por ordem inversa

for i in range(9, -1, -1):
    print(numbers[i])